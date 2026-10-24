# Agent 4 Dispatch: Experimental Reproduction Benchmark (Larsen 2024 PdAg)

**Assigned Branch:** `feat/larsen-pdag-benchmark`  
**Parent Commit:** `unified-reactor-model`  
**Primary Deliverable:** `notebooks/benchmarks/larsen_2024_benchmark.ipynb`

---

## 1. Context & Objectives
You are tasked with reproducing the experimental conversion and selectivity results from Victor Larsen’s Bachelor End Project thesis:
* **Title:** *Semihydrogenation of acetylene to ethylene with a PdAg catalyst* (TU Delft, Catalysis Engineering Group, June 2024).
* **Supervisors:** Ir. Damian Vico van Berkel & Prof. Atsushi Urakawa.
* **Primary Source:** `Articles/2 meeting Damian + Zoë/BEP Example.pdf` (97 pages) in the project management archive.

Larsen investigated the static steady-state trade-offs of acetylene hydrogenation over bimetallic $PdAg$ catalysts ($\text{Pd}_0\text{Ag}$, $\text{Pd}_2\text{Ag}$, $\text{Pd}_3\text{Ag}$) in a $150\ \text{mg}$ quartz tubular packed-bed reactor ($100\ ^\circ\text{C}$, $1\ \text{bar}$).

---

## 2. Ground-Truth Warning & Known Extraction Pitfalls
**CRITICAL: Do not fall into known extraction traps recorded in `conventions.md` §12!**

1. **Scanned Raster Appendices (No Text Layer):**
   The main text of `BEP Example.pdf` ends on page 54. **Appendix E (Tables E.1–E.3: fitted parameter tables)** and **Appendix F (Python code screenshots, Differential Evolution bounds, reactor dimensions)** occupy pages 71–88. These pages are **bitmap images with zero text layer**. Any text search or simple `pypdf` text extraction on these pages returns empty strings!
2. **Incomplete Parameter Sets:**
   Previous runs circulated an incomplete 6-parameter set (`k1`, `k2`, `K_C2H2`, `K_C2H4`, `K_inh`, `K_H2`). This set was missing $r_{1,\max}$ and the fitted non-integer exponent $n_{\text{inh}}$. Without these, Larsen's final rate law (Eqs. 6.9–6.11) cannot be evaluated.
3. **Missing Reactor Normalization:**
   Cross-sectional area $A$, bed length $L$, and catalyst bed density $\rho_{\text{support}}$ are omitted from the main thesis text; they exist only inside the Python code screenshots in Appendix F.
4. **No Raw Tables, Only Graphical Plots:**
   Larsen published overall RMSEs (5.10%, 5.43%, 7.14 percentage points), but experimental points exist only in the graphical curves of Appendices B, C, and D.

---

## 3. Required Methodology & Verification Steps

### Step 1: Render and OCR/Inspect Appendix Pages 71–88
Using Python (`fitz` / PyMuPDF or `pdf2image`):
1. Render pages 71–76 (Appendix E: Parameter tables) and pages 77–88 (Appendix F: Python script) to 300 DPI PNG images in a scratch directory.
2. Inspect the rendered images to extract:
   - The exact reactor tube dimensions: internal diameter $d_t$ (or cross section $A$), bed length $L$, mass of catalyst ($150\ \text{mg}$), mass of SiC diluent ($300\ \text{mg}$), total gas flow rate ($30\ \text{mL/min}$).
   - The complete parameter sets from Tables E.1, E.2, and E.3, including $k_1, k_2, K_{\text{C}_2\text{H}_2}, K_{\text{C}_2\text{H}_4}, K_{\text{H}_2}, K_{\text{inh}}, r_{1,\max}$, and $n_{\text{inh}}$.

### Step 2: Digitize Experimental Curves from Appendices B, C, D
1. Extract the experimental data points from:
   - **Appendix B:** Conversion and selectivity vs. $p_{\text{C}_2\text{H}_2}$
   - **Appendix C:** Conversion and selectivity vs. $p_{\text{C}_2\text{H}_4}$
   - **Appendix D:** Conversion and selectivity vs. $p_{\text{H}_2}$
   for all three catalyst variants ($\text{Pd}_0\text{Ag}$, $\text{Pd}_2\text{Ag}$, $\text{Pd}_3\text{Ag}$).
2. Save the digitized coordinates to clean CSV files under `notebooks/benchmarks/data/`.

### Step 3: Implement the 1D Differential Reactor ODE Model
Implement Larsen's molar balance ODEs (Eqs. 4.6–4.9):
$$\frac{d F_i}{d z} = A \, \rho_{\text{support}} \, \sum_j \nu_{i,j} \, r_j$$
With Extended LHHW rate laws (Eqs. 6.9–6.11):
$$r_1 = \frac{k_1 K_{\text{C}_2\text{H}_2} p_{\text{C}_2\text{H}_2} K_{\text{H}_2} p_{\text{H}_2}}{\left(1 + K_{\text{C}_2\text{H}_2} p_{\text{C}_2\text{H}_2} + K_{\text{C}_2\text{H}_4} p_{\text{C}_2\text{H}_4} + K_{\text{H}_2} p_{\text{H}_2}\right)^2}$$
$$r_2 = \frac{k_2 K_{\text{C}_2\text{H}_4} p_{\text{C}_2\text{H}_4} K_{\text{H}_2} p_{\text{H}_2}}{\left(1 + K_{\text{C}_2\text{H}_2} p_{\text{C}_2\text{H}_2} + K_{\text{C}_2\text{H}_4} p_{\text{C}_2\text{H}_4}\right)^2 \left(1 + K_{\text{inh}} p_{\text{C}_2\text{H}_2}\right)^{n_{\text{inh}}}}$$

### Step 4: Validate RMSE against Larsen's Reported Benchmarks
Compute the root-mean-square error (RMSE) in percentage points between model predictions and experimental points:
$$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{k=1}^N \left(X_{\text{pred}, k} - X_{\text{meas}, k}\right)^2}$$
Verify that simulated RMSE matches Larsen's published values:
- $\text{Pd}_0\text{Ag}$: $\approx 5.10\ \text{percentage points}$
- $\text{Pd}_2\text{Ag}$: $\approx 5.43\ \text{percentage points}$
- $\text{Pd}_3\text{Ag}$: $\approx 7.14\ \text{percentage points}$

---

## 4. Deliverable
A clean, self-contained, and fully executed Jupyter notebook:
`notebooks/benchmarks/larsen_2024_benchmark.ipynb`
with side-by-side plots reproducing Larsen's Conversion & Selectivity curves and explicit error metrics.


**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts.