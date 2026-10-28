# Subgoals & Gate Receipts — Larsen (2024) PdAg Replication

**Status: COMPLETED (2026-10-25).** The selected-curve benchmark and executed BDF notebook are complete. Known data limit: the thesis omits full raw Pd₂Ag/Pd₃Ag response tables, so the reported all-experiment RMSE values are preserved from Figure 6.6 but cannot be independently recalculated.

## 01 — High-Resolution Source Extraction
- [x] Render scanned Appendix E/F pages at 300 DPI and inspect them visually.
- [x] Confirm E.1–E.3 are standard-model variant comparisons, not final parameter tables.
- [x] Transcribe all eight final parameters per catalyst from Figure 6.6.
- [x] Recover Appendix F geometry and the Table 6.1 catalyst masses: 0.5 cm tube ID, 2.65 g cm⁻³ support density, and 100/75/100 mg for Pd₀Ag/Pd₂Ag/Pd₃Ag.

## 02 — Experimental Data Extraction
- [x] Transcribe selected exact Pd₀Ag responses from the Appendix F experiment and comparison tables.
- [x] Digitize the matching Pd₂Ag and Pd₃Ag responses from Figures 6.1–6.4; mark chart-derived values as estimates with reading uncertainty.
- [x] Save selected responses and parameter provenance to CSV under `notebooks/benchmarks/data/`.
- [x] Correct source mapping: Figures 6.1–6.4 and Appendix A are experimental; Appendices B–D are simulated.

## 03 — Differential Reactor Model
- [x] Implement the species molar balances and final extended LHHW law, including `r1_max` and `n_inh`.
- [x] Use He as the inert balance gas and exclude CO.
- [x] Integrate the model with `solve_ivp(method="BDF")` at all 45 selected feed conditions and calculate conversion/selectivity.

## 04 — RMSE and Figure Comparison
- [x] Plot measured/digitized selected curves with model overlays for Figures 6.1–6.4.
- [x] Calculate paired experiment RMSE and component RMSE for the selected 15-point subsets.
- [x] Record Larsen's all-experiment RMSE values from Figure 6.6 (5.0962/5.4320/7.1353 percentage points; N=41/42/41).
- [x] State the limit: the thesis does not provide full raw response tables for Pd₂Ag/Pd₃Ag, so the published all-experiment RMSE values cannot be independently recalculated from this source alone.

## 05 — Gate Receipt
- [x] Execute `notebooks/benchmarks/larsen_2024_benchmark.ipynb` with zero cell errors in under 60 seconds.
- [x] Commit the notebook, selected response data, parameter data, and 300-DPI Appendix E/F renders.
