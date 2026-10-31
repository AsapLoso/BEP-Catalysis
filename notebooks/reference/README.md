# Reactor notebook references

This folder contains implementations and proposals kept for comparison. The personal working notebook is [../unified_dynamic_reactor.ipynb](../unified_dynamic_reactor.ipynb). Edit that notebook by default; open a reference when a specific comparison is useful.

## Contents

- [v3/](./v3/) is the implemented V3 vertical slice, including its vendor engine and locked environment. Its scope and limitations are documented in [research/specs/v3/README.md](../../research/specs/v3/README.md).
- [v4/](./v4/README.md) contains the imported V4 dynamic CO notebook, its builder, and an isolated copy of the engine used by that branch.
- [legacy/](./legacy/) contains the older inline transient model and its Python scaffold copy.
- [ai/](./ai/) contains an explicitly labeled AI proposal. Treat it as a comparison prompt, not scientific validation.
- [snapshots/](./snapshots/) contains saved drafts with incomplete provenance; they are retained for comparison.

Historical V1/V2 dynamic-response runs and literature benchmark work are indexed under [../benchmarks/](../benchmarks/README.md).

## Reference discipline

Saved notebook outputs show what was present in those snapshots. They do not establish that the notebooks run in this repository, reproduce a paper, or validate the BEP model. Read each artifact's README and audit report before reusing equations or parameters.
