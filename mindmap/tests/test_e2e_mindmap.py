"""End-to-End integration test suite for the complete BEP Ownership Mind Map system."""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import json
import hashlib
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
import threading
import shutil
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer
import pytest

from mindmap.editor import (
    load_map,
)
from mindmap import preview as preview_module
from mindmap.preview import (
    MindMapRequestHandler,
    CANONICAL_PATH,
    DRAFT_PATH,
    STATIC_DIR,
)
from mindmap.schema import merge_maps
from mindmap.research_review import compile_questions_portfolio, generate_review_dossier_markdown


def test_e2e_canonical_and_draft_integrity():
    """Verify the preserved root/three-arm reference graph and AI-only draft tiers."""
    can_map = load_map(CANONICAL_PATH)
    can_map.validate_canonical_integrity()
    assert {"bep", "physics", "mathematics", "systems_control"}.issubset({node.id for node in can_map.nodes})
    for n in can_map.nodes:
        assert n.is_draft is False

    drf_map = load_map(DRAFT_PATH)
    assert drf_map.nodes
    for n in drf_map.nodes:
        assert n.tier in {0, 1}
        assert n.is_draft is True
        # Citation gaps are valid and should remain explicit rather than being fabricated.
        assert isinstance(n.sources, list)

    merged = merge_maps(can_map, drf_map)
    assert len(merged.nodes) == len(can_map.nodes) + len(drf_map.nodes)
    merged.validate_canonical_integrity()
    merged.validate_parents_exist()


def test_e2e_guided_tour_questions_and_review_dossier_generate():
    """Verify the migrated review pipeline generates its portfolio without legacy output files."""
    q_data = compile_questions_portfolio()
    assert q_data["phase_num"] == 4
    assert len(q_data["questions"]) >= 6

    for q in q_data["questions"]:
        assert "id" in q and q["id"].startswith("Q-BEP-REVIEW-")
        assert "question" in q and len(q["question"]) > 10
        assert "suggested_options" in q and len(q["suggested_options"]) >= 2
        assert "recommended" in q and q["recommended"].startswith("(Recommended)")
        assert "rationale" in q and len(q["rationale"]) > 10

    dossier_text = generate_review_dossier_markdown()
    assert "Executive Review Dossier" in dossier_text
    assert "Recommended Sequential Review Path" in dossier_text
    assert "Question Portfolio" in dossier_text
    assert "does not approve it" in dossier_text
    assert "Promote to Approved" not in dossier_text


def test_e2e_preview_server_and_promotion_safety(tmp_path, monkeypatch):
    """Verify the existing graph endpoints and that refused promotion cannot mutate source files."""
    canonical_path = tmp_path / "bep_map.yaml"
    draft_path = tmp_path / "bep_draft_overlay.yaml"
    shutil.copy2(CANONICAL_PATH, canonical_path)
    shutil.copy2(DRAFT_PATH, draft_path)
    monkeypatch.setattr(preview_module, "CANONICAL_PATH", canonical_path)
    monkeypatch.setattr(preview_module, "DRAFT_PATH", draft_path)

    server = ThreadingHTTPServer(("127.0.0.1", 0), MindMapRequestHandler)
    host, port = server.server_address
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://{host}:{port}"

    try:
        init_can = load_map(canonical_path)
        init_drf = load_map(draft_path)
        expected_can_count = len(init_can.nodes)
        expected_drf_count = len(init_drf.nodes)
        expected_total = expected_can_count + expected_drf_count

        # Test merged graph API
        with urllib.request.urlopen(f"{base_url}/api/graph?mode=merged") as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert len(data["nodes"]) == expected_total

        # Test canonical graph API
        with urllib.request.urlopen(f"{base_url}/api/graph?mode=canonical") as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert len(data["nodes"]) == expected_can_count

        # Promotion is disabled and must leave both isolated map files byte-identical.
        before = {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (canonical_path, draft_path)
        }
        req = urllib.request.Request(
            f"{base_url}/api/promote",
            data=json.dumps({"id": "synthetic-test-question", "new_tier": 2}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with pytest.raises(urllib.error.HTTPError) as err:
            urllib.request.urlopen(req)
        assert err.value.code == 410
        res = json.loads(err.value.read().decode("utf-8"))
        assert "Promotion is disabled" in res["error"]
        assert {
            path: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (canonical_path, draft_path)
        } == before
        assert len(load_map(canonical_path).nodes) == expected_can_count
        assert len(load_map(draft_path).nodes) == expected_drf_count

    finally:
        server.shutdown()
        server.server_close()
