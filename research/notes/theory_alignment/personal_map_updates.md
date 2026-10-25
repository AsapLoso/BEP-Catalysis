# Personal mind-map update proposals

**Status: proposals only.** No owner map, AI map, archive, or master mind-map file was edited.

## Evidence and current placement

This proposal follows the bep-map-edit-review rules. I reviewed the read-only owner map snapshot pinned in research/specs/v3/SOURCE_MANIFEST.md: migration commit 0cd47473a93a71f6200a21e6b66c40d6e3bc7a77, owner-map blob 8a9b7fda318849ad6369cf2e75899a3969290f64. The snapshot contains:

- own_ma_mathematical_modeling, under mathematics, maturity idea, with owner-approved structural placement only.
- own_ma_surface_kinetic_equations, under own_ma_mathematical_modeling, maturity idea, with owner-approved structural placement only.
- A correction record withdrawing the earlier unpreviewed own_ma_reactor_model, assumption, and axial-dispersion scaffold. The map notes that a reactor-model structure remains tentative until the owner approves concepts individually.

The source snapshot is not proof of a newer owner decision. These proposals do not restore the withdrawn IDs, promote maturity, approve a model, or claim human source verification.

## Proposed concepts

The IDs below are proposal labels for review; they do not exist in the owner map and should not be imported without item-by-item owner approval.

| Proposed ID and title | Proposed parent | Proposed stage | Proposed scope | Evidence and unresolved questions |
|---|---|---|---|---|
| proposal_ma_transport_scaling — Transport Scaling and Regime Checks | own_ma_mathematical_modeling | Idea; proposal only | Define mass/thermal Peclet, axial Damköhler, film Damköhler, Biot and Thiele groups with explicit velocity, area, density, and rate bases. Record which values are measured, screened, or unavailable. | Froment, Bischoff & De Wilde, 2011, pp. 157–159, 559–561, 703–708; Schbib et al., 1996, p. 1500, Eq. 14. Target Dax, physical properties, kinetic basis, pellet diffusivity and eggshell depth remain unmeasured or unspecified. |
| proposal_ma_flux_boundary_conditions — Flux-Based Reactor Boundary Conditions | own_ma_mathematical_modeling | Idea; proposal only | Derive the dispersed-bed inlet condition from total-flux continuity and state the assumptions behind a zero-dispersive-flux outlet. Separate the dispersed model from the zero-dispersion hyperbolic limit. | Danckwerts, 1953; Froment et al., 2011, pp. 559–561 and 703–708. Target apparatus domains, valve/line dynamics, and tracer RTD are unknown. |
| proposal_ma_spatial_numerics — Spatial Discretization and Numerical Dispersion | own_ma_mathematical_modeling | Idea; proposal only | Compare centered, upwind, and flux-limited method-of-lines candidates; record order, PeΔz condition, conservation, and grid-sensitivity evidence. The map should record candidates and evidence, not lock a numerical method. | Froment et al., 2011, axial-dispersion formulation, pp. 703–708; Gobbo et al., 2004, p. 550, as one method precedent. No new BEP scheme approval is implied. |
| proposal_ma_periodic_response — Periodic Forcing and Dynamic Response | own_ma_mathematical_modeling | Idea; proposal only | Distinguish gas residence, measured surface relaxation, forcing period, phase lag, and cycle-integrated performance. State that a PSSA closure has no independent surface memory. | The branch V3 blueprint documents an illustrative PSSA gas transient and explicitly lacks fitted dynamic surface times. A periodic optimum or resonance is not established for the BEP catalyst. |

### Alternative hierarchy for owner decision

The table places the four proposed concepts directly under own_ma_mathematical_modeling. This avoids recreating the withdrawn Reactor Model node and gives each claim a clear scope. A single owner-reviewed Reactor Model umbrella with these as children would reduce top-level clutter, but would reintroduce a node family that the snapshot says is tentative. The owner should choose whether to keep the direct children, review a new umbrella separately, or leave these concepts in notes. No option is preselected in the personal map.

## Cross-link proposal for surface kinetics

Consider a proposed cross-link from existing own_ma_surface_kinetic_equations to a future CO-adsorption / competitive-inhibition explanation, subject to owner approval. Do not edit that node's source list or maturity from this dossier.

The scope should preserve the distinction between model and catalyst. Schbib et al. (1996, p. 1502, Eqs. 24–25) and Gobbo et al. (2004, p. 548, Eqs. 3–4) use a shared CO-containing denominator that cancels in their acetylene-to-ethylene rate ratio. Those equations do not establish that CO modulation changes selectivity in the BEP catalyst. A different claim needs a source-specific rate expression or target data.

## Approval and source status

Each proposed concept remains at **Idea / unapproved proposal** until the owner reviews its exact title, parent, summary, scope, and source links. The owner must decide whether to create, revise, defer, or reject each item. This document records no owner response.

The technical citations have only the scope stated above. Froment et al. provide design-level transport equations and criteria; they do not supply BEP parameters. Schbib et al. study a homogeneous Pd/R-Al₂O₃ catalyst, and Gobbo et al. model an industrial front-end system. Neither source validates the BEP PdAg catalyst or its apparatus.
