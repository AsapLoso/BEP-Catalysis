# Goal — Complete existing BEP mind-map viewer for a continuously evolving personal scientific map

**Mission date:** 2026-10-22. **Mission type:** targeted software implementation, backend compatibility, data-safety tests and frontend finishing work. This is **not** a science-research mission, a new mind-map prototype, or a request to populate/approve the owner's scientific graph.

## Git/repository setup

- Repository: `AsapLoso/project-management-agents`
- **Exact code starting and PR target branch:** `devcontainer` (the existing mind-map implementation).
- Create a fresh scoped feature branch off latest `devcontainer`. Do not use or overwrite any other worker's topic branch, uncommitted changes or scientific dataset.
- The **authoritative instructions for owner-led map semantics** live **on a different, unmerged docs branch**: `docs/bep-theme-first-progress-units-20261022`, in `Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/`. You must fetch these files explicitly by their named ref rather than assuming they exist on `devcontainer`.
- Open a reviewable PR against `devcontainer`. The owner permits immediate merge of a *properly scoped and fully validated* PR, **only after diff review, required checks and current branch-protection constraints are satisfied**. Do not merge incomplete, lossy, unsafe or conflicted changes. Preserve separately reversible commits where applicable.

## Read first (in order)

1. `Academics/BEP/Catalysis/mindmap/README.md`, `schema.py`, `editor.py`, `mcp_server.py`, `preview.py`, `static/` and `tests/`, **on `devcontainer`**. This is an existing Python/YAML/HTML/JS graph application; **enhance it in place**. Investigate actual implementation and test behavior before editing.
2. `.agents/skills/bep-map-edit-review/SKILL.md` and `.agents/skills/reversible-change-review/SKILL.md`; project `conventions.md` §13; `research/notes/bep_mindmap_node_contract_2026_10_20.md`.
3. On docs ref `docs/bep-theme-first-progress-units-20261022`: `research/manual_map_sessions_2026_10_22/README.md`, `SESSION_STATE.md`, `owner_working_map/state.md`, `owner_working_map/THEME_FIRST_PROGRESS_UNITS_2026_10_22.md` and `owner_working_map/NODE_TEMPLATE.yaml`.
4. Read `owner_working_map/current_map.yaml` and `reference_map.yaml` **without modifying them**; `current_map.yaml` has JSON-shaped content despite its extension. The eight-node graph is a *historical implementation snapshot*. Read the node data as-is; **do not claim the revised graph has already been created**.
5. `Academics/BEP/Catalysis/research/notes/bep_mindmap_ui_wishlist_2026_10_20.md` on `devcontainer`. Check what the current JS canvas already supports, including focus/root-path mode, before rewriting anything.

## Current design decision and no-blocker principle

The owner and another ChatGPT session are **actively authoring the personal BEP scientific map**. Your frontend must be usable **while that dataset changes**; the map content does not need to be completed before interface development.

The latest user decision is to keep **two real scientific investigative themes, not invent a third**:

```
BEP
 └─ Physics
    └─ Reaction Chemistry & Pathways
       └─ Our Reactions                    (R1, R2, R3 explained inside this node)
          ├─ Microscopic pathways
          │  ├─ R1
          │  ├─ R2
          │  └─ R3
          └─ Viability & conditions
             ├─ R1
             ├─ R2
             └─ R3
```

These are **six potentially independently progressing research-question nodes**, not nine or a mandatory limit of six. If the owner continues to add or reparent nodes, the application must display the resulting hierarchy without hardcoded path, title, depth or node count. Mathematics and Systems & Control remain the other two first-level arms. The above tree is a **frontend fixture / design target only**, not permission to update the personal `current_map.yaml`.

**Core authoring principle:** Nodes represent *independently trackable scientific questions*, while claims, equations, quotations, source links, assumptions and detailed explanations live *inside* nodes. Two R3/R1 questions can have different progress states.

## Required implementation

### A. Non-lossy data and ownership contract — address before enabling edits

- Identify how the existing editor, schema and preview currently parse/serialize data. Pydantic currently uses `extra="ignore"`: unknown rich-node keys can vanish during round-trips. Implement a **lossless, validated adapter/schema** for the owner-working map and supporting reference links. Test using actual representative data and scratch fixtures. Keep unknown/existing fields safe; no global scientific-data rewrite.
- Keep **AI reference map** distinct from **owner personal map**, including provenance and status. Provide an explicit user-selectable or clearly labelled view mode; do not silently synthesize, auto-approve, or overwrite either graph.
- Preserve stable node IDs, exactly one parent per node (except root), connectedness/acyclicity, cross-map references, written scientific notes, source locators, claim IDs, user annotations and history.
- Support **five concept/writing stages**: `idea`, `ai_worked_out`, `human_worked_out`, `informal_writing`, `formal_writing`. Keep independent `structural_approval`, `owner_read_status`, `owner_content_approval` and per-claim `ai_attached` versus `human_verified`. The existing old integer `tier` values require a documented, backward-compatible mapping or read-only legacy treatment. **Never equate inserting/approving a node with the owner's personal scientific understanding.**
- Fix or safely disable the legacy `/api/promote` and tour/promote buttons that currently default to `new_tier=2` when approval is clicked. Explicit review and provenance are required for human status; AI evidence never promotes human citation verification. If secure editing is beyond scope, make those actions **read-only/disabled with clear explanation**, not silently unsafe.
- Treat `NODE_TEMPLATE.yaml` as a **semantic proposal**; it currently lists three scientific maturity labels in places while the newer five-stage writing contract is in the owner decision notes. Reconcile representation **without inventing science, owner approvals, or unknown evidence**. Define and test migration carefully; preserve original values and record conversions.
- Make the owner dataset configurable by explicit path/ref/fixture. Since it may not exist on the code branch, default to the existing functioning app data, add an opt-in safe owner-map loader/adapter, and clearly distinguish **preview loaded from snapshot** versus **live authoritative owner data**. Do **not** claim cross-branch GitHub updates are instantly live without actually implementing them.

### B. Scientific details and citations

- Clicking a node opens a useful details view: its question, progress, notes, rendered equations, claims, assumptions/limitations, open questions, source citations, and review status.
- Display claim-to-source provenance as far as data permits: `owner node → AI reference node/claim → source record → passage locator and brief quotation`. Resolve stable IDs when records are available. Clearly show absent/uninspected excerpts or unresolved claim matches; **never invent quotes or mark as human-verified**.
- Allow linked related nodes/shared evidence without duplicating physical scientific assertions.
- Handle rich or missing data gracefully; no crashes, silent truncation or citation overclaim.

### C. Existing SVG frontend finishing pass

- **Retain the existing viewer** and its generally liked aesthetics; no parallel mock app. Preserve the three first-level **scientific** arms. A–M dossiers and administrative material must not masquerade as fourth/fifth scientific root branches; do not delete their data, provide reference navigation or filtering instead.
- Make **Overview** usable with head-arm separation, responsive fit/spacing and progressive disclosure. Improve existing focus/path mode (connected SVG nodes, root-to-selected ancestry plus immediate children), preserve user selection and navigation across data reloads.
- Navigation must support rapid scientific speedruns: select next sibling/question, read what is known, see `Idea` vs worked-out status, inspect original reference links, and return to the parent without searching through an unreadable giant canvas.
- Avoid hardcoded number of themes/children. Focus on reader usability and reliable data semantics over decorative animation.

### D. Tests, documentation and deliverable

- Test schema round-trip **including every rich owner field**, absent citations, multiple stages, mixed current/legacy records, six-question fixture and an additional arbitrary-depth branch. Verify no lost IDs, sources, notes, approvals or unknown metadata.
- Regression-test owner/AI map isolation, paths/links, graph hierarchy, cycles, focus navigation, safe handling/disablement of promotion API, and exact preservation of human verification statuses.
- Use isolated/test copies and ensure no test mutates the live reference or owner scientific YAML. Run existing tests plus added targeted tests; state any runtime/browser tests that could not actually run.
- Update `mindmap/README.md` and any relevant map skill/contract alongside code changes, explaining safe startup with working owner snapshots and how ongoing separate map branches get loaded. Include a simple example/run command and inspectable screenshots if a browser runtime is available.
- Produce logically scoped commits, a PR with source/diff/verification receipts and a clear list of *what is implemented*, *what needs owner decisions*, and *what only works with local runtime or explicit data syncing*.

## Explicit boundaries

- **Do not edit** the live personal map, reference science sources, old AI research nodes, R1–R3 Wayfinder tickets or human-approval statuses to make UI demonstrations pass. Use fixtures/scratch snapshots.
- **Do not** expand scientific taxonomy or research chemistry in this Work mission; another session owns that work.
- **Do not** wait for the owner to finish defining more themes, or for the source-passage audit, before beginning implementation. The app must be robust to continued backend science development.
- **Do not** assume local desktop runtime or OneDrive state equals GitHub; inspect existing code first, use accessible environment, flag missing browser/runtime verification truthfully.
- **Do not** demand an invented third theme or an already-migrated six-node tree before starting.

**Success criterion:** The existing BEP mind-map application safely renders an evolving personal question/progress graph and linked AI scientific citations, without discarding rich node fields or wrongly converting AI material or owner placement into human-understood or human-verified statuses. The separate scientific-map session can keep working in parallel from GitHub.
