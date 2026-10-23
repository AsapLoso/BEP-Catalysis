"""Local stdio MCP Server for BEP Ownership Mind Map.

Exposes deterministic mind-map editing tools via standard Model Context Protocol (MCP) JSON-RPC 2.0.
"""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from Academics.BEP.Catalysis.mindmap.editor import (
        add_node,
        attach_source,
        delete_node,
        edit_node,
        load_map,
        reparent_node,
        set_importance,
        set_tier,
    )
    from Academics.BEP.Catalysis.mindmap.schema import MindMapNode, merge_maps
except (ImportError, ModuleNotFoundError):
    from editor import (
        add_node,
        attach_source,
        delete_node,
        edit_node,
        load_map,
        reparent_node,
        set_importance,
        set_tier,
    )
    from schema import MindMapNode, merge_maps

DEFAULT_DATA_DIR = Path(__file__).resolve().parent / "data"
CANONICAL_PATH = DEFAULT_DATA_DIR / "bep_map.yaml"
DRAFT_PATH = DEFAULT_DATA_DIR / "bep_draft_overlay.yaml"


class MindMapMCPServer:
    """Stdio JSON-RPC 2.0 MCP Server for deterministic mind map edits."""

    def __init__(self, canonical_path: Path = CANONICAL_PATH, draft_path: Path = DRAFT_PATH):
        self.canonical_path = Path(canonical_path)
        self.draft_path = Path(draft_path)

    def _get_target_path(self, is_draft: bool) -> Path:
        return self.draft_path if is_draft else self.canonical_path

    def get_map(self, mode: str = "merged") -> Dict[str, Any]:
        """Get the mind map graph. mode: 'canonical', 'draft', or 'merged'."""
        if mode == "canonical":
            m = load_map(self.canonical_path)
            return m.model_dump(mode="json")
        elif mode == "draft":
            m = load_map(self.draft_path)
            return m.model_dump(mode="json")
        else:
            can = load_map(self.canonical_path)
            if self.draft_path.exists():
                drf = load_map(self.draft_path)
                merged = merge_maps(can, drf)
                return merged.model_dump(mode="json")
            return can.model_dump(mode="json")

    def execute_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        is_draft = arguments.get("is_draft", True)
        path = self._get_target_path(is_draft)

        if name == "get_map":
            mode = arguments.get("mode", "merged")
            return self.get_map(mode=mode)

        elif name == "add_node":
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
            # For draft nodes, parents may exist in canonical map
            canonical_ids = set()
            if self.canonical_path.exists():
                can_map = load_map(self.canonical_path)
                canonical_ids = {n.id for n in can_map.nodes}

            res = add_node(
                path,
                node_data,
                is_canonical=not is_draft,
                allowed_external_parents=canonical_ids if is_draft else None,
            )
            return res.model_dump(mode="json")

        elif name == "edit_node":
            node_id = arguments["id"]
            fields = {k: v for k, v in arguments.items() if k not in ("id", "is_draft")}
            res = edit_node(path, node_id, is_canonical=not is_draft, **fields)
            return res.model_dump(mode="json")

        elif name == "reparent_node":
            node_id = arguments["id"]
            new_parent_id = arguments.get("new_parent_id")
            canonical_ids = set()
            if is_draft and self.canonical_path.exists():
                can_map = load_map(self.canonical_path)
                canonical_ids = {n.id for n in can_map.nodes}
            res = reparent_node(
                path,
                node_id,
                new_parent_id,
                is_canonical=not is_draft,
                allowed_external_parents=canonical_ids if is_draft else None,
            )
            return res.model_dump(mode="json")

        elif name == "delete_node":
            node_id = arguments["id"]
            cascade = arguments.get("cascade", False)
            deleted = delete_node(path, node_id, cascade=cascade, is_canonical=not is_draft)
            return {"deleted_nodes": deleted}

        elif name == "set_tier":
            node_id = arguments["id"]
            tier = arguments["tier"]
            res = set_tier(path, node_id, tier, is_canonical=not is_draft)
            return res.model_dump(mode="json")

        elif name == "set_importance":
            node_id = arguments["id"]
            importance = arguments.get("importance")
            res = set_importance(path, node_id, importance, is_canonical=not is_draft)
            return res.model_dump(mode="json")

        elif name == "attach_source":
            node_id = arguments["id"]
            source = {
                "title": arguments["title"],
                "doi": arguments.get("doi"),
                "path": arguments.get("path"),
                "citation": arguments.get("citation"),
                "section": arguments.get("section"),
            }
            res = attach_source(path, node_id, source, is_canonical=not is_draft)
            return res.model_dump(mode="json")

        elif name == "promote_node":
            raise ValueError(
                "Promotion is disabled. Moving a node between maps requires a separately recorded, "
                "scoped owner decision; placement must not imply human understanding or citation verification."
            )

        else:
            raise ValueError(f"Unknown MCP tool: {name}")

    def list_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "get_map",
                "description": "Retrieve the mind map graph (canonical, draft, or merged).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "mode": {"type": "string", "enum": ["canonical", "draft", "merged"], "default": "merged"}
                    },
                },
            },
            {
                "name": "add_node",
                "description": "Add a new node to the mind map (draft overlay by default).",
                "inputSchema": {
                    "type": "object",
                    "required": ["id", "title"],
                    "properties": {
                        "id": {"type": "string"},
                        "parent": {"type": "string"},
                        "title": {"type": "string"},
                        "tier": {"type": "integer", "minimum": 0, "maximum": 1},
                        "importance": {"type": "integer", "minimum": 0, "maximum": 3},
                        "rationale": {"type": "string"},
                        "notes": {"type": "string"},
                        "is_draft": {"type": "boolean", "default": True},
                    },
                },
            },
            {
                "name": "edit_node",
                "description": "Edit fields of an existing node.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        "id": {"type": "string"},
                        "title": {"type": "string"},
                        "rationale": {"type": "string"},
                        "notes": {"type": "string"},
                        "is_draft": {"type": "boolean", "default": True},
                    },
                },
            },
            {
                "name": "reparent_node",
                "description": "Change the parent of an existing node with cycle checking.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        "id": {"type": "string"},
                        "new_parent_id": {"type": "string"},
                        "is_draft": {"type": "boolean", "default": True},
                    },
                },
            },
            {
                "name": "delete_node",
                "description": "Delete a node from the map (optionally cascading).",
                "inputSchema": {
                    "type": "object",
                    "required": ["id"],
                    "properties": {
                        "id": {"type": "string"},
                        "cascade": {"type": "boolean", "default": False},
                        "is_draft": {"type": "boolean", "default": True},
                    },
                },
            },
            {
                "name": "set_tier",
                "description": "Set only the legacy AI-reference tiers 0-1. Tiers 2-4 are read-only and are never inferred from approval.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id", "tier"],
                    "properties": {
                        "id": {"type": "string"},
                        "tier": {"type": "integer", "minimum": 0, "maximum": 1},
                        "is_draft": {"type": "boolean", "default": True},
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
                        "id": {"type": "string"},
                        "importance": {"type": ["integer", "null"], "minimum": 0, "maximum": 3},
                        "is_draft": {"type": "boolean", "default": True},
                    },
                },
            },
            {
                "name": "attach_source",
                "description": "Attach a zero-hallucination source reference to a node.",
                "inputSchema": {
                    "type": "object",
                    "required": ["id", "title"],
                    "properties": {
                        "id": {"type": "string"},
                        "title": {"type": "string"},
                        "doi": {"type": "string"},
                        "path": {"type": "string"},
                        "citation": {"type": "string"},
                        "section": {"type": "string"},
                        "is_draft": {"type": "boolean", "default": True},
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
                    "serverInfo": {"name": "bep-mindmap-mcp", "version": "1.0.0"},
                },
            }
        elif method == "notifications/initialized":
            return None
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {"tools": self.list_tools()},
            }
        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            try:
                res = self.execute_tool(tool_name, tool_args)
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]},
                }
            except Exception as e:
                return {
                    "jsonrpc": "2.0",
                    "id": msg_id,
                    "error": {"code": -32000, "message": str(e)},
                }
        else:
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
                    sys.stdout.write(json.dumps(resp) + "\n")
                    sys.stdout.flush()
            except Exception as e:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32700, "message": f"Parse error: {e}"},
                }
                sys.stdout.write(json.dumps(err_resp) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    server = MindMapMCPServer()
    server.run_stdio()
