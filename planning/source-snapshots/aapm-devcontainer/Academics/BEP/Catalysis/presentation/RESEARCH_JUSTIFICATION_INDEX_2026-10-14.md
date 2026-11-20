> **GESPREKSSTATUS: K = GEDEELTELIJK GEËVALUEERD; L EN M = NIET BESPROKEN / NIET GEËVALUEERD.** De Markdownonderzoeken van L en M zijn door de assistant opgesteld, maar de gebruiker heeft die inhoud nog niet samen met ons besproken. Behandel geen van deze drie letters als volledig geëvalueerd of als goedgekeurde presentatie-inhoud.

# BEP presentation — research index: why this physics, why this model, what has been learned?

**Presentation structure / all current files:** [PRESENTATION_STRUCTURE.md](PRESENTATION_STRUCTURE.md) · [deep dives](deep-dives/). This A–M index is the research taxonomy, not the final slide order or spoken script.

**Revised:** 2026-10-14 · **Status:** source map and deep-dive agenda, **not** an approved slide order or final choice of model.

> [DECISION: user, 2026-10-14] **Give the old and the newer code equal scientific attention.** Neither should merely serve as the other's failed prototype. Investigate *why* physical assumptions, reaction mechanisms, parameters, representations, numerical methods and validation routes differ.
>
> [DECISION:] The previous six headings A–F were too broad. The new **A–M index is a research-question taxonomy**, not 13 compulsory slides. Each heading is a separate potential discussion across messages. In particular, **G (numerics) must not implicitly assume that both implementations use the same algorithm**, nor should one algorithm be treated as mandatory without evidence.
>
> [DECISION:] Read original sub-narratives as ideas and testimony, not as conclusions. Keep raw stories separately in [01 — state space](sub-stories/01_three_concentrations_to_state_space.md), [02 — proposal to optimisation](sub-stories/02_proposal_to_predictive_optimization.md), [03 — Urmès 2019→2022 and continuous pellet distribution](sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md), [04 — necessary fidelity and weak-effect identification](sub-stories/04_model_fidelity_and_identifiability.md), and [visual gags](sub-stories/visual_gags.md).

## Orientation — two primary code spotlights, three implementation layers

| Line | Where it lives | Physical ambition / what it represents | What it **does not yet** establish |
|---|---|---|---|
| **Legacy transient-model scaffold** (Spotlight H) | [`3_Model/c2h2_hydrogenation_transient_model.py`](../3_Model/c2h2_hydrogenation_transient_model.py), [its audit](../3_Model/state.md), [framework audit](../3_Model/transient_model_framework_audit.md) | Coupled bulk gas, radially resolved pore gas and **dynamic** surface coverages; 11 field types, 1,480 *allocated* coordinates in the documented grid. Useful to explain the modelling ambition and why internal states matter. | Active chemistry with default constants, correct/complete physical and numerical closure, an independently verified reacting prediction. The legacy numerical defects matter. |
| **Newer modular `pbr` package** (part of Spotlight I) | Documented in [scientific-method Wayfinder](../research/wayfinder/scientific_method_selection.md) and [alternate implementation audit](../research/dossiers/scientific_wayfinder_2026_10_13/alternate_implementation.md); package source is described as a local sibling `Methanol-Catalysis/pbr/` | Reusable kinetic laws and parameters, flow/model utilities, callable inlet forcing, test infrastructure. Published steady/PSSA kinetics can provide a reacting baseline. | That optional relaxation/coverage states actually feed back into gas reaction rates, or that it implements the proposed non-PSSA elementary surface kinetics. |
| **New reacting vertical slice** (part of Spotlight I, distinct from `pbr`) | [`hermes/reacting-vertical-slice-2026-10-13` branch](https://github.com/AsapLoso/project-management-agents/tree/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model) and its [reactor script](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) | Builds a reacting 1D reactor around imported Urmès 2019 LHHW/PSSA kinetics; includes constant/periodic inlet gates, uniform and radial-pellet paths, analytic-Jacobian work, sensitivity study and receipts. | A verified, general non-PSSA transient surface model, a proven periodic **yield improvement**, experimental validation, or clean reproduction without the required local sibling dependency. |

**Important:** This is not a linear "old → universally better new" evolution. It is a scientific trade-off: the older framework *aims to resolve surface dynamics* but cannot yet provide credible reacting chemistry; the newer branch *performs reacting numerical experiments* with a quasi-steady **surface** closure. Both can be presented honestly, provided their scope is explicit. The [notebook-first HTML prototype](BEP_Catalysis_Presentation_v1.ipynb) is a separate **transport-only teaching/demo artifact**, not a fourth validated reactor implementation.

### The revised deep-dive map (A–M)

| Module | Distinct research question | Evidence or decision expected from its deep dive |
|---|---|---|
| **A. Scientific objective and success criterion** | What did the project actually promise to predict/optimise, and what would count as success? | Proposal → prediction target → measurable comparison |
| **B. Literature and origin of decisions** | Which papers supplied which ideas, and what did we independently add? | Attribution/provenance tree; unresolved primary-paper checks |
| **C. Reaction mechanism and surface physics** | Which chemistry and site processes do we need to retain? | Network/coverage diagram, assumptions and alternatives |
| **D. Kinetic models and parameter identification** | Why choose these rate laws/constants, and can observations identify them? | Kinetics/parameter provenance ledger |
| **E. Experimental conditions and transport regimes** | Why these operating ranges, scales and simplifications? | Geometry/feed/transport ledger; dimensional estimates |
| **F. Physical balance architecture and state description** | What constitutes the state and how are bulk, pellet and surface coupled? | Comparable equation/closure diagrams for both approaches |
| **G. Mathematical and numerical methods** | Which discretisations, time integration and computational strategies are justified *in each implementation*? | Method comparison with error/cost trade-offs; **no presumed common method** |
| **H. Old-code spotlight: what was actually built and audited?** | What does the 1,480-coordinate scaffold demonstrate, and what does it teach? | Walkthrough, evidence, strengths and limitations |
| **I. New-code spotlight: what changed and what really runs?** | What do the modular `pbr` package and the newer reacting slice actually achieve? | Walkthrough, configuration, evidence, competing closures |
| **J. Verification, bugs and corrections** | Which conclusions survived attempts to falsify them; which were retracted? | Audit ledger with corrected claims and reproducible tests |
| **K. Results, sensitivities and interpretation** | What have simulations actually shown, including negative/failed results? | Figure/receipt ledger and bounded interpretations |
| **L. Periodic operation, fitting and optimisation** | How does a credible predictor lead to input forcing, baseline comparison, calibration or control? | Separate accomplished work, hypotheses and future tasks |
| **M. Presentation synthesis and narrative devices** | How do the two code spotlights and scientific discoveries make one coherent talk? | Storyboard options, evidence labels, visuals and speaker cues |

## Deep-dive briefs

### A — Scientific objective: which question are we answering?

- Read: [master proposal `main.tex`](../0_Project_Management/main.tex), [proposal-to-optimisation sub-narrative](sub-stories/02_proposal_to_predictive_optimization.md), [presentation Wayfinder](../research/wayfinder/bep_presentation_2026_10_14.md).
- Separate the original question about **periodic inlet forcing and ethylene selectivity/yield** from intermediate deliverables (forward solver, calibration, optimisation, experimental comparison).
- Define outputs and comparisons: conversion vs selectivity vs *cycle-averaged ethylene yield*, equal-mean-feed steady reference, admissible forcing, and measured rather than invented criteria.
- Investigate the authority of the submitted proposal PDF versus alternate drafts; don't treat a proposal's hypothesis as a result.
- **Deep-dive deliverable:** one precise scientific question, success criteria, and claims that today's evidence cannot yet support.

### B — Where did the modelling ideas come from?

**Source-provenance correction (user, 2026-10-14):** Berger (2008) was **not deliberately used for the original code**; the supervisor later drew attention to it. Compare it against the model retrospectively, but never misrepresent the software as derived from Berger. Urmès 2019 **is** used for the newer reacting model; Urmès 2022 is a directly relevant **later publication, not yet implemented**. The 2008→2019→2022 history is **not an agreed presentation red thread**. Details and follow-up: [deep dive B](deep-dives/B_literature_priority_2026-10-14.md) and [sub-story 03](sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md).


**Deep dive completed (source ranking, not finished paper-level method selection):** [B — priority literature, source → code → open research decisions](deep-dives/B_literature_priority_2026-10-14.md). **Top four:** Urmès 2022 (most direct transient/periodic predecessor), Urmès 2019 (actual PSSA kinetic parameters in newer reacting code), Berger 2008 (transient bulk/surface model and transport criteria), Larsen thesis (local experiment/steady comparator, some numeric provenance unresolved). Keep Borodziński/Bond 2006/2008, Silveston 1995, Urakawa 2008 as important supporting literature, not substitutes for calibrated data. Important distinction: Urmès 2022 reports **flow oscillations for kinetic identification**; our PP seeks **periodic inlet-concentration forcing and performance**. Novelty and equation compatibility are not yet established.

- Read: [Berger 2008 dossier](../Articles/analyses/dynamic_kinetics_berger2008.md), [framework audit](../3_Model/transient_model_framework_audit.md), [literature collection](../resources.md), [scientific-method literature reuse](../research/dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md).
- Distinguish Berger's time-dependent axial balances/surface states from **our** added radial pellet resolution; distinguish general catalyst reviews from catalyst-specific parameters.
- Compare Urmès 2019 (published kinetic parameter source) with Urmès 2022 (direct periodic-operation lead, full model/SI not yet established in this record); compare Larsen's measured/fitted regime separately.
- Consider Silveston, Urakawa, Borodziński, Froment and Danckwerts for motivation, chemistry, transport and boundary conditions respectively, checking the primary sources and applicable regimes.
- **Deep-dive deliverable:** paper → actual equation/idea → applicability → how it entered each code path; unresolved citations clearly marked.

### C — The chemical story, not merely three arrows

**Deep dive completed (mechanism audit, not final kinetic selection):** [C — source-backed network and code-by-code mechanism comparison](deep-dives/C_reaction_mechanism_2026-10-14.md). **Core:** net `C2H2→C2H4→C2H6` masks dissociative H2 adsorption, acetylene/ethylene competition, vinyl and ethyl intermediates, readsorption and site occupancy. **Legacy** has 3 genuine θ ODEs and compressed two-H steps but zero source-fit constants; **reacting 2019-based** path has published LHHW/PSSA rates and no dynamic θ; **draft PR #3** has 5 dynamic θ but experimental uncalibrated elementary rates. Urmès 2022 reports dynamic microkinetics but full paper/SI not verified. **Unresolved:** choice of single vs multiple sites, parameter transfer Pd/Al2O3→PdAg/SiO2, relative timescales and neglected side reactions. Follow D for parameter identifiability, E/F for regime/conservation.


- Read: [legacy elementary-step scaffold](../3_Model/c2h2_hydrogenation_transient_model.py), [Borodziński & Bond consensus](../Articles/paper_analyses/borodzinskiSelectiveHydrogenationEthyne2006_consensus.md), [Larsen consensus](../Articles/paper_analyses/larsenSemihydrogenationAcetyleneEthylene2024_consensus.md).
- Investigate desired C2H2 + H2 → C2H4 and competing C2H4 + H2 → C2H6, adsorption/desorption, site competition, H2 dissociation, readsorption, catalyst-specific side reactions and omissions.
- Explicitly ask: are surface coverages **dynamic states** or **algebraic/PSSA values**? A published LHHW rate does not automatically specify elementary non-equilibrium surface-rate constants.
- **Deep-dive deliverable:** mechanistic diagram with source-supported retained/ignored steps for each implementation.

### D — Kinetic law, constants and identifiability

**Deep dive completed (parameter provenance/structural reasoning, not calibration):** [D — Table 5, identifiability, three kinetic implementations](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md). **Main finding:** Urmès 2019 source-fitted effective PSSA (r_1,r_2), with fixed K1/K5/N_S versus fitted K2/k4⁰/k7⁰/E4/E7, is what the reacting Hermes slice invokes; the legacy scaffold has 8 zero kinetic constants and the PR #3 non-PSSA variant requires 10 uncalibrated elementary rates. (r_2/r_1) reveals correlated parameter groups (K_2 K_5); no unique recovery of microscopic rates from composite steady parameters. Do not re-use retracted Larsen numbers. Source/catalyst transfer → E; mass/site conservation → F; missing public pbr package / code gates → I/J.


- Read: [`3_Model/resources.md`](../3_Model/resources.md), [Urmès source-check receipt](../3_Model/probes/urmes2019_source_receipt.json), [source-verification script](../3_Model/probes/verify_urmes2019_source.py), [Larsen retractions](../Articles/paper_analyses/larsenSemihydrogenationAcetyleneEthylene2024_consensus.md).
- Separate LHHW/PSSA, non-PSSA elementary dynamics, Arrhenius parameterisations (reference-temperature versus pre-exponential conventions), rates per mass/site/volume and pressure units.
- Mark every number **published / derived / calibrated / assumed / placeholder**, with page or equation, validity range, units and exact runtime use.
- Model identifiability is distinct from simulation: parameter compensation, observable vs hidden states and which experimental perturbations constrain them. Previously **retracted Larsen constants must not re-enter** via a secondary summary.
- **Deep-dive deliverable:** side-by-side mechanism/parameter ledger; unresolved non-PSSA parameter gap explicit.

**[D follow-up, user hypothesis 2026-10-14]** Transient input excitation **may** improve kinetic parameter identifiability compared with steady measurements; this is **not** shown by the existing BEP model. State dimension (legacy 3 θ; draft five θ) differs from independent fit constants (legacy eight k slots; draft ten coefficients plus site density). Urmès 2022 already demonstrates related **flow-modulation** parameter estimation; SSITKA/TAP are research leads, not authorised lab procedures. Details: [D8](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md) and [proposal-to-optimisation sub-story](sub-stories/02_proposal_to_predictive_optimization.md). Future A/M hypothesis framing only.

**[B rerun / D qualification, 2026-10-14]** The user reports Damian recommended *not* adding transport-limitation physics because the additional fidelity was unnecessary in the current scope. Do not claim **all** transport was excluded: axial advection persists, the old model has radial pore fields, the newer baseline assumes a uniform pellet and negligible external film. **Transport/instrument response can mask surface kinetics** and thus challenge the earlier speculative identifiability benefit of periodic forcing. Berger 2008 *already* reviews TAP/SSITKA; user had crossed out TAP as a nonpriority on supervisor advice. Thin catalyst-zone/Y-procedure is a specialised TAP inverse-diffusion method, **not** a recommendation for our PBR. See [B rerun](deep-dives/B_literature_priority_2026-10-14.md) and [D8 correction](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md). Verify exact apparatus, transport timescales and source annotations in E before generalising.

**Short presentation sub-narrative (2026-10-14):** [04 — Noiseless first: can we fit the parameters?](sub-stories/04_model_fidelity_and_identifiability.md). **Only argument to carry into the presentation:** weak physical signatures may be hidden by noise; repeated cycles might help, but first test parameter distinguishability with **noiseless cyclic simulated outputs** under an explicitly chosen model, input and observable. If structurally indistinguishable, 10,000 repeats of the same experiment cannot resolve them; a failed optimiser is not in itself a proof. The **0.12% film concentration difference** is only one illustrative physical screening, **not** a quantified outlet sensitivity. **E is technical background, not a planned presentation section.**

### E — What physical operating regime are we actually modelling?

**Deep dive documented (source/cross-code regime audit, not numerical or experimental validation):** [E — catalyst, geometry, feed, timescales, transport and provenance](deep-dives/E_operating_regime_transport_2026-10-14.md). **Key evidence:** Urmès 2019 source experiment 0.1g Pd/α-Al2O3 +0.5g inert, 4mm ID, 200mL/min, 51–62°C, 1.26bar, Table 7 Carberry 3.3×10⁻⁴, Weisz–Prater 0.017, heat screens; Hermes combines the published PSSA chemistry with partly Larsen-like 75mg/5mm geometry, gamma-labelled support and assumed transport constants. Derived Hermes geometry L≈4.48mm, gas τ≈11.88ms, pore τ≈1.17ms; source 0.12% gas-film screening is *conditional*. **Do not claim** its uniform-pellet radius/tortuosity sensitivity sweep confirms physics: those variables do not enter the default uniform-pellet RHS. Older pressure-unit narrative has additional arithmetic/sign errors logged in E5. **Source Figure 7 p_C2H2=0.95kPa and nominal feed Condition 1 y=1.0% need NOT be identical experimental runs.** Hand off source/boundary-conservation to F and numerical receipt audit to J.


- Read: [transport reference](../1_Transport_Phenomena/pbr_transport_phenomena.md), [proposal](../0_Project_Management/main.tex), [new reacting slice](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py), [unit-correction narrative](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/research/notes/NARRATIVE_hundred_second_pellet_units_bug_2026-10-13.md).
- Inventory temperature, total and partial pressure, inlet species including inert carrier, flow, bed length/void fraction, pellet radius/porosity, tortuosity, catalyst properties and diffusivities. Don't mix operating points from different catalysts as though one measured setup.
- Compare residence, reaction, diffusion and external-film timescales; calculate/adjudicate Péclet, Damköhler, Thiele/effectiveness and film criteria **for a stated configuration**, rather than asserting universal cutoffs.
- Separate what a formula or scale *suggests* from what the implemented numerical solution proves. The pressure-units bug is cross-linked to J.
- **Deep-dive deliverable:** configuration/provenance table and justified transport-regime map (including edge cases).

### F — What physics do our equations and states represent?

**Deep dive documented (equation/state audit, not conservation validation):** [F — bulk, pore and surface inventories; model state vectors](deep-dives/F_conservation_state_space_2026-10-14.md). Legacy: **11 physical field types**, **1,480 allocated** = 80 bulk +800 pore +600 occupied-site states; **140 outer-shell entries** are fixed/constrained/frozen by the current defective code, so a count of potentially evolving assigned derivatives is **1,340**, not a claim of independently identifiable variables. Hermes baseline: 60×4=**240** bulk gas states, reacting **PSSA** source chemistry; optional 60×(4+9×4)=**2,400** radially resolved states, **no dynamic θ**. Draft PR #3 adds five dynamic site occupancies locally but remains uncalibrated/unintegrated. **Derived scientific concern:** in both radially resolved RHS pathways, pellet averaged reaction appears in the bulk RHS *as well as* pore reaction and storage; the physically conservative coupled formulation requires equal/opposite **interfacial flux** in bulk and pore balances. This is **not** a duplicate (C_t) multiplication (already retracted by legacy audit D5); quantify and verify discrete conservation in **J** before asserting an observed failure. **Presentation selection:** a compact bulk→pore→site diagram and complementary old/new comparison, not a derivation of every PDE.


- Read: [sub-narrative 01](sub-stories/01_three_concentrations_to_state_space.md), [framework audit](../3_Model/transient_model_framework_audit.md), [Wayfinder conservation questions](../research/wayfinder/scientific_method_selection.md).
- Compare bulk concentration fields, pellet pore concentrations and optional explicit θ dynamics; how inventories, reaction source terms, pellet averaging and boundary conditions couple without double-counting or unphysical state mutation.
- Describe **physical model choices**, not code performance: plug flow versus dispersion, film versus pseudo-homogeneous interface, radially resolved versus uniform pellet, PSSA versus true surface ODEs, isothermal versus energy balance.
- Revisit “the reactor has a memory”: what constitutes a sufficient instantaneous state; distinguish **allocated numerical coordinates** from independent state variables, and time-varying input from state.
- **Deep-dive deliverable:** two annotated balance/closure schematics, their state vectors, mass/site conservation requirements and a fair explanation of what extra physics each captures.

### G — Mathematical formulation, numerical schemes and computational feasibility

**[G research dive completed, editorial choices still open]** [G — full numerical methods, stiffness, Jacobian and solver feasibility](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md). Both implementations use spatial **MOL**, upwind1 and implicit **BDF**, not an explicit time integrator; new code also includes an unverified TVD2 option and analytic **dense** Jacobian for the 240-state uniform baseline, with a separate optional 2,400-state radial path. Legacy D6 records ~0.016 s per RHS and ~23 s for a naïve 1,480-column finite-difference Jacobian in a historical test; these are **not** new-code performance figures. New resolved Jacobian contains code-visible cross-derivative and shell-coupling questions; numerical verification belongs to J. **User wants full method alternatives available for reflection, not only the retrospective takeaway.** Key F/G issues for Zoë remain **OPEN and UNSENT** in [deck-level agenda](DECK_OPEN_QUESTIONS.md). No accepted slide selection yet.


- Read: [old code and audit](../3_Model/state.md), [scientific-method map](../research/wayfinder/scientific_method_selection.md), [new solver/Jacobian narrative](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/research/notes/BUG_NOTE_bdf_jacobian_cost_2026-10-13.md).
- **Open comparison questions:** finite volume vs finite difference vs collocation; MOL vs full discretisation; explicit vs implicit vs IMEX integration; BDF vs Radau/other justified candidates; sparse/analytic/finite-difference Jacobians; grid design and convergence; stiff versus non-stiff ranges.
- For *each* implementation, report **what is actually used**, why it was chosen (or inherited), errors/limitations, and whether any proposed alternative has been run or merely discussed. Do **not** accidentally imply that the new code lacks MOL/upwind/central/BDF or that both use identical numerical treatment.
- Separate spatial discretisation from implicit time stepping; parameter fitting loops from feedback control loops. Performance is part of numerical feasibility, not proof of physical correctness.
- **Deep-dive deliverable:** algorithm-by-algorithm comparison, dimensionality/cost/accuracy gates, and reasons to keep/change each choice.

### H — Spotlight: legacy 1,480-coordinate scaffold

- Read: [original script](../3_Model/c2h2_hydrogenation_transient_model.py), [execution defect register D1–D6](../3_Model/state.md), [two distinct audits](../3_Model/transient_model_framework_audit.md), [audit probe](../3_Model/probes/audit_2026_09_30.py).
- Walk through the architecture, state packing, reaction/surface equations, 20×10 mesh, boundary handling, explicit θ derivatives, transport terms, BDF integration; explain what mathematical problem this script *attempted* to solve.
- Show **independent forensic progress**: why the code audit found state mutation, centre symmetry errors and missing coverage-shell derivatives; distinguish genuine defects, modelling choices, conventions and unresolved scientific questions.
- Clear boundary: zero kinetic tuples in this tracked scaffold, known defects, and no validated reacting transient selectivity claim. Transport can still evolve when rates are zero.
- **Deep-dive deliverable:** self-contained old-code walkthrough with one tested mathematical insight, one audit demonstration and precise limitations — **not just a “before” slide**.

### I — Spotlight: modular kinetics and the new reacting vertical slice

> **🚩 OVERWEEG — NIET BESLOTEN (user, 14 October 2026).** The **only current presentation candidate** from I is the short bridge *original model scaffold → published reacting LHHW/PSSA rates → time-dependent inlet excitation → predicted outlet*, explicitly **without** claiming periodic yield improvement or dynamic surface kinetics. [Short optional narrative 05](sub-stories/05_reacting_model_inlet_candidate.md). **Do not lock this into slides.** The user found the deeper technical I material insufficiently interesting for now and **deliberately deferred a full I deep dive**; keep the existing research pointers below for J/K/future, not a task to execute immediately.


- Read: [`pbr` audit](../research/dossiers/scientific_wayfinder_2026_10_13/alternate_implementation.md), [new vertical-slice script](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py), [branch mission](../research/briefing/REACTING_REACTOR_VERTICAL_SLICE_2026-10-13.md), [sensitivity code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/sensitivity_study.py).
- Treat **modular `pbr` library** and **reacting slice built on top** as distinct layers, not the same file/repository. Compare source-backed Horiuti–Polanyi LHHW kinetics, PSSA closure, configurable 1D flow, uniform/radial pellet versions, source/test gates, analytic Jacobian and actual run evidence.
- Why a PSSA reacting baseline matters: it supplies a defensible chemical reference; why it does not settle the proposal's dynamic-coverage question: surface coverages need not affect reaction rates as evolving states. Neither dismiss nor over-credit this approach.
- **Dependency warning:** the vertical slice searches for a local sibling `Methanol-Catalysis/pbr`; the connected `AsapLoso/Methanol-Catalysis` default `main` inspected on 14 October did not contain that directory. Reproduction therefore requires a pinned copy/commit of the actually used `pbr` source.
- **Deep-dive deliverable:** independent new-code walkthrough with one sourced reacting result and its limitations, plus an explicit old-vs-new **scientific** comparison.

### J — Verification, adversarial checks and the stories of changed conclusions

- Read: [old D1–D6 audit](../3_Model/state.md), [scientific-method verification tickets](../research/wayfinder/scientific_method_selection.md), [audit of the withdrawn ~116.6 s pellet claim and diffusivity-unit correction](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/research/notes/NARRATIVE_hundred_second_pellet_units_bug_2026-10-13.md), [Jacobian-cost note](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/research/notes/BUG_NOTE_bdf_jacobian_cost_2026-10-13.md).
- Include invariants: atomic/site balance, positivity, boundary behaviour, limiting analytical cases, zero-kinetics control, mesh/tolerance convergence, Jacobian finite-difference spot checks and direct source-to-runtime parameter matching.
- **Retraction/correction story to audit before slides:** the former **116.6 s** claim is withdrawn; the note says “wrong by a factor of 1000”, while the endpoints **116.6 s → 1.17 ms** and **1.45e−10 → 1.45e−5 m²/s** imply roughly **100,000×**, not 1000×. The ~1.17 ms replacement still needs its inputs and diffusivity convention checked before it is used as a scientific result. The physical reversal is important, but the numerical wording is internally inconsistent.
- Old “pellet is the bottleneck” note is explicitly **retracted** by the follow-up; do not quote it as a valid result. The Jacobian story is valuable, but avoid extrapolating timing claims without bench-specific reproduction.
- **Deep-dive deliverable:** *claim → test/receipt → confirmed, disputed or retracted → consequences for model choice* ledger.

### K — What results exist, and how do we interpret them?

**NIET VOLLEDIG GEËVALUEERD — ALLEEN K.** Alleen de conclusie dat voorlopige simulatoroutputs geen voldoende gevalideerde reactorresultaten zijn, is besproken. De oorspronkelijke bespreking over werkende reacting baseline, conversie/selectiviteit, parametergevoeligheid, periodieke eindconcentratieproef en J-gerelateerde tests blijft **TER EVALUATIE**. Zie [K — checklist open inhoud](deep-dives/K_results_validation_status_2026-10-14.md).

**[USER DECISION 2026-10-14 — no sufficiently validated reactor result for presentation yet.]** [K — results validity/status note](deep-dives/K_results_validation_status_2026-10-14.md). Numerical output exists in the Hermes sensitivity receipt, but because physics/solver inconsistencies and missing verification remain, **do not promote 9.30% conversion or 76.93% net selectivity to scientific conclusions**. A recorded computed output is not the same as a valid reactor prediction; *bug-free* is not a literal requirement, but appropriate validation is. Sinusoidal inlet code exists, but periodic gain, output phase and cycle-averaged yield improvement have **not** been established. Keep K as a **status/evidence check**, not an automatic results slide; J owns the remaining verification questions. The 13 October briefing's claim that reacting code/periodic forcing is wholly absent is superseded by the later Hermes branch, without making that branch scientifically validated.


- Read: [current Wednesday plan](WEDNESDAY_DECK_PLAN_2026-10-14.md), [supervisor briefing](../research/briefing/BEP_SUPERVISOR_BRIEFING_2026-10-13.md), [new sensitivity receipt](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/evidence/vertical_slice/sensitivity_receipt.json), [new frequency-response source](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/frequency_response.py).
- Distinguish a saved transport demo, package/source checks (24/24), test-suite passes (37), coverage-range matches (**10/12**, not stale 11/12), reacting numerical snapshots, sensitivity sweep and a genuine sustained periodic comparison. Never aggregate these into “model validated”.
- The sensitivity receipt includes baseline conversion/selectivity numbers for one assumed configuration; it also reports **negative ethylene selectivity at a high-temperature point**. Investigate the metric/physical regime and numerical state before selecting plots.
- The frequency-response script has exploratory text referring to a `[tau_res, tau_p]` band even after the unit correction inverted their ordering; execution output/receipt was **not located in the checked branch directory**. Treat its inference as unverified.
- **Deep-dive deliverable:** results inventory with exact commit, execution command, output arrays, provenance, numerical sanity and one sentence of what the observation does/does not mean.

### L — From predictor to fitting, periodic operation and optimisation

**NIET BESPROKEN — NIET GEËVALUEERD — LETTER L.** Het onderzoeksdocument is door de assistant geschreven maar de gebruiker heeft de volledige L-inhoud nog niet geëvalueerd. Geen goedgekeurde inhoudelijke selectie of slides.

**L researched (14 Oct 2026), editorial selection still open:** [L — fair periodic comparisons, PSSA vs true surface memory, input splines and optional pellet populations](deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md). **Core conceptual distinction:** compare periodic feed not just to a steady feed at the *same mean*, but eventually to the **best admissible steady feed** at fair reactant/throughput constraints before asserting a “steady yield cap” was beaten. Proposed period-integrated **net** ethylene metric must subtract ethylene **already present in the inlet** and be measured only once the reactor has reached a periodic response. PSSA gas-only models can produce time-dependent outlet dynamics through transport/nonlinear rates **without actual evolving adsorbate θ**; a PSSA periodic gain (if ever observed) does **not** prove surface-memory mechanisms. B-splines are input trajectory controls, not a reduced model for physical states. **No scientific periodic gain, validated forward reactor, or optimised waveform has been established.** Pellet-radius distribution in one shared-bulk reactor remains a separately **deferred** idea under [sub-story 03](sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md). Keep full letter material for the user's selection; **do not auto-promote to slides**.


- Read: [sub-narrative 02](sub-stories/02_proposal_to_predictive_optimization.md), [master proposal](../0_Project_Management/main.tex), [scientific-method decision map](../research/wayfinder/scientific_method_selection.md).
- Distinguish (1) forward simulation, (2) inverse parameter estimation, (3) open-loop inlet trajectory optimisation, (4) closed-loop reactor feedback and state estimation, (5) implicit numerical integration. These are different axes, not alternatives in one menu.
- Does a PSSA kinetics model respond dynamically through residence/transport alone? Yes in principle; it does **not** demonstrate dynamical adsorbate memory. What evidence could discriminate the two in periodic forcing?
- B-splines parameterise an inlet **control waveform**, not the full reactor state. A claim of periodic advantage needs a scientifically fair steady reference and cycle-averaged metric, not merely an oscillatory outlet.
- Wind-farm/Van Wingerden structural analogy may be a separate future research motivation, **not** chemical-model justification.
- **Deep-dive deliverable:** logical chain *validated forward model → identifiable parameters/uncertainty → fair baseline → controlled inlet study → eventual optimisation/experimental test*, with status flags on each transition.

### M — Turn research into a coherent talk (without discarding the alternatives)

**NIET BESPROKEN — NIET GEËVALUEERD — LETTER M.** De assistant heeft een eerste editorial review van PR #4 geschreven, maar de gebruiker heeft M nog niet inhoudelijk geëvalueerd of goedgekeurd. Geen geaccordeerde slidekeuzes.

**M editorial review completed 14 October — NO final slide decision:** [M — scientific synthesis of the actual ten-slide PR #4](deep-dives/M_editorial_synthesis_pr4_2026-10-14.md) · [PR #4 (open/unmerged)](https://github.com/AsapLoso/project-management-agents/pull/4). The Work branch contains a **real ten-slide deck, editable bullet DOCX, Markdown outline, speaker cues and evidence checklist**, and its own reported visual QA. **Do not duplicate its output on devcontainer.** Research/editorial priority: scientific question → physical state/MOL → equal old/new code emphasis → kinetics/fidelity distinction → G upwind/stiffness/amplitude+phase caveat → current validity boundary (K) → fair periodic-vs-steady experiment (L). **Potential compression:** Work slides 3+4 overlap (state-space), slides 5+6 may overlap (PSSA/kinetic-information); slide 10 risks mixing too many future lines. 🚩 User has *not selected* I optional Narrative 05 even though Work incorporated it within slide 5. User and Zoë F/G science decisions remain open, unsent; don't imply approval. A/H/J separately remain open research modules. This is not a prescribed new ten-slide script.


- Read: [Wednesday production plan](WEDNESDAY_DECK_PLAN_2026-10-14.md), [narrative 01](sub-stories/01_three_concentrations_to_state_space.md), [narrative 02](sub-stories/02_proposal_to_predictive_optimization.md), [visual gags](sub-stories/visual_gags.md), [current HTML prototype README](README.md).
- Narrative layers: **proposal and original question** → **scientific/model choices** → **old scaffold and discoveries** → **new reacting baseline and discoveries** → **honest comparison, missing bridge and next test**. Neither implementation should be reduced to a footnote.
- A scientific research-talk should explain why each decisive choice was made, not merely show a technical inventory of code, numerical outputs or lengthy notebooks.
- Optional moment: “My poor laptop” handoff to Codespaces, after a measured/comprehensible computation bottleneck. It is a *visual beat*, not a substitute for an evidence slide.
- The two HTML presentations are design/prototype concerns **outside** this source index; their current quality does not decide what is scientifically true. Do not silently promote draft raw narratives or retracted results into final speaker claims.
- **Deep-dive deliverable:** evidence-tagged candidate story beats, which are core/backup, and one justified transition between the two code spotlights. **Not** an automatic 13-slide deck.

## Shared comparison checklist (use in H and I, do not declare a winner prematurely)

| Compare the same axis | Old scaffold (H) | Modular `pbr` + reacting slice (I) |
|---|---|---|
| **Question / purpose** | Physically resolved transient state-space architecture | Source-backed reacting baseline / model experiments |
| **Species and chemistry** | Four gas + three explicitly evolved coverage fields intended; default kinetics zero | Four gas channels in slice; published LHHW rate law with algebraic coverage closure |
| **Spatial physics** | Axial bulk and radial pellet fields both allocated | Axial bulk with uniform or radially resolved pellet path; no explicit dynamic θ field |
| **Numerics** | MOL/upwind/radial finite difference/BDF in checked script, with D1–D6 audit | Check exact branch implementation: upwind, radial flux form, BDF with analytic Jacobian and variants; don't assume inherited implementation details |
| **Evidence** | Independently reproduced defect register; transport-only work separate | Source checks, gate scripts, branch sensitivity receipt and preliminary reacting results, still subject to audit |
| **Scientific limit** | Untested reacting transient coverage prediction | PSSA reacting results cannot alone settle transient-coverage mechanism |
| **What it teaches** | Why modelling memory/states and numerical audits matter | Why sourced kinetics, units, practical solver performance and controlled comparisons matter |

## Suggested deep-dive order (discussion schedule, not deck order)

**Phase 1 — justification:** A → B → C → D → E.  
**Phase 2 — two complete models:** F → H → I; use G to compare their numerical solutions without assuming a prescribed numerical recipe.  
**Phase 3 — evidence:** J → K; correct or quarantine disputed results before using them in a narrative.  
**Phase 4 — meaning and presentation:** L → M; integrate both code stories with the original promise.

Each discussion should end with a small *decision/provenance record*:

| Field | Required content |
|---|---|
| **Question** | What did we try to establish? |
| **Source** | Exact file/page/figure and, for code, branch/commit |
| **Old / new comparison** | What is different, and why is that difference consequential? |
| **Status** | [FACT:] / [DECISION:] / [UNVERIFIED:] / [UNRESOLVED:] |
| **Evidence** | Equation, test, plot, units, comparison or explicit lack of evidence |
| **Presentation hook** | One potential memorable visual or explanation; optional until reviewed |
| **Next action** | Smallest next verification or human modelling choice |

## Experimental bridge: explicit transient surface kinetics (14 October 2026)

[UNVERIFIED: experimental code] [Draft PR #3](https://github.com/AsapLoso/project-management-agents/pull/3) extends the newer reacting vertical slice **optionally** with five evolving surface species (H*, C2H2*, C2H3*, C2H4*, C2H5*) and site/atom-balanced adsorption/reaction fluxes, without changing the default Urmès-2019 PSSA path. The stand-alone algebra module and five local unit checks pass; the **full reactor has not been executed** using these equations, and the elementary kinetic constants are **not sourced**. No demonstrated advantage or validated transient site dynamics follow.

- Relevant deep dives: **C** (elementary steps, mechanism), **D** (kinetic parameters and identifiability), **F** (dynamic θ and gas/surface inventory), **G** (stiffness and Jacobian), **I** (new code spotlight), **J/K** (validation and claimed results).
- [Technical note in experimental branch](https://github.com/AsapLoso/project-management-agents/blob/experiment/non-pssa-surface-2026-10-14/Academics/BEP/Catalysis/research/notes/NON_PSSA_SURFACE_BRIDGE_2026-10-14.md) clarifies exact implementation and adoption gates.
- **Why it matters:** Urmès et al. (2022), [DOI 10.1002/cctc.202101826](https://doi.org/10.1002/cctc.202101826), reports a transient single-site microkinetic acetylene-hydrogenation model under periodic flow. Its abstract and supporting figures are available; complete mechanistic equations and independently estimated rate constants require full-paper verification before the new experimental bridge is scientifically calibrated.

## Deferred outlook — narrative 03 (not on today's implementation path)

[DECISION: user, 2026-10-14] [Sub-story 03](sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md) records **two future extensions**: (1) source-backed non-PSSA elementary surface kinetics (experimental [draft PR #3](https://github.com/AsapLoso/project-management-agents/pull/3) is only a start), and (2) **one reactor coupled to a continuous pellet-radius distribution**, rather than independently simulating a few pellet sizes. The second asks whether a size distribution broadens/shifts transient responses and practical feeding performance, with population-weighted rates and shared bulk transport.

This is **outlook under L/M**, informed by C/D/E/F, not a new stand-alone slide or immediate programming task. The question of *novelty relative to Urmès 2022* is unresolved and must be researched later. A–M are **research categories**, not chronological presentation slides. Preserve both code spotlights in H and I. **Defer implementation and experiments.**

### Cross-cutting safety rails

- Do not confuse **a literature-reported parameter**, **an engineering assumption**, **a numerical result**, **a proposed mechanism**, and **an experimentally validated effect**.
- Check versions: at this revision `devcontainer` contains the presentation/index; the reacting-vertical-slice work remains on the separate `hermes/reacting-vertical-slice-2026-10-13` branch. It is not yet a pinned fully reproducible build from a fresh GitHub checkout.
- Be sceptical about internal inconsistencies even when they appear in strongly worded narrative files. The 1000× versus 100000× units mismatch is an explicit pending correction.
- No final choice of model, kinetics, physical closure or control strategy is made by this index; those remain research and owner/supervisor decisions.
