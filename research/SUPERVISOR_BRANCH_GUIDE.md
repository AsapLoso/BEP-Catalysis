# BEP — what is on main, and what remains on other branches

**Supervisor-facing navigation draft · 1 November 2026**  
The purpose is to make **one starting point**, while keeping historical material available without implying it is a validated thesis. This guide is *not* a scientific result or a request for Damian to audit all the branches.

## A two-minute route

1. Start with the [root README](../README.md) and [notebook index](../notebooks/README.md).
2. The [author's own working notebook](../notebooks/unified_dynamic_reactor.ipynb) is a **four-cell conceptual sketch, not an executable reactor model**. It must not be presented as a completed thesis simulation.
3. The [V3](../notebooks/reference/v3/README.md) and [V4](../notebooks/reference/v4/README.md) notebooks are **reference implementations**, and the [Schbib/Larsen benchmarks](../notebooks/benchmarks/README.md) are attempts/audits with limitations. Their saved output does not prove the owner has checked or understood the results.
4. The [literature selection report](reports/isothermal_co_kinetics_source_selection.md) is an *AI-supported source screen*, not independently adopted as scientific truth. It did not identify a ready isothermal CO-dependent PFR benchmark under the particular screening criteria.
5. The next meaningful supervisor discussion is **which one literature source, measured operating point, comparison variable and modest modelling scope** should be tackled in an independently explainable Jupyter notebook.

## Optional branches (only if a specific question needs them)

| Branch / PR | Where to start | Why it is **not** silently merged into main |
| --- | --- | --- |
| [Personal map + viewer](https://github.com/AsapLoso/BEP-Catalysis/tree/migration/bep-map-consolidation-20261023) ([PR #1](https://github.com/AsapLoso/BEP-Catalysis/pull/1)) | Its [branch README](https://github.com/AsapLoso/BEP-Catalysis/blob/migration/bep-map-consolidation-20261023/README.md) links the owner map, AI reference maps and local viewer; there is also a [historical read-only HTML export](https://github.com/AsapLoso/BEP-Catalysis/blob/migration/bep-map-consolidation-20261023/research/manual_map_sessions_2026_10_22/owner_working_map/exports/BEP_owner_map_Damian_review_2026-10-23.html). | Map node placements, five understanding stages, unverified citations, approval boundaries and competing frontend imports require separate review. The viewer is **local/read-only**; a GitHub source link is not a hosted interactive page. |
| [Isothermal CO kinetics source-selection](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/isothermal-co-kinetics-source-selection) ([issue #12](https://github.com/AsapLoso/BEP-Catalysis/issues/12)) | [Report copied to main](reports/isothermal_co_kinetics_source_selection.md). | The evidence screen is already readable on main; the full research branch is not an approved kinetic model or owner-verified reproduction. |
| [Schbib benchmark source](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/schbib-co-benchmark) ([PR #15](https://github.com/AsapLoso/BEP-Catalysis/pull/15)) | [Benchmark index](../notebooks/benchmarks/README.md), [audit](reports/schbib_parameter_and_benchmark_audit.md). | The central notebook and report already appear on main. Additional saved plots/handoffs remain references; source parameter issues are unresolved. |
| [Larsen benchmark source](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/larsen-pdag-benchmark) ([PR #17](https://github.com/AsapLoso/BEP-Catalysis/pull/17)) | [Benchmark index](../notebooks/benchmarks/README.md), [audit](reports/larsen_2024_equation_and_baseline_audit.md). | Original thesis PDF, appendix renders and other provenance are large/branch-specific; the benchmark is restricted and does not include CO. |
| [Dynamic V4 branch](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/v4-dynamic-reactor) ([PR #14](https://github.com/AsapLoso/BEP-Catalysis/pull/14)) | [V4 snapshot on main](../notebooks/reference/v4/README.md). | The reference simulation is retained; extra agent handoffs are not necessarily needed to review one notebook or justify its physics. |
| [PdAg–CO synthesis handoff](https://github.com/AsapLoso/BEP-Catalysis/tree/feat/pdag-co-synthesis) ([PR #16](https://github.com/AsapLoso/BEP-Catalysis/pull/16)) | [Existing evidence index](../research/evidence/README.md). | Preliminary integration and reference output must not be presented as a validated PdAg+CO reactor. |
| [Archived AAPM planning](https://github.com/AsapLoso/BEP-Catalysis/tree/archive/aapm-bep-planning-maps-20261023) ([PR #2](https://github.com/AsapLoso/BEP-Catalysis/pull/2)) and [source map PR #26](https://github.com/AsapLoso/BEP-Catalysis/pull/26) | The archive branch's \`planning/README.md\`; PR #26's proposed \`planning/SOURCE_MAP.md\`. | Historical checklists and provenance are not the current task list, and should not clutter the supervisor tour. |
| [Large task backlog](https://github.com/AsapLoso/BEP-Catalysis/tree/bep-lossless-task-union-20261023) ([draft PR #7](https://github.com/AsapLoso/BEP-Catalysis/pull/7)) | PR description and preserved records. | Thousands of historic task occurrences are not an actionable one-week science plan. |

**Other preserved branches:** model variants, setup/Codespace work, guided science loop, map alignment and discussion audits. See the [technical branch triage](BRANCH_TRIAGE_2026_10_31.md) for their dispositions. Their existence is not evidence of completion or owner approval. The guide deliberately avoids dumping all 20+ branch names on Damian.

## Decision rule for future merges

- **Put on \`main\`:** a clear top-level guide, small verifiably useful scientific assets, source links, and independently checked/runnable notebook results *with accurate status and source provenance*.
- **Link but preserve outside \`main\`:** large PDFs and page renders, alternate versions, extensive AI maps, historical archives, competing node authority, experimental branches and internal process/audit discussions.
- **Never auto-promote:** personal understanding stages, unverified citation claims, AI hypotheses or simulations to human-approved, experimentally validated or supervisor-accepted status.
- **Before any import:** compare the candidate against the current main branch, identify *unique* relevant files, inspect deletions/conflicts and demonstrate what Damian can inspect afterwards. No broad merge simply because "main should have everything."
- **If optional branch lacks a clear README:** document the deficiency or add a tiny branch-local explanation separately. Do not claim every branch is already self-explanatory.

## What this guide does *not* do

It does not guarantee that a collaborator can access a private GitHub repository, that a browser can execute a local viewer, or that the older notebooks run on Damian's machine. It does not send an email. A simple directly runnable notebook and an actual supervisor discussion remain open scientific work.
