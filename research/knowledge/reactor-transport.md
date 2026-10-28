# Reactor balances, transport, and assumptions

## Model layers discussed

The archived transient framework separates bulk-gas concentration Cᵦ(z,t), pellet-pore concentration cₚ(z,r,t), and surface coverage θ(z,r,t). It also discusses keeping a film-surface concentration Cₛ as a separate quantity. Keeping Cᵦ and Cₛ distinct permits an explicit film balance; setting Cₛ = Cᵦ removes that resistance and recovers a pseudo-homogeneous closure.

A separate pore state is not the same as a separate film resistance. Finite radial diffusion is not the same as an instantaneously uniform pellet. The documents repeatedly warn against collapsing these modeling choices into one decision.

## Alternatives preserved in the record

| Modeling question | Recorded alternatives | What remains unsettled |
|---|---|---|
| Axial transport | Plug-flow or high-Péclet reduction; finite axial dispersion with Danckwerts boundary conditions | Target bed Péclet number and measured residence-time response are not recorded here |
| External transfer | Set Cₛ = Cᵦ; or solve a film/pellet flux relation | Target film coefficient and whether film resistance matters |
| Pellet transport | Uniform or lumped pellet; finite radial diffusion with center symmetry | Target radius, porosity, effective diffusivity, and source-supported geometry |
| Surface chemistry | Algebraic PSSA coverage; or dynamic coverage ODEs | Whether data require surface memory beyond gas/pore transport |
| Thermal model | Fixed-temperature baseline; or energy balance with reaction heat and heat transfer | Measured temperature gradients and the intended project scope |

The older framework audit records a historical choice of separate Cᵦ and Cₛ state structure, then equality to reproduce Berger’s collapsed model, plus explicit intraparticle diffusion as an extension. The same audit says no axial dispersion, no external film, no readsorption closure, and no energy balance remain scope choices or open questions. It also flags a transcription ambiguity in the source void-fraction convention. These are dated statements, not a current model specification.

## Owner-attributed direction

The October 19 notebook handoff records a preference for finite radial pellet diffusion, an instantaneous pellet-shell condition tied to the local bulk concentration, and no external film resistance. It also records a proposed comparison varying Rₚ and D_eff while holding Rₚ²/D_eff fixed. The handoff labels this as the owner’s chosen first investigation at that checkpoint; later work may have changed priorities. It does not establish that the reduction is valid for the final reactor.

The same handoff marks a particle-size distribution as a later hypothesis. A separate October 16 user-thought capture explicitly parks that idea and withdraws a prior 116.6-second diffusion claim; the user-reported replacement 0.001166 seconds remains subject to checking its inputs and units. Another dated handoff gives only a rough 5–30 ms exploration range. These values conflict and none should be used as an accepted physical timescale.

## Evidence and limitations

The AAPM transport reference is a synthesis for orientation. Its dimensionless criteria and equations must be traced to the paper-specific source dossiers before use. The September framework audit compares one proposed model against a Berger dossier and distinguishes source-level equation issues from code-level defects. It does not establish that the target project has chosen the same closure.

## Sources

- [Scientific method-selection map](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/scientific_method_selection.md)
- [Framework audit](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md)
- [Radial notebook handoff](../../planning/source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/notes/session_handoff_radial_notebook_and_parallel_work_2026_10_19.md)
- [Raw-user-thought capture](../../planning/source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/notes/user_thought_dump_2026_10_18_reactor_recovery.md)
- [Reconciliation capture](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/notes/reconsolidation_capture_2026-10-16.md)
