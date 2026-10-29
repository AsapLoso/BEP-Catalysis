"""Fail-closed Wayfinder grammar check for the integrated BEP science campaign."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Builds.OpenCode_Harness.core.prompt_spec import WayfinderMap  # noqa: E402

MAP_REL = "Academics/BEP/Catalysis/research/wayfinder/bep_integrated_scientific_campaign_2026_10_22.md"
EXPECTED_ISLANDS = {
    "Catalyst and Kinetics",
    "Conservation, Transport, and Numerical Mathematics",
    "Identification and Control",
    "Independent Evidence Audit",
    "Target-specific project decisions",
}
EXPECTED_TYPES = {"C1": "research", "M1": "research", "S1": "research", "A1": "research"}
STATED_OPEN_TICKETS = 4
EXPECTED_VERIFICATION_CMD = "python Academics/BEP/Catalysis/research/wayfinder/validate_bep_integrated_scientific_campaign_2026_10_22_map.py"
EXPECTED_COMMIT_FILES = [
    "Academics/BEP/Catalysis/research/wayfinder/bep_integrated_scientific_campaign_2026_10_22.md",
    "Academics/BEP/Catalysis/research/wayfinder/bep_integrated_scientific_campaign_2026_10_22_prompts.md",
    "Academics/BEP/Catalysis/research/wayfinder/validate_bep_integrated_scientific_campaign_2026_10_22_map.py",
    "Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/research_backlog.yaml",
    "Academics/BEP/Catalysis/state.md",
    "Academics/BEP/Catalysis/history.log",
    "task.md",
]
EXPECTED_COMMIT_MESSAGE = "Chart BEP integrated scientific research campaign"


def main() -> int:
    map_path = REPO_ROOT / MAP_REL
    if not map_path.exists():
        print(f"FAIL -- map not found: {map_path}")
        return 1
    m = WayfinderMap.from_markdown(map_path.read_text(encoding="utf-8"))
    failures: list[str] = []
    if set(m.islands) != EXPECTED_ISLANDS:
        failures.append(f"islands {sorted(m.islands)} != expected {sorted(EXPECTED_ISLANDS)}")
    open_tickets = [ticket for ticket in m.active_frontier if ticket.status == "open"]
    if len(m.active_frontier) != STATED_OPEN_TICKETS or len(open_tickets) != STATED_OPEN_TICKETS:
        failures.append(f"parsed {len(m.active_frontier)} tickets ({len(open_tickets)} open), expected {STATED_OPEN_TICKETS}")
    by_id: dict[str, list] = {}
    for ticket in m.active_frontier:
        ticket_id = ticket.title.split(" ", 1)[0]
        by_id.setdefault(ticket_id, []).append(ticket)
        if "*" in ticket.title:
            failures.append(f"{ticket_id}: title contains parser-sensitive asterisk")
    duplicates = sorted(ticket_id for ticket_id, entries in by_id.items() if len(entries) > 1)
    if duplicates:
        failures.append(f"duplicate ticket IDs: {duplicates}")
    for ticket_id, expected_type in EXPECTED_TYPES.items():
        entries = by_id.get(ticket_id, [])
        if not entries:
            failures.append(f"ticket missing from parse: {ticket_id}")
            continue
        if entries[0].ticket_type != expected_type:
            failures.append(f"{ticket_id}: parsed type {entries[0].ticket_type!r}, expected {expected_type!r}")
        if not entries[0].question.strip():
            failures.append(f"{ticket_id}: empty question")
    if not m.fog_of_war:
        failures.append("fog of war is empty")
    if not m.out_of_scope:
        failures.append("out-of-scope section is empty")
    if m.verification_cmd != EXPECTED_VERIFICATION_CMD:
        failures.append(f"verification command parsed as {m.verification_cmd!r}")
    if m.scoped_commit_files != EXPECTED_COMMIT_FILES:
        failures.append(f"scoped commit files parsed as {m.scoped_commit_files!r}")
    if m.commit_message != EXPECTED_COMMIT_MESSAGE:
        failures.append(f"commit message parsed as {m.commit_message!r}")
    if failures:
        print(f"FAIL -- {MAP_REL}")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print(f"PASS -- {len(m.active_frontier)} tickets, {len(m.islands)} islands, {len(m.fog_of_war)} fog items; execution contract verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
