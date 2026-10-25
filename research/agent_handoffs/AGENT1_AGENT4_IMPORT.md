# Agent 1 + Agent 4 reference import for Agent 5

This directory records a **file-level Git blob import** into `feat/pdag-co-synthesis` for exploratory PdAg + CO research. The two independent benchmarks are **reference evidence**; their equations, fitted parameters and plots are not automatically applicable to the combined catalyst. No source was adapted or revalidated by this import.

## Source refs and imported data
- Agent 1 Schbib steady-state benchmark: `feat/schbib-co-benchmark` at `88e44ebb781f3b9ad661f8a42102b936b3ed68dc`.
  - `notebooks/benchmarks/schbib_1996_steady_state.ipynb` and four `schbib_fig*.png` outputs.
  - Original Agent 1 contract in `research/agent_handoffs/agent-1-schbib/{GOAL,TODO}.md`.
  - Schbib's source HTML/PDF/text already existed in the target branch under `research/literature/`; this integration does not overwrite them.
- Agent 4 Larsen PdAg benchmark: `feat/larsen-pdag-benchmark` at `c084fe953a60c7135a504d09f9e04ae74610de7f`.
  - `notebooks/benchmarks/larsen_2024_benchmark.ipynb`, `notebooks/benchmarks/data/larsen_2024_{parameters,selected_curves}.csv`.
  - `notebooks/benchmarks/source_renders/appendix_pages/`: README and 18 PNG page renders (pp. 71–88 of the upstream thesis).
  - Original Agent 4 contract in `research/agent_handoffs/agent-4-larsen/{GOAL,TODO}.md`.

## Reproducibility and interpretation
- These are **unaltered Git blobs**, including any existing notebook outputs. The import did not rerun or validate either notebook.
- The full Larsen primary thesis **is not added**: appendix screenshots and digitized/derived CSVs do not replace source verification against the full thesis. Check access to the original thesis separately; label unavailable verification.
- The Larsen notebook accesses relative `data/` paths; run it with the working directory `notebooks/benchmarks/` (or adjust the launch environment without changing the source).
- The two branches have different reactor and kinetic bases. Before combining models, verify parameter units, catalyst domains, adsorption assumptions, benchmark quality and whether the CO term can predict differential inhibition. A shared denominator can cancel in instantaneous rate ratios.
- **Do not merge the two branches wholesale**: their root `GOAL.md`/`TODO.md` have branch-specific meanings, and their histories contain unrelated V3 deletions. The target's root `GOAL.md`/`TODO.md` remain the authority for Agent 5.
- **No owner approval** of the combined kinetic hypothesis, personal map or personally authored notebook is implied.

Source pointers: https://github.com/AsapLoso/BEP-Catalysis/tree/feat/schbib-co-benchmark and https://github.com/AsapLoso/BEP-Catalysis/tree/feat/larsen-pdag-benchmark
