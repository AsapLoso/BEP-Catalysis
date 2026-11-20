# Agent 1 — Schbib source/benchmark audit gates

**Current state (2026-10-26): AUDIT EXECUTED; report and reproducible notebook delivered.** See [the research report](research/reports/schbib_parameter_and_benchmark_audit.md), [the executed benchmark notebook](notebooks/benchmarks/schbib_1996_steady_state.ipynb), and [the derived result record](research/evidence/derived/schbib_1996_audit_results.json). The plan was approved before substantive model changes. Commit and branch-push receipt is recorded in the task completion summary.

## 01 — Source verification

- [x] Visually inspect the archived Schbib PDF at PDF pages 4, 6, 7, and 8 (printed pp.1499, 1501–1503); transcribe Tables 3, 4, 6, 8 and Eqs. 22, 24, 25 with source locators. **PASS.** The original PDF, HTML, and extracted-text source files were left unchanged.
- [x] Keep the printed Table 8 and author-shared correction as separate records and parameter sets. **PASS.** ACS authorship and ResearchGate uploader/signature records support attribution to Noemí S. Schbib; visual verification and publisher/erratum confirmation remain **BLOCKED** because the linked PDF returns 404. The extracted correction changes `k_A`/`k_E` units from gcat to kgcat while retaining their numeric logs; this mass-basis difference remains unresolved.
- [x] Record the Table 7 prose/table inconsistency and distinguish directly sourced values from interpretations and diagnostics. **PASS.** The report retains this unresolved discrepancy.

## 02 — Numerical execution and controlled comparisons

- [x] Inspect Python/runtime dependencies and execute the model under Rule 19. **PASS.** Python 3.12.14 with NumPy, SciPy, pandas, Matplotlib, ipykernel, nbclient, and nbformat was available; no packages or dependency files were changed. See the report/JSON receipt for interpreter, package versions, and exact command.
- [x] Compare original printed and complete author-shared parameter sets; separately run one-group sensitivities, full versus simplified kinetics, mass-basis and concentration-unit checks. **PASS.** Diagnostics are labeled and not represented as physically consistent source models.
- [x] Validate atom balance, finite/nonnegative accepted states, positive denominators, Arrhenius/log behavior, unit invariance, and solver refinement. **PASS** for tested trajectories; numerical tolerances and measured deltas are in the report and result record.
- [x] Reproduce the historical Table 6 run in a temporary copy and preserve the historical notebook byte-for-byte. **PASS.** Fresh temporary outputs agree with stored historical outputs; historical plot files were not modified.
- [x] Execute the fresh notebook top-to-bottom and inspect rendered plots. **PASS.** Four new diagnostic plots were inspected; saved historical plots were inspected separately.

## 03 — Experimental gates and interpretation

- [x] Evaluate Table 6 with the original printed Table 8 set. **BLOCKED overall:** C₂H₂ predictions are 0.8409%, 0.0099%, and 0.0018% versus 98.31%, 98.99%, and 98.62% measured.
- [x] Evaluate Table 6 with the author-shared text set. **PASS provisionally for C₂H₂ only:** maximum absolute C₂H₂ error 1.475 percentage points. **BLOCKED overall:** maximum C₂H₄ error is 10.763 points for net disappearance (9.583 points if the measured quantity is interpreted as reaction-2 extent). The correction is author-attributed but not independently document-authenticated or publisher-verified.
- [x] Evaluate Figures 1–4. Figure 1 quantitative pointwise comparison **BLOCKED** (no digitization); Figure 2 **PARTIAL** inlet-rate scale check; Figures 3–4 **PARTIAL** acetylene-outlet checks and **BLOCKED** full profiles/heat-transfer reproduction.
- [x] Separate internal implementation checks from experimental validation. **PASS** internally does not imply full source-model reproduction; full Table 6 benchmark gate remains **BLOCKED**.

## 04 — Report, handoff, and delivery

- [x] Deliver [`research/reports/schbib_parameter_and_benchmark_audit.md`](research/reports/schbib_parameter_and_benchmark_audit.md), checked source transcription, separate correction provenance record, derived JSON, and fresh notebook outputs.
- [x] Preserve the pre-audit notebook as [`notebooks/benchmarks/schbib_1996_steady_state_historical.ipynb`](notebooks/benchmarks/schbib_1996_steady_state_historical.ipynb).
- [x] Give the future Agent 5 a bounded handoff: the Pd/α-Al₂O₃ reaction bookkeeping and provenance-labeled rate laws are usable as reference; the two CO adsorption pre-exponentials remain alternatives; neither set is validated for PdAg transfer.
- [x] Commit and push only to `feat/schbib-co-benchmark`; no PR, merge, personal-map edit, or other-branch change.

The complete all-species Table 6 reproduction remains unresolved. Do not describe the author-shared table as an independently verified erratum or claim that one correction alone explains the discrepancy.


## 05 — Small follow-up: independent state-space numerical verification (NOT a new source fit)
- [x] Document and scratch-run a **two-reaction-extent** formulation against the isothermal Table 6 system. SymPy balance equations and four SciPy solvers yield the previously reported species-flow numerical predictions to displayed precision. Record checked scope and runtime in [analysis note](research/evidence/analysis/schbib_reaction_extent_state_space_crosscheck_2026_10_26.md).
- [x] Add independently implemented [cross-check script](notebooks/benchmarks/schbib_1996_extent_crosscheck.py) to the agent branch. It checks the extent-space results against the original six-flow derived JSON without changing the audit notebook.
- [x] Execute the repository-local script with its derived JSON present and capture stdout/runtime. **PASS:** `E·N = 0`; max solver spread 1.013×10⁻⁷ pp; maximum difference from the six-flow JSON 4.934×10⁻⁶ pp; elapsed time 1.27 s. It covers both parameter sets and all three CO cases and checks acetylene conversion, net ethylene conversion, and reaction-2 extent. See the updated analysis note and audit report.
- [x] State the fixed-temperature reference boundary. The visually checked printed Table 8 law remains usable for a reproducible Pd/α-Al₂O₃ reference calculation with the base-10 `log A` assumption and gcat-to-kg mass conversion stated. Its Table 6 predictions are not experimentally validated; the correction's publisher status, visual values and kgcat/gcat intent remain unestablished.
- [ ] If Model III work is authorized, first inventory every published heat/mass-transfer coefficient, catalyst pellet diameter, wall temperature profile and experimental input; separate published numeric values from parameters available only through cited correlations and genuinely missing quantities. **Do not substitute another kinetics paper merely because thermal/transport inputs are incomplete.**

The Model III inventory was outside this bounded follow-up and was not repeated.

The existing all-species Table 6 result is still **BLOCKED**. No changes to Agent 5 or owner map are authorized by this check.
