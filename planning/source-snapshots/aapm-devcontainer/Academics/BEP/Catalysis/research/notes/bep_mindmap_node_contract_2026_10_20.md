# BEP Mind Map — portable node contract and discussion-writing protocol

**2026-10-20 · Canonical for the format of future map discussions; document-only design decision, not approval to mutate scientific graph nodes.**  
**Read first after compaction:** [the taxonomy's START HERE checklist](bep_ownership_mindmap_taxonomy_2026_10_20.md#start-here--concrete-execution-checklist-2026-10-20). Use this node contract alongside the checklist.  
**Project:** Acetylene semi-hydrogenation BEP; tree is scientific knowledge/ownership, **not** a Wayfinder decision map or A–M slide outline.

The later `FRONTEND_WORK_GOAL_2026_10_22.md` specifically authorized software/schema/test/documentation changes. That authorization does not permit changing the live personal map, scientific claims, citations or owner-approval records.

## 2026-10-22 implementation addendum — current owner-map contract

The earlier sections below record the 2026-10-20 design baseline and must not be mistaken for today's graph. The owner has since chosen **two research themes** and **six independently trackable R1/R2/R3 questions**. That structure is a UI regression fixture, not a hard-coded limit or proof that a revised personal graph has been created. New nodes, parent paths and depths must remain data-driven.

Use five concept/writing stages: `idea`, `ai_worked_out`, `human_worked_out`, `informal_writing`, and `formal_writing`. Keep `structural_approval`, `owner_read_status`, `owner_content_approval`, AI-attached evidence, and per-claim/source `human_verified` separate. The existing viewer accepts the personal graph only as an explicit, read-only local file or already-fetched Git snapshot. It does not fetch GitHub or write either map. The AI reference graph stays separate; its `claim_refs` and source records may be resolved for navigation, but AI support summaries are not quotations or human-verified citations.

Historical integer tiers remain readable as legacy data and are never converted into owner progress or approval. Promotion is disabled at the HTTP, editor, MCP and tour surfaces. Unknown rich fields and nested metadata must survive adapter and legacy-editor round trips.

## 0. What exists NOW (verified from GitHub, not executed locally)

An **actual application already exists** in [`Academics/BEP/Catalysis/mindmap/`](../../mindmap/), on `devcontainer` as inspected 2026-10-20:

- `schema.py`: Pydantic `MindMapNode`, `SourceItem`, graph/canonical validation.
- `editor.py`: read/save YAML, atomic writes, add/edit/reparent/delete, source attach, draft-to-canonical promotion.
- `mcp_server.py`: local stdio MCP tools; `preview.py` and `static/`: HTTP browser/JSON API/SSE live reload; `tests/`: tests **exist** (not executed in this chat).
- `data/bep_map.yaml`: **4 canonical records** — `bep`, `physics`, `mathematics`, `systems_control`; root currently stores `tier: 2`. This proves the *file* exists, not owner science validation.
- `data/bep_draft_overlay.yaml`: **69 AI-draft records after C1/C2 science-data passes (21 Oct)**: the previous 33 nodes are preserved; **28 deep C1 chemistry descendants plus 8 C2 kinetics/closure nodes** (all AI reference tier 0/1) were added beneath the two important C1 children. Detailed receipt is in the [taxonomy](bep_ownership_mindmap_taxonomy_2026_10_20.md#2026-10-21--c1-backend-scientific-data-pass-ai-generated-not-owner-reviewed). Previous baseline: 15 original researched draft concepts, 15 proposed Level-2 themes, one PDC course-support node, and **two first-child C1 branches** (`c1_reaction_chemistry_pathways`, `c1_catalyst_active_site_chemistry`). Eleven older concepts were reparented within the draft overlay earlier. C1 parent has AI-worked-out research notes; both new children are Idea. **No scientific claim or citation has been human-verified by these edits.**
- The **actual local checkout, local unpushed commits, runtime health and current test results remain UNVERIFIED**. Always inspect before code changes; don't destroy or replace existing work. The earlier statement "implementation not found/not started" is outdated for the GitHub snapshot.

**Historical implementation mismatches observed before the 2026-10-22 retrofit:**
1. Legacy `tier: 0..4` conflated progress labels and owner approval; it is now read-only and the five explicit stages above carry progress.
2. Legacy `SourceItem` had no claim-specific owner verification; the adapter now retains claim links and displays source/link verification independently.
3. `promote_draft_node(..., new_tier=2)` and browser `/api/promote` previously implied owner understanding. They now refuse promotion without mutating files.
4. The old `extra="ignore"` configuration could drop new YAML fields. Legacy editor models now allow unknown fields, and the owner adapter validates its core contract while retaining extra metadata.
5. AI-reference and personal maps remain separate; the owner-map frontend view reads only an explicit snapshot and makes no map edits. Do not promote themes or old researched overlay entries into `bep_map.yaml` without topic-specific owner approval.

## 1. The one-node record (portable semantic contract)

**One record = one independently understandable concept**, *not* an entire letter's contents in one blob. A deep sub-note is another record. For discussion and later migration use YAML syntax with explicit keys, even when embedded as a fenced block in Markdown. Retain existing stable IDs wherever a concept corresponds to an existing node; new IDs must not be derived from the node's mutable full path.

### Fields

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | stable string | Unique immutable identity. Keep existing IDs during migration. Never rename ID when reparenting or retitling |
| `parent` | ID or null | Exactly one immediate parent, root alone null. **Depth computed from ancestry**, not hard-coded |
| `title` | string | Short display label |
| `kind` | enum, suggested | `discipline / theme / subject / letter / concept / detail` for UI/search; does not supersede parent relation |
| `progress_stage` | enum | `idea / ai_worked_out / human_worked_out / informal_writing / formal_writing` — concept/writing stage, independent of review |
| `structural_approval` | status | Whether this node's structure or placement was accepted; independent of progress and source verification |
| `owner_read_status` | status | Whether the owner has read/reviewed the node's content; never inferred from placement or a commit |
| `owner_content_approval` | status | Whether the owner approved the content; independent from structural approval |
| `importance` | null or 0–3 | Optional importance stars, **not confidence or proof** |
| `rationale` | string | Why the node belongs relative to its parent |
| `notes` | long Markdown string | Substantive explanation, equations, assumptions, caveats; long text welcome |
| `open_questions` | list of strings | What remains unresolved |
| `claims` | list of objects | Bounded statements with stable IDs and separately linked AI/reference evidence |
| `sources` | list of objects | Traceable references, passage locator, access bounds and independent `human_verified` status |
| `related_ids` | list of IDs | Cross-discipline links *without* duplicate scientific content |
| `research_letters` | list (e.g. `[D]`) | Link to existing A–M dossier(s), not necessarily a letter-as-parent rule |
| `origin` | optional | `owner_statement / ai_synthesis / paper / experiment / code / proposal` or equivalent provenance |

**Suggested source-object fields:** `id`, `title`, `path` or `url` or `doi`, optional `citation`, `locator` (page/section/equation/cell), `supports` (the bounded claim or AI evidence summary), `review` / `human_verified` as separate fields. **No URL/DOI or quotation fabrication.** A course/archive being relevant is *not* evidence that it supports a specific reactor claim.

**No "human-verified by default" shortcuts.** `human_worked_out` requires owner review of actual contents. `human_verified` requires owner review of a particular cited passage/data point and the connection to a particular claim. Accepting a node's position qualifies only `approval: accepted`.

### Parser-friendly example: ONE PROPOSAL, NOT LIVE GRAPH DATA

The following corresponds to the real PDC course but is intentionally only a **proposed** knowledge node. Its proposed parent is a Level-2 theme not yet approved/created, so it MUST NOT be inserted into live YAML until that parent exists and the specific edit is authorized.

```yaml
id: pdc_process_dynamics_foundations
parent: system_modelling_reduction
title: "PDC — Process Dynamics foundations"
kind: subject
maturity: ai_worked_out
approval: proposed
importance: null
rationale: >-
  Course-based control engineering background relevant to reactor system
  modelling, but not itself evidence that a specific reactor result is valid.
notes: |-
  Process Dynamics & Control (PDC) is archived under the BEP as course
  support. Relevant fundamentals include dynamic process modelling,
  linearisation, transfer functions, time-delay and step-response modelling.
  Its SISO control examples include PID, feedforward, IMC and Smith predictor.
  Distinguish an educational analogue from a validated packed-bed model.
open_questions:
  - "Which course concepts belong in the BEP tree, and which are only background?"
sources:
  - title: "PDC course overview (harvest analysis)"
    path: "Academics/BEP/Catalysis/2_Courses/PDC/course_overview.md"
    locator: "Sections 1–4"
    supports: "PDC course scope and archived example topics, not reactor-specific evidence"
    review: ai_attached
related_ids: []
research_letters: []
origin: ai_synthesis
```

**Existing implementation's serialization:** the legacy AI-reference files use a top-level `nodes: [ ... ]` YAML collection. The owner adapter consumes a separate `nodes` collection as a read-only snapshot, preserving rich fields and unknown metadata; it does not merge or copy the personal graph into `bep_map.yaml`. Keep owner and AI reference sources separate. The current `bep_draft_overlay.yaml` remains a **separate existing backlog**, not a trash bin or a generated copy of any proposed hierarchy.

## 2. Historical levels and the letter rule

The examples in this section record an older taxonomy discussion. They are not a current personal-map snapshot, a required node count, or the latest theme decision. The owner-map software must follow whichever valid parent paths its explicitly selected snapshot contains.

- **Level 0:** root `bep`.
- **Level 1:** `physics`, `mathematics`, `systems_control` (fixed decisions).
- **Historical proposal only:** 15 AI-proposed themes (**C1–C15**) appeared in an earlier taxonomy checklist. The latest owner decision is two research themes with independently trackable R1/R2/R3 questions; do not create the 15-node proposal as a personal-map hierarchy.
- **Level 3 and beyond:** relevant subjects, branches and A–M letter anchors wherever they fit; **a letter is NOT required at Level 3**, and may follow intermediate concepts. Some letters are cross-cutting references rather than compulsory buckets.
- **Unlimited deeper levels:** Level 6 was *only illustrative*. Levels 7, 8, 9+ are welcome; no graph-depth maximum should be imposed by validators, visualizer, schema or authoring workflow. Compute depth from the recursive `parent` chain. The 39 A–M L4/L5/L6 checklist items are **review passes / minimum coverage reminders**, not a prescribed leaf depth or a complete list of required sub-nodes.
- **Historical C1 decision receipt:** the older taxonomy recorded `physics_catalytic_chemistry` with two first-child branches. Preserve that as prior context only; it does not override the latest two-theme decision or establish that a revised personal map has been authored. Never mark downstream science personally understood from this receipt.

**Do not force every node to have a letter.** E.g. PDC foundations, filtering, or experimental instrumentation may exist as normal Level-3 subjects with their own children.

## 3. How to write down EVERY conversation step so another AI can read it

Use a compact and append-friendly **proposal/decision transaction**, not an unstructured paraphrase. In the canonical taxonomy document, under the active checkpoint, record:

```yaml
checkpoint: C11
date: "2026-10-20"
action: propose  # propose | accept | revise | reject | defer
node_id: system_modelling_reduction
parent_id: systems_control
proposed_title: "System Modelling & Reduction"
discussion_summary: "Broad subject; PDC dynamics would be a descendant or cross-link."
user_decision: null       # exact accepted correction / approval if given
evidence_paths:
  - "Academics/BEP/Catalysis/0_Project_Management/main.tex"
scientific_maturity: idea  # never upgraded based on a structural approval
graph_mutation: none       # none | approved_draft | approved_canonical
```

**Every follow-up note must identify**: `checkpoint`, exact node IDs, parent IDs, `action`, what changed, user authority, whether any actual YAML/PR was touched, and next checkpoint. Only advance/tick a checklist box when the owner has decided the topic boundary or a verified implementation receipt exists. Do not infer owner approval from silence or from an AI-generated detailed dossier.

After each material step update **three locations coherently**:
1. **Taxonomy / checklist:** C1–C15 or letter L4/L5/L6 + brief decision receipt; a current cursor.
2. **Structured node proposal(s)** as above in the dossier/approved graph when authorized; preserve stable IDs, parent and evidence status.
3. **BEP state / root task** only for major stage/status changes (avoid echoing every scientific sub-node), and append `history.log` only for meaningful decisions/commits.

**Single writer** for edits to a given YAML. Validate against the current schema, detect duplicate IDs, missing parents, or cycles; diff before approving mutation. Never infer write authority just because a change appears in a conversational draft.

## 4. PDC — core reference, not yet a Level-2 category

**PDC = Process Dynamics & Control**, archived in [`2_Courses/PDC/`](../../2_Courses/PDC/); [course overview](../../2_Courses/PDC/course_overview.md) and [resources](../../2_Courses/PDC/resources.md).

The *archived course overview* lists:
- **Part 1: Process Dynamics**, Modules 1–4: introduction to processes; dynamic modelling/transport; linearisation/Laplace/transfer functions; PFD/P&ID and instrumentation.
- **Part 2: Process Control**, Modules 5–7: SISO control; MIMO control; optional process optimization. The harvested **eleven notebooks cover SISO Module 5**, not evidence that Modules 6–7 were taught/archived in that corpus. Specific notebook subjects include PID, step response/FOPTD, dead-time compensation, IMC, feedforward and nonlinear CSTR controller comparison.
- **Relevance**: PDC is a natural course/reference umbrella for S&C `System Modelling & Reduction`, `System Identification`, and `Control & Performance Optimization`; and for Mathematics `Dynamical Systems & Stability`. **Propose a PDC-linked Level-3 subject/cross-links**, do **not add a sixteenth Level-2 theme automatically**.
- PDC cannot by itself establish statements about the real BEP catalyst, exact reactor physics, thermal runaway bounds, or a successful control experiment. Treat its course-derived sources as **AI-attached** pending claim-specific human review. Some existing mind-map draft nodes cite PDC rather broadly; reconcile claims before promotion.

## 5. Required retrofit audit and acceptance gates (do not code until instruction)

- [ ] Confirm local worktree and whether unpushed changes supersede GitHub version of `mindmap/`.
- [ ] Extract/verify actual old `tier` meanings and **migrate without claiming owner understanding**. Keep existing stable IDs and the root/three fixed arms.
- [ ] Add `approval` independent of `maturity`; remove promotion's implicit `new_tier=2` claim. Maintain AI overlay vs accepted canonical.
- [ ] Add source `review` status + locator/supported claim; retain existing `doi/path/citation/section`, don't silently drop fields (`extra="ignore"` risk).
- [ ] Validate every added/reparented node; protect against duplicate IDs, missing parents, cycles, unknown fields and unintended cascading deletion.
- [ ] Ensure read-only map navigation and any editor authorization are clearly separated; validate actual `/api/promote` behaviour and approval model.
- [ ] Preserve existing app/tests and check tests, `pixi run preview` and live SSE refresh in the **real checkout**; record test receipts.
- [ ] Reconcile legacy overlay scientific claims and broad PDC citations against A–M scientific review and course overview. No automatic verification.
- [ ] Confirm after retrofit that both machines and future sessions can read a **single authoritative graph**, with a deterministic export/migration format and no unexplained shadow graph.

## 6. Re-entry cursor

- **Found in GitHub:** real app source `Academics/BEP/Catalysis/mindmap/` on `devcontainer` with `data/bep_map.yaml` (4 unchanged canonical nodes), `data/bep_draft_overlay.yaml` (**69 draft nodes: 33 original + 28 C1 AI-authored + 8 C2 AI-authored; existing centered Arrhenius claim corrected**), `schema.py`, `editor.py`, `mcp_server.py`, `preview.py`, `static/`, `tests/`. This is a draft-overlay content retrofit only; the runtime and local changes are unverified.
- **Not established:** local unpushed WIP state, whether `pixi run preview` succeeds, scientific correctness, or existence of actual owner approval for any overlay topic.
- **Next conversation:** resume C1's remaining chemistry-versus-kinetics boundaries; **the two major child branches under C1 are already a user structural decision**. Then C2–C15 Level-2 reviews. Keep all lower-layer examples open and extend the graph to any warranted depth; treat PDC as a supporting course/foundation, not a verified reactor research finding.
- **Next code step when specifically authorized:** safe local comparison + migration-aware retrofitting against this contract; no new prototype.

