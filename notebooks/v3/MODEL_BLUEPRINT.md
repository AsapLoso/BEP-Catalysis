# BEP V3 model blueprint

**Status: provisional baseline for implementation; physical assumptions remain subject to owner review.** This blueprint selects a deliberately bounded gas-dynamic reactor model with the Urmès et al. (2019) algebraic PSSA rate law. It is not an owner-approved mechanism for the BEP catalyst and is not an experimentally validated BEP model.

## 1. Scope and model question

Build one reproducible method-of-lines model that answers a narrow question: *given a source-derived Pd/α-Al₂O₃ fitted kinetic closure and a declared plug-flow bed scenario, how does a small periodic change in the inlet reactive-gas composition appear at the outlet when the gas holdup is dynamic but the surface is constrained to the published PSSA closure?*

This preserves the useful V0 bulk-gas reactor architecture and the tested V2 conservative finite-volume advection, stiff integration, rate-law interface, and immutable parameter objects. It does not preserve V0's unparameterized dynamic coverage ODEs. It simplifies V1/V2 by disabling resolved pellet states: Urmès et al. report small internal and external transfer criteria for their own experiment (Table 7), but those criteria do not establish negligible transport in the BEP apparatus. The source's intrinsic-kinetics setup gives a defensible minimal baseline for a source-matched calculation; transferring that simplification to BEP remains a review question.

The dynamic run is an illustrative model scenario, not a reconstruction of a measured transient: Urmès et al. fit steady data and report no sinusoidal forcing experiment. The notebook will not infer surface memory, frequency optima, PdAg kinetics, or experimental response from this run.

## 2. Governing equations and state

The dynamic state is four gas-phase concentrations on an axial finite-volume grid:

`Y = [C_H2(z_k), C_C2H2(z_k), C_C2H4(z_k), C_C2H6(z_k)]`, with `C_i` in mol m⁻³ of bed void gas. Argon is the inert remainder at fixed total pressure; it is not a reactive state. There are no radial-pore or adsorbate states.

For each represented species,

\[
\frac{\partial C_i}{\partial t}
= -\frac{u_s}{\varepsilon_b}\frac{\partial C_i}{\partial z}
+ \frac{W_{cat}}{A L\,\varepsilon_b}\,R_i(p,T),
\qquad p_i=C_i R_g T.
\]

Here `u_s = Q/A` is superficial velocity, `u_i = u_s/ε_b` is interstitial velocity, `A=πD_t²/4`, `L` is bed length, `W_cat/(A L)` is active-catalyst mass per bed volume, and `R_i` is mol kg_cat⁻¹ s⁻¹. This is the `Uniform`-pellet limit of V2's void-volume balance: in its `derive()` convention, `ρ_active,eff(1−ε_b)=W_cat/(A L)`. It keeps the catalyst-mass source basis explicit and avoids introducing an unmeasured pellet diffusivity.

The four-species net source vector is

\[
\mathbf R=(-r_A-r_E,\;-r_A,\;r_A-r_E,\;r_E),
\]

in order H₂, C₂H₂, C₂H₄, C₂H₆. This represents the two overall transformations `C₂H₂ + H₂ → C₂H₄` and `C₂H₄ + H₂ → C₂H₆`. Carbon and hydrogen are conserved by each source vector. The input/output inert balance is implicit; the model holds `T`, `P`, and total volumetric feed fixed and does not solve total-molar-flow contraction. This is a small-conversion approximation that must be reported with the result.

## 3. Provisional kinetic closure

Use the Urmès single-site PSSA expressions from printed p. 4, with parameters from Table 5 on printed p. 6:

\[
D_s=1+\sqrt{K_1p_{H_2}}+K_2p_{C_2H_2}+p_{C_2H_4}/K_5,
\]

\[
r_A=N_S k_{04}e^{-E_4/(R_gT)}
\frac{K_1K_2p_{C_2H_2}p_{H_2}}{D_s^2},
\qquad
r_E=N_S k_{07}e^{-E_7/(R_gT)}
\frac{(K_1/K_5)p_{C_2H_4}p_{H_2}}{D_s^2}.
\]

`r_A,r_E` are mol kg_cat⁻¹ s⁻¹. Pressure is Pa, temperature K, activation energies J mol⁻¹ inside the exponent (the table gives kJ mol⁻¹), adsorption constants retain the printed units, and `N_S` is mol Pd_s kg_cat⁻¹. The Arrhenius prefactors are the paper's uncentered pre-exponentials.

The baseline transcription is `K₁=13 Pa⁻¹`, `K₂=107 Pa⁻¹`, `K₅=7.4 Pa`, `k₀₄=1.4×10⁸ mol (mol Pd_s)⁻¹ s⁻¹`, `k₀₇=3.6×10⁹ mol (mol Pd_s)⁻¹ s⁻¹`, `E₄=48.5 kJ mol⁻¹`, `E₇=54.8 kJ mol⁻¹`, and `N_S=2×10⁻³ mol Pd_s kg_cat⁻¹`. The paper reports confidence intervals for the four fitted quantities `K₂`, `k₀₄`, `k₀₇`, `E₄`, and `E₇`; the baseline uses the tabulated central estimates and does not fit them again.

At any instantaneous gas composition the PSSA coverages are calculated algebraically as

\[
\theta_* = D_s^{-1},\quad
\theta_H = \sqrt{K_1p_{H_2}}/D_s,\quad
\theta_{C_2H_2}=K_2p_{C_2H_2}/D_s,\quad
\theta_{C_2H_4}=(p_{C_2H_4}/K_5)/D_s.
\]

They are diagnostics only, not integrated states. The reduced closure omits vinyl/ethyl coverages from the site balance and treats both rate-determining steps as irreversible under the tested conditions, as described on printed pp. 3–4. V0's elementary dynamic rates cannot be combined with these effective fitted rates without source-supported elementary constants.

### Published `K₁` conflict

The original PDF prints `K₁=611 Pa⁻¹` as an estimate on p. 5 and `K₁=13 Pa⁻¹` as fixed in Table 5 on p. 6. Both are printed with inverse-pressure units; the article does not reconcile them. V3 uses 13 for the Table 5 fitted-model attempt and computes a same-feed `K₁=611` sensitivity for coverages/rates. This sensitivity records the consequence; it does not explain the paper's discrepancy as a unit conversion or claim to resolve it.

## 4. Closures, conditions, and parameters

| Choice | V3 value / rule | Basis and evidence status | Review boundary |
|---|---|---|---|
| Catalyst / kinetic domain | Urmès 0.05 wt% Pd/α-Al₂O₃ fitted law | `urmes2019`, printed pp. 1, 3–6; `c1_urmes_source_catalyst`, `c2_urmes_2019_effective_rates` | Not the BEP PdAg catalyst; transfer is provisional. |
| Temperature cases | 324.15 K (51°C) dynamic run and primary comparison; 335.15 K (62°C) second comparison | Urmès Table 1 and Table 6, printed pp. 4 and 10; Arrhenius parameters Table 5 | Isothermal, no energy balance. `own_ph_isothermal_theory` covers only the elementary fixed-T physical special case, not this model's adequacy. |
| Pressure / feed | 126,000 Pa; condition 1 fractions C₂H₂ .010, H₂ .043, C₂H₄ .70, Ar .247 | Urmès printed p. 4 and Table 6 p. 10 | Ar is implicit/untracked; pressure is fixed. |
| Molar / volumetric flow | `Ftot=149 μmol s⁻¹` from Table 6; `Q=Ftot R_g T/P` at reactor T/P | Urmès Table 6 p. 10; ideal-gas conversion is a declared model calculation | V2's raw `200 mL min⁻¹` is a source-reported flow reference; V3 uses the table's total molar flow to avoid silently treating reference-volume flow as reactor-volume flow. |
| Active catalyst mass | `Wcat=0.1 g` | Urmès Table 6 p. 10 | Source's 0.5 g inert alumina diluent affects packing but not the active catalyst rate basis. |
| Pellet / film | `Uniform` radial closure and `NoExternalResistance`; no `D_e`, tortuosity or pellet states in the RHS | Urmès Table 7 p. 10 reports Weisz–Prater `1.7×10⁻² < 0.33` and Carberry `3.3×10⁻⁴ < 0.05` for its system; V2 `closures.py::Uniform` / `NoExternalResistance` | The source values only apply to that tested catalyst and operating range; no BEP transfer data. The particle-size midpoint (75 μm radius) is descriptive only. |
| Axial closure | No axial dispersion; inlet Dirichlet and convective outflow; V2 conservative TVD2 face flux | V1/V2 cells 0–1 and `pbr/closures.py::NoDispersion`, `discretisation.py::axial_advection`; `ph_axial_dispersion`, `ph_danckwerts`, `ma_conservative_finite_volume` | No BEP tracer/RTD data. Danckwerts conditions belong to the alternative dispersion model and are not silently mixed into the hyperbolic limit. |
| Bed length | `L=(h/d_p) d_p`, `h/d_p=193` from Urmès Table 7, `d_p=150 μm` midpoint of the reported 100–200 μm sieve interval | Urmès printed pp. 9–10 and Table 7 p. 10 | Treat the midpoint conversion and use of the reported ratio as a declared reconstruction. Source dilution and exact packed height are not reported as an independent absolute measurement. |
| Bed void fraction | `ε_b=0.45` for the transient gas-holdup scenario | Borrowed V2 value, not Urmès or BEP measurement | Sets dynamic residence time. It cancels from the ideal steady catalyst-mass-coordinate limit; no owner approval. |
| Effective catalyst density passed to V2 engine | `ρ_active,eff = Wcat/[A L (1−ε_b)]` so the engine's derived bed length equals the declared `L` and its bulk catalyst loading equals `Wcat/(A L)` | Algebraic mapping of measured source mass/diameter, the declared `ε_b`, and the model's code convention; not a physical pellet density | Label it *active-equivalent density*, never report it as a measured particle density. This is a bookkeeping bridge required by V2's `derive()` API. |
| Forcing | 10% common in-phase cosine modulation of modeled reactive feed, 20 Hz, fixed `P,T,Q`; argon implicit as balance | 10% common modulation follows V2 implementation pattern; 20 Hz is selected relative to the declared scenario residence-time scale | Entirely illustrative: Urmès reports no such forcing or transient. Do not infer a best frequency, surface-memory response, or BEP operating proposal. |
| Axial grid / time solver | Finite-volume `N_z=64` baseline; BDF with `rtol=1e-6`, `atol=1e-10`; compare N_z=32/64/128 and a tighter temporal solve | V2 `SolverSettings`, `TVD2`, BDF; `ma_stiff_solver`, `ma_numerical_checks` | These are numerical settings, not physical data; acceptance checks below. |

## 5. Source choice trace and alternatives

| Model decision | Evidence and map links | Why selected / alternative deferred |
|---|---|---|
| Gas-only axial state and method of lines | V0 `reactor_model`; V1/V2 `pbr/solver.py::Model.rhs`; proposal §3.1; `ma_gas_pde`, `ph_axial_balance`, `ma_pde_ode_coupling`, `ma_conservative_finite_volume` | Retains V0's central bulk-gas balance while removing its unsafe mutable state-view, unsupported microkinetics, and pellet stencil. Reuses tested V2 bulk transport and source terms. |
| Algebraic Urmès PSSA kinetics | S3/S4 `Urmes2019Rate`; Urmès printed pp. 3–6; `c2_urmes_2019_effective_rates`, `c2_urmes_2019_adsorption_denominator`, `c2_urmes_2019_net_rates`, `c2_urmes_2019_parameter_ledger`, `c2_pssa_not_steady_reactor` | It is parameterized and source matched for steady Pd kinetics. V0 elementary surface ODEs are deferred because constants are all zero placeholders and dynamic `theta` would need real elementary time scales (`c2_dynamic_theta_model_calibration_gap`). |
| Uniform pellet, no film | Urmès Table 7 p. 10; `ph_pellet_transport`, `internal_diffusion_thiele`, `external_film_transfer`; V2 `Uniform` and `NoExternalResistance` | The original kinetic experiment reports low source-system transport criteria. Resolved pellet diffusion / Fuller `D_e` is deferred because this vertical slice does not need it and the integrated map lacks the specific Fuller source/correlation. Revisit for target catalyst only with particle/transport evidence. |
| No axial dispersion / fixed velocity | V1/V2 and pbr closures; `ph_axial_dispersion`, `ph_danckwerts`, `ph_variable_superficial_velocity`, uncertainty `target_total_flow_velocity_closure` | Keeps a bounded hyperbolic model. No target tracer evidence supports a dispersion coefficient; source total flow is highly inert diluted, but V3 still does not solve pressure drop or composition-dependent flow. |
| Isothermal | Urmès conditions and source Table 7 heat-transfer criteria; proposal §3.1; `ph_isothermal`, `ph_energy_balance` | Supported for the source experiment's conditions, not independently established for BEP. An energy PDE is deferred. |
| Common composition modulation | V2 inlet helper and S5's transport teaching narrative; `ma_initial_boundary`, `ma_pde_ode_coupling` | Demonstrates gas residence response with a specified forcing. It is not a published input or an owner-approved experiment design. A future BEP run should instead use measured MFC/analyzer transfer functions and a selected actuator waveform. |

Dynamic coverages with `dtheta/dt=(theta_ss−theta)/tau` are explicitly rejected for this V3 baseline: V2's relaxation option is a generic linear extension, not a fitted mechanism, and no source supports `tau`. True elementary dynamic coverages are also deferred because V0 has zero constants and Urmès fitted composite rates do not identify all elementary rates. A separate sensitivity-only relaxation experiment would need a future blueprint amendment and prominent assumed-parameter labeling.

## 6. Numerical acceptance criteria

The notebook is acceptable as a runnable vertical slice if it records all of the following as observed outputs (not only assertions inspected by eye):

1. **Source and parameter transcription:** all Table 5 baseline values, units, temperatures, feed fractions, pressure, `Ftot`, catalyst mass, tube ID, particle-size interval and Table 7 ratios are printed in one provenance table. The 611/13 comparison is visible with both exact page locators.
2. **Kinetic algebra:** at nonnegative source-condition partial pressures, all rates/coverages are finite; coverages are nonnegative and sum with `θ*` to 1 within `1e-12`; the two reaction vectors conserve C and H exactly.
3. **Geometry and unit-basis check:** the active-equivalent `rho` passed to the engine reproduces declared `L` to `1e-10` relative tolerance; `u_s=Q/A`, `u_i=u_s/ε_b`; and `ρ_active,eff(1−ε_b) A L = Wcat` within `1e-12` relative tolerance. List units alongside each derived value.
4. **RHS checks:** the right-hand side does not mutate the input state; matching uniform gas and inlet has zero advection; disabling radial states makes RHS/results independent of the diffusivity sentinel; no NaN/Inf.
5. **Transient run:** BDF reports success; the run covers at least 5 periods at 20 Hz after a constant-feed baseline initialization; all concentrations are finite and minimum concentration is no lower than `−1e−8 mol m⁻³`; plot inlet/outlet partial-pressure or concentration histories and identify that delay comes from the gas model, not surface dynamics.
6. **Resolution/tolerance sensitivity:** compare source-condition steady outlet conversion and ethane flow across `N_z=32,64,128`; report the 64→128 relative change, target `<1%`. Compare the baseline and tighter temporal tolerances (`rtol=1e-8`, `atol=1e-12`) for the periodic run at shared output times; report relative RMS change, target `<1%`. A miss must be recorded and grid/step settings changed narrowly.
7. **Published steady point:** compare predicted acetylene conversion and ethane outlet flow at condition 1 (1.0% C₂H₂ feed) for 51°C and 62°C against Urmès Table 1 printed p. 4 (`X=0.13,0.23`; `F_C2H6=0.07,0.11 μmol s⁻¹`) and Table 6 p. 10 conditions (`Ftot=149 μmol s⁻¹`, `Wcat=0.1 g`, `P=1.26 bar`). Record absolute/relative differences and Table 1's reported repeatability RSDs (conversion 9.3/7.8%, ethane 19/16%) as context, not formal confidence intervals. Table 1 pools repeats across two catalyst loadings, so this is an attempted point check, not an exact individual-run reconstruction. Do not retune parameters to force agreement.
8. **Evidence level:** distinguish a code check, numerical resolution check, comparison with a reported paper point, and experimental validation. The V3 run cannot establish the last of these.

The paper point check is a useful independent run target because the source prints the standard feed, operating conditions, catalyst mass and Table 1 output. A stricter comparison to individual Figure 1/2 points is blocked unless figure data are transparently digitized; no numerical figure table or raw measurements are included in the recovered source.

## 7. Exact theory crosswalk plan

`THEORY_CROSSWALK.md` will map the implemented terms to real integrated-map IDs and source locators: balances to `ma_gas_pde` / `ph_axial_balance` / `ma_conservative_finite_volume`; rates and coverages to `c2_urmes_2019_effective_rates`, `c2_urmes_2019_adsorption_denominator`, `c2_urmes_2019_net_rates`, and `c2_urmes_2019_parameter_ledger`; PSSA scope to `c2_pssa_not_steady_reactor` / `c2_surface_kinetic_closure_choices` / `c2_dynamic_theta_model_calibration_gap`; numerical and boundary choices to `ma_initial_boundary`, `ph_axial_dispersion`, `ma_stiff_solver`, and `ma_numerical_checks`; and model limits to `ph_variable_superficial_velocity`, `ph_pellet_transport`, `external_film_transfer`, `ph_isothermal`, and `ph_energy_balance`. Each owner-map column will say either the actual personal ID and recorded scope or “no live owner concept / not owner-reviewed.” The AI map is not an approval source.

## 8. Owner-review questions left open

- Should this Urmès Pd baseline remain the provisional explanatory model, or should V3 stop at a code demonstration until source-aligned PdAg BEP kinetics exist?
- Is the assumed `ε_b=0.45` acceptable for an explicitly illustrative residence-time scenario, given that it sets the dynamic lag?
- Should a future model carry argon and total molar-flow variation explicitly before frequency-response interpretation?
- How should the primary paper's `K₁` text/table conflict be resolved, if at all, beyond reporting both and using Table 5 for the fitted-model attempt?
- Which equation/closure should the owner work through first before any supervisor-facing scientific claim?

## Gate C disposition

This is a bounded, source-traceable implementation plan. It uses the tabulated Urmès fit as a provisional baseline, removes unsupported dynamic coverages and unneeded pellet diffusivity, and makes bed-holdup assumptions explicit. If the benchmark point comparison fails or differs, V3 remains a useful executable vertical slice with an evidenced limitation; no parameters are to be adjusted merely to manufacture agreement. Implementation may start only with this blueprint recorded and the associated owner uncertainties retained.
