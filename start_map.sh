#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -x ".venv/bin/python" ]; then
  python3 -m venv .venv
  .venv/bin/pip install -q -r requirements.txt
fi

PORT="${BEP_MINDMAP_PORT:-8780}"
echo "Starting BEP Mind Map at http://127.0.0.1:${PORT}/?mode=owner"

exec .venv/bin/python -m mindmap.preview \
  --host 127.0.0.1 \
  --port "$PORT" \
  --owner-map research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml \
  --reference-map research/manual_map_sessions_2026_10_22/owner_working_map/reference_map.yaml \
  --git-root . \
  --no-browser
