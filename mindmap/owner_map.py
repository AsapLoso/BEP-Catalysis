"""Read-only adapter for explicitly selected owner-map snapshots and references."""

from __future__ import annotations

import hashlib
import posixpath
import re
import subprocess
from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import unquote
from typing import Any, Dict, Optional, Tuple, Union

import yaml

from mindmap.schema import OwnerMapDocument, ReferenceMapDocument

MAX_READER_BYTES = 5 * 1024 * 1024
MAX_FIGURE_BYTES = 10 * 1024 * 1024
READER_TEXT_SUFFIXES = {".md", ".markdown", ".txt", ".yaml", ".yml", ".json"}
READER_VISIBILITIES = {"node_detail", "reader", "visible"}
READER_IMAGE_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
}
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def _read_source(
    *,
    path: Optional[Union[str, Path]],
    git_ref: Optional[str],
    git_path: Optional[str],
    git_root: Union[str, Path],
) -> Tuple[bytes, Dict[str, Any]]:
    if path is not None:
        if git_ref is not None or git_path is not None:
            raise ValueError("Choose a local path or a local Git ref and path, not both.")
        selected_path = Path(path).expanduser().resolve(strict=True)
        if not selected_path.is_file():
            raise ValueError(f"Snapshot path is not a file: {selected_path}")
        content = selected_path.read_bytes()
        return content, {
            "kind": "local_snapshot",
            "label": f"Local snapshot · {selected_path.name}",
            "snapshot_id": hashlib.sha256(content).hexdigest(),
            "location": selected_path.name,
        }

    if git_ref is None and git_path is None:
        raise ValueError("An explicit snapshot path or Git ref/path is required.")
    if not git_ref or not git_path:
        raise ValueError("A Git snapshot requires both --map-ref and --map-git-path.")
    if git_ref.startswith("-") or any(char in git_ref for char in "\r\n:"):
        raise ValueError("Git ref must be a branch, tag, or commit identifier.")

    normalized_git_path = git_path.replace("\\", "/")
    relative = PurePosixPath(normalized_git_path)
    windows_path = PureWindowsPath(normalized_git_path)
    if (
        relative.is_absolute()
        or windows_path.is_absolute()
        or windows_path.drive
        or not relative.parts
        or ".." in relative.parts
        or "\0" in normalized_git_path
    ):
        raise ValueError("Git snapshot path must be a repository-relative file path.")

    root = Path(git_root).expanduser().resolve(strict=True)
    resolved = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--verify", f"{git_ref}^{{commit}}"],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if resolved.returncode != 0:
        raise ValueError(f"Git ref is not available locally: {git_ref}. Fetch it explicitly first.")
    commit = resolved.stdout.strip()
    shown = subprocess.run(
        ["git", "-C", str(root), "show", f"{commit}:{relative.as_posix()}"],
        check=False,
        capture_output=True,
    )
    if shown.returncode != 0:
        raise ValueError(f"Could not read {relative.as_posix()} from local ref {git_ref}.")

    content = shown.stdout
    return content, {
        "kind": "local_git_ref_snapshot",
        "label": f"Local Git ref snapshot · {git_ref}",
        "snapshot_id": commit,
        "location": f"{git_ref}:{relative.as_posix()}",
        "commit": commit,
    }


def _parse_document(content: bytes, label: str) -> Dict[str, Any]:
    try:
        document = yaml.safe_load(content.decode("utf-8"))
    except (UnicodeDecodeError, yaml.YAMLError) as exc:
        raise ValueError(f"Could not parse {label} as UTF-8 YAML/JSON: {exc}") from exc
    if not isinstance(document, dict):
        raise ValueError(f"{label} must contain an object with named fields.")
    return document


def load_owner_map_snapshot(
    *,
    path: Optional[Union[str, Path]] = None,
    git_ref: Optional[str] = None,
    git_path: Optional[str] = None,
    git_root: Union[str, Path] = ".",
    reference_path: Optional[Union[str, Path]] = None,
    reference_git_ref: Optional[str] = None,
    reference_git_path: Optional[str] = None,
) -> Dict[str, Any]:
    """Validate and return read-only snapshot data for the existing viewer."""
    owner_bytes, owner_source = _read_source(
        path=path,
        git_ref=git_ref,
        git_path=git_path,
        git_root=git_root,
    )
    owner_raw = _parse_document(owner_bytes, "owner map")
    owner = OwnerMapDocument.model_validate(owner_raw)

    reference: Dict[str, Any] = {}
    reference_source: Optional[Dict[str, Any]] = None
    reference_data_sources: list[Dict[str, Any]] = []
    if reference_path is not None or reference_git_ref is not None or reference_git_path is not None:
        reference_bytes, reference_source = _read_source(
            path=reference_path,
            git_ref=reference_git_ref,
            git_path=reference_git_path,
            git_root=git_root,
        )
        reference_raw = _parse_document(reference_bytes, "reference map")
        base = reference_raw.get("base", {})
        snapshot = base.get("migrated_snapshot", base) if isinstance(base, dict) else {}
        if isinstance(snapshot, dict) and not reference_raw.get("nodes") and (snapshot.get("nodes_path") or snapshot.get("sources_path")):
            if not snapshot.get("nodes_path") or not snapshot.get("sources_path"):
                raise ValueError("Reference-map manifest must name both nodes_path and sources_path.")

            def read_manifest_file(key: str, label: str) -> Tuple[bytes, Dict[str, Any]]:
                if snapshot.get("read_from_working_tree") is True and reference_source["kind"] == "local_snapshot":
                    relative_path = _normalize_asset_path(snapshot[key])
                    root = Path(git_root).expanduser().resolve(strict=True)
                    selected = (root / Path(*relative_path.parts)).resolve(strict=True)
                    if not _path_is_within(selected, root) or not selected.is_file():
                        raise ValueError(f"Reference-map {label} must stay inside the selected repository root.")
                    return _read_source(path=selected, git_ref=None, git_path=None, git_root=root)
                pinned_ref = snapshot.get("commit") or snapshot.get("ref") or snapshot.get("branch")
                if not pinned_ref:
                    raise ValueError("Reference-map manifest must pin its component files to a local Git ref.")
                return _read_source(
                    path=None,
                    git_ref=str(pinned_ref),
                    git_path=str(snapshot[key]),
                    git_root=git_root,
                )

            nodes_bytes, nodes_source = read_manifest_file("nodes_path", "nodes file")
            sources_bytes, sources_source = read_manifest_file("sources_path", "sources file")
            reference_nodes = _parse_document(nodes_bytes, "AI reference nodes")
            reference_sources = _parse_document(sources_bytes, "AI reference sources")
            reference_raw["nodes"] = reference_nodes.get("nodes", [])
            reference_raw["sources"] = reference_sources.get("sources", [])
            reference_data_sources.extend([nodes_source, sources_source])
            if snapshot.get("uncertainties_path"):
                uncertainty_bytes, uncertainty_source = read_manifest_file("uncertainties_path", "uncertainties file")
                uncertainty_document = _parse_document(uncertainty_bytes, "AI reference uncertainties")
                reference_raw["uncertainties"] = uncertainty_document.get("uncertainties", [])
                reference_data_sources.append(uncertainty_source)
        reference_model = ReferenceMapDocument.model_validate(reference_raw)
        reference = reference_model.model_dump(mode="json", exclude_unset=True)

    return {
        "nodes": [node.model_dump(mode="json", exclude_unset=True) for node in owner.nodes],
        "owner_map": owner.model_dump(mode="json", exclude_unset=True),
        "reference_map": reference,
        "source": {
            **owner_source,
            "role": "owner_personal_map",
            "status": "snapshot",
            "authoritative": False,
            "read_only": True,
        },
        "reference_source": reference_source,
        "reference_data_sources": reference_data_sources,
        "access": "Read-only local snapshot. No GitHub fetch or map write was performed.",
    }


def _file_reference_dict(value: Any, label: str) -> Dict[str, Any]:
    if isinstance(value, str):
        return {"path": value}
    if isinstance(value, dict):
        return value
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json", exclude_unset=True)
    raise ValueError(f"{label} must be a relative path or a file-reference object.")


def _normalize_asset_path(value: Any, *, allow_parent: bool = False) -> PurePosixPath:
    if isinstance(value, (PurePosixPath, PureWindowsPath)):
        raw_path = value.as_posix()
    elif isinstance(value, str):
        raw_path = value
    else:
        raw_path = ""
    normalized = raw_path.strip().replace("\\", "/")
    windows_path = PureWindowsPath(normalized)
    path = PurePosixPath(normalized)
    if not normalized or "\0" in normalized:
        raise ValueError("Reader file path must be a non-empty relative path.")
    if windows_path.is_absolute() or windows_path.drive or path.is_absolute():
        raise ValueError("Reader file paths must be repository-relative, not absolute.")
    if not allow_parent and ".." in path.parts:
        raise ValueError("Reader file paths cannot traverse outside their selected root.")
    if not path.parts or path.as_posix() in ("", "."):
        raise ValueError("Reader file path cannot be empty.")
    return path


def _path_is_within(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _load_owner_node(
    *,
    node_id: str,
    path: Optional[Union[str, Path]],
    git_ref: Optional[str],
    git_path: Optional[str],
    git_root: Union[str, Path],
) -> Tuple[Any, Dict[str, Any]]:
    owner_bytes, source = _read_source(
        path=path,
        git_ref=git_ref,
        git_path=git_path,
        git_root=git_root,
    )
    owner = OwnerMapDocument.model_validate(_parse_document(owner_bytes, "owner map"))
    node = next((item for item in owner.nodes if item.id == node_id), None)
    if node is None:
        raise FileNotFoundError(f"Owner-map node not found: {node_id}")
    return node, source


def _read_local_asset(
    relative_path: PurePosixPath,
    *,
    map_path: Union[str, Path],
    git_root: Union[str, Path],
    base_file: Optional[Union[str, Path]] = None,
    max_bytes: int,
) -> Tuple[bytes, Path]:
    owner_file = Path(map_path).expanduser().resolve(strict=True)
    map_directory = owner_file.parent
    snapshot_directory = map_directory.parent
    selected_root = Path(git_root).expanduser().resolve(strict=True)
    asset_candidates = (snapshot_directory, map_directory, selected_root)
    allowed_roots = (map_directory, selected_root)
    candidates = []
    if base_file is not None:
        candidates.append(Path(base_file).parent / Path(*relative_path.parts))
    candidates.extend(root / Path(*relative_path.parts) for root in asset_candidates)

    seen = set()
    for candidate in candidates:
        try:
            resolved = candidate.resolve(strict=True)
        except OSError:
            continue
        if resolved in seen:
            continue
        seen.add(resolved)
        if not any(_path_is_within(resolved, root) for root in allowed_roots) or not resolved.is_file():
            continue
        data = resolved.read_bytes()
        if len(data) > max_bytes:
            raise ValueError("Reader file exceeds the configured size limit.")
        return data, resolved
    raise FileNotFoundError(f"Reader file not found in the selected snapshot: {relative_path.as_posix()}")


def _git_asset_candidates(
    relative_path: PurePosixPath,
    *,
    git_path: Optional[str],
    base_file: Optional[str] = None,
) -> list[str]:
    candidates = []
    if base_file is not None:
        candidates.append(posixpath.join(posixpath.dirname(base_file), relative_path.as_posix()))
    candidates.append(relative_path.as_posix())
    if git_path:
        candidates.append(posixpath.join(posixpath.dirname(git_path), relative_path.as_posix()))

    normalized = []
    for candidate in candidates:
        candidate = posixpath.normpath(candidate)
        if candidate in ("", ".", "..") or candidate.startswith("../") or candidate.startswith("/"):
            continue
        if candidate not in normalized:
            normalized.append(candidate)
    return normalized


def _read_git_asset(
    relative_path: PurePosixPath,
    *,
    commit: str,
    git_path: Optional[str],
    git_root: Union[str, Path],
    base_file: Optional[str] = None,
    max_bytes: int,
) -> Tuple[bytes, str]:
    root = Path(git_root).expanduser().resolve(strict=True)
    for repo_path in _git_asset_candidates(relative_path, git_path=git_path, base_file=base_file):
        result = subprocess.run(
            ["git", "-C", str(root), "show", f"{commit}:{repo_path}"],
            check=False,
            capture_output=True,
            timeout=10,
        )
        if result.returncode != 0:
            continue
        if len(result.stdout) > max_bytes:
            raise ValueError("Reader file exceeds the configured size limit.")
        return result.stdout, repo_path
    raise FileNotFoundError(f"Reader file not found in the selected local Git snapshot: {relative_path.as_posix()}")


def _read_snapshot_asset(
    value: Any,
    *,
    options: Dict[str, Any],
    source: Dict[str, Any],
    base_file: Optional[Union[str, Path]] = None,
    allow_parent: bool = False,
    max_bytes: int = MAX_READER_BYTES,
) -> Tuple[bytes, Union[Path, str]]:
    relative_path = _normalize_asset_path(value, allow_parent=allow_parent)
    if source["kind"] == "local_snapshot":
        return _read_local_asset(
            relative_path,
            map_path=options["path"],
            git_root=options.get("git_root", "."),
            base_file=base_file,
            max_bytes=max_bytes,
        )
    return _read_git_asset(
        relative_path,
        commit=source["commit"],
        git_path=options.get("git_path"),
        git_root=options.get("git_root", "."),
        base_file=str(base_file) if base_file is not None else None,
        max_bytes=max_bytes,
    )


def load_owner_reader_document(
    *,
    node_id: str,
    background_index: Optional[int] = None,
    path: Optional[Union[str, Path]] = None,
    git_ref: Optional[str] = None,
    git_path: Optional[str] = None,
    git_root: Union[str, Path] = ".",
) -> Dict[str, Any]:
    """Load one explicitly linked reader or audit text file from a snapshot."""
    node, source = _load_owner_node(
        node_id=node_id, path=path, git_ref=git_ref, git_path=git_path, git_root=git_root
    )
    if background_index is None:
        reference = node.reader_file
        label = "reader_file"
    else:
        if background_index < 0 or background_index >= len(node.background_files):
            raise FileNotFoundError("Background file index is not present on this node.")
        reference = node.background_files[background_index]
        label = "background_files entry"
    if reference is None:
        raise FileNotFoundError(f"No {label} is recorded for node {node_id}.")

    descriptor = _file_reference_dict(reference, label)
    visibility = descriptor.get("visibility")
    if background_index is None and visibility is not None and visibility not in READER_VISIBILITIES:
        raise FileNotFoundError(f"The reader file is not marked for node-detail display on node {node_id}.")
    relative_path = descriptor.get("path") or descriptor.get("file")
    suffix = Path(str(relative_path or "")).suffix.lower()
    if suffix not in READER_TEXT_SUFFIXES:
        raise ValueError("Linked reader and background files must be Markdown or plain text.")
    data, resolved = _read_snapshot_asset(
        relative_path,
        options={"path": path, "git_path": git_path, "git_root": git_root},
        source=source,
    )
    try:
        content = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("Linked reader file is not valid UTF-8 text.") from exc
    normalized_path = str(relative_path).replace("\\", "/")
    return {
        "node_id": node_id,
        "path": normalized_path,
        "file_name": PurePosixPath(normalized_path).name,
        "kind": descriptor.get("kind"),
        "visibility": descriptor.get("visibility"),
        "status": descriptor.get("status"),
        "purpose": descriptor.get("purpose"),
        "human_review": descriptor.get("human_review"),
        "content": content,
        "_resolved_path": resolved,
    }


def load_owner_reader_figure(
    *,
    node_id: str,
    relative_path: str,
    path: Optional[Union[str, Path]] = None,
    git_ref: Optional[str] = None,
    git_path: Optional[str] = None,
    git_root: Union[str, Path] = ".",
) -> Dict[str, Any]:
    """Read a raster image only when the selected reader Markdown links it."""
    node, source = _load_owner_node(
        node_id=node_id, path=path, git_ref=git_ref, git_path=git_path, git_root=git_root
    )
    if node.reader_file is None:
        raise FileNotFoundError("No reader Markdown page is recorded for this node.")
    descriptor = _file_reference_dict(node.reader_file, "reader_file")
    visibility = descriptor.get("visibility")
    if visibility is not None and visibility not in READER_VISIBILITIES:
        raise FileNotFoundError("The reader file is not marked for node-detail display.")
    reader_path = descriptor.get("path") or descriptor.get("file")
    if Path(str(reader_path or "")).suffix.lower() not in {".md", ".markdown"}:
        raise ValueError("Reader figures can only be loaded from a Markdown reader page.")
    reader_data, resolved_reader = _read_snapshot_asset(
        reader_path,
        options={"path": path, "git_path": git_path, "git_root": git_root},
        source=source,
    )
    try:
        reader_content = reader_data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("Linked reader file is not valid UTF-8 Markdown.") from exc
    without_fenced_code = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", reader_content)
    linked_paths = {unquote(match.group(1)) for match in MARKDOWN_IMAGE_RE.finditer(without_fenced_code)}
    requested = unquote(relative_path)
    if requested not in linked_paths:
        raise FileNotFoundError("Figure is not linked from this node's reader page.")

    base_file: Union[Path, str] = resolved_reader
    figure_relative = _normalize_asset_path(requested, allow_parent=True)
    content_type = READER_IMAGE_TYPES.get(Path(figure_relative.name).suffix.lower())
    if not content_type:
        raise ValueError("Reader figures must use PNG, JPEG, GIF, or WebP format.")
    data, resolved = _read_snapshot_asset(
        figure_relative,
        options={"path": path, "git_path": git_path, "git_root": git_root},
        source=source,
        base_file=base_file,
        allow_parent=True,
        max_bytes=MAX_FIGURE_BYTES,
    )
    return {"content": data, "content_type": content_type, "path": str(resolved)}


def owner_snapshot_source_available(
    *, path: Optional[Union[str, Path]], git_ref: Optional[str], git_path: Optional[str]
) -> bool:
    """Return whether an explicit owner snapshot source was configured."""
    if path is not None and (git_ref is not None or git_path is not None):
        raise ValueError("Choose a local path or a local Git ref and path, not both.")
    if (git_ref is None) != (git_path is None):
        raise ValueError("A Git snapshot requires both --owner-map-ref and --owner-map-git-path.")
    return path is not None or (git_ref is not None and git_path is not None)
