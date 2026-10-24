# Subgoals & Gate Receipts — Larsen (2024) PdAg Replication

## 01 — High-Resolution Raster Appendix Extraction
- [ ] Render pages 71–88 of `BEP Example.pdf` to 300 DPI PNG images in `scratch/larsen_appendices/`.
- [ ] Extract full parameter sets from Tables E.1–E.3, specifically recovering $r_{1,\max}$ and $n_{\text{inh}}$.
- [ ] Extract tube diameter, bed length, and catalyst mass from Appendix F Python code screenshots.

## 02 — Experimental Curve Digitization
- [ ] Digitize data points from Appendix B (vs. $p_{\text{C}_2\text{H}_2}$), Appendix C (vs. $p_{\text{C}_2\text{H}_4}$), and Appendix D (vs. $p_{\text{H}_2}$) across $\text{Pd}_0\text{Ag}$, $\text{Pd}_2\text{Ag}$, and $\text{Pd}_3\text{Ag}$.
- [ ] Save raw coordinates to CSV in `notebooks/benchmarks/data/`.

## 03 — 1D Differential Reactor ODE Simulation
- [ ] Implement Larsen's molar balance ODEs (Eqs. 4.6–4.9) with Extended LHHW rate laws (Eqs. 6.9–6.11).
- [ ] Solve ODEs across experimental partial pressures.

## 04 — RMSE Validation & Figure Overlay
- [ ] In `notebooks/benchmarks/larsen_2024_benchmark.ipynb`, plot simulated vs. measured conversion and selectivity curves.
- [ ] Calculate RMSE in percentage points and confirm agreement with Larsen's published values (Pd0Ag: ~5.10%, Pd2Ag: ~5.43%, Pd3Ag: ~7.14%).

## 05 — Gate Receipt
- [ ] Notebook executes cleanly with 0 errors in < 60 seconds. Commit notebook and digitized data.
