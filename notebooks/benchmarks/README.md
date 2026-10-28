# Notebook benchmarks

This folder contains benchmark notebooks and saved benchmark snapshots. Keep each notebook beside a short note identifying its source, version, saved-output status, and whether it has actually been rerun in this checkout.

## Historical dynamic-response snapshots

| Folder | Notebook | Source snapshot |
|---|---|---|
| [v1/](./v1/) | `bep_dynamic_reactor_response.ipynb` | [Methanol-Catalysis commit `791e51c0eba11f4bd5095f48d0520c6af317f5f8`](https://github.com/AsapLoso/Methanol-Catalysis/blob/791e51c0eba11f4bd5095f48d0520c6af317f5f8/notebooks/bep_dynamic_reactor_response.ipynb) |
| [v2/](./v2/) | `bep_dynamic_reactor_response.ipynb` | [Methanol-Catalysis commit `2ee0dc1a84529d6830dcc628fc771878907fb22c`](https://github.com/AsapLoso/Methanol-Catalysis/blob/2ee0dc1a84529d6830dcc628fc771878907fb22c/notebooks/bep_dynamic_reactor_response.ipynb) |

These are historical literature-reproduction attempts. Their saved outputs were preserved from their source commits; they have not been freshly validated in this checkout. Their code uses the upstream `pbr` package. See [the V3 source manifest](../../research/specs/v3/SOURCE_MANIFEST.md) for pinned provenance and limitations.

## New benchmark work

The [Wayfinder plan](../../research/wayfinder/bep_v4_reactor_model.md) proposes additional Schbib and Larsen benchmark notebooks. Those notebooks and data do not exist here yet; add them when the benchmark work is carried out and document their source and verification status.
