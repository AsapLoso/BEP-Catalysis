# Agent 5 — next integration PR gate (preparation only, 2026-10-25)

**STATUS: NOT AUTHORIZED FOR SCIENTIFIC COUPLING.** This is a handoff and proposed PR procedure, not a PR or a merge. The main Agent 5 contracts are [GOAL.md](../../GOAL.md), [TODO.md](../../TODO.md), and [issue #8](https://github.com/AsapLoso/BEP-Catalysis/issues/8).

## Dependency chain

1. Agent 1 works solely on `feat/schbib-co-benchmark`, per [issue #10](https://github.com/AsapLoso/BEP-Catalysis/issues/10). Required: a documented Schbib source/correction audit, table-of-kinetics provenance, dimensional checks, actual Table 6 reproduction or honestly blocked outcome, report and executed notebook. A **public author-shared Table 8 correction** is a specific lead; journal-erratum status and corrected constants need independent source verification. Keep the earlier imported Schbib notebook as historical evidence.
2. Agent 4 works solely on `feat/larsen-pdag-benchmark`, per [issue #11](https://github.com/AsapLoso/BEP-Catalysis/issues/11). Required: verification of Eq. 6.9–6.11 and flow/parameter units, reproducibility/measurement comparisons, readable source-faithful transcriptions of Appendix E/F PDF pages 71–88 (from the **already committed** images), and report/notebook. The source thesis PDF is separate in the owner's Zotero archive and **not presumed accessible remotely**.
3. **Owner / assistant review:** check audit evidence, source accessibility, unresolved uncertainties, source laws, tests and exact agent commit SHAs. Approve the scientific direction and integration scope, **not automatically the accuracy of every parameter as personal understanding**.
4. **Only then draft a targeted PR** from a new temporary integration branch into `feat/pdag-co-synthesis` importing precisely inspected corrected reference artifacts. **Create the PR; do not automatically merge it**. The owner decides what to import, and whether to merge.
5. After integration approval, and separately after the owner's explicit **go**, agent 5 may begin independently investigating combined PdAg + CO hypotheses. No old goal/prompt grants immediate permission.

## Why the next PR is not a whole-branch merge

PR #9 already imported A1/A4's previous notebooks, Larsen CSVs and source image renders into this branch. These are **historical snapshots** and don't update when their originating branches change. The new audits may contradict old equations/units. A whole-branch merge risks taking unrelated V3 ancestry, overwriting root `GOAL.md`/`TODO.md` and concealing model-version differences.

Prefer new, version-named **audited** reference locations (for example `notebooks/reference/a1_schbib_audited/` and `notebooks/reference/a4_larsen_audited/` with their requisite data, original source references and runnable instructions). Do not silently overwrite `notebooks/benchmarks/schbib_1996_steady_state.ipynb` or `notebooks/benchmarks/larsen_2024_benchmark.ipynb` until the owner has reviewed the diff. Another option is retaining source branch commits and explicitly duplicating only approved artifacts under evidence snapshots. If code depends on relative `data/` paths, make the new references executable without modifying historical notebooks.

**PR acceptance checklist:** clear comparison against Agent 5 current HEAD; exact source branch SHA and files; no unrelated file deletion/overwrite; correct GOAL/TODO preserved; explanatory provenance README and source-access table; reviewed source equations vs copied code; reproducibility environment and test receipts; unresolved science stated. Disallow force-push/PR auto-merge.

## Persistent evidence layout on all five branches

`research/evidence/original/` for unchanged originals + source links; `research/evidence/transcriptions/` for page-indexed readable source text with visual-check status; `research/evidence/analysis/` for AI scientific interpretation; `research/evidence/derived/` for processed data and numerical outputs. Existing historical source paths are unchanged; layer labels do **not** confer validation or owner knowledge.

The owner's separate map queue Q99–Q106 contains future science-learning questions. Scientific audits are **reference works**; they do not update human-owned map nodes or personal notebook text.
