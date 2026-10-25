# Agent 4 — Larsen (2024) source-faithful PdAg benchmark re-audit

**Branch:** `feat/larsen-pdag-benchmark`  
**Current task:** independently review and, where warranted, correct the 2024 source-rate formulas, volume-flow basis and benchmark.  
**Tracking issue:** [#11 — Larsen primary-source audit](https://github.com/AsapLoso/BEP-Catalysis/issues/11)  
**Dependency:** Agent 5's PdAg–CO synthesis remains paused until Agent 1 and 4 produce auditable baselines and the owner reviews them.

## 0. Begin in plan mode — expand, challenge, then execute

First read this GOAL, `TODO.md`, issue #11, the original thesis where accessible, the **existing** notebook/CSV/appendix renders, and `AGENTS.md`. **Design your own detailed investigation plan** from the user-suggested corrections, not just an implementation list. Explain competing interpretations and propose source checks and numerical experiments that can distinguish them.

**Present the plan for the owner's review before changing model equations/data.** Once reviewed/approved, work autonomously within `feat/larsen-pdag-benchmark`: investigate, run, modify files, document evidence, commit and push without per-commit permission. No force-push, PR or merge, no modification of `main`/other branches, owner personal map or personally authored notebook.

Your plan needs a source-access assessment, priority/order of corrections, exactly what is considered published versus computed, regression tests, expected changes in predictions, fallback for missing full thesis/raw measurements, and honest PASS/BLOCKED criteria.

## 1. Available evidence: inspect before re-creating

**The appendix IS already in this branch**, in normal Git-tracked files:

- `notebooks/benchmarks/source_renders/appendix_pages/README.md` — explains the rendered source and page numbering.
- `notebooks/benchmarks/source_renders/appendix_pages/page-71.png` through `page-88.png` — **18 existing high-resolution 300-DPI image renders of PDF pages 71–88** (not thesis printed page numbers). These are Appendix E/F, containing model-variant tests, inputs/code and Pd₀Ag experimental/comparison tables. **Use these; do not regenerate unless they prove inadequate.**
- `notebooks/benchmarks/larsen_2024_benchmark.ipynb` — previous executed 13-cell benchmark, with stored outputs; **not** independent proof of a correct source model.
- `notebooks/benchmarks/data/larsen_2024_parameters.csv` — eight extracted parameter fields per catalyst, marked **inferred** units.
- `notebooks/benchmarks/data/larsen_2024_selected_curves.csv` — selected response table: exact transcriptions and visually digitized markers labelled differently.

**Missing here:** the *full* Larsen 2024 thesis PDF. The owner reports it exists in a **local Zotero archive** outside this Git branch. Check whether the actual execution environment offers accessible Zotero files, prior project archives or source-publisher access. Historical absolute `file:///c:/Users/...` pointers in earlier notes are not portable. Do **not** assume those paths or Zotero archives are mounted in cloud environments. If the thesis is accessible, inspect it with actual PDF page images and text, especially the main-text Eq. 6.9–6.11 and Figure 6.6 (printed p. 38). If not, explicitly mark which questions are unverified: appendix pages 71–88 **do not substitute** for pages containing the main-body equations. Do not silently call derived CSVs a primary source.

**Primary thesis:** Victor Larsen, *Semihydrogenation of acetylene to ethylene with a PdAg catalyst*, TU Delft BEP (June 2024). The paper/project is a **Bachelor End Project, not a master's thesis**.

## 2. Mandatory readable appendix transcription — evidence before code corrections

The existing 18 original PNG page renders are *not* an accessible text substitute. **Deliver a page-indexed, human-readable source transcription** at `research/evidence/transcriptions/larsen_2024_appendix_E_F.md`, covering PDF page indices 71–88, with readable tables, equations, and relevant printed-code passages. Use `research/evidence/transcriptions/larsen_appendix_E_F_worklist.md` as the tracked transcription specification and link each section to its corresponding original image. Provide printed thesis page numbers where present, and explicit `[unclear]` markers for unreadable cells; don't invent missing content. If using OCR as a draft aid, visually verify each page/table against the render. Keep all personal interpretation and proposed model corrections in `research/evidence/analysis/` or the audit report, never inside literal source transcription. Existing derived CSVs and stored model outputs are not verified transcripts.

**The owner should NOT have to evaluate source mathematics to grant plan approval.** Present source-evidence comparisons, falsifiable model checks, options and remaining uncertainties, with your own technical recommendation and independent validation responsibility. Ask the owner only for scope/priorities or genuinely unresolvable policy/physical-design choices. Never equate an owner's plan approval with verification of a source equation.

## 3. Key disputed questions — evidence before source-law edits

1. **Eq. 6.11 exponent:** The imported notebook currently computes `r2` using the **square** of `(1 + K_C2H2*p_C2H2 + K_C2H4*p_C2H4)`. Another reading of the original thesis reports a **first-power** denominator. **Do not declare either one source-faithful without reading the exact original equation and, if possible, its derivation/Appendix F implementation.** Preserve side-by-side interpretations and the actual effects on calculated rates/conversion/selectivity. Distinguish manuscript error, alternative fit and coding mistake as hypotheses.
2. **Eq. 6.9/6.10 and saturation:** Verify the full acetylene rate, its second-order adsorption factor and the capped `r1 = r1_raw / (1 + r1_raw/r1_max)`. Check how the distinct `(1+K_inh p_A)^{n_inh}` factor enters `r2`; do not invent a shared site denominator merely for symmetry.
3. **Volume-flow basis:** The existing notebook uses `F_total = (P_reactor * Q_inlet)/(R * T_reactor)` at 373.15 K for `flow_ml_min`. Does Larsen's source report *actual* volume or standardized flow (`mL/min`, `sccm`, STP definition or mass-flow controller)? Verify the applicable `T_ref,P_ref` explicitly before converting. Document a controlled sensitivity for ambiguous conventions.
4. **Units and normalization:** The source does not clearly specify units for all eight fitted coefficients. Verify any explicit source definitions; mark each inference as *inferred*, not established. Check pressure (Pa/bar/mbar), rate basis (mol/kgcat/s), catalyst-specific masses (Pd₀Ag 100 mg, Pd₂Ag 75 mg, Pd₃Ag 100 mg), tube diameter, support density and mass-normalized volume flow versus true reactor-volume GHSV. Do not claim source conversion/fit validation based only on plausible orders of magnitude.
5. **Data provenance:** Figure 6.6 contains the final eight-parameter vectors; standard-model Appendix E tables are **not** those final vectors. Figures 6.1–6.4 / Appendix A are experimental; B–D are simulated. Appendix F has an exact Pd₀Ag table; the branch's Pd₂Ag/Pd₃Ag selected curves are digitized estimates. Do not claim the full all-experiment RMSEs have been independently reproduced without original responses for all 41/42/41 experiments.

Separate the original thesis model, the pre-existing agent reproduction, any corrected source-faithful version, and optional alternate hypotheses. **No silent retuning to force better agreement.** The challenge is to establish what was actually published and fitted, not merely to generate attractive overlays.

## 3. Required deliverables AFTER plan review

1. `research/reports/larsen_2024_equation_and_baseline_audit.md` with exact page/equation/figure locators, provenance/units matrix, original-vs-alternative formula comparison, flow-reference assessment, test results, independent experimental comparison and unresolved source blockers. Explain whether the full thesis was actually read.
2. Update the on-branch `notebooks/benchmarks/larsen_2024_benchmark.ipynb` and only related derived CSVs **when a correction is warranted**. Keep the original source snapshot recoverable in Git, document what changed and why, and do not confuse a new fit with reproduction of Larsen's fitted model. Use the existing appendix renders without changing their raster contents.
3. Run source-based conversion/selectivity cases for all three catalyst designations. Compare exact Pd₀Ag table data against independently calculated values, digitized Pd₂Ag/Pd₃Ag points with their uncertainty, and published whole-dataset RMSE values **only as literature claims** when full response tables are unavailable. Verify element balances, units, rate denominators, solver BDF/Radau/tolerance sensitivity and flow conversion. State actual runtime and software environment.
4. Update `TODO.md` with true PASS/BLOCKED receipts (do not carry forward the old blanket `COMPLETED` banner as scientific validation), exact commit SHA and unresolved uncertainties.
5. Supply a concise handoff for Agent 5: which rate law and parameter/unit basis is defensible and what remains unknown before introducing hypothetical CO adsorption.

## 4. Ownership and historical record

This is **AI reference work only**, distinct from the owner's personal scientific knowledge map and own notebook. Keep derivations as research notes, not author-approved `index.md` or personal nodes. Later owner-facing study questions are tracked in the separate Q99–Q106 owner map queue.

**Historical note:** Earlier `GOAL.md` versions explicitly printed a squared `r2` denominator and proclaimed the selected-curve benchmark completed on 2026-10-25. That is preserved in Git history as previous work; this re-audit **does not pre-judge** whether the source formula or fitted units were reproduced correctly.
