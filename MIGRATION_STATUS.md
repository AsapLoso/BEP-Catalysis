# BEP migration provenance and limitations

**Destination:** `AsapLoso/BEP-Catalysis`, private, staging branch `migration/bep-map-consolidation-20261023`.
**Original:** `AsapLoso/project-management-agents`, project subtree `Academics/BEP/Catalysis/`.
**Date:** 2026-10-23.

## Preserved file snapshots

| Dataset / code | Snapshot basis | Destination | Files |
|---|---|---|---:|
| Latest map viewer including Python, JS, tests and local ELK worker | [PR #207](https://github.com/AsapLoso/project-management-agents/pull/207), `7fdf2653e23cc68f5e0d059ef49e454c77b8bedb` | `mindmap/` | 24 |
| Personal map, reviewed/discussion notes, review queue, bridge proposals and rich pages | [PR #186](https://github.com/AsapLoso/project-management-agents/pull/186), `2296d8e0eb9aee94c267df2fde51d4b845ac884d` (inherits #182) | `research/manual_map_sessions_2026_10_22/` | 55 |
| Integrated AI map + citation/evidence audit + binary supplement | [PR #198](https://github.com/AsapLoso/project-management-agents/pull/198), `d7625472fb0c0315d5b9abbc7cf5679cfe59c9ee` (builds on #180) | `research/integrated_reference_map_2026_10_22/` | 34 |
| Independent scientific reference v2 | [PR #175](https://github.com/AsapLoso/project-management-agents/pull/175), `ea391357ad8e4e03cfd27324d4b274513826b254` | `research/independent_reference_map_2026_10_21/` | 11 |
| Independent scientific reference v1 preserved separately | [PR #173](https://github.com/AsapLoso/project-management-agents/pull/173), `e330492418150103a219f49bb7e850ece4aac5b9` | `history/independent-reference-map-v1/` | 11 |
| Reconciliation proposals v1/v2/v3, **not approved taxonomy** | [#177](https://github.com/AsapLoso/project-management-agents/pull/177) / [#196](https://github.com/AsapLoso/project-management-agents/pull/196) / [#197](https://github.com/AsapLoso/project-management-agents/pull/197) | `research/map_comparison_reconciliation*/` | 12 |
| Alternate concurrent frontend/owner-adapter changes, deliberately not merged with #207 | [PR #199](https://github.com/AsapLoso/project-management-agents/pull/199), `5b07f0e98ceebc20f6f217ff0571326f0c3feae7` | `incoming/pr-199/` | 13 |
| Map authoring/review skill, safe Git edits skill, node contract, taxonomy plan and work handoff | AAPM #186 and `devcontainer` | `.agents/skills/`, `research/notes/` | 5 |

**Total source files copied:** 165. Original content is kept in separately named branches/datasets where science or implementation choices conflict. The source's entire Git history is **not** rewritten into this repo.

## Original PRs

- [Full original BEP-related PR register](migration/SOURCE_PRS.md): 69 source PRs from AAPM, with machine-readable original metadata in `SOURCE_PRS.json`.
- Original PR numbers, GitHub review comments, reviewer approvals, branch relationships and original commits **cannot be moved verbatim** by file copy. Those original PR links remain authoritative.
- **Not every PR's historical content was duplicated:** the tables above are the complete copied snapshot scope. Unlisted source branches and non-map research are intentionally not claimed migrated.
- Neither the source PRs nor this new destination's main branch were merged, closed, or approved by this transfer.

## Frontend reconciliation and remaining decisions

- **Implemented in this PR branch:** PR #207 and PR #199 viewer/adapter work is reconciled in the existing app, with the competing source snapshot retained in incoming/pr-199/. The viewer reads evolving owner nodes without hardcoded question names, preserves the five independent stages and per-citation human-verification state, and never writes owner or reference map data.
- **Implemented in this PR branch:** repository-relative imports and preview paths, root runtime requirements, and [Open_BEP_Mind_Map.bat](Open_BEP_Mind_Map.bat) provide the one-click local read-only owner snapshot. The launcher does not fetch Git branches.
- **Verification:** the Python and JavaScript regression suites and the Windows launcher smoke test run in GitHub Actions. The 14 real-browser captures and their report remain linked from [issue #4](https://github.com/AsapLoso/BEP-Catalysis/issues/4); they document the captured viewer states before the latest equal-sector and default tour-placement refinement. Post-refinement browser capture remains a separate verification item if no desktop browser is available.
- Owner review and the migration PR's merge decision remain open. The remaining repository-choice decision for Methanol-Catalysis notebooks is tracked separately in [AAPM PR #212](https://github.com/AsapLoso/project-management-agents/pull/212); notebooks remain linked, not duplicated.
- Never conflate AI reference-map research with owner-approved nodes, nor a successful software test with experimental validation.
