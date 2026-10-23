# BEP Scientific Map — GitHub Cloud Work Handoff (previous approach)

**CURRENT GOAL SUPERSEDED for independent reconstruction:** [Use the independent reference map prompt](bep_independent_reference_map_work_prompt_2026_10_21.md) for the next Work chat. This older document describes the prior incremental-edit proposal and is retained as history; **do not seed the new independent version from the existing 69-node map or these detailed examples**.


**Current goal: build and organize an AI SCIENTIFIC REFERENCE MAP as backend content, anchored in the original BEP proposal.** This supersedes the earlier UI-first implementation plan in this document. No frontend work or user-PC sync in this execution.

## Required edit review and reversible checkpoints (21 Oct update)

Use [`bep-map-edit-review`](../../../../.agents/skills/bep-map-edit-review/SKILL.md) plus [mind-map data README](../../mindmap/README.md) **for every scientific graph data edit**. Each independently meaningful edit gets a narrowly scoped Git commit and a checked, **user-inspectable Git diff**. Revert mistakes using a new revert commit or revert PR without destroying intervening changes. In GitHub-API-only mode use blob-SHA guarded writes and compare the old/new node records and the GitHub PR patch. This workflow is for traceability and review, **not** automatic scientific or human-knowledge certification. Keep this skill and README co-maintained with the frontend/parser/editor on any future compatibility change. **Current work resumes with scientific DATA**, not frontend or backend software development.

## Owner's confirmed model

There are **two conceptually distinct maps / roles**, not necessarily two implemented storage systems yet:

- **AI reference map:** autonomously populated by AI, without obtaining node-by-node user approval. May hold **grey Ideas** and **yellow AI-worked-out content only**. This can be broad, deeply nested, speculative where labelled, and source-rich. **It can NEVER certify blue Human worked out or silently promote into the personal map.**
- **Owner's personal understanding map:** built with the owner through conversation. **Every authoring/promoting change requires actual, specific owner approval.** Authoring rights, source-claim verification and owner scientific understanding remain separate. The current application schema does *not yet* implement every required permission/state distinction; preserve the governance boundary without falsely asserting that the app already enforces it.

**Unlimited depth, no arbitrary research quota for this execution — but not an arbitrary encyclopedia.** The original [BEP proposal](../../0_Project_Management/main.tex) and [proposal roadmap](../../0_Project_Management/bep_proposal_roadmap.md) are the **center of gravity**. Explore subjects that help explain, question, model, simulate, identify, measure or extend this project. If a subject goes well outside the proposal, state the scientific connection and label it as supportive or future research. The owner did not ask to permanently cap the scope of the wider project.

### Scientific center of gravity (do not treat as established experimental results)

- Selective acetylene semi-hydrogenation in a packed-bed catalytic reactor: C2H2 → C2H4 → C2H6, catalyst chemistry, ethylene yield/selectivity, mechanistic pathways, site coverages.
- Flow and transport: gas convection/dispersion, external film effects, intraparticle pore diffusion, Pe/Da and model reduction assumptions.
- Mathematical physics: coupled spatial and temporal balances, mass/site/energy conservation, PDE/ODE/DAE structure, discretization (method of lines, upwind/central, alternatives) and stiff integrators.
- Dynamics and control: transient inlet composition forcing, surface memory versus PSSA, Jacobians/stability/periodic solutions, observable hidden states, identification, filtering and optimization.
- Experiments, available measurements, literature applicability and uncertainty; identify which topics are core to the BEP model versus optional extensions such as realtime control and wider fundamental theory.

Important epistemic caveat: the original proposal may *propose* periodic input improvements, specific kinetic models or filters. The reference map must distinguish objectives/hypotheses from established results, and source applicability from physically calibrated models.

## Original working methodology (heuristic, not a hard waterfall)

1. **First layer: disciplines** — exactly **Physics**, **Mathematics**, **Systems & Control** under the BEP root. This structural choice was made by the owner.
2. **Second layer: scientific themes** — audit/refine the **15 AI-proposed Level-2 topics** (five per discipline initially); owner has not individually approved them. As AI-reference organization, refinement can continue without blocking for approval.
3. **Then go letter-by-letter through A–M** as *research extraction and provenance*: for each dossier extract concepts, evidence and questions, and place them into whichever scientific branches are appropriate. **Letters are not a fourth scientific arm or forced fixed-depth parents.**
4. **Fill missing scientific connections beyond A–M**, guided by the proposal. Science discoveries may cause earlier theme boundaries or lower nodes to be revised. All hierarchy depths allowed (Level 8 already occurs).

The user's original first-layer/second-layer/per-letter itinerary is the baseline. Scientific-taxonomy audits and node inventories are useful supporting methods, **not mandatory bureaucratic bottlenecks that prevent expanding the AI reference map**.

## Phase-1 reconnaissance — already done (verify current HEAD once)

**Private repository:** `AsapLoso/project-management-agents`, integration branch usually `devcontainer`. Root repo instructions `AGENTS.md`, `.agents/AGENTS.md`; scoped `conventions.md` §13.

**Existing backend:**
- `Academics/BEP/Catalysis/mindmap/data/bep_map.yaml` — 4 canonical records (BEP root + three disciplines). These records alone do **not** prove the owner personally understands the scientific content.
- `Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml` — 61 draft records at 21 Oct, including 15 earlier AI-concept records, 15 broad theme proposals, one PDC supporting node, two major C1 child nodes and 28 more detailed C1 AI descendants from [PR #148](https://github.com/AsapLoso/project-management-agents/pull/148). Deepest node depth 8. Their content and placement are **AI proposals, not approved personal knowledge**.
- Real Python schema/editor/MCP/synthesis and preview/viewer already exist in `mindmap/`. The old `synthesize_research.py` has a different historical candidate graph; its current save operation rejects replacing the curated overlay when mismatches exist. **Do not overwrite the 61-node file with those candidates.**
- Current Pydantic model has legacy 0–4 tiers and `extra="ignore"`; it can lose unknown metadata **at the backend**, not merely in frontend display. Old `/api/promote` defaults to tier 2, inappropriately conflating draft inclusion with human understanding. **Never use that promotion path.** Preserve source/review context in existing supported fields until a tested schema migration is explicitly authorized.
- The existing end-to-end promotion test writes the actual YAML files before attempting restoration; do not run that test against authoritative working files. Use a disposable/test-isolated checkout.
- The A–M index, [science taxonomy/checklist](bep_ownership_mindmap_taxonomy_2026_10_20.md), [node contract](bep_mindmap_node_contract_2026_10_20.md), [C deep dive](../../presentation/deep-dives/C_reaction_mechanism_2026-10-14.md), [D deep dive](../../presentation/deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md), proposal, roadmap, literature and model audits are source inputs. Check exact file content/line/DOI before assigning source support.

**Read-only evidence limits:** previous ChatGPT reconnaissance checked GitHub files and static logic, not the user's unpushed Windows state or a cloud browser runtime. No need to synchronize with the computer to begin.

## Specific Work goal — ready to send after this handoff

> Use GitHub and your cloud environment to continue constructing the **AI BACKEND SCIENTIFIC REFERENCE MAP** for the BEP acetylene semi-hydrogenation project. The repository is `AsapLoso/project-management-agents` on `devcontainer`; app/data live at `Academics/BEP/Catalysis/mindmap/`.
>
> This ChatGPT session has **already performed preliminary GitHub reconnaissance**. Read scoped repo instructions, BEP `conventions.md`, the [taxonomy/checklist](bep_ownership_mindmap_taxonomy_2026_10_20.md), [node contract](bep_mindmap_node_contract_2026_10_20.md), this handoff, the **original proposal and roadmap**, and the A–M research index. Verify baseline data counts and branch head, and don't repeat frontend discovery.
>
> **Scientific process:** (1) retain the owner-set three scientific disciplines; (2) reason through and propose/refine the fifteen broad AI-reference themes; (3) use the A–M research dossiers one by one to extract source-backed concepts into the scientific graph; (4) add scientifically relevant supporting and missing subjects anchored in the original proposal. **These are heuristics, not rigid stages**: iterate as new evidence changes the taxonomy. There is no fixed maximum depth or arbitrary node quota for this execution, but justify the relevance of any large excursion beyond the proposal.
>
> **Do not halt AI-reference work waiting for per-node owner approval.** This first map is your AI knowledge scaffold, and it may be expanded freely in the **Idea/AI worked out (grey/yellow)** states only. Never mark a node `human_worked_out`, approve it into the owner's separate personal map, or claim human-verified citations. The owner's personal map is **strictly opt-in, on explicit approval of each change**. Do not invent a new storage layout before checking the existing schema/editor and proposing a safe way to express this separation.
>
> Use existing node IDs and sources; protect all 61 existing records from loss. For each new or reorganized concept provide parent, substantial explanatory notes/equations when warranted, scoped source locators, explicit assumptions, limitations and open questions. Avoid automatically promoting literature *hypotheses* into established physical measurements. The published 2019 effective PSSA kinetics and an uncalibrated dynamic surface θ model are **not interchangeable**. Keep duplicates under control with cross-links/proposals rather than erasing old notes.
>
> **Practical first execution slice:** independently audit the existing **Level-2 boundaries and the 28 recent C1 descendants** against the proposal, then develop a coherent evidence-backed next batch (begin with C2 kinetics and its scientific prerequisites, or another topic if the audit shows a more sensible order). Continue through additional proposal-relevant topics as capacity permits, recording a checkpoint after each coherent science section. Do not overinvest in UI, tour, spacing or popup features.
>
> Validate ID uniqueness, all parents, no cycles and unlimited-depth compatibility. Test backend parsing/writing **in an isolated copy**, and never run the mutating promotion integration test against the real files. Do not write new unsupported schema fields unless migration is tested to be lossless.
>
> On a clean feature branch, checkpoint **each logical science edit** into an independently reviewable Git commit, inspect and present its diff following the skill, then commit scoped reference-map research data and record scientific progress/source limits in BEP state/history/checklist. Open a PR for review **without auto-merging**. Report what was actually populated, what remains provisional, what sources support it, any blocked technical backend metadata work, and a next-science cursor. **The PR is a code review mechanism, not a claim of owner scientific understanding.** STOP when your coherent execution pass is ready for review.

## Exclusions and unresolved engineering decisions

- **Out of scope for this execution:** frontend redesign and local device synchronization.
- **Future engineering:** source-preserving backend parser/schema migration, independent metadata for maturity / inclusion approval / citation verification / owner-authored record, and robust non-promoting UI actions. These affect data integrity but do not justify blocking ordinary AI-reference content drafting.
- **Personal map writes:** forbidden without the owner's actual, change-specific approval. A global permission to build AI reference material is not permission to write owner understanding.
- **Open scientific judgments:** C1/C2 boundary and the fifteen theme boundaries can evolve; mechanistic alternatives and periodic yield improvement remain questions, not validated results.

## Session-handoff limitations

The local [session-handoff](../../../../.agents/skills/session-handoff/SKILL.md) expects OpenCode logs/session-ID, local working-tree inspection and quarantine facilities. These were not available in this GitHub-only ChatGPT environment. This durable file is an authoritative **scoped handoff**, not a false claim that all local tool-dependent steps were executed.
