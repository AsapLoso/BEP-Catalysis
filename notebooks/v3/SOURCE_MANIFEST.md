# BEP V3 source manifest

**Core inventory:** five inputs = four original notebooks plus one Python script. All five snapshots are read-only source records under `sources/`; no input was edited. Their Git blob IDs were recomputed from downloaded bytes and match the recorded upstream blobs.

## Target branch and base

| Item | Verified value |
|---|---|
| Target repository | `AsapLoso/BEP-Catalysis` |
| Working branch | `v3/bep-vertical-slice-20261023` (already existed locally; preserved) |
| Initial V3 checkpoint | `08967eaed47febdf597ebb60f48e6184cbab75bc` |
| Requested base | `migration/bep-map-consolidation-20261023` |
| Verified base commit | `6803814cd827e4f91323fa7b6f406eea579b286b` |
| Current remote branch state checked | Migration branch still at `6803814...`; no remote V3 branch exists. No push or PR attempted. |

## Immutable core inputs

| ID | Role and source limitation | Upstream origin | Source commit / blob SHA / bytes | Snapshot |
|---|---|---|---|---|
| S1 | V0 Python Method-of-Lines scaffold; all kinetic constants are zero placeholders and its audit lists numerical defects. | `AsapLoso/project-management-agents`, `devcontainer`, `Academics/BEP/Catalysis/3_Model/c2h2_hydrogenation_transient_model.py` | commit `598de520c7d4fa8cb9dacc58b18b85919e302ef0`; blob `eeb8dce1df58fd250c80aaeada85081e9ba8f4c0`; 10,338 bytes | [`S1_v0_python_598de52.py`](sources/S1_v0_python_598de52.py) |
| S2 | Migrated legacy notebook; same 1,480-state model and zero-rate elementary placeholders as V0, not an independent kinetic model. | `AsapLoso/Methanol-Catalysis`, `main`, `content/c2h2_hydrogenation_transient_model.ipynb` | commit `b62794500ed966b27bb521bf1d5e600994a899c3`; blob `9fba7f8d93f5257200997b04ecdf17688c0bb162`; 33,885 bytes | [`S2_migrated_legacy_main_b627945.ipynb`](sources/S2_migrated_legacy_main_b627945.ipynb) |
| S3 | V1 dynamic-response notebook; saved exploratory outputs, uses the upstream `pbr` package, PSSA chemistry and assumed/borrowed pellet/reactor inputs; no target calibration or experiment validation. | `AsapLoso/Methanol-Catalysis`, `feat/bep-dynamic-reactor-response-notebook` (PR #1 snapshot), `notebooks/bep_dynamic_reactor_response.ipynb` | commit `791e51c0eba11f4bd5095f48d0520c6af317f5f8`; blob `44614ff57b62418f5767d8f337ed42c00737eb3a`; 2,355,722 bytes | [`S3_v1_dynamic_response_791e51c.ipynb`](sources/S3_v1_dynamic_response_791e51c.ipynb) |
| S4 | V2 revision of the same path as V1, separately pinned; saved outputs and a V2 handoff report a run, but do not demonstrate a paper-matched reactor reproduction, target calibration or experiment validation. | `AsapLoso/Methanol-Catalysis`, `feat/bep-dynamic-reactor-response-v2` (PR #2 snapshot), `notebooks/bep_dynamic_reactor_response.ipynb` | commit `2ee0dc1a84529d6830dcc628fc771878907fb22c`; blob `87d4a3a6681ebb6cffac07923e20fc226aeb5683`; 2,951,774 bytes | [`S4_v2_dynamic_response_2ee0dc1.ipynb`](sources/S4_v2_dynamic_response_2ee0dc1.ipynb) |
| S5 | BEP explanatory/presentation notebook. It has a spatial-state narrative, grid illustration and a separate inert-tracer example; that example is not the BEP kinetic simulator and not model validation. | `AsapLoso/project-management-agents`, `devcontainer`, `Academics/BEP/Catalysis/presentation/BEP_Catalysis_Presentation_v1.ipynb` | commit `598de520c7d4fa8cb9dacc58b18b85919e302ef0`; blob `9932424ffb1c2339b6e446f6987c9454e4c5cb9c`; 86,692 bytes | [`S5_presentation_598de52.ipynb`](sources/S5_presentation_598de52.ipynb) |

The current `project-management-agents/devcontainer` tip reported by `git ls-remote` is `cc24b831f0d6e71f2f2ec13f829787b29d6dd27e`; the pinned S1/S5 content comes from the exact older commit listed above, not an assumption that the current tip is identical. The live V1/V2 branch tips matched the pinned commits when checked on 2026-10-23.

## Supporting V0 and map context

- V0 implementation audit: `project-management-agents/Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md`; code defect ledger and execution state: `3_Model/state.md`. These are audit records, not independent physical source papers. The audit itself flags paper-excerpt claims as unverified; do not promote them to primary-source evidence without a cited source locator.
- Integrated AI reference map at the V3 base: `research/integrated_reference_map_2026_10_22/`; `nodes.yaml` blob `ff508ddf167296a73a4843a9a68ff82b9ddb0037`. AI-authored, maturity ceiling `ai_worked_out`; no human understanding or human citation verification asserted.
- Personal map snapshot at the V3 base: `research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml` blob `8a9b7fda318849ad6369cf2e75899a3969290f64`. Read-only. Q92 and the 2026-10-23 owner-review handoff say the proposed Reactor Model assumptions were withdrawn to queue/archive; do not create or infer personal-map approval from V3.

## V2 engine and rerun provenance

V2 support code and tests were read from the exact S4 commit. The V2 `pbr/` package has no install metadata; its upstream `pixi.toml` imports the repository-root package by `PYTHONPATH="."`. V3 does not depend on an external checkout or that private path. The exact V2 `pbr/` package is vendored under `notebooks/v3/vendor/pbr/`; all 11 copied Python files were re-hashed and match their S4 commit blobs. No vendor source file was edited. V3 selects the Uniform radial closure, so the builder receives zero diffusivity sentinels that the RHS does not read; these are not physical parameter estimates. `vendor/README.md` documents this closure and the upstream `K₁` comment that V3 does not treat as resolving the primary-source discrepancy.

| V2 file | Source blob SHA |
|---|---|
| `pbr/__init__.py` | `8a714a94a8526edc65f16c93728f2aaf43926a21` |
| `pbr/chemistry.py` | `ebe23da668d64b5e44a837fc36f6fdc7fb0cf6ec` |
| `pbr/closures.py` | `aa12b22a072fe0e6c93be72101f411b2c514c4ec` |
| `pbr/discretisation.py` | `7850b51cad78ad6aa00476302efae8a14abfd8f8` |
| `pbr/model.py` | `7968e36241f657e88b162739baafe718d00214ee` |
| `pbr/parameter_sets.py` | `d1b9efe8d9f0e73a63b065f2c3f63f535652cfed` |
| `pbr/parameters.py` | `b5c36235fbd6861cf50ea719df4a32c0d5fe7dd5` |
| `pbr/provenance.py` | `c219b8ec2caa3331bbd1fcb9809846f8c93814c0` |
| `pbr/solver.py` | `54783b7370d03b7a763f23dfcfd2023b795ca3d2` |
| `pbr/species.py` | `775e308e5e39cbc9be04240c7972d3f5b5877fbd` |
| `pbr/sweep.py` | `b667181d4133e8ff7eef7dc1f70543aa7c366c00` |
| `tests/test_discretisation.py` | `226d08b7f53564ba3c3f805f48985bdf06392145` |
| `tests/test_solver.py` | `3511b426a21f043c269f5408f80706779fb7c0e5` |
| `tests/test_bep_response_analysis.py` | exact S4 commit; hash to be recorded if copied |
| `notebooks/bep_response_analysis.py` | `9dc43c460e1ea58990aee4b354e125284966e647` (optional plotting helper; V3 may use a smaller documented plotting layer) |

Independent rerun of the exact V2 tests in a temporary uv environment:

```text
uv run --no-project --python 3.12 --with pytest==8.4.2 --with numpy==2.5.3 --with scipy==1.18.0 --with pydantic==2.13.5 python -m pytest /tmp/bep-v3-v2-src/tests -q
63 passed in 10.41s
```

This receipt verifies the V2 code's existing unit/integration checks under that environment; it is not a V3 run, paper reproduction or experimental validation. The V2 handoff reports a separate 22-cell notebook run and 7 figures; those are prior branch receipts, not rerun evidence for V3.

## V3 environment and execution

`pyproject.toml` pins direct dependencies and `uv.lock` pins the resolved environment. It requires Python `>=3.12,<3.13`; the verified worker used Python 3.12.14, NumPy 2.5.3, SciPy 1.18.0, Pydantic 2.13.5, Matplotlib 3.10.8, ipykernel 6.30.1 and nbconvert 7.16.6.

```text
uv sync --project notebooks/v3 --locked
uv run --project notebooks/v3 python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 notebooks/v3/bep_v3_vertical_slice.ipynb
```

The executed V3 notebook is the receipt for the run. First execution exposed a setup error (an array was passed where the V2 engine expects an inlet callable); the notebook was corrected to use `make_inlet()` and then executed successfully. Numerical outputs and solver diagnostics are preserved in the notebook and summarized in `PROGRESS.md` and `DAMIAN_HANDOFF.md`.

The supporting Urmès primary PDF is available in the mounted project-management repository at `Academics/BEP/Catalysis/Articles/acquired_pdfs/urmesKineticStudySelective2019.pdf`; it is cited in the notebook by DOI and printed-page locator, but is not a sixth input snapshot. The V3 clean-checkout run uses no path to that PDF.

## Source comparison cautions carried forward

- V0/S2 dynamic surface states and elementary placeholders do not become validated kinetic equations merely because the scaffolds name them.
- S3/S4 use Urmès et al. (2019) fitted PSSA rates, which permit a transient gas reactor but do not provide finite-rate surface-coverage dynamics.
- Urmès et al. (2019) printed p. 5 estimates `K₁ = 611 Pa⁻¹`; Table 5, printed p. 6, fixes `K₁ = 13 Pa⁻¹`. This is an unresolved conflict in the primary source. Use 13 when attempting its Table 5 fitted model, and retain the contradiction for investigation; do not describe it as a resolved unit conversion.
- S5's inert tracer result is an illustration of transport memory, not a kinetic rate or experimental response.
