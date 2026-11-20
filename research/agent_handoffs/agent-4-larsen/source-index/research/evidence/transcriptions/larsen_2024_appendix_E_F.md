# Larsen 2024 — Appendix E/F page-checked transcription

**Primary source:** Victor Larsen, *Semihydrogenation of acetylene to ethylene with a PdAg catalyst*, TU Delft Bachelor End Project, June 2024. The PDF in `research/evidence/original/` is the user-provided copy (SHA-256 `b5aaa2300ff9b64aca70e58cc5e4d8be30b3c12ee264e69af89e01c86f5120c9`); official-deposit equivalence is not established.

**Source renders:** 18 unmodified 300-DPI PNGs of one-based PDF pages 71–88: [page guide](../../../notebooks/benchmarks/source_renders/appendix_pages/README.md). Each image link below points to the checked original render. Printed page numbers are transcribed from the page itself.

**Method/status:** I inspected each of the 18 render PNGs visually, using OCR only to locate content. `checked_against_image` means the text explicitly transcribed in that page section was compared with the image. Tables E.1–E.3 and all readable Appendix F code on PDF pp. 78–88 are transcribed. The page-referenced [CSV](larsen_2024_appendix_F_visible_table_rows.csv) contains all displayed rows and legible cells from the Pd₀Ag/Pd₂Ag/Pd₃Ag processed input-table displays and the complete 41-row Pd₀Ag `comparison_de_df` display. Literal source ellipses, cells cropped at a page edge and raster cells that cannot be read reliably are marked explicitly. The Pd₃Ag middle rows are absent from Larsen's pandas display. Other computed DataFrame previews on pp. 80–85 are documented by page, dimensions and visible row ranges; they are not additional experimental input tables and their preview cells are not separately transcribed. On p. 85, all 41 `df_fit` rows are displayed, but pandas elides columns; the visible source fields duplicate the p. 80 input table and the transformed columns are not copied into a second table. The source-limited transcription does not recover the workbook or a complete experimental dataset. No OCR draft is presented as a verified transcript.

## PDF page 71 — Appendix E divider

- **Original image:** [page-71.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-71.png)
- **Printed page:** 65
- **Review status:** `checked_against_image`
- **Visible source text:** `E` / `Table tests`.
- **Coverage/uncertainty:** Divider only; none.

## PDF page 72 — blank divider verso

- **Original image:** [page-72.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-72.png)
- **Printed page:** 66
- **Review status:** `checked_against_image`
- **Visible source text:** Running divider `E. Table tests`; otherwise blank.
- **Coverage/uncertainty:** No table or equation.

## PDF page 73 — Table E.1, Pd₀Ag

- **Original image:** [page-73.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-73.png)
- **Printed page:** 67
- **Review status:** `checked_against_image`
- **Visible source heading/caption:** `E.1. Table per cat. with every LHHW model variance`; `E.1.1. Pd₀Ag`; `Table E.1: Overview of the tested kinetic model variants for Pd₀Ag, if ✓ it is a variable in the LHHW model and if × the term is let out of the LHHW model`.
- **Column headings:** Variant; H₂-term; C₂H₄-term; Inhibition term; K_H₂; Power Law; Overall RMSE; RMSE_conversion; RMSE_selectivity.
- **Transcription:** `✓` and `×` are reproduced as printed; dashes are printed dashes.

| Variant | H₂ | C₂H₄ | Inhibition | K_H₂ | Power law | Overall RMSE | Conversion RMSE | Selectivity RMSE |
|---|:---:|:---:|:---:|:---:|:---:|---:|---:|---:|
| 1 | ✓ | ✓ | ✓ | ✓ | × | 42.3166 | 66.51 | 4.31 |
| 2 | ✓ | ✓ | × | × | × | 15.2241 | 27.12 | 3.52 |
| 2a | × | ✓ | × | × | × | 17.2401 | 28.02 | 3.21 |
| 2b | ✓ | × | × | × | × | 28.6856 | 49.81 | 3.21 |
| 2c | × | × | × | × | × | 29.5322 | 49.81 | 5.78 |
| 3 | ✓ | ✓ | ✓ | × | × | 13.8472 | 24.88 | 3.71 |
| 3a | × | ✓ | ✓ | × | × | 17.4908 | 28.53 | 4.10 |
| 3b | ✓ | × | ✓ | × | × | 10.7848 | 18.38 | 3.67 |
| 3c | × | × | ✓ | × | × | 2338.0896 | 49.81 | 3987.61 |
| 4 | ✓ | ✓ | × | ✓ | × | 17.5358 | 30.36 | 3.46 |
| 4 smaller bounds | ✓ | ✓ | × | ✓ | × | 11.4083 | 18.45 | 6.56 |
| 4a | × | ✓ | × | × | × | 32.7246 | 35.62 | 3.45 |
| 4b | ✓ | × | × | ✓ | × | — | — | — |
| 4c | × | × | × | × | × | 29.5322 | 49.81 | 5.78 |
| 5 | ✓ | ✓ | ✓ | ✓ | × | 6.4395 | 9.73 | 4.55 |
| 5 smaller bounds | ✓ | ✓ | ✓ | ✓ | × | 8.7065 | 13.89 | 5.81 |
| 5a | × | ✓ | ✓ | × | × | 17.4908 | 28.53 | 4.10 |
| 5b | ✓ | × | ✓ | ✓ | × | 28.6857 | 49.81 | 3.21 |
| 5c | × | × | ✓ | × | × | 2338.0896 | 49.81 | 3987.61 |
| 5d | ✓ | ✓ | ✓ | ✓ | × | 18.0673 | 30.75 | 5.51 |
| 6 | ✓ | ✓ | × | × | ✓ | 8.4021 | 13.95 | 3.53 |
| 6 smaller bounds | ✓ | ✓ | × | × | ✓ | 7.0357 | 12.64 | 3.34 |
| 7 | ✓ | ✓ | ✓ | × | ✓ | 7.6719 | 12.63 | 5.59 |
| 8 | ✓ | ✓ | × | ✓ | ✓ | 15.1870 | 24.02 | 3.54 |
| 9 | ✓ | ✓ | ✓ | ✓ | ✓ | 14.5374 | 23.22 | 2.73 |
| 9 smaller bounds | ✓ | ✓ | ✓ | ✓ | ✓ | 7.0172 | 12.64 | 3.16 |
| 10 | ✓ | ✓ | ✓ | ✓ | ✓ | 8.2459 | 11.39 | 6.63 |

## PDF page 74 — Table E.2, Pd₂Ag

- **Original image:** [page-74.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-74.png)
- **Printed page:** 68
- **Review status:** `checked_against_image`
- **Visible source heading/caption:** `E.1.2. Pd₂Ag`; Table E.2 gives the tested kinetic model variants for Pd₂Ag and defines `✓` as a variable in the LHHW model and `×` as a term left out.
- **Column headings:** Variant; H₂-term; C₂H₄-term; Inhibition term; K_H₂; Power Law; Overall RMSE; RMSE_conversion; RMSE_selectivity.

| Variant | H₂ | C₂H₄ | Inhibition | K_H₂ | Power law | Overall RMSE | Conversion RMSE | Selectivity RMSE |
|---|:---:|:---:|:---:|:---:|:---:|---:|---:|---:|
| 1 | ✓ | ✓ | ✓ | ✓ | × | 73.2983 | 94.85 | 46.38 |
| 2 | ✓ | ✓ | × | × | × | 12.8855 | 13.46 | 18.36 |
| 2a | × | ✓ | × | × | × | 14.5874 | 13.97 | 20.47 |
| 2b | ✓ | × | × | × | × | 9.4210 | 9.36 | 15.66 |
| 2c | × | × | × | × | × | 2361.6036 | 13.46 | 4014.28 |
| 3 | ✓ | ✓ | ✓ | × | × | 12.7469 | 13.46 | 18.26 |
| 3a | × | ✓ | ✓ | × | × | 14.3602 | 13.46 | 20.97 |
| 3b | ✓ | × | ✓ | × | × | 10.3796 | 11.39 | 15.88 |
| 3c | × | × | ✓ | × | × | 54.1860 | 75.43 | 22.03 |
| 4 | ✓ | ✓ | × | ✓ | × | 11.9816 | 13.46 | 16.81 |
| 4 smaller bounds | ✓ | ✓ | × | ✓ | × | 12.7543 | 13.44 | 18.30 |
| 4a | × | ✓ | × | × | × | 14.5874 | 13.97 | 20.47 |
| 4b | ✓ | × | × | ✓ | × | 9.4182 | 9.38 | 15.65 |
| 4c | × | × | × | × | × | 2361.6036 | 13.46 | 4014.28 |
| 5 | ✓ | ✓ | ✓ | ✓ | × | 12.0874 | 13.46 | 16.97 |
| 5 smaller bounds | ✓ | ✓ | ✓ | ✓ | × | 14.1928 | 13.46 | 20.77 |
| 5a | × | ✓ | ✓ | × | × | 14.3602 | 13.46 | 20.97 |
| 5b | ✓ | × | ✓ | ✓ | × | 12.7298 | 13.46 | 18.23 |
| 5c | × | × | ✓ | × | × | 54.1860 | 75.43 | 22.03 |
| 5d | ✓ | ✓ | ✓ | ✓ | × | 12.1767 | 13.46 | 17.15 |
| 6 | ✓ | ✓ | × | × | ✓ | 9.8769 | 4.38 | 19.15 |
| 6 smaller bounds | ✓ | ✓ | × | × | ✓ | 9.4047 | 3.97 | 18.98 |
| 7 | ✓ | ✓ | ✓ | × | ✓ | 10.4806 | 5.62 | 19.62 |
| 8 | ✓ | ✓ | × | ✓ | ✓ | 12.7709 | 10.71 | 19.37 |
| 9 | ✓ | ✓ | ✓ | ✓ | ✓ | 13.1385 | 11.55 | 21.30 |
| 9 smaller bounds | ✓ | ✓ | ✓ | ✓ | ✓ | 10.9095 | 7.61 | 18.91 |
| 10 | ✓ | ✓ | ✓ | ✓ | ✓ | 25.2860 | 13.46 | 41.70 |

## PDF page 75 — Table E.3, Pd₃Ag

- **Original image:** [page-75.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-75.png)
- **Printed page:** 69
- **Review status:** `checked_against_image`
- **Visible source heading/caption:** `E.1.3. Pd₃Ag`; Table E.3 gives the tested kinetic model variants for Pd₃Ag and defines `✓` as a variable in the LHHW model and `×` as a term left out.
- **Column headings:** Variant; H₂-term; C₂H₄-term; Inhibition term; K_H₂; Power Law; Overall RMSE; RMSE_conversion; RMSE_selectivity.

| Variant | H₂ | C₂H₄ | Inhibition | K_H₂ | Power law | Overall RMSE | Conversion RMSE | Selectivity RMSE |
|---|:---:|:---:|:---:|:---:|:---:|---:|---:|---:|
| 2 | ✓ | ✓ | × | × | × | 42.6540 | 13.65 | 73.31 |
| 2a | × | ✓ | × | × | × | 42.7758 | 13.65 | 76.29 |
| 2b | ✓ | × | × | × | × | 42.4521 | 13.65 | 72.90 |
| 2c | × | × | × | × | × | 2392.2863 | 13.65 | 4070.10 |
| 3 | ✓ | ✓ | ✓ | × | × | 42.6557 | 13.65 | 73.31 |
| 3a | × | ✓ | ✓ | × | × | 42.7382 | 13.65 | 74.90 |
| 3b | ✓ | × | ✓ | × | × | 42.6281 | 13.65 | 73.27 |
| 3c | × | × | ✓ | × | × | 2392.2830 | 13.65 | 4070.09 |
| 4 | ✓ | ✓ | × | ✓ | × | 43.0763 | 13.65 | 81.82 |
| 4 smaller bounds | ✓ | ✓ | × | ✓ | × | 46.9826 | 13.96 | 92.28 |
| 4a | × | ✓ | × | × | × | 42.7758 | 13.65 | 76.29 |
| 4b | ✓ | × | × | ✓ | × | 808.4597 | 13.65 | 1276.75 |
| 4c | × | × | × | × | × | 2392.2870 | 13.65 | 4070.10 |
| 5 | ✓ | ✓ | ✓ | ✓ | × | 42.1434 | 12.76 | 72.67 |
| 5 regular LHHW model | ✓ | ✓ | ✓ | ✓ | × | 46.9933 | 13.93 | 92.32 |
| 5a | × | ✓ | ✓ | × | × | 42.7382 | 13.65 | 74.90 |
| 5b | ✓ | × | ✓ | ✓ | × | 42.6548 | 13.65 | 73.31 |
| 5c | × | × | ✓ | × | × | 2392.2830 | 13.65 | 4070.09 |
| 5d | ✓ | ✓ | ✓ | ✓ | × | 42.2333 | 12.95 | 73.09 |
| 6 | ✓ | ✓ | × | × | ✓ | 41.8279 | 11.96 | 73.49 |
| 6 smaller bounds | ✓ | ✓ | × | × | ✓ | 41.8141 | 11.70 | 73.48 |
| 7 | ✓ | ✓ | ✓ | × | ✓ | 41.7086 | 11.81 | 72.75 |
| 8 | ✓ | ✓ | × | ✓ | ✓ | 41.9421 | 11.70 | 73.57 |
| 9 | ✓ | ✓ | ✓ | ✓ | ✓ | 42.1767 | 13.46 | 74.86 |
| 9 smaller bounds | ✓ | ✓ | ✓ | ✓ | ✓ | 41.7004 | 11.84 | 72.80 |
| 10 | ✓ | ✓ | ✓ | ✓ | ✓ | 55.2482 | 13.65 | 111.18 |

## PDF page 76 — blank page

- **Original image:** [page-76.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-76.png)
- **Printed page:** 70
- **Review status:** `checked_against_image`
- **Visible source text:** No substantive text.

## PDF page 77 — Appendix F divider

- **Original image:** [page-77.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-77.png)
- **Printed page:** 71
- **Review status:** `checked_against_image`
- **Visible source heading:** `F. Standard LHHW model code`.

## PDF page 78 — Appendix F import, input workbook, Pd₂Ag table start

- **Original image:** [page-78.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-78.png)
- **Printed page:** 72
- **Review status:** `checked_against_image` for code and all displayed Pd₂Ag cells
- **Visible source structure:** Heading `Kinetic modeling Acetylene semihydrogenation`; notebook imports NumPy, pandas, Matplotlib, SciPy ODE/optimization functions and warning utilities; reads a local Excel workbook with one sheet per catalyst; comments explicitly exclude experiment 34 (Excel row 36) from the Pd₀Ag data; maps the Pd₂Ag columns to an experiment number, flow, WHSV, feed volume percentages, catalyst mass, conversion, selectivity and carbon balance.
- **Visible table headings:** `exp_numb`, `flow (mL/min)`, `WHSV (cm^3/h/g cat.)`, `vol. % C2H2`, `vol. % C2H4`, `vol. % H2`, `vol. % He`, `vol. % CO`, `mass cat. (mg)`, `conv`, `selec`, `C-balans` [sic]. A header-like input row precedes experiment rows in the displayed DataFrame.
- **Experiment IDs visible:** Pd₂Ag `EXP1`–`EXP23` (table continues on PDF page 79). The source display includes processed responses; these are not raw chromatograph areas or unprocessed measurements.
- **Table transcription:** Every displayed Pd₂Ag cell, including its header-like row and rows `EXP1`–`EXP23`, is transcribed in `larsen_2024_appendix_F_visible_table_rows.csv`, with PDF page 78 / printed page 72 locators. The CSV preserves the printed spellings and decimal precision. These are author-processed responses, not raw chromatograph areas.

- **Selected processed-response cells** (source columns `exp_numb`, `conv`, `selec`, and `C-balans`):

  | ID | Conversion (%) | Selectivity (%) | C balance (%) |
  |---|---:|---:|---:|
  | EXP1 | 58.018857 | 95.600234 | 86.818862 |
  | EXP2 | 86.417753 | 94.243281 | 87.317188 |
  | EXP3 | 99.276357 | 84.886849 | 91.513288 |
  | EXP4 | 99.349524 | 55.846520 | 90.843877 |
  | EXP14 | 99.661391 | 27.756005 | 96.066297 |
  | EXP15 | 99.659019 | 57.629123 | 83.283371 |
  | EXP16 | 99.653853 | 36.294416 | 95.328362 |
  | EXP17 | 99.681646 | 47.284657 | 96.457802 |
  | EXP19 | 99.602241 | 25.834125 | 98.121920 |
  | EXP20 | 99.624922 | 10.648119 | 97.369070 |
  | EXP21 | 99.548308 | 68.096788 | 96.180869 |

- **Coverage/uncertainty:** The complete visible table is in the linked CSV. EXP2's printed conversion is `86.417753`; the earlier selected-response extract said `86.417763`. This source transcription records the image reading and does not revise the prior numerical-audit artifacts or metrics. See the source-vs-extract note in the CSV.

## PDF page 79 — Appendix F Pd₂Ag table end, Pd₃Ag preview, combined-table setup

- **Original image:** [page-79.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-79.png)
- **Printed page:** 73
- **Review status:** `checked_against_image` for the complete Pd₂Ag continuation and all displayed Pd₃Ag cells
- **Visible source structure:** Pd₂Ag table continues without an ellipsis through `EXP42`, yielding 42 processed experiment rows. The Pd₃Ag table preview shows `EXP1`–`EXP4`, a literal pandas ellipsis, and terminal displayed rows `EXP73`–`EXP77`; its footer reads `78 rows × 12 columns` (including the header-like row). The Pd₀Ag extraction begins below it.
- **Transcribed table fields:** same 12 headings listed for PDF page 78.
- **Selected Pd₂Ag processed-response cells:** the source table visibly contains rows `EXP35`–`EXP38` for the acetylene-variation curve. Their response values are excerpted below and in the derived ID crosswalk; the table is displayed through `EXP42`.
- **Table transcription:** All Pd₂Ag rows `EXP24`–`EXP42` and every displayed Pd₃Ag cell (header-like row, `EXP1`–`EXP4`, ellipsis, `EXP73`–`EXP77`) are in the linked CSV. Visible Pd₃Ag head response pairs (conversion, selectivity, %) are `(99.74857, 68.89139)`, `(99.714813, 56.165749)`, `(99.63909, 35.640171)`, and `(99.306389, -82.203658)`. These are author-processed outputs, not raw GC measurements.
- **Selected Pd₂Ag acetylene-series rows (source `conv` / `selec`, %):**

  | ID | Conversion (%) | Selectivity (%) |
  |---|---:|---:|
  | EXP35 | 79.318032 | 96.909178 |
  | EXP36 | 92.487792 | 82.667845 |
  | EXP37 | 92.832456 | 76.951782 |
  | EXP38 | 95.392858 | 50.886892 |
- **Coverage/uncertainty:** All Pd₂Ag rows are visible and transcribed. The Pd₃Ag middle rows are omitted by the original pandas display, not cropped from the page. EXP36's displayed selectivity reads `82.667845`; an earlier selected-response extract says `89.667845`. The CSV records the page image reading; the numerical-audit files and metrics are unchanged in this transcription-only pass.

## PDF page 80 — Appendix F Pd₀Ag processed response table and combined data

- **Original image:** [page-80.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-80.png)
- **Printed page:** 74
- **Review status:** `checked_against_image` for the complete displayed Pd₀Ag table, concatenation code and preview metadata
- **Visible source structure:** The Pd₀Ag table is continuous: it contains `EXP1`–`EXP33` and `EXP35`–`EXP42`; `EXP34` was excluded in the preceding code cell. Every displayed Pd₀Ag input-table cell is in the linked CSV. The concatenated table footer reads `163 rows × 13 columns` and includes a header-like row for each catalyst. A note above constants reads: `All the constants that can be filled out beforehand, and turning DW [g] into Dz [m]. Through density of Al2O3 = 3.987 g/cm^3` [capitalization/grammar as printed].
- **Transcribed observation:** The values shown in the `conv`, `selec`, and `C-balans` columns are processed results, not raw GC chromatograms. Pd₂Ag has its own 42-row processed-response table; Pd₃Ag has a much longer but screen-truncated display.
- **Coverage/uncertainty:** The input display is complete; it is not a head/tail preview. The separate concatenated `df_all` display is head/tail only and includes a literal ellipsis; its preview cells and omitted combined rows are not separately transcribed. The 3.987 g cm⁻³ alumina note is transcribed as printed; the separate audit records its disagreement with PDF p. 81 without altering the source transcription.

## PDF page 81 — Appendix F geometry, reactor balances and standard LHHW equations

- **Original image:** [page-81.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-81.png)
- **Printed page:** 75
- **Review status:** `checked_against_image` for all readable code, constants, balance structure and displayed rate equations
- **Visible constants (transcription):** `R = 8.314` (J mol⁻¹ K⁻¹); `D = 0.5` cm; `rho = 2.65` (comment: density SiO₂, g cm⁻³); catalyst masses read from the data tables; `T = 373` (comment: 100 Celsius); `P_total = 100000` Pa; `A = (np.pi * D**2)/4` cm²; `dW_dz = rho * A * 100` g m⁻¹. The displayed catalyst lengths are approximately 0.001921871 m for Pd₀Ag, 0.001441403 m for Pd₂Ag, and 0.001921871 m for Pd₃Ag.
- **Visible balance structure:** `dF/dz = dW_dz × [-r1, r1-r2, r2, -r1-r2, 0, 0]` for C₂H₂, C₂H₄, C₂H₆, H₂, He and CO. The solver shown is `solve_ivp(..., method="LSODA", rtol=1e-9, atol=1e-14)`.
- **Displayed standard LHHW equations (as printed on this page):**

  \[
  r_1=\frac{k_1 K_1p_A K_3p_{H_2}}{(1+K_1p_A+K_2p_E+K_3p_{H_2})^2},\qquad
  r_2=\frac{k_2 K_2p_E K_3p_{H_2}}{(1+K_1p_A+K_2p_E)^2(1+K_{inh}p_A)}.
  \]

- **Visible pressure handling:** The displayed code clamps each partial pressure at zero and divides its Pa value by `1e5`; the inline comment calls this conversion “from Pa to bar.” This is the literal divisor visible on PDF p. 81.
- **Coverage/uncertainty:** Readable code on this page is transcribed below. The source shows the standard LHHW model, not the final extended model of main-text Eqs. 6.9–6.11; this is a source-scope distinction, not a cropped passage.

## PDF page 82 — Appendix F ideal-gas feed conversion and combined rows

- **Original image:** [page-82.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-82.png)
- **Printed page:** 76
- **Review status:** `checked_against_image` for the readable flow-conversion code, equations, and output dimensions
- **Visible source calculation (transcribed):** A function removes repeated rows marked `flow [mL/min]`; calculates `V_m3_s = flow × 1e-6 / 60`; calculates total inlet molar flow as `F_tot_mol_s = P * V_m3_s / (R*T)`; divides feed volume percentages by 100 and multiplies by total molar flow to set species inlet flows. The rendered call supplies `R`, `T`, `P_total`, and a flow-column label. No explicit mass-flow-controller standard reference condition is stated.
- **Visible output:** Combined processed dataset footer `160 rows × 26 columns` after repeated header-like rows are removed (consistent with 41 Pd₀Ag + 42 Pd₂Ag + 77 Pd₃Ag experiment rows).
- **Coverage/uncertainty:** The 160-row output is a head/tail preview with a literal pandas ellipsis; its intermediate rows are not printed. The preview includes wide columns elided by pandas. It is a calculated flow table, not an additional experimental response table.

## PDF page 83 — Appendix F simulated response table

- **Original image:** [page-83.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-83.png)
- **Printed page:** 77
- **Review status:** `checked_against_image` for the readable code and preview structure
- **Visible source structure:** A three-reaction species-flow simulation is applied to the combined 160-row input DataFrame; simulated conversion/selectivity are assembled by experiment number and catalyst. Pandas output footer reads `160 rows × 4 columns`; the visible head and tail are not the full table.
- **Coverage/uncertainty:** The displayed `sim_results_df` and `exp_results_df` are 160-row head/tail previews with a literal pandas ellipsis; intermediate rows are not printed. The merged `comparison_df` begins at the bottom of PDF p. 83 and continues on p. 84. These are standard-model outputs and copied processed responses, not raw experimental measurements. The complete fitted Pd₀Ag comparison output is transcribed separately from PDF pp. 87–88.

## PDF page 84 — Appendix F RMSE computation and standard-model score

- **Original image:** [page-84.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-84.png)
- **Printed page:** 78
- **Review status:** `checked_against_image` for all readable RMSE code, formula, score, and visible preview ranges
- **Visible source formula:** `RMSE_i = sqrt(((conv_sim - conv_exp)^2 + (selec_sim - selec_exp)^2)/2)`; overall score is the arithmetic mean of the experiment RMSE values. The code calls `np.sum(RMSE_results)/len(df_all)`.
- **Visible output:** `Overall RMSE = 472.42114981326106` for this standard-model run over the combined table.
- **Coverage/uncertainty:** The numeric score is a standard-model code output, not Figure 6.6's final extended-model score. The seven-column output preview is head/tail only and contains a literal pandas ellipsis; no unprinted rows are reconstructed.

## PDF page 85 — Appendix F displayed fit subset

- **Original image:** [page-85.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-85.png)
- **Printed page:** 79
- **Review status:** `checked_against_image` for filter, row count and comments
- **Visible text/code:** Heading `Optimisation`; prose says “Need to use: differential_evolution” and says catalysts are fitted separately because each has its own kinetics. Under `Start fitting with the "best" data`, code sets `df_fit = df_all[df_all["catalyst"] == "AgPd0"].copy()`. The `#All data` line and `#df_fit = df_all.copy()` are commented. Output footer: `41 rows × 26 columns`.
- **Coverage/uncertainty:** The display contains all 41 AgPd0 rows (indices 0–40), with no row ellipsis; its wide middle columns are elided by pandas. Its visible input fields duplicate the already transcribed PDF p. 80 table; the transformed columns are not copied into a second table. This is the standard-model AgPd0 subset and does not expose a final Pd₂Ag/Pd₃Ag selection mask.

## PDF page 86 — Appendix F standard fit function

- **Original image:** [page-86.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-86.png)
- **Printed page:** 80
- **Review status:** `checked_against_image` for all readable function code and all six bounds
- **Visible structure:** A six-variable Differential Evolution bound list, a comparison function that simulates each DataFrame row, a paired conversion/selectivity RMSE routine, and an objective function. The variables passed to the standard-model rate function are `k1`, `k2`, `K1`, `K2`, `Kinh`, and `KH`; no `r1_max` or `n_inh` is present in this displayed standard-model code.
- **Visually transcribed Differential Evolution bounds** (the displayed standard-model order is k1, k2, K1, K2, Kinh, KH):

      bounds = [
          (1e-10, 1),     # k1
          (1e-10, 1),     # k2
          (1e-10, 1000),  # K1
          (1e-10, 1000),  # K2
          (1e-10, 1000),  # Kinh
          (1e-10, 1000),  # KH
      ]

- **Coverage/uncertainty:** All readable function lines and bound entries are transcribed below. These bounds belong to the six-variable standard model and cannot evaluate the later eight-element Figure 6.6 parameter vectors.

## PDF page 87 — Appendix F Differential Evolution output

- **Original image:** [page-87.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-87.png)
- **Printed page:** 81
- **Review status:** `checked_against_image` for the optimizer call, readable printed results, and comparison-table rows on this page
- **Visible run settings:** Differential Evolution output shows 50 steps, population size 42, tolerance `1e-8`, seed 42 and a polishing step with `L-BFGS-B`.
- **Visible output:** Standard-model AgPd0 optimization prints a best overall RMSE of approximately `6.439535`; the optimizer output is for the six-variable model/subset on PDF page 85. Table E.1 variant 5 reports the same score to four decimals (`6.4395`).
- **Coverage/uncertainty:** The 50 Differential Evolution progress lines are console output rather than code or table entries and are not copied. The fitted comparison table begins on this page; its displayed rows are transcribed in the linked CSV. The source's last row at the page foot is marked where any cell is cropped or unreadable.

## PDF page 88 — Appendix F Pd₀Ag comparison rows and parity code

- **Original image:** [page-88.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-88.png)
- **Printed page:** 82
- **Review status:** `checked_against_image` for all readable plotting code and the complete displayed comparison table
- **Visible source structure:** Remaining Pd₀Ag comparison output rows are shown, followed by conversion/selectivity parity-plot code. The code sets a relative band `band = 0.10`, calculates the fraction of predicted points inside the band, and separately calculates conversion and selectivity RMSE. Plot labels show experimental vs simulated values; the screenshot begins/continues a Pd₀Ag parity plot.
- **Coverage/uncertainty:** The `comparison_de_df` display has 41 rows × 6 columns across PDF pp. 87–88, without a source ellipsis; every row is transcribed in the linked CSV. Simulated cells that cannot be read reliably at the page-87 foot, and the unreadable EXP21 experimental-conversion digit, are marked `[unclear]`. The parity-plot output at the bottom of PDF p. 88 is clipped by the screenshot boundary; no graph points are digitized.

## Appendix F — readable code transcription

These are literal, page-linked excerpts from the notebook screenshots. They preserve the source's variable names and comments. `[unclear]` marks characters that cannot be distinguished in the raster; `[cropped]` marks text cut by the page/image boundary. No missing code is reconstructed from the benchmark notebook. Table outputs remain distinct from this code transcription.

### PDF page 78 / printed page 72 — imports, workbook reads and Pd₂Ag field mapping

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import differential_evolution, minimize
from scipy.stats import t as student_t
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

plt.rcParams.update({
    "figure.dpi": 110,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
})

# Import of all needed extensions, and plot standard view.
data_AgPd0 = pd.read_excel(
    "/Users/Victor/Desktop/Uni/MGT 4e jaar/BEP/Acetylene_Data.xlsx",
    sheet_name="AgPd0_#102_Copy", usecols="A, B, C, F, G, H, I, J, L, AM, AI, AJ",
)
data_AgPd2 = pd.read_excel(
    "/Users/Victor/Desktop/Uni/MGT 4e jaar/BEP/Acetylene_Data.xlsx",
    sheet_name="AgPd2_#102", usecols="A, B, C, F, G, H, I, J, L, AM, AT, AJ",
)
data_AgPd3 = pd.read_excel(
    "/Users/Victor/Desktop/Uni/MGT 4e jaar/BEP/Acetylene_Data.xlsx",
    sheet_name="AgPd3_#102", usecols="A, B, C, F, G, H, I, J, L, AM, AT, AJ",
)

# Exclude experiment 34 (Excel row 36) from the AgPd0 dataset.
# The experiment labels are text values such as "EXP34", so first extract the number.
exp_number_AgPd0 = pd.to_numeric(
    data_AgPd0.iloc[:, 0].astype(str).str.extract(r"(\d+)", expand=False),
    errors="coerce",
)
data_AgPd0 = data_AgPd0[
    (exp_number_AgPd0.ne(34)) | (exp_number_AgPd0.isna())
].reset_index(drop=True)

# 1. AgPd2
exp_numb_AgPd2 = data_AgPd2.iloc[:, 0]
flow_AgPd2 = data_AgPd2.iloc[:, 1]
WHSV_AgPd2 = data_AgPd2.iloc[:, 2]
vol_percent_C2H2_AgPd2 = data_AgPd2.iloc[:, 3]
vol_percent_C2H4_AgPd2 = data_AgPd2.iloc[:, 4]
vol_percent_H2_AgPd2 = data_AgPd2.iloc[:, 5]
vol_percent_He_AgPd2 = data_AgPd2.iloc[:, 6]
vol_percent_CO_AgPd2 = data_AgPd2.iloc[:, 7]
m_cat_AgPd2 = data_AgPd2.iloc[:, 8]
conv_AgPd2 = data_AgPd2.iloc[:, 9]
selec_AgPd2 = data_AgPd2.iloc[:, 10]
C_balans_sqrd2 = data_AgPd2.iloc[:, 11]

tabel_AgPd2 = data_AgPd2.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]].copy()
tabel_AgPd2.columns = [
    "exp_numb", "flow (mL/min)", "WHSV (cm^3/h/g cat.)",
    "vol. % C2H2", "vol. % C2H4", "vol. % H2", "vol. % He",
    "vol. % CO", "mass cat. (mg)", "conv", "selec", "C-balans",
]
display(tabel_AgPd2)
```

**Table cells:** the displayed table contains the header-like row at display index 0 and `EXP1`–`EXP23` at indices 1–23. The exact checked Pd₂Ag response cells on this page are listed in the page-78 section above. Remaining small numeric cells are `[unclear]` where the image does not support a confident character-by-character reading.

### PDF page 79 / printed page 73 — Pd₃Ag and Pd₀Ag field mapping

```python
# AgPd3 columns follow the same input order as AgPd2.
exp_numb_AgPd3 = data_AgPd3.iloc[:, 0]
flow_AgPd3 = data_AgPd3.iloc[:, 1]
WHSV_AgPd3 = data_AgPd3.iloc[:, 2]
vol_percent_C2H2_AgPd3 = data_AgPd3.iloc[:, 3]
vol_percent_C2H4_AgPd3 = data_AgPd3.iloc[:, 4]
vol_percent_H2_AgPd3 = data_AgPd3.iloc[:, 5]
vol_percent_He_AgPd3 = data_AgPd3.iloc[:, 6]
vol_percent_CO_AgPd3 = data_AgPd3.iloc[:, 7]
m_cat_AgPd3 = data_AgPd3.iloc[:, 8]
conv_AgPd3 = data_AgPd3.iloc[:, 9]
selec_AgPd3 = data_AgPd3.iloc[:, 10]
C_balance_AgPd3 = data_AgPd3.iloc[:, 11]

tabel_AgPd3 = data_AgPd3.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]].copy()
tabel_AgPd3.columns = [
    "exp_numb", "flow (mL/min)", "WHSV (cm^3/h/g cat.)",
    "vol. % C2H2", "vol. % C2H4", "vol. % H2", "vol. % He",
    "vol. % CO", "mass cat. (mg)", "conv", "selec", "C-balans",
]
display(tabel_AgPd3)

# 0. AgPd0
exp_numb_AgPd0 = data_AgPd0.iloc[:, 0]  # exp. number AgPd0
flow_AgPd0 = data_AgPd0.iloc[:, 1]  # flow per exp. number AgPd0
WHSV_AgPd0 = data_AgPd0.iloc[:, 2]  # Contact time per exp. number AgPd0
vol_percent_C2H2_AgPd0 = data_AgPd0.iloc[:, 3]  # vol.% C2H2 AgPd0
vol_percent_C2H4_AgPd0 = data_AgPd0.iloc[:, 4]  # vol.% C2H4 AgPd0
vol_percent_H2_AgPd0 = data_AgPd0.iloc[:, 5]  # vol.% H2 AgPd0
vol_percent_He_AgPd0 = data_AgPd0.iloc[:, 6]  # vol.% He AgPd0
vol_percent_CO_AgPd0 = data_AgPd0.iloc[:, 7]  # vol.% CO AgPd0
m_cat_AgPd0 = data_AgPd0.iloc[:, 8]  # mass cat. AgPd0
conv_AgPd0 = data_AgPd0.iloc[:, 9]  # conversion of AgPd0 through experiment
selec_AgPd0 = data_AgPd0.iloc[:, 10]  # selectivity of AgPd0 through experiment
C_balans_AgPd0 = data_AgPd0.iloc[:, 11]  # carbon balance of AgPd0 through experiment

tabel_AgPd0 = data_AgPd0.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]].copy()
tabel_AgPd0.columns = [
    "exp_numb", "flow (mL/min)", "WHSV (cm^3/h/g cat.)",
    "vol. % C2H2", "vol. % C2H4", "vol. % H2", "vol. % He",
    "vol. % CO", "mass cat. (mg)", "conv", "selec", "C-balans",
]
display(tabel_AgPd0)
```

**Table cells:** the Pd₃Ag display reads `EXP1`–`EXP4`, `[source display ellipsis]`, `EXP73`–`EXP77`, and `78 rows × 12 columns` (the count includes its header-like row). The middle records are absent from the printed display, not merely unreadable. The Pd₂Ag tail includes `EXP24`–`EXP42`; row values too small to distinguish exactly are marked `[unclear]` rather than reconstructed.

### PDF page 80 / printed page 74 — combined catalyst table

```python
def prepare_table(tabel, catalyst_name):
    df_temp = tabel.copy()
    df_temp["catalyst"] = catalyst_name
    return df_temp

df_all = pd.concat([
    prepare_table(tabel_AgPd0, "AgPd0"),
    prepare_table(tabel_AgPd2, "AgPd2"),
    prepare_table(tabel_AgPd3, "AgPd3"),
], ignore_index=True)
display(df_all)
```

The output shows a `163 rows × 13 columns` footer. The visible head/tail rows and their six-decimal response cells are not all confidently readable; intermediate rows are hidden by the DataFrame display. No values are filled from another CSV.

### PDF page 81 / printed page 75 — constants, catalyst masses, PFR and standard LHHW rate function

```python
R = 8.314                         # J mol^-1 K^-1
D = 0.5                           # diameter; cm
rho = 2.65                        # density SiO2; g cm^-3
m_cat_AgPd0 = data_AgPd0.iloc[2, 8]  # mass of AgPd0 catalyst
m_cat_AgPd2 = data_AgPd2.iloc[2, 8]  # mass of AgPd2 catalyst
m_cat_AgPd3 = data_AgPd3.iloc[2, 8]  # mass of AgPd3 catalyst
T = 373                           # 100 Celsius
P_total = 100000                  # Pa
A = (np.pi * D**2) / 4           # reactor area; cm^2
dW_dz = rho * A * 100            # g m^-1

m_cat_AgPd0 = pd.to_numeric(data_AgPd0.iloc[:, 8].astype(str).str.replace(",", ".", regex=False), errors="coerce").dropna().iloc[0]
m_cat_AgPd2 = pd.to_numeric(data_AgPd2.iloc[:, 8].astype(str).str.replace(",", ".", regex=False), errors="coerce").dropna().iloc[0]
m_cat_AgPd3 = pd.to_numeric(data_AgPd3.iloc[:, 8].astype(str).str.replace(",", ".", regex=False), errors="coerce").dropna().iloc[0]

W_total_AgPd0 = m_cat_AgPd0 / 1000  # mg to g
W_total_AgPd2 = m_cat_AgPd2 / 1000  # mg to g
W_total_AgPd3 = m_cat_AgPd3 / 1000  # mg to g
L_total_AgPd0 = W_total_AgPd0 / dW_dz  # calculation of reactor length AgPd0; m
L_total_AgPd2 = W_total_AgPd2 / dW_dz  # calculation of reactor length AgPd2; m
L_total_AgPd3 = W_total_AgPd3 / dW_dz  # calculation of reactor length AgPd3; m

# Reproducibility
rng = np.random.default_rng(seed=42)

def pfr_rhs(z, F, LHHW, T, P_total, dW_dz, k1, k2, K1, K2, Kinh, KH):
    F = np.maximum(F, 0.0)        # numerical safety; negative flows are unphysical
    F_tot = F.sum()
    if F_tot <= 0:
        return np.zeros_like(F)
    y = F / F_tot                  # mole fraction
    p_C2H2, p_C2H4, p_C2H6, p_H2, p_He, p_CO = y * P_total
    r1, r2 = LHHW(p_C2H2, p_C2H4, p_H2, T, k1, k2, K1, K2, Kinh, KH)
    dFdz = dW_dz * np.array([-r1, r1-r2, r2, -r1-r2, 0.0, 0.0])
    return dFdz

def solve_pfr(F0, L_total, LHHW, T, P_total, dW_dz,
              k1, k2, K1, K2, Kinh, KH, n_points=50):
    z_eval = np.linspace(0.0, L_total, n_points)
    sol = solve_ivp(
        lambda z, F: pfr_rhs(z, F, LHHW, T, P_total, dW_dz,
                             k1, k2, K1, K2, Kinh, KH),
        t_span=(0.0, L_total), y0=F0, method="LSODA", t_eval=z_eval,
        rtol=1e-9, atol=1e-14,
    )
    if not sol.success:
        raise RuntimeError(f"Integration failed: {sol.message}")
    return sol.t, sol.y

def LHHW(p_C2H2, p_C2H4, p_H2, T, k1, k2, K1, K2, Kinh, KH):
    pA = max(p_C2H2, 0.0) / 1e5  # pressure from Pa to bar [source comment]
    pE = max(p_C2H4, 0.0) / 1e5  # pressure from Pa to bar [source comment]
    pH = max(p_H2, 0.0) / 1e5    # pressure from Pa to bar [source comment]
    denom = (1.0 + K1*pA + K2*pE + KH*pH)**2
    r1 = k1*K1*pA*KH*pH / denom
    r2 = k2*K2*pE*KH*pH / (denom * (1.0 + Kinh*pA))
    return r1, r2
```

The displayed output prints reactor area `0.19634954006936207 cm²` and bed lengths approximately `0.0019218710109210008 m` (AgPd0), `0.0014414032581907506 m` (AgPd2), and `0.0019218710109210008 m` (AgPd3). In the literal code, the `denom` shared by `r1` and `r2` includes `KH*pH`; the printed equation immediately above the code is transcribed separately. This note records the two source renderings without choosing between them.

### PDF page 82 / printed page 76 — flow conversion

The preceding `Simulation (check)` cell is readable:

```python
k1_test = 1.5e-6  # /bar
k2_test = 1e-6    # /bar
K1_test = 100     # /bar
K2_test = 0.1     # /bar
Kinh_test = 3     # /bar
KH_test = 1       # /bar
z, F = solve_pfr(
    [1e-6, 2e-6, 0.0, 1e-6, 69e-6, 0.0],
    L_total=L_total_AgPd0, LHHW=LHHW, T=T, P_total=P_total, dW_dz=dW_dz,
    k1=k1_test, k2=k2_test, K1=K1_test, K2=K2_test,
    Kinh=Kinh_test, KH=KH_test,
)
ax = plt.gca()
ax.plot(z, F[0], label="C2H2")
ax.plot(z, F[1], label="C2H4")
ax.plot(z, F[2], label="C2H6")
plt.legend()
```

```python
def V_flow_flow(df, R, T, P, flow_col):
    df = df.copy()
    # remove repeated text rows
    df = df[df[flow_col] != "flow [mL/min]"].reset_index(drop=True)
    # flow from mL/min to mol/s
    df["V_m3_s"] = df[flow_col] * 1e-6 / 60
    df["F_tot_mol_s"] = P * df["V_m3_s"] / (R * T)
    # vol.% to fraction
    df["y_C2H2"] = df["vol. % C2H2"] / 100
    df["y_C2H4"] = df["vol. % C2H4"] / 100
    df["y_H2"] = df["vol. % H2"] / 100
    df["y_He"] = df["vol. % He"] / 100
    df["y_CO"] = df["vol. % CO"] / 100
    # components in mol/s
    df["F_C2H2_in"] = df["y_C2H2"] * df["F_tot_mol_s"]
    df["F_C2H4_in"] = df["y_C2H4"] * df["F_tot_mol_s"]
    df["F_H2_in"] = df["y_H2"] * df["F_tot_mol_s"]
    df["F_He_in"] = df["y_He"] * df["F_tot_mol_s"]
    df["F_CO_in"] = df["y_CO"] * df["F_tot_mol_s"]
    df["F_C2H6_in"] = 0.0
    return df
```

The displayed call and output preview identify `160 rows × 26 columns`; the DataFrame shows head/tail rows separated by an ellipsis. Intermediate cells are not present on the page.

The page also applies the flow conversion to `tabel_AgPd0`, `tabel_AgPd2`, and `tabel_AgPd3` to create `data_AgPd0_mol_s`, `data_AgPd2_mol_s`, and `data_AgPd3_mol_s`. The readable combined-table call is `df_all = V_flow_flow(df_all, R, T, P_total, flow_col="flow (mL/min)")`, followed by `display(df_all)`.

### PDF page 83 / printed page 77 — simulated and experimental responses

```python
def conv_selec_sim(F0, F_out, F_C4=0):
    F_C2H2_feed = F0[0]  # in
    F_C2H4_feed = F0[1]  # in
    F_C2H6_feed = F0[2]  # in
    F_C2H2_out = F_out[0]  # out
    F_C2H4_out = F_out[1]  # out
    F_C2H6_out = F_out[2]  # out
    F_H2_out = F_out[3]  # out
    C2H2_consumed = F_C2H2_feed - F_C2H2_out
    C2H6_formed = F_C2H6_out - F_C2H6_feed
    conversion_sim = C2H2_consumed / F_C2H2_feed * 100
    selectivity_sim = (1 - (C2H6_formed + 2*F_C4) / C2H2_consumed) * 100
    return conversion_sim, selectivity_sim, C2H2_consumed, C2H6_formed

sim_results = []
for i in range(0, len(df_all)):
    row = df_all.iloc[i]
    F0 = [row["F_C2H2_in"], row["F_C2H4_in"], row["F_C2H6_in"],
          row["F_H2_in"], row["F_He_in"], row["F_CO_in"]]
    z, F = solve_pfr(
        F0=F0, L_total=L_total_AgPd0, LHHW=LHHW, T=T, P_total=P_total,
        dW_dz=dW_dz, k1=k1_test, k2=k2_test, K1=K1_test, K2=K2_test,
        Kinh=Kinh_test, KH=KH_test,
    )
    F_out = F[:, -1]  # get outlet/recover from sim
    conversion_sim, selectivity_sim, C2H2_consumed, C2H6_formed = conv_selec_sim(
        F0=F0, F_out=F_out, F_C4=0,
    )  # calculation of X, S, etc.
    sim_results.append({"exp_numb": row["exp_numb"], "catalyst": row["catalyst"],
                        "conv_sim": conversion_sim, "selec_sim": selectivity_sim})
sim_results_df = pd.DataFrame(sim_results)
display(sim_results_df)

exp_results = []
for i in range(0, len(df_all)):
    row = df_all.iloc[i]
    exp_results.append({"exp_numb": row["exp_numb"], "catalyst": row["catalyst"],
                        "conv_exp": row["conv"], "selec_exp": row["selec"]})
exp_results_df = pd.DataFrame(exp_results)
display(exp_results_df)

comparison_df = pd.merge(sim_results_df, exp_results_df,
                         on=["exp_numb", "catalyst"], how="inner")
display(comparison_df)
```

The output displays have `160 rows × 4 columns` for each response table and `160 rows × 6 columns` for the merge. Only the pandas head/tail rows appear; the omitted middle is a source display ellipsis.

### PDF page 84 / printed page 78 — per-experiment RMSE and plotting

```python
def calc_RMSE(conv_sim, conv_exp, selec_sim, selec_exp):
    RMSE = np.sqrt(((conv_sim - conv_exp)**2 + (selec_sim - selec_exp)**2) / 2)
    return RMSE

RMSE_results = []
for i in range(0, len(df_all)):
    row = comparison_df.iloc[i]
    RMSE = calc_RMSE(
        conv_sim=row["conv_sim"], conv_exp=row["conv_exp"],
        selec_sim=row["selec_sim"], selec_exp=row["selec_exp"],
    )
    RMSE_results.append(RMSE)
comparison_df["RMSE"] = RMSE_results
display(comparison_df)
print("Overall RMSE =", np.sum(RMSE_results) / len(df_all.iloc[:, 0]))
```

The source output is `Overall RMSE = 472.42114981326106`. The visible 160-row, seven-column RMSE DataFrame is head/tail only. The plotting cell loops over catalyst names and makes separate conversion and selectivity parity plots:

```python
for catalyst_name in comparison_df["catalyst"].unique():
    df_cat = comparison_df[comparison_df["catalyst"] == catalyst_name]
    plt.figure()
    plt.scatter(df_cat["conv_exp"], df_cat["conv_sim"])
    plt.plot([0, 100], [0, 100], linestyle="--")
    plt.xlabel("Experimental conversion (%)")
    plt.ylabel("Simulated conversion (%)")
    plt.title(f"Parity plot: C2H2 conversion - {catalyst_name}")
    plt.show()

    plt.figure()
    plt.scatter(df_cat["selec_exp"], df_cat["selec_sim"])
    plt.plot([0, 100], [0, 100], linestyle="--")
    plt.xlabel("Experimental selectivity (%)")
    plt.ylabel("Simulated selectivity (%)")
    plt.title(f"Parity plot: C2H4 selectivity - {catalyst_name}")
    plt.show()
```

### PDF page 85 / printed page 79 — fit subset selection

```python
# Only AgPd0
df_fit = df_all[df_all["catalyst"] == "AgPd0"].copy()
# All data
# df_fit = df_all.copy()
display(df_fit)
```

The output reports `41 rows × 26 columns`. Pandas displays a head and tail, not all 41 records; it also elides middle columns in each wide row. Those omitted values are not inferred from the input table.

### PDF page 86 / printed page 80 — standard-model optimization functions

```python
# For now, all the same. Can later be further improved
bounds = [
    (1e-10, 1),     # k1
    (1e-10, 1),     # k2
    (1e-10, 1000),  # K1
    (1e-10, 1000),  # K2
    (1e-10, 1000),  # Kinh
    (1e-10, 1000),  # KH
]

def make_comparison_df(df, k1, k2, K1, K2, Kinh, KH):
    sim_results = []
    for i in range(0, len(df)):
        row = df.iloc[i]
        F0 = [row["F_C2H2_in"], row["F_C2H4_in"], row["F_C2H6_in"],
              row["F_H2_in"], row["F_He_in"], row["F_CO_in"]]
        z, F = solve_pfr(
            F0=F0,
            L_total=L_total_AgPd0,
            LHHW=LHHW,
            T=T,
            P_total=P_total,
            dW_dz=dW_dz,
            k1=k1,
            k2=k2,
            K1=K1,
            K2=K2,
            Kinh=Kinh,
            KH=KH,
        )
        F_out = F[:, -1]
        conversion_sim, selectivity_sim, C2H2_consumed, C2H6_formed = conv_selec_sim(
            F0=F0, F_out=F_out, F_C4=0,
        )
        sim_results.append({"exp_numb": row["exp_numb"], "catalyst": row["catalyst"],
                            "conv_sim": conversion_sim, "selec_sim": selectivity_sim})
    sim_results_df = pd.DataFrame(sim_results)
    exp_results = []
    for i in range(0, len(df)):
        row = df.iloc[i]
        exp_results.append({
            "exp_numb": row["exp_numb"],
            "catalyst": row["catalyst"],
            "conv_exp": row["conv"],
            "selec_exp": row["selec"],
        })
    exp_results_df = pd.DataFrame(exp_results)
    comparison_df = pd.merge(
        sim_results_df,
        exp_results_df,
        on=["exp_numb", "catalyst"],
        how="inner",
    )
    return comparison_df

def calc_overall_RMSE(comparison_df):
    RMSE_values = []
    for i in range(0, len(comparison_df)):
        row = comparison_df.iloc[i]
        RMSE_i = calc_RMSE(
            conv_sim=row["conv_sim"],
            conv_exp=row["conv_exp"],
            selec_sim=row["selec_sim"],
            selec_exp=row["selec_exp"],
        )
        RMSE_values.append(RMSE_i)
    overall_RMSE = np.mean(RMSE_values)
    return overall_RMSE

def objective_function(params, df):
    k1, k2, K1, K2, Kinh, KH = params
    comparison_df = make_comparison_df(df, k1, k2, K1, K2, Kinh, KH)
    RMSE = calc_overall_RMSE(comparison_df)
    if not np.isfinite(RMSE):
        return 1e10
    return RMSE
```

The six bounds and function bodies are readable on PDF p. 86. The code uses `L_total_AgPd0` inside `make_comparison_df` and contains no `r1_max` or `n_inh` parameters.

### PDF page 87 / printed page 81 — test call and optimizer invocation

```python
test_rmse = objective_function([1, 1, 1, 1, 1, 1], df_fit)
print("Test RMSE:", test_rmse)

result = differential_evolution(
    objective_function, bounds=bounds, args=(df_fit,), strategy="best1bin",
    maxiter=50, popsize=42, tol=1e-8, seed=42, polish=True, disp=True,
)
best_k1, best_k2, best_K1, best_K2, best_Kinh, best_KH = result.x
print("Best k1:", best_k1)
print("Best k2:", best_k2)
print("Best K1:", best_K1)
print("Best K2:", best_K2)
print("Best Kinh:", best_Kinh)
print("Best KH:", best_KH)
print("Best RMSE:", result.fun)
```

The source output prints `Test RMSE: 2296.780351681826`, followed by the best fitted values `k1 = 7.105213653332459e-05`, `k2 = 1.049169014537864e-05`, `K1 = 936.2110142510355`, `K2 = 10.207742660587007`, `Kinh = 971.9975266336327`, `KH = 3.331935118563628`, and `Best RMSE = 6.439535000722007`. The 50 per-generation objective lines are visible in the source image but are not copied as they are progress output rather than code or table entries.

### PDF page 88 / printed page 82 — fitted comparison and parity plots

```python
comparison_de_df = make_comparison_df(
    df_fit, best_k1, best_k2, best_K1, best_K2, best_Kinh, best_KH)
display(comparison_de_df)

cat_name = "AgPd0"
de_steps = result.nit
best_RMSE = result.fun
df_cat_2 = comparison_de_df[comparison_de_df["catalyst"] == cat_name]
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
band = 0.10  # 10% relative deviation band
x_line = np.linspace(0, 100, 200)

conv_within_10pct = (
    (df_cat_2["conv_sim"] >= df_cat_2["conv_exp"] * (1 - band)) &
    (df_cat_2["conv_sim"] <= df_cat_2["conv_exp"] * (1 + band))
)
selec_within_10pct = (
    (df_cat_2["selec_sim"] >= df_cat_2["selec_exp"] * (1 - band)) &
    (df_cat_2["selec_sim"] <= df_cat_2["selec_exp"] * (1 + band))
)
n_conv_within = conv_within_10pct.sum()
n_selec_within = selec_within_10pct.sum()
total_cat_points = len(df_cat_2)
perc_conv_within = n_conv_within / total_cat_points * 100
perc_selec_within = n_selec_within / total_cat_points * 100
rmse_conv = np.sqrt(np.mean((df_cat_2["conv_sim"] - df_cat_2["conv_exp"])**2))
rmse_selec = np.sqrt(np.mean((df_cat_2["selec_sim"] - df_cat_2["selec_exp"])**2))

# Conversion parity plot
axes[0].scatter(df_cat_2["conv_exp"], df_cat_2["conv_sim"])
axes[0].plot([0, 100], [0, 100], linestyle="--", color="gray")  # parity-line
axes[0].plot(x_line, x_line * (1 + band), linestyle="--", alpha=0.45,
             color="green", label="±10% band")  # error band
axes[0].plot(x_line, x_line * (1 - band), linestyle="--", alpha=0.45,
             color="green")  # error band
axes[0].set_xlabel("Experimental (%)")
axes[0].set_ylabel("Simulated (%)")
axes[0].set_title("C2H2 conversion")
axes[0].text(
    0.05, 0.95,
    f"RMSE: {rmse_conv:.2f}\\n"
    f"Within ±10% rel.: {n_conv_within}/{total_cat_points}\\n"
    f"({perc_conv_within:.1f}%)",
    transform=axes[0].transAxes,
    verticalalignment="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
)
axes[0].grid(True, alpha=0.1)

# Selectivity parity plot
axes[1].scatter(df_cat_2["selec_exp"], df_cat_2["selec_sim"])
axes[1].plot([0, 100], [0, 100], linestyle="--", color="gray")  # parity-line
axes[1].plot(x_line, x_line * (1 + band), linestyle="--", alpha=0.45,
             color="green", label="±10% band")  # error band
axes[1].plot(x_line, x_line * (1 - band), linestyle="--", alpha=0.45,
             color="green")  # error band
axes[1].set_xlabel("Experimental (%)")
axes[1].set_ylabel("Simulated (%)")
axes[1].set_title("C2H4 selectivity")
axes[1].text(
    0.05, 0.95,
    f"RMSE: {rmse_selec:.2f}\\n"
    f"Within ±10% rel.: {n_selec_within}/{total_cat_points}\\n"
    f"({perc_selec_within:.1f}%)",
    transform=axes[1].transAxes,
    verticalalignment="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
)
axes[1].grid(True, alpha=0.1)
fig.suptitle("Parity plots: AgPd0", fontsize=18)
fig.text(
    0.5, 0.05,
    f"LHHW with all K's implemented and C2 inhibition | DE steps: {de_steps} | best RMSE: {best_RMSE:.4f}",
    ha="center", fontsize=12,
)
fig.text(
    0.5, 0.0,
    f"k1 = {best_k1:.4f}, k2 = {best_k2:.4f}, K1 = {best_K1:.4f}, K2 = {best_K2:.4f}, Kinh = {best_Kinh:.4f}, KH = {best_KH:.4f}",
    ha="center", fontsize=12,
)
plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.show()
```

The source comparison DataFrame continues directly across PDF pp. 87–88 and reports `41 rows × 6 columns`; its displayed rows 0–40 are present across the two page images, without a source ellipsis. The `conv_exp`/`selec_exp` columns are processed experimental responses included in this standard-model output; `conv_sim`/`selec_sim` are predictions. This table is not a raw measurement table or the final Figure 6.6 fit. PDF p. 80 and p. 83 print EXP3 selectivity as `98.759845`, while this comparison table prints `98.759846`; both source readings are preserved without harmonizing them. The parity-plot output itself is cut off at the lower edge of PDF p. 88; no graph points are digitized here.

## Transcriber notes — not source text

1. Table E.1–E.3 are standard-model variant comparisons. They are not the eight-parameter final vectors in main-text Figure 6.6.
2. Appendix F includes processed Pd₂Ag conversion/selectivity rows, despite the absence of a raw workbook/GC record in this repository. The Pd₃Ag table display is truncated; the displayed 77-row count comes from its DataFrame footer/combined count, not from a recovered raw workbook.
3. Appendix F's readable code passages across PDF pp. 78–88 are now transcribed above. The source does not expose the original workbook, and the pandas displays omit rows/columns with ellipses or show raster digits too small to certify. The exact omitted or unreadable regions are identified page by page. This closes the recoverable code transcription; it does not make the displayed data tables complete or recover the raw experiment data.
4. This transcription pass reads the page-81 pressure divisor as `1e5`. The earlier audit report's `1e3` statement was a transcription error; numerical results and audit calculations were not rerun or changed in this work.
