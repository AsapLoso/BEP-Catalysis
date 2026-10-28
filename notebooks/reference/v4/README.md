# V4 dynamic reactor reference

This is an imported reference snapshot from the `feat/v4-dynamic-reactor` branch at commit [18cba29](https://github.com/AsapLoso/BEP-Catalysis/tree/18cba29e1c5832e860dde8446c0851ad2175cdd9/notebooks/v4). The personal working notebook remains [../../unified_dynamic_reactor.ipynb](../../unified_dynamic_reactor.ipynb).

## Contents

- [unified_v4_dynamic_reactor.ipynb](./unified_v4_dynamic_reactor.ipynb) contains the saved V4 notebook snapshot.
- [build_notebook.py](./build_notebook.py) regenerates the notebook alongside the script.
- [vendor/pbr/](./vendor/pbr/) is the V4 branch's engine snapshot. It is kept separate from [../v3/](../v3/) so V4 work cannot replace the V3 reference engine.

## Model scope and limits

V4 advances gas concentrations and surface coverages as dynamic states, includes CO in the gas and surface states, and uses a finite-volume inlet with periodic CO forcing. The notebook's dynamic surface relaxation time is an exploratory assumption because the cited source does not provide elementary adsorption/desorption rates. The branch also interprets an ambiguous logarithm convention as base 10. These are model choices recorded by the source notebook, not owner-approved assumptions.

The notebook's saved outputs came from the feature branch. They have not been rerun after import into the central branch and do not establish experimental validation or a Pareto improvement. Compare its source assumptions with the separate Schbib audit at [research/reports/schbib_parameter_and_benchmark_audit.md](../../../research/reports/schbib_parameter_and_benchmark_audit.md).

The source branch environment manifest does not declare pandas even though the notebook imports it. Review the runtime dependencies before executing this snapshot. The builder also replaces the notebook file when run, so retain a copy first if the saved outputs matter.
