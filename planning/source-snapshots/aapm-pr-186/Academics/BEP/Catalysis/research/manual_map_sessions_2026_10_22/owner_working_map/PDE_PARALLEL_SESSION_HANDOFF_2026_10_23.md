> **HISTORICAL — SUPERSEDED 2026-10-23:** This report describes 11 earlier agent placements, not the current approved map. Seven unpreviewed nodes were later withdrawn after owner correction. Read [OWNER_REVIEW_GATE_HANDOFF_2026_10_23.md](OWNER_REVIEW_GATE_HANDOFF_2026_10_23.md) first, inspect live graph and Q86–Q95; do not reinstate this document's old nodes or maturity claims.

# Parallel science map session handoff — physics PDE concepts & Mathematics Reactor Model

**Checkpoint:** Friday 23 October 2026. **Authoritative branch:** `docs/bep-theme-first-progress-units-20261022`; **authoritative live data:** `owner_working_map/current_map.yaml` (refetch GitHub HEAD and blob SHA on every actual write). The owner's speed-run request was to **place actual graph nodes, one at a time**, separating human-owned qualitative understanding from non-owner-verified equations and actual model assumptions. Supporting history, bridged ideas and reader pages must stay maintained; current data fields/stages always come from the live map.

## Mandatory startup

1. Read `.agents/skills/bep-map-edit-review/SKILL.md` and `.agents/skills/reversible-change-review/SKILL.md`, plus the scientific node contract.
2. Fetch latest `current_map.yaml`, `bridges.yaml`, `ACTION_QUEUE_2026_10_22.md`, `state.md`, and this handoff file. The other scientific agent works under Catalyst Surface & Active Sites / Adsorption. It may add nodes or alter status concurrently.
3. Read the relevant owner-facing pages under `owner_working_map/pages/bep/physics/thermodynamics_thermal_dynamics/`, `.../physics/reaction_chemistry_pathways/reaction_heat_generation/`, and `.../mathematics/mathematical_modeling/reactor_model/`. Do not rely on dated state banners over live data.
4. Use the pinned integrated AI reference (not fresh web search) for `ph_axial_balance`, `ma_gas_pde`, `ph_danckwerts`, `ph_axial_dispersion`, `ph_energy_balance`, `ma_pde_ode_coupling`. The original BEP proposal `0_Project_Management/main.tex` §3.1 is a primary local basis. The 2008 Berger equation exists in `Articles/analyses/dynamic_kinetics_berger2008.md`, and an explicit inconsistency warning is in `3_Model/transient_model_framework_audit.md` (see bridge note).

## Work accomplished in one-at-a-time commits (11 placed nodes)

**Owner-owned Physical Tier4 concept (Human worked out):**
- `own_ph_wall_temperature_boundary` under `own_ph_isothermal_theory`: wall Dirichlet sets the boundary, **not** the interior. Human maturity only for that qualitative physical distinction.
- `own_ph_radial_temperature_reduction` under `own_ph_isothermal_theory`: axial z is the long, retained direction; radial r is the dimension omitted/averaged at reactor-bed scale; this differs from axial mass dispersion. Human maturity only for this basic physical distinction.

**Equation children beneath those actual physical concepts (Idea only):**
- `own_ph_wall_dirichlet_equation`, formula `T(R,z,t)=T_w`; not an asserted BEP wall BC or user-derived mathematics.
- `own_ph_radial_temperature_average_equation`, cross-section mean and conditional approximation; no measured small-gradient/rapid-mixing claim.

**Other Physics Idea nodes:**
- `own_ph_thermal_energy_balance_theory` under `own_ph_thermodynamics_thermal_dynamics`, a *theoretical* energy-conservation subject, not the chosen reactor energy equation.
- `own_ph_reaction_heat_generation` under `own_ph_reaction_chemistry_pathways` (chemistry/kinetics lens), with `q'''_rxn=-ΣΔ_rH_j r_j^(V)` as AI background and no claim that the BEP has a third independent reaction rate.

**Mathematics concrete structure, all Idea:**
- Existing `mathematics → own_ma_mathematical_modeling` now contains `own_ma_reactor_model` → `own_ma_model_approximations`.
- Direct children of Approximations: `own_ma_assumption_isothermal`, `own_ma_assumption_radial_reduction`, `own_ma_assumption_axial_dispersion` (all **Idea** until the actual model equations and notebook are verified). Existing Surface Kinetic Equations remains a sibling, not reparented.

**Logic not to lose:** A prescribed wall Dirichlet condition ≠ radially uniform T. Radial cross-section approximation \(T(r,z,t)≈\bar T(z,t)\) does NOT automatically imply global isothermal \(T=T₀\): global isothermal is a *special stronger approximation only when remaining axial/time variations are also negligible or prescribed away*. Axial mass dispersion is a term along retained z, independent of radial reduction; removing it affects boundary-order requirements. Turbulence is out-of-scope speculation, **not** established absence of radial gradients.

## Three distinct bridges, NOT yet part of live personal graph

- `B-MODEL-BC-01` — **mathematical BC requirements**: flux-based Danckwerts/Robin for finite dispersion, inflow Dirichlet for ideal advection, outlet/initial conditions, thermal wall BC. Also its local Berger Eq1/Eq4b provenance note (PDF original must be checked; velocity/porosity ambiguity).
- `B-TP-REDUCTIONS-01` — **future Transport Phenomena theory** of axial species dispersion and reactor-bed radial reduction, without asserting TP has a live parent yet.
- `B-HEAT-LENSES-01` — thermodynamics balance theory vs rate×enthalpy chemical heat source vs future mathematical energy balance. Do not create shared parent just to connect them.
- Existing `B-M1`, `B-M2`, `B-M3` remain theory/math questions for spatiotemporal PDEs, autonomous state derivative, MOL and stiff solver; explicit parent decisions not made. Existing B-P3 (film/pellet/transport), B-LH-ARR-01 (kinetic temperature law) remain related future bridges.

## Parallel-worker contract

**Other science writer:** Owns catalyst site taxonomy, adsorption, LH/LR/ER, and its queued owner-comprehension discussions. Avoid modifying its nodes, approvals or reader files.

**This Mathematics/thermal session:** Has done scoped edits only to physical thermal nodes, existing Math Modeling branch, reaction-heat Idea, bridges/reader pages and state/queue. Future independent worker should claim a **disjoint subtree** (for example Transport Phenomena *only after owner structural approval*, or mathematical BC derivations as AI bridge notes). Document that ownership boundary in a small file before writing to a shared `current_map.yaml`.

**Write discipline:** Every one-node transaction fetches latest blob SHA; add just one approved node + its approval index and decision receipt, update with CAS, read back and verify no unrelated node/stage/source change. Keep reader files in named topic directories; queue/state updates are follow-on commits. If concurrent modifications hit the same file, read back, replay only scoped delta, and verify; never force-push, blind merge/rebase or overwrite unknown sibling changes. For a truly independent research track, branch from fresh science HEAD and write **only new research/bridge files**, then ask for owner-approved, targeted integration into the latest live map.

**Epistemic contract:** Stage Human worked out only for exact concepts the owner paraphrased/approved; page wording not separately read. Equations, catalyst-specific closures, gradients/turbulence, Danckwerts regimes and actual BEP code remain Ideas or AI-sourced with `human_verified=false`. AI worked out requires full source-bounded explanation where only owner understanding is missing; a candidate heading never suffices.

## Next action: reconsolidate rather than proliferate

Review the visible local hierarchy (Thermodynamics with human children; Chemistry heat source; Mathematics model approximations), inspect reader completeness and stage boundaries, compare the original 2008 paper PDF against the local dossier before citing Eq(1)/BC as verified, and identify only the next **one** user-approved scientific concept to discuss. No automatic Formal Writing or broad promoted maturity. Today's Damian portable review/export may be stale relative to live node count; regenerate/review before any sharing.
