# Larsen 2024 — prior agent's readable Appendix F selected data (NOT source-certified)

This page makes part of the existing **machine-readable CSV** accessible as an ordinary Markdown table. It is **not** a page-by-page verified transcription of the thesis. The table below is reproduced from `notebooks/benchmarks/data/larsen_2024_selected_curves.csv`, rows tagged `response_origin=exact_appendix_F_table` by the prior Agent 4. Whether each numeric cell matches the **original image** is still an open, explicit verification task.

**Original source location claimed by the earlier agent:** Larsen 2024 thesis, Appendix F experiment and comparison table (printed pp. 75–76). Actual page images: `notebooks/benchmarks/source_renders/appendix_pages/page-71.png` through `page-88.png`; the exact PDF-to-printed-page mapping must be confirmed visually.

| Prior agent ID | Flow reported (mL/min) | Catalyst mass (mg) | Feed C2H2 (%) | C2H4 (%) | H2 (%) | He (%) | GHSV value (cm³ h⁻¹ gcat⁻¹, reference convention unresolved) | C2H2 conversion (%) | C2H4 selectivity (%) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXP1 | 200 | 100 | 1 | 20 | 20 | 59 | 120000 | 10.462575 | 99.716055 |
| EXP2 | 150 | 100 | 1 | 20 | 20 | 59 | 90000 | 20.991291 | 98.858475 |
| EXP3 | 100 | 100 | 1 | 20 | 20 | 59 | 60000 | 41.147780 | 98.759846 |
| EXP4 | 50 | 100 | 1 | 20 | 20 | 59 | 30000 | 89.976409 | 94.960679 |

These four rows apply only to **Pd0Ag** in the prior agent's CSV. No new physical units or reference temperature are inferred from these values.

## What remains to be checked

- Visually identify the **exact page and row** corresponding to each prior extraction and whether the numbers are original experimental values, an appendix's computed comparison, or something else.
- Transcribe remaining appendix pages 71–88, including numerical tables, code and any exact source equations, under `../transcriptions/larsen_2024_appendix_E_F.md`. This is a **required future output**; it does not yet exist.
- Confirm source definitions of volumetric flow, catalyst density, pressure and fitted parameter units. The current main-body Eq. 6.11 is outside the available Appendix E/F images, so cannot be certified from this excerpt.
- Keep notes about numerical model validity and interpretation under `../analysis/`, **not** in source-faithful transcription.

The owner need not certify these values; Agent 4 must provide the independent original-image comparison and the unresolved uncertainties.
