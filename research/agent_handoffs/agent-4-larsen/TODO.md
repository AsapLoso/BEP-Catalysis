# Agent 4 — Larsen 2024 source-audit execution receipt

**Status:** Revised plan approved and executed on feat/larsen-pdag-benchmark. This branch contains a restricted independent audit, not a full-data validation of Figure 6.6.

## Completed

- [x] Fetched the latest remote branch and reviewed intervening source-audit changes before implementation.
- [x] Verified the uploaded thesis binary SHA-256: b5aaa2300ff9b64aca70e58cc5e4d8be30b3c12ee264e69af89e01c86f5120c9. The tracked copy matches the upload; official-deposit identity remains unverified.
- [x] Visually rechecked PDF p. 43 Eqs. 6.9–6.11 and PDF p. 44 Figure 6.6; separately transcribed main-text model/results excerpts.
- [x] Transcribed Appendix E Tables E.1–E.3 and all readable Appendix F code on PDF pp. 78–88; transcribed every displayed processed-input table row and legible cell plus the complete 41-row Pd₀Ag comparison table, with page locators and explicit `[unclear]`/cropping/source-ellipsis markers.
- [x] Mapped all 15 selected Pd₂Ag operating conditions to displayed Appendix F experiment IDs and four Pd₃Ag Figure 6.1 head rows. The crosswalk preserves condition-match versus same-record uncertainty.
- [x] Added source-processed response cells for the mapped Pd₂Ag/Pd₃Ag rows without modifying the historical selected-curve CSV or relabeling processed outputs as raw GC data.
- [x] Reconciled source/table counts: Pd₀Ag 41, Pd₂Ag 42 and Pd₃Ag 77 processed rows; Figure 6.6 reports 41/42/41. The 36-row Pd₃Ag final-fit exclusion mask is not shown.
- [x] Compared printed first-power Eq. 6.11 with the historical/Appendix F squared alternative using the same Figure 6.6 vectors and no refit.
- [x] Created and top-to-bottom executed a separate source-audit notebook plus a reproducible nbclient runner. The original benchmark notebook remains unchanged.
- [x] Saved model predictions, five flow-reference scenarios, solver/balance checks, mapped processed-subset metrics, pointwise plot/table discrepancies and reconciliation tables under research/evidence/derived/.
- [x] Wrote the independent source/model/data audit report and updated this GOAL/TODO status without claiming full source completion.

## Numerical receipt

- Selected chart subset, paired RMSE (pp), first-power / squared:
  - Pd₀Ag: 13.4450 / 5.2680, 15 points.
  - Pd₂Ag: 15.4886 / 5.4700, 15 points.
  - Pd₃Ag: 21.2881 / 21.0815, 15 points.
- Visible source-processed mapped subset, first-power / squared: Pd₀Ag 13.4450 / 5.2680 (15); Pd₂Ag 16.3833 / 6.1663 (15); Pd₃Ag 9.7003 / 9.5815 (4). These unequal subsets are not final fit metrics.
- Four plot/table differences exceed the prior ±2 pp graph-reading band: Pd₂Ag Figure 6.2 conversion at 10 and 15 mbar; Pd₂Ag Figure 6.4 selectivity at 100 mbar H₂; Pd₃Ag Figure 6.1 selectivity at GHSV 30000 h⁻¹.
- Paired RMSE formula agrees with direct Eq. 4.14–4.15 evaluation within 1e-12 pp. Stored squared-law historical metrics are reproduced within 4.3e-7 pp.
- Max BDF/Radau difference 1.73e-5 pp; max base/tight tolerance difference 1.69e-5 pp; consistent Pa-to-kPa parameter scaling difference 7.47e-10 pp.
- Most negative integrated species flow −6.62e-17 mol s⁻¹; maximum elemental-flow residual 2.89e-19 mol atoms s⁻¹. Tests passed at the tolerances recorded in the audit report.

## PASS / BLOCKED gates

- **PASS:** uploaded-file hash; target equation notation; Figure 6.6 eight-value transcription; Appendix E tables; recoverable Appendix F code/input-table/comparison-table transcription; source RMSE definition; fixed-parameter candidate-law comparison; selected-row numerical stability and elemental balances; no-CO model scope.
- **PASS with source gaps:** Appendix F readable code and visible processed-table/comparison entries are transcribed. The Pd₃Ag middle rows are absent from Larsen's display; six cell values across five rows are marked `[unclear]`; a page-edge comparison row is partly unreadable; intermediate DataFrame previews omit rows/columns, and the p. 85 `df_fit` output elides columns. These limitations do not alter the processed-input table counts.
- **PASS with limitation:** Pd₀Ag/Pd₂Ag processed-row counts and all 15 selected Pd₂Ag table ID matches; four visible Pd₃Ag flow-row ID matches.
- **BLOCKED:** four source table versus plotted response mismatches; Pd₃Ag's 36 final-fit IDs; raw GC/workbook provenance; independent Figure 6.6 all-experiment RMSE; official thesis version; final extended fit implementation; source-certified temperature, flow reference and final fitted-parameter units.

## Reproduction environment

- OS: Linux 6.18.55-x86_64, glibc 2.41.
- Interpreter: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python` (preinstalled runtime; no dependencies installed or repository environment files changed).
- Python 3.12.14; NumPy 2.3.5; pandas 2.2.3; SciPy 1.17.0; Matplotlib 3.10.8; nbformat 5.11.1; nbclient 0.11.0.
- Command: python notebooks/benchmarks/run_larsen_source_audit.py
- Execution: nbclient, Python 3 kernel, timeout 600 s, working directory notebooks/benchmarks, 18 cells, top-to-bottom. Runtime: 29.095 s.
- Executed notebook SHA-256: 5966774c96f99186095e0c07be205d8f5c7367125ec96e81877f882693ce3465.
- Tolerances: paired metric atol 1e-12 pp; stored historical regression <0.02 pp; solver/tolerance and unit-scaling response changes <1e-4 pp; minimum flow state >−1e-10 mol s⁻¹; element-flow residual <1e-10 mol atoms s⁻¹.

## Git receipt

- Implementation commit: `a3af8ee03642f053b143273b5040a6904678453a`.
- This receipt update is a second documentation commit; its SHA is reported in the final handoff because a commit cannot contain its own hash.
- Branch: feat/larsen-pdag-benchmark.
- No PR, merge, force-push, personal-map edit or Agent 5 synthesis was made.
