# BEP scientific map v3: what the choices change

**Status:** AI-authored provisional research. This is information for later project decisions; it does not select a catalyst, metric, input, model, or evidence threshold. It does not claim personal understanding or human citation verification.

## What changed from v2

The v2 comparison had 21 nodes: a root, three disciplines and 17 themes, plus a 143-row crosswalk to the integrated research graph and a preserved 144-row crosswalk to the original/independent maps. V3 retains those records and adds 16 new nodes (15 scientific subnodes plus one decision-information theme), 16 cross-links, expanded source evidence, and a critical audit of 16 high-consequence claims in the proposal. The new subnodes focus on the scientific consequences of decisions that can be made later.

The central comparison remains: periodic performance is a target question, not a premise. Positive and null results in the literature are both conditional on their model, catalyst, transport and comparator.

## The project choice domains, with the relevant science

### Catalyst and working surface

The available literature is not one universal PdAg model. Urmès et al. (2019) fit steady tail-end kinetics over a specific supported Pd/α-Al2O3 catalyst. Urmès et al. (2022) use small-amplitude periodic flow oscillations over Pd/α-Al2O3 for parameter estimation and outlet-history prediction. Mei et al. (2009) analyze idealized Pd(111) and Pd–Ag/Pd(111) surfaces with first-principles kinetic Monte Carlo. In-situ structure and industrial catalyst studies add other support/composition/preparation conditions. These are useful competing models and pathway hypotheses; constants and mechanisms transfer only with a material and operating-condition argument.

Information needed later includes the catalyst batch, metal ratio/loading, support phase, particle/egg-shell geometry, pretreatment, run history, feed, pressure, temperature and measured side products. That list explains what makes source applicability checkable; it does not request a selection now.

### Success metric and accounting

For cycle-mean molar flows of acetylene A and ethylene E, candidate definitions include

- conversion: (X_A=(\bar F_{A,in}-\bar F_{A,out})/\bar F_{A,in});
- incremental ethylene selectivity: (S_E=(\bar F_{E,out}-\bar F_{E,in})/(\bar F_{A,in}-\bar F_{A,out}));
- incremental ethylene yield: (Y_E=(\bar F_{E,out}-\bar F_{E,in})/\bar F_{A,in}=X_A S_E), under this stated two-component definition;
- net productivity: ((\bar F_{E,out}-\bar F_{E,in})/m_{cat}), with time normalization already in the cycle-mean flow.

These definitions diverge when ethylene is in the feed, flow varies, side products/deposits matter, or one averages instantaneous ratios instead of taking a ratio of cycle-integrated amounts. A selectivity target also needs conversion or throughput guardrails. A resource objective may include hydrogen, inert dilution, energy, actuator wear or campaign catalyst life. Those choices affect the ranking and can be documented after seeing the available measurements.

### Manipulated input and apparatus

“Concentration modulation” can mean several physically different input paths:

- composition changes at fixed total flow: partial pressures change while nominal residence time may be approximately held;
- total flow changes at fixed composition: reactant delivery and residence time/RTD both change;
- independent or phase-shifted H2 and C2H2 changes: the stoichiometric ratio and competitive adsorption change;
- temperature forcing: a different stimulus and actuator pathway.

A setpoint is not the waveform at the catalyst. MFC/valve response, mixer and tubing holdup, pressure control, bed RTD, exit volume and analyzer sampling can attenuate and phase-shift signals. Literature on switching apparatus warns that mixing and pressure control are material. The plant choice is therefore partly a measurement question: what command can be delivered and verified in the relevant frequency range?

### Model fidelity

PSSA versus dynamic surface coverages is a relaxation-time and predictive-discrimination question. For a local coverage model (\dot\theta=f(\theta,c_s,T)), the slowest stable eigenmode of (J_\theta=\partial f/\partial\theta) sets a local relaxation scale. Compare that scale with the **measured local forcing after actuator and bed filtering**. Rapid command frequency alone does not prove that PSSA fails.

Likewise, a large axial Péclet number screens axial dispersion against advection but does not establish negligible pellet/film resistance, radial gradients, thermal gradients or changing velocity. RTD and target properties matter. First-order upwind can suppress oscillations but adds leading numerical diffusion approximately (D_{num}=u\Delta z/2) in its semidiscrete constant-speed form. That numerical spreading can obscure physical pulse attenuation unless convergence is shown.

### Evidence threshold

Keep these statements separate:

1. **Mechanistic hypothesis:** a proposed adsorbate/transport explanation.
2. **Fitted model:** parameters and a model reproduce the data used for fitting.
3. **Held-out prediction:** the model predicts conditions not used for calibration.
4. **Model-optimized candidate:** a feasible computed cycle under a stated model and constraints.
5. **Experimental gain:** a repeatable measured cycle beats an optimized steady comparator on the same metric and resource basis, with uncertainty.

Periodic excitation can improve parameter information without improving process performance. A simulated optimizer result is not an experiment; a local candidate beating one nominal steady point is not proof against the best feasible steady operation.

## Critical claims corrected or bounded

- The proposal's phrase “fixed thermodynamic equilibrium” confuses a stationary kinetic surface with equilibrium.
- The 40-fold temperature-pulse figure refers to CO oxidation on Pt with thermal actuation. The primary accessible abstract confirms a significant rate increase; a 2026 review supplies the exact 40-fold comparison. The magnitude is not yet rechecked in the primary full text and does not transfer to acetylene feed forcing.
- Ethylene desorption is a plausible PdAg pathway hypothesis in idealized/static models, but periodic desorption caused by inlet concentration waves is not established by the cited acetylene periodic study.
- “Rapid forcing breaks PSSA” and (\tau_{des}\sim T<\tau_{res}) need target-specific timescale evidence; neither is universal.
- “Physically impossible to measure” is too absolute: modulation-excitation spectroscopy measures selected species in suitable lab systems. Full distributed state reconstruction remains a separate observability question.
- Upwind and smooth B-splines are method choices, not proof of physical validity or of a gain. Upwind numerical diffusion and basis refinement matter.
- The proposal alternates among yield, selectivity and production rate. Define a cycle metric before optimization.
- Novelty is narrowed by Urmès et al. 2022: periodic acetylene flow experiments already exist for kinetic parameter estimation. Their accessible abstract does not settle full axial PDE scope or optimization of performance.

The machine-readable claim audit records exact proposal locations, classifications, source IDs, scope limits and unresolved evidence. The new map keeps the owner's choices deferred while making their consequences reviewable.

## Source coverage added or directly rechecked

| Source | Type/access in this pass | Contribution and boundary |
|---|---|---|
| [Urmès et al. 2022](https://doi.org/10.1002/cctc.202101826) | Primary acetylene study; publisher abstract/preview | Periodic flow oscillations for kinetic parameter estimation and outlet-history modeling on Pd/α-Al2O3; no gain claim in accessible abstract. |
| [Zhu et al. 2021](https://doi.org/10.1016/j.cej.2021.131559) | Primary thermal-pulse study; publisher abstract | Fast temperature-control platform and CO oxidation on Pt; distinct chemistry and input. |
| [Monai et al. 2026](https://doi.org/10.1021/acscatal.5c07014) | Open-access perspective; full text read | Summarizes thermal-pulse conditions including the 40-fold CO-oxidation comparison and highlights scale-up, heat-removal and evidence limits; quantitative value remains secondary pending primary check. |
| [Feimer et al. 1982](https://doi.org/10.1016/0009-2509(82)80051-1) | Primary theoretical article; publisher abstract | Model-specific adsorption/desorption family predicts no rate improvement. |
| [Ziegelhoeffer et al. 1972](https://doi.org/10.1016/0009-2509(72)80144-1) | Primary theoretical article; publisher abstract | Model-specific porous-pellet case gives a frequency window that improves selectivity under strong diffusion limitation. |
| [Horn & Bailey 1971](https://doi.org/10.1007/BF00934000) | Primary theoretical article; metadata/indexed abstract | Sufficient conditions, not a BEP-ready necessary-and-sufficient test. |
| [Mei et al. 2009](https://doi.org/10.1016/j.jcat.2009.09.004) | Primary atomistic KMC article; publisher/PNNL abstract and preview | Pd/PdAg pathway and ethylene-desorption hypotheses; not a supported target transient model. |
| [Urmès et al. 2019](https://doi.org/10.3390/catal9020180) | Primary steady kinetic study; full text in inherited registry | One selected Pd/α-Al2O3 steady PSSA fit with its conditions and unresolved K1 table/text discrepancy. |
| [Silveston et al. 1995](https://doi.org/10.1016/0920-5861(95)00101-K) | Review; selected pages in inherited registry | General periodic operation and apparatus-switching context, not target evidence. |
| [Danckwerts 1953](https://doi.org/10.1016/0009-2509(53)80001-1) | Primary theoretical paper; selected original pages in inherited registry | Residence-time distribution and boundary scope, not target PdAg kinetics. |
| [Urakawa et al. 2008](https://doi.org/10.1016/j.ces.2007.06.009) | Primary methods/application paper; full text in inherited registry | Selected modulation-excitation surface-species observations, not complete packed-bed observability. |
| [Waldron et al. 2020](https://doi.org/10.1039/C9RE00342H) | Primary method paper; full text in inherited registry | Transient-flow Fisher-information design in a different chemistry; information gain is not performance gain. |
| [Kaps et al. 2026](https://doi.org/10.1002/cctc.202501403) | Primary methanol study; full text in inherited registry | Cross-system periodic operation and comparator separation, not a transferable acetylene result. |

## Gaps that remain

- Exact primary-text check of Zhu's quantitative 40-fold comparison.
- Traceability of the proposal's referenced local PdAg dataset and its match to the physical target.
- Direct target evidence for catalyst batch/working state, dynamic surface relaxation, axial/pellet transport and heat transfer.
- Target actuator, mixer, analyzer, sampling and safety envelope.
- An explicitly chosen cycle objective and a fair optimized steady feasible set.
- No target simulation, fitting, optimization experiment or validation is included in this map update.

All map content remains provisional AI research. No personal understanding or human approval is claimed.
