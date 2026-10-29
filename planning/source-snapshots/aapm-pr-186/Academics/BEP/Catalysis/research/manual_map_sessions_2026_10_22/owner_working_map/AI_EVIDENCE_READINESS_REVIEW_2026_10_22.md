# BEP six-question AI evidence-readiness review — 2026-10-22

**Purpose:** Speedrun comparison of EXISTING archived personal-map material, AI integrated reference nodes, and their source ledger. **This is AI-generated review material, not an approved personal scientific-map mutation.** A recommendation below is not a change to the actual stage of a bridge or node.

**Read order / governing decisions:** `README.md`, `SESSION_STATE.md`, `owner_working_map/state.md`, `THEME_FIRST_PROGRESS_UNITS_2026_10_22.md`, `VIABILITY_SOURCE_CROSSWALK_2026_10_22.md`, three owner-map YAMLs, and `.agents/skills/bep-map-edit-review/SKILL.md`. Governing reset: `current_map.yaml` has four anchors only; earlier chemistry records are snapshotted in `bridges.yaml`. Chosen *candidate* structure: `Reaction Chemistry & Pathways → Our Reactions (R1/R2/R3 in-node) → {Viability & Conditions, Microscopic pathways} → {R1,R2,R3}`. Exactly **two** themes and **six** independent questions, no third theme. Neither a theme nor its children have been reinserted.

## Status vocabulary and outcome

- **Actual:** All six question candidates are bridge-stage **Idea**, unplaced; no owner reading/content approval, no human worked out, no informal or formal writing, and no human source verification are recorded.
- **AI-ready recommendation** means a *separately bounded explanatory draft is possible from already read reference material*, **not** that the particular owner unit has changed status. It is eligible for owner content/placement discussion after explanation, not an auto-promotion.
- **Five stages:** Idea → AI worked out → Human worked out → Informal Writing → Formal Writing. Owner reading, approval and per-claim citation verification are orthogonal.

| Bridge / proposed question | AI-ready assessment | Actual personal stage | Main source/reference support | Deliberate limitation |
| --- | --- | --- | --- | --- |
| **B-V-R1** — Which conditions allow C₂H₂ → C₂H₄ in a specified catalyst/regime? | **AI worked out candidate** at qualitative, conditional scope | Idea / unplaced | `ph_sequential_path`, `ph_mechanism_choice`; `urmes2019`, `pachulski2012`, `mei2009` | No mapped BEP PdAg operating envelope / unique elementary route |
| **B-V-R2** — Which conditions allow C₂H₄ → C₂H₆ and how significant? | **AI worked out candidate** at qualitative, conditional scope | Idea / unplaced | `ph_sequential_path`, `ph_mechanism_choice`, `c1_ethylene_overhydrogenation`; `urmes2019`, `mei2009` | No BEP-specific significance / forcing-dependent selectivity |
| **B-V-R3** — When could a distinct C₂H₂ → C₂H₆ route matter beyond R1+R2? | **Remain Idea** for the stated target-specific significance question | Idea / unplaced | `c1_parallel_ethane_paths`, `c1_no_independent_direct_rate`; `bos_westerterp_1993`, `mei2009` | Historical/abstract evidence, no target-specific quantitative bound |
| **Micro-R1** — Which microscopic sequences realize R1? | **AI worked out candidate** as *model-specific pathways*, not established BEP mechanism | Idea / unplaced; existing generic `B-R1` is a separate earlier ticket | `c1_horiuti_polanyi_family`, `c1_vinyl_intermediate`, `c1_adsorbed_ethylene_fork`, `c1_adsorbed_ethylene_desorption`; `urmes2019` | Table-3 arrows/equilibria not owner-verified; supported Pd ≠ target PdAg |
| **Micro-R2** — Which microscopic sequences realize R2? | **AI worked out candidate** as *model-specific pathways* | Idea / unplaced; existing generic `B-R2` is a separate earlier ticket | `c1_adsorbed_ethylene_fork`, `c1_ethylene_readsorption`, `ph_sequential_path`; `urmes2019`, `mei2009` | Adsorbed continuation and gas ethylene readsorption cannot be partitioned by a net rate alone |
| **Micro-R3** — Which distinct pathways yield ethane starting from acetylene? | **Remain Idea** for independent target-route determination; a conceptual distinction is AI-written | Idea / unplaced; existing generic `B-R3` is a separate earlier ticket | `c1_parallel_ethane_paths` (AI worked out conceptual comparison), `c1_vinyl_ethylidene_alternative` (**Idea** in reference), `mei2009`, `bos_westerterp_1993` | Alternative ideal-surface mechanism not demonstrated or quantified for BEP |

**Do not silently create Micro-R1/2/3 bridge IDs** as if the owner approved these as personal graph entries; previous `B-R1/2/3` are generic reaction evidence tickets. This note supplies content for a future explicit decision.

## Compact scientific explanations presented for consideration

### Viability / conditions

**R1:** Adsorbed acetylene and dissociatively adsorbed hydrogen can generate the desired C₂H₄; ethylene must be released instead of further hydrogenated. Site occupation/competition, hydrogen chemical availability and product desorption determine whether selective production is kinetically accessible. The hydrogenation reaction's thermodynamic feasibility alone is not a prediction of rate or selectivity. Existing Pd and PdAg source models cover different catalysts, conditions and effective site descriptions. **Unknown:** calibrated BEP-specific operation and selection under periodic forcing.

**R2:** Both incoming and newly produced gas-phase C₂H₄ can adsorb and become C₂H₆; continuation of adsorbed C₂H₄* can also contribute. Competition for sites and hydrogen, ethylene partial pressure and desorption versus hydrogen addition determine the observed effective channel in a model-dependent way. A fitted R2 rate does not identify a unique elementary origin. **Unknown:** magnitude and reaction-path balance at BEP conditions.

**R3:** `C₂H₂ + 2 H₂ → C₂H₆` is the sum of the R1/R2 net equations. It neither implies a separate microscopic route nor excludes continuous surface conversion without ethylene desorption. A distinct bypass such as the vinyl/ethylidene possibility in model Pd/PdAg KMC requires original-paper and target-catalyst scrutiny before it can be called independently important. **Unknown:** a trustworthy quantitative bound or regime in which an independently parametrized R3 rate matters.

### Microscopic pathways (the second and final chosen theme)

**R1:** A model-specific Horiuti–Polanyi family uses H₂ dissociation, adsorbed acetylene, formation of vinyl (C₂H₃*), further addition to C₂H₄*, then desorption as gas ethylene. Stars denote surface-associated species, not separately measured concentrations. Intermediate coverages and reversibility are source/model-dependent, not guaranteed BEP chemistry. Urmès 2019 pp. 3–6/Table 3 is AI full-text-inspected, but old dossier step-by-step arrows are **not** certified reproductions.

**R2:** Ethylene in the feed or formed in the reactor may adsorb to C₂H₄* and undergo subsequent H additions toward ethane. Alternatively, an acetylene-derived surface intermediate may continue hydrogenating without first desorbing ethylene. A net two-reaction closure cannot determine which ethane molecules follow which route. Existing mechanistic treatment is sufficient for **a comparative candidate explanation**, not target-specific elementary rate constants.

**R3:** Keep (i) the overall stoichiometric R1+R2 conversion, (ii) adsorbed continuation through an ethylene-like intermediate without gas-phase release, and (iii) a bypass of that intermediate as distinct descriptions. Mei 2009 gives an ideal-surface KMC discussion of alternative intermediates; `c1_vinyl_ethylidene_alternative` is **Idea** in the reference graph and Bos & Westerterp 1993 has no full-text-inspected passage in this ledger. No separate `r_direct` for the BEP may be assumed.

## Explicit literature access / evidence limits

- `urmes2019` — 0.05 wt% Pd/α-Al₂O₃ tail-end, 2019 *Catalysts* 9(2) 180, DOI 10.3390/catal9020180; **AI full text read**, especially pp. 2–6, 9–11 and Table 3. Single-site fit for source conditions; not the BEP PdAg catalyst or transient gain.
- `pachulski2012` — Pd–Ag/Al₂O₃ *Applied Catalysis A* 445–446, 107–120, DOI 10.1016/j.apcata.2012.08.018; **AI abstract only**, selected two-site LH model; no dynamic BEP validation.
- `mei2009` — idealized Pd(111) and PdAg/Pd(111) KMC *Journal of Catalysis* 268(2), 181–195, DOI 10.1016/j.jcat.2009.09.004; **AI abstract/preview only**, not target-packed-bed mechanistic proof.
- `bos_westerterp_1993` — *Chemical Engineering and Processing* 32(1), 1–7, DOI 10.1016/0255-2701(93)87001-B; **bibliographic/historical attachment, original full text not inspected** in integrated ledger.
- `borodzinski2000` — Pd/α-Al₂O₃ mixture-kinetics A/E-site model, DOI 10.1016/S0926-860X(99)00498-6; **AI full text inspected**, source-specific only.
- Integrated AI reference: `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/{nodes,sources}.yaml` at `work/bep-integrated-reference-map-v1-20261022`; no new external research campaign undertaken.
- Thermodynamic favorability, kinetic accessibility, experimental evidence and dominance under a given regime are *separate assessment fields*, not four new graph branches. No target-specific free-energy thresholds, rates or site coverages calculated in this pass.

## Owner authorization and exact cursor

**No new structural or scientific approval has been given in this session.** Existing accepted design remains merely the two-theme/six-slot bridge plan. None of the six candidates has actually moved beyond **Idea**. No `current_map.yaml`, `bridges.yaml`, AI reference map, science-code or frontend mutation is authorized merely by this review.

**Exact next owner interaction:** `Viability & Conditions → B-V-R1` — owner to assess the now-presented *bounded* explanation and specify whether its exact content and placement are accepted for insertion as **AI worked out** (without any inference of human reading/understanding/citation verification). After that, handle `B-V-R2` then `B-V-R3`. Scientific summaries for the second theme **Microscopic pathways R1→R2→R3** are prepared above; revisit each for owner scope before actual insertion. If no reply, the status remains Idea, and the cursor stays at B-V-R1. Use parent + immediate R1/R2/R3 siblings in displays; no broad Mermaid styling/colour.
