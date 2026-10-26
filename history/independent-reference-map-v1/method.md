# Method — independent BEP scientific reference map (v1)

## Scope and evidence boundary

This dataset reconstructs the scientific territory of the BEP on dynamic feed-composition forcing for selective acetylene semi-hydrogenation in a packed-bed reactor. It is a reusable AI reference graph. It is not a fitted reactor model, a literature systematic review, a validated catalyst mechanism, or an experimental result. Node maturity is limited to `idea` and `ai_worked_out`; no human understanding or verification is asserted.

The scientific question is framed as: under what catalyst-specific kinetic, transport, instrumentation and safety conditions can periodic inlet composition change the cycle-integrated net ethylene production relative to an optimized steady baseline? The proposal's improvement claim remains a hypothesis. No numerical kinetic parameters, measured yield gain, or optimal forcing period were invented.

## Proposal revision selected

`Academics/BEP/Catalysis/0_Project_Management/main.tex` is the scope anchor because the source guide identifies it as the primary project framing and it contains the proposal's integrated introduction, literature review and methodology. It proposes a one-dimensional gas-phase advection–dispersion model coupled to non-pseudo-steady surface coverages; an isothermal, open-loop baseline; candidate method-of-lines/upwind or OCFE discretization; BDF/Radau integration; B-spline forcing; and a planned steady calibration, in-silico optimization, then physical test.

The standalone `section1_intro.tex`, `section2_lit.tex`, and `section3_method.tex` were read as alternate drafts, not silently merged into that baseline. The standalone literature draft makes a categorical no-framework claim and discusses observers; the 2022 direct acetylene periodic-operation paper narrows that claim. The standalone method describes a grey-box Latin-hypercube sampling approach, whereas main.tex specifies two-tier calibration (spectroscopically bounded adsorption terms followed by macroscopic GC fitting). These are alternative calibration proposals, not one implemented method. Main.tex is used as the v1 baseline and the unresolved choice is recorded below.

The roadmap is planning context only. Its particle-scale diffusion model, broader controller/estimator ideas, and other extensions are not treated as evidence or inserted into the core PDE. The main proposal itself has no explicit intraparticle concentration field.

## Independently derived hierarchy

Exactly three first-level disciplines follow the task contract:

- **Physics** contains the chemical network, catalyst surface inventory and mechanism alternatives, bed/pellet transport, thermal/catalyst evolution, and experimental observables.
- **Mathematics** contains conservative balance construction, rate/stoichiometric bases, initial-boundary-value problems, dimensionless groups, discretization and solver verification, inverse problems, and periodic-orbit/stability analysis.
- **Systems & Control** contains the plant input/state/output boundary, actuator and analyzer constraints, excitation design, waveform optimization and matched baselines, then a clearly future state-estimation branch.

This split is based on the question each concept answers: what physical process occurs; how it is represented and analyzed; or how inputs, observations and decisions are designed. Topics that genuinely span disciplines use `related_ids`; they are not duplicated as competing tree definitions. The hierarchy has 63 nodes including the root and intentionally varies in depth.

## Governing conventions used in this map

### Gas-phase balance

For the primary conservative form, Cᵢ is gas concentration in mol m⁻³ of void gas, uₛ is superficial velocity in m s⁻¹ based on total bed cross-section, ε_b is bed void fraction, D_ax,ᵢ is axial dispersion in m² s⁻¹ under the flux convention below, ρ_p is catalyst mass per pellet volume in kg_cat m⁻³_pellet, and rⱼ is mol reaction kg_cat⁻¹ s⁻¹. With product-positive stoichiometry νᵢⱼ,

```text
ε_b ∂ₜ Cᵢ + ∂z(uₛ Cᵢ)
= ∂z(ε_b D_ax,ᵢ ∂z Cᵢ) + (1−ε_b) ρ_p Σⱼ νᵢⱼ rⱼ
```

The product (1−ε_b)ρ_p is catalyst mass per bed volume. If the properties are constant, dividing by ε_b gives interstitial velocity uᵢ=uₛ/ε_b. Other concentration, dispersion or catalyst-density conventions are possible, but the porosity factors must change consistently. This is a dimensionally clarified derivation of the proposal's intended balance, not a verbatim transcription of its compact rate term.

With total axial flux Jᵢ=uₛCᵢ−ε_bD_ax,ᵢ∂zCᵢ, the chosen dispersed-bed boundary closure is uₛCᵢ,in=Jᵢ(0) at the inlet and ∂zCᵢ(L)=0 at the outlet. The actual upstream mixer, downstream analyzer volume and apparatus geometry may require a different domain.

### Surface states

For a mechanism with signed surface stoichiometry νˢ, a per-site-normalized rate rˢ gives dθ/dt=νˢrˢ(p,θ,T). A single monodentate lattice obeys θ_*+Σₗθₗ=1; a species occupying sₗ sites gives θ_*+Σₗsₗθₗ=1. Rates stated per catalyst mass or area require an active-site-density conversion before they can update fractional coverage. Site families and adsorption states are mechanism choices, not universal facts.

### Performance and scaling

Use explicit molar-flow definitions and subtract inlet ethylene. One candidate periodic yield is
Y_E=∫₀ᵀ(F_E,out−F_E,in)dt / ∫₀ᵀF_A,in dt.
A selectivity objective has a different denominator and can reward low throughput; consider a productivity objective or a conversion floor. For the declared convention, Pe=uᵢL/D_ax, Da_ref=(S_ref/C_ref)L/uᵢ, and period-based St=(L/uᵢ)/T_pulse. If angular frequency is used, ωL/uᵢ=2πSt. These groups are descriptive and require measured or justified inputs.

## Literature and provenance method

The proposal and repository bibliography establish what the project planned and cited. External scientific statements are limited to source locators actually inspected. Full-text access is explicitly marked; most kinetic papers were available only as publisher abstracts or indexed metadata, so the map does not invent their detailed rate laws. The Urakawa MES paper was read in full and is used only for its demonstrated method, periodic excitation and square-wave practicality in its own catalytic example. Primary-source applicability is indexed by catalyst, support, reaction, forcing mode and access level.

A crucial scope audit found Urmès et al. (2022), *Microkinetic Modeling of Acetylene Hydrogenation Under Periodic Reactor Operation*, which reports small-amplitude flow oscillations, dynamic kinetic estimation and reproduction of fixed-bed outlet composition for Pd/α-Al₂O₃. The accessible abstract and first-page preview do not establish whether the full model contains a spatially resolved axial PDE. Thus the broad novelty claim in the proposal is not safe; the narrower PdAg-specific, spatial-model/optimization gap remains an open question pending the full article and Supporting Information.

## Independence disclosure

The map hierarchy and explanations were derived from the source-guide proposal, original source material accessible in this pass, and explicit balance/units reasoning. The repository's map-review skill required reading the repository governance section on independent reconstructions. In that section, I saw two names for prior C1 topics. I did not open the legacy map YAML, generated nodes, prior A–M dossiers, or old map conclusions. This creates possible lexical contamination; the present hierarchy was rebuilt from the proposal and scientific sources and is not claimed to be information-theoretically blind. This disclosure is preserved so a later review can assess independence honestly.

## Boundaries and unresolved decisions

- The 2012 Pd–Ag/Al₂O₃ abstract reports a two-site steady kinetic model; 2019 and 2022 Pd/α-Al₂O₃ papers describe single-site models under their respective regimes. These are catalyst-specific alternatives, not a contradiction to resolve by selecting one universally.
- The 2022 article is directly relevant to periodic acetylene hydrogenation but is not yet fully inspected. Exact spatial scope, boundary conditions, data and optimization claims remain unverified.
- Thermal pulsing on Pt for CO oxidation (Zhu et al., 2021) is not evidence for microsecond acetylene kinetics, feed-composition modulation, PdAg, or dynamic yield.
- MES supports dynamic species detection in instrumented laboratory systems. It does not imply coverage profiles across a full industrial bed are directly observable.
- The proposal's τ_des≈T_pulse<τ_residence, PSSA failure under all rapid forcing, inherent square-wave numerical instability, zero-redesign claim, and guaranteed local-minimum claim are audited as hypotheses or overstatements in `claim_audit.md`.
- The cited Larsen thesis and Froment textbook were not independently accessed. Their status and limits are explicit in `sources.yaml`.

## Schema extension

`nodes.yaml` follows the task's suggested root and per-node fields. Node `equations` use objects with `name`, `expression`, `variables`, and `conditions`; `claim_refs` use `source_id`, exact `locator`, `evidence_type`, and `supports`. `sources.yaml` extends the source minimum with claim-level support/limits and cross-citation IDs. Both are standalone YAML 1.2 documents.
