# BEP branch triage — 31 October 2026

**Purpose:** prevent branch proliferation from blocking a short supervisor handoff or the next scientific notebook. This is a *disposition*, not automatic authorization to merge or delete anything.

## Verified current default

- `main` now includes the scientific workspace formerly isolated on `unified-reactor-model` (merged PR #28) and the bounded CO-source-selection report.
- Entry point for Damian: root `README.md`. It explicitly states that `notebooks/unified_dynamic_reactor.ipynb` is a four-cell conceptual sketch, **not executable**. V3/V4, Schbib and Larsen are references/audits, not owner-approved thesis results.
- The isothermal CO-sensitive PFR source screen concluded **NO SOURCE READY**. Do not reopen a general search without a targeted missing-evidence question.

## Disposition by action

| Priority | Branches / PRs | Action now |
| --- | --- | --- |
| DONE — preserve | `unified-reactor-model`, merged #28; `docs/bep-guided-science-loop-20261029`, `docs/bep-proactive-execution-handoff-20261029` | Core scientific content and workflow documentation have landed on `main`. Keep historical branches; no further import required for supervisor review. |
| NOW — scientific evidence only | `feat/isothermal-co-kinetics-source-selection` (#12 issue, source report), `feat/gobbo-steady-state-benchmark` | The CO-selection report is now copied verbatim to `main`. Gobbo remains a separate candidate/source: only inspect if it closes the chosen benchmark's evidence gap. |
| REFERENCE — selective later import | `feat/schbib-co-benchmark` (#15), `feat/larsen-pdag-benchmark` (#17), `feat/v4-dynamic-reactor` (#14), `feat/pdag-co-synthesis` (#16), `integrate/agent1-agent4-into-agent5-20261025`, `feat/v3-coupled-reactor`, `feat/unified-reactor-v3-public` | Main already contains the central model/benchmark notebooks. Remaining differences include plots, rendered pages, handoff files and old layouts; **no wholesale merge** without a unique scientific reason. PdAg+CO synthesis is not validated. |
| TOOLING — postpone | `setup/codespaces-bep-python-codex` (draft #13) | The documented environment path predates the current `notebooks/reference/v3` layout. Fix when an actual reproducible notebook execution requires it. |
| HISTORY / KNOWLEDGE TRANSFER — postpone | `archive/aapm-bep-planning-maps-20261023` (#2), `codex/bep-source-map-archive-20261029` (#26), `bep-lossless-task-union-20261023` (draft #7), `migration/bep-map-consolidation-20261023` (draft #1), `feat/personal-map-alignment` | Preserve evidence and personal-map authority without merging historical AAPM snapshots or the 2,471-cluster backlog into the current science plan. This is reference information, not a weekly task list. |
| DOCS ONLY — review before close | `codex/bep-guided-workflow-main-20261029` (#25), `docs/supervision-conversation-audit-20261029` (draft #27) | #25 may contain small link repairs vs current main: compare the actual diff, then take only missing corrections. #27 concerns discussion analysis, not science handoff. Neither is a prerequisite for Damian. |

## A bounded sorting-agent task

1. Compare **each remaining branch against current `main`**, not a stale `unified-reactor-model` base; record only unique scientific assets, with source commit and file path. Ignore documentation duplication.
2. For any proposed import, state what *concrete owner-facing result* it enables (e.g. a specific reproducible measured point). Mark **KEEP AS REFERENCE** otherwise.
3. Do not delete branches, close PRs, move owner-map nodes, change scientific assumptions or merge large PDFs/figures without separate evidence and explicit permission.
4. Deliver one compact table with **IMPORT EXACT PATH / KEEP REFERENCE / SUPERSEDED / NEEDS OWNER DECISION**. At most three import candidates; implement only genuinely approved small scientific fixes.

**Stop condition:** the supervisor can find the current notebooks and their limitations in two clicks, and the author has a single next scientific checklist item. No need to process every archived task occurrence to achieve that.
