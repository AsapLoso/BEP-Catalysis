# Agent 1 — Schbib source/benchmark audit gates

**Current state (2026-10-25): PREPARING PLAN; SOURCE AUDIT NOT YET VERIFIED.** The pre-existing notebook and four plots are historical artifacts, not verified Table 6 reproduction. Read `GOAL.md` and [issue #10](https://github.com/AsapLoso/BEP-Catalysis/issues/10). Do not check a box without a source or execution receipt.

## 00 — Plan for owner review (first)
- [ ] Inspect the original Schbib PDF/HTML/text, historical notebook/plots and any accessible author/publisher correction; check source access and exact relevant pages.
- [ ] Present an **independently expanded scientific plan**, explicitly testing alternative causes of the failed Table 6 result, including corrected logs, unit/mass bases, rate equations and reactor heat/geometry closure.
- [ ] Receive owner review/approval of the plan **before substantive changes to models and primary-code implementation**.

## 01 — Source-verified kinetics and source audit (after plan approval)
- [ ] Record Table 3/4/6/8 evidence by page/figure/table, plus any verified correction provenance and author/publisher status.
- [ ] Verify original vs potential corrected `log10 A(K_H)`/`log10 A(K_CO)`; distinguish logarithms from numerical pre-exponentials and check concentration/catalyst mass/rate units.
- [ ] Check complete vs simplified rate equations and each adsorption-denominator term; test dimensional factors and catalyst/bed definitions.
- [ ] Check laboratory temperature/pressure/flow and heat-transfer model against the adiabatic simplified notebook; document where exact reproduction is not justified.

## 02 — Reproducibility and failure isolation
- [ ] Independently execute baseline with original printed values; write actual Table 6 residuals and Figure 1–4 differences. Saved historical outputs are not rerun results.
- [ ] Test verifiable corrected/alternative parameter interpretations **one change at a time**; explicitly document unresolvable data, discrepancies and any differences in physical reactor assumptions.
- [ ] Check species/element balance, nonnegative/finite states, positive denominators, solver convergence, temperature law and mass/volume factor units.
- [ ] Explain the common-denominator local rate-ratio cancellation and distinguish reactor outlet selectivity and gas-phase thermal responses.

## 03 — Research report and handoff
- [ ] Deliver `research/reports/schbib_parameter_and_benchmark_audit.md` with source citations, validation table, reproducibility instructions, actual environment and uncertainties.
- [ ] Correct/update `notebooks/benchmarks/schbib_1996_steady_state.ipynb` where justified; preserve source-version/provenance explanations and old interpretation in Git history.
- [ ] Provide an Agent 5 readiness receipt: **PASS if a source-faithful parameter/rate formulation is demonstrable; BLOCKED if not**, listing exact unresolved transfer/validation risks. Do not force PASS to produce a success narrative.
- [ ] Commit/push on `feat/schbib-co-benchmark` only after plan approval, and report exact SHA. No PR/merge; no owner personal-map edits.

## Historical baseline status (not new checkmarks)
- The branch already contains an executed notebook and four generated figures.
- The notebook's source-input PFR check reported severe acetylene Table 6 disagreement; **the existing "figure reproduction" alone is not an independently validated benchmark.**
