# Independent Adversarial Audit: BEP Catalysis Modeling Views & Mathematical Formulations

**Mission:** You are an independent, highly critical senior researcher in Chemical Reaction Engineering and Numerical Analysis. Your mandate is to conduct a rigorous, adversarial scientific audit of the modeling hypotheses, kinetic rate laws, parameter interpretations, and numerical schemes established for the TU Delft Bachelor End Project (BEP) on acetylene semi-hydrogenation ($C_2H_2 + H_2 \rightarrow C_2H_4 \rightarrow C_2H_6$) over bimetallic PdAg catalysts with periodic Carbon Monoxide ($CO$) inlet modulation.

**Auditing Standard:**
- **Zero Hallucination / Grounded Claims (Rules 16 & 41):** Do not accept any kinetic rate law, constant, unit, or boundary condition without verifying it against primary source equations or physical first principles.
- **No Confirmation Bias:** Actively search for physical inconsistencies, parameter identifiability issues, solver stiffness traps, unit mismatches, and boundary condition violations.

---

## Pillar 1: Victor Larsen (2024) Bimetallic PdAg Kinetics

### The Established View
1. **Source Context:** Larsen (2024) measured acetylene semi-hydrogenation over eggshell catalysts in an isothermal fixed-bed reactor at $P \approx 1\text{ bar}$, $T = 80\text{--}100\ ^\circ\text{C}$ across three compositions: $\text{Pd}_1\text{Ag}_0$, $\text{Pd}_2\text{Ag}_1$, and $\text{Pd}_3\text{Ag}_1$.
2. **Kinetics Formulation (Eqs. 6.9–6.11):**
   - Acetylene hydrogenation:
     $$r_1 = \frac{r_{1,\max} \cdot r_{1,\text{raw}}}{r_{1,\max} + r_{1,\text{raw}}}, \quad r_{1,\text{raw}} = \frac{k_1 P_A P_H}{(1 + K_A P_A + K_E P_E + \sqrt{K_H P_H})^2}$$
   - Ethylene over-hydrogenation to ethane:
     $$r_2 = \frac{k_2 P_E P_H}{(1 + K_{E2} P_E + \sqrt{K_{H2} P_H}) \cdot (1 + K_{\text{inh}} P_A)^{n_{\text{inh}}}}$$
3. **Physical Interpretation:**
   - Ag dilution physically isolates contiguous Pd ensembles (ensemble effect), suppressing ethylene multi-point adsorption while acetylene (smaller ensemble) remains active.
   - Charge transfer lowers the Pd d-band center (electronic effect), weakening ethylene adsorption and promoting rapid desorption before over-hydrogenation.

### Your Audit Tasks
- [ ] **Equation Verification:** In Larsen's thesis text (PDF p. 43, printed p. 37), does Eq. 6.11 have a first-power or squared adsorption term? Reconcile the discrepancy between printed Eq. 6.11 and the code in Appendix F (PDF p. 86).
- [ ] **Parameter Identifiability & Extrapolation:** Examine the 8 fitted parameter vectors in Figure 6.6. Are all 8 parameters well-conditioned, or is there strong cross-correlation between $r_{1,\max}$ and $k_1$? Can these parameters be extrapolated beyond Larsen's narrow range of $80\text{--}100\ ^\circ\text{C}$?
- [ ] **Data Completeness:** Confirm that Larsen's experiments contain zero $CO$ co-feed data and establish the exact bounds of applicability.

---

## Pillar 2: Schbib et al. (1996) Model III vs. Isothermal PFR Gap

### The Established View
1. **The Discrepancy:** In Schbib et al. (1996) Table 8, evaluating the published rate constants at $150\text{ ppm } CO$ and $16.3\text{ bar}$ yields:
   $$K_{CO} = 10^{13.6} \exp\left(-\frac{9950\text{ cal/mol}}{R T}\right) \approx 1.67 \times 10^7\ \text{m}^3/\text{kmol}$$
   $$K_{CO} C_{CO} \approx 1460 \implies \left[1 + K_H C_H^{1/2} + K_{CO} C_{CO}\right]^3 \approx 3.1 \times 10^9$$
   Plugging this directly into an isothermal 1D PFR yields an acetylene conversion of only $\approx 0.85\%$ (versus the measured $98.31\%$).
2. **Root Cause:** Schbib's parameters were fitted in a 2D non-isothermal pellet/bed model (**Model III**) where severe intra-particle concentration and temperature gradients offset the denominator. Consequently, Table 8 parameters cannot be transferred into an isothermal plug-flow reactor without severe under-prediction.
3. **Author-Shared Correction:** A public author-shared correction matches $C_2H_2$ conversion within $1.48$ percentage points, but produces unphysical net disappearance of ethylene ($C_2H_4$) under isothermal conditions.

### Your Audit Tasks
- [ ] **Quantitative Verification:** Verify the numerical evaluation of Schbib Table 8 at $T = 328.15\text{ K}$, $P = 16.3\text{ bar}$, $150\text{ ppm } CO$. Does the rate denominator indeed exceed $10^9$?
- [ ] **Industrial Precedent Check:** Inspect Gobbo et al. (2004) Table 2. Did Gobbo shift the pre-exponential factors down by 3.5 log units when converting units to SI, and did this act as an empirical workaround for the Model III denominator scaling?
- [ ] **Ethylene Extent Check:** Verify why the author-shared correction fails on ethylene selectivity. Does it over-predict reaction 2 or force negative net ethylene generation?

---

## Pillar 3: Mathematical Modeling & Transport Scaling (V4 Engine)

### The Established View
1. **Governing Continuum Balance:**
   $$\varepsilon_b \frac{\partial C_i}{\partial t} = - u_s \frac{\partial C_i}{\partial z} + D_{ax} \frac{\partial^2 C_i}{\partial z^2} + \rho_b \sum_j \nu_{ij} r_j$$
2. **Dimensionless Regime:** Axial mass Péclet number $Pe_{m,ax} = \frac{u_s L}{D_{ax}} \approx 17\text{--}400 \gg 1$.
   - Convection dominates strongly over axial dispersion.
   - In the hyperbolic limit ($D_{ax} \to 0$), upwind spatial discretization ($N_z$ nodes) maintains total mass conservation and avoids numerical oscillations.
3. **Boundary Conditions:**
   - Inlet: Danckwerts total-flux continuity $-D_{ax} \left.\frac{\partial C_i}{\partial z}\right|_{0^+} = u_s \left(C_{i,\text{in}}(t) - C_i(0^+, t)\right)$ simplifies to Dirichlet $C_i(0, t) = C_{i,\text{in}}(t)$ in the convective limit.
   - Outlet: Zero dispersive flux $\left.\frac{\partial C_i}{\partial z}\right|_L = 0$.
4. **ODE Integration:** The resulting $N_z \times 5$ system is stiff and integrated using SciPy `solve_ivp(method='BDF')`.

### Your Audit Tasks
- [ ] **Numerical Dispersion vs. Physical Dispersion:** With $N_z = 50\text{--}100$ grid points, evaluate the artificial numerical dispersion $D_{\text{num}} = \frac{u_s \Delta z}{2}$. Does numerical dispersion exceed the physical axial dispersion coefficient $D_{ax}$?
- [ ] **Conservation During Transients:** Does the upwind discretization strictly conserve carbon and hydrogen atoms across the spatial grid when the inlet undergoes sharp square-wave jumps ($\Delta C_{CO} \operatorname{sgn}(\sin(2\pi t / \tau))$)?
- [ ] **PSSA Assessment:** Confirm that gas accumulation $\varepsilon_b \frac{\partial C_i}{\partial t}$ is actively integrated, and verify whether surface coverage relaxation ($\partial \theta_k / \partial t$) must also be dynamically integrated or if pseudo-steady-state surface coverage ($\partial \theta / \partial t \approx 0$) is physically defensible at low residence times.

---

## Pillar 4: Bimetallic PdAg + CO Dynamic Synthesis

### The Established View
1. **Synthesis Hypothesis:** Larsen's validated PdAg bimetallic rate equations are expanded by incorporating a competitive Langmuir-Hinshelwood Carbon Monoxide adsorption term into the denominator:
   $$\text{Den} = 1 + K_A P_A + K_E P_E + \sqrt{K_H P_H} + K_{CO} P_{CO}$$
2. **Dynamic Mechanism:** Periodic square-wave modulation of inlet $CO$ modulates surface coverage $\theta_{CO}(z, t)$, creating dynamic traveling waves that periodically suppress over-hydrogenation while purging to restore high acetylene conversion, thereby breaking the static Pareto trade-off.

### Your Audit Tasks
- [ ] **Alloy Adsorption Transferability:** Is it physically defensible to take an equilibrium constant $K_{CO}$ measured on pure $\text{Pd}/\text{Al}_2\text{O}_3$ and apply it to a $\text{PdAg}$ alloy? Since Silver lowers the Pd d-band center, does $K_{CO}$ weaken on $\text{Pd}_2\text{Ag}_1$ compared to pure $\text{Pd}$? How sensitive is the dynamic Pareto frontier to variations in $K_{CO}$?
- [ ] **Phase Lag and Damping:** At superficial gas velocities corresponding to bed residence times $\tau_{\text{res}} \sim 0.1\text{--}2\text{ s}$, does the traveling $CO$ concentration wave retain sharp square-wave features, or does the adsorption-desorption capacitance of the bed smooth the wave into a sinusoidal profile?
- [ ] **Pareto Frontier Verification:** What specific quantitative criterion must be met to claim that periodic operation "breaks the steady-state Pareto ceiling"?

---

## Deliverable
Deliver your audit findings as a structured markdown report covering:
1. **Validated Strengths:** What parts of the formulations are mathematically and physically sound.
2. **Deficiencies & Traps:** Specific risks, unit mismatches, or unverified assumptions.
3. **Actionable Recommendations:** Exact modifications needed before presenting this simulation suite to supervisor Damian Vico van Berkel.
