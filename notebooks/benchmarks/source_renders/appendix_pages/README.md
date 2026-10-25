# Larsen 2024 — Appendix E/F visual source guide

These files are **already committed to this branch**: 18 PNGs of Larsen's thesis PDF pages **71–88**, rendered at 300 DPI. Their filenames use the **1-based PDF page index**; these numbers are **not the printed thesis page numbers**.

**Open directly here:**  
[71](page-71.png) · [72](page-72.png) · [73](page-73.png) · [74](page-74.png) · [75](page-75.png) · [76](page-76.png) · [77](page-77.png) · [78](page-78.png) · [79](page-79.png)  
[80](page-80.png) · [81](page-81.png) · [82](page-82.png) · [83](page-83.png) · [84](page-84.png) · [85](page-85.png) · [86](page-86.png) · [87](page-87.png) · [88](page-88.png)

## What this source set can and cannot verify

- The images preserve scan-only **Appendix E/F** material for close inspection: alternative LHHW model comparison tables, selected modelling/code/input listings, and the Pd₀Ag experimental/comparison table. Read any scientific assertions directly from the rendered pages; the fact of a file's existence does not verify its contents.
- The **entire original thesis PDF is NOT in this branch**. The owner reports it exists separately in a local Zotero archive, which may not be available in a remote agent checkout. Do not interpret old `file:///c:/Users/...` links as automatically accessible here.
- Main-text **Eqs. 6.9–6.11**, **Figure 6.6 (printed p. 38)**, original experimental **Figures 6.1–6.4** and other main-body context **are not supplied by these Appendix E/F image files**. Do not claim to have read the disputed `r2` denominator exponent or full parameter-unit definitions from these images alone.
- The on-branch derived data `../../data/larsen_2024_parameters.csv` and `../../data/larsen_2024_selected_curves.csv` are **working transcriptions/digitizations**, not independent replacements for the actual thesis. The associated `../../larsen_2024_benchmark.ipynb` is a historical attempted reproduction with stored outputs.
- Apparent contradictions between the body equation, Appendix F code, fitted Figure 6.6 parameter vectors and prior notebook implementation require direct evidence with exact locators. Where the full thesis is not accessible, record **SOURCE BLOCKED** instead of guessing or silently changing the kinetics.

## Suggested audit order

1. Review this appendix and the existing derived files, identifying exactly which equations/inputs/observations they actually support.
2. Seek the full original thesis through legitimately accessible project/Zotero or publisher records in the active execution environment. If available, verify Eq. 6.11, Eq. 6.9–6.10, Figure 6.6, flow reference conditions and explicitly defined coefficient units directly.
3. Cross-check source statements against the notebook **before** altering code or claiming model reproducibility. Do not re-render these pages simply because an earlier prompt asked for rendering.
4. In the audit report, include a source-access matrix: **exact source/page actually inspected → claim it supports → accessibility status → what is still unknown.**

See branch-root [GOAL.md](../../../GOAL.md), [TODO.md](../../../TODO.md) and [Agent 4 source-audit issue #11](https://github.com/AsapLoso/BEP-Catalysis/issues/11).

**Provenance:** renders are from Victor Larsen's June 2024 TU Delft Bachelor End Project thesis. Their raster image files were imported on the earlier Agent 4 branch and **are not altered by this documentation update**.
