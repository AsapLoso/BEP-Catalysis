# Agent 1 Dispatch: Steady-State Lab Benchmark with CO (Schbib et al. 1996)

**Assigned Branch:** `feat/schbib-co-benchmark`  
**Parent Commit:** `unified-reactor-model`  
**Primary Deliverable:** `notebooks/benchmarks/schbib_1996_steady_state.ipynb`

---

## 1. Context & Objectives
You are tasked with building a rigorous, verified 1D steady-state plug flow reactor (PFR) model reproducing the laboratory benchmark results from **Schbib et al. (1996)** (*Ind. Eng. Chem. Res.* 35(5), 1496–1503). This paper provides the gold standard for acetylene hydrogenation with trace Carbon Monoxide ($CO$) competitive adsorption on a commercial $Pd/\alpha\text{-Al}_2\text{O}_3$ catalyst.

Your model must simulate:
1. Acetylene semi-hydrogenation: $C_2H_2 + H_2 \rightarrow C_2H_4$ ($r_1$)
2. Ethylene over-hydrogenation: $C_2H_4 + H_2 \rightarrow C_2H_6$ ($r_2$)
under varying temperatures ($288\text{--}393\ \text{K}$), pressures ($1\text{--}35\ \text{atm}$), and trace $CO$ concentrations ($0\text{--}5000\ \text{ppm}$).

---

## 2. Primary Ground Truth Sources
Do not guess or hallucinate any parameters. All data must be read directly from the workspace files:
- **Full Machine-Readable HTML:** [`research/literature/schbib_1996_full_article.html`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_full_article.html)
- **Primary PDF:** [`research/literature/schbib_1996_front_end_acetylene_hydrogenation.pdf`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_front_end_acetylene_hydrogenation.pdf)
- **Extracted Text:** [`research/literature/schbib_1996_extracted_text.txt`](file:///c:/Users/Deuts/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/BEP-Catalysis/research/literature/schbib_1996_extracted_text.txt)

### Key Data Tables to Extract from HTML:
- **Table 3 (Feed & Operating Conditions):**
  - Feed: $CH_4 = 6.53\%$, $C_2H_2 = 0.52\%$, $C_2H_4 = 43.99\%$, $C_2H_6 = 26.72\%$, $H_2 = 22.1\%$, $CO = 150\text{--}5000\ \text{ppm}$.
  - Gas flow: $100\ \text{cm}^3\ (\text{STP})/\text{min}$, Catalyst mass: $1\text{--}3\ \text{g}$, $T = 288\text{--}393\ \text{K}$, $P = 1\text{--}35\ \text{atm}$.
- **Table 4 (Catalyst Properties):**
  - Support: $\alpha\text{-Al}_2\text{O}_3$, $Pd = 0.04\ \text{wt}\%$, BET surface area: $21\ \text{m}^2/\text{g}$, Apparent density: $1.61\ \text{g/cm}^3$, Porosity: $54.5\%$.
- **Table 6 (CO Inhibition Benchmark Data):**
  - $150\ \text{ppm}\ CO$ at $341\ \text{K}$: $X_{C_2H_2} = 98.31\%$, $X_{C_2H_4} = 10.45\%$
  - $1400\ \text{ppm}\ CO$ at $359\ \text{K}$: $X_{C_2H_2} = 98.99\%$, $X_{C_2H_4} = 6.70\%$
  - $5000\ \text{ppm}\ CO$ at $393\ \text{K}$: $X_{C_2H_2} = 98.62\%$, $X_{C_2H_4} = 6.08\%$
- **Table 8 (Kinetic & Adsorption Parameters):**
  $$(-r_j) = \frac{k_j C_j C_H \rho_s (1 - \varepsilon_b)}{\left[1 + K_H C_H^{1/2} + K_{CO} C_{CO}\right]^3}$$
  - $k_A$: $\log A_i = 31.1\ \text{m}^6/(\text{s}\cdot\text{g}_{\text{cat}}\cdot\text{kmol})$, $E = 45.51\ \text{kcal/gmol}$ ($190.42\ \text{kJ/mol}$)
  - $k_E$: $\log A_i = 26.6\ \text{m}^6/(\text{s}\cdot\text{g}_{\text{cat}}\cdot\text{kmol})$, $E = 42.94\ \text{kcal/gmol}$ ($179.66\ \text{kJ/mol}$)
  - $K_H$: $\log A_i = 20.2\ \text{m}^3/\text{kmol}$, $E = 21.22\ \text{kcal/gmol}$ ($88.78\ \text{kJ/mol}$)
  - $K_{CO}$: $\log A_i = 13.6\ \text{m}^3/\text{kmol}$, $E = 9.95\ \text{kcal/gmol}$ ($41.63\ \text{kJ/mol}$)

---

## 3. Mathematical Model Specification
The 1D steady-state plug flow balance equations for species $i \in \{C_2H_2, C_2H_4, C_2H_6, H_2, CO\}$:
$$\frac{d F_i}{d z} = A \, \rho_s (1 - \varepsilon_b) \, \sum_j \nu_{i,j} \, r_j$$
$$\frac{d T}{d z} = \frac{A \, \rho_s (1 - \varepsilon_b) \sum_j (-\Delta H_{r,j}) r_j}{\sum_i F_i C_{p,i}}$$

Where:
- $\nu_{i,j}$ are stoichiometric coefficients:
  - Reaction 1 ($C_2H_2 + H_2 \rightarrow C_2H_4$): $\Delta H_{r,1} = -172\ \text{kJ/mol}$
  - Reaction 2 ($C_2H_4 + H_2 \rightarrow C_2H_6$): $\Delta H_{r,2} = -136\ \text{kJ/mol}$

---

## 4. Specific Reproduction Targets
Your Jupyter notebook must generate:
1. **Conversion vs. Temperature:** Replicate **Figure 1** ($X_{C_2H_2}$ and $X_{C_2H_4}$ vs. $T \in [290, 360]\ \text{K}$).
2. **Reaction Rates vs. Temperature:** Replicate **Figure 2** ($r_1$ and $r_2$ vs. $T$).
3. **Axial Profiles:** Replicate **Figures 3 & 4** showing axial conversion and temperature profiles along the bed, clearly demonstrating how trace $CO$ prevents thermal runaway.
4. **Validation Table:** Print a direct comparison between simulated conversions and the measured values from **Table 6** ($150, 1400, 5000\ \text{ppm}\ CO$).

---

## 5. Execution & Verification Rules
- Use `solve_ivp` with `method='Radau'` or `'BDF'` for stiff ODE integration.
- Strictly adhere to **Rule 19**: Global conda base Python environment, no inline `python -c` scripts.
- Execute the notebook end-to-end to ensure all cells run cleanly with zero errors.
- Ensure the notebook executes in under 60 seconds on a standard laptop.
