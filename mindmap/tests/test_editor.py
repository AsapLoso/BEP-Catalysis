"""Unit and integration tests for BEP Mind Map schema, editor, and MCP server."""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[5]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
MINDMAP_DIR = Path(__file__).resolve().parents[1]
if str(MINDMAP_DIR) not in sys.path:
    sys.path.insert(0, str(MINDMAP_DIR))

import shutil
import tempfile
import hashlib
import pytest

from Academics.BEP.Catalysis.mindmap.editor import (
    add_node,
    attach_source,
    delete_node,
    edit_node,
    load_map,
    promote_draft_node,
    reparent_node,
    save_map,
    set_importance,
    set_tier,
)
from Academics.BEP.Catalysis.mindmap.mcp_server import MindMapMCPServer
from Academics.BEP.Catalysis.mindmap.schema import MindMap, MindMapNode, SourceItem


@pytest.fixture
def temp_map_dir(tmp_path: Path):
    """Fixture providing temporary canonical and draft map files."""
    canonical_seed = tmp_path / "bep_map.yaml"
    draft_seed = tmp_path / "bep_draft_overlay.yaml"

    seed_content = """nodes:
  - id: bep
    parent: null
    title: "Dual BEP: Acetylene Semi-Hydrogenation Reactor Modeling"
    tier: 2
    importance: 3
    rationale: "Core root node."
    notes: ""
    sources: []
    open_questions: []
    is_draft: false
  - id: physics
    parent: bep
    title: "Physics"
    tier: 0
    importance: null
    rationale: "Physical foundations."
    notes: ""
    sources: []
    open_questions: []
    is_draft: false
  - id: mathematics
    parent: bep
    title: "Mathematics"
    tier: 0
    importance: null
    rationale: "Mathematical foundations."
    notes: ""
    sources: []
    open_questions: []
    is_draft: false
  - id: systems_control
    parent: bep
    title: "Systems & Control"
    tier: 0
    importance: null
    rationale: "Control foundations."
    notes: ""
    sources: []
    open_questions: []
    is_draft: false
"""
    canonical_seed.write_text(seed_content, encoding="utf-8")
    draft_seed.write_text("nodes: []\n", encoding="utf-8")
    return tmp_path, canonical_seed, draft_seed


def test_canonical_seed_integrity():
    """Verify canonical seed file exists and passes canonical integrity."""
    pkg_canonical = Path(__file__).resolve().parents[1] / "data" / "bep_map.yaml"
    assert pkg_canonical.exists()
    m = load_map(pkg_canonical)
    m.validate_canonical_integrity()
    m.validate_parents_exist()
    assert len(m.nodes) == 4
    assert m.get_node("bep") is not None
    assert m.get_node("bep").tier == 2
    assert {n.id for n in m.nodes if n.parent == "bep"} == {
        "physics", "mathematics", "systems_control"
    }


def test_schema_duplicate_id_rejection():
    """Verify schema rejects duplicate node IDs."""
    data = {
        "nodes": [
            {"id": "bep", "parent": None, "title": "Root"},
            {"id": "bep", "parent": None, "title": "Duplicate Root"},
        ]
    }
    with pytest.raises(Exception, match="Duplicate node id"):
        MindMap.model_validate(data)


def test_schema_cycle_detection():
    """Verify schema rejects cyclic graphs."""
    data = {
        "nodes": [
            {"id": "node_a", "parent": "node_b", "title": "A"},
            {"id": "node_b", "parent": "node_a", "title": "B"},
        ]
    }
    with pytest.raises(Exception, match="Cycle detected"):
        MindMap.model_validate(data)


def test_schema_tier_and_importance_bounds():
    """Verify bounds for tier (0-4) and importance (0-3)."""
    with pytest.raises(Exception):
        MindMapNode(id="test", title="Test", tier=5)

    with pytest.raises(Exception):
        MindMapNode(id="test", title="Test", tier=-1)

    with pytest.raises(Exception):
        MindMapNode(id="test", title="Test", importance=4)

    node_ok = MindMapNode(id="test", title="Test", tier=3, importance=2)
    assert node_ok.tier == 3
    assert node_ok.importance == 2


def test_legacy_owner_status_and_high_tier_writes_are_refused(temp_map_dir):
    _, can_path, _ = temp_map_dir
    before = hashlib.sha256(can_path.read_bytes()).hexdigest()
    with pytest.raises(ValueError, match="Legacy tiers 2-4 are read-only"):
        set_tier(can_path, "physics", 2, is_canonical=True)
    with pytest.raises(ValueError, match="Owner progress, placement approval"):
        edit_node(can_path, "physics", is_canonical=True, owner_content_approval="approved")
    assert hashlib.sha256(can_path.read_bytes()).hexdigest() == before


def test_editor_add_and_edit_node(temp_map_dir):
    """Test adding and editing a node."""
    _, can_path, _ = temp_map_dir
    new_node = MindMapNode(
        id="kinetics",
        parent="physics",
        title="Kinetics",
        tier=1,
        importance=3,
        rationale="LHHW reaction rate laws",
    )
    add_node(can_path, new_node, is_canonical=True)

    m = load_map(can_path)
    assert len(m.nodes) == 5
    assert m.get_node("kinetics").title == "Kinetics"

    edit_node(can_path, "kinetics", is_canonical=True, notes="Arrhenius and Langmuir terms")
    m2 = load_map(can_path)
    assert m2.get_node("kinetics").notes == "Arrhenius and Langmuir terms"


def test_editor_reparent_and_cycle_guard(temp_map_dir):
    """Test reparenting and cycle guard."""
    _, can_path, _ = temp_map_dir
    add_node(can_path, MindMapNode(id="kinetics", parent="physics", title="Kinetics"), is_canonical=True)
    add_node(can_path, MindMapNode(id="arrhenius", parent="kinetics", title="Arrhenius"), is_canonical=True)

    # Reparent arrhenius to bep directly
    reparent_node(can_path, "arrhenius", "bep", is_canonical=True)
    m = load_map(can_path)
    assert m.get_node("arrhenius").parent == "bep"

    # Self-parent should fail
    with pytest.raises(ValueError, match="cannot be its own parent"):
        reparent_node(can_path, "arrhenius", "arrhenius", is_canonical=True)


def test_editor_delete_leaf_vs_cascade(temp_map_dir):
    """Test deleting leaf node and cascading delete."""
    _, can_path, _ = temp_map_dir
    add_node(can_path, MindMapNode(id="transport", parent="physics", title="Transport"), is_canonical=True)
    add_node(can_path, MindMapNode(id="diffusion", parent="transport", title="Diffusion"), is_canonical=True)

    # Attempt to delete transport without cascade should fail
    with pytest.raises(ValueError, match="has 1 children"):
        delete_node(can_path, "transport", cascade=False, is_canonical=True)

    # Delete with cascade
    deleted = delete_node(can_path, "transport", cascade=True, is_canonical=True)
    assert set(deleted) == {"transport", "diffusion"}
    m = load_map(can_path)
    assert m.get_node("transport") is None
    assert m.get_node("diffusion") is None


def test_editor_attach_source(temp_map_dir):
    """Test attaching verified sources."""
    _, can_path, _ = temp_map_dir
    source = {
        "title": "Berger et al. (2008)",
        "doi": "10.1016/j.ces.2008.08.012",
        "path": "Articles/analyses/dynamic_kinetics_berger2008.md",
        "section": "Section 5 - Criteria for transport limitations",
    }
    attach_source(can_path, "physics", source, is_canonical=True)
    m = load_map(can_path)
    phy = m.get_node("physics")
    assert len(phy.sources) == 1
    assert phy.sources[0].doi == "10.1016/j.ces.2008.08.012"


def test_draft_overlay_promotion_is_disabled_without_data_loss(temp_map_dir):
    """Draft placement never implies owner understanding and refused calls preserve both files."""
    _, can_path, draft_path = temp_map_dir

    # Add node to draft overlay pointing to canonical parent 'physics'
    draft_node = MindMapNode(
        id="thiele_modulus",
        parent="physics",
        title="Thiele Modulus & Effectiveness Factor",
        tier=1,
        importance=3,
        rationale="Evaluates internal pore diffusion resistance vs surface reaction rate",
    )
    canonical_ids = {n.id for n in load_map(can_path).nodes}
    add_node(draft_path, draft_node, is_canonical=False, allowed_external_parents=canonical_ids)

    d_map = load_map(draft_path)
    assert len(d_map.nodes) == 1
    assert d_map.nodes[0].id == "thiele_modulus"
    assert d_map.nodes[0].tier == 1

    before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in (can_path, draft_path)}
    with pytest.raises(ValueError, match="Promotion is disabled"):
        promote_draft_node(draft_path, can_path, "thiele_modulus", new_tier=2)
    assert {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in (can_path, draft_path)} == before
    assert load_map(can_path).get_node("thiele_modulus") is None
    assert load_map(draft_path).get_node("thiele_modulus") is not None


def test_mcp_server_flow(temp_map_dir):
    """Test MindMapMCPServer tool calls."""
    _, can_path, draft_path = temp_map_dir
    server = MindMapMCPServer(canonical_path=can_path, draft_path=draft_path)

    # 1. Initialize
    init_resp = server.handle_request({"jsonrpc": "2.0", "id": 1, "method": "initialize"})
    assert init_resp["result"]["serverInfo"]["name"] == "bep-mindmap-mcp"

    # 2. Tools list
    list_resp = server.handle_request({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    tool_names = [t["name"] for t in list_resp["result"]["tools"]]
    assert "add_node" in tool_names
    assert "promote_node" in tool_names

    # 3. Add draft node via tool call
    call_resp = server.handle_request({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "add_node",
            "arguments": {
                "id": "mol_discretization",
                "parent": "mathematics",
                "title": "Method of Lines Discretization",
                "tier": 1,
                "importance": 2,
                "rationale": "Semi-discretize spatial domain via finite differences",
                "is_draft": True,
            },
        },
    })
    assert "error" not in call_resp
    result_text = call_resp["result"]["content"][0]["text"]
    assert "mol_discretization" in result_text

    # 4. Promotion is explicitly refused and both map files remain unchanged.
    before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in (can_path, draft_path)}
    prom_resp = server.handle_request({
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {
            "name": "promote_node",
            "arguments": {"id": "mol_discretization", "new_tier": 2},
        },
    })
    assert "error" in prom_resp
    assert "Promotion is disabled" in prom_resp["error"]["message"]
    assert {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in (can_path, draft_path)} == before

    # 5. Check merged map
    map_resp = server.handle_request({
        "jsonrpc": "2.0",
        "id": 5,
        "method": "tools/call",
        "params": {"name": "get_map", "arguments": {"mode": "canonical"}},
    })
    map_text = map_resp["result"]["content"][0]["text"]
    assert "mol_discretization" not in map_text
