# BEP-Catalysis

Bachelor End Project research on acetylene semi-hydrogenation in a packed-bed reactor, with a proposed focus on carbon-monoxide-dependent selectivity and periodic operation.

## Start here: notebook and evidence status (31 October 2026)

This is a **research workspace**, not a validated, ready-to-run final thesis model. Source transcriptions, saved notebook outputs, proposed physics, and the author's own implementation must not be confused.

| Material | Where | Status |
| --- | --- | --- |
| **Author's working notebook** | [notebooks/unified_dynamic_reactor.ipynb](notebooks/unified_dynamic_reactor.ipynb) | Early four-cell conceptual sketch with pseudocode; **not a runnable reactor simulation**. This is the notebook the author intends to develop. |
| **V3 reference implementation** | [notebooks/reference/v3/](notebooks/reference/v3/) | Historical executed gas-phase transient/PSSA vertical slice with a pinned environment, numerical checks and important source-model limitations. **Reference, not independent thesis validation**. |
| **V4 reference** | [notebooks/reference/v4/](notebooks/reference/v4/) | Separate dynamic CO model snapshot; not promoted to the owner's implementation. |
| **Schbib (1996) benchmark** | [notebooks/benchmarks/](notebooks/benchmarks/README.md) and [audit](research/reports/schbib_parameter_and_benchmark_audit.md) | Reproduction remains unresolved for the reported species; do not cite it as validated PFR performance. |
| **Larsen (2024) benchmark** | [notebooks/benchmarks/](notebooks/benchmarks/README.md) and [audit](research/reports/larsen_2024_equation_and_baseline_audit.md) | Restricted benchmark audit, unresolved data conventions; **does not model CO**. |

**Immediate scientific gap:** there is currently no demonstrated, experimentally matched, fixed-temperature CO-sensitive PFR benchmark ready to serve as the thesis foundation. The [source-selection report](research/reports/isothermal_co_kinetics_source_selection.md) records an evidence-screened **NO SOURCE READY** result. Bos (1993) supplies a CO-sensitive rate-law candidate but its measurements use a Berty reactor; applying that law in a PFR is a model transfer, not reproduction of Bos's reactor.

## A short route for supervisor review

1. See the [23 October supervisor meeting directions](research/notes/meetings/2026-10-23_supervisor_meeting.md): reproducible steady-state literature benchmark first; only then dynamic/periodic CO operation.
2. Open the [notebook index](notebooks/README.md), then the author's early notebook and relevant reference notebooks **separately**. The V3 [model assumptions and receipts](research/specs/v3/README.md) are documented; they do not establish a finished thesis.
3. Review the [Schbib](research/reports/schbib_parameter_and_benchmark_audit.md) and [Larsen](research/reports/larsen_2024_equation_and_baseline_audit.md) audits before trusting parameter values or generated plots.
4. Agree on a **specific paper, one observable quantity and one reproducible operating point**, then implement and verify that minimal steady-state case in a clean notebook.

The [V3 Damian handoff](research/specs/v3/DAMIAN_HANDOFF.md) is a historical **draft for owner review**, not a sent communication or a statement of approval. No fresh model execution or scientific verification is claimed by this README update.

For deeper project navigation use the [research index](research/README.md) and [model structure notes](Structure.md). Agent/mapping workflows live under `.agents/` and are not prerequisite reading for reviewing a scientific notebook.
