# BEP scientific-map comparison and reconciliation update

**Status:** AI-authored scientific comparison and proposed taxonomy. All content remains provisional at Idea / AI-worked-out maturity; this update does not certify personal understanding, human citation verification, or approval.

## Scope and snapshots

This is an update to the 21 October comparison, using its immutable original-map and independent-v2 snapshots and the later integrated research snapshot as an evidence and structure update.

| Dataset | Immutable identity | Coverage |
|---|---|---|
| Original AI reference map | `devcontainer` commit `f18682d97153251f23396ca7b82fd9dd38f0edf0`; canonical blob `5669f2481cbb24505f49cc5531069553defd8cbd`, overlay blob `5816807c2d3077e367d3a3bb9ce014a76b3112fe` | 4 canonical shell records + 69 draft overlay records |
| Independent reference v2 | `work/bep-independent-reference-v2-20261021` commit `ea391357ad8e4e03cfd27324d4b274513826b254` | 79 nodes + 28 source records |
| Integrated research snapshot | `work/bep-integrated-reference-map-v1-20261022` commit `1cd680f95902a0a79b17afb084fa29ab49c6b25f` | 143 nodes, 65 source/context records, 340 claim-source refs, 59 typed relations, 96 historical attachments, 21 reconciliations, 23 uncertainties |

The original map files and histories, independent v2 files and histories, and previous 144-row source-map crosswalk are preserved. The new proposal adds a 143-row crosswalk from the later integrated graph to its proposed themes. Each row points to its immutable source node; the proposed semantic placement is reviewable and reversible.

## Taxonomy and depth

Only the common root and three discipline IDs align across the original and independent maps. Their concept IDs otherwise differ, so title similarity is insufficient for direct ID merging.

The original overlay is deeper (maximum depth 8) and is strongest in detailed acetylene/Pd pathway and kinetic branches: adsorbed intermediates, sequential ethylene hydrogenation, adsorption/site balances, PSSA rate laws, PdAg-related alternatives, and kinetic bookkeeping. It preserves useful project-specific context and source attachments, while its overlay citation objects have inconsistent claim-level scope and access metadata.

Independent v2 is shallower (maximum depth 4) with explanatory summaries, equations, assumptions, explicit limitations, source access notes, and uncertainty tracking. It strengthens the conceptual scaffolding for physical inputs/measurements, cycle-integrated metrics, parameter uncertainty, periodic-versus-optimized-steady comparisons, and conditional no-gain results.

The later integrated graph grows to maximum depth 7 with 17 depth-two themes. It retains detailed chemistry while adding source-specific model alternatives, a separate physical-instrumentation theme, mathematical optimization, conservative transport and finite-volume derivations, Fisher-information design, periodic-orbit analysis, evidence-class distinctions, 59 typed relations and a broader uncertainty ledger. The 17-theme structure clarifies two boundaries that were collapsed in the first proposal: physical measurement versus state estimation, and mathematical optimization versus the control problem’s objective/feasible set. The mathematical-optimization theme currently has no children in the integrated graph; it needs detailed descendants for optimal-control transcription, local/global optimality, Pareto continuation, and robust comparison.

## Unique scientific contributions

### Original AI reference map

- Deep target-reaction chemistry and catalyst-specific kinetic structures provide useful candidate subtrees: adsorption competition, site occupancy, vinyl/ethyl routes, product readsorption, sequential ethylene hydrogenation, and side products.
- Its centered Arrhenius correction and source-specific rate forms can be retained with equation-level assumptions and units.
- Its content also records project model context and 96 historical source attachments. Attachments are provenance leads; they do not all represent independent publications or claim-level support.

### Independent reference v2

- It treats periodic benefit as an unresolved question rather than a premise.
- It lays out separate limiting cases: stable LTI mean-response equality; Jensen’s inequality for a memoryless concave response; and a weak no-worse optimum only when the steady feasible set is embedded under identical constraints.
- It defines cycle metrics and requires an optimized, physically feasible steady comparator. It follows the manipulated signal through actuator, mixer, bed, outlet and analyzer dynamics.
- It distinguishes information-rich periodic experiments from performance-improving periodic operation.

### Later integrated research

- It retains distinct catalyst-specific closures: Urmès 2019 single-site Pd PSSA; Borodziński–Cybulski’s deposit-associated A/E fitted model; Stytsenko et al.’s Pd–Mn adsorption-substitution proposal; Dehghani et al.’s industrial Pd–Ag rate/activity model; and idealized Pd/PdAg and PdAg/TiO2 surface studies. These describe different systems and evidence; they do not jointly identify one target mechanism.
- It derives variable-velocity conservative flux and bed-volume units, finite-volume cancellation, a narrow scalar explicit positivity bound, Fisher-information expressions, persistent-excitation scope, and periodic-orbit conditions.
- It separates campaign-time catalyst activity from within-cycle adsorbate memory and separates experimental observations from fitted predictions or model-derived precision.
- It reports an existing same-agent second-pass audit of ten representative source/derivation checks. That audit is useful additional AI review; it is not independent peer review or comprehensive claim entailment.

## Disagreements and claim corrections

1. **Periodic gain has no universal sign.** Feimer et al. report no rate improvement for the adsorption/desorption model family they analyze; Ziegelhoeffer et al. model a diffusion-limited pellet case where a frequency window improves selectivity; Horn–Bailey give sufficient conditions rather than a universal result. Kaps et al. (2026) report methanol-system periodic results and separate the selected same-time-average-feed experimental reference from their model-based steady/periodic Pareto calculations. None establishes a gain for the BEP target. ([Feimer et al.](https://doi.org/10.1016/0009-2509(82)80051-1), [Ziegelhoeffer et al.](https://doi.org/10.1016/0009-2509(72)80144-1), [Horn & Bailey](https://doi.org/10.1007/BF00934000), [Kaps et al.](https://doi.org/10.1002/cctc.202501403))

2. **Periodic acetylene modeling already exists.** Urmès et al. (2022) use small-amplitude flow oscillations on Pd/α-Al2O3 for kinetic parameter estimation and fitted outlet histories. The accessible publisher abstract does not report a productivity comparison, PdAg target, or fully resolved axial-model scope. The novelty question therefore narrows to target material/model fidelity and an optimized steady comparison. ([Urmès et al. 2022](https://doi.org/10.1002/cctc.202101826))

3. **Kinetic model differences are alternatives, not contradictions.** Single-site PSSA, deposit-associated sites, Pd–Mn adsorption substitution, and PdAg-specific models have different catalyst, support, feed, and evidence bases. Target catalyst composition, pretreatment, and transient data are needed before choosing among them. ([Urmès et al. 2019](https://doi.org/10.3390/catal9020180), [Borodziński & Cybulski](https://doi.org/10.1016/S0926-860X(99)00498-6), [Stytsenko et al.](https://doi.org/10.1016/j.mcat.2022.112750), [Dehghani et al.](https://doi.org/10.3390/pr7030136))

4. **Berger DOI error is bibliographic.** The original overlay binds the catalytic-kinetics review to DOI `10.1016/j.ces.2008.08.012`, which resolves to a nanofluidization paper. Berger et al.’s “Dynamic methods for catalytic kinetics” is DOI `10.1016/j.apcata.2008.03.020`. Correcting the record does not validate every attached equation. ([unrelated DOI record](https://doi.org/10.1016/j.ces.2008.08.012), [Berger et al.](https://doi.org/10.1016/j.apcata.2008.03.020))

5. **Urmès 2019 contains an unresolved internal parameter discrepancy.** The article’s text gives K1 = 611 Pa^-1 from a calculation while Table 5 lists K1 = 13 Pa^-1 fixed. The integrated record preserves the discrepancy; it does not choose one as a target parameter. ([Urmès et al. 2019](https://doi.org/10.3390/catal9020180))

6. **Measurement and inference need separate branches.** Modulation-excitation spectroscopy has detected selected surface species in suitable catalytic systems. This supports a physical measurement theme, while full internal packed-bed observability remains target-specific. Waldron’s estimated precision is a model-design result based on a specified information/error model, separate from raw measurements. ([Urakawa et al.](https://doi.org/10.1016/j.ces.2007.06.009), [Waldron et al.](https://doi.org/10.1039/C9RE00342H))

7. **Transport boundaries remain apparatus-dependent.** Danckwerts-type flux conditions and the abstract-only Mott–Green alternative encode different external-domain interpretations. The target mixer, tubing, bed, exit volume, and analyzer determine the boundary/model partition. No boundary option is promoted as target truth. ([Danckwerts](https://doi.org/10.1016/0009-2509(53)80001-1), [Mott & Green](https://doi.org/10.1080/00986445.2013.871708))

## Source coverage and its limits

The original overlay records 96 historical attachments, while the previous audit found 32 distinct title strings, 15 internal paths, and 5 DOI strings. These include papers, repository documents, project notes, course material, and code references. Attachment count is not publication count.

Independent v2 normalizes 28 source/context records. The integrated source catalog has 65 records, including 19 marked full-text read, 3 abstract-and-preview, and 14 abstract-only; other entries include repository files, bibliographic metadata, and inherited attachment records. These categories describe access and provenance, not evidential weight. Full-text reads still require claim-level locators, and abstract-only records remain bounded to accessible summaries.

Useful primary-source scope checks for this update include the publisher abstract for Urmès 2022, full-text source records for Urmès 2019, Borodziński 2000, Stytsenko 2022, Dehghani 2019, Waldron 2020 and Kaps 2026, and the abstract-level competing periodic-operation cases. The exact access level and limits are recorded per source in the proposed JSON map and the immutable integrated source registry.

## Proposed unified structure

The proposed machine-readable map has 21 nodes: the shared root and three disciplines plus 17 themes. It retains the earlier 144-row source-map crosswalk by reference and adds a new 143-row integrated-node-to-theme crosswalk. Every integrated node maps to its nearest depth-two theme, with root and discipline nodes mapped directly. The proposal adds:

- **Physics:** reaction network/products; catalyst/site/working surface; kinetic law and surface memory; packed-bed/pellet transport; thermal response and catalyst evolution; physical measurements and instrumentation.
- **Mathematics:** stoichiometric/continuum conservation; dimensionless scales; numerical discretization and verification; periodic orbits and conditional no-gain limits; identifiability and uncertainty; mathematical optimization/optimal control.
- **Systems & Control:** plant boundary and input realization; periodic excitation and discrimination; cycle objective and steady benchmark; observability and state estimation; feasibility and robustness.

Cross-links join pathway alternatives to kinetics, catalyst state to identifiability, transport to plant boundaries, measurement to observability, excitation to parameter information, and cycle response to optimization and benchmarking. The full map includes equations, assumptions, evidence classes, provenance, limitations, cross-links, and unresolved questions.

## Open project decisions

1. Target catalyst/support/geometry/preparation and operating surface.
2. Objective, cycle averaging, inlet ethylene handling, conversion floor, and campaign/resource accounting.
3. Available input variables, command-to-bed transfer, total-flow coupling, and hardware/safety limits.
4. Evidence-supported PSSA or dynamic-coverage choice, transport/thermal fidelity, and boundary domain.
5. Calibration, held-out prediction, uncertainty margin, and experimental match required for a gain claim.

These decisions remain open. The map does not assert a gain, chosen mechanism, fitted parameter, human-verified citation, or personal understanding.
