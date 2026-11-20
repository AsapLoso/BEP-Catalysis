# Handoff — BEP manual personal-map work and separate citation-audit mission

**Snapshot:** 2026-10-22. **Authoritative material is GitHub, not memory or chat compression.**

## Entry points (two distinct workstreams)

### A. Owner-directed scientific personal map — resume a conversation

Repo: `AsapLoso/project-management-agents`  
Manual branch: `research/bep-manual-map-session-20261022`  
Unmerged draft PR: https://github.com/AsapLoso/project-management-agents/pull/182  
Directory: `Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/`

**Read in order:** `state.md` (authoritative current frontier), `current_map.yaml` (actual owner-led hierarchy and scientific content), `bridges.yaml` (unplaced ideas), `reference_map.yaml` (AI reference pointer) and `NODE_TEMPLATE.yaml`. The original `../SESSION_STATE.md` is a secondary pointer, not more authoritative than `state.md`.

**Current state when this handoff was written:**
- Exactly **8 records** in `current_map.yaml`: BEP root, Physics, Mathematics, Systems & Control, and **four** Reaction Chemistry & Pathways tree records.
- Current Physics structure approved **for placement only**: `BEP → Physics → Reaction Chemistry & Pathways`, with three sibling children: `Acetylene hydrogenation — net reactions`, `Alternative microscopic pathways`, `Pathway viability across regimes`.
- **Active navigation frontier:** `own_ph_alternative_surface_paths` (second of those sibling children). **Next candidate, NOT added:** `B-ALT-01` (surface-bound hydrogen-addition/intermediate branching); another bridge is `B-ALT-02` (ethylene desorption vs further surface hydrogenation).
- Chemical net equations `R1 C2H2+H2→C2H4`, `R2 C2H4+H2→C2H6`, `R3 C2H2+2H2→C2H6` are *all explanatory content within the net-reaction node*. `R3=R1+R2` stoichiometrically; this does NOT verify a separate fitted kinetic pathway. Optional R1/R2/R3 deeper branches are **bridges**, not yet inserted; see latest `bridges.yaml` and Wayfinder file `research/wayfinder/bep_reaction_pathway_evidence_2026_10_22.md`.
- **Owner scientific text:** AI-worked-out, **unread**, and content **unapproved**; citation-to-claim evidence remains AI level; **no human-worked-out/blue and no human-verified citation**. Owner's accepted structure is independent of reading/approval of notes or knowledge level. Earlier snapshots stating the whole structure was unapproved were superseded by a later explicit structural decision—always trust latest actual state.
- The user wants to *reclaim their BEP intellectually*: traverse one child at a time, use rich scientific nodes and source references, ask only useful scientific questions (no elementary oral quizzes). If a topic arises too early, park it in `bridges.yaml`—particularly spatiotemporal reactor behavior, autonomous state-dependent dynamics, MOL and the film-flux detail.
- Preserve three scientific working files: `current_map.yaml`, `reference_map.yaml`, `bridges.yaml`; supplementary `state.md` and `NODE_TEMPLATE.yaml` are instructions, not additional maps. Change only the active owner-map branch after explicit placement decision, and update the state after every material decision.
- Citation-linked current-map records contain preliminary AI source-node mappings to the older 143-node snapshot, **not** passage-level quotes. Some attachments may be overly broad; do not silently mark them verified.
- **DO NOT merge PR #182 into `devcontainer`** as its underlying experimental ancestry differs and may remove the legacy overlay. Replay reviewed paths through a safe additive PR when user requests integration.

### B. Autonomous citation audit — run as new Work goal

Open integrated AI scientific reference PR: https://github.com/AsapLoso/project-management-agents/pull/180  
Branch: `work/bep-integrated-reference-map-v1-20261022`; prior verified head: `1cd680f95902a0a79b17afb084fa29ab49c6b25f`. **Re-check latest head.**  
Scientific data: `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/` (143 nodes, 65 source/context records, 340 citations as verified 2026-10-22). Includes full literature/provenance, link and reconciliation records, validation, research backlog and unresolved uncertainties.

**The work instructions were deliberately saved on the manual branch, not PR #180** so they don't interfere with the autonomous science graph. Read [WORK_GOAL.md](WORK_GOAL.md) followed by [EXECUTION_PLAN.md](EXECUTION_PLAN.md). For actual execution, create a **new branch from latest PR #180 head and an unmerged PR against `work/bep-integrated-reference-map-v1-20261022`**. Suggested exact output folder: `.../integrated_reference_map_2026_10_22/citation_audit/`.

Citation requirement: `owner node → AI reference node/claim → source ID → precise inspected passage and short quotation → interpretive scope`. Quotes and locators must be real; absent/inaccessible must be marked as such, not hallucinated. AI-side re-auditing after a compaction or major batch must reopen the source, not merely trust prior summaries; `AI-checked` is never `human_verified`.

**Node writing stages** are Idea / AI worked out / Human worked out / Informal Writing / Formal Writing. **Citation authority** is an independent AI versus Human status. **Reading status**, **structural placement**, **content approval**, and **scientific understanding** are additional independent dimensions.

This audit is a separate Work goal. It must not mutate owner-map science, advance the personal tree, or auto-promote sources.

## Source-truth and known gaps

- There is a prior manual scientific transport note at `../01_gas_film_pellet_transport.md` about bed/pellet flux normalization. Supporting AI material; not a currently traversed owner node.
- The manual `reference_map.yaml` pins the AI reference head and contains one independent literature lead: Bos et al. (1993), **commercial Pd/Al₂O₃ kinetic experiments** (Twente institutional abstract; purported open full PDF not yet fully read in the manual pass), **not present under its unique `bos_etal_1993_kinetic` identity in the 65 source records** at last check. Do not invent a citation ID in PR #180.
- R1–R3 chemistry, multiple microscopic paths, and conditional viability by catalyst/operating conditions require bounded source evidence. Beware Bos direct-path statement (review, abstract only), Mei 2009 KMC idealized Pd/PdAg (abstract/preview), and Urmès 2019 full text (Pd/α-Al₂O₃, not target PdAg).
- Scientific research waves SG1–SG4 already improved the AI map. Validation passed structural checks, **not all scientific truth**; several inherited citations remain uninspected, and no target-catalyst periodic gain is established.

## How a different chat should resume

For **manual ownership discussion**, begin with: "Read the most recent GitHub `owner_working_map/state.md` and the active node on branch `research/bep-manual-map-session-20261022`; continue only one branch level without changing reading/approval statuses."

For **the new Work citation campaign**, paste [GOAL_PROMPT.md](GOAL_PROMPT.md) into a fresh cloud-only Work session. It explicitly points to GitHub's complete `WORK_GOAL.md` and `EXECUTION_PLAN.md`, includes the safe branch relationship, and requires actual evidence production and an unmerged PR.

When updating any of these files, verify the remote SHA, preserve concurrent changes and record Git commit/diff; no promises of background work in a normal chat.
