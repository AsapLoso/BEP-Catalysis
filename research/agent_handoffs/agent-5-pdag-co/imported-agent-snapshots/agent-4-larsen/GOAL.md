# Agent 4 Dispatch: Experimental Reproduction Benchmark (Larsen 2024 PdAg)

**Assigned Branch:** `feat/larsen-pdag-benchmark`  
**Parent Commit:** `unified-reactor-model`  
**Primary Deliverable:** `notebooks/benchmarks/larsen_2024_benchmark.ipynb`

**Status:** COMPLETED (2026-10-25), with the raw-data limitation documented. The notebook reproduces selected published curves and records the thesis RMSE values; the thesis does not provide the full Pd₂Ag/Pd₃Ag response tables needed for an independent all-experiment RMSE calculation.

---

## 1. Context & Objectives
You are tasked with reproducing the experimental conversion and selectivity results from Victor Larsen’s Bachelor End Project thesis:
* **Title:** *Semihydrogenation of acetylene to ethylene with a PdAg catalyst* (TU Delft, Catalysis Engineering Group, June 2024).
* **Supervisors:** Ir. Damian Vico van Berkel & Prof. Atsushi Urakawa.
* **Primary Source:** Larsen's 97-page June 2024 thesis PDF in the project management archive.

Larsen investigated static steady-state acetylene hydrogenation over $\text{Pd}_0\text{Ag}$, $\text{Pd}_2\text{Ag}$, and $\text{Pd}_3\text{Ag}$ at $100\ ^\circ\text{C}$ and $1\ \text{bar}$. Table 6.1 reports catalyst masses of 100, 75, and 100 mg, respectively.

---

## 2. Ground-Truth Warning & Known Extraction Pitfalls
**CRITICAL: Do not fall into known extraction traps recorded in `conventions.md` §12!**

1. **Scanned Raster Appendices (No Text Layer):**
   Appendix E and F pages are raster screenshots and need high-resolution visual inspection. Tables E.1–E.3 compare standard LHHW model variants; they are not the final fitted-parameter vectors. Appendix F contains standard-model code, Differential Evolution bounds, reactor inputs, and a 41-row Pd₀Ag experiment/comparison table. The complete eight-parameter vectors used for the final model are printed above the parity plots in Figure 6.6 (printed p. 38).
2. **Incomplete Parameter Sets:**
   Previous runs circulated an incomplete 6-parameter set (`k1`, `k2`, `K_C2H2`, `K_C2H4`, `K_inh`, `K_H2`). This set was missing $r_{1,\max}$ and the fitted non-integer exponent $n_{\text{inh}}$. Without these, Larsen's final rate law (Eqs. 6.9–6.11) cannot be evaluated.
3. **Reactor Normalization and Conditions:**
   Appendix F gives a 0.5 cm tube diameter and a support density of 2.65 g cm⁻³; bed length follows from these and the catalyst mass. Table 6.1 gives catalyst-specific masses. The experimental feeds use H₂, C₂H₂, C₂H₄, and He; CO was not studied.
4. **Experimental versus Simulated Plots:**
   Experimental curves for the three catalysts are in Figures 6.1–6.4 and Appendix A. Appendices B–D contain simulated curves. Appendix F prints the Pd₀Ag experiment and comparison tables; the full raw response tables for Pd₂Ag and Pd₃Ag are not present in the thesis, so their plotted responses must be digitized and labelled as estimates.

---

## 3. Required Methodology & Verification Steps

### Step 1: Render and Inspect Appendix Pages 71–88
Using Python (`fitz` / PyMuPDF or `pdf2image`):
1. Render Appendix E and F pages to 300 DPI PNG images in a scratch directory and inspect them visually.
2. Record the Appendix E standard-model comparisons separately from the final parameter vectors in Figure 6.6. Extract all eight final parameters for each catalyst, including $r_{1,\max}$ and $n_{\text{inh}}$.
3. Recover the Appendix F tube diameter and support density, then combine them with catalyst-specific masses and experimental flows to derive bed length and inlet conditions.

### Step 2: Extract Experimental Curves from Figures 6.1–6.4
1. Extract selected experimental responses from Figures 6.1–6.4, using exact Appendix F values for Pd₀Ag where available and visual digitization for Pd₂Ag/Pd₃Ag.
2. Keep exact table transcription and estimated chart coordinates distinguishable in the CSV provenance columns. Do not use simulated Appendix B–D curves as measured data.

### Step 3: Implement the 1D Differential Reactor ODE Model
Implement Larsen's molar balance ODEs (Eqs. 4.6–4.9):
Integrate the balances with `scipy.integrate.solve_ivp(method="BDF")` across the selected experimental conditions.
$$\frac{d F_i}{d z} = A \, \rho_{\text{support}} \, \sum_j \nu_{i,j} \, r_j$$
With Extended LHHW rate laws (Eqs. 6.9–6.11):
$$r_{1,\mathrm{raw}} = \frac{k_1 K_{\text{C}_2\text{H}_2} p_{\text{C}_2\text{H}_2} K_{\text{H}_2} p_{\text{H}_2}}{\left(1 + K_{\text{C}_2\text{H}_2} p_{\text{C}_2\text{H}_2} + K_{\text{C}_2\text{H}_4} p_{\text{C}_2\text{H}_4} + K_{\text{H}_2} p_{\text{H}_2}\right)^2},\qquad r_1=\frac{r_{1,\mathrm{raw}}}{1+r_{1,\mathrm{raw}}/r_{1,\max}}$$
$$r_2 = \frac{k_2 K_{\text{C}_2\text{H}_4} p_{\text{C}_2\text{H}_4} K_{\text{H}_2} p_{\text{H}_2}}{\left(1 + K_{\text{C}_2\text{H}_2} p_{\text{C}_2\text{H}_2} + K_{\text{C}_2\text{H}_4} p_{\text{C}_2\text{H}_4}\right)^2 \left(1 + K_{\text{inh}} p_{\text{C}_2\text{H}_2}\right)^{n_{\text{inh}}}}$$

### Step 4: Validate RMSE against Larsen's Reported Benchmarks
For each experiment, compute $e_k=\sqrt{((X_{\mathrm{sim},k}-X_{\mathrm{exp},k})^2+(S_{\mathrm{sim},k}-S_{\mathrm{exp},k})^2)/2}$ and average $e_k$ over the available selected points. Report this selected-curve error separately from Larsen's published all-experiment metric. The published metric uses 41/42/41 experiments and cannot be independently recalculated for Pd₂Ag/Pd₃Ag because their full raw response tables are absent.
Report Larsen's published values:
- $\text{Pd}_0\text{Ag}$: $\approx 5.10\ \text{percentage points}$
- $\text{Pd}_2\text{Ag}$: $\approx 5.43\ \text{percentage points}$
- $\text{Pd}_3\text{Ag}$: $\approx 7.14\ \text{percentage points}$

---

## 4. Deliverable
A clean, self-contained, and fully executed Jupyter notebook:
`notebooks/benchmarks/larsen_2024_benchmark.ipynb`
with side-by-side plots reproducing Larsen's Conversion & Selectivity curves and explicit error metrics.


**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts. The source corrections above replace the inaccurate initial descriptions of the parameter tables, experimental figures, and reactor conditions.
