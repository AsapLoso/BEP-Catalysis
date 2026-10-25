# Wayfinder: BEP V4 Dynamic Reactor Model & Literature Benchmarks

## 1. Destination
A scientifically verified, self-contained, reproducible 1D dynamic packed-bed reactor simulation suite for acetylene semi-hydrogenation with competitive Carbon Monoxide ($CO$) inlet modulation. Delivered as clean, standalone Jupyter notebooks in the **Legacy Reactor Format** and consolidated via PR #6 (`unified-reactor-model` -> `main`) for supervisor Damian Vico van Berkel to clone and run directly on his laptop with zero custom package installations.

**Runbooks & Governing Standards:**
- Workspace Guide: [`AGENTS.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/AGENTS.md)
- Physical & Mathematical Framework: [`Structure.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/Structure.md)
- Supervisor Guidance: [`research/notes/meetings/2026-10-23_supervisor_meeting.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/notes/meetings/2026-10-23_supervisor_meeting.md)
- Literature Library & Errata: AAPM [`Academics/BEP/Catalysis/resources.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/Aa%20Project%20management/Academics/BEP/Catalysis/resources.md) & [`conventions.md` §12](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/Aa%20Project%20management/Academics/BEP/Catalysis/conventions.md#L450-L550)
- Master Dispatch Prompts: [`research/wayfinder/prompts/MASTER_DISPATCH_PROMPTS.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/wayfinder/prompts/MASTER_DISPATCH_PROMPTS.md)

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
* **Governing Files:** `GOAL.md`, `TODO.md`, [`research/wayfinder/prompts/agent_1_schbib_steady_state.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/wayfinder/prompts/agent_1_schbib_steady_state.md)
* **Source Assets:**
  - Machine-readable HTML: [`research/literature/schbib_1996_full_article.html`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_full_article.html) (Tables 3, 4, 6, 8)
  - Primary PDF: [`research/literature/schbib_1996_front_end_acetylene_hydrogenation.pdf`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_front_end_acetylene_hydrogenation.pdf)
  - Text Extraction: [`research/literature/schbib_1996_extracted_text.txt`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_extracted_text.txt)
* **Active Tickets:**
  - [ ] **T1.1: 1D Steady-State PFR ODE Formulation** (`wayfinder:task`) — *Implement $dF_i/dz$ and non-isothermal $dT/dz$ with Schbib rate laws.*
  - [ ] **T1.2: Figure 1 & 2 Reproduction** (`wayfinder:task`) — *Replicate $X_i(T)$ and $r_i(T)$ curves across $T \in [290, 360]\ \text{K}$.*
  - [ ] **T1.3: Figures 3 & 4 Runaway Suppression** (`wayfinder:task`) — *Simulate axial profiles showing thermal runaway prevention via CO.*
  - [ ] **T1.4: Table 6 Conversion Benchmark** (`wayfinder:task`) — *Validate model conversions against measured values at 150, 1400, 5000 ppm CO.*
* **Primary Code Deliverable:** `notebooks/benchmarks/schbib_1996_steady_state.ipynb` (runs in < 60s).

### Island 2: V4 Dynamic Coupled Packed-Bed Reactor Engine
* **Branch:** [`feat/v4-dynamic-reactor`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/v4-dynamic-reactor)
* **Governing Files:** `GOAL.md`, `TODO.md`, [`research/wayfinder/prompts/agent_2_v4_dynamic_coupled.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/wayfinder/prompts/agent_2_v4_dynamic_coupled.md)
* **Source Assets:**
  - Vendored Engine: `notebooks/v3/vendor/pbr/` (`chemistry.py`, `solver.py`, `closures.py`)
  - Framework Spec: [`Structure.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/Structure.md)
* **Active Tickets:**
  - [ ] **T2.1: CO Chemistry & Schbib Rate Integration** (`wayfinder:task`) — *Add CO species and cubed denominator kinetics to `pbr.chemistry`.*
  - [ ] **T2.2: True Transient MOL-ODE Verification** (`wayfinder:task`) — *Verify active accumulation $\varepsilon_b \partial C_{b,i} / \partial t \neq 0$ and BDF solver convergence to steady state.*
  - [ ] **T2.3: Danckwerts Periodic Inlet Forcing** (`wayfinder:task`) — *Implement $C_{\text{CO,in}}(t) = C_{\text{CO,mean}} + \Delta C_{\text{CO}} \operatorname{sgn}(\sin(2\pi t / \tau_p))$ across $\tau_p \in [0.1, 10]\ \text{s}$.*
  - [ ] **T2.4: 2D Wave Propagation & Limit Cycles** (`wayfinder:task`) — *Generate spatiotemporal heatmaps $C_i(z, t)$ and phase planes ($X(t)$ vs. $S(t)$).*
  - [ ] **T2.5: Pareto Dynamic Enhancement Gate** (`wayfinder:task`) — *Calculate cycle-averaged $(\overline{X}, \overline{S})$ proving enhancement over steady state.*
* **Primary Code Deliverable:** `notebooks/v4/unified_v4_dynamic_reactor.ipynb` (runs in < 3 min).

### Island 3: Transport Theory, Mathematical Rigor & Oral Defense Prep
* **Branch:** [`feat/personal-map-alignment`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/personal-map-alignment)
* **Governing Files:** `GOAL.md`, `TODO.md`, [`research/wayfinder/prompts/agent_3_theory_and_defense.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/wayfinder/prompts/agent_3_theory_and_defense.md)
* **Source Assets:**
  - Supervisor Transcript: [`research/notes/meetings/2026-10-23_supervisor_meeting.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/notes/meetings/2026-10-23_supervisor_meeting.md)
  - Theoretical Conventions: AAPM `conventions.md` & `resources.md`
* **Active Tickets:**
  - [ ] **T3.1: Dimensionless Number Scaling** (`wayfinder:task`) — *Evaluate $Pe_{m,ax}, Pe_p, Da_I, Da_{II}, Bi_m, \Phi$ across the lab operating window.*
  - [ ] **T3.2: Danckwerts Boundary Condition Proof** (`wayfinder:task`) — *Derive flux continuity at $z=0$; prove why Dirichlet conditions violate mass conservation during transients.*
  - [ ] **T3.3: 25-Question Defense Bank** (`wayfinder:task`) — *Author 25 questions with explicit "Supervisor Traps" and rigorous "Model Answers" across 5 themes.*
  - [ ] **T3.4: Personal Mind Map Alignment** (`wayfinder:task`) — *Draft non-destructive alignment proposals in `research/notes/theory_alignment/` using `bep-map-edit-review`.*
* **Primary Theory Deliverable:** `research/notes/theory_alignment/mathematical_formulation_and_defense_prep.md`.

### Island 4: Victor Larsen (2024) PdAg Experimental Curve Replication
* **Branch:** [`feat/larsen-pdag-benchmark`](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/larsen-pdag-benchmark)
* **Governing Files:** `GOAL.md`, `TODO.md`, [`research/wayfinder/prompts/agent_4_larsen_pdag_benchmark.md`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/wayfinder/prompts/agent_4_larsen_pdag_benchmark.md)
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

## 4. The Fog of War (Downstream Slices)
- *Island 5: Synthesis of Larsen PdAg kinetics with Schbib CO periodic modulation.*
- *Island 6: Frequency optimization and asymmetric duty-cycle tuning ($t_{\text{pulse}} \ll t_{\text{purge}}$).*
- *Long-horizon industrial deactivation and multi-bed adiabatic cascades (excluded to focus on microkinetics and dynamic modulation).*

---

## 5. Out of Scope
- Frontend UI dashboards, web applications, or ELK visualizers.
- Blind parameter fitting without primary literature grounding.
- Direct mutations to the owner's personal mind map without explicit authorization.

