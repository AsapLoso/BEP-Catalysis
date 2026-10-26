"""Live preview web server for BEP Ownership Mind Map.

Serves the interactive visualizer, provides JSON APIs, and watches YAML files for live SSE reload.
"""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import argparse
import json
import os
import threading
import time
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union

try:
    from Academics.BEP.Catalysis.mindmap.editor import load_map
    from Academics.BEP.Catalysis.mindmap.schema import MindMap, merge_maps
    from Academics.BEP.Catalysis.mindmap.owner_map import (
        load_owner_reader_document,
        load_owner_reader_figure,
        load_owner_map_snapshot,
        owner_snapshot_source_available,
    )
except (ImportError, ModuleNotFoundError):
    from editor import load_map
    from schema import MindMap, merge_maps
    from owner_map import (
        load_owner_map_snapshot,
        load_owner_reader_document,
        load_owner_reader_figure,
        owner_snapshot_source_available,
    )

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
DATA_DIR = BASE_DIR / "data"
CANONICAL_PATH = DATA_DIR / "bep_map.yaml"
DRAFT_PATH = DATA_DIR / "bep_draft_overlay.yaml"
REPO_ROOT = BASE_DIR.parents[3]
OWNER_SNAPSHOT_OPTIONS: Dict[str, Any] = {}
OWNER_SNAPSHOT_ENABLED = False


class EventBroadcaster:
    """Manages active SSE client connections and file watching."""

    def __init__(self, data_dir: Path = DATA_DIR, extra_paths: Optional[Set[Path]] = None):
        self.data_dir = data_dir
        self.extra_paths = set(extra_paths or set())
        self.clients: Set[BaseHTTPRequestHandler] = set()
        self.lock = threading.Lock()
        self._running = True
        self._last_mtimes: Dict[Path, float] = {}
        self._watcher_thread = threading.Thread(target=self._watch_loop, daemon=True)

    def register(self, handler: BaseHTTPRequestHandler) -> None:
        with self.lock:
            self.clients.add(handler)

    def unregister(self, handler: BaseHTTPRequestHandler) -> None:
        with self.lock:
            self.clients.discard(handler)

    def broadcast(self, message: str = "reload") -> None:
        with self.lock:
            to_remove = set()
            for handler in self.clients:
                try:
                    payload = f"data: {message}\n\n".encode("utf-8")
                    handler.wfile.write(payload)
                    handler.wfile.flush()
                except Exception:
                    to_remove.add(handler)
            for handler in to_remove:
                self.clients.discard(handler)

    def _get_mtimes(self) -> Dict[Path, float]:
        mtimes = {}
        paths = set(self.data_dir.glob("*.yaml")) if self.data_dir.exists() else set()
        paths.update(self.extra_paths)
        for p in paths:
            try:
                if p.is_file():
                    mtimes[p] = p.stat().st_mtime
            except Exception:
                pass
        return mtimes

    def watch_paths(self, paths: Set[Path]) -> None:
        self.extra_paths.update(Path(path) for path in paths)

    def _watch_loop(self) -> None:
        self._last_mtimes = self._get_mtimes()
        while self._running:
            time.sleep(0.5)
            current = self._get_mtimes()
            changed = False
            for p, mtime in current.items():
                if p not in self._last_mtimes or self._last_mtimes[p] != mtime:
                    changed = True
                    break
            if changed or len(current) != len(self._last_mtimes):
                self._last_mtimes = current
                self.broadcast("reload")

    def start(self) -> None:
        self._watcher_thread.start()

    def stop(self) -> None:
        self._running = False


BROADCASTER = EventBroadcaster()


class MindMapRequestHandler(BaseHTTPRequestHandler):
    """HTTP Request Handler for Mind Map Preview."""

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path in ("/", "/index.html"):
            self._serve_file(STATIC_DIR / "index.html", "text/html; charset=utf-8")
        elif path == "/style.css":
            self._serve_file(STATIC_DIR / "style.css", "text/css; charset=utf-8")
        elif path == "/app.js":
            self._serve_file(STATIC_DIR / "app.js", "application/javascript; charset=utf-8")
        elif path == "/graph-utils.js":
            self._serve_file(STATIC_DIR / "graph-utils.js", "application/javascript; charset=utf-8")
        elif path == "/api/config":
            self._handle_api_config()
        elif path == "/api/graph":
            self._handle_api_graph(parsed.query)
        elif path == "/api/reader":
            self._handle_api_reader(parsed.query)
        elif path == "/api/figure":
            self._handle_api_figure(parsed.query)
        elif path == "/events":
            self._handle_events()
        else:
            self.send_error(404, "Not Found")

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/promote":
            self._handle_api_promote()
        else:
            self.send_error(404, "Not Found")

    def _serve_file(self, file_path: Path, content_type: str) -> None:
        if not file_path.exists():
            self.send_error(404, "File not found")
            return
        data = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def _handle_api_graph(self, query_str: str) -> None:
        query = urllib.parse.parse_qs(query_str)
        mode = query.get("mode", ["merged"])[0]

        try:
            if mode == "owner":
                if not OWNER_SNAPSHOT_ENABLED:
                    self._send_json(
                        {"error": "Owner map snapshot is not configured. Select one explicitly at startup."},
                        status=404,
                    )
                    return
                res = load_owner_map_snapshot(**OWNER_SNAPSHOT_OPTIONS)
            elif mode == "canonical":
                m = load_map(CANONICAL_PATH)
                res = m.model_dump(mode="json")
            elif mode == "draft":
                if DRAFT_PATH.exists():
                    m = load_map(DRAFT_PATH)
                    res = m.model_dump(mode="json")
                else:
                    res = {"nodes": []}
            else:
                # Merged
                can = load_map(CANONICAL_PATH)
                if DRAFT_PATH.exists():
                    drf = load_map(DRAFT_PATH)
                    merged = merge_maps(can, drf)
                    res = merged.model_dump(mode="json")
                else:
                    res = can.model_dump(mode="json")
            if mode != "owner":
                res["source"] = {
                    "role": "ai_reference_map",
                    "status": "local_checkout_snapshot",
                    "authoritative": False,
                    "read_only": True,
                    "label": {
                        "canonical": "AI reference map · canonical file in this checkout",
                        "draft": "AI reference map · draft overlay in this checkout",
                    }.get(mode, "AI reference map · combined local checkout files"),
                }
            res["mode"] = mode
            self._send_json(res)
        except Exception as e:
            self._send_json({"error": str(e)}, status=500)

    def _handle_api_config(self) -> None:
        modes = ["merged", "canonical", "draft"]
        if OWNER_SNAPSHOT_ENABLED:
            modes.append("owner")
        self._send_json({
            "available_modes": modes,
            "owner_snapshot_enabled": OWNER_SNAPSHOT_ENABLED,
            "owner_snapshot_read_only": True,
        })

    def _owner_file_options(self) -> Dict[str, Any]:
        return {
            key: OWNER_SNAPSHOT_OPTIONS[key]
            for key in ("path", "git_ref", "git_path", "git_root")
            if key in OWNER_SNAPSHOT_OPTIONS
        }

    def _handle_api_reader(self, query_str: str) -> None:
        if not OWNER_SNAPSHOT_ENABLED:
            self._send_json({"error": "Owner map snapshot is not configured."}, status=404, cors=False)
            return
        query = urllib.parse.parse_qs(query_str)
        node_id = query.get("node_id", [""])[0]
        if not node_id:
            self._send_json({"error": "A node_id is required."}, status=400, cors=False)
            return
        try:
            background_raw = query.get("background_index", [None])[0]
            background_index = int(background_raw) if background_raw is not None else None
            asset = load_owner_reader_document(
                node_id=node_id,
                background_index=background_index,
                **self._owner_file_options(),
            )
        except FileNotFoundError as exc:
            self._send_json({"error": str(exc)}, status=404, cors=False)
            return
        except (TypeError, ValueError) as exc:
            self._send_json({"error": str(exc)}, status=400, cors=False)
            return
        except Exception as exc:
            self._send_json({"error": f"Could not read linked owner file: {exc}"}, status=500, cors=False)
            return

        if query.get("raw", ["0"])[0] == "1":
            content_type = "text/markdown; charset=utf-8" if background_index is None else "text/plain; charset=utf-8"
            self._send_bytes(asset["content"].encode("utf-8"), content_type, asset["file_name"])
            return
        asset.pop("_resolved_path", None)
        self._send_json(asset, cors=False)

    def _handle_api_figure(self, query_str: str) -> None:
        if not OWNER_SNAPSHOT_ENABLED:
            self._send_json({"error": "Owner map snapshot is not configured."}, status=404, cors=False)
            return
        query = urllib.parse.parse_qs(query_str)
        node_id = query.get("node_id", [""])[0]
        relative_path = query.get("path", [""])[0]
        if not node_id or not relative_path:
            self._send_json({"error": "A node_id and relative path are required."}, status=400, cors=False)
            return
        try:
            figure = load_owner_reader_figure(
                node_id=node_id,
                relative_path=relative_path,
                **self._owner_file_options(),
            )
        except FileNotFoundError:
            self._send_json({"error": "Figure is not available in the selected owner snapshot."}, status=404, cors=False)
            return
        except (TypeError, ValueError):
            self._send_json({"error": "Figure path or format is not supported."}, status=400, cors=False)
            return
        except Exception:
            self._send_json({"error": "Could not read figure from the selected owner snapshot."}, status=500, cors=False)
            return
        self._send_bytes(figure["content"], figure["content_type"], Path(figure["path"]).name)

    def _send_bytes(self, data: bytes, content_type: str, file_name: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Content-Disposition", f"inline; filename*=UTF-8''{urllib.parse.quote(file_name)}")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, payload: Dict[str, Any], status: int = 200, *, cors: bool = True) -> None:
        data = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        if cors:
            self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def _handle_api_promote(self) -> None:
        self._send_json({
            "error": (
                "Promotion is disabled. Moving a node between maps requires a separately recorded, "
                "scoped owner decision; placement must not imply human understanding or citation verification."
            )
        }, status=410)

    def _handle_events(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Send initial ping
        self.wfile.write(b": connected\n\n")
        self.wfile.flush()

        BROADCASTER.register(self)
        try:
            while True:
                time.sleep(15)
                # Keepalive heartbeat
                self.wfile.write(b": heartbeat\n\n")
                self.wfile.flush()
        except Exception:
            pass
        finally:
            BROADCASTER.unregister(self)

    def log_message(self, format: str, *args) -> None:
        # Suppress noisy SSE logging
        if "/events" not in self.path:
            super().log_message(format, *args)


def run_server(
    host: str = "127.0.0.1",
    port: int = 8765,
    open_browser: bool = False,
    owner_map_path: Optional[Path] = None,
    owner_map_ref: Optional[str] = None,
    owner_map_git_path: Optional[str] = None,
    reference_map_path: Optional[Path] = None,
    reference_map_ref: Optional[str] = None,
    reference_map_git_path: Optional[str] = None,
    git_root: Path = REPO_ROOT,
) -> None:
    global OWNER_SNAPSHOT_OPTIONS, OWNER_SNAPSHOT_ENABLED
    if reference_map_path is not None and (reference_map_ref is not None or reference_map_git_path is not None):
        raise ValueError("Choose a local reference-map path or a local Git ref and path, not both.")
    if (reference_map_ref is None) != (reference_map_git_path is None):
        raise ValueError("A reference-map Git snapshot requires both --reference-map-ref and --reference-map-git-path.")
    OWNER_SNAPSHOT_ENABLED = owner_snapshot_source_available(
        path=owner_map_path,
        git_ref=owner_map_ref,
        git_path=owner_map_git_path,
    )
    if not OWNER_SNAPSHOT_ENABLED and any((reference_map_path, reference_map_ref, reference_map_git_path)):
        raise ValueError("A reference map can only be loaded alongside an explicit owner-map snapshot.")
    OWNER_SNAPSHOT_OPTIONS = {
        "path": owner_map_path,
        "git_ref": owner_map_ref,
        "git_path": owner_map_git_path,
        "git_root": git_root,
        "reference_path": reference_map_path,
        "reference_git_ref": reference_map_ref,
        "reference_git_path": reference_map_git_path,
    }
    if OWNER_SNAPSHOT_ENABLED:
        # Fail at startup for stale or invalid local refs instead of silently
        # presenting an empty/partial owner map in the browser.
        load_owner_map_snapshot(**OWNER_SNAPSHOT_OPTIONS)
    watched_paths: Set[Path] = set()
    if owner_map_path is not None:
        watched_paths.add(Path(owner_map_path))
    if reference_map_path is not None:
        watched_paths.add(Path(reference_map_path))
    BROADCASTER.watch_paths(watched_paths)
    BROADCASTER.start()
    server = ThreadingHTTPServer((host, port), MindMapRequestHandler)
    url = f"http://{host}:{port}/"
    print(f"[preview] BEP Mind Map server running at {url}")
    if open_browser:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[preview] Stopping server...")
    finally:
        BROADCASTER.stop()
        server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description="BEP Mind Map Live Preview Server")
    parser.add_argument("--host", default="127.0.0.1", help="Server host")
    parser.add_argument("--port", type=int, default=8765, help="Server port")
    parser.add_argument("--no-browser", action="store_true", help="Do not open browser automatically")
    parser.add_argument("--owner-map", type=Path, help="Explicit local owner-map snapshot path (read-only)")
    parser.add_argument("--owner-map-ref", help="Explicit already-fetched local Git ref for the owner map")
    parser.add_argument("--owner-map-git-path", help="Repository-relative owner-map file path used with --owner-map-ref")
    parser.add_argument("--reference-map", type=Path, help="Optional local AI reference map or manifest snapshot")
    parser.add_argument("--reference-map-ref", help="Optional already-fetched local Git ref for the reference map manifest or file")
    parser.add_argument("--reference-map-git-path", help="Repository-relative manifest/file path used with --reference-map-ref")
    parser.add_argument("--git-root", type=Path, default=REPO_ROOT, help="Local repository root for Git-ref snapshots")
    args = parser.parse_args()

    run_server(
        host=args.host,
        port=args.port,
        open_browser=not args.no_browser,
        owner_map_path=args.owner_map,
        owner_map_ref=args.owner_map_ref,
        owner_map_git_path=args.owner_map_git_path,
        reference_map_path=args.reference_map,
        reference_map_ref=args.reference_map_ref,
        reference_map_git_path=args.reference_map_git_path,
        git_root=args.git_root,
    )


if __name__ == "__main__":
    main()
