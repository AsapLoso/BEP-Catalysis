"""Unit and integration tests for BEP Mind Map research synthesis and draft overlay."""

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

import pytest

from Academics.BEP.Catalysis.mindmap.editor import load_map
from Academics.BEP.Catalysis.mindmap.schema import merge_maps
from Academics.BEP.Catalysis.mindmap.synthesize_research import CANONICAL_PATH, DRAFT_PATH, synthesize_and_save


def test_synthesis_generation_and_schema():
    """Stale candidates must not replace the curated draft overlay."""
    before_count = len(load_map(DRAFT_PATH).nodes)
    before = DRAFT_PATH.read_bytes()
    with pytest.raises(RuntimeError, match="Refusing to overwrite the curated draft overlay"):
        synthesize_and_save()
    assert DRAFT_PATH.read_bytes() == before
    assert DRAFT_PATH.exists()
    assert len(load_map(DRAFT_PATH).nodes) == before_count


def test_draft_nodes_remain_unapproved():
    """Draft maturity stays separate from approval and scientific understanding."""
    loaded = load_map(DRAFT_PATH)
    for node in loaded.nodes:
        assert node.tier in {0, 1}, f"Draft node '{node.id}' has an unexpected tier {node.tier}"
        assert node.is_draft is True, f"Node '{node.id}' must have is_draft=True"


def test_attached_sources_have_traceable_locators():
    """Attached sources are traceable; an empty list is not falsely called verified."""
    loaded = load_map(DRAFT_PATH)
    for node in loaded.nodes:
        for s in node.sources:
            if hasattr(s, "title"):
                assert s.title.strip(), f"Node '{node.id}' has source with empty title"
                # Presence of a locator is not proof that it supports a claim.
                assert (s.doi is not None and len(s.doi) > 0) or (s.path is not None and len(s.path) > 0), \
                    f"Node '{node.id}' source '{s.title}' lacks both DOI and repository path."


def test_scientific_graph_has_only_three_level_one_arms():
    """Research letters and project tasks do not become scientific root branches."""
    can_map = load_map(CANONICAL_PATH)
    drf_map = load_map(DRAFT_PATH)
    merged = merge_maps(can_map, drf_map)
    root = next(node for node in merged.nodes if node.parent is None)
    arm_ids = {node.id for node in merged.nodes if node.parent == root.id}
    assert arm_ids == {"physics", "mathematics", "systems_control"}

    nodes_by_id = {node.id: node for node in merged.nodes}
    for node in drf_map.nodes:
        current = node
        visited = set()
        while current.parent is not None:
            assert current.id not in visited, f"Cycle detected at '{current.id}'"
            visited.add(current.id)
            assert current.parent in nodes_by_id, f"Missing parent '{current.parent}' for '{current.id}'"
            current = nodes_by_id[current.parent]
        assert current.id == root.id, f"Draft node '{node.id}' is detached from the BEP root"


def test_synthesis_merged_map_acyclic():
    """Verify merged map (canonical + draft overlay) forms an acyclic valid tree."""
    can_map = load_map(CANONICAL_PATH)
    drf_map = load_map(DRAFT_PATH)
    merged = merge_maps(can_map, drf_map)

    # Check that canonical integrity is preserved
    merged.validate_canonical_integrity()
    merged.validate_parents_exist()

    # Total nodes should be canonical (4) + draft (>=12)
    assert len(merged.nodes) == len(can_map.nodes) + len(drf_map.nodes)
