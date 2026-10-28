# Notebook benchmarks

This folder contains benchmark notebooks and saved benchmark snapshots. Keep each notebook beside a short note identifying its source, version, saved-output status, and whether it has actually been rerun in this checkout.

## Historical dynamic-response snapshots

| Folder | Notebook | Source snapshot |
|---|---|---|
| [v1/](./v1/) | `bep_dynamic_reactor_response.ipynb` | [Methanol-Catalysis commit `791e51c0eba11f4bd5095f48d0520c6af317f5f8`](https://github.com/AsapLoso/Methanol-Catalysis/blob/791e51c0eba11f4bd5095f48d0520c6af317f5f8/notebooks/bep_dynamic_reactor_response.ipynb) |
| [v2/](./v2/) | `bep_dynamic_reactor_response.ipynb` | [Methanol-Catalysis commit `2ee0dc1a84529d6830dcc628fc771878907fb22c`](https://github.com/AsapLoso/Methanol-Catalysis/blob/2ee0dc1a84529d6830dcc628fc771878907fb22c/notebooks/bep_dynamic_reactor_response.ipynb) |

These are historical literature-reproduction attempts. Their saved outputs were preserved from their source commits; they have not been freshly validated in this checkout. Their code uses the upstream `pbr` package. See [the V3 source manifest](../../research/specs/v3/SOURCE_MANIFEST.md) for pinned provenance and limitations.

## Literature benchmark work

| Study | Notebook and support | Audit record | Scope/status |
|---|---|---|---|
| Schbib (1996) | [steady-state audit](./schbib_1996_steady_state.ipynb), [historical snapshot](./schbib_1996_steady_state_historical.ipynb), [extent cross-check](./schbib_1996_extent_crosscheck.py) | [report](../../research/reports/schbib_parameter_and_benchmark_audit.md) | Table 6 reproduction for both reported species remains blocked; the report distinguishes source-faithful parameters from an author-shared but visually unverified correction. |
| Larsen (2024) | [historical benchmark](./larsen_2024_benchmark.ipynb), [source audit](./larsen_2024_source_audit.ipynb), [data](./data/) | [report](../../research/reports/larsen_2024_equation_and_baseline_audit.md) | Restricted selected-row audit, not a full refit; source conventions and several data discrepancies remain unresolved. It does not model CO. |

These are separate source studies and must not be combined into one parameter set or treated as a single validated reactor model. The notebooks retain their branch outputs; they have not been rerun after import to this branch.

The Schbib source files are archived in [research/literature/](../../research/literature/). The Larsen thesis PDF and page renders remain on its source branch because they are large binary artifacts: [Larsen branch snapshot](https://github.com/AsapLoso/BEP-Catalysis/tree/adf33269fadc2a70891a144ed6dd86f25c58db25/research/evidence/original).

The imported work came from [feat/schbib-co-benchmark](https://github.com/AsapLoso/BEP-Catalysis/tree/777eac20c6f4874a784c2831fa43fb3c18710ab7/notebooks/benchmarks) and [feat/larsen-pdag-benchmark](https://github.com/AsapLoso/BEP-Catalysis/tree/adf33269fadc2a70891a144ed6dd86f25c58db25/notebooks/benchmarks). Those feature branches remain available for continued work.
