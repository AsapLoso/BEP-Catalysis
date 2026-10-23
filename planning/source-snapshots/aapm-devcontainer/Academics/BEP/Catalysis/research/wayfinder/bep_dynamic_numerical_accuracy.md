# Wayfinder: Dynamic Numerical Accuracy / Attenuation — BEP Catalysis

**Status:** Focused follow-up map, recorded 16 October 2026. All tickets below are **parked**: this records open scientific decisions without execution, scheduling, owner assignment, or automatic priority increase.
**Parent:** [BEP Catalysis master Wayfinder](bep_catalysis_master.md) · [BEP state](../../state.md)
**Evidence starting points:** [E — transport regime](../../presentation/deep-dives/E_operating_regime_transport_2026-10-14.md), [F — conservation and state space](../../presentation/deep-dives/F_conservation_state_space_2026-10-14.md), [G — numerical methods](../../presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md), [framework audit](../../3_Model/transient_model_framework_audit.md), [reconsolidation capture](../notes/reconsolidation_capture_2026-10-16.md).

## 1. Destination

Decide what numerical and physical evidence is sufficient to trust transient reactor observables for the BEP's experimental question, and what fair experiment/model comparison should follow. Completion means the accuracy measures, conservation ledger, source-matched benchmark and relationship between the 2019 PSSA and 2022 non-PSSA models are explicit and supported by evidence. This map plans decisions; it does not run simulations or edit reactor code.

## 2. Decision log

- [ ] **No model-selection or implementation decision is made by this map.** The recommendation in the linked capture is AI inference only.
- [ ] **No automatic priority change.** Existing project priorities and open tasks remain as they were.
- [ ] **The approximate 116.6 s pellet timescale is withdrawn.** The user-specified replacement (~0.001166 s) remains to be checked against its source inputs before use as a scientific fact.

## 3. Parked decision tickets

### Island: Dynamic numerical accuracy / attenuation

- [ ] **Choose transient accuracy observables** (`wayfinder:grilling`) — Which outlet quantities and tolerances matter for the scientific claim (amplitude, phase/delay, cycle-averaged conversion/selectivity/ethylene yield), and what numerical error is acceptable for each?
  - Status: Parked; question recorded, no experiment run.
  - Dependencies: owner selects the observable(s); then formulate the numerical comparison.
- [ ] **Separate physical attenuation from numerical attenuation** (`wayfinder:research`) — For the selected forcing and outlet observable, what part of amplitude/phase loss comes from physical transport/reaction and what part from axial/radial discretization, timestep/tolerances and solver error?
  - Status: Parked; requires a matched limiting case and refinement plan.
  - Dependencies: accuracy observable; explicit transport/kinetics assumptions.
- [ ] **Set convergence evidence** (`wayfinder:grilling`) — What mesh, timestep/tolerance and solver comparisons are sufficient before a transient result is reported?
  - Status: Parked; no threshold is set here.
  - Dependencies: selected observables and baseline model.
- [ ] **Close the mass/atom conservation ledger** (`wayfinder:research`) — Which gas, pore, catalyst and surface inventories and boundary fluxes must be combined, and what residual criterion demonstrates C/H conservation in the coupled implementation?
  - Status: Parked; F documents a possible source double-booking, not an executed conservation failure proof.
  - Dependencies: selected model state vector and rate basis.

### Island: Pellet transport and particle population

- [ ] **Choose the explicit pellet-radius/diffusion comparison** (`wayfinder:grilling`) — Which radius range, diffusivity basis, pellet geometry and catalyst/operating condition define a meaningful radius sweep?
  - Status: Parked; the user asked to consider enabling pellet-radius resolution. The previously stated ~116.6 s timescale is withdrawn; the ~0.001166 s replacement is not independently verified here.
  - Dependencies: resolve diffusivity and geometry conventions; source-matched operating point.
- [ ] **Choose a particle-size distribution basis** (`wayfinder:grilling`) — Should a later population model use measured sieve data or a stated positive distribution (including whether a truncated Gaussian is appropriate), and how should total catalyst mass be conserved?
  - Status: Parked; Gaussian sizes were user-proposed, not implemented or selected.
  - Dependencies: particle-size evidence and model response to radius.
- [ ] **Map transport/kinetics regimes** (`wayfinder:research`) — Which dimensionless groups and source-matched conditions distinguish reaction, film, pore-diffusion and axial-transport limitation, and which can be omitted for the selected observable?
  - Status: Parked; literature thresholds must remain paper-specific.
  - Dependencies: verify geometry, pressure, diffusivity, particle basis and kinetic source.

### Island: Experimental benchmark and surface memory

- [ ] **Define the Urmès 2019 experimental benchmark** (`wayfinder:research`) — Which source operating points and measured outputs can the reacting PSSA vertical slice reproduce under matched catalyst, feed, pressure, temperature, bed and particle assumptions?
  - Status: Parked; source-to-code transcription checks do not answer this.
  - Dependencies: retrieve/identify the measurement table/figure and compare the exact code path and units.
- [ ] **Select the 2019/2022 validation sequence** (`wayfinder:grilling`) — Should the 2019 source-matched PSSA reproduction be the first benchmark before a dynamic-surface model, or is there a user-selected reason to proceed directly to a 2022 transient non-PSSA benchmark?
  - Status: Parked; the linked preference is an AI recommendation, not a user decision.
  - Dependencies: experimental benchmark scope; full 2022 source/parameter audit.
- [ ] **Establish what the 2022 memory mechanism predicts** (`wayfinder:research`) — What exact elementary network, parameter values, initial/periodic coverage state and measured transient observables are supported by the full 2022 paper and SI?
  - Status: Parked; the opt-in implementation is not treated as source-verified or calibrated.
  - Dependencies: access and full-text audit of the primary paper and supporting information.

## 4. Fog of war

- Whether later model integration is required to answer the thesis question, after model-specific benchmarks expose which physical states are necessary.
- Whether the measured particle-size population materially changes the selected cyclic outlet observables after radius sensitivity is established.
- Whether experimental noise and parameter identifiability limit discrimination between transport memory and surface memory.
- Whether any observed periodic benefit persists against both a matched same-mean steady benchmark and the best admissible steady operating point.

## 5. Out of scope

- Executing a radius sweep, adding a size distribution, implementing the 2022 kinetics, fixing the legacy framework, changing the deck, or running simulations.
- Treating source transcription, isolated unit tests, or internal code agreement as experimental validation.
- Automatically promoting a parked item to the active project frontier or changing its priority.

## 6. Reading order

1. [Reconsolidation capture and evidence-bound comparison](../notes/reconsolidation_capture_2026-10-16.md).
2. [E — operating regime and transport](../../presentation/deep-dives/E_operating_regime_transport_2026-10-14.md).
3. [F — conservation and state space](../../presentation/deep-dives/F_conservation_state_space_2026-10-14.md).
4. [G — numerical methods and feasibility](../../presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md).
5. [Model state and audits](../../3_Model/state.md) and [2022 non-PSSA bridge](../notes/NON_PSSA_SURFACE_BRIDGE_2026-10-14.md).
