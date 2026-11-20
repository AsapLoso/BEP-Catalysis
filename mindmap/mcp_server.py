"""Local stdio MCP Server for BEP Ownership Mind Map.

Exposes deterministic mind-map editing tools via standard Model Context Protocol (MCP) JSON-RPC 2.0.
Supports:
- AI reference map (`reference_map.yaml`, writable anytime; maturity capped at `ai_worked_out`)
- Personal owner map (`current_map.yaml`, writable only with explicit `owner_approved=True` + `approval_note`)
- Structured Thesis & Audit node fields and linked Markdown reader pages
- Legacy `canonical`/`draft` fallback when instantiated with `canonical_path`/`draft_path`
"""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
import yaml

from mindmap.editor import (
    add_node,
    attach_source,
    delete_node,
    edit_node,
    load_map,
    reparent_node,
    set_importance,
    set_tier,
)
from mindmap.schema import PROGRESS_STAGES, merge_maps

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_DIR = Path(__file__).resolve().parent / "data"
CANONICAL_PATH = DEFAULT_DATA_DIR / "bep_map.yaml"
DRAFT_PATH = DEFAULT_DATA_DIR / "bep_draft_overlay.yaml"
DEFAULT_OWNER_MAP_PATH = REPO_ROOT / "research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml"
DEFAULT_REFERENCE_MAP_PATH = REPO_ROOT / "research/manual_map_sessions_2026_10_22/owner_working_map/reference_map.yaml"

AI_ALLOWED_STAGES = {"idea", "ai_worked_out"}
STRUCTURED_NODE_FIELDS = {
    "parent",
    "title",
    "kind",
    "maturity",
    "question",
    "summary",
    "open_questions",
    "equations",
    "assumptions",
    "limitations",
    "reader_file",
    "rationale",
    "notes",
    "sources",
    "claims",
    "background_files",
    "related_ids",
    "related_ai_reference_ids",
    "importance",
}


class MindMapMCPServer:
    """Stdio JSON-RPC 2.0 MCP Server for deterministic mind map edits."""

    def __init__(
        self,
        canonical_path: Optional[Path] = None,
        draft_path: Optional[Path] = None,
        owner_path: Optional[Path] = None,
        reference_path: Optional[Path] = None,
    ):
        self._explicit_legacy = canonical_path is not None or draft_path is not None
        self.canonical_path = Path(canonical_path) if canonical_path is not None else CANONICAL_PATH
        self.draft_path = Path(draft_path) if draft_path is not None else DRAFT_PATH
        self.owner_path = Path(owner_path) if owner_path is not None else DEFAULT_OWNER_MAP_PATH
        self.reference_path = Path(reference_path) if reference_path is not None else DEFAULT_REFERENCE_MAP_PATH

    def _default_target(self) -> str:
        return "legacy" if self._explicit_legacy else "ai"

    def _get_target_path(self, is_draft: bool) -> Path:
        return self.draft_path if is_draft else self.canonical_path

    def _map_path_for_target(self, target: str) -> Path:
        if target == "owner":
            return self.owner_path
        if target == "ai":
            return self.reference_path
        raise ValueError(f"Unsupported map target '{target}'. Expected 'ai' or 'owner'.")

    def _load_structured_doc(self, path: Path) -> Dict[str, Any]:
        if not path.exists():
            return {"nodes": []}
        raw_text = path.read_text(encoding="utf-8")
        data = yaml.safe_load(raw_text) or {}
        if not isinstance(data, dict) or not isinstance(data.get("nodes"), list):
            raise ValueError(f"Map file '{path}' must be a mapping containing a 'nodes' list.")
        return data

    def _save_structured_doc(self, path: Path, data: Dict[str, Any]) -> None:
        self._validate_nodes(data.get("nodes", []))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def _validate_nodes(self, nodes: List[Dict[str, Any]]) -> None:
        ids: Set[str] = set()
        by_id: Dict[str, Dict[str, Any]] = {}
        for node in nodes:
            nid = node.get("id")
            if not isinstance(nid, str) or not nid.strip():
                raise ValueError("Every node must have a non-empty string 'id'.")
            if nid in ids:
                raise ValueError(f"Duplicate node id '{nid}'.")
            if not isinstance(node.get("title"), str) or not node["title"].strip():
                raise ValueError(f"Node '{nid}' must have a non-empty 'title'.")
            ids.add(nid)
            by_id[nid] = node

        for nid in ids:
            seen: Set[str] = set()
            curr: Optional[str] = nid
            while curr is not None:
                if curr in seen:
                    raise ValueError(f"Cycle detected involving node '{curr}'.")
                seen.add(curr)
                node = by_id.get(curr)
                if node is None:
                    break
                curr = node.get("parent")

    def _require_owner_approval(self, target: str, arguments: Dict[str, Any]) -> str:
        if target != "owner":
            return ""
        approved = arguments.get("owner_approved")
        note = str(arguments.get("approval_note") or "").strip()
        if approved is not True or not note:
            raise ValueError(
                "Owner map writes require owner_approved=true and a non-empty approval_note "
                "quoting the owner's scoped approval."
            )
        return note

    def _enforce_maturity_policy(self, target: str, maturity: Optional[str]) -> None:
        if maturity is None:
            return
        if maturity not in PROGRESS_STAGES:
            raise ValueError(f"Invalid maturity stage '{maturity}'. Must be one of {list(PROGRESS_STAGES)}.")
        if target == "ai" and maturity not in AI_ALLOWED_STAGES:
            raise ValueError(
                f"AI map maturity is capped at {sorted(AI_ALLOWED_STAGES)}; cannot set '{maturity}'."
            )

    def _resolve_reader_path(self, map_path: Path, rel_path: str) -> Path:
        map_dir = map_path.resolve().parent
        session_root = map_dir.parent
        candidate = Path(rel_path)
        if candidate.is_absolute():
            raise ValueError("Reader path must be relative, not absolute.")
        prefix = f"{map_dir.name}/"
        resolved = (session_root / candidate).resolve() if rel_path.startswith(prefix) else (map_dir / candidate).resolve()
        try:
            resolved.relative_to(map_dir)
        except ValueError as exc:
            raise ValueError(f"Reader path '{rel_path}' escapes map directory '{map_dir}'.") from exc
        return resolved

    def _filter_structured_fields(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        fields: Dict[str, Any] = {}
        for key in STRUCTURED_NODE_FIELDS:
            if key in arguments and arguments[key] is not None:
                fields[key] = arguments[key]
        return fields

    def get_map(
        self,
        mode: str = "merged",
        target: Optional[str] = None,
        node_id: Optional[str] = None,
        include_children: bool = False,
    ) -> Dict[str, Any]:
        """Get the mind map graph or a single node."""
        if target in ("owner", "ai"):
            data = self._load_structured_doc(self._map_path_for_target(target))
            nodes = data.get("nodes", [])
            if node_id:
                node = next((n for n in nodes if n.get("id") == node_id), None)
                if node is None:
                    raise ValueError(f"Node '{node_id}' not found in '{target}' map.")
                result: Dict[str, Any] = {"target": target, "node": node}
                if include_children:
                    result["children"] = [n for n in nodes if n.get("parent") == node_id]
                return result
            return {"target": target, "dataset": data.get("dataset", {}), "nodes": nodes}

        if mode == "canonical":
            m = load_map(self.canonical_path)
            return m.model_dump(mode="json")
        if mode == "draft":
            m = load_map(self.draft_path)
            return m.model_dump(mode="json")
        can = load_map(self.canonical_path)
        if self.draft_path.exists():
            drf = load_map(self.draft_path)
            return merge_maps(can, drf).model_dump(mode="json")
        return can.model_dump(mode="json")

    def execute_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        target = arguments.get("target") or self._default_target()
        is_draft = arguments.get("is_draft", True)

        if name == "get_map":
            return self.get_map(
                mode=arguments.get("mode", "merged"),
                target=arguments.get("target") or (None if self._explicit_legacy else "owner"),
                node_id=arguments.get("node_id"),
                include_children=bool(arguments.get("include_children", False)),
            )

        if name == "promote_node":
            raise ValueError(
                "Promotion is disabled. Moving a node between maps requires a separately recorded, "
                "scoped owner decision; placement must not imply human understanding or citation verification."
            )

        if target in ("ai", "owner"):
            return self._execute_structured_tool(name, target, arguments)

        # Legacy canonical/draft behavior preserved for backward compatibility.
        path = self._get_target_path(is_draft)
        if name == "add_node":
            requested_tier = arguments.get("tier", 1 if is_draft else 0)
            if requested_tier >= 2:
                raise ValueError(
                    "Legacy tiers 2-4 are read-only because they can imply owner understanding or writing status."
                )
            node_data = {
                "id": arguments["id"],
                "parent": arguments.get("parent"),
                "title": arguments["title"],
                "tier": requested_tier,
                "importance": arguments.get("importance"),
                "rationale": arguments.get("rationale", ""),
                "notes": arguments.get("notes", ""),
                "sources": arguments.get("sources", []),
                "open_questions": arguments.get("open_questions", []),
                "is_draft": is_draft,
            }
            canonical_ids = {n.id for n in load_map(self.canonical_path).nodes} if self.canonical_path.exists() else set()
            res = add_node(
                path,
                node_data,
                is_canonical=not is_draft,
                allowed_external_parents=canonical_ids if is_draft else None,
            )
            return res.model_dump(mode="json")
        if name == "edit_node":
            fields = {k: v for k, v in arguments.items() if k not in ("id", "is_draft", "target")}
            return edit_node(path, arguments["id"], is_canonical=not is_draft, **fields).model_dump(mode="json")
        if name == "reparent_node":
            canonical_ids = {n.id for n in load_map(self.canonical_path).nodes} if (is_draft and self.canonical_path.exists()) else set()
            return reparent_node(
                path,
                arguments["id"],
                arguments.get("new_parent_id"),
                is_canonical=not is_draft,
                allowed_external_parents=canonical_ids if is_draft else None,
            ).model_dump(mode="json")
        if name == "delete_node":
            deleted = delete_node(path, arguments["id"], cascade=arguments.get("cascade", False), is_canonical=not is_draft)
            return {"deleted_nodes": deleted}
        if name == "set_tier":
            return set_tier(path, arguments["id"], arguments["tier"], is_canonical=not is_draft).model_dump(mode="json")
        if name == "set_importance":
            return set_importance(path, arguments["id"], arguments.get("importance"), is_canonical=not is_draft).model_dump(mode="json")
        if name == "attach_source":
            source = {
                "title": arguments["title"],
                "doi": arguments.get("doi"),
                "path": arguments.get("path"),
                "citation": arguments.get("citation"),
                "section": arguments.get("section"),
            }
            return attach_source(path, arguments["id"], source, is_canonical=not is_draft).model_dump(mode="json")
        raise ValueError(f"Unknown MCP tool: {name}")

    def _execute_structured_tool(self, name: str, target: str, arguments: Dict[str, Any]) -> Any:
        map_path = self._map_path_for_target(target)

        if name == "read_reader_page":
            data = self._load_structured_doc(map_path)
            node = next((n for n in data["nodes"] if n.get("id") == arguments["id"]), None)
            if node is None:
                raise ValueError(f"Node '{arguments['id']}' not found in '{target}' map.")
            reader_meta = node.get("reader_file") or {}
            rel_path = reader_meta.get("path") if isinstance(reader_meta, dict) else None
            if not rel_path:
                raise ValueError(f"Node '{arguments['id']}' has no reader_file.path.")
            file_path = self._resolve_reader_path(map_path, rel_path)
            if not file_path.exists():
                raise ValueError(f"Reader file '{rel_path}' does not exist on disk.")
            return {"id": node["id"], "path": rel_path, "content": file_path.read_text(encoding="utf-8")}

        approval_note = self._require_owner_approval(target, arguments)
        data = self._load_structured_doc(map_path)
        nodes: List[Dict[str, Any]] = data["nodes"]

        if name == "add_node":
            node_id = arguments["id"].strip().lower()
            if any(n.get("id") == node_id for n in nodes):
                raise ValueError(f"Node '{node_id}' already exists in '{target}' map.")
            parent_id = arguments.get("parent")
            if parent_id is not None and not any(n.get("id") == parent_id for n in nodes):
                raise ValueError(f"Parent node '{parent_id}' not found in '{target}' map.")
            maturity = arguments.get("maturity") or ("idea" if target == "ai" else "idea")
            self._enforce_maturity_policy(target, maturity)
            new_node: Dict[str, Any] = {
                "id": node_id,
                "parent": parent_id,
                "title": arguments["title"].strip(),
                "maturity": maturity,
                "question": arguments.get("question", ""),
                "summary": arguments.get("summary", ""),
                "open_questions": arguments.get("open_questions", []),
                "equations": arguments.get("equations", []),
                "assumptions": arguments.get("assumptions", []),
                "limitations": arguments.get("limitations", []),
                "rationale": arguments.get("rationale", ""),
                "notes": arguments.get("notes", ""),
                "sources": arguments.get("sources", []),
                "claims": arguments.get("claims", []),
            }
            for key, val in self._filter_structured_fields(arguments).items():
                new_node[key] = val
            if target == "owner":
                new_node["owner_approval_status"] = "owner_approved_placement"
                new_node["decision_receipt"] = {"approval_note": approval_note}
            nodes.append(new_node)
            self._save_structured_doc(map_path, data)
            return new_node

        node = next((n for n in nodes if n.get("id") == arguments["id"]), None)
        if node is None:
            raise ValueError(f"Node '{arguments['id']}' not found in '{target}' map.")

        if name == "edit_node":
            fields = self._filter_structured_fields(arguments)
            self._enforce_maturity_policy(target, fields.get("maturity"))
            for key, val in fields.items():
                node[key] = val
            if target == "owner":
                node["decision_receipt"] = {"approval_note": approval_note}
            self._save_structured_doc(map_path, data)
            return node

        if name == "reparent_node":
            new_parent_id = arguments.get("new_parent_id")
            if new_parent_id is not None and not any(n.get("id") == new_parent_id for n in nodes):
                raise ValueError(f"Parent node '{new_parent_id}' not found in '{target}' map.")
            node["parent"] = new_parent_id
            if target == "owner":
                node["decision_receipt"] = {"approval_note": approval_note}
            self._save_structured_doc(map_path, data)
            return node

        if name == "delete_node":
            cascade = bool(arguments.get("cascade", False))
            to_delete: Set[str] = {node["id"]}
            if cascade:
                changed = True
                while changed:
                    changed = False
                    for candidate in nodes:
                        if candidate.get("parent") in to_delete and candidate["id"] not in to_delete:
                            to_delete.add(candidate["id"])
                            changed = True
            elif any(n.get("parent") == node["id"] for n in nodes):
                raise ValueError(f"Node '{node['id']}' has children; pass cascade=true to delete them.")
            data["nodes"] = [n for n in nodes if n.get("id") not in to_delete]
            self._save_structured_doc(map_path, data)
            return {"deleted_nodes": sorted(to_delete)}

        if name == "set_maturity":
            stage = arguments["stage"]
            self._enforce_maturity_policy(target, stage)
            node["maturity"] = stage
            if target == "owner":
                node["decision_receipt"] = {"approval_note": approval_note}
            self._save_structured_doc(map_path, data)
            return node

        if name == "set_importance":
            node["importance"] = arguments.get("importance")
            self._save_structured_doc(map_path, data)
            return node

        if name == "attach_source":
            source: Dict[str, Any] = {"title": arguments["title"]}
            for opt in ("doi", "path", "citation", "section"):
                if arguments.get(opt):
                    source[opt] = arguments[opt]
            if target == "ai":
                source["verification"] = "ai_attached"
            node.setdefault("sources", []).append(source)
            self._save_structured_doc(map_path, data)
            return node

        if name == "write_reader_page":
            existing_rf = node.get("reader_file") if isinstance(node.get("reader_file"), dict) else {}
            rel_path = arguments.get("path") or existing_rf.get("path") or f"{map_path.parent.name}/pages/{node['id']}/index.md"
            file_path = self._resolve_reader_path(map_path, rel_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(arguments["content"], encoding="utf-8")
            node["reader_file"] = {
                **existing_rf,
                "path": rel_path,
                "visibility": arguments.get("visibility") or existing_rf.get("visibility") or "node_detail",
            }
            if target == "owner":
                node["decision_receipt"] = {"approval_note": approval_note}
            self._save_structured_doc(map_path, data)
            return {"id": node["id"], "reader_file": node["reader_file"], "written_bytes": len(arguments["content"].encode("utf-8"))}

        raise ValueError(f"Unknown MCP tool: {name}")

    def list_tools(self) -> List[Dict[str, Any]]:
        approval_props = {
            "target": {"type": "string", "enum": ["ai", "owner"], "default": "ai", "description": "'ai' writes reference_map.yaml anytime; 'owner' writes current_map.yaml only with owner_approved=true."},
            "owner_approved": {"type": "boolean", "default": False, "description": "Must be true for target='owner'."},
            "approval_note": {"type": "string", "description": "Required scoped owner approval note when target='owner'."},
        }
        structured_props = {
            "question": {"type": "string", "description": "Research question addressed by this node."},
            "summary": {"type": "string", "description": "Concise thesis summary."},
            "maturity": {"type": "string", "enum": list(PROGRESS_STAGES)},
            "open_questions": {"type": "array", "items": {"type": "string"}},
            "equations": {"type": "array", "items": {"type": ["string", "object"]}},
            "assumptions": {"type": "array", "items": {"type": "string"}},
            "limitations": {"type": "array", "items": {"type": "string"}},
            "rationale": {"type": "string"},
            "notes": {"type": "string"},
            "sources": {"type": "array", "items": {"type": ["string", "object"]}},
            "claims": {"type": "array", "items": {"type": "object"}},
            "reader_file": {"type": "object", "properties": {"path": {"type": "string"}, "visibility": {"type": "string"}}},
            "related_ids": {"type": "array", "items": {"type": "string"}},
            "related_ai_reference_ids": {"type": "array", "items": {"type": "string"}},
            "importance": {"type": ["integer", "null"], "minimum": 0, "maximum": 3},
        }
        return [
            {
                "name": "get_map",
                "description": "Retrieve the owner or AI reference mind map graph (or a single node by node_id).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target": {"type": "string", "enum": ["owner", "ai", "legacy"], "default": "owner"},
                        "mode": {"type": "string", "enum": ["canonical", "draft", "merged"], "default": "merged"},
                        "node_id": {"type": "string"},
                        "include_children": {"type": "boolean", "default": False},
                    },
                },
            },
            {
                "name": "add_node",
                "description": "Add a structured node to the AI map anytime, or to the owner map with explicit owner_approved=true.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id", "title"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "parent": {"type": ["string", "null"]},
                        "title": {"type": "string"},
                        "kind": {"type": "string"},
                        **structured_props,
                    },
                },
            },
            {
                "name": "edit_node",
                "description": "Update structured Thesis & Audit fields on an existing node.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "title": {"type": "string"},
                        **structured_props,
                    },
                },
            },
            {
                "name": "reparent_node",
                "description": "Change a node's parent with cycle checking.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "new_parent_id": {"type": ["string", "null"]},
                    },
                },
            },
            {
                "name": "delete_node",
                "description": "Delete a node (optionally cascading).",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "cascade": {"type": "boolean", "default": False},
                    },
                },
            },
            {
                "name": "set_maturity",
                "description": "Set a node's 5-stage maturity (AI map capped at idea / ai_worked_out).",
                "inputSchema": {
                    "type": "object",
                    "required": ["id", "stage"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "stage": {"type": "string", "enum": list(PROGRESS_STAGES)},
                    },
                },
            },
            {
                "name": "set_importance",
                "description": "Set importance stars (0-3 or null).",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "importance": {"type": ["integer", "null"], "minimum": 0, "maximum": 3},
                    },
                },
            },
            {
                "name": "attach_source",
                "description": "Attach a structured source reference to a node.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id", "title"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "title": {"type": "string"},
                        "doi": {"type": "string"},
                        "path": {"type": "string"},
                        "citation": {"type": "string"},
                        "section": {"type": "string"},
                    },
                },
            },
            {
                "name": "read_reader_page",
                "description": "Read the linked Markdown reader page for a node.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        "target": {"type": "string", "enum": ["owner", "ai"], "default": "owner"},
                        "id": {"type": "string"},
                    },
                },
            },
            {
                "name": "write_reader_page",
                "description": "Create or update a node's linked Markdown reader page and update reader_file.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id", "content"],
                    "properties": {
                        **approval_props,
                        "id": {"type": "string"},
                        "content": {"type": "string"},
                        "path": {"type": "string"},
                        "visibility": {"type": "string", "default": "node_detail"},
                    },
                },
            },
            {
                "name": "promote_node",
                "description": "Disabled for safety: promotion needs a separate scoped owner decision and must not infer understanding or citation verification.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        "id": {"type": "string"},
                        "new_tier": {"type": "integer", "default": 2},
                        "cascade": {"type": "boolean", "default": False},
                    },
                },
            },
        ]

    def handle_request(self, req: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        msg_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "bep-mindmap-mcp", "version": "1.1.0"},
                },
            }
        if msg_id is None or (isinstance(method, str) and method.startswith("notifications/")):
            return None
        if method == "ping":
            return {"jsonrpc": "2.0", "id": msg_id, "result": {}}
        if method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {"tools": self.list_tools()},
            }
        if method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            try:
                res = self.execute_tool(tool_name, tool_args)
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2, ensure_ascii=False)}]},
                }
            except Exception as e:
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32000, "message": str(e)},
                }
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        }

    def run_stdio(self) -> None:
        """Run interactive JSON-RPC 2.0 loop over stdin and stdout."""
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                req = json.loads(line)
                resp = self.handle_request(req)
                if resp is not None:
                    sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
                    sys.stdout.flush()
            except Exception as e:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32700, "message": f"Parse error: {e}"},
                }
                sys.stdout.write(json.dumps(err_resp) + "\n")
                sys.stdout.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description="BEP Mind Map stdio MCP server")
    parser.add_argument("--workspace-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--owner-map", type=Path, default=None)
    parser.add_argument("--reference-map", type=Path, default=None)
    args = parser.parse_args()

    root = args.workspace_root.resolve()
    owner_path = args.owner_map or (root / "research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml")
    ref_path = args.reference_map or (root / "research/manual_map_sessions_2026_10_22/owner_working_map/reference_map.yaml")
    server = MindMapMCPServer(owner_path=owner_path, reference_path=ref_path)
    server.run_stdio()


if __name__ == "__main__":
    main()
