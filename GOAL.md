# Agent 3 Dispatch: Theory Alignment, Transport Rigor & Defense Preparation

**Assigned Branch:** `feat/personal-map-alignment`  
**Parent Commit:** `unified-reactor-model`  
**Primary Deliverable:** `research/notes/theory_alignment/mathematical_formulation_and_defense_prep.md`

---

## 1. Context & Objectives
You are tasked with securing the mathematical and transport phenomena foundations of the Bachelor End Project (BEP) and preparing the author for a flawless oral thesis defense before Ir. Damian Vico van Berkel and Prof. Atsushi Urakawa.

In catalysis engineering, dynamic packed-bed modeling fails defense reviews when authors cannot rigorously justify their continuum assumptions, boundary conditions, or non-dimensional scaling regimes.

---

## 2. Core Theoretical Tasks

### A. Non-Dimensional Transport Scaling & Regime Verification
Derive and evaluate the dimensionless criteria across the laboratory packed-bed operating window ($L = 0.05\text{--}0.2\ \text{m}$, $d_p = 1\text{--}3\ \text{mm}$, $u = 0.01\text{--}0.1\ \text{m/s}$):
1. **Péclet Numbers (Mass and Thermal):**
   $$Pe_{m,ax} = \frac{u \, L}{D_{ax}}, \quad Pe_{p} = \frac{u \, d_p}{D_{ax}}$$
   Evaluate the validity of axial dispersion neglect vs. retention, referencing Danckwerts (1953) and Bischoff & Levenspiel.
2. **Damköhler Numbers:**
   $$Da_I = \frac{\text{reaction rate}}{\text{bulk convective rate}} = \frac{k \, \rho_b \, L}{u}$$
   $$Da_{II} = \frac{\text{reaction rate}}{\text{interphase mass transfer rate}} = \frac{k \, \rho_b \, d_p}{k_g \, a_v}$$
3. **Biot Numbers & Internal Transport:**
   $$Bi_m = \frac{k_g \, R_p}{D_{\text{eff}}}, \quad \Phi = R_p \sqrt{\frac{k \, \rho_s}{D_{\text{eff}}}}$$
   Evaluate Thiele modulus $\Phi$ and effectiveness factor $\eta$ for the eggshell catalyst pellets ($Pd$ outer shell).

### B. Mathematical Boundary Condition Justification
Formulate the mathematical justification for:
1. **Danckwerts Boundary Conditions:** Why flux-continuity at $z=0$ is strictly required for transient inlet pulsing, and why Dirichlet conditions ($C(0, t) = C_{\text{in}}(t)$) fail mass conservation during steep concentration transients.
2. **Neumann Outflow Condition:** Why $\left.\frac{\partial C}{\partial z}\right|_{z=L} = 0$ is valid when $Pe_{m,ax} \gg 1$.
3. **Method of Lines Discretization:** Order of accuracy ($\mathcal{O}(\Delta z^2)$ centered vs. upwind schemes) and handling of numerical Péclet constraints ($Pe_{\Delta z} = \frac{u \Delta z}{D_{ax}} \le 2$) to avoid spurious numerical oscillations.

---

## 3. Oral Defense Question Bank (25 Questions & Model Answers)
Draft an exhaustive 25-question defense bank organized into 5 thematic clusters:
1. **Reactor Transport & Non-Idealities (5 Qs):** Wall effects, channeling, axial dispersion limits, pressure drop (Ergun).
2. **Kinetics & Surface Adsorption (5 Qs):** Langmuir-Hinshelwood derivation, competitive $CO$ poisoning, why $H_2$ modulation cannot exceed steady state while $CO$ modulation can.
3. **Numerical Analysis & Stiff Solvers (5 Qs):** Stiffness ratio $\lambda_{\max}/\lambda_{\min}$, BDF vs. explicit Runge-Kutta, algebraic constraints, mass matrix conditioning.
4. **Periodic Forcing & Dynamic Catalysis (5 Qs):** Relaxation times $\tau_{\text{ads}} \ll \tau_{\text{res}}$, phase shift between gas and surface coverages $\theta_i$, resonance tuning of period $\tau_p$.
5. **Experimental Feasibility & Validation (5 Qs):** GC sampling response lag vs. mass spec (MS), valve switching dead-volume, thermal inertia of the packed bed.

Each question must include:
- **Supervisor Trap:** What flawed intuition the supervisor is probing for.
- **Model Answer:** Concise, mathematically rigorous explanation using specific equations and physical constants.

---

## 4. Personal Mind Map Alignment (skill: `bep-map-edit-review`)
- Review the personal mind map files in AAPM archive.
- Ensure all proposed changes strictly respect Rule 42 (Trade-offs belong to the user) and the personal map guardrails.
- Retain all personal map proposals in `research/notes/theory_alignment/` without modifying master maps without explicit owner approval.


**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts.