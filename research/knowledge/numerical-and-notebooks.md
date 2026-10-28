# Numerical implementation and notebook history

## Legacy transient scaffold

The September 2026 AAPM record describes a Method-of-Lines scaffold with 20 axial positions and 10 radial positions, totaling 1,480 ODE components, integrated with BDF. Its kinetic constants were deliberately zero. The saved run therefore did not demonstrate reacting or periodic reactor behavior.

The dated audit records implementation defects including mutation of the solver state, a spherical-center coefficient of 3 where its analytic check gives 6, a frozen surface-coverage shell, and a particle-rate quadrature reported about 16% low on the tested grid. The separate framework audit records equation and closure conflicts. These are historical audit findings for that scaffold; they are not asserted here as defects in every later notebook.

## Notebook and model branches

| Record | What the existing index says | Evidence boundary |
|---|---|---|
| Methanol-Catalysis transient notebook | The local notebook has 11 cells, 5 code and 6 markdown, and describes the legacy MOL model | It was inspected structurally here and not executed |
| V1 and V2 dynamic-response snapshots | Pinned to Methanol-Catalysis commits `791e51c0eba11f4bd5095f48d0520c6af317f5f8` and `2ee0dc1a84529d6830dcc628fc771878907fb22c` | Saved outputs are historical and were not freshly rerun in the current repository branch |
| V3 vertical slice | Has a source manifest and a verification handoff; the V3 wayfinder marks it superseded by V4 | Source transcription, unit checks, and model-output reproduction are separate gates |
| V4 dynamic reactor | The October 28 local `unified-reactor-model` ref has a V4 wayfinder and notebook references, including a CO-modulation objective | This consolidation did not run the notebook or independently validate its scientific claims |
| Literature benchmarks | Schbib and Larsen have separate notebooks, data and audit records | The benchmark README says imported snapshots were not rerun and must not become one shared parameter set |

The [benchmark index](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/notebooks/benchmarks/README.md) identifies the Schbib Table 6 all-species reproduction as blocked and the Larsen audit as a restricted selected-row review. The [model verification milestones](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/notes/model_verification_milestones.md) distinguish component algebra checks and source transcription from full-model convergence, published-result reproduction, matched experimental comparison, and independent validation.

## Verification hierarchy preserved

1. A source transcription receipt does not prove the code reproduces the source output.
2. Algebraic or unit checks do not prove a complete coupled reactor prediction.
3. Numerical convergence does not prove agreement with matched experimental data.
4. Fitting a source dataset does not establish independent predictive performance.
5. A saved notebook output is historical evidence until the current code, environment, and run are checked.

No numerical receipt is added here. The source reports and notebooks remain the correct starting points for a later verification review.
