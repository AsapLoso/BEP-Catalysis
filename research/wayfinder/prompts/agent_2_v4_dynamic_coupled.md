# Agent 2 Dispatch: Dynamic 1D Coupled Reactor Engine (Periodic CO Modulation)

**Assigned Branch:** `feat/v3-coupled-reactor`  
**Parent Commit:** `unified-reactor-model`  
**Primary Deliverable:** `notebooks/reference/v4/unified_v4_dynamic_reactor.ipynb`

---

## 1. Context & Objectives
You are tasked with implementing the dynamic 1D coupled packed-bed reactor model simulating **periodic inlet modulation of Carbon Monoxide ($CO$)** for acetylene semi-hydrogenation. 

In the 2026-10-23 supervisor meeting, Ir. Damian Vico van Berkel established the central scientific thesis:
> *"Modulating hydrogen, you will never surpass steady state. Just the kinetics don't allow you to... Mostly related on CO... by tuning the concentration of CO on the surface you might be able to tune... poisoning and competitive adsorption... and then you can start trying to explain what your part of the thesis is which is more the mathematics of periodic operation."*

Your mission is to demonstrate numerically that periodic inlet concentration cycling of $CO$ dynamically decouples catalyst activity from ethylene selectivity, shifting the time-averaged trade-off above the static steady-state limit.

---

## 2. Mathematical Continuum Model

### Governing Equations (1D Axial Dispersion Model + Langmuir-Hinshelwood Kinetics):
For each gas species $i \in \{C_2H_2, C_2H_4, C_2H_6, H_2, CO\}$:
$$\varepsilon_b \frac{\partial C_i}{\partial t} = D_{ax,i} \frac{\partial^2 C_i}{\partial z^2} - u \frac{\partial C_i}{\partial z} - \rho_b \, r_i(C, T)$$

Energy balance (Isothermal base case or non-isothermal extension):
$$(\varepsilon_b \rho_g C_{p,g} + (1 - \varepsilon_b) \rho_s C_{p,s}) \frac{\partial T}{\partial t} = \lambda_{ax} \frac{\partial^2 T}{\partial z^2} - u \rho_g C_{p,g} \frac{\partial T}{\partial z} + \rho_b \sum_j (-\Delta H_{r,j}) r_j$$

### Langmuir-Hinshelwood Kinetics with Competitive CO Adsorption:
$$r_1 = \frac{k_1 \, C_{C_2H_2} \, C_{H_2}}{\left[1 + K_H C_{H_2}^{1/2} + K_{CO} C_{CO}\right]^3}$$
$$r_2 = \frac{k_2 \, C_{C_2H_4} \, C_{H_2}}{\left[1 + K_H C_{H_2}^{1/2} + K_{CO} C_{CO}\right]^3}$$

### Danckwerts Transient Boundary Conditions:
At inlet $z = 0$:
$$u C_i(0, t) - D_{ax,i} \left.\frac{\partial C_i}{\partial z}\right|_{z=0} = u \, C_{i,\text{in}}(t)$$
At outlet $z = L$:
$$\left.\frac{\partial C_i}{\partial z}\right|_{z=L} = 0$$

### Periodic Forcing Functions:
At $z = 0$, $C_{CO,\text{in}}(t)$ is periodically modulated:
1. **Square-Wave Modulation:**
   $$C_{CO,\text{in}}(t) = C_{CO,\text{mean}} + \Delta C_{CO} \operatorname{sgn}\left(\sin\left(\frac{2\pi t}{\tau_p}\right)\right)$$
2. **Sinusoidal Modulation:**
   $$C_{CO,\text{in}}(t) = C_{CO,\text{mean}} + \Delta C_{CO} \sin\left(\frac{2\pi t}{\tau_p}\right)$$
Where $\tau_p$ is the modulation period, systematically varied relative to the reactor residence time $\tau_{\text{res}} = L/u$ ($\tau_p / \tau_{\text{res}} \in [0.1, 10]$).

---

## 3. Implementation Assets
- Use the vendored `pbr` engine in [notebooks/reference/v3/vendor/pbr/](../../../notebooks/reference/v3/vendor/pbr/) as the V3 comparison implementation (63/63 tests passed in the recorded V3 verification).
- Consult [Structure.md](../../../Structure.md) for parameter conventions.
- Discretize space via Method of Lines (MOL) on $N_z \in [50, 100]$ interior nodes.
- Integrate time using stiff solvers (`scipy.integrate.solve_ivp` with `method='BDF'` or `'Radau'`).

---

## 4. Required Notebook Figures & Analysis
The notebook `notebooks/reference/v4/unified_v4_dynamic_reactor.ipynb` must produce:
1. **Baseline Validation:** Convergence to steady state under constant $C_{CO,\text{in}}$, matching Agent 1's benchmark.
2. **Spatiotemporal Wave Propagation:** 2D heatmap / carpet plot $C_i(z, t)$ showing concentration waves travelling through the packed bed under periodic square-wave cycling.
3. **Limit Cycle Phase Plane:** Limit cycle trajectories of Conversion $X(t)$ vs. Ethylene Selectivity $S(t)$ over multiple periods.
4. **Time-Averaged Performance Comparison:**
   $$\overline{X} = \frac{1}{\tau_p} \int_0^{\tau_p} X(t) dt, \quad \overline{S} = \frac{1}{\tau_p} \int_0^{\tau_p} S(t) dt$$
   A Pareto plot comparing $(\overline{X}, \overline{S})$ under periodic operation against the static steady-state trade-off curve across varying periods $\tau_p$.

---

## 5. Execution Guardrails
- Total notebook execution runtime must remain under **3 minutes** on standard hardware.
- Use vectorized RHS functions in NumPy to prevent CPU bottlenecks.
- Apply **Rule 19**: Base conda Python, all imports validated.
- Adhere to **Rule 15**: Clear, rigorous scientific explanations; zero marketing fluff.
