# BEP V3 artifact-to-theory map

**Gate B record.** This compares the five pinned inputs individually. An implementation occurrence is evidence of what code does; it does not establish that the choice is physically correct, source-validated, or understood by the owner. The integrated map is an AI-authored reference graph with an `ai_worked_out` ceiling. Personal-map status below is transcribed from the read-only 2026-10-22 snapshot and its 2026-10-23 owner-review handoff.

## S1 — V0 Python scaffold

**Source:** `sources/S1_v0_python_598de52.py`, pinned in `SOURCE_MANIFEST.md`.

### Implemented theory and evidence

- **States / architecture — source locations:** `ModelParams` lines 8–43; species and grid constants lines 51–65; `reactor_model` lines 124–213. A method-of-lines state vector carries bulk gas `C_b[N_z,4]`, pore gas `c_p[N_z,N_r,4]`, and three adsorbate coverages `theta[N_z,N_r,3]`; with `N_z=20`, `N_r=10`, it has 1,480 coordinates. The code integrates from an all-zero initial state for 10 s with SciPy BDF (lines 218–258). The gas list is H₂, C₂H₂, C₂H₄ and C₂H₆; no inert state is carried.
- **Elementary kinetic proposal — source location:** `calculate_rates` lines 72–121. A single vacant-site balance is `theta_v = 1 - (theta_H + theta_C2H2 + theta_C2H4)`. The candidate steps are dissociative H₂ adsorption/desorption, C₂H₂ adsorption/desorption, adsorbed C₂H₂ hydrogenation to adsorbed C₂H₄, C₂H₄ adsorption/desorption, and hydrogenation to gas-phase ethane. Gas and surface source vectors are handwritten in the same function. `ModelParams.kinetics` sets all eight forward/reverse constants to `(0,0)` and the rate helper reads only the first tuple value, so the saved run does not exercise this chemistry or Arrhenius temperature behavior.
- **Transport equations / closures — source locations:** state unpack at lines 124–142; shell assignment at lines 152–157; radial operator at lines 176–193; pellet rate quadrature at lines 195–202; bulk upwind balance at lines 204–211. The implementation uses spherical coordinates (`s=2`), approximate center/interior finite differences, `c_p(R)=C_b` as a hard no-film assignment, and a first-order backward/upwind bulk derivative. It sets no axial dispersion and has no energy equation. Initial gas and surface states are all zero; inlet values are H₂=10 and C₂H₂=1 mol m⁻³, products zero.
- **Numerical claims / limitations — evidence:** `state.md` §§“What the model is” and “Defect register” record measured code defects D1–D6: RHS mutates the input via a reshaped view; spherical center coefficient is 3 rather than 6; outer-shell coverage derivative is zero; left-endpoint rate quadrature is about 16% low at the default grid; the rate-unit docstring conflicts with its use and history retracts a previous double-`C_t` claim; and dense finite-difference Jacobians make the 1,480-state RHS expensive. The separate framework audit §§3–5 concerns equation/spec conflicts, including velocity/porosity convention, time criteria, a missing readsorption requirement, unsupported energy scope, dead film branch, a Biot-definition inversion, and claims it labels unverified. The audit is an AI transcript-versus-dossier comparison, not the original Berger paper; do not treat its unverified source assertions as primary evidence. The notebook's actual saved run is in S2, not a new run receipt here.

### AI reference and source evidence

- Relevant real nodes: `ma_gas_pde`, `ph_axial_balance`, `ma_surface_balance`, `ma_stoichiometry`, `ma_initial_boundary`, `ma_pellet_scaling`, `ph_pellet_transport`, `external_film_transfer`, `ma_pde_ode_coupling`, `ma_stiff_solver`, `ma_numerical_checks`, `c2_surface_kinetic_closure_choices`, and `c2_dynamic_theta_model_calibration_gap`.
- `ma_gas_pde` / `ph_axial_balance` link to `proposal_main`, Methodology §3.1, lines 180–185. The map describes a dimensionally explicit conservative balance and flags the proposal's compact notation as basis-ambiguous. `bed_equation_basis_and_pellet_scope` explicitly says pellet diffusion is an extension, not the proposal baseline. These general nodes do not validate the V0 discretization or its constants.
- `ma_surface_balance` links to `proposal_main`, Methodology §3.1, lines 187–192, as a proposed dynamic coverage equation. `c2_dynamic_theta_model_calibration_gap` records that dynamic coverage ODEs need independent elementary parameters. No primary source for V0's actual eight rates or values is cited in the code; values are zero placeholders. Therefore the particular V0 elementary kinetics are **unverified / unsupported for simulation**.
- `ph_pellet_transport` supplies a generic spherical pellet equation, but its claim references support a derived extension and other source examples, not V0's particular finite-difference implementation. The exact V0 quadrature/stencil has **no direct AI-map source citation**; map nodes are conceptual context only.
- Numerical choices map to `ma_stiff_solver` and `ma_numerical_checks`; `proposal_main` §§3.1–3.2 is proposal context, while actual defect evidence comes from the reproducible V0 audit ledger, not a paper result.

### Personal-map coverage and review scope

- `own_ma_mathematical_modeling` and `own_ma_surface_kinetic_equations`: **Idea**, structural placement only; source claims are AI-attached and not human-verified. These do not approve the exact V0 equations or its chosen state vector.
- `own_ph_adsorption`: recorded as **Human worked out / Informal Writing** for basic adsorption and surface interaction, with the specific earlier owner-approved page scope. That status does not establish the V0 vacancy balance, dissociative H₂ model, rate equations, catalyst match or citations.
- `own_ph_isothermal_theory`: **Human worked out only** for the globally fixed-temperature physical special case. It does not approve V0's `T=400 K`, the absence of an energy equation, or a specific model assumption.
- There is no live owner-approved Reactor Model or model-approximation node. The model-specific tree was withdrawn to the Q92 review queue/archive. No personal-map update is authorized or made.

**Execution status:** source code and its recorded defect probes were inspected; no independent V0 run in this gate. The zero-rate defaults make a successful integration a transport scaffold check, not a kinetic prediction.

## S2 — Migrated legacy notebook

**Source:** `sources/S2_migrated_legacy_main_b627945.ipynb`, pinned in `SOURCE_MANIFEST.md`.

### Implemented theory and evidence

- The 11-cell notebook has five code cells. Markdown describes a 1,480-state MOL PBR; code cells 2, 4, 6, 8 and 10 reproduce the V0 parameter class, 20×10 grid/species, elementary rate function, bulk/pore/coverage RHS and BDF execution. The notebook's code agrees with S1's model semantics: zero kinetic constants, `C_s=C_b`, spherical center approximation, left-endpoint pellet rate weights and zero initial state.
- Code cell 10 contains a saved stream output: “Simulatie succesvol afgerond in 324.70 seconden!” and 83 BDF points. This is stored historical output, not an independently repeated run. Since all reaction constants are zero and initial gas is zero, that output is not evidence of active chemistry or a kinetic result.
- No independent equations, parameters, closure, calibration or simulation are added by migration. It is a second presentation of the V0 scaffold, not an independent model revision.

### AI reference and source evidence

- Same contextual IDs as S1: `ma_gas_pde`, `ph_axial_balance`, `ma_surface_balance`, `ma_stoichiometry`, `ma_initial_boundary`, `ph_pellet_transport`, `ma_pde_ode_coupling`, `ma_stiff_solver`, `ma_numerical_checks`, and `c2_dynamic_theta_model_calibration_gap`.
- Direct source evidence for the notebook's exact implementation is the notebook cells themselves and S1; `proposal_main` §§3.1–3.2 is project intent, not proof of the notebook's equations. The V0 `state.md` defect ledger is execution-derived audit evidence. No source citation for the placeholder elementary constants is present.

### Personal-map coverage and review scope

Coverage and limits are the same as S1. Seeing or migrating the concept into a notebook does not move `own_ma_mathematical_modeling` or `own_ma_surface_kinetic_equations` beyond Idea / structure-only. No owner review of these specific equations or saved outputs is recorded.

**Execution status:** notebook contains stored output from the source revision; not rerun during Gate A. Output claim is explicitly separated from V3 execution evidence.

## S3 — V1 dynamic-response notebook

**Source:** `sources/S3_v1_dynamic_response_791e51c.ipynb`, pinned to the V1 PR #1 branch commit. It shares its path with S4 but is a distinct Git object.

### Implemented theory and evidence

- **Narrative/closures:** cells 0–1 state plug flow, no axial dispersion, spherical finite-volume pellet, center symmetry, `c_p(R)=C_b` (no external film), porosity-inclusive `D_e=ε_pD_m/τ` with pore operator `D_e/ε_p`, conservative bulk/pore exchange, and algebraic Urmès PSSA; it explicitly excludes dynamic coverages.
- **Configuration:** cell 4 sets `N_z=4`, `N_r=5`, 200 Hz, 10% common cosine modulation, 12 periods, 60 samples/period, 1% settling heuristic with 3 consecutive pairs, BDF, `rtol=1e-4`, `atol=1e-8`. Cell 8 builds the model from `Inputs.catalogued("urmes2019")`, sets spherical radial geometry and `TVD2`, initializes bulk and pellet gas uniformly to inlet concentration, and integrates with dense output and sparse Jacobian pattern.
- **Kinetics and parameters:** cells 5–6 render the V2 `PROVENANCE` registry. Kinetics, temperature, pressure, flow and composition are tagged to Urmès 2019. Particle radius is derived from the midpoint of its 100–200 μm sieve fraction; porosity, particle density, tortuosity, bed void fraction and geometry/mass choices include transferred/assumed values. The notebook says diffusivity is a Fuller–Schettler–Giddings estimate with `D_e=ε_pD_m/τ`, not a measured BEP pellet value. The AI map has no Fuller source record/node for that correlation in this edition; it is **unmapped in the integrated map**, even though the upstream code carries a citation key.
- **Saved calculation:** cell 8's stored output reports solver success, 0.20 s, `nfev=509`, range 0–36.01 mol m⁻³. Cell 15 reports a 1% cycle-pair heuristic passing at the final 5 pairs, beginning period 7. Cell 18 reports exact-overlap trajectories for same-`R²/D_e` variants at its coarse V1 grid. These are saved source-revision outputs and code-level sensitivity diagnostics, not target experiments or independent runs in this task.
- **Model code provenance:** the V1 commit's `pbr/` blobs are byte-identical to S4's V2 `pbr/` blobs (verified through Git tree object IDs). Its notebook plotting helper differs from V2. Thus the broad engine implementation is the same; the V1 notebook configuration and diagnostics differ.

### AI reference and source evidence

- Exact useful IDs: `c2_urmes_2019_effective_rates`, `c2_urmes_2019_adsorption_denominator`, `c2_urmes_2019_net_rates`, `c2_urmes_2019_parameter_ledger`, `c2_pssa_not_steady_reactor`, `ph_axial_balance`, `ma_gas_pde`, `ph_pellet_transport`, `internal_diffusion_thiele`, `external_film_transfer`, `ma_conservative_finite_volume`, `ma_initial_boundary`, `ma_stiff_solver`, `ma_numerical_checks`, `ph_variable_superficial_velocity`, and `c2_surface_kinetic_closure_choices`.
- The AI map's `urmes2019` source record states full text was AI-read, scoped to 0.05 wt% Pd/α-Al₂O₃ steady tail-end kinetics (printed pp. 2–6 and 9–11), and does not support PdAg transients or target dynamic coverages. `c2_urmes_2019_effective_rates` cites printed pp. 3–6 / Table 3–5; `c2_urmes_2019_adsorption_denominator` cites printed p. 4; `c2_urmes_2019_parameter_ledger` cites printed p. 5 and p. 6 Table 5.
- `ph_pellet_transport` cites `shi2024` and proposal-derived extension context, not the specific Fuller correlation or a BEP diffusivity. `transport_and_residence_time` remains open because no target tracer, particle or transport coefficients are available. `target_total_flow_velocity_closure` and `target_boundary_domain_and_flux_closure` are also unresolved.
- `urmes2019_hydrogen_adsorption_constant` is explicitly `unresolved_primary_source_conflict`: text p. 5 gives 611 Pa⁻¹ and Table 5 p. 6 fixes 13 Pa⁻¹. V1 uses Table 5's 13. It does not investigate the contradiction. An upstream V2 code comment calls it “resolved”; that comment is **not adopted** as a resolution of the paper's own conflicting statements.

### Personal-map coverage and review scope

- `own_ma_mathematical_modeling` and `own_ma_surface_kinetic_equations` remain Idea / structure-only. Their presence does not approve the V1/V2 package or Urmès equation for the BEP.
- Related live kinetic-topic records `own_ma_lh_surface_rate_forms`, `own_ma_h2_dissociative_equilibrium`, and `own_ma_arrhenius_temperature_dependence` are Idea; the recorded owner scope is summary/structural approval only, not full equation understanding. `own_ph_h2_adsorption_equilibrium` is AI worked out but explicitly not owner-understood. `own_ph_adsorption`'s basic physical concept/writing scope does not extend to the Urmès PSSA derivation.
- `own_ph_isothermal_theory` covers only the elementary globally fixed-T physical special case. There is no live owner-approved no-film, no-dispersion, pellet diffusion, boundary or constant-velocity model-assumption node. Q92 says the former Reactor Model proposal is queue/archive pending one-at-a-time review.

**Execution status:** saved outputs are present; this V1 notebook was not independently executed in Gate A. The engine/tests were independently rerun from the later exact S4 commit, and the V1 engine blob hashes match V2.

## S4 — V2 dynamic-response notebook

**Source:** `sources/S4_v2_dynamic_response_2ee0dc1.ipynb`, pinned to the V2 PR #2 commit. This is not the V1 object.

### Implemented theory and evidence

- **PDE/closures:** cells 0–1 define dynamic bulk and pore gas, spherical cell-centered finite-volume radial diffusion, no axial dispersion, no external film, porosity-inclusive diffusivity `D_e=ε_pD_m/τ`, equal/opposite bulk–pore interface exchange, and Urmès PSSA gas rates. Coverages are algebraic; no surface memory ODE is present. `pbr/discretisation.py::radial_diffusion_fv` uses shell concentration as a boundary value, and `pbr/solver.py::Model.rhs` applies the pellet chemistry source once and the opposite surface flux in the bulk balance.
- **Kinetic equations:** `pbr/chemistry.py::Urmes2019Rate.rates` implements `D=1+√(K₁p_H₂)+K₂p_C₂H₂+p_C₂H₄/K₅`; `r_A=N_S k₄⁰e^(−E₄/RT)K₁K₂p_C₂H₂p_H₂/D²`; `r_E=N_S k₇⁰e^(−E₇/RT)(K₁/K₅)p_C₂H₄p_H₂/D²`; gas source `(-r_A-r_E,-r_A,r_A-r_E,r_E)`. `parameters.py::Urmes2019` records raw pre-exponential Arrhenius form (not a centered form). `parameter_sets.py::urmes_2019` selects Table 5 values. The two gas reactions conserve C/H in the reduced represented system, but omit other carbon products and are scoped to the source conditions.
- **Operating and geometry choices:** cells 4–8 set 200 Hz, 10% common cosine modulation, 16 periods, 60 samples/period, `N_z=8`, `N_r=12`, BDF, `rtol=1e-4`, `atol=1e-8`; initialize uniform bed/pore composition at the peak inlet and use a sparse Jacobian. The `urmes2019` catalogue takes `T=324.15 K`, `P=126 kPa`, `Q=200 mL/min`, feed fractions C₂H₂=.010, C₂H₄=.70, H₂=.043, Ar=.247. It takes the Urmès particle radius midpoint 75 μm, but uses a 5 mm tube and 75 mg catalyst mass from a different source/assumption; particle porosity=.50, particle density=1550 kg/m³, tortuosity=3 and bed void=.45 are transferred/assumed. `D_e` is derived from a Fuller binary gas correlation with tortuosity; the source map does not contain that named citation or a matching reference node.
- **Flow, boundary and energy:** `pbr/solver.py::derive` computes one constant superficial velocity from inlet volumetric flow and area; no total-flow/pressure-drop coupling. No-axial-dispersion closure makes the inlet concentration condition plus convective outflow appropriate to the chosen model, but actual BEP boundary domains are unknown. The model is isothermal and contains no energy equation.
- **Saved V2 run:** final cell output reports Python 3.12.14, NumPy 2.5.3, SciPy 1.18.0, Pydantic 2.13.5; baseline success at 8×12, 0.464 s, `nfev=890`, `njev=4`, `nlu=80`, output range 0–36.02 mol m⁻³. The five final cycle pairs pass the 1% relative-RMS settling heuristic. The equal-`R²/D_e` tests overlap exactly in stored results. These receipts support execution and implementation-similarity only; there is no mesh/time convergence, source-matched Urmès reactor benchmark, BEP calibration or experiment validation.
- **Independent engine verification:** exact S4 `pbr/` and three test files were extracted and their tests rerun in the environment recorded in `SOURCE_MANIFEST.md`; 63 tests passed. The upstream handoff and saved notebook outputs remain distinct from this test receipt.

### AI reference and source evidence

- Exact useful IDs: `c2_urmes_2019_effective_rates`, `c2_urmes_2019_adsorption_denominator`, `c2_urmes_2019_net_rates`, `c2_urmes_2019_parameter_ledger`, `c2_pssa_not_steady_reactor`, `c2_surface_kinetic_closure_choices`, `c2_dynamic_theta_model_calibration_gap`, `ph_axial_balance`, `ma_gas_pde`, `ph_pellet_transport`, `ma_pellet_scaling`, `internal_diffusion_thiele`, `external_film_transfer`, `ma_conservative_finite_volume`, `ma_initial_boundary`, `ma_stiff_solver`, `ma_numerical_checks`, `ph_variable_superficial_velocity`, `ph_axial_dispersion`, and `ph_danckwerts`.
- `urmes2019` source record: full article PDF AI-read; printed pp. 2–6 Tables 2–5 and pp. 9–11; 0.05 wt% Pd/α-Al₂O₃, intrinsic steady kinetics, not PdAg transient validation. Printed p. 4 contains the rate derivation and reduced single-site denominator; Table 5 p. 6 has fitted/fixed values. Printed p. 5 has the conflicting hydrogen constant estimate. This was independently checked in the local source PDF for this map exercise; personal source review remains unapproved and unrecorded.
- `ph_axial_balance` / `ma_gas_pde` use the proposal and explicitly warn that density/rate/velocity bases must be specified; `bed_equation_basis_and_pellet_scope` says pellet diffusion is an extension. The V2 implementation is a coherent finite-volume extension, not a verbatim implementation of the proposal PDE.
- `ma_conservative_finite_volume` links proposal-derived cell balances to `di_giuliano_pellegrino2019`; it is a general numerical reference, not experimental verification of the V2 reactor.
- `transport_and_residence_time`, `target_boundary_domain_and_flux_closure`, and `target_total_flow_velocity_closure` remain open. `ph_variable_superficial_velocity` explains the variable-flow alternative; no target data chooses it. Fuller diffusivity provenance is absent from the AI map and therefore **unmapped** here.

### Personal-map coverage and review scope

Same current records and limits as S3. In particular, no personal `Reactor Model`, no approved implementation closure nodes, no Human worked out Urmès equation, no human verification of the source citation, and no owner approval of constant velocity, no-film, no-dispersion, pellet/diffusivity or bed geometry choices is present. Do not infer approval from the V2 branch or its technical handoff.

**Execution status:** source notebook's stored 22-cell outputs are present; source package unit/integration tests have a fresh independent 63/63 receipt. The V2 notebook itself has not been rerun as the V3 artifact.

## S5 — BEP presentation / explanatory notebook

**Source:** `sources/S5_presentation_598de52.ipynb`, pinned in `SOURCE_MANIFEST.md`.

### Implemented theory and evidence

- **Conceptual route:** cells 0–1 explain why bulk concentration alone may not encode pore concentration or adsorbate coverage; they describe `C_b(z,t)`, `c_p(z,r,t)`, and `theta(z,r,t)` as distinct field types. Cell 4 presents a schematic advection–reaction PDE and MOL statement `dy/dt=F(t,y;p)`.
- **Numerical illustration:** cell 5 checks the spherical-center identity for `c=r²`. Cells 7–8 deliberately simulate one inert tracer using pure one-dimensional upwind advection, smooth tanh inlet step, 20 axial cells, BDF, no reaction, no radial field and no kinetic parameters. Stored output includes a figure and solver count. Cell 9 explicitly says this is not conversion, selectivity, a kinetic fit or experimental agreement.
- **Evidence boundary:** the diagram is labelled not a simulation output; the transport-only trace is illustrative. The stated V0 grid sizes are explanatory context. This artifact offers a clear teaching sequence, not a second reactor implementation and not evidence for the physical rate law.

### AI reference and source evidence

- Relevant IDs: `ma_gas_pde`, `ma_initial_boundary`, `ma_pde_ode_coupling`, `ma_stiff_solver`, `ma_numerical_checks`, and (as conceptual rather than implemented model) `ph_pellet_transport` / `ma_surface_balance`.
- `proposal_main`, Methodology §3.1 lines 180–192 and §3.2 lines 207–208, is project context for the distributed model and candidate BDF method. It is not evidence for the notebook's tanh input, transport-only result or a target actuator. No primary paper is cited for that numerical tracer illustration; those claims are supported by the executable cell alone.
- The exact V0 defect ledger supports the need to keep source-state mutation and center-stencil checks visible, but S5's own small tracer RHS is a separate implementation and does not audit the BEP `pbr` engine.

### Personal-map coverage and review scope

`own_ma_mathematical_modeling` is Idea / structural placement only; no live Math node records MOL or the specific presentation notebook's tracer demonstration. The basic adsorption node and the elementary fixed-temperature concept are not evidence that the owner understood this transport/numerics example. No owner review of S5 or personal-map update is recorded.

**Execution status:** S5 contains stored code outputs and assertions; not independently rerun during Gate A. Its own limitation text rules out interpreting the trace as kinetic or experimental evidence.

## Cross-source comparison and gap register

| Topic | What the five sources actually do | Map/evidence connection | Owner coverage / status |
|---|---|---|---|
| Surface closure | S1/S2 propose dynamic elementary `theta` ODEs with zero constants; S3/S4 use Urmès effective PSSA rates and no surface state; S5 has no surface chemistry. These closures cannot be combined by simply retaining V0 coverages while inserting the Urmès fitted rates. | `ma_surface_balance`, `c2_surface_kinetic_closure_choices`, `c2_pssa_not_steady_reactor`, `c2_dynamic_theta_model_calibration_gap`; reconciliation `pssa_vs_dynamic_coverages`; `urmes2019` printed pp. 3–6 vs proposal §3.1 lines 187–192. | Surface mathematical model `own_ma_surface_kinetic_equations` is Idea / structural only. Dynamic elementary rates are unparameterized. Urmès PSSA equation is not personally reviewed. |
| Urmès kinetics / `K₁` | S3/S4 use `K₁=13 Pa⁻¹` from Table 5. The source itself prints `611 Pa⁻¹` as a calculated estimate on p. 5 and `13 Pa⁻¹` fixed in Table 5 p. 6. V2 comments' coverage check does not erase that primary-source conflict. | `c2_urmes_2019_effective_rates`, `c2_urmes_2019_adsorption_denominator`, `c2_urmes_2019_parameter_ledger`; source `urmes2019`, printed p. 4 derivation, p. 5 estimate, Table 5 p. 6; reconciliation `urmes2019_hydrogen_adsorption_constant` is unresolved. | `own_ma_lh_surface_rate_forms`, `own_ma_h2_dissociative_equilibrium`, `own_ma_arrhenius_temperature_dependence` all Idea / summary-structure scope; `own_ph_h2_adsorption_equilibrium` is AI worked out but not owner-understood. No human source verification. |
| Gas balance / rate basis | V0 uses hand-built bulk/pore factors and an unclear `R_gas` docstring; V2 uses net gas rates per catalyst mass, a finite-volume pore balance, and opposite interfacial flux. Both use a constant-flow velocity closure. | `ph_axial_balance`, `ma_gas_pde`, `ma_stoichiometry`, `ma_pde_ode_coupling`, `ma_conservative_finite_volume`, `ph_variable_superficial_velocity`; `bed_equation_basis_and_pellet_scope`; `target_total_flow_velocity_closure`. | `own_ma_mathematical_modeling` is Idea / structural only; no owner-approved reactor balance/basis or total-flow closure node. |
| Pellet / film / bed dispersion | V0 has a node-centered pellet stencil and hard `c_p(R)=C_b`; V1/V2 use cell-centered radial FV and finite intrapellet diffusion, with no film and no axial dispersion; S5 has no pellet. Urmès Table 7 reports low transport criteria only for its own crushed/diluted Pd/α-Al₂O₃ conditions. | `ph_pellet_transport`, `internal_diffusion_thiele`, `external_film_transfer`, `ph_axial_dispersion`, `ph_danckwerts`, `ma_initial_boundary`; source `urmes2019` Table 7 / printed pp. 9–10; `transport_and_residence_time`, `target_boundary_domain_and_flux_closure`. | No live personal transport or reactor-approximation nodes. Q92 model-approximation subtree is queue/archive. No target particle/tracer data or user approval. |
| Diffusivity / geometry | V1/V2 derive `D_e` through a Fuller correlation and assumed tortuosity; V2 uses Urmès radius midpoint but other-source tube/mass/bed/pellet assumptions. V0's values are placeholders. | `ph_pellet_transport` is general context; V2's source key `fullerSchettlerGiddings1966` has **no matching source record or exact correlation node** in integrated `sources.yaml` / `nodes.yaml`; mark **unmapped**. V2 registry is code provenance, not a map/source record. | No approved personal-map parameter or transport choice. D_e and borrowed geometry are assumptions, not target measurements. |
| Axial dispersion / boundaries | V1/V2 disable axial dispersion; their inlet/outflow choices follow a hyperbolic plug-flow model. The proposal says Danckwerts-type conditions but does not specify apparatus domains or detailed equations. | `ph_axial_dispersion`, `ph_danckwerts`, `ma_initial_boundary`; primary source `danckwerts1953` printed pp. 9–11, Eqs. 27–32 is a steady first-order basis, not a universal target boundary; uncertainty `target_boundary_domain_and_flux_closure`. | No live owner-approved boundary/dispersion model node. No measured target input/output tracer response. |
| Temperature | S1/S2 fix 400 K; S3/S4 use Urmès 324.15 K; S5 has no reacting temperature model. None carries an energy equation. | `ph_isothermal`, `ph_energy_balance`, `ma_initial_boundary`; source `proposal_main` §3.1 lines 185–197; models' temperature is an implementation choice. | `own_ph_isothermal_theory` Human worked out only for the globally fixed-temperature physical special case; actual selected model condition, thermal adequacy and kinetics are not approved. |
| Presentation evidence | S5's tracer demonstrates a pure transport delay for its illustrative scalar equation; it says it is not a kinetic result. | Generic context `ma_gas_pde`, `ma_pde_ode_coupling`; no source record for the illustrative trace. | No owner review recorded. |

### Unmapped / unverified / unresolved register

1. **Unverified dynamic microkinetics:** V0 elementary constants are placeholders; no source-supported set of forward/reverse constants, gas/surface elemental inventory audit or target calibration is included. `c2_dynamic_theta_model_calibration_gap` supports this gap, not the equations' validity.
2. **Unresolved published source conflict:** `urmes2019_hydrogen_adsorption_constant`: 611 versus 13 Pa⁻¹ in adjacent printed pages; 13 is the Table 5 fitted-model transcription, but its source-internal conflict must be investigated and cited as such.
3. **AI-only source review:** integrated map labels Urmès full-text review AI-checked; personal source claim review is not human verified. Our local PDF text check in this task does not change personal-map status.
4. **PSSA transfer:** the Urmès single-site PSSA fit is for 0.05 wt% Pd/α-Al₂O₃ steady tail-end experiments, not a measured PdAg BEP transient. The fitted closure does not support independent dynamic coverage time constants.
5. **Flow and boundary:** constant superficial velocity, constant pressure, the inlet/outlet domain and omitted axial dispersion are not settled for the target apparatus; exact uncertainties are `target_total_flow_velocity_closure`, `target_boundary_domain_and_flux_closure`, and `transport_and_residence_time`.
6. **Pellet and diffusion data:** no target pellet radius distribution, porosity, density, tortuosity, measured species diffusivity, film coefficient or tracer response. Fuller correlation appears in V2 code provenance but is **unmapped** in this AI-map edition.
7. **Parameter transfer:** the V2 kinetic feed is source-derived; V2 reactor and pellet geometry combines assumptions and source values from different catalyst systems. It is not an Urmès apparatus match.
8. **Model outputs / evidence levels:** source-saved notebook output, a passing code suite, numerical convergence, a paper reproduction and an experiment validation are distinct. Only the V2 code tests have a fresh independent receipt in this task so far; none is an experiment validation.
9. **Owner learning / review:** personal coverage is as listed per artifact. No actual Reactor Model node or closure approval exists; no owner knowledge or citation verification is inferred from any input notebook.

## Gate B disposition

The five artifacts represent three materially different things: (i) a defective, unparameterized dynamic-coverage scaffold (S1/S2), (ii) a transient gas/pellet implementation driven by a steady fitted PSSA closure (S3/S4), and (iii) an explanatory tracer-only presentation example (S5). Their useful methods can inform a later bounded model, but they are not one compatible model to concatenate. The next gate must explicitly select and bound the provisional baseline, state assumptions and missing evidence, and keep all owner review pending.
