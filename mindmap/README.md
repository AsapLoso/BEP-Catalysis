# BEP scientific knowledge map — data contracts and edit workflow

This existing Python/YAML mind-map application renders an evolving **scientific reference map** for the BEP on dynamic acetylene semi-hydrogenation in a packed-bed reactor. **Its data are the deliverable; the graph viewer is a consumer.** The existing SVG viewer also supports an explicitly selected, read-only snapshot of the owner's personal map, while preserving the AI reference map as a separate view.

## Two complementary skills — scientific meaning first

- [`bep-map-edit-review`](../../../../.agents/skills/bep-map-edit-review/SKILL.md) is the **specific map-authoring and correction skill**. It resolves which graph is the target, what a user-approved personal edit means, what AI can author without asking, how to interpret a complaint, how to preserve scientific provenance, and how independent reference reconstruction works.
- [`reversible-change-review`](../../../../.agents/skills/reversible-change-review/SKILL.md) is the **general Git/sync transaction skill**. It handles isolated changes, pull/edit/push/pull-and-compare, precise diffs, integration commit preservation and safe targeted reverts for any file or service.

**Trigger:** use the map skill for node/content/topology/approval/complaint requests and the general skill for persistence. Do not use Git correctness as a substitute for scientific or user-approval correctness.

**Maintain both skills and this README whenever relevant parser, editor, frontend, data format or review semantics change**; review/update in the same PR. A content-only science-data edit does not require redesigning those components.

## Where information lives

- `data/bep_map.yaml`: existing canonical BEP root and three discipline arms; legacy `tier` values are not evidence of user understanding.
- `data/bep_draft_overlay.yaml`: AI reference knowledge, source notes and concepts (grey `tier: 0` Idea, yellow `tier: 1` AI worked out). May grow without individual owner permission; must **never self-promote above yellow**.
- The **user's personal understanding map** is separate and only changed on explicit, change-specific owner approval. The opt-in owner snapshot view is read-only; the preview API does not write either map. No Git commit/merge/diff review equates to owner understanding.
- [Node contract](../research/notes/bep_mindmap_node_contract_2026_10_20.md) sets the desired rich fields. The legacy editor preserves unknown metadata, and the owner-map adapter validates core IDs, stages, source links and graph structure while retaining unknown fields. Keep personal-map content in its separate source and use snapshots for viewing.
- [Taxonomy and review plan](../research/notes/bep_ownership_mindmap_taxonomy_2026_10_20.md) defines the three science arms, AI-proposed Level-2 themes, and A–M source-dossier extraction. Unlimited levels are fine. [Original BEP proposal](../0_Project_Management/main.tex) is the scientific center of gravity, not a hard expansion limit.
- [Project conventions](../conventions.md) §13, [BEP state](../state.md), and [Work handoff](../research/notes/bep_mindmap_work_handoff_2026_10_21.md) explain governance and next tasks.

## Independent AI reference reconstruction

A new AI research map can be constructed **from zero in a new data-only directory**, without opening this existing reference overlay until the fresh version is committed and frozen. That old overlay remains versioned for a later unbiased comparison. This is an *information-exposure policy*, not deletion or an assertion of perfect blindness; old map details in global rules/states may leak inadvertently. See [fresh Work prompt](../research/notes/bep_independent_reference_map_work_prompt_2026_10_21.md).

## Read-only owner snapshots and progress

The owner view is **opt-in** and reads a local file or an already-fetched local Git ref. It does not fetch GitHub, change a branch, write YAML, or claim that a snapshot is the latest authoritative map. The default AI reference view continues to use the existing application data.

Example from the repository root, after fetching the documentation branch and the pinned AI reference commit named in its `owner_working_map/reference_map.yaml` manifest:

```sh
python -m mindmap.preview \
  --owner-map research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml \
  --reference-map research/manual_map_sessions_2026_10_22/owner_working_map/reference_map.yaml \
  --git-root .
```

The reference manifest records the original AAPM source commit and the migrated BEP Catalysis snapshot. Its component files are read from this checkout as a read-only local snapshot; no remote fetch is performed. If a file is missing, startup fails with a clear error. You can instead pass other explicit local files, or an already-fetched local Git ref and repository-relative path. Refresh reloads the selected snapshot; GitHub changes appear only after the user explicitly fetches a newer ref and restarts or selects it.

Owner nodes support five stages: `idea`, `ai_worked_out`, `human_worked_out`, `informal_writing`, and `formal_writing`. Structural approval, owner reading, owner content approval, AI source attachment, and claim/source `human_verified` are displayed separately. Historical integer tiers are labelled read-only and never migrated into an owner decision. `/api/promote`, the drawer promotion button, and the tour promotion button are disabled; the API returns HTTP 410 and editor/MCP writes fail closed for owner-review fields.

The selected-node panel keeps the title, summary, one progress-stage cue, and any linked reader page visible. Technical notes, source audit, and hidden background files are behind explicit disclosures; a background document loads only after it is selected. Markdown is rendered with raw HTML escaped, and linked raster figures load on request. Unlinked SVG assets are not discovered or exposed. AI references open in a separate panel with evidence notes, source access/verification metadata, limitations, and directly linked uncertainties; they remain separate from the personal map. Search shows reference results only when an owner snapshot and its reference manifest are explicitly loaded. Link presence does not imply owner understanding or human source verification.

## Reproducible edit-and-review cycle

1. Read the current branch/HEAD and exact records. Make one coherent, source-bound scientific edit in an isolated branch; preserve concurrent changes and node IDs.
2. Inspect `git diff -- data/bep_draft_overlay.yaml` (or the exact changed paths) **before** making a scoped commit. Use `git add -- <exact edited paths>`, then `git commit -m "BEP map: ..."`; never global-stage.
3. Inspect `git show --stat --oneline HEAD` and the exact patch after commit. For GitHub API-only work, compare old vs new node text before `update_file` and inspect the resulting GitHub commit or PR Files view. **Share a diff link and summary with the user**; the link is the verification mechanism for changes, not for scientific truth.
4. Validate YAML syntax/IDs/parents/acyclicity and source caveats. Test round-trip serialization in an isolated scratch copy when available; report tests *not run* if not. Never run the mutating promotion test against the live YAML.
5. To undo a logical mistake, use a new revert commit or dedicated revert PR, after inspecting conflicts with later edits. Do not force-push or hard reset shared work.
6. **Preserve the logical commits when merging.** For scientific-data PRs containing several separately reversible edits, choose a GitHub **merge commit** (`merge_method=merge`) or a rebase that retains those individual commits, **not squash merge**. Otherwise the patch may still be reversed selectively, but its pre-squash commits are not directly revertible on the integration branch. [PR #159](https://github.com/AsapLoso/project-management-agents/pull/159) is a documented earlier **squash exception**: the three source-branch science edits have individual diff pages, but undoing just one from `devcontainer` needs a targeted inverse patch; reverting the squash commit undoes all three edits at once.

**Compatibility boundary:** the legacy `/api/promote` route is retained only as a clear HTTP 410 refusal. Use the AI reference editor only for AI-reference content; it cannot write owner progress, placement approvals, reading status, or positive citation verification. The opt-in owner snapshot view remains read-only.

**Not a second viewer:** this README documents the current scientific dataset and its controlled Git history; no parallel frontend app is required.
