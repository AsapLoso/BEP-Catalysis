# Derived datasets and computational results

For processed/digitized/transformed values, simulation outputs and reproducibility receipts. Existing `notebooks/benchmarks/data/` and notebooks/figures keep their paths; index them here with source and generating code SHA rather than moving them in a bulk migration.

Record: original input locator, transformation/recalculation formula, units, uncertainty, stored-vs-newly-executed status, run environment, baseline comparison and what a result **does not validate**. Never label digitized or fitted values as raw experimental data.

## Current Schbib audit outputs

- [`schbib_1996_audit_results.json`](schbib_1996_audit_results.json): machine-readable extracted results and execution receipt, generated from the fresh executed notebook; source and correction status are encoded separately.
- [Audited PFR notebook](../../../notebooks/benchmarks/schbib_1996_steady_state.ipynb): freshly executed source-set and diagnostic comparisons.
- [Historical notebook snapshot](../../../notebooks/benchmarks/schbib_1996_steady_state_historical.ipynb): byte-preserved pre-audit notebook outputs.
- [Research report](../../reports/schbib_parameter_and_benchmark_audit.md): interpretation, acceptance gates, and uncertainty register.
