# Wayfinder: BEP V3 Dynamic Reactor Model & Literature Benchmark

## 1. Destination
A self-contained, reproducible 1D dynamic packed-bed reactor simulation for acetylene semi-hydrogenation with competitive carbon monoxide ($CO$) modulation, delivered as a clean Jupyter Notebook (`notebooks/unified_dynamic_reactor.ipynb`) and top-level `README.md` on `main` that supervisor Damian can clone and run directly on his laptop without custom package installations.

**Runbooks:** `AGENTS.md`, `Structure.md`, `research/literature/README.md`, `notebooks/v3/GOAL.md`.

---

## 2. Decisions So Far
- [x] **Zero-Hallucination Grounding**: Pinned literature kinetics to the Langmuir-Hinshelwood rate laws and verified constants of Schbib et al. (1996) / Gobbo et al. (2004) Table 1 (2026-10-24, commit `3cd3998`).
- [x] **Primary Reactor Geometry**: Isothermal single packed-bed tube (bench-scale) to isolate 1D transport and CO coverage dynamics, avoiding multi-bed adiabatic cascade complexity for the core baseline (2026-10-25).
- [x] **Delivery Architecture**: PR #6 (`unified-reactor-model` -> `main`) serves as the consolidation route so Damian can clone `main` directly (2026-10-25).
- [x] **Thesis Physics Core**: Focus on periodic $CO$ modulation rather than $H_2$ modulation, because $CO$ acts as a reversible competitive moderator that decouples the activity-selectivity trade-off (2026-10-23 supervisor meeting).
- [x] **Parallel Worker Dispatch & Consolidation Protocol**: Dispatch all 3 workers simultaneously on their isolated branches (`feat/gobbo-steady-state-benchmark`, `feat/v3-coupled-reactor`, `feat/personal-map-alignment`). Once audited, their verified outputs merge into `unified-reactor-model`, sync to the personal map, and merge into `main` for Damian's Monday clone (2026-10-25).

---

## 3. Active Frontier

### Island 1: Steady-State Benchmark (`feat/gobbo-steady-state-benchmark`)
- [ ] **T01: 1D Steady-State ODE System** (`wayfinder:task`) — *Implement the 1D steady-state plug-flow mass balance ODE with Schbib/Gobbo kinetics.*
  - Status: Ready
  - Dependencies: None
  - Artifact: `notebooks/bep_steady_state_benchmark.ipynb`
- [ ] **T02: CO Sensitivity & Pareto Curves** (`wayfinder:research`) — *Run parametric sweeps across inlet CO concentrations (0 to 500 ppm) to reproduce the classic trade-off: declining C2H2 conversion vs surging C2H4 selectivity.*
  - Status: Open
  - Dependencies: T01

### Island 2: Coupled Dynamic Engine (`feat/v3-coupled-reactor`)
- [ ] **T03: 1D Bulk + Radial Pellet MOL Discretization** (`wayfinder:task`) — *Couple 1D axial advection/dispersion to 1D radial intra-pellet diffusion using Method of Lines and stiff BDF integration.*
  - Status: Ready
  - Dependencies: None (branches from `unified-reactor-model`)
  - Artifact: `notebooks/unified_dynamic_reactor.ipynb`
- [ ] **T04: Elemental Mass Conservation Verification** (`wayfinder:task`) — *Implement rigorous assertion checks ensuring total Carbon and Hydrogen flux balances close within 1e-4 tolerance.*
  - Status: Open
  - Dependencies: T03

### Island 3: Periodic CO Modulation (`feat/v3-coupled-reactor`)
- [ ] **T05: Inlet Time-Dependent Forcing** (`wayfinder:task`) — *Implement periodic square-wave inlet CO concentration switching: $C_{\text{CO}}(t) = C_{\text{base}} + \Delta C \cdot \text{sgn}(\sin(2\pi t / T_p))$.*
  - Status: Open
  - Dependencies: T03
- [ ] **T06: Periodic Orbit Settling Heuristic** (`wayfinder:research`) — *Simulate across multiple cycles until the limit cycle converges ($\max |y(t + T_p) - y(t)| < \text{tol}$), calculating cycle-averaged selectivity.*
  - Status: Open
  - Dependencies: T05

### Island 4: Personal Map & Defense Prep (`feat/personal-map-alignment`)
- [ ] **T07: Kinetics & Adsorption Node Alignment** (`wayfinder:task`) — *Document the physical derivation of competitive CO site blocking and dissociative H2 adsorption in `research/notes/theory_alignment/`.*
  - Status: Ready
  - Dependencies: None
- [ ] **T08: Oral Defense Prep Summary** (`wayfinder:grilling`) — *Synthesize concise answers to committee grilling questions on Mears criteria, Weisz-Prater moduli, and PSSA coverage validity.*
  - Status: Open
  - Dependencies: T07

---

## 4. Not Yet Specified (The Fog of War)

### Island: Industrial Scale-Up & Non-Isothermal Dynamics
- *Adiabatic multi-bed cascade with intercoolers* (Gobbo 2004 plant layout).
- *Empirical green-oil oligomerization deactivation over 400 days.*
- *Dynamic thermal runaway margins during CO pulse transitions.*

### Island: Dynamic Forcing Optimization
- *Frequency response and optimal duty-cycle tuning for maximum time-averaged ethylene yield.*
- *Asymmetric pulsing (short sharp CO poison pulses vs long regeneration phases).*

---

## 5. Out of Scope
- Frontend web applications, ELK graph visualizers, or custom GUI dashboards (explicitly forbidden per supervisor instruction).
- Re-estimating kinetic parameters via ab-initio DFT (literature parameters are authoritative for this BEP).
- Unverified modifications to the owner's personal mindmap.
