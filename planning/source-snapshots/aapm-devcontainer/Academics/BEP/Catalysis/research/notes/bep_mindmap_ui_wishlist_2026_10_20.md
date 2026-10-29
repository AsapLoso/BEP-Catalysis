# BEP Mind Map — UI wishlist and navigation design review

**Captured:** 2026-10-20, from the owner's screenshot and written feedback.  
**Status:** **WISHLIST / design**, not an authorized implementation or an assertion that runtime behavior has been verified.  
**Canonical graph and node governance:** [taxonomy/checklist](bep_ownership_mindmap_taxonomy_2026_10_20.md) · [node contract](bep_mindmap_node_contract_2026_10_20.md) · [existing application](../../mindmap/).  
**App goal:** improve the already-existing application in place; **do not build a new mock**.

## The owner's observations and requests (preserve exactly as intent)

1. **"Letters thingy is just wrong. Simple fix."** The screenshot places the `Deep Dive Letters (A–M)` as a prominent extra root branch, with individual letters, rather than locating relevant research narratives against the scientific map.
2. **"Too dense."** Add visibly larger **padding between head branches**, especially the Physics / Mathematics / Systems & Control subtrees. Owner explicitly asked to **jot down as a UI wishlist**; do not assume they wanted spacing implemented immediately.
3. **"Maybe single line view?"** Explore a non-2D, single-focus navigation mode: the **one selected line / branch** should expand to the right, while its **singular ancestry line traces back to the root**. Other unrelated sections should not crowd the screen. This is a requested concept, not yet a finalized interaction design.
4. **"You do some thinking too"** — evaluate alternatives and better interaction patterns instead of merely adjusting the current force of padding.

**Positive constraint:** the owner says the map **looks nice**. Preserve its visual language, subdued background, clear cards/links and general aesthetic where possible. Fix information architecture and navigation first, not a cosmetic full redesign.

## Screenshot reading and epistemic boundary

The screenshot shows the central BEP root leading not only to `Physics`, `Mathematics`, and `Systems & Control`, but also to prominent `Deep Dive Letters (A–M)` and `Administrative & Milestones` branches. Many yellow `AI Draft` cards and orange dashed edges are simultaneously shown; lengthy labels are tiny and very dense. The header legend still shows **five tiers** and the header takes substantial horizontal room.

**Do not assume the screenshot exactly matches the branch presently visible to GitHub tooling.** Read-only inspection of `devcontainer` on 2026-10-20 finds `mindmap/static/app.js` with five-tier legend, `mindmap/data/bep_map.yaml` with four canonical root/discipline nodes and `bep_draft_overlay.yaml` with **33** draft nodes (15 original research + 15 broad themes + one PDC + two C1 children). It does **not** by itself locate the screenshot's additional root siblings, letter cluster or all of the rendered research nodes. Possibilities include local/unpushed WIP, another branch or a generated/imported overlay; **inspect the actual runtime source/data before changing this UI**. This document does not verify where screenshot-only nodes are stored.

Do not overwrite screenshot-only or unpushed work. Do not edit `bep_map.yaml` / scientific maturity based merely on UI feedback.

## Prioritized product backlog

Each item has an owner-specified **requirement** or an **assistant proposal**. Priority refers to UI-design sequence, not a global BEP deadline.

### P0 — Correct mental model and preserve orientation

- [ ] **UI-01 [OWNER REQUEST — strong] — Remove the A–M branch as a competing SCIENTIFIC root hierarchy.** Exactly the three scientific arms belong at Level 1. Treat A–M as **research dossiers/annotations/alternate navigation index**: a letter can be tagged on multiple science nodes through `research_letters` / cross references; if browsing by letter, show the dossier's research question and links to the corresponding science nodes. The letter C may link to both chemical pathways and catalyst sites and neighboring kinetics; A/B/M are cross-disciplinary. **Do not delete existing letter content**, and do not invent a single parent for each letter merely to satisfy the tree. If the current app requires letters-as-nodes for a view, maintain a *derived alternate index*, not an extra science root.
- [ ] **UI-02 [ASSISTANT CONSEQUENCE] — Separate project-management material.** `Administrative & Milestones` shown as an extra root sibling should appear in a separate **Project / Tasks** panel, tab or filter (or cross-link), not claim Level-1 scientific classification. Preserve its task data and original references. Ask before relocating persisted nodes.
- [ ] **UI-03 [OWNER REQUEST — strong] — Add whitespace between three head branches.** Try branch-aware/sublane padding based on *visible subtree bounding boxes*, not just uniform increased card spacing. Space between Physics/Math/S&C greater than spacing within a single theme; recompute when collapsing, expanding or filtering. Avoid excessive whitespace within a focused branch.
- [ ] **UI-04 [OWNER REQUEST — exploratory] — Focused single-path view (see detailed design below).** Keep a clear root → … → selected-node ancestry and one rightward active exploration path; hide unrelated subtrees. Do not require zooming far out to read a subject.

### P1 — More practical navigation

- [ ] **UI-05 [ASSISTANT PROPOSAL] — Two linked views, not one layout asked to do everything:** **Overview** (high-level 2D scientific landscape, default initially collapsed at Level 1/2) and **Focus / Path** (one conceptual chain with immediate child choices). Switching views must retain selection, expanded path and back-navigation; don't re-author graph data.
- [ ] **UI-06 [ASSISTANT PROPOSAL] — Progressive disclosure:** collapsed-by-default on large graphs, child-count indicators, one-subtree expand controls and an explicit **Expand All** confirmation/limit if it would produce an unreadable canvas. Viewport fits selected section, not always the entire graph.
- [ ] **UI-07 [ASSISTANT PROPOSAL] — Breadcrumb, Back and jump-to-parent:** `BEP › Physics › Catalytic Chemistry › Catalyst Chemistry & Active Sites` visible and clickable; current selection and tree depth should be unmistakable. If the user jumps via search, restore the full ancestry chain.
- [ ] **UI-08 [ASSISTANT PROPOSAL] — Find and jump:** search node titles, source notes and IDs; optional filters for science discipline, A–M dossier, maturity, open questions and draft/canonical; jump focuses a single node rather than expanding every matching branch.
- [ ] **UI-09 [ASSISTANT PROPOSAL] — Details where the reading happens:** modest card title/preview but rich side pane for Markdown, equations, source locators, importance stars and open questions. Do not force all science into tiny 220px cards.
- [ ] **UI-10 [ASSISTANT PROPOSAL] — Keep UI and metadata honest:** three scientific understanding states (Idea / AI worked out / Human worked out), **independent** source review badges (AI-attached/human-verified), and distinct *draft/canonical inclusion* status. The screenshot and checked-in code still have the **obsolete 0–4 five-tier legend**. Never equate a node's placement/approval with human scientific review. Audit old `promote` behavior before enabling promotions.
- [ ] **UI-11 [ASSISTANT PROPOSAL] — Different edge types:** structural parent/child (solid), scientific cross-reference (subtle dotted/hover-only), A–M dossier link (small tag/badge). The current large number of orange dashed links visually overwhelms the structural story; edge semantics should be explicit.
- [ ] **UI-12 [ASSISTANT PROPOSAL] — Responsive reading experience:** on laptops and phones collapse the huge header/legend into a menu and allow keyboard/trackpad navigation, accessible focus targets, touch-friendly child selection. Offer a full-width reading panel and semantic zoom/fit without text becoming illegible.

### P2 — Later, after the hierarchy and focus mode are usable

- [ ] **UI-13 [ASSISTANT PROPOSAL] — Expandable guided tour:** a letter-based tour becomes a *navigation overlay through science nodes*, not a separate branch; persist visited position, reveal only nearby concepts and offer “Open dossier”.
- [ ] **UI-14 [ASSISTANT PROPOSAL] — Optional overview mini-map / local map preview:** show approximate location without demanding that every node remain visible.
- [ ] **UI-15 [ASSISTANT PROPOSAL] — Smooth transitions + focus memory:** zoom/scroll interpolation, remember user position per view, avoid jumping to origin during live reload; do not let aesthetics compromise performance.

## Recommended Focus / Path mode — specific interaction sketch

**Best starting design: a _Miller-columns/path-browser hybrid_**, rather than forcing an enormous 2D tree into a one-pixel-wide stripe:

```text
[← Back] [BEP > Physics > Catalytic Chemistry > Catalyst Chemistry]
                                                   [selected subject]

 Left: compact breadcrumb (the ONLY visible ancestry route to root)
 Right: choose ONE child at a time to advance one conceptual depth
 ┌──────────────────────────┬────────────────────────────┐
 │ Catalyst Chemistry       │ Immediate children         │
 │ (substantive notes)      │ • Pd-based catalyst        │
 │                          │ • Active sites             │
 │                          │ • Adsorption mechanisms    │
 └──────────────────────────┴────────────────────────────┘
                select “Active sites” → new breadcrumb segment,
                new detail, new immediate-child list;
                unrelated sibling subtrees stay hidden.
```

An equally viable rendering is **a single horizontal visual spine** (root on left → selected subject), then small sibling/next-child cards on its far-right end. Which rendering the owner prefers remains **UNDECIDED**. Do **not** implement an arbitrary final layout solely from this sketch.

This mode is inherently **unlimited-depth**: each click advances one step, regardless of graph depth (7, 8, 9+ allowed), while navigation costs stay approximately constant. Root ancestry is displayed once, not cloned for each leaf. Cross-links are separate non-tree targets, not new parents. For large child sets, use a compact scrollable child list, optionally with search.

### Context transitions to test

1. At global root show just the **three scientific arms** and a small `Other resources` button for project/admin, literature, A–M.
2. Enter Physics → C1 → `Catalyst Chemistry & Active Sites`; breadcrumb shows one chain, only direct children appear to its right; parent notes remain easy to access.
3. Click a child, then Back; preserve scroll/selection. Switch to Overview, highlight selected node and show no more than immediate neighbors initially.
4. Open Letter C index: show linked C1/C2 subjects and dossier without creating a science-root `Letters` branch.
5. Search a depth-8 node and jump straight to it with correct ancestor trail, no “expand everything” explosion.

## Implementation guidance / inspect-before-code

- This is a **wishlist-only** document. Owner did **not** ask to code these improvements in this turn. Continue collecting feedback and request a concrete implementation goal when ready.
- Inspect runtime's actual generated graph and UI source; trace screenshot-only extra branches and letter cluster to their real data source, then fix information architecture **non-destructively**. The GitHub `devcontainer` branch is a baseline, not proof it is the running version.
- Preserve all node IDs, linked citations, A–M dossiers, status distinctions, and per-node notes. The scientific graph has unlimited conceptual depth and should not require padding with empty levels.
- Add tests around alternate views/lens: root must expose exactly three science arms; letters become cross-links or separate index; no lost nodes; focus ancestry exactly one root path; navigation works beyond depth 6; expansion and persistent selection behave when filtering.
- Prefer incremental retrofit in the existing `Academics/BEP/Catalysis/mindmap/` Python/JS/YAML project. No parallel mock; avoid merging data changes when unseen local WIP is unsynced.

## Work handoff after this wishlist

When a Work session starts: **read the canonical taxonomy/checklist, node contract and THIS UI wishlist, inspect real branch/worktree/browser runtime, report findings and risks, then wait for the user's goal prompt before implementing UI**. Do not interpret this brainstorming record as authorization to rewrite the application.

**Current scientific checkpoint remains C1/C2 Physics boundaries; UI wishlist work does not certify any scientific node.**
