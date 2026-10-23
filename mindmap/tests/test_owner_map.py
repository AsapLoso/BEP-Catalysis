"""Lossless owner/reference adapter and evolving graph regression tests."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from pydantic import ValidationError

REPO_ROOT = Path(__file__).resolve().parents[5]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Academics.BEP.Catalysis.mindmap.editor import edit_node, load_map
from Academics.BEP.Catalysis.mindmap.owner_map import load_owner_map_snapshot
from Academics.BEP.Catalysis.mindmap.schema import (
    MindMap,
    OwnerMapDocument,
    ReferenceMapDocument,
)


STAGES = ["idea", "ai_worked_out", "human_worked_out", "informal_writing", "formal_writing"]


def rich_owner_fixture() -> dict:
    """Synthetic compatibility fixture: two themes, six questions, and a deep branch."""
    nodes = [{
        "id": "root", "parent": None, "title": "BEP root", "kind": "root",
        "progress_stage": "idea", "structural_approval": "owner_chosen_root",
        "owner_read_status": "unread", "owner_content_approval": "unapproved",
        "notes": "Root annotations survive serialization.", "sources": [],
        "private_extension": {"revision": 3, "nested": ["kept", {"flag": False}]},
    }]
    for theme in ("theme-a", "theme-b"):
        nodes.append({
            "id": theme, "parent": "root", "title": f"Theme {theme[-1].upper()}", "kind": "theme",
            "progress_stage": "idea", "structure_status": "owner_approved_structure_only",
            "owner_read_status": "unread", "owner_content_approval": "unapproved",
            "rationale": "A structural node with independent content status.",
            "sources": [],
        })
        for index, reaction in enumerate(("R1", "R2", "R3")):
            node_id = f"{theme}-{reaction.lower()}"
            source_id = f"source-{theme}-{reaction.lower()}"
            claim_id = f"claim-{theme}-{reaction.lower()}"
            link = {
                "reference_node_id": f"reference-{node_id}",
                "source_id": source_id,
                "reference_commit": "0123456789abcdef",
                "relation_to_claim": "supports_context",
                "owner_review": "unread",
                "human_verified": False,
                "future_link_metadata": {"retained": True},
            }
            claim = {
                "id": claim_id,
                "statement": f"Bounded claim for {reaction}.",
                "evidence_type": "source_model_result",
                "source_ids": [source_id],
                "status": "ai_attached",
                "human_verified": False,
                "ai_reference_links": [link],
                "claim_extension": "preserve claim provenance",
            }
            source = {
                "id": source_id,
                "title": f"Source for {reaction}",
                "doi": None,
                "url": None,
                "locator": f"Section {index + 1}",
                "supports": [f"Supports the bounded {reaction} claim."],
                "source_access": "abstract_checked",
                "review": "ai_attached",
                "human_verified": False,
                "owner_read_status": "unread",
                "owner_citation_approval": "unapproved",
                "source_extension": {"source_note": "kept exactly"},
            }
            node = {
                "id": node_id,
                "parent": theme,
                "title": f"Question {reaction} in {theme}",
                "question": f"Independent question {reaction}.",
                "kind": "research_question",
                "maturity": STAGES[(index + (0 if theme == "theme-a" else 2)) % len(STAGES)],
                "progress_stage": STAGES[(index + (0 if theme == "theme-a" else 2)) % len(STAGES)],
                "approval": "accepted",
                "structure_status": "owner_approved_structure_only",
                "understanding_status": "ai_worked_out",
                "human_understanding_review": "not_assessed",
                "owner_read_status": "unread",
                "owner_approval_status": "structure_only",
                "owner_content_approval": "unapproved",
                "source_claim_review": "ai_attached_only",
                "summary": f"Summary for {reaction}.",
                "rationale": f"Rationale for {reaction}.",
                "notes": f"Detailed notes for {reaction}, with no truncation.\nSecond line.",
                "equations": [{"id": reaction, "expression": f"x_{reaction} = y", "meaning": "Illustrative only", "units": []}],
                "claims": [claim],
                "sources": [source],
                "assumptions": [f"Assumption for {reaction}"],
                "limitations": [f"Limit for {reaction}"],
                "related_ids": [],
                "ai_reference_related_ids": [f"reference-{node_id}"],
                "open_questions": [f"What remains open for {reaction}?"],
                "origin": "synthetic_test_fixture",
                "decision_receipt": {"structure": "accepted", "understanding": "none"},
            }
            nodes.append(node)
            if reaction == "R1" and theme == "theme-a":
                nodes.append({
                    "id": "citation-gap", "parent": node_id, "title": "Citation gap",
                    "progress_stage": "idea", "claims": [{
                        "id": "gap-claim", "statement": "No citation supplied.",
                        "source_ids": [], "status": "citation_gap",
                    }], "sources": [],
                })

    nodes.append({
        "id": "legacy-progress-record", "parent": "root", "title": "Legacy record",
        "tier": 2, "owner_content_approval": "unapproved", "human_understanding_review": "not_assessed",
    })

    last_parent = "theme-a-r1"
    for depth in range(1, 9):
        node_id = f"deep-{depth}"
        nodes.append({"id": node_id, "parent": last_parent, "title": f"Depth {depth}", "progress_stage": "idea"})
        last_parent = node_id
    return {
        "dataset": {"role": "owner_personal_map", "edition": "fixture-v1", "extra": {"kept": True}},
        "nodes": nodes,
        "top_level_extension": ["round-trip", {"revision": 2}],
    }


def test_owner_map_round_trip_preserves_all_rich_fields_and_independent_stages():
    raw = rich_owner_fixture()
    original = json.loads(json.dumps(raw))
    parsed = OwnerMapDocument.model_validate(raw)
    serialized = parsed.model_dump(mode="json", exclude_unset=True)

    assert serialized == original
    assert raw == original, "validation must not mutate the caller's map object"
    assert len([node for node in serialized["nodes"] if node.get("kind") == "research_question"]) == 6
    assert {node["progress_stage"] for node in serialized["nodes"] if "progress_stage" in node} == set(STAGES)
    assert serialized["nodes"][0]["private_extension"] == original["nodes"][0]["private_extension"]
    q_r1 = next(node for node in serialized["nodes"] if node["id"] == "theme-a-r1")
    assert q_r1["claims"][0]["ai_reference_links"][0]["future_link_metadata"] == {"retained": True}

    legacy = next(node for node in serialized["nodes"] if node.get("id") == "legacy-progress-record")
    assert legacy.get("progress_stage") is None
    assert legacy["human_understanding_review"] == "not_assessed"
    assert legacy["owner_content_approval"] == "unapproved"

    gap = next(node for node in serialized["nodes"] if node["id"] == "citation-gap")
    assert gap["claims"][0]["source_ids"] == []
    assert "human_verified" not in gap["claims"][0]


def test_owner_graph_validation_rejects_duplicates_missing_parents_and_disconnection():
    base = rich_owner_fixture()
    duplicate = json.loads(json.dumps(base))
    duplicate["nodes"].append(json.loads(json.dumps(duplicate["nodes"][1])))
    with pytest.raises(ValidationError, match="Duplicate owner-map node id"):
        OwnerMapDocument.model_validate(duplicate)

    missing = json.loads(json.dumps(base))
    missing["nodes"][1]["parent"] = "missing"
    with pytest.raises(ValidationError, match="references missing parent"):
        OwnerMapDocument.model_validate(missing)

    disconnected = json.loads(json.dumps(base))
    disconnected["nodes"].append({"id": "second-root", "parent": None, "title": "Second root"})
    with pytest.raises(ValidationError, match="exactly one root"):
        OwnerMapDocument.model_validate(disconnected)

    cyclic = {"nodes": [
        {"id": "root", "parent": None, "title": "Root"},
        {"id": "cycle-a", "parent": "cycle-b", "title": "Cycle A"},
        {"id": "cycle-b", "parent": "cycle-a", "title": "Cycle B"},
    ]}
    with pytest.raises(ValidationError, match="exactly one root|Cycle detected"):
        OwnerMapDocument.model_validate(cyclic)


def test_reference_map_resolves_claim_refs_without_inventing_quotes_or_owner_verification():
    owner = rich_owner_fixture()
    reference = {
        "dataset": {"role": "ai_reference_map", "human_source_verification": "not_asserted"},
        "nodes": [{
            "id": "reference-theme-a-r1", "parent": None, "title": "Reference concept",
            "claim_refs": [{
                "source_id": "source-theme-a-r1", "locator": "Section 2.3",
                "evidence_type": "source_model_result", "supports": "Model result in reference scope only.",
            }],
        }],
        "sources": [{
            "id": "source-theme-a-r1", "title": "AI reference source", "access_status": "abstract_checked",
            "verification": "ai_checked_text", "human_verified": False,
        }],
    }
    reference_model = ReferenceMapDocument.model_validate(reference)
    ref_serialized = reference_model.model_dump(mode="json", exclude_unset=True)
    assert ref_serialized == reference

    # The public helper is shared with the browser; check the current schema shape.
    question = next(node for node in owner["nodes"] if node["id"] == "theme-a-r1")
    link = question["claims"][0]["ai_reference_links"][0]
    assert link["reference_node_id"] == "reference-theme-a-r1"
    assert reference_model.nodes[0].claim_refs[0].locator == "Section 2.3"
    assert reference_model.sources[0].human_verified is False
    assert "excerpt" not in reference_model.sources[0].model_dump(exclude_unset=True)


def test_legacy_map_editor_round_trip_retains_future_fields(tmp_path: Path):
    path = tmp_path / "legacy.yaml"
    path.write_text(yaml.safe_dump({
        "dataset_extension": {"preserve": True},
        "nodes": [{
            "id": "root", "parent": None, "title": "Root", "tier": 2,
            "owner_content_approval": "unapproved",
            "future_node_field": {"nested": ["value", {"flag": False}]},
            "sources": [{
                "title": "Source", "locator": "Section 4", "review": "ai_attached",
                "human_verified": False, "future_source_field": {"state": "retained"},
            }],
        }],
    }, sort_keys=False), encoding="utf-8")

    edit_node(path, "root", notes="Edited only the requested legacy field.")
    reread = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert reread["dataset_extension"] == {"preserve": True}
    assert reread["nodes"][0]["future_node_field"] == {"nested": ["value", {"flag": False}]}
    assert reread["nodes"][0]["sources"][0]["future_source_field"] == {"state": "retained"}
    assert reread["nodes"][0]["sources"][0]["human_verified"] is False
    assert reread["nodes"][0]["owner_content_approval"] == "unapproved"

    before = hashlib.sha256(path.read_bytes()).hexdigest()
    with pytest.raises(ValueError, match="Owner progress, placement approval"):
        edit_node(path, "root", owner_content_approval="approved")
    with pytest.raises(ValueError, match="Owner progress, placement approval"):
        edit_node(path, "root", claims=[{"id": "unsafe", "human_verified": True}])
    assert hashlib.sha256(path.read_bytes()).hexdigest() == before


def test_explicit_local_and_pinned_git_snapshots_are_read_only(tmp_path: Path):
    raw_owner = rich_owner_fixture()
    owner_path = tmp_path / "owner.yaml"
    owner_path.write_text(yaml.safe_dump(raw_owner, sort_keys=False), encoding="utf-8")
    owner_hash = hashlib.sha256(owner_path.read_bytes()).hexdigest()
    loaded = load_owner_map_snapshot(path=owner_path)
    assert len(loaded["nodes"]) == len(raw_owner["nodes"])
    assert loaded["source"]["read_only"] is True
    assert loaded["source"]["authoritative"] is False
    assert hashlib.sha256(owner_path.read_bytes()).hexdigest() == owner_hash

    git_root = tmp_path / "git-source"
    git_root.mkdir()
    subprocess.run(["git", "init", "-b", "main", str(git_root)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(git_root), "config", "user.name", "Test"], check=True)
    subprocess.run(["git", "-C", str(git_root), "config", "user.email", "test@example.invalid"], check=True)
    (git_root / "reference").mkdir()
    (git_root / "reference" / "nodes.yaml").write_text(yaml.safe_dump({
        "nodes": [{"id": "ref-root", "parent": None, "title": "Reference root", "claim_refs": []}],
    }, sort_keys=False), encoding="utf-8")
    (git_root / "reference" / "sources.yaml").write_text(yaml.safe_dump({
        "sources": [{"id": "source-1", "title": "Reference source", "human_verified": False}],
    }, sort_keys=False), encoding="utf-8")
    subprocess.run(["git", "-C", str(git_root), "add", "reference"], check=True)
    subprocess.run(["git", "-C", str(git_root), "commit", "-m", "add reference fixture"], check=True, capture_output=True)
    pinned_commit = subprocess.run(
        ["git", "-C", str(git_root), "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()

    (git_root / "manifest.yaml").write_text(yaml.safe_dump({
        "base": {
            "commit": pinned_commit,
            "nodes_path": "reference/nodes.yaml",
            "sources_path": "reference/sources.yaml",
        },
    }, sort_keys=False), encoding="utf-8")
    (git_root / "owner.yaml").write_text(yaml.safe_dump(raw_owner, sort_keys=False), encoding="utf-8")
    subprocess.run(["git", "-C", str(git_root), "add", "manifest.yaml", "owner.yaml"], check=True)
    subprocess.run(["git", "-C", str(git_root), "commit", "-m", "add owner and snapshot manifest"], check=True, capture_output=True)
    git_owner_hash = hashlib.sha256((git_root / "owner.yaml").read_bytes()).hexdigest()

    loaded_git = load_owner_map_snapshot(
        git_ref="HEAD",
        git_path="owner.yaml",
        git_root=git_root,
        reference_git_ref="HEAD",
        reference_git_path="manifest.yaml",
    )
    assert loaded_git["source"]["kind"] == "local_git_ref_snapshot"
    assert loaded_git["reference_map"]["nodes"][0]["id"] == "ref-root"
    assert loaded_git["reference_map"]["sources"][0]["id"] == "source-1"
    assert len(loaded_git["reference_data_sources"]) == 2
    assert hashlib.sha256((git_root / "owner.yaml").read_bytes()).hexdigest() == git_owner_hash
