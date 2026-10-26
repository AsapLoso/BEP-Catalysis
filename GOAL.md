# Agent 4 — Larsen 2024 PdAg source audit

**Branch:** feat/larsen-pdag-benchmark
**Tracking issue:** GitHub issue #11 — Larsen primary-source audit
**Execution status (2026-10-26):** The owner approved the revised research plan. Independent source checks, selected-row ID reconciliation and fixed-parameter numerical tests have been run. This is a restricted audit; the full source-faithful final-fit reproduction is not complete.

## Mission

Establish what Victor Larsen's June 2024 TU Delft Bachelor End Project actually prints and what can be numerically reproduced from the available thesis evidence for acetylene semihydrogenation over Pd₀Ag, Pd₂Ag and Pd₃Ag. Keep literal source text, author-processed response tables, graph digitizations, model outputs and scientific interpretation distinct.

No Larsen CO experiment was found or is modeled. Do not use the incomplete six-parameter Appendix F standard-model fit as a substitute for the eight-parameter Figure 6.6 vectors; the missing terms r₁,max and nᵢₙₕ are necessary for the later law.

## Current source findings

- The owner-uploaded 97-page PDF matches SHA-256 b5aaa2300ff9b64aca70e58cc5e4d8be30b3c12ee264e69af89e01c86f5120c9. Its internal creation metadata is 2026-06-26; equivalence to an official 2024 deposit remains unverified.
- Main-text Eq. 6.11 (PDF p. 43 / printed p. 37) has no superscript on the first r₂ adsorption denominator factor. Appendix F's standard LHHW code and the historical notebook use a squared factor. The final extended-fit code is not present, so the Figure 6.6 fitting law remains unproven.
- Methods text says experiments ran at 80 °C; the abstract, Table 6.1 and Appendix F code say 100 °C. The MFC flow reference basis and fitted parameter units are not stated unambiguously.
- Appendix F contains 42 Pd₂Ag author-processed response rows, all displayed; it does not contain the raw workbook or GC peak areas. The Pd₃Ag table reports 77 processed rows but displays only EXP1–4 and EXP73–77 around an ellipsis. Figure 6.6 reports N=41 for Pd₃Ag, leaving 36 IDs outside the reported fit count without an inclusion mask.
- Four selected Figure 6.1–6.4 plot digitizations differ from condition-matched Appendix F response cells by more than the previous ±2 percentage-point chart-reading uncertainty. Preserve both values pending source-data review.
- Appendix E Tables E.1–E.3 are fully transcribed. Appendix F has visually checked formulas, constants, bounds, selected table values and code passages, but its complete screenshot code/table content is not fully transcribed.

## Deliverables and verification

- Source transcripts: research/evidence/transcriptions/larsen_2024_appendix_E_F.md and larsen_2024_main_source_excerpts.md.
- Separate historical implementation: notebooks/benchmarks/larsen_2024_benchmark.ipynb remains unchanged. The independent, executable audit is notebooks/benchmarks/larsen_2024_source_audit.ipynb with runner notebooks/benchmarks/run_larsen_source_audit.py.
- Crosswalks, selected processed table rows, predictions, flow sensitivities and numerical checks are indexed in research/evidence/derived/README.md.
- Findings, citations, results, PASS/BLOCKED gates and reproduction receipt are in research/reports/larsen_2024_equation_and_baseline_audit.md.
- Numerical checks PASS for the paired RMSE formula, fixed-vector historical squared-law regression, solver/tolerance sensitivity, stoichiometric invariants, positivity tolerance, and consistent Pa↔kPa unit rescaling. The printed Eq. 6.11 first-power scenario was also computed without refitting.
- Full Appendix F transcription, exact four plot/table discrepancies, Pd₃Ag final-fit IDs, full-data RMSE reproduction, official PDF-version authentication, and source-certified temperature/flow/parameter units remain BLOCKED.

## Remaining evidence needed for a source-complete baseline

1. Original input workbook and raw GC records, including the complete processed/final fit inputs.
2. Exact plot source values or independent review of the four response differences.
3. The final extended-model implementation and the row masks used for Figure 6.6.
4. Authenticated official thesis deposit/version and any revision history.
5. Unambiguous experimental temperature, flow reference, pressure basis and fitted coefficient units.
6. Full human-readable Appendix F transcription where source screenshots expose readable text.

## Ownership and workflow boundaries

This is AI reference work, separate from the owner's personal knowledge map and personally authored notebook. Preserve the original PDF, source renders and historical benchmark implementation. Work only on feat/larsen-pdag-benchmark. Do not edit the personal map, create a PR, merge, force-push, or perform an Agent 5 CO synthesis.
