# Evidence index

This folder keeps source-faithful transcriptions, research analyses, and derived outputs separate. An imported branch artifact is not an owner-approved model assumption or proof of experimental validation.

## Imported reactor work

- **V4 dynamic reactor:** [notebook reference](../../notebooks/reference/v4/README.md), imported from [feat/v4-dynamic-reactor at 18cba29](https://github.com/AsapLoso/BEP-Catalysis/tree/18cba29e1c5832e860dde8446c0851ad2175cdd9/notebooks/v4). Its dynamic surface-relaxation time and logarithm convention remain assumptions recorded by that notebook.
- **Schbib (1996):** [benchmark report](../reports/schbib_parameter_and_benchmark_audit.md), [transcriptions](./transcriptions/), [derived results](./derived/schbib_1996_audit_results.json). The printed parameter set does not reproduce the reported acetylene conversion; the author-shared alternative is not visually verified and still does not reproduce both reported species.
- **Larsen (2024):** [benchmark report](../reports/larsen_2024_equation_and_baseline_audit.md), [transcriptions](./transcriptions/), [derived tables](./derived/). The audit is a restricted selected-row comparison, not a full fit reproduction, and it does not model CO.

The source branches remain available: [Schbib](https://github.com/AsapLoso/BEP-Catalysis/tree/777eac20c6f4874a784c2831fa43fb3c18710ab7), [Larsen](https://github.com/AsapLoso/BEP-Catalysis/tree/adf33269fadc2a70891a144ed6dd86f25c58db25), and [V4](https://github.com/AsapLoso/BEP-Catalysis/tree/18cba29e1c5832e860dde8446c0851ad2175cdd9). Their feature branches were not modified by this import.

## Evidence classes

- [original/](./original/): links to primary source files. The Schbib paper is archived under [research/literature](../literature/). The Larsen thesis PDF and 18 page renders are large binary files retained on its source branch; see [the original-source index](./original/README.md).
- [transcriptions/](./transcriptions/): readable source excerpts, tables, and working transcriptions. Each file states its verification limits.
- [analysis/](./analysis/): independent derivations and source comparisons.
- [derived/](./derived/): processed tables and machine-readable calculation results, not raw measurements.
- [reports/](../reports/README.md): consolidated findings and unresolved gates.

Notebook outputs and previous branch execution receipts are historical snapshots. No notebook was rerun as part of importing these references into the central branch.
