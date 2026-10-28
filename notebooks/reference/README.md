# Reactor notebook references

This folder contains implementations and proposals kept for comparison. The personal working notebook is [../unified_dynamic_reactor.ipynb](../unified_dynamic_reactor.ipynb). Edit that notebook by default; open a reference when a specific comparison is useful.

## Contents

- [v3/](./v3/) is the implemented V3 vertical slice, including its vendor engine and locked environment. Its scope and limitations are documented in [research/specs/v3/README.md](../../research/specs/v3/README.md).
- [v4/](./v4/README.md) is the reserved location for a future V4 reference notebook. The notebook has not been implemented in this checkout; its planning map is [bep_v4_reactor_model.md](../../research/wayfinder/bep_v4_reactor_model.md).
- [legacy/](./legacy/) contains the older inline transient model and its Python scaffold copy.
- [ai/](./ai/) contains an explicitly labeled AI proposal. Treat it as a comparison prompt, not scientific validation.
- [snapshots/](./snapshots/) contains saved drafts with incomplete provenance; they are retained for comparison.

Historical V1 and V2 dynamic-response runs are grouped under [../benchmarks/](../benchmarks/README.md), since they are source-based benchmark snapshots rather than current implementations.

## Reference discipline

Saved notebook outputs show what was present in those snapshots. They do not establish that the notebooks run in this repository, reproduce a paper, or validate the BEP model. Check each artifact's source and assumptions before reusing equations or parameters.
