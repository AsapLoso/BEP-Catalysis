"""Fail-closed validator for a Wayfinder map (copy per initiative, then fill TODOs).

Saved by convention as research/wayfinder/validate_<name>_map.py and wired as the
map's Execution Contract verification_cmd:

    pixi run python "research/wayfinder/validate_<name>_map.py"

Exit codes: 0 = PASS, 1 = validation failure, 2 = template not configured.
The validator exists because the map parser fails SILENTLY (drops malformed
or emphasis-carrying titles, downgrades mistyped tickets) -- the count and
type assertions below are the only guard. A map's own stated ticket count is
a hard assertion: stated must equal parsed, fail-closed.
"""

from __future__ import annotations

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[5]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Builds.OpenCode_Harness.core.prompt_spec import WayfinderMap  # noqa: E402

# ---------------------------------------------------------------------------
# TODO(per map): fill ALL of these, then delete this guard block's exit(2).
# ---------------------------------------------------------------------------
MAP_REL = "Academics/BEP/Catalysis/research/wayfinder/bep_reaction_pathway_evidence_2026_10_22.md"
EXPECTED_ISLANDS = {"R1 Semi-hydrogenation", "R2 Ethylene over-hydrogenation", "R3 Acetylene-to-ethane overall conversion"}
EXPECTED_TYPES = {"R1": "research", "R2": "research", "R3": "research"}
STATED_OPEN_TICKETS = 3
EXPECTED_VERIFICATION_CMD = "pixi run python Academics/BEP/Catalysis/research/wayfinder/validate_bep_reaction_pathway_evidence_map.py"
EXPECTED_COMMIT_FILES = [
    "Academics/BEP/Catalysis/research/wayfinder/bep_reaction_pathway_evidence_2026_10_22.md",
    "Academics/BEP/Catalysis/research/wayfinder/validate_bep_reaction_pathway_evidence_map.py",
    "Academics/BEP/Catalysis/research/wayfinder/bep_reaction_pathway_evidence_prompts.md",
    "Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/bridges.yaml",
    "Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/state.md",
]
EXPECTED_COMMIT_MESSAGE = "docs(bep): park R1-R3 source-research ideas in a focused Wayfinder"

if not EXPECTED_TYPES or STATED_OPEN_TICKETS == 0 or not EXPECTED_VERIFICATION_CMD:
    print("FAIL -- template not configured: fill MAP_REL, EXPECTED_ISLANDS,")
    print("        EXPECTED_TYPES, STATED_OPEN_TICKETS and the Execution Contract")
    print("        constants for THIS map, then delete this guard.")
    raise SystemExit(2)


def main() -> int:
    failures: list[str] = []
    map_path = REPO_ROOT / MAP_REL
    if not map_path.exists():
        print(f"FAIL -- map not found: {map_path}")
        return 1
    m = WayfinderMap.from_markdown(map_path.read_text(encoding="utf-8"))

    if set(m.islands) != EXPECTED_ISLANDS:
        failures.append(f"islands {sorted(m.islands)} != expected {sorted(EXPECTED_ISLANDS)}")

    open_tickets = [t for t in m.active_frontier if t.status == "open"]
    if len(m.active_frontier) != STATED_OPEN_TICKETS or len(open_tickets) != STATED_OPEN_TICKETS:
        failures.append(
            f"ticket count drift: parsed {len(m.active_frontier)} frontier tickets "
            f"({len(open_tickets)} open) but the map states {STATED_OPEN_TICKETS}"
        )

    by_id: dict[str, list] = {}
    for t in m.active_frontier:
        tid = t.title.split(" ", 1)[0]
        by_id.setdefault(tid, []).append(t)
        if "*" in t.title:
            failures.append(f"{tid}: title contains '*' (silent-drop regression class): {t.title!r}")
    dupes = sorted(tid for tid, ts in by_id.items() if len(ts) > 1)
    if dupes:
        failures.append(f"duplicate ticket IDs: {dupes}")
    missing = sorted(set(EXPECTED_TYPES) - set(by_id))
    if missing:
        failures.append(f"tickets missing from parse (silently dropped?): {missing}")
    for tid, want in EXPECTED_TYPES.items():
        got = by_id.get(tid, [None])[0]
        if got is None:
            continue  # already reported as missing
        if got.ticket_type != want:
            failures.append(f"{tid}: type parsed as {got.ticket_type!r}, expected {want!r} (type capture voided?)")
        if not got.question.strip():
            failures.append(f"{tid}: empty question")
        elif want == "grilling" and not got.question.strip().endswith("?"):
            failures.append(f"{tid}: grilling question must end with '?' (HITL, never self-answered)")

    if not m.fog_of_war and EXPECTED_TYPES:
        failures.append("fog of war is empty")
    if not m.out_of_scope:
        failures.append("out-of-scope section is empty")

    if m.verification_cmd != EXPECTED_VERIFICATION_CMD:
        failures.append(f"verification_cmd parsed as {m.verification_cmd!r}")
    if m.scoped_commit_files != EXPECTED_COMMIT_FILES:
        failures.append(f"scoped_commit_files parsed as {m.scoped_commit_files!r}")
    if m.commit_message != EXPECTED_COMMIT_MESSAGE:
        failures.append(f"commit_message parsed as {m.commit_message!r}")

    if failures:
        print(f"FAIL -- {MAP_REL}:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(
        f"PASS -- {len(m.active_frontier)}/{STATED_OPEN_TICKETS} tickets parsed, "
        f"{len(m.islands)} islands, {len(m.fog_of_war)} fog items, "
        f"{len(m.out_of_scope)} out-of-scope items; Execution Contract fields verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
