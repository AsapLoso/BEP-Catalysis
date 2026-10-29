# Global BEP presentation outline

**Can timing the feed favor ethylene?**

Dynamic acetylene semi-hydrogenation · BEP research progress

**Checkpoint:** 14 October 2026 · 10 slides · approximately 9 min 30 s

**Research refresh:** devcontainer 996781c; B–G, optional narrative 05, K status and L outlook read.

**Primary handoff:** [Editable Word outline](BEP_Presentation_Outline.docx), with native text and bullets.

## Central argument

- **Original objective:** determine how periodic concentration forcing changes acetylene semi-hydrogenation and ethylene performance.
- **Physical challenge:** a changing inlet interacts with nonlinear chemistry and retained internal inventories.
- **Modeling development:** the legacy scaffold represents candidate hidden dynamics; the newer PSSA reactor uses published effective kinetics. Their different scopes create a question about necessary fidelity and usable parameters.
- **Mathematical challenge:** conservation, spatial accuracy, time integration and coupled-solve cost determine whether we can interpret a transient response.
- **Current conclusion:** implementation, source checks and mathematical examples establish bounded progress. K supplies no validated reactor-performance result.
- **Next milestone:** Understand and verify the reactor’s transient response before judging the value of periodic feeding.

This is an **elaborated bullet outline**, not a written speech. Projected slides carry the visual argument; the bullets and short context below provide the scientific material to discuss.

## Running order

| Slide | Message | Time |
|---|---|---|
| 1 | Can timing the feed favor ethylene? | 40 s |
| 2 | Two reasons timing could matter | 50 s |
| 3 | Describe where the history lives | 60 s |
| 4 | 11 fields become 1,480 coordinates | 60 s |
| 5 | Reacting gas, quasi-steady surface | 60 s |
| 6 | More states need more kinetic information | 50 s |
| 7 | Compute the transient we mean | 65 s |
| 8 | The grid can change the pulse | 65 s |
| 9 | Know what each result establishes | 60 s |
| 10 | Use the predictor to test and learn | 60 s |

## 1. Can timing the feed favor ethylene?

**Key message:** Periodic inlet concentration is a proposed way to change ethylene performance; its benefit remains unproven.

- Acetylene is an unwanted component of valuable ethylene streams. Hydrogenation removes acetylene but can also consume ethylene into ethane.
- Compare a steady feed with a changing feed under matched reactant budgets and operating constraints. The temporal pattern is the proposed design variable.
- The original proposal asks how concentration forcing changes spatial adsorbate dynamics and intermediary selectivity. A credible forward predictor is the prerequisite for quantitative optimization.

**Context:** The reaction chain introduces why the intermediate matters, including ethylene already present in the inlet. The opening establishes the research question without promising a periodic advantage. Both inlet sketches are conceptual; no reactor-output curve is shown.

**Proposed visual:** Reaction chain, two inlet sketches with the same indicated mean, and a single packed-bed icon.

**Connection to the next part:** Explain why the timing could matter before introducing a model.

**Sources:** [Project proposal, central question and methodology](../0_Project_Management/main.tex) · [C — mechanism and kinetic closures](deep-dives/C_reaction_mechanism_2026-10-14.md) · [02 — proposal to predictive optimization](sub-stories/02_proposal_to_predictive_optimization.md) · [K — preliminary outputs and current result boundaries](deep-dives/K_results_validation_status_2026-10-14.md)

**Claim IDs:** Q01, CH01, K01 · **Time:** 40 s

## 2. Two reasons timing could matter

**Key message:** Periodic effects can arise from nonlinear effective kinetics; independent surface dynamics add another mechanism.

- Competitive adsorption couples the reaction rates to several species. For nonlinear rates, the average response need not equal the response at average local conditions.
- Adsorption, surface reaction and desorption can adjust on different timescales. If coverages evolve independently, the surface retains information about earlier conditions.
- A PSSA surface can still sit inside a dynamic gas reactor. Surface memory is an additional modeled mechanism, not a prerequisite for every possible periodic effect. Neither mechanism guarantees improvement.

**Context:** This distinction keeps the two implementations scientifically relevant. The audience should understand what each closure can represent before comparing state counts. We do not claim that an actual surface-relaxation timescale or beneficial frequency window has been established for the intended reactor.

**Proposed visual:** Two complementary panels: nonlinear competitive rates and a schematic occupied-site surface with independent coverage evolution.

**Connection to the next part:** Locate the internal inventories that could carry a transient response.

**Sources:** [C — mechanism and kinetic closures](deep-dives/C_reaction_mechanism_2026-10-14.md) · [D — effective parameters and identifiability](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md) · [01 — from concentrations to state space](sub-stories/01_three_concentrations_to_state_space.md)

**Claim IDs:** NL01, DYN01 · **Time:** 50 s

## 3. Describe where the history lives

**Key message:** A candidate physical state collects the internal inventories needed to predict the retained dynamics.

- Bulk gas varies along the reactor; pore concentrations and occupied surface sites may add internal storage. Which fields are necessary depends on the regime and observable.
- Conservation balances, kinetic relations, initial conditions and boundary conditions define the model. Inter-compartment exchange must be consistent with the retained inventories.
- Method of Lines discretizes spatial fields while leaving time integration as a separate problem. The resulting state-space form maps prescribed inlet u(t), parameters p and current state x to an evolving outlet y.

**Context:** The state is intended to summarize the relevant past through present physical quantities. This is conditional on the retained physics being sufficient; adding coordinates does not prove model completeness or observability. The three-layer drawing is the legacy modeling ambition, not a statement that all layers are necessary in every operating regime.

**Proposed visual:** Input → bulk profile → pellet pores → surface occupancy, followed by the state-space equation and outlet.

**Connection to the next part:** Show how those fields become the original numerical scaffold.

**Sources:** [F — inventories, state space and conservation questions](deep-dives/F_conservation_state_space_2026-10-14.md) · [G — numerical methods and analytic advection example](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md) · [01 — from concentrations to state space](sub-stories/01_three_concentrations_to_state_space.md) · [Legacy scaffold source](../3_Model/c2h2_hydrogenation_transient_model.py)

**Claim IDs:** MOL01, CONS01 · **Time:** 60 s

## 4. 11 fields become 1,480 coordinates

**Key message:** The legacy scaffold represents a rich candidate state, while its reacting parameterization and numerical closure remain unfinished.

- The documented mesh has 20 axial points and 10 radial nodes: 80 bulk-gas entries, 800 pore-gas entries and 600 surface-coverage entries.
- The three occupied coverage fields have their own intended evolution. This is the architectural route for independent surface memory, beyond instantaneous PSSA closure.
- The total is an allocation count: 140 shell entries are fixed, constrained or frozen in the inspected code. Eight default kinetic prefactors are zero and six numerical defects are documented. These limit reacting inference without erasing the architectural work.

**Context:** The state count is a consequence of physical fields and spatial resolution, rather than a collection of different chemical species. The old code should receive attention on its own terms: explain what it represents and why, then state the specific missing evidence. Do not describe all 1,480 entries as independent physical modes or claim chemical stiffness from a zero-kinetics run.

**Proposed visual:** Axial bed and radial pellet mesh linked to three state-count blocks and one allocation total.

**Connection to the next part:** Separate the ability to write detailed dynamics from the kinetic information needed to calculate them.

**Sources:** [Legacy scaffold source](../3_Model/c2h2_hydrogenation_transient_model.py) · [Legacy executed audit and defects](../3_Model/state.md) · [F — inventories, state space and conservation questions](deep-dives/F_conservation_state_space_2026-10-14.md) · [G — numerical methods and analytic advection example](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md)

**Claim IDs:** OLD01, OLD02 · **Time:** 60 s

## 5. Reacting gas, quasi-steady surface

**Key message:** The newer simulator evolves gas concentrations using Urmès 2019 effective kinetics, without independent surface-coverage ODEs.

- The uniform-pellet baseline combines a time-dependent 1D gas balance with source-backed LHHW/PSSA reaction rates. Its default allocation is 60 × 4 = 240 gas entries.
- Local gas composition determines algebraic surface coverages and rates. The simulator accepts a prescribed inlet, including a sinusoidal acetylene perturbation, while the surface closure remains PSSA.
- Saved preliminary outputs and source checks exist. The current periodic gate compares terminal outlet snapshots; it does not establish settled cycles, harmonic gain/phase or cycle-averaged yield improvement. Source/catalyst/geometry transfer and reproducibility remain open.

**Context:** This gives the newer implementation comparable scientific attention without treating it as a universally superior replacement. The optional radial PSSA configuration has 2,400 entries and separate conservation/Jacobian questions. The source imports a local pbr sibling dependency absent from this repository snapshot. Narrative 05 is used only as the brief controlled-inlet transition within this already selected model comparison.

**Proposed visual:** Prescribed inlet → evolving gas state → algebraic coverages → effective reaction rates; 240-entry uniform baseline badge.

**Connection to the next part:** Ask what can be inferred from effective fitted constants and what additional surface dynamics would require.

**Sources:** [Reacting simulator, pinned Hermes snapshot a842535](https://github.com/AsapLoso/project-management-agents/blob/a84253576a82c33f894b594f0a5b58d6aac3b943/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) · [D — effective parameters and identifiability](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md) · [E — source conditions and reactor assumptions (background)](deep-dives/E_operating_regime_transport_2026-10-14.md) · [F — inventories, state space and conservation questions](deep-dives/F_conservation_state_space_2026-10-14.md) · [K — preliminary outputs and current result boundaries](deep-dives/K_results_validation_status_2026-10-14.md) · [05 — optional controlled-inlet transition](sub-stories/05_reacting_model_inlet_candidate.md) · [Selected Urmès 2019 source-transcription receipt](../3_Model/probes/urmes2019_source_receipt.json)

**Claim IDs:** NEW01, NEW02, DYN01, K01 · **Time:** 60 s

## 6. More states need more kinetic information

**Key message:** Model fidelity must be supported by usable kinetic information and a specified prediction target.

- Dynamic surface equations need parameters governing their individual adsorption, desorption and reaction processes. Effective steady/PSSA parameter groups cannot simply be assigned to every elementary step.
- The Urmès 2019 source fit encountered correlated parameters; five Table 5 quantities were fitted while three were fixed. Reported intervals belong to that source model and regime.
- The richer scaffold and the reacting PSSA baseline address different parts of the problem. A controlled test of added surface dynamics requires matched physical assumptions and a parameterized alternative, rather than comparing unmatched code outputs.

**Context:** This is where literature makes a scientific decision useful: it identifies both the information available for the baseline and the information missing for a more detailed dynamic closure. It also motivates the small later identification hypothesis. Additional states do not automatically create independent measured information or improve prediction.

**Proposed visual:** Two evidence requirements: independent coverage evolution needs elementary rates; effective PSSA kinetics uses fitted parameter groups. A common target links the two.

**Connection to the next part:** Even a chosen, parameterized model must still be solved accurately and at a practical cost.

**Sources:** [D — effective parameters and identifiability](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md) · [C — mechanism and kinetic closures](deep-dives/C_reaction_mechanism_2026-10-14.md) · [E — source conditions and reactor assumptions (background)](deep-dives/E_operating_regime_transport_2026-10-14.md) · [Urmès et al. 2019, Catalysts 9, 180](https://doi.org/10.3390/catal9020180)

**Claim IDs:** PAR01, DYN01 · **Time:** 50 s

## 7. Compute the transient we mean

**Key message:** Numerical accuracy and computational feasibility depend on different, testable parts of the calculation.

- Both inspected production scripts use Method of Lines, first-order upwind axial advection and implicit SciPy BDF time integration. Explicitly retained surface states do not imply explicit time stepping.
- Fast decaying modes can restrict a stable explicit step even when the desired trajectory is slower. Actual stiffness depends on the chosen nonzero rates, transport and numerical boundary treatment; it has not been demonstrated as fast chemistry in the zero-kinetics scaffold.
- Neighboring transport cells and local chemistry create structured couplings. The legacy dense finite-difference Jacobian is costly; the newer analytic Jacobian is still dense. Sparse methods are a candidate improvement, with derivative and boundary checks required first.

**Context:** Forward Euler plus upwind is a proposed controlled comparison, not an implemented replacement. No matched BDF/Radau/explicit accuracy-cost study or validated newer-code speedup factor is claimed. The matrix picture shows expected local coupling structure schematically; it is not a measured sparsity plot of the current dense matrix.

**Proposed visual:** Space / time / coupling panels, plus a schematic block-neighbor coupling pattern.

**Connection to the next part:** Make accuracy tangible by considering a pulse whose correct transport response is known.

**Sources:** [G — numerical methods and analytic advection example](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md) · [Legacy executed audit and defects](../3_Model/state.md) · [Reacting simulator, pinned Hermes snapshot a842535](https://github.com/AsapLoso/project-management-agents/blob/a84253576a82c33f894b594f0a5b58d6aac3b943/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) · [Open F/G scientific questions for Zoë](DECK_OPEN_QUESTIONS.md)

**Claim IDs:** G01, G02 · **Time:** 65 s

## 8. The grid can change the pulse

**Key message:** A distorted waveform must be checked for numerical contributions before being interpreted as reactor physics.

- For ideal constant-velocity advection without reaction or dispersion, the outlet is the inlet delayed by the residence time, with unchanged amplitude.
- For N uniform upwind cells with exact integration of the semidiscrete equations, the steady harmonic amplitude ratio is [1 + (ωΔz/u)²]^(−N/2) and phase lag is N atan(ωΔz/u). With N = 60 and a period equal to one residence time, amplitude retention is 0.720942; lag is 358.6926° versus the ideal 360°. The 1.3074° phase lead error is also a timing error.
- This is a defined linear transport calculation, not a reacting-simulator output. Forward Euler at CFL = 1 shifts pure advection exactly; that special cancellation need not survive reactions, diffusion or smaller stability-limited steps. Grid and time errors therefore need controlled comparison.

**Context:** The plotted curves are generated directly from the analytic delay and the discrete harmonic transfer function, including its phase. They are normalized mathematical signals over two cycles. The 60-cell illustration is not a measured error estimate for the composite Hermes reactor, nor an executed model benchmark. The arithmetic was independently checked during deck generation. The zero-crossing inset magnifies the normalized interval around one period: the upwind crossing occurs at t/T=0.99636846 instead of 1.00000000. Both responses retain the forcing frequency. A different frequency or accumulated time-integrator phase drift is not established by this exact-time steady harmonic example.

**Proposed visual:** Analytic ideal-advection and semidiscrete upwind harmonic curves, an explicit zero-crossing phase zoom, and amplitude/phase labels. Conditions and the Euler CFL=1 exception remain visible.

**Connection to the next part:** State what the existing evidence establishes and what checks remain before chemical inference.

**Sources:** [G — numerical methods and analytic advection example](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md) · [Open F/G scientific questions for Zoë](DECK_OPEN_QUESTIONS.md)

**Claim IDs:** G03 · **Time:** 65 s

## 9. Know what each result establishes

**Key message:** Current progress supports the model architecture and selected source/mathematical checks; reactor performance conclusions remain open.

- Implemented: a distributed legacy scaffold, nonzero source-backed PSSA reacting code, and a controllable periodic inlet. Saved preliminary calculations exist.
- Checked or derived: selected kinetic-source transcription, documented legacy defects, physical inventory reasoning and the analytic pure-advection example. None is experimental validation of the composite reactor.
- Still needed for quantitative physical conclusions: consistent source/catalyst/geometry assumptions, conservative exchange for resolved paths, derivative checks, spatial/time convergence, and a properly evaluated periodic comparison.

**Context:** K explicitly concludes that no specific conversion/selectivity number is currently sufficiently validated for a presentation result. Diagnostic synthetic-case numbers are therefore excluded. The 24/24 transcription receipt and 10/12 coverage-range count remain traceable in the checklist rather than becoming performance headlines. Zoë's F/G questions remain open and unsent.

**Proposed visual:** Three status lanes: implemented, checked/derived, and open for physical inference.

**Connection to the next part:** Return to the original question through the smallest defensible next comparisons.

**Sources:** [K — preliminary outputs and current result boundaries](deep-dives/K_results_validation_status_2026-10-14.md) · [F — inventories, state space and conservation questions](deep-dives/F_conservation_state_space_2026-10-14.md) · [G — numerical methods and analytic advection example](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md) · [E — source conditions and reactor assumptions (background)](deep-dives/E_operating_regime_transport_2026-10-14.md) · [Selected Urmès 2019 source-transcription receipt](../3_Model/probes/urmes2019_source_receipt.json) · [PSSA coverage-range receipt](../3_Model/probes/pbr_implementation_receipt.json) · [Legacy executed audit and defects](../3_Model/state.md) · [Open F/G scientific questions for Zoë](DECK_OPEN_QUESTIONS.md)

**Claim IDs:** K01, CONS01, SRC01, NUM01, CONFLICT01 · **Time:** 60 s

## 10. Use the predictor to test and learn

**Key message:** A verified and appropriately calibrated predictor would let us test periodic performance and investigate parameter information.

- Performance: compare settled steady and periodic behavior under matched feed budgets and operating constraints. Define a cycle-integrated net ethylene metric that accounts for inlet ethylene. A same-mean steady reference answers one comparison; claiming superiority over the best admissible steady operation requires that stronger benchmark too.
- Parameter information: first generate noiseless cyclic responses with known parameters and test distinguishability for the chosen model, input and observable. Identical responses under that experiment cannot be separated by repeating it unchanged; failure of a parameter-recovery optimizer alone does not demonstrate non-identifiability.
- Noise and repeated cycles follow an informative idealized test. The current milestone is a transient response we can trust; improved periodic yield remains a research question.

**Context:** The identification argument is a small, conditional outlook, not a completed test or a new main objective. Urmès 2022 is a relevant flow-oscillation identification precedent at abstract level here, not an implemented method or evidence for this concentration-forcing yield hypothesis. Pellet-size distributions, reduction and feedback control remain optional later extensions. L proposes candidate net-production/yield definitions and distinguishes the same-mean reference from the best admissible steady competitor. The objective and physical constraints remain open scientific choices, not an implemented or supervisor-approved optimization.

**Proposed visual:** One predictor branching to a matched performance comparison and a small noiseless-first parameter-information test; return to the opening reactor icon.

**Connection to the next part:** End on the research question and the concrete requirements for answering it.

**Sources:** [Project proposal, central question and methodology](../0_Project_Management/main.tex) · [K — preliminary outputs and current result boundaries](deep-dives/K_results_validation_status_2026-10-14.md) · [02 — proposal to predictive optimization](sub-stories/02_proposal_to_predictive_optimization.md) · [04 — noiseless-first identification hypothesis](sub-stories/04_model_fidelity_and_identifiability.md) · [D — effective parameters and identifiability](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md) · [Urmès et al. 2022, transient flow-oscillation identification (abstract-level here)](https://doi.org/10.1002/cctc.202101826) · [L — fair periodic metrics, benchmarks and research outlook](deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md)

**Claim IDs:** Q01, FUT01, REF01, K01, FUT02 · **Time:** 60 s

## Editorial boundaries and later integration

- Both code approaches receive equal spotlight time and explicit scope. No experimental draft PR is merged, calibrated or treated as validation.
- Literature supports choices: Urmès 2019 supplies implemented effective kinetics; Berger provides a retrospective comparison framework; Urmès 2022 is an abstract-level transient-identification comparator. No invented paper-to-code development chronology.
- E remains background. The conditional external-film estimate, full balance derivations, exact old defect timings, optional radial details and pellet distributions are backup material.
- Narrative 05 remains an optional transition integrated within slide 5; no separate I technical section is added. Sub-story 04 remains a small future hypothesis in slide 10.
- Forward Euler, alternative integrators, sparse methods, conservative resolved exchange and parameter recovery are proposed comparisons, not new executed results. F/G questions for Zoë remain open and unsent.
- K excludes synthetic conversion/selectivity numbers and positive periodic-yield claims from the deck. Its preliminary-output status is preserved.
- Later research should update the relevant claim, slide, context and cue together. Contradictions must be recorded in [the integration log](INTEGRATION_LOG.md) and [claim ledger](CLAIM_SOURCE_CHECKLIST.md).

## Files to use

- [Editable Word outline](BEP_Presentation_Outline.docx)
- [Standalone slide deck](BEP_Dynamic_Acetylene_Progress.html) · [slide PDF](BEP_Dynamic_Acetylene_Progress.pdf)
- [Printable outline](BEP_Presentation_Outline.html) · [outline PDF](BEP_Presentation_Outline.pdf)
- [Concise speaker cues](SPEAKER_NOTES.md) · [claim/source checklist](CLAIM_SOURCE_CHECKLIST.md)
- Editable content: [presentation_content.json](presentation_content.json); layout/generation: [build_presentation.cjs](scripts/build_presentation.cjs).
