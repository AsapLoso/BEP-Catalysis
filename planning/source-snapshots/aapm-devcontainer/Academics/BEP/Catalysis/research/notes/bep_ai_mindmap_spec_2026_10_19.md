# BEP ownership mind map — conversation-first V1 specification

**Captured:** 2026-10-19; **taxonomy/interaction refinements:** 2026-10-20.  
**Current canonical taxonomy and working plan:** [20 October ownership mind-map taxonomy](bep_ownership_mindmap_taxonomy_2026_10_20.md). **That document supersedes this earlier draft on color tiers and proposed Level-2 subjects.** This document remains the implementation/viewer design reference.  
**Status:** Design and taxonomy on GitHub; **existing Python/JS application and YAML discovered** on `devcontainer` at `Academics/BEP/Catalysis/mindmap/` (four canonical nodes, fifteen older overlay nodes). **Local unpushed work/runtime/tests unverified**. **Retrofit existing work; do not build a second mock.** Individual map edits require explicit owner approval. [Portable node schema and change-record protocol](bep_mindmap_node_contract_2026_10_20.md).  
**Project:** Dual BEP Catalysis (acetylene semi-hydrogenation). This is **not** the literature-extraction knowledge graph under `Articles/graph/` and **not** a replacement for Wayfinder, `state.md`, or existing research artifacts.

## Goal and workflow

Restore an at-a-glance, navigable sense of ownership over the whole BEP. The owner and AI brainstorm branch names, placement and conceptual structure **together**. The **AI is the only editor** of the persisted map; the visual mind map is a read-only, navigable projection of the saved graph.

- The assistant may **propose** nodes, sources, tiers, names and connections in conversation, but **does not write** them without an explicit approval or direct edit command from the owner. Brainstorming is never approval.
- A direct command (e.g. "add intraparticle diffusion under transport phenomena") is the authorization for **that specific edit**; ambiguous requests require resolving the ambiguity before writing.
- All changes are scoped to what was approved. No background enrichment, automatic branch expansion, silent reassignment, implicit source citation or autonomous status promotion.
- The map updates automatically in the running local preview after the saved file changes. The user does **not** need an interactive visual editor.

## Graph structure

- One central project node/title. Exactly **three first-level arms** by initial convention: **Physics**, **Mathematics**, **Systems & Control**. Keep the label **Physics** even though it includes chemistry.
- The tree is directional and hierarchical; arbitrary depth, each node has one parent. The visual direction can be chosen for readability but edges are always conceptually parent → child.
- Examples of **candidate** second-level branches for brainstorming, **not approved entries**:
  - Physics → reaction kinetics, transport phenomena, reactor physics.
  - Mathematics → governing equations/PDEs, discretization, numerical solvers.
  - Systems & Control → system identification, model reduction, periodic excitation/control.
- Branch names, ordering and grouping are owner decisions, to be settled iteratively. Do not pre-populate speculative topics as if approved research.
- Cross-topic relationships may be useful later, but preserve a clean parent/child map in V1; add cross-links only if explicitly requested. Not every scientific dependency needs to be represented as a hierarchy edge.

## Color and citation statuses — updated 20 October

**Single node maturity dimension, three categories (owner conversation supersedes the earlier five-tier suggestion):**

| State | Suggested visual color | Definition |
| --- | --- | --- |
| **Idea** | Grey | Named/proposed, not substantively developed |
| **AI worked out** | Amber | Substantive AI research or interpretation, human scientific review outstanding |
| **Human worked out** | Blue | Owner personally worked through/reviewed or explicitly adopted the actual content |

**Independent source/citation status** (distinct icons/colors): **AI-attached** means proposed or connected by AI, *not human verified*; **human-verified** means owner explicitly checked the relevant passage/evidence as supporting the specific claim. No source becomes human-verified merely by appearing in a document; no concept becomes human-worked-out merely by approving its placement in the tree. No separate documentation-writing maturity scale in V1.

The complete scientific taxonomy, six-level illustration (including **three child levels below a letter**), 15 candidate Level-2 themes, A–M mapping and staged review plan are in [the taxonomy note](bep_ownership_mindmap_taxonomy_2026_10_20.md). It is a draft layout **not yet authorized as live graph data**.

## Rich node information (compact visible block, details on click)

**Keep the nodes small on the canvas** (title, maturity/color, perhaps star rating and small source indicator), and show the fuller record in a read-only detail panel/tooltip on click.

Recommended fields:

- **Stable ID** independent of title (rename-safe), parent ID, display title, optional short description.
- **Maturity** (Idea / AI worked out / Human worked out; drives fill color).
- **Importance** as optional **0–3 stars** (research value or priority, not proof, certainty or completeness).
- **Rationale / why here:** one or two sentences explaining why this branch is worth including *relative to its parent*.
- **Sources / evidence links**: zero or more links to papers/DOIs/Zotero keys, repo paths, notebook and code references, equations, or research notes; where possible include locator (section/page/cell), and whether the source is verified/reviewed. Adding a reference is not the same as verifying its support for a claim.
- **Notes / remarks:** free text with the owner's reasoning, a question, caveat, interpretation or next thought.
- Optional **open questions**, tags and sibling order. Do not mandate a long database schema or multiple status dimensions.

Stars and presence of sources are shown as badges/icons/metadata, **not additional competing node colors**. No silent auto-filling of papers or claimed results. Unknown information stays empty/unknown.

Illustrative (non-canonical) initial YAML data shape, adapted from a concurrent 19 October specification and **not approved as persisted map data**:

```yaml
nodes:
  - id: n_project
    parent: null
    title: "BEP — Catalytic Reactor Modelling"
    maturity: idea
    importance: null
    rationale: "Scientific knowledge map of the dual BEP."
    notes: ""
    sources: []
  - id: n_physics
    parent: n_project
    title: Physics
    maturity: idea
    importance: null
    rationale: ""
    notes: ""
    sources: []
  - id: n_mathematics
    parent: n_project
    title: Mathematics
    maturity: idea
    importance: null
    rationale: ""
    notes: ""
    sources: []
  - id: n_control
    parent: n_project
    title: Systems & Control
    maturity: idea
    importance: null
    rationale: ""
    notes: ""
    sources: []
```

The IDs are stable opaque identifiers, not paths; renaming or reparenting must never change them. Additional nodes, sources and validation fields will be settled during implementation. The root and three main arms are a design decision, not proof that a graph has already been initialized.

## Interaction / visualization V1

- Read-only **interactive graph**: mouse-wheel zoom, click-and-drag panning, fit-to-view, expand/collapse branches, and click node for full details.
- Automatically arranged directed tree; legible labels and sensible branch separation. A suitable graph visualization library can handle layout.
- Render the exact stored graph (and its selected metadata), not an independently generated interpretation. Preserve zoom/pan where feasible on refresh.
- No need for direct visual creation, deletion, dragging nodes to reparent, form editing, dashboards, voice controls or autonomous research import.

## Local storage, MCP and Pixi preview

- Prefer one human-readable, git-tracked **YAML** graph file, with enough metadata on each node; JSON/database is **not required**. Avoid proliferating files before a concrete need. Schema validation is welcome as implementation detail.
- A small deterministic Python layer, optionally exposed as a **local stdio MCP server**, handles narrowly defined operations: read/search, add, rename, reparent, delete, set tier, set stars, edit rationale/notes, attach/remove source.
- Validation requirements: stable IDs; unique nodes; existing parent; no cycles; exact target resolution; safe atomic write; ability to review what changed; fail without mutation if invalid or ambiguous. Deletions/multi-node operations should be explicit. Git provides revision history.
- The AI uses natural language as the **primary edit interface from V1**. It proposes and obtains approval; the Python/MCP layer performs the deterministic file operation. Remote ChatGPT needs an explicitly connected bridge to reach a local MCP/server; don't imply this chat can edit local disk without one.
- From within the **mind-map directory**, `pixi run preview` launches a **local live preview**. Watching the saved map file triggers immediate browser re-render without manual rebuild or page refresh (where feasible). A file-watcher/dev server handles this; Pixi just launches it.
- **Existing verified reference implementation**: `AsapLoso/Methanol-Catalysis` (main) has `[tasks] preview = "myst start"` in `pixi.toml`. Reuse the **developer experience and inspect existing watch behavior**, but do not assume MyST itself must power the graph. Keep the map's own dependencies isolated as needed.
- **Existing code placement is known:** `Academics/BEP/Catalysis/mindmap/` (Python `schema.py`, `editor.py`, `mcp_server.py`, `preview.py`, JS `static/`, YAML `data/`, `tests/`). Use the existing implementation as retrofit base; verify the local WIP and test commands before mutating. **Its current `tier:0..4` and promotion default to owner-understood are semantically outdated.** See [node contract](bep_mindmap_node_contract_2026_10_20.md).

## MVP acceptance checks

1. New local checkout can start map preview via `pixi run preview` from the map directory.
2. Starts with approved project root and three named arms; shows a directional, pan/zoomable, collapsible graph.
3. Click reveals node title, tier, stars, rationale, notes and source links.
4. An expressly approved spoken/typed edit, routed through the local AI/MCP editing mechanism, changes precisely the intended YAML records.
5. Saving the YAML visibly updates an already-open preview automatically.
6. No approved edit → **no map mutation**; invalid structure → **no saved edit**.
7. Maturity changes do not masquerade as scientific validation; no automatic source invention.

## Ordered next steps — existing implementation retrofit, not a mock

**Canonical actionable checklist and compaction checkpoint:** [20 October taxonomy, START HERE](bep_ownership_mindmap_taxonomy_2026_10_20.md#start-here--concrete-execution-checklist-2026-10-20). That document tracks individual Level-2 themes (15) and per-letter Level-4/5/6 work (39), alongside retrofit tests and a re-entry receipt.

1. **Read-only inspect current local WIP** and preserve code, branch, data, stable IDs and uncommitted files. GitHub baseline location `Academics/BEP/Catalysis/mindmap/` verified, but local unpushed work remains **UNVERIFIED**.
2. **Review proposed Level-2 scientific themes in conversation** and then A–M subject placements. No approval of live graph mutation should be inferred from documentation work.
3. **Retrofit current code in place** with the approved hierarchy, three understanding statuses, independent two-state citation statuses, rich nested notes and deterministic edits. Do not create an unrelated demo/mock application.
4. Test real app functionality: approval boundary, notes/sub-notes, citation badges, YAML validation, live preview via `pixi run preview`, pan/zoom/collapse; record receipts.
5. Continue deeper per-letter review and integrate expressly approved nodes; preserve source references and the current worktree.

## Explicitly out of scope for now

Wayfinder restructuring, project-wide automatic indexing, literature-graph migration, automatic research progress inference, elaborate database architecture, graphical editing and separate analytics dashboards.

## Decision provenance

- **User-decided:** three main arms; AI edits only by approval; conversation-first brainstorming; complete scientific scope; up to three nested sub-note levels below each letter (or more if needed); node states idea/AI worked out/human worked out and independent AI-attached/human-verified citation status; local file; preview via `pixi run preview`; pan/zoom; stars, sources and explanations; record decisions in GitHub.
- **Design suggestions, subject to refinement:** current three-color palette, proposed 15 broad Level-2 themes, letter placements, 0–3 importance stars, YAML field names, local stdio MCP, proposed library/layout and final implementation directory.
- **Implementation:** Verified repository source and YAML exist under `mindmap/`; this design document **does not establish successful runtime, tests or any local unpushed changes**. Retrofit it in place. No scientific claims are verified by the design note.
