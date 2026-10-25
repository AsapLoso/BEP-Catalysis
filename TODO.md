# Agent 4 — Larsen 2024 independent re-audit gates

**Current status (2026-10-25): prior selected-curve notebook exists; SOURCE-FAITHFUL BASELINE IS UNDER REVIEW.** The prior `COMPLETED` banner is a **historical implementation receipt**, not approval of the exact source equation, flow/parameter units or independent experimental validation. Read revised `GOAL.md` and [issue #11](https://github.com/AsapLoso/BEP-Catalysis/issues/11) first.

## 00 — Source access and own plan (before code changes)
- [x] **Source access only:** the 97-page Larsen PDF has now been uploaded to `research/evidence/original/` and its Git blob matches the user-uploaded original (`8207c91e...`); the native text layer is also available. **This does NOT verify an official 2024 deposit or its scientific content.**
- [ ] Inspect **existing** 18 render PNGs: `notebooks/benchmarks/source_renders/appendix_pages/page-71.png` … `page-88.png`, plus `README.md`; do not reproduce them unless necessary. They cover Appendix E/F, **not** main-text Eq. 6.11.
- [ ] Plan a **literal, human-readable, visually checked, page-by-page transcription** `research/evidence/transcriptions/larsen_2024_appendix_E_F.md` for the 18 rendered pages. Preserve table/code fidelity and mark ambiguous fields; do not substitute already-derived CSVs for original text.
- [ ] Inspect the imported notebook, selected-curve CSV, parameter CSV and source/experiment distinction; record historical assertions vs directly verified claims.
- [ ] Present an independently developed **scientific re-audit plan** addressing disputed Eq. 6.11, feed volume-flow reference basis, missing fitted coefficient units, source access, discriminating comparisons and actual PASS/BLOCKED criteria. Get owner plan feedback before substantive model changes.

## 01 — Readable original-source transcription and equation audit (after plan approval)
- [ ] Transcribe each available PDF page 71–88 into Markdown text/tables/code as source-faithfully as possible, with original image links, method, printed-page index where visible and visual verification status. Keep interpretations in a separate analysis file.
- [ ] Use the now-accessible full PDF to visually verify Eqs. 6.9–6.11 (PDF p. 43), Figure 6.6 parameter plot (PDF p. 44), experimental methods, and flow definitions. Treat native text and graph/scan images differently; do not fabricate unrecognized table cells.
- [ ] Read original thesis Eq. 6.9–6.11 (or label unavailable), including `r1_raw`, `r1_max` cap, `r2` inhibition factor and **first vs squared adsorption denominator**. Audit alternative Appendix F code if it implements a different model. Record exact page/equation evidence.
- [ ] Compare source-printed formula with the previous notebook's `r2` squared denominator, using the SAME fitted coefficients, and report numerical effects; do not silently refit.
- [ ] Extract Figure 6.6 eight-element vectors (k1,k2,r1_max,K_C2H2,K_H2,K_C2H4,K_inh,n_inh); record direct transcription vs inferred units and preserve model/pressure basis.
- [ ] Resolve or bracket flow volume reference conditions: actual vs STP/standardized `flow_ml_min`, the correct `T_ref,P_ref`, mass-normalized space velocity, catalyst loading, tube diameter and support density.
- [ ] Inspect experimental Figure 6.1–6.4/Appendix A versus simulated B–D; do not mistake selected-digitized points or appendix variant tables for measured data or final parameters.

## 02 — Independent no-CO reproducibility
- [ ] Run source-faithful BDF simulations at source feed/mass conditions for Pd0Ag, Pd2Ag, Pd3Ag; record outputs, actual software environment and convergence checks.
- [ ] Verify molar/element balances, positivity, finite states and denominator/rate-law dimensional consistency.
- [ ] Compare to exact Pd0Ag Appendix F measured table and estimated Pd2Ag/Pd3Ag plot points with uncertainty; keep published all-experiment RMSE (41/42/41 source experiments) separate from selected-subset performance.
- [ ] Investigate whether changed Eq. 6.11 or feed flow convention *improves/worsens* literature reproduction; include contradictory or null results and identifiability caveats.

## 03 — Report and handoff
- [ ] Write `research/reports/larsen_2024_equation_and_baseline_audit.md`: primary-source locators; source accessibility; full equation comparison; parameter/units ledger; flow reference definition; data provenance; numerical evidence; limitations.
- [ ] Correct the notebook / derived CSV **only if warranted by primary evidence**. Preserve old implementation and outputs in Git history and document all changes.
- [ ] Mark source-derived reproduction **PASS or BLOCKED** (not automatically completed merely because the notebook runs). Supply the verification receipt and remaining source questions to Agent 5.
- [ ] Commit/push only on `feat/larsen-pdag-benchmark` after owner approves the plan. No PR or merge, no personal-map modifications; report commit SHA.

## Prior historical implementation (preserved in Git, not rechecked now)
- A 13-cell Larsen benchmark notebook and selected response/parameter CSVs exist with saved executed plots.
- Appendix E/F were already rendered into 18 Git-tracked 300-DPI PNGs.
- Earlier work reported source Figure 6.6 RMSEs and 45 selected curve comparisons. Its code currently has a squared `r2` denominator and converts volumetric inlet flows using reactor conditions; **both require independent source verification**.
