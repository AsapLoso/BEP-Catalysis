# Larsen 2024 — Appendix E/F visual source guide

These files are **already committed to this branch**: 18 PNGs of Larsen's thesis PDF pages **71–88**, rendered at 300 DPI. Their filenames use the **1-based PDF page index**; these numbers are **not the printed thesis page numbers**.

**Open directly here:**  
[71](page-71.png) · [72](page-72.png) · [73](page-73.png) · [74](page-74.png) · [75](page-75.png) · [76](page-76.png) · [77](page-77.png) · [78](page-78.png) · [79](page-79.png)  
[80](page-80.png) · [81](page-81.png) · [82](page-82.png) · [83](page-83.png) · [84](page-84.png) · [85](page-85.png) · [86](page-86.png) · [87](page-87.png) · [88](page-88.png)

**Readable transcription status (2026-10-26):** The [page-linked transcription](../../../../research/evidence/transcriptions/larsen_2024_appendix_E_F.md) records all 18 pages after visual inspection. Appendix E Tables E.1–E.3 are transcribed in full. Appendix F has checked equations, constants, bounds, methods, selected processed responses and output excerpts, but not every code line or displayed table cell. Its Pd₃Ag display itself omits middle rows with an ellipsis. The transcription labels partial/ambiguous coverage rather than treating OCR or derived outputs as a source transcript. Scientific interpretation is kept in the separate audit report; processed and digitized values are indexed in `research/evidence/derived/`.

## What this source set can and cannot verify

- The images preserve scan-only **Appendix E/F** material for close inspection: alternative LHHW model comparison tables, selected modelling/code/input listings, and the Pd₀Ag experimental/comparison table. Read any scientific assertions directly from the rendered pages; the fact of a file's existence does not verify its contents.
- The [full original 97-page thesis PDF](../../../../research/evidence/original/Larsen%20-%202024%20-%20Semihydrogenation%20of%20acetylene%20to%20ethylene%20with%20a%20PdAg%20catalyst.pdf) is **now on this branch**, byte-verified against the owner's upload. A [machine-extracted text layer](../../../../research/evidence/transcriptions/larsen_2024_complete_native_text_unverified.txt) is searchable for native-text pages, but scanned Appendix E/F data remain incomplete in it. PDF metadata dates the compilation 2026; official deposit provenance remains unconfirmed.
- Main-text **Eqs. 6.9–6.11**, **Figure 6.6 (printed p. 38)**, original experimental **Figures 6.1–6.4** and other main-body context **are not supplied by these Appendix E/F image files**. Do not claim to have read the disputed `r2` denominator exponent or full parameter-unit definitions from these images alone.
- The on-branch derived data `../../data/larsen_2024_parameters.csv` and `../../data/larsen_2024_selected_curves.csv` are **working transcriptions/digitizations**, not independent replacements for the actual thesis. The associated `../../larsen_2024_benchmark.ipynb` is a historical attempted reproduction with stored outputs.
- Apparent contradictions between the body equation, Appendix F code, fitted Figure 6.6 parameter vectors and prior notebook implementation require direct evidence with exact locators. **The PDF is now accessible**; if any specific source reading is ambiguous, mark that claim unresolved instead of guessing.

## Audit result and open source requests

The independent audit is recorded in [the report](../../../../research/reports/larsen_2024_equation_and_baseline_audit.md). It checks the equation image and Figure 6.6 against the historical notebook, reconciles visible processed rows with selected plot conditions, and executes a separate fixed-parameter model comparison. It does not claim full reproduction of the final fits.

The remaining transcription/reproduction blockers are the complete Appendix F code and all visible Pd₀Ag/Pd₂Ag table cells, the final Pd₂Ag/Pd₃Ag fit masks, the hidden middle of the Pd₃Ag source display, and the original workbook/GC records. The final extended-model fitting code and source-certified units/reference conditions are also absent. Keep those gaps explicit; do not fill them from OCR, an inferred model, or digitized curves.

See branch-root [GOAL.md](../../../../GOAL.md), [TODO.md](../../../../TODO.md) and [Agent 4 source-audit issue #11](https://github.com/AsapLoso/BEP-Catalysis/issues/11).

**Provenance:** renders are from Victor Larsen's June 2024 TU Delft Bachelor End Project thesis. Their raster image files were imported on the earlier Agent 4 branch and **are not altered by this documentation update**.
