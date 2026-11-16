"""Unit tests for the two-map BEP Mind Map stdio MCP server."""

import json
from pathlib import Path
import tempfile
import unittest

from mindmap.mcp_server import MindMapMCPServer


class TestMindMapMCPServer(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name) / "owner_working_map"
        self.root.mkdir(parents=True)
        self.owner_path = self.root / "current_map.yaml"
        self.ref_path = self.root / "reference_map.yaml"

        self.owner_path.write_text(
            json.dumps({
                "dataset": {"name": "Owner Map", "role": "owner_selected_topology_not_ai_reference"},
                "nodes": [
                    {"id": "bep", "parent": None, "title": "BEP Root", "maturity": "idea"}
                ],
            }),
            encoding="utf-8",
        )
        self.ref_path.write_text(
            json.dumps({
                "dataset": {"name": "AI Reference Map", "role": "AI-only scientific reference"},
                "nodes": [
                    {"id": "bep", "parent": None, "title": "BEP AI Root", "maturity": "ai_worked_out"}
                ],
            }),
            encoding="utf-8",
        )
        self.server = MindMapMCPServer(owner_path=self.owner_path, reference_path=self.ref_path)

    def tearDown(self) -> None:
        self.tmpdir.cleanup()

    def test_ai_map_writable_anytime_and_capped(self) -> None:
        added = self.server.execute_tool("add_node", {
            "target": "ai",
            "id": "peclet_number",
            "parent": "bep",
            "title": "Peclet Number",
            "question": "When is axial dispersion negligible?",
            "summary": "Ratio of advective to dispersive transport.",
            "equations": ["Pe = u L / D_ax"],
            "assumptions": ["Steady plug flow"],
            "limitations": ["1D approximation"],
            "maturity": "ai_worked_out",
        })
        self.assertEqual(added["id"], "peclet_number")
        self.assertEqual(added["equations"], ["Pe = u L / D_ax"])

        with self.assertRaises(ValueError):
            self.server.execute_tool("set_maturity", {
                "target": "ai",
                "id": "peclet_number",
                "stage": "human_worked_out",
            })

    def test_owner_map_requires_explicit_approval(self) -> None:
        with self.assertRaises(ValueError):
            self.server.execute_tool("add_node", {
                "target": "owner",
                "id": "thiele",
                "parent": "bep",
                "title": "Thiele Modulus",
            })

        with self.assertRaises(ValueError):
            self.server.execute_tool("add_node", {
                "target": "owner",
                "id": "thiele",
                "parent": "bep",
                "title": "Thiele Modulus",
                "owner_approved": True,
                "approval_note": "   ",
            })

        res = self.server.execute_tool("add_node", {
            "target": "owner",
            "id": "thiele",
            "parent": "bep",
            "title": "Thiele Modulus",
            "summary": "Diffusion vs reaction rate in catalyst pellet.",
            "owner_approved": True,
            "approval_note": "Owner approved adding Thiele modulus under root.",
        })
        self.assertEqual(res["owner_approval_status"], "owner_approved_placement")
        saved = json.loads(self.owner_path.read_text(encoding="utf-8"))
        self.assertEqual(saved["dataset"]["name"], "Owner Map")
        self.assertEqual(len(saved["nodes"]), 2)

    def test_reader_page_roundtrip_and_traversal_guard(self) -> None:
        res = self.server.execute_tool("write_reader_page", {
            "target": "owner",
            "id": "bep",
            "content": "# BEP Root\n\nStructured notes.\n",
            "owner_approved": True,
            "approval_note": "Owner approved creating root reader page.",
        })
        self.assertEqual(res["reader_file"]["path"], "owner_working_map/pages/bep/index.md")

        read_back = self.server.execute_tool("read_reader_page", {"target": "owner", "id": "bep"})
        self.assertIn("Structured notes.", read_back["content"])

        with self.assertRaises(ValueError):
            self.server.execute_tool("write_reader_page", {
                "target": "ai",
                "id": "bep",
                "content": "bad",
                "path": "../../escape.md",
            })

    def test_jsonrpc_handshake_and_ping(self) -> None:
        init = self.server.handle_request({"jsonrpc": "2.0", "id": 1, "method": "initialize"})
        self.assertEqual(init["result"]["serverInfo"]["name"], "bep-mindmap-mcp")
        self.assertIsNone(self.server.handle_request({"jsonrpc": "2.0", "method": "notifications/initialized"}))
        self.assertEqual(self.server.handle_request({"jsonrpc": "2.0", "id": 2, "method": "ping"})["result"], {})


if __name__ == "__main__":
    unittest.main()
