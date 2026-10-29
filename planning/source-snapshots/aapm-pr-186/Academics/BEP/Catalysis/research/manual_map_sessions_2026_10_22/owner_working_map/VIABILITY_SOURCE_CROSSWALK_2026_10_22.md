> **RESET NOTE (2026-10-22):** This crosswalk is preserved AI background from **before** the owner's reset. Four previously saved reaction-science nodes are now archived with complete payloads under `bridges.yaml`; the personal `current_map.yaml` is four anchors only. R1/R2/R3 viability candidates all remain **Idea / not in the personal tree**. Even where existing reference material could furnish AI-worked-out scientific explanations, no automatic progression is authorized: discuss the relevant explanation with the owner first and separately obtain any requested map inclusion/content decision. Source inspection levels and human verification are unchanged. Start with **B-V-R1**. Historical crosswalk text below should never be interpreted as present live-node status.

# Viability & Conditions — source/status crosswalk (2026-10-22)

**Purpose:** Record the owner's speedrun question: *Sources? Compare with the current map? Is it AI worked out or Idea?* This is a targeted **existing-source comparison only**. No external literature search, no insertion into owner `current_map.yaml`, no human-approved status.

## Source-of-truth and comparison

- **Personal map:** `owner_working_map/current_map.yaml` on `docs/bep-theme-first-progress-units-20261022` (inherited from manual-map branch). Snapshot has **8 nodes**, including `own_ph_pathway_viability` (`maturity: ai_worked_out`, `owner_read_status: unread`, `owner_content_approval: unapproved`) and `own_ph_alternative_surface_paths` (same scientific status), each containing AI-attached source interpretations. Those are **broader thematic records**, not evidence that separate R1/R2/R3 viability work has been reviewed.
- **AI reference graph:** `research/integrated_reference_map_2026_10_22/nodes.yaml` and `sources.yaml` on `work/bep-integrated-reference-map-v1-20261022`, including `ph_mechanism_choice`, `ph_sequential_path`, `ph_pd_ag_surface`, `c1_acetylene_semihydrogenation`, `c1_ethylene_overhydrogenation`, `c1_parallel_ethane_paths` and `c1_no_independent_direct_rate`. These are AI-developed references, not human-verified facts.
- **Reaction tickets:** `research/wayfinder/bep_reaction_pathway_evidence_2026_10_22.md`, R1/R2/R3 **Idea**. The tickets address reaction pathway evidence and can be reused to trace viability; they are not completed source audits.
- **Current owner design:** two research themes under `Reaction Chemistry & Pathways → Our Reactions` with independent R1/R2/R3 question slots (**six** potential children total). The final per-reaction nodes have **not yet been inserted**.

## Viability branch: what sources support and what they do not

| Proposed independent question | Existing sources/reference IDs | Scoped available AI evidence | Current personal unit status |
| --- | --- | --- | --- |
| **R1** acetylene → ethylene viability | `urmes2019`: `ph_sequential_path`, `ph_mechanism_choice`; `pachulski2012`: `ph_mechanism_choice`; `mei2009`: `ph_pd_ag_surface` | Supported-Pd model/fit and separate PdAg steady-state kinetic model; atomistic ideal-Pd/PdAg comparison. These **motivate** conditions to check, but do not prove a particular R1 microscopic route on BEP catalyst. | **Idea as individual research/progress slot**; parent has AI-worked-out background |
| **R2** ethylene → ethane viability | `urmes2019`: `ph_sequential_path`, `ph_mechanism_choice`; `mei2009`: `ph_sequential_path`; `c1_ethylene_overhydrogenation` (AI contextual net reaction) | Overhydrogenation is represented in existing kinetic/net reaction models. Gas ethylene vs still-adsorbed continuation, site competition and regime-specific contribution remain separately unsettled. | **Idea as individual research/progress slot**; parent has AI-worked-out background |
| **R3** acetylene → ethane (overall/direct-route viability) | `bos_westerterp_1993`: `c1_parallel_ethane_paths`; `mei2009`: `c1_no_independent_direct_rate` (historical AI-attached references); `ph_reaction_network` | R3 is R1+R2 **stoichiometrically**; independent kinetic channel **not established** for BEP. Direct-route literature attachment is abstract/historical and the exact original paper passage was not inspected in this workflow. | **Idea**; no independent target-specific route verified |

The precise phrase **“AI worked out” applies to the *existing broader thematic node and reference material***, not automatically to these newly delineated **per-reaction viability questions**. A child should advance only after an independently scoped, source-aware scientific explanation is written and actually linked to that child. `human_worked_out`, `owner_read_status: read`, and `human_verified` never follow from this crosswalk.

## Concrete source ledger already available (not externally rechecked in this turn)

- **Urmès et al. (2019)**, [Catalysts 9(2), 180](https://doi.org/10.3390/catal9020180), DOI `10.3390/catal9020180`; integrated AI ledger reports **full text inspected**, printed pp. 2–6 and 9–11, especially Table 3/rate equations. **0.05 wt% Pd/α-Al₂O₃, tail-end conditions**; one-site model selected for that study, **not** proof of BEP PdAg site geometry or forcing behavior.
- **Pachulski, Schödel & Claus (2012)**, [Applied Catalysis A, 445–446, 107–120](https://doi.org/10.1016/j.apcata.2012.08.018), DOI `10.1016/j.apcata.2012.08.018`; **publisher abstract only**, selected two-site Langmuir–Hinshelwood PdAg/Al₂O₃ model in the reported steady reactor context; full article not inspected in integrated ledger.
- **Mei, Neurock & Smith (2009)**, [Journal of Catalysis 268(2), 181–195](https://doi.org/10.1016/j.jcat.2009.09.004), DOI `10.1016/j.jcat.2009.09.004`; **abstract/preview only** in integrated ledger; KMC idealized Pd(111)/PdAg-on-Pd(111) acetylene–ethylene surface/feed comparison, **not** experimentally validated BEP packed-bed mechanism or periodic gain.
- **Bos & Westerterp (1993)**, [Chemical Engineering and Processing 32(1), 1–7](https://doi.org/10.1016/0255-2701(93)87001-B), DOI `10.1016/0255-2701(93)87001-B`; **metadata and historical attachment, full text not inspected** by the integrated ledger; not adequate to assert an R3 direct route's contribution on BEP.
- **Borodziński & Cybulski (2000)**, [Applied Catalysis A 198, 51–66](https://doi.org/10.1016/S0926-860X(99)00498-6), DOI `10.1016/S0926-860X(99)00498-6`; **full text recorded inspected** (printed pp. 51–66) in integrated ledger; supports carbonaceous-deposit-associated A/E site model for its commercial Pd/α-Al₂O₃ conditions at 343 K, not a transferable PdAg pathway proof.

## Scientific assessment fields worth storing within each viability node

**Thermodynamic feasibility**, **kinetic accessibility**, **experimental support**, and **dominance under specified catalyst/feed/temperature/coverage** are **internal assessment fields/notes** rather than four automatically-created subnodes. Preserve known/unknown for each separately. “Represented in a fit” ≠ “uniquely measured elementary pathway” ≠ “dominant.”

## Next owner-led action

During the speedrun, use the two-theme/six-question design. For each specific question, start at `idea`, attach the existing **AI reference IDs** and qualified source records, identify the missing empirical/catalyst-specific claim, then decide whether the AI has *actually completed a bounded explanatory writeup*. Don't duplicate existing claims; don't assume all six children have been added to the current personal YAML. Discuss/approve any concrete node insertion or reparenting separately. Updating this note does not authorize graph migration.
