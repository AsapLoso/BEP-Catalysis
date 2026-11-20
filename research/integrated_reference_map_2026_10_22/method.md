# Integration and evidence method

## Source snapshots and preservation

The integration uses three immutable inputs, identified in `nodes.yaml` and `source_provenance.yaml`:

- The original canonical map and 69-node draft overlay from the exact `devcontainer` snapshot used by PR #177: commit `f18682d97153251f23396ca7b82fd9dd38f0edf0`; the two source blob IDs are recorded alongside it.
- The independent v2 reference map (79 nodes and 28 source/context records): commit `ea391357ad8e4e03cfd27324d4b274513826b254`.
- The comparison/reconciliation proposal (19 taxonomy records, 144 old-to-theme crosswalk rows and claim audits): commit `4afef28be1596f8e9a0f27a9d447b6e7a44f6e31`.

The source files and their histories were not edited. The integrated folder records a new view of those snapshots. Every prior concept has an individual row in `concept_mapping.yaml`; the prior crosswalk is retained verbatim in substance and extended with integrated target IDs. Merges preserve the source ID/title, explanation or notes, open questions and historical attachment relationships. Refinements and corrections say what changed and why. Multiple target IDs are used where a concept was split across physical measurement and systems observability.

## Graph and record structure

`nodes.yaml` is a rooted parent hierarchy with `bep` at the root and three canonical children: Physics, Mathematics, and Systems & Control. Theme nodes provide scientific branches; detailed concepts remain below their appropriate theme. `related_ids` complements the hierarchy. The separate edge file represents mechanistic, mathematical, numerical and plant/input/output relations that cannot be conveyed by parent-child placement alone.

Each scientific node may contain:

- A concise summary and longer explanatory text.
- Equations as expressions plus variable bases, units and conditions. Equations are not promoted from notation into target parameter claims.
- Assumptions, applicability limits, open questions and one or more evidence references.
- `source_map_refs` that preserve the previous map IDs from which content was retained or merged.

The node graph deliberately distinguishes an observed or source-fitted result from an interpretation, proposal hypothesis, or derivation. `claim_refs` carry a source ID, source locator, evidence class and the bounded statement supported. `prior_map_attachment_unverified` records the old attachment without claiming the cited span was checked. Internal project notes and AI research artifacts are retained only as lineage, not primary scientific evidence.

## Scientific synthesis

### Chemistry, surface state and reactor transport

The overall product-accounting backbone is C₂H₂ + H₂ → C₂H₄ followed by C₂H₄ + H₂ → C₂H₆. It is separate from elementary surface chemistry. Horiuti–Polanyi steps, adsorbed vinyl/ethyl intermediates, ethylene desorption/readsorption, alternate bypasses, multiple site families and carbonaceous deposits are represented as catalyst-conditioned alternatives. Site balances include vacancy occupancy and occupancy numbers; dissociative H₂ adsorption consumes two adjacent vacancies in the corresponding lattice model. No one route is declared universal for supported Pd, PdAg, ideal alloy surfaces, or an unknown target batch.

Two rate closures are kept distinct. Urmès et al. (2019) supplies an effective single-site pseudo-steady-state (PSSA) model for its 0.05 wt% Pd/α-Al₂O₃ tail-end dataset. A PSSA rate law can feed a transient gas-phase bed without adding dynamic surface states. An explicit coverage model instead adds equations such as `dθ/dt = ν_s r_s(p,θ,T)` and must define site inventories, kinetic coefficients and gas/surface elemental accounting. A dynamic outlet trace by itself does not identify which internal state caused the lag.

For the proposal baseline the gas balance is recorded as

`ε_b ∂_t C_i + ∂_z(u_s C_i) = ∂_z(ε_b D_ax,i ∂_z C_i) + (1−ε_b) ρ_p Σ_j ν_ij r_j`.

Here `C_i` is mol per gas-void volume, `u_s` is superficial velocity, `D_ax` is the axial-dispersion coefficient under the stated flux convention, `ε_b` is bed void fraction, `ρ_p` is catalyst mass per pellet-envelope volume, and `r_j` is mol per catalyst mass per second. If the catalyst density is already expressed per bed volume, the solid fraction must not be applied a second time. A constant-property conversion gives the interstitial velocity `u_i=u_s/ε_b`; variable coefficients remain inside flux derivatives. Danckwerts flux conditions, pressure/flow closure, and the chosen gas concentration basis must agree. If superficial velocity varies, it remains inside the advective flux divergence; a constant-u_s reduction drops C_i∂_z u_s. Under ideal-gas, fixed-P/T, fixed-area conditions u_s=F_tot RT/(P A_c), so a fixed inlet setpoint does not itself prove constant in-bed flow. A fully coupled dispersed-flow closure still needs total continuity, surface inventory, pressure and thermal conventions. Pellet radial diffusion, external film transfer, nonisothermal energy balances and aging are represented as extensions; none is silently inserted into the proposal's isothermal 1-D baseline.

### Conservation, discretization and numerical analysis

The matrix `ν_ij` maps reaction extent rates to gas species sources, while `ν_s` governs surface inventory change. A surface site constraint is algebraic; combining it with explicit coverage states can create a differential-algebraic system. Method of lines creates a finite ODE/DAE system from the axial discretization. High-Péclet central differencing may oscillate; upwind fluxes add numerical diffusion. BDF/Radau are candidates for stiff integration, not evidence that this model is stiff or that one solver has been verified. Input discontinuities should align with integration events or use a justified smooth approximation.

Integrating the bed balance over a finite cell yields ε_bΔz dC_i,k/dt = J_i,k−1/2 − J_i,k+1/2 + ΔzS_i,k. Shared face fluxes telescope in the global balance; the inventory, flux and source terms all have units mol m⁻² s⁻¹ after time differentiation. A scalar upwind-advection/centered-diffusion/forward-Euler stencil has nonnegative transport weights when Co+2Fo≤1 under uniform-grid, constant-coefficient assumptions; this is not a full reaction-network stability bound. A source-specific CO2-capture paper reports explicit-step restrictions and a method-of-lines implementation, but it does not validate the BEP solver. The map lists independent checks: species/element balance, site closure, nonnegative concentrations/coverages, initial and boundary consistency, periodic closure, mesh and tolerance refinement, and limiting-case comparisons. Solver stability is not the same as physical validity, positivity, conservation or accuracy. No target code, Jacobian, stiffness spectrum, mesh, runtime or convergence result is asserted.

### Inputs, measurements, identification and optimal comparison

The plant map separates the commanded feed from the realized component flow at the bed plane. MFC/valve response, mixer and transfer lines, reactor residence-time distribution and outlet analyzer dynamics all filter phase and amplitude. A tracer or inert-response test helps distinguish these delays from kinetic relaxation. Operando modulation-excitation spectroscopy is included as a laboratory measurement precedent; it does not imply full observability of every state in a distributed bed.

Structural identifiability is uniqueness under ideal observations; practical identifiability is the information available from finite noisy data. Parameter compensation and model alternatives can yield similar outputs. Periodic input can improve sensitivity to some parameter combinations but can also be filtered, confounded or unsafe; identification value is separate from performance gain. A cycle-integrated net ethylene/selectivity/yield metric must account for inlet ethylene and use the same feed/product basis for both modes. The steady comparator must be optimized over the same feasible plant, safety, catalyst-state and resource constraints. If constant steady controls are embedded as admissible periodic inputs and the score is identical, feasible-set inclusion implies weak no-worse ordering only. It does not prove a strict gain.

Stable LTI dynamics at settled periodic response preserve the DC response for a fixed-mean input. Jensen's inequality bounds a static scalar response when it is concave on the relevant input range. These are distinct restricted no-gain limits, not a theorem that nonlinear distributed catalytic reactors cannot benefit. Nonlinear memory, transport, phase and active constraints may give positive, zero or negative changes. No performance sign is asserted for the target BEP.

## Source inspection and correction rules

The local proposal, bibliography, inherited audits and article PDFs were inspected for evidence and lineage. In the catalyst wave, full text was read for Urmès 2019, Borodziński & Cybulski 2000, Dehghani et al. 2019, Stytsenko et al. 2022 and Wang et al. 2023. The one-site Pd/α-Al₂O₃ PSSA, deposit-associated Pd A/E closure, industrial Pd–Ag LHHW plus campaign-time activity decay, Pd–Mn adsorption-substitution model, and PdAg DFT/steady L–H microkinetic screen are represented as distinct source-conditioned alternatives. Wang et al. explicitly impose equilibrated C₂H₂/H₂ adsorption and dθ/dt=0, whereas Stytsenko et al. report strong hydrocarbon retention/displacement under a different promoted catalyst and use piecewise conversion/selectivity closures. Dehghani et al. couple pseudo-steady axial profiles to a slow scalar campaign activity state; that state is distinct from fast within-cycle coverage dynamics. The Dehghani article’s general and fitted activity equations differ in sign and have unresolved units/basis. None of these sources establishes a target transient coverage law. Publisher primary records were consulted for Shi 2024, Danckwerts 1953 and Urmès 2022; the accessible Urmès 2022 content remains abstract/preview and does not establish target PdAg gain or a particular distributed PDE. Crossref metadata was consulted for the Berger DOI correction and Bos & Westerterp (1993). Full text was additionally read for Di Giuliano and Pellegrino (2019), a CO2-capture packed-bed numerical study; the publisher abstract was read for Mott and Green (2015), whose competing boundary proposal remains equation-level unverified.

Correction receipts explicitly record:

- The legacy Berger DOI `10.1016/j.ces.2008.08.012` belongs to a nanofluidization article; the local Berger review `Dynamic methods for catalytic kinetics` is `10.1016/j.apcata.2008.03.020`. Correcting metadata does not validate every equation previously attached to Berger.
- The independent map's Larsen citation asserted 2024 and Delft; the inspected local PDF title page labels a BEP and does not show date or institution. Both the old assertion and local evidence are kept distinct; the date/institution remain open.
- The local Larsen equations (6.9)–(6.11) are an empirical extended LHHW fit with a rate cap and inhibition factor for the thesis data. They are not interpreted as explicit dynamic coverages or target-periodic kinetics.
- The legacy Bos & Westerterp DOI resolves to `Mechanism and kinetics of the selective hydrogenation of ethyne and ethene`; its metadata does not support calling it a review.
- Urmès et al. (2019) printed p. 5 estimates hydrogen adsorption `K₁=611 Pa⁻¹`, whereas Table 5 on printed p. 6 lists fixed `K₁=13 Pa⁻¹`. Both are retained as an unresolved source conflict. The ethylene `0.14 Pa⁻¹` strength and `K₅=7.4 Pa` denominator value use reciprocal conventions and are not labeled a second contradiction.
- The broad novelty claim is narrowed because Urmès et al. (2022) report periodic acetylene operation on Pd/α-Al₂O₃. This does not establish a PdAg target gain or an optimized steady benchmark.
- PSSA is not treated as universal; full-scale coverage observability is not called impossible; square-wave inputs are not called inherently solver-unstable; no local minimum is called inevitable for a maximization problem; and a timescale match alone is not treated as sufficient for gain.

## Known limits

Several older attachments lack exact locators or direct source-text support. They remain visibly labelled as historical and unverified. Some primary records are abstract-only, preview-only or citation-only. The independent source inventory also includes project records and out-of-scope sources; these remain in the source lineage with bounded applicability. Coverage gaps are enumerated in `coverage.yaml` and `uncertainties.yaml`. No target catalyst characterization, kinetic fit, reactor simulation, optimizer run, gain result or physical validation has been created.
