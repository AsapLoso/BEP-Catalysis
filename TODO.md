# Subgoals & Gate Receipts — V4 Dynamic 1D Coupled Reactor Engine

## 01 — Chemistry & CO Competitive Adsorption Engine
- [ ] Update `notebooks/v3/vendor/pbr/chemistry.py` to add Carbon Monoxide ($CO$) as an active species.
- [ ] Implement Schbib (1996) Langmuir-Hinshelwood kinetics with cubed denominator term $[1 + K_H C_H^{1/2} + K_{CO} C_{CO}]^3$.

## 02 — True Transient ODE Method of Lines (NO PSSA)
- [ ] Verify that the gas accumulation term $\varepsilon_b \frac{\partial C_{b,i}}{\partial t}$ is strictly active in `pbr/solver.py` (no pseudo-steady-state shortcuts).
- [ ] Discretize space via Method of Lines into a stiff ODE system $\frac{d\mathbf{y}}{dt} = \mathbf{F}(t, \mathbf{y})$.
- [ ] Verify solver convergence to baseline steady-state using `scipy.integrate.solve_ivp(method='BDF')`.

## 03 — Periodic Inlet Modulation Hook
- [ ] Implement Danckwerts boundary conditions at $z = 0$ with time-dependent inlet forcing:
  $C_{CO,\text{in}}(t) = C_{CO,\text{mean}} + \Delta C_{CO} \operatorname{sgn}(\sin(2\pi t / \tau_p))$.
- [ ] Test both square-wave and sinusoidal modulation across periods $\tau_p \in [0.1, 10]\ \text{s}$.

## 04 — Dynamic Wave Propagation & Limit Cycles
- [ ] In `notebooks/v4/unified_v4_dynamic_reactor.ipynb`, plot 2D spatiotemporal heatmaps $C_i(z, t)$ showing concentration waves traveling through the packed bed.
- [ ] Plot limit cycle trajectories in the phase plane: Conversion $X(t)$ vs. Ethylene Selectivity $S(t)$.

## 05 — Gate Receipt (Pareto Enhancement)
- [ ] Calculate cycle-averaged $(\overline{X}, \overline{S})$ and generate a Pareto comparison plot demonstrating that dynamic periodic CO operation shifts performance beyond the static steady-state limit.
- [ ] Notebook executes cleanly in < 3 minutes on CPU.
