# Subgoals & Gate Receipts — Bimetallic PdAg + CO Kinetic Synthesis

## 01 — Kinetic Parameter Crosswalk & Grounding
- [ ] Ingest Larsen (2024) Figure 6.6 & Appendix A 8-parameter kinetic vectors for $\text{Pd}_1\text{Ag}_0$, $\text{Pd}_2\text{Ag}_1$, and $\text{Pd}_3\text{Ag}_1$.
- [ ] Ingest Schbib et al. (1996) Table 8 competitive $CO$ chemisorption constants ($K_{0,\text{CO}} = 13.6\ \text{m}^3/\text{kmol}$, $E_{\text{ads}} = 41.63\ \text{kJ/mol}$).
- [ ] Verify unit consistency across rate equations and gas laws ($P$ in $\text{bar}/\text{atm}$ vs. $C$ in $\text{kmol/m}^3$).

## 02 — Steady-State Co-Feed Benchmark & Synergy Analysis
- [ ] In `notebooks/benchmarks/pdag_co_synthesis.ipynb`, implement the steady-state PFR balance using the Legacy Reactor Format (`ModelParams`, `calculate_rates`, `reactor_ode_rhs`, SciPy BDF solver).
- [ ] Sweep $CO$ concentration from $0$ to $1500\ \text{ppm}$ at constant temperature and space-time across all 3 catalyst alloy formulations.
- [ ] Evaluate the synergy hypothesis: quantify how much Ag alloying lowers the required $CO$ ppm threshold to suppress ethylene over-hydrogenation.

## 03 — Dynamic Inlet Modulation Implementation
- [ ] Implement Method of Lines (MOL) 1D dynamic continuum balance for gas accumulation ($\varepsilon_b \frac{\partial C_i}{\partial t} \neq 0$).
- [ ] Program inlet square-wave periodic $CO$ forcing:
  $$P_{\text{CO}}(t) = P_{\text{CO},\text{mean}} + \Delta P_{\text{CO}} \cdot \text{sgn}\left(\sin\left(\frac{2\pi t}{\tau}\right)\right)$$
- [ ] Simulate transient dynamic response across modulation periods $\tau \in [1\ \text{s}, 60\ \text{s}]$ and duty cycles $D \in [0.1, 0.9]$.

## 04 — Dynamic Pareto Frontier Evaluation
- [ ] Compute time-averaged conversion $\langle X_{\text{C}_2\text{H}_2} \rangle$ and selectivity $\langle S_{\text{C}_2\text{H}_4} \rangle$ once limit-cycle dynamic steady state is established.
- [ ] Plot the static co-feed Pareto frontier vs. the dynamic modulation Pareto frontier.
- [ ] Confirm whether dynamic $CO$ forcing breaks the static ceiling on $\text{PdAg}$.

## 05 — Gate Receipt & Notebook Verification
- [ ] Execute `notebooks/benchmarks/pdag_co_synthesis.ipynb` end-to-end in the global conda base environment.
- [ ] Verify zero runtime errors and total execution time under 90 seconds.
- [ ] Commit and push changes to `feat/pdag-co-synthesis`.
