# Agent 2 Dispatch: Dynamic 1D V4 Coupled Reactor Engine (True Transient ODE Integration)

**Assigned Branch:** `feat/v4-dynamic-reactor`  
**Parent Commit:** `unified-reactor-model`  
**Primary Deliverable:** `notebooks/v4/unified_v4_dynamic_reactor.ipynb`

---

## 1. Context & The Core V4 Scientific Upgrade
You are tasked with implementing the **V4 Dynamic Coupled Reactor Model** for acetylene semi-hydrogenation with periodic Carbon Monoxide ($CO$) inlet modulation.

### Why V3 Was Flawed & What Makes This V4:
1. **The PSSA Fallacy:** V3 relied on a Pseudo-Steady-State Approximation (PSSA / QSSA), assuming the gas phase and surface coverages adapt instantaneously ($\partial C / \partial t = 0$, $\partial \theta / \partial t = 0$). PSSA is by definition **not transient**—it destroys the physical wave propagation and phase lag essential to dynamic catalysis.
2. **True Transient ODE Integration:** V4 strictly retains the full time-accumulation terms:
   $$\varepsilon_b \frac{\partial C_{b,i}}{\partial t} \neq 0, \quad \varepsilon_p \frac{\partial c_{p,i}}{\partial t} \neq 0, \quad \frac{\partial \theta_j}{\partial t} \neq 0$$
   Spatial discretization via the Method of Lines (MOL) yields a stiff system of coupled ordinary differential equations (ODEs):
   $$\frac{d \mathbf{y}}{d t} = \mathbf{F}(t, \mathbf{y})$$
   which is integrated forward in time using a proven stiff ODE solver (`scipy.integrate.solve_ivp` with `method='BDF'` or `'Radau'`).
3. **Competitive CO Adsorption Kinetics:** Unlike V3 (which used CO-free Urmès kinetics), V4 incorporates the verified Langmuir-Hinshelwood rate laws from Schbib et al. (1996) where trace $CO$ competitively blocks active sites and suppresses over-hydrogenation.

---

## 2. Mathematical Formulation

### 1D Dynamic Axial Dispersion Equations (MOL Spatial Discretization):
For each gas component $i \in \{C_2H_2, C_2H_4, C_2H_6, H_2, CO\}$:
$$\varepsilon_b \frac{\partial C_{b,i}}{\partial t} = D_{ax,i} \frac{\partial^2 C_{b,i}}{\partial z^2} - u_s \frac{\partial C_{b,i}}{\partial z} - \frac{1 - \varepsilon_b}{\varepsilon_b} k_g a_v \left(C_{b,i} - c_{p,i}|_{r=R_p}\right)$$

### Intra-Particle Radial Diffusion & Reaction:
$$\varepsilon_p \frac{\partial c_{p,i}}{\partial t} = \frac{D_{e,i}}{r^2} \frac{\partial}{\partial r}\left(r^2 \frac{\partial c_{p,i}}{\partial r}\right) + \rho_s \sum_j \nu_{i,j} r_j(c_p, T)$$

*(Note: In the well-mixed pellet limit, the intra-pellet radial profile collapses to an effective volume-averaged reaction source term directly in the ODE).*

### Langmuir-Hinshelwood Kinetics with Competitive CO Adsorption:
$$r_1 = \frac{k_1 \, c_{C_2H_2} \, c_{H_2}}{\left[1 + K_H c_{H_2}^{1/2} + K_{CO} c_{CO}\right]^3}$$
$$r_2 = \frac{k_2 \, c_{C_2H_4} \, c_{H_2}}{\left[1 + K_H c_{H_2}^{1/2} + K_{CO} c_{CO}\right]^3}$$
Using Arrhenius and adsorption parameters from Schbib (1996) / Gobbo (2004) Table 1.

### Danckwerts Transient Inlet Boundary Condition:
At $z = 0$:
$$u_s C_{b,i}(0, t) - D_{ax,i} \left.\frac{\partial C_{b,i}}{\partial z}\right|_{z=0} = u_s \, C_{i,\text{in}}(t)$$
Where $C_{CO,\text{in}}(t)$ is periodically modulated:
$$C_{CO,\text{in}}(t) = C_{CO,\text{mean}} + \Delta C_{CO} \operatorname{sgn}\left(\sin\left(\frac{2\pi t}{\tau_p}\right)\right)$$

---

## 3. Implementation Plan
1. **Engine Foundation:** Adapt the vendored solver in `notebooks/v3/vendor/pbr/` to:
   - Ensure the gas-phase accumulation term is active (no PSSA shortcuts).
   - Add Carbon Monoxide ($CO$) as an active species in `pbr.chemistry`.
   - Implement the Schbib rate laws with $K_{CO}$.
2. **Stiff ODE Integration:** Run `solve_ivp(self.rhs, t_span, y0, method='BDF', atol=1e-10, rtol=1e-7)`.
3. **Execution Runtime:** Keep the notebook simulation runtime under **3 minutes** on a standard CPU.

---

## 4. Deliverable
A clean, self-contained, executed Jupyter Notebook:
`notebooks/v4/unified_v4_dynamic_reactor.ipynb`
Displaying:
- Dynamic concentration waves traveling along the reactor length over time ($z, t$).
- Limit cycle phase plane ($X(t)$ vs. $S(t)$).
- Time-averaged Pareto improvement of periodic $CO$ modulation over steady-state operation.


**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts.