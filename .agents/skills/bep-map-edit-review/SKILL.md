---
name: bep-map-edit-review
description: >-
  BEP Scientific Mind Map specialist. Trigger whenever asked to create, inspect,
  rearrange, approve, reject, promote, correct, compare or revert any node,
  scientific relationship, source, maturity level or graph hierarchy; also on
  complaints such as "this map is wrong", "why did you add that?", "undo that",
  or "make a fresh independent reference map". Enforces which map can be edited,
  records owner authorization, handles criticism calmly with precise targeted
  corrections and source checks, and preserves scientific topology. Invoke
  reversible-change-review separately for Git/diff/pull/push/revert mechanics.
  Co-maintain this skill with the map parser, editor and frontend.
---

# BEP scientific map — specific authoring, correction and owner-understanding policy

**This skill governs MEANING and AUTHORIZATION, not Git technique.** Use [`reversible-change-review`](../reversible-change-review/SKILL.md) for checkpoint/diff/remote verification/revert. Read BEP `conventions.md` §13, the [node contract](../../../Academics/BEP/Catalysis/research/notes/bep_mindmap_node_contract_2026_10_20.md), and the actual dataset before a targeted write. The existing viewer is not the sole source of truth.

## A. Decide WHICH map and which operation

**Conceptually different maps, not necessarily already separate implemented files:**

| Destination | Agent can independently author? | Highest knowledge state | What changes mean |
|---|---|---|---|
| AI scientific **reference** map / isolated new research draft | **Yes**; no per-node owner permission needed | Grey **Idea** / yellow **AI worked out** only | AI proposals/interpretations, not owner scientific knowledge |
| Owner's **personal/approved graph** or any `human_worked_out` (blue) status | **NO**, not without exact current owner approval | Blue only after explicit confirmation | Owner-chosen graph change; never implied by AI citation, Git merge or UI click |
| Source claim flagged as **human verified** | **NO** without actual review/evidence by owner | Independent status | Verification of a given citation-to-claim link, not maturity |

The existing SVG frontend has a separate, **read-only owner snapshot** mode. It accepts only an explicit local path or already-fetched local Git ref. It does not fetch GitHub, write owner YAML, or turn a snapshot into authoritative live state. The default AI-reference view remains separate.

**When the user says "change the actual graph":** determine whether the destination is the AI sandbox/reference draft or the personal/canonical presentation/understanding graph. If unclear and the write would touch the user's graph, **propose an exact patch and ask approval**; meanwhile AI may continue separate reference research. A request to "build the AI reference map" authorizes AI-only draft edits, not personal graph promotion. Do not call the legacy `promote_draft_node(..., new_tier=2)` or `/api/promote` as an approval shortcut.

**Approval transaction for the personal graph:**
1. Show **exact node IDs, titles, before/after parent/status/content, and scope** of change. For a single straightforward user-directed change, the user request itself may be explicit approval; no redundant approval dialogue.
2. If the instruction is ambiguous, ask one specific question; never infer approval from silence, the presence of a draft, a previous generic permission, an AI-generated explanation, or a successful Git operation.
3. Apply only the approved delta to the intended dataset/layer, with explicit record of user authorization (where available). Confirm no other personal nodes changed and no citation status was silently promoted.
4. Deliver an inspectable diff and revert instructions through the general workflow.

## B. Map-specific scientific model

- Single BEP scientific root. The owner previously selected first branches Physics / Mathematics / Systems & Control. Broad themes may be reconsidered for AI research. **No maximum depth**; levels 7, 8, 9+ are fine.
- Main subject: the original BEP proposal, dynamic acetylene semi-hydrogenation in a packed-bed reactor, with chemical/transport physics, catalyst coverages, mathematical numerical model, experiments, estimation and control. Broad supporting science is welcome with an explicit connection to this context; do not turn the task into unrelated encyclopedic expansion.
- The A–M research dossiers may inform multiple scientific branches; they are **source provenance/cross-links**, not obligatory siblings of the three science branches or forced tree ancestors. Their order is an **exploration itinerary**, not a fixed taxonomy.
- Preserve stable node IDs, parent ancestry, human decisions, annotations, source locators, open questions and important differences between literature models. Do not equate a speculative mechanism with experimentally validated kinetics; source-specific parameter sets remain conditioned on their catalysts and operating regimes.
- Each AI node is a separate substantive concept with notes/equations/assumptions as warranted. Distinguish (i) idea/unknown, (ii) AI synthesized with attached evidence, (iii) experimentally source-supported claim, (iv) human verified: different epistemic properties, not a ladder inferred from a color.
- **No data loss by serialization:** the current mind-map schema sets `extra="allow"` on its Pydantic models, so those models accept unknown fields. Do not promise that unknown fields survive every owner adapter or serialization path until that exact path is verified with round-trip validation. Display bugs are not source data defects by default. Code and data may advance at different times.
- The present 69-node AI draft is a **historical/provisional precedent**, not an authoritative answer for new independent reconstruction.

## C. Response protocol when the owner objects

A complaint, correction or frustrated reaction is **feedback**, not permission to destroy or replace the whole map:

1. **Restate the precise observed mismatch**, and identify current node IDs and relevant last edit/diff if possible. Distinguish a structural disagreement ("wrong parent"), scientific dispute ("this rate law doesn't apply"), missing information, UI-only presentation, and approval confusion.
2. **No panic reset.** Don't roll back a whole file, regenerate everything, silently "fix" unrelated branches, promote all nodes or commit a guessed interpretation. Preserve the scientific evidence and alternative viewpoints.
3. If clearly wrong **within autonomous AI reference scope**, make the smallest local correction, record the superseded claim as appropriate, run validation and link its patch; no need to ask permission. If owner explicitly requested the personal map correction, apply **only that approved change**. If multiple interpretations remain, **ask one direct, discriminating question** and offer a narrow proposed patch.
4. For requests to undo, inspect commit dependencies and use the reversible-change skill. **Do not delete a historically useful reference draft simply to hide it from a new agent**; use staged exposure and a comparison after an independent freeze, unless deletion is explicitly chosen after trade-off review.
5. Confirm whether the issue was corrected in *data* or only *rendering*. A good-looking graph does not prove correct physical or mathematical claims.

## D. New independent reconstruction mode ("from zero")

When directed to produce an independent AI reference map, **do not seed or imitate the previous dataset**. Treat this as a comparison experiment:

- **Source whitelist during blind stage:** original BEP proposal (`0_Project_Management/main.tex`, relevant proposal `section*.tex`, `references.bib`), and actual primary scientific literature / raw experiment descriptions intentionally selected for the task. Where uncertainty remains, label it rather than borrowing previous map conclusions. The root repository instructions still apply for safety, but skip reading map-specific taxonomy, existing map YAML, old map skill, prior map state/roadmaps and summaries **as scientific inputs** during the blind stage. Read *this authorization protocol* as governance only; do not inherit its example node hierarchy as scientific evidence.
- **No prior-map contamination:** do not open `mindmap/data/bep_draft_overlay.yaml`, prior mind-map taxonomy/specs, C1/C2 generated node contents, old synthesizer's candidate output or earlier AI map examples until the **new independent version is committed and frozen**. The three owner-decided first disciplines may be stated as a known structural constraint; otherwise allow the Level-2 themes/paths to emerge from primary sources.
- Write to a **fresh isolated path** (not the active `bep_map.yaml` or `bep_draft_overlay.yaml`). Include separate source manifest, uncertainty ledger and machine-readable scientific nodes; do not assume the current parser can safely round-trip the new experimental fields. This is a new *dataset*, not a replacement viewer.
- After freezing version 1 at a visible commit SHA, **and only then**, inspect the old map for comparison. Record convergences, surprises, possible bias, missing science and prior errors in a separate comparison artifact. Do NOT silently copy old nodes into the independent baseline.
- This is **instructional blindness**, not a guarantee of information-theoretic isolation: the old map remains in the same Git repository and may appear indirectly in global state/links or search results. Report accidental exposure honestly instead of asserting a perfect blind experiment.

## E. Compatibility and trigger enforcement

- Maintain **this map skill**, [general reversible-change skill](../reversible-change-review/SKILL.md), [map README](../../../Academics/BEP/Catalysis/mindmap/README.md), and node contract **alongside** changes in `mindmap/schema.py`, `editor.py`, `mcp_server.py`, `preview.py`, `synthesize_research.py`, `static/`, approval or metadata wiring. At minimum review each for still-correct constraints; update relevant content in the same PR, with regression tests for any changed behavior.
- Ordinary standalone scientific reference data edits follow this skill and the general change skill. They do **not** imply permission to refactor the application or alter the personal map.
- Every delivered map edit must state **which map**, changed node IDs/claims, source uncertainty, human approvals actually obtained, validation actually run, exact diff and easiest safe revert. If the user asks only for analysis, do not write the map without being asked.

## F. Frontend review-state and snapshot rules

- Owner snapshots retain an unbounded structural `tier` independently from five concept/writing stages: `idea`, `ai_worked_out`, `human_worked_out`, `informal_writing`, and `formal_writing`, recorded in `maturity` or `progress_stage`. `structural_approval`, `owner_read_status`, `owner_content_approval`, AI source attachment, and claim/source `human_verified` remain separate fields.
- SVG layout weights allocate space from visible descendants and card dimensions. Treat them as presentation only; they do not show scientific importance, evidence quality, progress, or owner approval. Layout should follow the current map structure without assuming a fixed number of themes or questions.
- For legacy AI-reference maps only, an integer `tier` without an explicit stage remains a read-only historical progress label. Never map it or node placement into personal understanding or citation review.
- The default owner-node view shows title, structural tier, maturity, summary, substantive notes and an optional linked Markdown `reader_file`. Its `kind` describes the linked page and never changes node maturity. Detailed questions, claims, citations, provenance and `background_files` remain available in the collapsed technical-audit section. Reader figures load only on demand; linked files are served from the selected snapshot without writing or fetching map data.
- The legacy promotion API returns HTTP 410, and legacy editor/MCP paths refuse owner-review field writes and positive `human_verified` updates. Do not re-enable promotion or add owner-status editing without a separately reviewed, explicit authorization workflow.
- Claim citations may follow `owner node → AI reference node/claim_ref → AI source record → locator`. Show unresolved links, missing excerpts, and unrecorded verification as such. AI `supports` summaries are not quotations; do not invent a passage or transfer the AI map's source-access status into owner human verification.
- Owner/reference snapshots read only explicitly selected local paths or already-fetched local refs. The app does not perform a live GitHub fetch; refresh reads the selected snapshot again. A changed remote branch is not visible until an explicit fetch and selection/restart.

**This is an authoring protocol. Git diffs are handled by the general reusable skill, not the reason this skill exists.**
