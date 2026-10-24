# Proposed repository structure — incremental, review-gated

## Recommendation

Adopt the proposed separation as a destination model, but migrate incrementally. Keep the archive immutable and keep scientific data changes outside this extraction PR. Add aliases and adapters before moving any live path; do not run a folder-rename sweep.

| Area | Role | Current evidence and move guidance |
|---|---|---|
| `planning/source-snapshots/` | Immutable inputs with pinned refs, blobs, and redaction metadata. | Already exists on archive PR #2 with 119 verified snapshots. Keep it unchanged; add future source records append-only. |
| `planning/backlog/` | Lossless occurrences, grouped review index, conflicts, and validation. | Added by this PR. Keep raw records separate from normalized clusters and owner-promoted roadmaps. |
| `planning/roadmaps/` | Reviewed summaries and current owner-approved project roadmap. | Create only after owner review of clusters and status conflicts. Link to specialist plans; do not paste all subtasks into a master checklist. |
| `research/owner-map/` | Owner-understanding map and owner-authored/approved content. | PR #1 already contains `research/manual_map_sessions_.../owner_working_map/` and `mindmap/`. Preserve paths initially; introduce a read-only alias or manifest before any move. |
| `research/ai-reference/` | AI research, evidence ledgers, hypotheses, and unverified claims. | PR #1 contains independent/integrated reference maps and source evidence under dated paths. Keep separate from the owner map; do not promote a proposal map to owner knowledge. |
| `mindmap/` | Application, adapters, tests, viewer, and export. | Existing PR #1 root `mindmap/` is the application. Keep its current path; use compatibility adapters for older AAPM package imports and links before relocating anything. Frontend reconciliation is a separate future PR. |
| `model/` | Maintained model implementation, parameter conventions, solver assumptions, validation record. | Preserve current `3_Model/` and notebook paths during discovery. Add a manifest/adapter first; move only after ownership and import paths are agreed. |
| `notebooks/` | Reproducible notebooks and notebook ownership/recovery notes. | PR #1 and PR #212 evidence show notebook workspace activity. Do not inventory or relocate notebooks as part of this task; first identify source, owner, and dependencies. |
| `supervision/` | Supervisor questions, owner-reviewed messages, meeting notes, and submission handoffs. | Keep communications and approval state separate from science maps. Nothing is sent as part of this work. |
| `thesis/` | Thesis narrative, presentation, and writing deliverables. | Preserve existing presentation/thesis artifacts; use references from a reviewed roadmap rather than copying task history. |
| `administration/` | Forms, committee, signatures, and institutional deadlines. | Keep form/committee actions distinct from model tasks and scientific verification. Do not infer dates from stale checklists. |

## Incremental move sequence

1. Merge the archive PR only through its existing review; preserve the 119 snapshot blob hashes. This task does not merge it.
2. Review the occurrence ledger and conflicts. Select confirmed current items and record owner decisions in a new roadmap without rewriting the source snapshots.
3. Keep PR #1's current `research/` and `mindmap/` locations. Add `README` aliases or adapters that map these to the intended owner-map, AI-reference, and frontend concepts.
4. Make one destination move at a time, with path compatibility, source refs, and a clean diff. Keep a rollback path and validate link/import users before retiring an alias.
5. Promote only explicitly reviewed summaries; leave the raw backlog append-only.

## Alternatives and constraints

A wholesale move now would break imports, links, and traceability while the archive and map migration PRs remain separate. Keeping all research under one tree is simpler for the current branch but risks mixing owner understanding with AI hypotheses. The proposed separation addresses that risk without requiring immediate file movement.

No `current_map.yaml`, AI reference graph, source science, notebook, frontend code, or supervisor text was changed for this proposal.
