# Method — independent BEP scientific reference map (v2 enrichment)

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

This split is based on the question each concept answers: what physical process occurs; how it is represented and analyzed; or how inputs, observations and decisions are designed. Topics that genuinely span disciplines use `related_ids`; they are not duplicated as competing tree definitions. The frozen v1 hierarchy had 63 nodes including the root. The v2 enrichment contains 79 nodes, keeps the same three direct disciplines, and intentionally varies depth.

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

A scope audit found Urmès et al. (2022), *Microkinetic Modeling of Acetylene Hydrogenation Under Periodic Reactor Operation*: its publisher abstract reports small-amplitude flow oscillations, dynamic kinetic estimation, and outlet-composition reproduction in a periodically modulated fixed bed for Pd/α-Al₂O₃. The available publisher “full text” route returned abstract-level content, and the listed Supporting Information could not be retrieved in this access session. The abstract does not establish a spatially resolved axial PDE or a cycle-performance optimization. The broad novelty claim is therefore unsafe; exact model scope and any narrower PdAg gap remain open.

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


## Second-pass synthesis — v2 enrichment (2026-10-21)

This pass starts from the frozen v1 graph and critically revises it; it is not an independent blind reconstruction. The v1 branch and files remain the baseline. The graph now contains 79 nodes and 28 source records, remains rooted at exactly three disciplines, and retains the `idea` / `ai_worked_out` ceiling. No personal map, simulation, fitted parameter set, optimum, or experimentally verified BEP gain is asserted.

### Taxonomy and linked scientific layers

Physics now distinguishes reaction chemistry from catalyst chemistry. Within catalyst chemistry, site ensembles, working PdAg surface structure, catalyst memory, reversible coverage, deposits and time-on-stream aging are related but non-interchangeable. Physical extensions separately represent pellet diffusion/film transfer, bed residence-time response, thermal balance and measurement dynamics. Mathematics links bed/pellet scales to periodic orbits and mean response. Systems & Control separates the commanded input, realized bed-plane waveform, identification experiments, performance testing and fair steady benchmark. Cross-links encode the common interfaces rather than duplicating the concepts.

### When a mean-performance gain is possible—or excluded

The statement “periodic operation can improve” is conditional. Three distinct no-gain limits are represented: (i) a stable LTI model at settled periodic response and fixed mean input preserves its DC output; (ii) for a memoryless concave scalar map on a convex admissible interval, Jensen’s inequality bounds average output by the constant input at the same mean; (iii) if every steady control embeds as a feasible constant periodic control under identical constraints and objective, the periodic optimum is weakly no worse by set inclusion. None establishes a strict gain for a nonlinear, dynamic, constrained catalytic bed or a ratio objective.

For a smooth weakly nonlinear system, zero-mean modulation can create a second-order DC response. Its sign and size depend on the model’s nonlinear cross-frequency response; a matched time constant is not a sufficient condition. Literature contrasts are kept distinct: Feimer et al. (1982) report no rate gain for the adsorption/desorption models they examined; Horn and Bailey (1971) provide sufficient, model-specific improvement conditions; Ziegelhoeffer et al. (1972) give a pellet example where a frequency window improves selectivity; Espinoza et al. (2022) report a tested ethane-oxidative-dehydrogenation case with no predicted mean-performance change over their simulated sweep and stable averaged conversion/selectivity in their experiment; Kaps et al. (2026) report an experimental methanol-synthesis FPO comparison with improved performance under their selected paired-input conditions, complicated by catalyst deactivation. These are competing model-specific findings, not a vote for either universal benefit or universal null response.

### Physical input, transport, catalyst and observation chain

The gas balance is explicitly conservative and basis-checked in `nodes.yaml` and above. The added pellet equation is an optional spherical effective-diffusion template, not part of the proposal baseline or a target-catalyst claim. The energy balance is likewise a screening extension; the isothermal assumption requires a bounded kinetic impact of measured temperature excursions. Bed dispersion, pellet penetration, gas residence, surface relaxation, catalyst drift, actuator/mixer response and analyzer response are distinct filters or memory states. A command is not a bed inlet; component molar flow, total flow, mole fraction and superficial velocity can change together. A measured outlet phase lag cannot be assigned to surface kinetics until line/analyzer dynamics are characterized.

The full-text Espinoza profile-reactor study is useful for the *method* of empty-tube control checks, inert compensation of total-flow variation, spatiotemporal gas/temperature profiling and operando characterization; its MoO₃/γ-Al₂O₃ ethane oxidation chemistry is not transferable to acetylene/PdAg. The Kaps full text is also cross-system. The Urmès et al. (2022) publisher page and abstract are directly relevant to acetylene dynamics and confirm a fixed-bed outlet-modeling study, but the available full-text link returned abstract-level content and its listed Supporting Information could not be retrieved. Exact spatial PDE scope, model equations and any performance comparison therefore remain open.

### Objective, evidence classes and access

Cycle conversion, cycle selectivity and net ethylene yield are defined as ratios of integrated molar amounts with inlet ethylene subtracted. Their algebraic relation holds only on the declared basis; the time-average of instantaneous selectivity is not generally the integrated ratio. Productivity needs a separate space/mass/time denominator. The fair benchmark uses an optimized steady point over the same feasible conditions and the same objective. Set nesting guarantees only a weak mathematical optimum ordering when its assumptions hold.

Provenance distinguishes source observation, proposal hypothesis, derivation under assumptions, interpretation and unverified claims. Full text read in this pass: Urmès et al. (2019), Berger et al. (2008), Espinoza et al. (2022) via the TU Hamburg repository PDF, and Kaps et al. (2026) publisher HTML. Urmès et al. (2022) is publisher abstract/preview-level; Mei (2009), Li (2021), Pachulski (2012), Feimer (1982), Horn/Bailey (1971) and Ziegelhoeffer (1972) are limited to abstract or indexed metadata as recorded in `sources.yaml`. This is a targeted second-pass research map, not a systematic review: access and selection limits prohibit claims of literature completeness.
