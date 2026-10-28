# Wayfinder: BEP V4 Dynamic Reactor Model & Literature Benchmarks

## 1. Destination
A scientifically verified, self-contained, reproducible 1D dynamic packed-bed reactor simulation suite for acetylene semi-hydrogenation with competitive Carbon Monoxide ($CO$) inlet modulation. Delivered as clean, standalone Jupyter notebooks in the **Legacy Reactor Format** and consolidated via PR #6 (`unified-reactor-model` -> `main`) for supervisor Damian Vico van Berkel to clone and run directly on his laptop with zero custom package installations.

**Runbooks & Governing Standards:**
- Workspace Guide: [AGENTS.md](../../AGENTS.md)
- Physical & Mathematical Framework: [Structure.md](../../Structure.md)
- Supervisor Guidance: [2026-10-23 supervisor meeting](../notes/meetings/2026-10-23_supervisor_meeting.md)
- Literature Library & Errata: AAPM `resources.md` and `conventions.md` §12 (outside this checkout)
- Master Dispatch Prompts: [MASTER_DISPATCH_PROMPTS.md](prompts/MASTER_DISPATCH_PROMPTS.md)

---

## 2. Settled Decisions
- [x] **Zero-Hallucination Citations (Rule 16)**: Kinetics anchored strictly in peer-reviewed literature. Parameters extracted from primary HTML/PDF sources (2026-10-24).
- [x] **Competitive CO Adsorption Core**: The central thesis question is dynamic decoupling of activity and selectivity via periodic $CO$ inlet modulation ($0\text{--}500\ \text{ppm}$) using Schbib et al. (1996) Langmuir-Hinshelwood kinetics with cubed denominator $[1 + K_H C_H^{1/2} + K_{CO} C_{CO}]^3$ (2026-10-23 meeting).
- [x] **V4 Transient Standard (No PSSA)**: Pseudo-Steady-State Approximations ($\partial C / \partial t = 0$, $\partial \theta / \partial t = 0$) are strictly banned. The gas accumulation term $\varepsilon_b \frac{\partial C_{b,i}}{\partial t}$ is actively resolved via Method of Lines into a stiff ODE system solved with SciPy BDF/Radau (2026-10-25).
- [x] **Legacy Reactor Format Code Standard**: All notebook models must be self-contained in a single inspectable script (`ModelParams` dataclass $\rightarrow$ `calculate_rates` $\rightarrow$ `reactor_ode_rhs` $\rightarrow$ `solve_ivp(method='BDF')` $\rightarrow$ inline matplotlib plots) (2026-10-25).
- [x] **Structured Legacy Goal Architecture**: Each child branch carries its own `GOAL.md` (completion authority) and `TODO.md` (numbered subgoals `01` to `05` with explicit gate receipts) (2026-10-25).

---

## 3. Active Frontier & File Topology

### Island 1: Laboratory Steady-State Benchmark with CO
* **Branch:** [`feat/schbib-co-benchmark`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/schbib-co-benchmark)
* **Governing Files:** `GOAL.md`, `TODO.md`, [agent_1_schbib_steady_state.md](prompts/agent_1_schbib_steady_state.md)
* **Source Assets:**
  - Machine-readable HTML: [schbib_1996_full_article.html](../literature/schbib_1996_full_article.html) (Tables 3, 4, 6, 8)
  - Primary PDF: [schbib_1996_front_end_acetylene_hydrogenation.pdf](../literature/schbib_1996_front_end_acetylene_hydrogenation.pdf)
  - Text extraction: [schbib_1996_extracted_text.txt](../literature/schbib_1996_extracted_text.txt)
* **Active Tickets:**
  - [ ] **T1.1: 1D Steady-State PFR ODE Formulation** (`wayfinder:task`) — *Implement $dF_i/dz$ and non-isothermal $dT/dz$ with Schbib rate laws.*
  - [ ] **T1.2: Figure 1 & 2 Reproduction** (`wayfinder:task`) — *Replicate $X_i(T)$ and $r_i(T)$ curves across $T \in [290, 360]\ \text{K}$.*
  - [ ] **T1.3: Figures 3 & 4 Runaway Suppression** (`wayfinder:task`) — *Simulate axial profiles showing thermal runaway prevention via CO.*
  - [ ] **T1.4: Table 6 Conversion Benchmark** (`wayfinder:task`) — *Validate model conversions against measured values at 150, 1400, 5000 ppm CO.*
* **Primary Code Deliverable:** `notebooks/benchmarks/schbib_1996_steady_state.ipynb` (runs in < 60s).

### Island 2: V4 Dynamic Coupled Packed-Bed Reactor Engine
* **Branch:** [`feat/v4-dynamic-reactor`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/v4-dynamic-reactor)
* **Governing Files:** `GOAL.md`, `TODO.md`, [agent_2_v4_dynamic_coupled.md](prompts/agent_2_v4_dynamic_coupled.md)
* **Source Assets:**
  - Vendored Engine: `notebooks/reference/v3/vendor/pbr/` (`chemistry.py`, `solver.py`, `closures.py`)
  - Framework Spec: [Structure.md](../../Structure.md)
* **Active Tickets:**
  - [ ] **T2.1: CO Chemistry & Schbib Rate Integration** (`wayfinder:task`) — *Add CO species and cubed denominator kinetics to `pbr.chemistry`.*
  - [ ] **T2.2: True Transient MOL-ODE Verification** (`wayfinder:task`) — *Verify active accumulation $\varepsilon_b \partial C_{b,i} / \partial t \neq 0$ and BDF solver convergence to steady state.*
  - [ ] **T2.3: Danckwerts Periodic Inlet Forcing** (`wayfinder:task`) — *Implement $C_{\text{CO,in}}(t) = C_{\text{CO,mean}} + \Delta C_{\text{CO}} \operatorname{sgn}(\sin(2\pi t / \tau_p))$ across $\tau_p \in [0.1, 10]\ \text{s}$.*
  - [ ] **T2.4: 2D Wave Propagation & Limit Cycles** (`wayfinder:task`) — *Generate spatiotemporal heatmaps $C_i(z, t)$ and phase planes ($X(t)$ vs. $S(t)$).*
  - [ ] **T2.5: Pareto Dynamic Enhancement Gate** (`wayfinder:task`) — *Calculate cycle-averaged $(\overline{X}, \overline{S})$ proving enhancement over steady state.*
* **Primary Code Deliverable:** `notebooks/reference/v4/unified_v4_dynamic_reactor.ipynb` (planned; no implementation is present in this checkout).

### Island 3: Transport Theory, Mathematical Rigor & Oral Defense Prep
* **Branch:** [`feat/personal-map-alignment`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/personal-map-alignment)
* **Governing Files:** `GOAL.md`, `TODO.md`, [agent_3_theory_and_defense.md](prompts/agent_3_theory_and_defense.md)
* **Source Assets:**
  - Supervisor transcript: [2026-10-23 supervisor meeting](../notes/meetings/2026-10-23_supervisor_meeting.md)
  - Theoretical Conventions: AAPM `conventions.md` & `resources.md`
* **Active Tickets:**
  - [ ] **T3.1: Dimensionless Number Scaling** (`wayfinder:task`) — *Evaluate $Pe_{m,ax}, Pe_p, Da_I, Da_{II}, Bi_m, \Phi$ across the lab operating window.*
  - [ ] **T3.2: Danckwerts Boundary Condition Proof** (`wayfinder:task`) — *Derive flux continuity at $z=0$; prove why Dirichlet conditions violate mass conservation during transients.*
  - [ ] **T3.3: 25-Question Defense Bank** (`wayfinder:task`) — *Author 25 questions with explicit "Supervisor Traps" and rigorous "Model Answers" across 5 themes.*
  - [ ] **T3.4: Personal Mind Map Alignment** (`wayfinder:task`) — *Draft non-destructive alignment proposals in `research/notes/theory_alignment/` using `bep-map-edit-review`.*
* **Primary Theory Deliverable:** `research/notes/theory_alignment/mathematical_formulation_and_defense_prep.md`.

### Island 4: Victor Larsen (2024) PdAg Experimental Curve Replication
* **Branch:** [`feat/larsen-pdag-benchmark`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/larsen-pdag-benchmark)
* **Governing Files:** `GOAL.md`, `TODO.md`, [agent_4_larsen_pdag_benchmark.md](prompts/agent_4_larsen_pdag_benchmark.md)
* **Source Assets:**
  - Primary Thesis: `Articles/2 meeting Damian + Zoë/BEP Example.pdf` (pages 71–88)
  - Ground-Truth Record: AAPM `conventions.md` §12
* **Active Tickets:**
  - [ ] **T4.1: 300 DPI Raster Appendix Extraction** (`wayfinder:task`) — *Render pages 71–88 to PNG; recover $r_{1,\max}, n_{\text{inh}}$, tube geometry, and DE bounds from code screenshots.*
  - [ ] **T4.2: Experimental Curve Digitization** (`wayfinder:task`) — *Extract data points from Appendices B, C, D across $\text{Pd}_0\text{Ag}, \text{Pd}_2\text{Ag}, \text{Pd}_3\text{Ag}$ to CSV.*
  - [ ] **T4.3: 1D Differential Reactor ODE Simulation** (`wayfinder:task`) — *Implement molar balances (Eqs. 4.6–4.9, 6.9–6.11) in the Legacy Reactor Format.*
  - [ ] **T4.4: RMSE Validation & Overlay** (`wayfinder:task`) — *Plot simulated vs. measured curves and verify reported RMSEs ($5.10\%, 5.43\%, 7.14\%$).*
* **Primary Code Deliverables:**
  - `notebooks/benchmarks/larsen_2024_benchmark.ipynb`
  - `notebooks/benchmarks/data/larsen_digitized_curves.csv`

---

## Island 5: Bimetallic PdAg + CO Dynamic Synthesis & Periodic Modulation (The Core BEP Innovation)
* **Branch:** [`feat/pdag-co-synthesis`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/pdag-co-synthesis)
* **Governing Files:** `GOAL.md`, `TODO.md`, `notebooks/benchmarks/pdag_co_synthesis.ipynb`
* **Source Assets:**
  - Larsen (2024) Master Thesis (Figure 6.6 & Appendix A 8-parameter kinetic vectors)
  - Schbib et al. (1996) Table 8 / Bos et al. (1993) (Competitive CO chemisorption isotherm)
* **Active Tickets:**
  - [ ] **T5.1: Bimetallic Kinetic Synthesis Formulation** (`wayfinder:task`) - *Unify Larsen PdAg rate expressions with competitive CO adsorption denominator.*
  - [ ] **T5.2: Steady-State Co-Feed Benchmark & Synergy Analysis** (`wayfinder:task`) - *Sweep 0-1500 ppm CO across Pd1Ag0, Pd2Ag1, Pd3Ag1 to quantify Ag site-isolation benefits.*
  - [ ] **T5.3: Periodic Dynamic Inlet Modulation** (`wayfinder:task`) - *Implement square-wave CO pulsing with varying period (1-60 s) and duty cycle (0.1-0.9).*
  - [ ] **T5.4: Dynamic Pareto Frontier Evaluation** (`wayfinder:task`) - *Compare steady-state vs. dynamic conversion-selectivity frontiers to test breaking the static ceiling.*
* **Primary Code Deliverable:**
  - `notebooks/benchmarks/pdag_co_synthesis.ipynb`

---

## 4. The Fog of War (Downstream Slices)
- *Island 6: Frequency optimization and asymmetric duty-cycle tuning ({\text{pulse}} \ll t_{\text{purge}}$).*
- *Multi-dimensional radial heat transport & Hotspot mitigation in pilot-scale tubes.*

---

## 5. Out of Scope
- Frontend UI dashboards, web applications, or ELK visualizers.
- Blind parameter fitting without primary literature grounding.
- Direct mutations to the owner's personal mind map without explicit authorization.

