# BEP V3 source manifest

**Status:** Primary model-source inventory is blocked pending the missing `BEP_V3_GOAL.md`. No source snapshot or source SHA has been guessed.

## Working base

| Item | Value |
|---|---|
| Repository | `AsapLoso/BEP-Catalysis` |
| V3 branch | `v3/bep-vertical-slice-20261023` |
| Base ref requested | `migration/bep-map-consolidation-20261023` |
| Verified base commit | `6803814cd827e4f91323fa7b6f406eea579b286b` |
| Goal file | `notebooks/v3/GOAL.md` — not available in the mounted workspace or target branch |

## Required source artifacts

The mission prompt identifies five artifacts. Their exact upstream refs and paths are specified only by the unavailable goal. These rows remain unresolved until that file is supplied.

| ID | Required artifact | Upstream ref / path | Immutable snapshot | Source commit / blob SHA | Status / notes |
|---|---|---|---|---|---|
| S1 | V0 `.py` model | Unknown | Not created | Unknown | Awaiting goal; do not infer model or parameter details. |
| S2 | Migrated legacy notebook | Unknown | Not created | Unknown | Awaiting goal. |
| S3 | V1 notebook | Unknown | Not created | Unknown | Shares a filename with V2 on a different ref; ref identity must be preserved. |
| S4 | V2 notebook | Unknown | Not created | Unknown | Shares a filename with V1 on a different ref; ref identity must be preserved. |
| S5 | BEP presentation / explanatory notebook | Unknown | Not created | Unknown | The mission identifies this as an explanatory example, not an independently validated simulator. |

## Read-only map context recorded at the base commit

These are provenance inputs for later theory and coverage mapping. They are not model-source snapshots, scientific validation, or evidence that the owner understands a concept.

| Dataset | Path at base | Git blob SHA | Read status / boundary |
|---|---|---|---|
| Integrated AI reference map | `research/integrated_reference_map_2026_10_22/nodes.yaml` | `ff508ddf167296a73a4843a9a68ff82b9ddb0037` | Overview and targeted reactor/transport context read. AI-authored; its maturity ceiling is `ai_worked_out`. |
| Owner personal map snapshot | `research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml` | `8a9b7fda318849ad6369cf2e75899a3969290f64` | Read-only. Current snapshot has 50 live nodes. The Reactor Model proposal is queue-only under Q92; no personal-map change is authorized by this task. |

## Snapshot protocol after the goal is restored

For each source row, record the repository, exact ref, source path, resolved commit SHA, blob SHA, byte size, and snapshot destination before analysis. Preserve V1 and V2 as distinct source objects even if their filenames match. Keep the source snapshots immutable; create the sixth, synthesized artifact separately as `notebooks/v3/bep_v3_vertical_slice.ipynb` only after the theory map and model blueprint are complete.
