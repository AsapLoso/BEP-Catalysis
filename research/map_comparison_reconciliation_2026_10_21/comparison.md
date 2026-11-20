# BEP scientific-map comparison and reconciliation proposal

**Status:** AI-authored comparison and proposed structure; all scientific content remains provisional at Idea / AI-worked-out maturity. This is not a personal-understanding map, approval record, or merged scientific dataset.

## Scope and immutable source snapshots

This comparison reads two distinct datasets without changing either one:

| Dataset | Versioned location | Snapshot identity | Records |
|---|---|---|---:|
| Original AI map | [`mindmap/data/bep_map.yaml`](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/mindmap/data/bep_map.yaml) plus [`bep_draft_overlay.yaml`](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml) | `devcontainer` at `f18682d97153251f23396ca7b82fd9dd38f0edf0`; file blobs `5669f2481cbb24505f49cc5531069553defd8cbd` and `5816807c2d3077e367d3a3bb9ce014a76b3112fe` | 4 canonical shell records + 69 AI-overlay records |
| Independent map v2 | [`independent_reference_map_2026_10_21/`](https://github.com/AsapLoso/project-management-agents/tree/work/bep-independent-reference-v2-20261021/Academics/BEP/Catalysis/research/independent_reference_map_2026_10_21) | `work/bep-independent-reference-v2-20261021` at `ea391357ad8e4e03cfd27324d4b274513826b254` | 79 total nodes + 28 source records |

The original map’s README distinguishes its four-record canonical shell from the 69-record AI overlay and explicitly says legacy tier labels do not establish owner understanding. This proposal therefore refers to the overlay as AI research, keeps all source node IDs as provenance, and does not write to either original dataset. The comparison branch is based on the independent-v2 branch; the original `devcontainer` history is read-only input.

## Structural comparison

| Feature | Original AI map on `devcontainer` | Independent map v2 | Reconciliation implication |
|---|---|---|---|
| Root and disciplines | One root and Physics / Mathematics / Systems & Control; 69 additional overlay nodes | Same four root/discipline IDs and 75 additional nodes | Preserve those four shared IDs. Only these four IDs overlap; concept IDs otherwise differ, so map identity requires a semantic crosswalk, not ID-based deduplication. |
| Depth and shape | Maximum depth 8; strong parent-child detail in C1 reaction/catalyst chemistry and C2 kinetics | Maximum depth 4; fuller node explanations, assumptions, claim refs and cross-links | Retain the original’s useful deep chemical detail while using explanatory claims and cross-links so depth does not substitute for understanding. |
| Top-level balance | 5 Physics, 5 Mathematics and 5 Systems & Control themes, then a Physics-heavy C1/C2 expansion | 5 depth-2 themes per discipline; 28 Physics, 28 Mathematics and 22 Systems & Control records including each arm | Keep three arms and a small set of coherent themes, then deepen only where distinct concepts require it. |
| Scientific maturity | All 69 overlay nodes have `is_draft: true`; legacy tiers are 0 or 1. Four canonical records do not certify personal understanding. | One `idea` and 78 `ai_worked_out`; no human-worked-out status | Keep proposed unified records AI-only. Structural inclusion, source review and personal understanding remain separate. |

## What each map contributes uniquely

### Original map: unusually deep target-chemistry and project-model detail

The original is strongest in its detailed tree for reaction intermediates and competing paths: vinyl, adsorbed ethylene, ethyl, ethylidene, ethylidyne, secondary ethylene hydrogenation, and possible C4+/deposit effects. It records a specific PdAg thesis LHHW rate closure, full versus reduced site balances, dissociative-hydrogen alternatives, and the important distinction between pseudo-steady surface kinetics and a dynamically forced reactor. That last distinction should be retained: a reactor can have transient gas/transport states even when its surface kinetics are represented by an instantaneous PSSA closure.

It also contributes a centered-Arrhenius correction: the reference-rate form is `k(T)=k(Tref) exp[-Ea/R(1/T−1/Tref)]`; the uncentered `k0` cannot be substituted directly unless `k(Tref)=k0 exp[-Ea/(R Tref)]`. Its overlay explicitly retracts a blanket claim that centering forces a universal parameter-correlation threshold. Keep that correction, but attach it to a claim-specific, correct source.

### Independent v2: stronger conditions, comparison logic and evidence boundaries

V2 makes the forcing claim conditional. It derives limiting no-gain cases for stable LTI systems at settled periodic response and static concave responses, distinguishes nonlinear mean rectification from a guaranteed positive gain, and states the weak optimum-ordering result only when the periodic feasible set contains every steady control under identical constraints. It defines cycle-integrated metrics, calls for a matched optimized steady benchmark, and separates kinetic identification from performance improvement.

It also makes physical input realization and observation explicit: actuator command is not the bed-plane waveform; residence-time distribution, mixing, pellet/film transport, analyzer dynamics, thermal response and catalyst state can all shape measured outlet cycles. Its claim/source structure records access, scope and what each source does not establish.

## Source coverage and a verified citation defect

The original overlay contains 96 source attachments, 32 distinct title strings, 15 distinct internal paths and 5 distinct DOI strings. These are not 96 independent publications: the records mix thesis excerpts, project conventions, code, course materials, dossiers and external sources. Citation objects usually have title/path/section, but no uniform structured field saying exactly which claim a cited span supports.

V2 has 28 normalized source records, including 20 DOI-bearing records, with source type, access/applicability and `does_not_support` boundaries. Count differences are not a quality score; V2 still includes abstract-level records and its `sources.yaml` dataset metadata says edition `v1` while `nodes.yaml` says `v2-enrichment`. That metadata mismatch should be corrected in a later scoped data change.

**Verified bibliographic mismatch in the original overlay:** nodes `centered_arrhenius` and `surface_coverage_dynamics` cite “Berger et al. (2008) Chemical Engineering Science 63” with DOI `10.1016/j.ces.2008.08.012`. The publisher record for that DOI identifies *Nanofluidization as affected by vibration and electrostatic fields*, not a catalytic-kinetics paper. The relevant Berger et al. review *Dynamic methods for catalytic kinetics* is in *Applied Catalysis A* and has DOI `10.1016/j.apcata.2008.03.020`, which v2’s `berger2008` source record uses. The old DOI link cannot support those two cited claims; this is a citation defect, not proof that the rate law or surface-balance claim is false. Recheck the correct article text and locator before carrying those claims into any future authoritative source ledger. ([wrong DOI’s publisher record](https://www.sciencedirect.com/science/article/pii/S0009250908004132); [Berger et al. review](https://www.sciencedirect.com/science/article/abs/pii/S0926860X08001610))

The DOI overlap across maps is three records: Urmès 2019, Mei et al. 2009 and Borodziński & Bond 2006. The original map’s DOI `10.1016/0255-2701(93)87001-B` is not in v2; v2 adds direct periodic-acetylene, PdAg-structure, transport, measurement and periodic-operation literature. Citation granularity and access still need claim-by-claim review.

## Scientific disagreements, alternatives and evidence boundaries

| Topic | Comparison | Resolution proposed |
|---|---|---|
| Does periodic forcing improve performance? | An original overlay note says cycling “breaks” steady trade-offs and that alternating hydrogen feeds prevent over-hydrogenation by stripping hydrides. V2 rejects a universal sign. The primary literature also gives model-specific opposing cases: Feimer et al. report adsorption/desorption models with no rate improvement, while Ziegelhoeffer et al. derive a selectivity/frequency window for a particular diffusion-limited pellet example; Horn–Bailey provide sufficient conditions, not a universal theorem. | Retain the hydride-stripping statement only as an unverified mechanism hypothesis. Make gain/no-gain conditional on the target plant, objective, constraints, waveform and model; compare with an optimized steady point. ([Feimer 1982](https://doi.org/10.1016/0009-2509(82)80051-1); [Ziegelhoeffer 1972](https://doi.org/10.1016/0009-2509(72)80144-1); [Horn & Bailey 1971](https://doi.org/10.1007/BF00934000)) |
| Is periodic acetylene modelling novel? | Urmès et al. (2022) already report small-amplitude periodic-flow experiments on Pd/α-Al₂O₃, parameter estimation and a transient fixed-bed outlet model. The accessible publisher article describes identification/prediction, not an optimized net-production comparison for the BEP’s PdAg catalyst. The full article/SI spatial scope remains unresolved in v2. | Narrow the gap to the actual target catalyst/support, model scope, objective and optimized steady benchmark. Do not claim “no periodic acetylene model exists.” ([Urmès et al. 2022](https://doi.org/10.1002/cctc.202101826)) |
| Which microscopic route and surface are active? | The original map records detailed alternatives informed by the first-principles KMC study of Pd(111)/Pd–Ag surfaces. That study predicts vinyl and ethylidene routes and an Ag effect for its model surfaces. Li et al. combine atomistic modelling and experiments for a specific Pd₁Ag₃/TiO₂ catalyst and identify condition-dependent PdAg surface structure. Neither establishes the active structure/rates of the project’s exact supported catalyst. | Preserve pathway/site alternatives as catalyst- and source-specific. Keep target composition, support, pretreatment and operating-surface state as open inputs. ([Mei et al. 2009](https://doi.org/10.1016/j.jcat.2009.09.004); [Li et al. 2021](https://doi.org/10.1021/jacs.1c02471)) |
| PSSA versus dynamic surface coverages | These are alternative kinetic closures, not contradictory reactor models. A dynamic gas/bed model may use algebraic surface kinetics; explicit coverage ODEs require elementary adsorption/reaction rates and consistent gas-plus-surface balances. | Keep both under one “kinetic closure” theme, with model-selection and calibration evidence required before promoting one as target truth. Urmès 2019 is source-specific supported-Pd kinetics; it does not automatically calibrate a PdAg dynamic-coverage model. ([Urmès et al. 2019](https://doi.org/10.3390/catal9020180)) |
| What is the objective and fair comparator? | Original nodes use “ethylene yield” and discuss selectivity/operating limits; v2 separates yield, selectivity and productivity and requires matched constraints against an optimized steady comparator. This is a metric/design ambiguity, not a scientific contradiction. | Defer the exact objective, feed basis, conversion floor, campaign horizon and safety/hardware constraints to explicit project decisions. |
| Transport, thermal and numerical fidelity | Original nodes contain film/pellet criteria, 1-D balances, MOL, BDF/Radau, heat exchange and runaway concepts. V2 adds conservative balance conventions, RTD and actuator/sensor dynamics, and treats energy/pellet/dispersion extensions as hypotheses to assess. Neither supplies the target apparatus data. | Retain alternatives; use target-specific dimensionless screening, tracer/temperature/transport evidence and numerical convergence before model reduction is accepted. |

## Proposed integrated structure

The machine-readable [`proposed_unified_map.yaml`](proposed_unified_map.yaml) preserves `bep` and the three discipline arms, then proposes five themes per arm. It crosswalks the original overlay IDs and independent-v2 IDs into shared concepts rather than overwriting or renaming either dataset. A–M dossiers and PDC/course material are provenance/cross-links, not required taxonomy ancestors.

The proposed themes combine: (1) reaction network and product metrics; (2) catalyst/site structure; (3) kinetic closure and memory; (4) packed-bed transport; (5) thermal/catalyst evolution; (6) conservation equations; (7) dimensionless scaling; (8) numerical methods and verification; (9) periodic dynamics and average-gain limits; (10) inverse problems and uncertainty; (11) plant/input realization; (12) excitation and identification; (13) objective and steady benchmark; (14) measurement/observability; and (15) feasibility and validation.

Cross-links explicitly connect surface and bed timescales to forcing period, realized inlet and sensor filtering; catalyst-structure alternatives to kinetic identifiability; energy release to feasibility constraints; and cycle metrics to steady/periodic optimization.

## Decisions that require project input before a unified map could become authoritative

1. **Target catalyst:** exact Pd/Ag ratio, support, particle/egg-shell geometry, preparation/pretreatment, feed composition and operating window. These decide which source-specific mechanisms can be carried forward.
2. **Success metric:** maximize net ethylene productivity/yield, selectivity at a minimum conversion, or a multi-objective tradeoff. Decide whether inlet ethylene subtraction, startup/campaign duration, energy and aging costs belong in the score.
3. **Control set:** composition only, total flow, temperature or several inputs; actual MFC/mixer bandwidth, total-flow coupling, pressure and safety limits.
4. **Model fidelity:** retain a PSSA LHHW closure, identify an explicit dynamic-coverage model, and decide which dispersion, pellet, film and thermal states are justified by target evidence.
5. **Evidence threshold:** which target-specific thesis/lab data and held-out dynamic tests would be sufficient to select a mechanism and validate a performance comparison.

These questions are left open rather than decided by the map comparison.

## Validation and preservation record

The comparison used GitHub’s current `devcontainer` tree and the exact independent-v2 branch head above; original file blob SHAs and v2 commit are embedded for reproducibility. The comparison branch changes only this new research folder. Neither `mindmap/data/bep_map.yaml`, `mindmap/data/bep_draft_overlay.yaml`, nor the independent v2 dataset is rewritten or merged. Proposed nodes stay at AI-only maturity; no personal-understanding or human-verified status is created.
