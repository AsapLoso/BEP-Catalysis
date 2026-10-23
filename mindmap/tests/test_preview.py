"""Unit and integration tests for Mind Map preview server and visualizer assets."""

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

import json
import hashlib
import shutil
import threading
import time
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer
import pytest

from Academics.BEP.Catalysis.mindmap import preview as preview_module
from Academics.BEP.Catalysis.mindmap.preview import MindMapRequestHandler, STATIC_DIR, CANONICAL_PATH, DRAFT_PATH
from Academics.BEP.Catalysis.mindmap.editor import add_node, load_map
from Academics.BEP.Catalysis.mindmap.schema import MindMapNode


def test_static_assets_exist():
    """Verify HTML, CSS, and JS visualizer assets exist and are properly structured."""
    assert (STATIC_DIR / "index.html").exists()
    assert (STATIC_DIR / "style.css").exists()
    assert (STATIC_DIR / "app.js").exists()
    assert (STATIC_DIR / "vendor" / "elk-api.js").exists()
    assert (STATIC_DIR / "vendor" / "elk-worker.min.js").exists()
    assert (STATIC_DIR / "vendor" / "ELK-LICENSE.md").exists()

    html = (STATIC_DIR / "index.html").read_text(encoding="utf-8")
    assert "BEP Ownership Mind Map" in html
    assert "mindmap-svg" in html
    assert "details-drawer" in html
    assert "tour-panel" in html

    css = (STATIC_DIR / "style.css").read_text(encoding="utf-8")
    assert "--tier-0-color" in css
    assert "--tier-1-color" in css
    assert "--tier-2-color" in css
    assert "--tier-3-color" in css
    assert "--tier-4-color" in css
    assert ".is-draft" in css

    js = (STATIC_DIR / "app.js").read_text(encoding="utf-8")
    assert "buildHierarchy" in js
    assert "layoutTree" in js
    assert '"elk.algorithm": "radial"' in js
    assert '"elk.radial.centerOnRoot": "true"' in js
    assert '"elk.radial.wedgeCriteria": "NODE_SIZE"' in js
    assert '"elk.direction": "RIGHT"' not in js
    assert "showDrawer" in js
    assert "EventSource" in js


@pytest.fixture
def preview_server(tmp_path: Path, monkeypatch):
    """Start a preview server pointed only at isolated copies of the checked-in maps."""
    canonical = tmp_path / "bep_map.yaml"
    draft = tmp_path / "bep_draft_overlay.yaml"
    shutil.copy2(CANONICAL_PATH, canonical)
    shutil.copy2(DRAFT_PATH, draft)
    monkeypatch.setattr(preview_module, "CANONICAL_PATH", canonical)
    monkeypatch.setattr(preview_module, "DRAFT_PATH", draft)

    server = ThreadingHTTPServer(("127.0.0.1", 0), MindMapRequestHandler)
    host, port = server.server_address
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    base_url = f"http://{host}:{port}"
    yield base_url

    server.shutdown()
    server.server_close()


def test_preview_http_endpoints(preview_server: str):
    """Verify HTTP GET / and static asset delivery."""
    # 1. Index HTML
    with urllib.request.urlopen(f"{preview_server}/") as resp:
        assert resp.status == 200
        content = resp.read().decode("utf-8")
        assert "<title>BEP Ownership Mind Map</title>" in content

    # 2. CSS
    with urllib.request.urlopen(f"{preview_server}/style.css") as resp:
        assert resp.status == 200
        assert "text/css" in resp.headers.get("Content-Type")

    # 3. JS
    with urllib.request.urlopen(f"{preview_server}/app.js") as resp:
        assert resp.status == 200
        assert "javascript" in resp.headers.get("Content-Type")

    with urllib.request.urlopen(f"{preview_server}/vendor/elk-api.js") as resp:
        assert resp.status == 200
        assert "javascript" in resp.headers.get("Content-Type")
        assert "ELK" in resp.read().decode("utf-8")

    with urllib.request.urlopen(f"{preview_server}/vendor/elk-worker.min.js") as resp:
        assert resp.status == 200
        assert "javascript" in resp.headers.get("Content-Type")
        assert len(resp.read()) > 300_000
def test_preview_api_graph(preview_server: str):
    """Verify GET /api/graph returns canonical and merged mind map graphs."""
    with urllib.request.urlopen(f"{preview_server}/api/graph?mode=canonical") as resp:
        assert resp.status == 200
        data = json.loads(resp.read().decode("utf-8"))
        node_ids = {n["id"] for n in data["nodes"]}
        assert "bep" in node_ids
        assert "physics" in node_ids
        assert "mathematics" in node_ids
        assert "systems_control" in node_ids


def test_preview_api_promote(preview_server: str):
    """Verify POST /api/promote is disabled and preserves both isolated YAML files."""
    # First add a draft node to DRAFT_PATH
    test_node_id = "test_preview_dummy_node"
    draft_node = {
        "id": test_node_id,
        "parent": "mathematics",
        "title": "Test Dummy Integrator",
        "tier": 1,
        "importance": 2,
        "rationale": "Implicit backward differentiation formula for test",
        "is_draft": True,
    }
    canonical_ids = {n.id for n in load_map(preview_module.CANONICAL_PATH).nodes}
    add_node(preview_module.DRAFT_PATH, draft_node, is_canonical=False, allowed_external_parents=canonical_ids)
    before = {
        path: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (preview_module.CANONICAL_PATH, preview_module.DRAFT_PATH)
    }

    # Post to /api/promote
    req = urllib.request.Request(
        f"{preview_server}/api/promote",
        data=json.dumps({"id": test_node_id, "new_tier": 2}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with pytest.raises(urllib.error.HTTPError) as err:
        urllib.request.urlopen(req)
    assert err.value.code == 410
    result = json.loads(err.value.read().decode("utf-8"))
    assert "Promotion is disabled" in result["error"]
    assert {
        path: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in (preview_module.CANONICAL_PATH, preview_module.DRAFT_PATH)
    } == before
    assert load_map(preview_module.CANONICAL_PATH).get_node(test_node_id) is None
    assert load_map(preview_module.DRAFT_PATH).get_node(test_node_id) is not None


def test_preview_owner_snapshot_is_read_only_and_separate(preview_server: str, tmp_path: Path, monkeypatch):
    """Owner snapshots use a distinct opt-in mode and never share the AI reference files."""
    owner_map = tmp_path / "owner_snapshot.yaml"
    owner_map.write_text(
        "dataset:\n  role: owner_personal_map\nnodes:\n"
        "  - id: root\n    parent: null\n    title: BEP\n    progress_stage: idea\n    owner_read_status: unread\n"
        "  - id: theme_a\n    parent: root\n    title: Theme A\n    progress_stage: ai_worked_out\n"
        "  - id: theme_b\n    parent: root\n    title: Theme B\n    progress_stage: idea\n"
        "  - id: q_one\n    parent: theme_a\n    title: Question one\n    progress_stage: human_worked_out\n    owner_content_approval: unapproved\n    claims: []\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(preview_module, "OWNER_SNAPSHOT_ENABLED", True)
    monkeypatch.setattr(preview_module, "OWNER_SNAPSHOT_OPTIONS", {"path": owner_map})
    owner_before = hashlib.sha256(owner_map.read_bytes()).hexdigest()

    with urllib.request.urlopen(f"{preview_server}/api/config") as resp:
        config = json.loads(resp.read().decode("utf-8"))
    assert "owner" in config["available_modes"]
    assert config["owner_snapshot_read_only"] is True

    with urllib.request.urlopen(f"{preview_server}/api/graph?mode=owner") as resp:
        graph = json.loads(resp.read().decode("utf-8"))
    assert {node["id"] for node in graph["nodes"]} == {"root", "theme_a", "theme_b", "q_one"}
    assert graph["source"]["role"] == "owner_personal_map"
    assert graph["source"]["read_only"] is True
    assert graph["nodes"][-1]["owner_content_approval"] == "unapproved"

    req = urllib.request.Request(
        f"{preview_server}/api/promote",
        data=json.dumps({"id": "q_one", "new_tier": 2}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with pytest.raises(urllib.error.HTTPError) as err:
        urllib.request.urlopen(req)
    assert err.value.code == 410
    assert hashlib.sha256(owner_map.read_bytes()).hexdigest() == owner_before
