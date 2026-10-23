"""Read-only adapter for explicitly selected owner-map snapshots and references."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Optional, Tuple, Union

import yaml

try:
    from Academics.BEP.Catalysis.mindmap.schema import OwnerMapDocument, ReferenceMapDocument
except (ImportError, ModuleNotFoundError):
    from schema import OwnerMapDocument, ReferenceMapDocument


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

    relative = PurePosixPath(git_path)
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
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
        if isinstance(base, dict) and not reference_raw.get("nodes") and (base.get("nodes_path") or base.get("sources_path")):
            pinned_ref = base.get("commit") or base.get("branch")
            if not pinned_ref or not base.get("nodes_path") or not base.get("sources_path"):
                raise ValueError("Reference-map manifest must pin both nodes_path and sources_path to a local ref.")
            nodes_bytes, nodes_source = _read_source(
                path=None,
                git_ref=str(pinned_ref),
                git_path=str(base["nodes_path"]),
                git_root=git_root,
            )
            sources_bytes, sources_source = _read_source(
                path=None,
                git_ref=str(pinned_ref),
                git_path=str(base["sources_path"]),
                git_root=git_root,
            )
            reference_nodes = _parse_document(nodes_bytes, "AI reference nodes")
            reference_sources = _parse_document(sources_bytes, "AI reference sources")
            reference_raw["nodes"] = reference_nodes.get("nodes", [])
            reference_raw["sources"] = reference_sources.get("sources", [])
            reference_data_sources.extend([nodes_source, sources_source])
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


def owner_snapshot_source_available(
    *, path: Optional[Union[str, Path]], git_ref: Optional[str], git_path: Optional[str]
) -> bool:
    """Return whether an explicit owner snapshot source was configured."""
    if path is not None and (git_ref is not None or git_path is not None):
        raise ValueError("Choose a local path or a local Git ref and path, not both.")
    if (git_ref is None) != (git_path is None):
        raise ValueError("A Git snapshot requires both --owner-map-ref and --owner-map-git-path.")
    return path is not None or (git_ref is not None and git_path is not None)
