# BEP V3 vertical slice

This folder contains the five immutable source snapshots, their theory audit, a provisional model blueprint, and the new V3 notebook. Start with `GOAL.md` and `PROGRESS.md` for scope and verified receipts.

## Reproduce the notebook

From the repository root, with Python 3.12 available:

```sh
uv sync --project notebooks/reference/v3 --locked
uv run --project notebooks/reference/v3 python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 notebooks/reference/v3/bep_v3_vertical_slice.ipynb
```

Open `bep_v3_vertical_slice.ipynb` in Jupyter to inspect the saved run, diagnostics and inline plots. The notebook locates `vendor/pbr` relative to the checkout and does not import from a separate Methanol-Catalysis checkout. The locked environment in `pyproject.toml` and `uv.lock` contains Python 3.12-compatible, version-pinned numerical and notebook dependencies.

The engine source is the unchanged V2 `pbr/` package from commit `2ee0dc1a84529d6830dcc628fc771878907fb22c`; per-file Git blob hashes are in `SOURCE_MANIFEST.md`. The notebook selects its Uniform-pellet, zero-film, zero-dispersion and algebraic-surface closures. Diffusivity sentinels used by the unchanged builder are not physical values and are not read by the Uniform-closure RHS.

## Scientific scope

The Urmès PSSA fit is a provisional implementation baseline for a bounded source-system model. It is not owner approval of every equation or physical assumption, not a PdAg/BEP kinetic model, and not experimental validation. The paper's K₁ values conflict (`611 Pa⁻¹` in p. 5 text; `13 Pa⁻¹` in Table 5, p. 6); V3 uses 13 for the fitted-model attempt and preserves the discrepancy. The transient bed void fraction is borrowed, and the source's steady table comparison is mixed. See `THEORY_CROSSWALK.md`, `DAMIAN_HANDOFF.md` and `STUDY_PRIORITIES.md` before using the results.

The personal map remains read-only. `DAMIAN_HANDOFF.md` is a draft for owner review and has not been sent.

The Unified Reactor Model branch does not include the integrated AI reference map or personal-map snapshot used for the theory crosswalk. Their source blobs are pinned in `SOURCE_MANIFEST.md` and linked to migration snapshot commit `0cd47473a93a71f6200a21e6b66c40d6e3bc7a77`; they are not runtime dependencies of the notebook.
