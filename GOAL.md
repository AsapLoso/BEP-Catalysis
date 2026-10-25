# Agent 5 Dispatch: Bimetallic PdAg Kinetics with Competitive CO Adsorption & Dynamic Inlet Modulation

**Assigned Branch:** `feat/pdag-co-synthesis`  
**Parent Commit:** `unified-reactor-model`  
**Primary Deliverable:** `notebooks/benchmarks/pdag_co_synthesis.ipynb`

---

## 1. Context & Research Significance
This island represents the central research novelty of the Bachelor End Project (BEP) at TU Delft, directly addressing the core research question established with supervisor Damian (2026-10-23):
> *"Victor Larsen (June 2024) hit the static conversion-selectivity trade-off ceiling on bimetallic PdAg catalysts without CO. Hydrogen modulation alone cannot beat steady-state kinetics. To shatter the static ceiling, you must synthesize Larsen's bimetallic site kinetics with competitive Carbon Monoxide (CO) adsorption and evaluate periodic inlet forcing."*

You are tasked with unifying:
1. **Larsen (2024) Bimetallic $\text{PdAg}$ Kinetics:** Alloy site-isolation effects across $\text{Pd}_1\text{Ag}_0$, $\text{Pd}_2\text{Ag}_1$, and $\text{Pd}_3\text{Ag}_1$.
2. **Schbib et al. (1996) CO Inhibition Kinetics:** Competitive chemisorption denominator term ($K_{\text{CO}} P_{\text{CO}}$) that selectively suppresses ethylene over-hydrogenation.
3. **Dynamic Inlet Modulation Engine:** Method of Lines (MOL) 1D reactor with periodic square-wave $CO$ dosing to evaluate whether dynamic forcing breaks the static Pareto frontier.

---

## 2. Primary Ground Truth Sources
All kinetic constants and parameters must be sourced directly from repository primary files:
- **Larsen (2024) Master Thesis:**
  - PDF: [`research/literature/larsen_2024_master_thesis.pdf`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/larsen_2024_master_thesis.pdf)
  - Extracted Text: [`research/literature/larsen_2024_extracted_text.txt`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/larsen_2024_extracted_text.txt)
  - Figure 6.6 & Appendix A: 8-parameter kinetic vectors for $\text{Pd}_1\text{Ag}_0$, $\text{Pd}_2\text{Ag}_1$, and $\text{Pd}_3\text{Ag}_1$.
  - 18 High-Resolution Rendered Pages: `scratch/larsen_appendices/`
- **Schbib et al. (1996) Industrial & Engineering Chemistry Research:**
  - Lossless HTML: [`research/literature/schbib_1996_full_article.html`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_full_article.html)
  - Extracted Text: [`research/literature/schbib_1996_extracted_text.txt`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_extracted_text.txt)
  - Table 8: $K_{\text{CO}}$ adsorption pre-exponential ($\log A = 13.6\ \text{m}^3/\text{kmol}$) and heat of adsorption ($E = 41.63\ \text{kJ/mol}$).

---

## 3. Kinetic Synthesis Formulation

### 3.1 Coupled Langmuir-Hinshelwood Rate Laws
For catalyst alloy $m \in \{\text{Pd}_1\text{Ag}_0, \text{Pd}_2\text{Ag}_1, \text{Pd}_3\text{Ag}_1\}$:

$$r_1 = \frac{k_{1,m}(T) \, K_{A,m}(T) P_A \, K_{H,m}(T) P_H^{0.5}}{\left(1 + K_{A,m} P_A + K_{E,m} P_E + K_{H,m} P_H^{0.5} + \mathbf{K_{\text{CO}}(T) P_{\text{CO}}}\right)^{n_{\text{inh},m}}}$$

$$r_2 = \frac{k_{2,m}(T) \, K_{E,m}(T) P_E \, K_{H,m}(T) P_H^{0.5}}{\left(1 + K_{A,m} P_A + K_{E,m} P_E + K_{H,m} P_H^{0.5} + \mathbf{K_{\text{CO}}(T) P_{\text{CO}}}\right)^{n_{\text{inh},m}}}$$

Where:
- $P_A, P_E, P_H, P_{\text{CO}}$ are partial pressures of acetylene, ethylene, hydrogen, and carbon monoxide.
- $k_{1,m}, k_{2,m}$ are Larsen's rate constants.
- $n_{\text{inh},m}$ is the site-inhibition exponent from Larsen (2024).
- $K_{\text{CO}}(T) = K_{0,\text{CO}} \exp\left(\frac{-\Delta H_{\text{ads},\text{CO}}}{R T}\right)$ is Schbib's competitive chemisorption equilibrium constant.

### 3.2 1D Dynamic Reactor Balance Equations (Legacy Reactor Format)
The gas phase balances along axial coordinate $z$ (or catalyst mass $W$):
$$\varepsilon_b \frac{\partial C_i}{\partial t} = - \frac{\partial (u_z C_i)}{\partial z} + (1 - \varepsilon_b)\rho_s \sum_j \nu_{i,j} r_j$$
$$\left[\varepsilon_b \rho c_p + (1 - \varepsilon_b)\rho_s c_{p,s}\right] \frac{\partial T}{\partial t} = - u_z \rho c_p \frac{\partial T}{\partial z} + (1 - \varepsilon_b)\rho_s \sum_j (-\Delta H_{r,j}) r_j - \frac{4 U}{d_t}(T - T_{\text{wall}})$$

---

## 4. Specific Reproduction & Exploration Targets
In `notebooks/benchmarks/pdag_co_synthesis.ipynb`:
1. **Steady-State Co-Feed Benchmark:**
   - Simulate conversion $X_{C_2H_2}$ and selectivity $S_{C_2H_4}$ vs. $CO$ inlet concentration ($0\text{--}1500\ \text{ppm}$) across all 3 catalyst formulations ($\text{Pd}_1\text{Ag}_0, \text{Pd}_2\text{Ag}_1, \text{Pd}_3\text{Ag}_1$).
   - Determine whether the bimetallic Ag site-isolation reduces the required $CO$ dosage to achieve $>95\%$ selectivity.
2. **Periodic Dynamic Inlet Modulation:**
   - Implement square-wave periodic $CO$ forcing at the reactor inlet:
     $$P_{\text{CO}}(t) = P_{\text{CO},\text{mean}} + \Delta P_{\text{CO}} \cdot \text{sgn}\left(\sin\left(\frac{2\pi t}{\tau}\right)\right)$$
   - Vary cycling period $\tau \in [1\ \text{s}, 60\ \text{s}]$ and duty cycle $D \in [0.1, 0.9]$.
3. **Dynamic Pareto Frontier Evaluation:**
   - Construct the Pareto curve: Selectivity vs. Conversion.
   - Overlay the steady-state co-feed frontier against the dynamic modulation frontier to definitively verify if dynamic forcing breaks the static ceiling.

---

## 5. Execution & Verification Rules
- Follow the **Legacy Reactor Format**: self-contained notebook, transparent dataclass `ModelParams`, vector rates, direct `scipy.integrate.solve_ivp(method='BDF')`.
- Strictly adhere to **Rule 19**: Run in global conda base Python environment; no multi-line inline scripts.
- Ensure the notebook executes cleanly end-to-end with zero errors in under 90 seconds.

**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` tracks gate receipts.
