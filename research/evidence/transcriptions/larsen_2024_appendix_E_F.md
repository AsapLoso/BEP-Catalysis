# Larsen 2024 — Appendix E/F page-checked transcription

**Primary source:** Victor Larsen, *Semihydrogenation of acetylene to ethylene with a PdAg catalyst*, TU Delft Bachelor End Project, June 2024. The PDF in `research/evidence/original/` is the user-provided copy (SHA-256 `b5aaa2300ff9b64aca70e58cc5e4d8be30b3c12ee264e69af89e01c86f5120c9`); official-deposit equivalence is not established.

**Source renders:** 18 unmodified 300-DPI PNGs of one-based PDF pages 71–88: [page guide](../../../notebooks/benchmarks/source_renders/appendix_pages/README.md). Each image link below points to the checked original render. Printed page numbers are transcribed from the page itself.

**Method/status:** I inspected each of the 18 render PNGs visually, using OCR only to locate content. `checked_against_image` means the text explicitly transcribed in that page section was visually compared with the image. It does **not** mean every code line or every data-table cell on that page is transcribed. Tables E.1–E.3 are transcribed in full. Appendix F's large processed experiment tables and long notebook screenshots are only structurally/partially transcribed; their omitted cells are identified below. Those pages remain `ambiguous` for a complete transcription. No OCR draft is presented as a verified transcript.

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
- **Review status:** `ambiguous` (visible excerpts checked; full code and table cells not transcribed)
- **Visible source structure:** Heading `Kinetic modeling Acetylene semihydrogenation`; notebook imports NumPy, pandas, Matplotlib, SciPy ODE/optimization functions and warning utilities; reads a local Excel workbook with one sheet per catalyst; comments explicitly exclude experiment 34 (Excel row 36) from the Pd₀Ag data; maps the Pd₂Ag columns to an experiment number, flow, WHSV, feed volume percentages, catalyst mass, conversion, selectivity and carbon balance.
- **Visible table headings:** `exp_numb`, `flow (mL/min)`, `WHSV (cm^3/h/g cat.)`, `vol. % C2H2`, `vol. % C2H4`, `vol. % H2`, `vol. % He`, `vol. % CO`, `mass cat. (mg)`, `conv`, `selec`, `C-balans` [sic]. A header-like input row precedes experiment rows in the displayed DataFrame.
- **Experiment IDs visible:** Pd₂Ag `EXP1`–`EXP23` (table continues on PDF page 79). The source display includes processed responses; these are not raw chromatograph areas or unprocessed measurements.
- **Selected processed-response cells transcribed from the displayed Pd₂Ag table** (full table has 42 rows across PDF pp. 78–79; this excerpt is not a replacement for the entire input table). Source columns are `exp_numb`, `conv`, `selec`, and `C-balans`:

  | ID | Conversion (%) | Selectivity (%) | C balance (%) |
  |---|---:|---:|---:|
  | EXP1 | 58.018857 | 95.600234 | 86.818862 |
  | EXP2 | 86.417763 | 94.243281 | 87.317188 |
  | EXP3 | 99.276357 | 84.886849 | 91.513288 |
  | EXP4 | 99.349524 | 55.846520 | 90.843877 |
  | EXP14 | 99.661391 | 27.756005 | 96.066297 |
  | EXP15 | 99.659019 | 57.629123 | 83.283371 |
  | EXP16 | 99.653853 | 36.294416 | 95.328362 |
  | EXP17 | 99.681646 | 47.284657 | 96.457802 |
  | EXP19 | 99.602241 | 25.834125 | 98.121920 |
  | EXP20 | 99.624922 | 10.648119 | 97.369070 |
  | EXP21 | 99.548308 | 68.096788 | 96.180869 |

- **Uncertain/omitted:** The dense screenshot contains many exact cells and source-code lines that are not transcribed here. Do not use these notes as a machine-readable replacement for the source table.

## PDF page 79 — Appendix F Pd₂Ag table end, Pd₃Ag preview, combined-table setup

- **Original image:** [page-79.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-79.png)
- **Printed page:** 73
- **Review status:** `ambiguous` (table shape and displayed IDs checked; full rows not transcribed)
- **Visible source structure:** Pd₂Ag table continues through `EXP42`, yielding 42 processed experiment rows. The Pd₃Ag table preview shows `EXP1`–`EXP4`, an ellipsis, and terminal displayed rows `EXP73`–`EXP77`; the printed DataFrame footer reads `78 rows × 12 columns` (including the header-like row). The Pd₀Ag extraction begins below it.
- **Transcribed table fields:** same 12 headings listed for PDF page 78.
- **Selected Pd₂Ag processed-response cells:** the source table visibly contains rows `EXP35`–`EXP38` for the acetylene-variation curve. Their response values are excerpted below and in the derived ID crosswalk; the table is displayed through `EXP42`.
- **Visible Pd₃Ag head rows:** `EXP1`–`EXP4` are displayed before the Pandas ellipsis. The flow-curve processed responses shown are respectively `(99.74857, 68.89139)`, `(99.714813, 56.165749)`, `(99.63909, 35.640171)`, and `(99.306389, -82.203658)` for conversion and selectivity (%). These are table outputs from the thesis's processed dataset, not raw GC measurements. The display does not show the middle Pd₃Ag rows.
- **Selected Pd₂Ag acetylene-series rows (source `conv` / `selec`, %):**

  | ID | Conversion (%) | Selectivity (%) |
  |---|---:|---:|
  | EXP35 | 79.318032 | 96.909178 |
  | EXP36 | 92.487792 | 89.667845 |
  | EXP37 | 92.832456 | 76.951782 |
  | EXP38 | 95.392858 | 50.886892 |
- **Uncertain/omitted:** The ellipsis is part of the original Pandas display; the Pd₃Ag middle rows are not printed on this page. The 42 Pd₂Ag numerical cells are not copied into this Markdown transcription.

## PDF page 80 — Appendix F Pd₀Ag processed response table and combined data

- **Original image:** [page-80.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-80.png)
- **Printed page:** 74
- **Review status:** `ambiguous` (table structure, filter and selected cells checked; full 41-row table not transcribed)
- **Visible source structure:** Pd₀Ag table contains `EXP1`–`EXP42` except `EXP34`, consistent with the earlier exclusion. The combined table preview is labelled `163 rows × 13 columns`; it includes one retained header-like row per catalyst in the displayed inputs. A note above constants reads: `All the constants that can be filled out beforehand, and turning DW [g] into Dz [m]. Through density of Al2O3 = 3.987 g/cm^3` [capitalization/grammar as printed].
- **Transcribed observation:** The values shown in the `conv`, `selec`, and `C-balans` columns are processed results, not raw GC chromatograms. Pd₂Ag has its own 42-row processed-response table; Pd₃Ag has a much longer but screen-truncated display.
- **Uncertain/omitted:** Full numerical rows are not retyped in this transcript. The 3.987 g cm⁻³ alumina note conflicts with the next page's code comment that sets `rho = 2.65` and labels it SiO₂ density; see the separate audit, not as an editorial correction to this source text.

## PDF page 81 — Appendix F geometry, reactor balances and standard LHHW equations

- **Original image:** [page-81.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-81.png)
- **Printed page:** 75
- **Review status:** `checked_against_image` for the constants, balance structure and displayed rate equations; code listing not fully transcribed
- **Visible constants (transcription):** `R = 8.314` (J mol⁻¹ K⁻¹); `D = 0.5` cm; `rho = 2.65` (comment: density SiO₂, g cm⁻³); catalyst masses read from the data tables; `T = 373` (comment: 100 Celsius); `P_total = 100000` Pa; `A = (np.pi * D**2)/4` cm²; `dW_dz = rho * A * 100` g m⁻¹. The displayed catalyst lengths are approximately 0.001921871 m for Pd₀Ag, 0.001441403 m for Pd₂Ag, and 0.001921871 m for Pd₃Ag.
- **Visible balance structure:** `dF/dz = dW_dz × [-r1, r1-r2, r2, -r1-r2, 0, 0]` for C₂H₂, C₂H₄, C₂H₆, H₂, He and CO. The solver shown is `solve_ivp(..., method="LSODA", rtol=1e-9, atol=1e-14)`.
- **Displayed standard LHHW equations (as printed on this page):**

  \[
  r_1=\frac{k_1 K_1p_A K_3p_{H_2}}{(1+K_1p_A+K_2p_E+K_3p_{H_2})^2},\qquad
  r_2=\frac{k_2 K_2p_E K_3p_{H_2}}{(1+K_1p_A+K_2p_E)^2(1+K_{inh}p_A)}.
  \]

- **Visible pressure handling:** The displayed code clamps each partial pressure at zero and divides its Pa value by `1e3`; the inline comment calls this conversion “from Pa to bar.” The arithmetic division is by 1000, not 100000; this source-code label/scale is recorded without silently correcting it.
- **Uncertain/omitted:** The screenshot is a code image; not every line is retyped. The page's standard LHHW model is not the final extended model of main-text Eqs. 6.9–6.11.

## PDF page 82 — Appendix F ideal-gas feed conversion and combined rows

- **Original image:** [page-82.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-82.png)
- **Printed page:** 76
- **Review status:** `checked_against_image` for equations and row count; code screenshot not fully transcribed
- **Visible source calculation (transcribed):** A function removes repeated rows marked `flow [mL/min]`; calculates `V_m3_s = flow × 1e-6 / 60`; calculates total inlet molar flow as `F_tot_mol_s = P * V_m3_s / (R*T)`; divides feed volume percentages by 100 and multiplies by total molar flow to set species inlet flows. The rendered call supplies `R`, `T`, `P_total`, and a flow-column label. No explicit mass-flow-controller standard reference condition is stated.
- **Visible output:** Combined processed dataset footer `160 rows × 26 columns` after repeated header-like rows are removed (consistent with 41 Pd₀Ag + 42 Pd₂Ag + 77 Pd₃Ag experiment rows).
- **Uncertain/omitted:** Head and tail rows are shown with ellipsis; complete combined input and simulated-flow table is not printed.

## PDF page 83 — Appendix F simulated response table

- **Original image:** [page-83.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-83.png)
- **Printed page:** 77
- **Review status:** `ambiguous` (dataflow checked; output is truncated)
- **Visible source structure:** A three-reaction species-flow simulation is applied to the combined 160-row input DataFrame; simulated conversion/selectivity are assembled by experiment number and catalyst. Pandas output footer reads `160 rows × 4 columns`; the visible head and tail are not the full table.
- **Uncertain/omitted:** Exact intermediate rows and complete code are not transcribed. This is an output of the standard-model code, not raw experimental measurement.

## PDF page 84 — Appendix F RMSE computation and standard-model score

- **Original image:** [page-84.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-84.png)
- **Printed page:** 78
- **Review status:** `checked_against_image` for the displayed RMSE formula and score
- **Visible source formula:** `RMSE_i = sqrt(((conv_sim - conv_exp)^2 + (selec_sim - selec_exp)^2)/2)`; overall score is the arithmetic mean of the experiment RMSE values. The code calls `np.sum(RMSE_results)/len(df_all)`.
- **Visible output:** `Overall RMSE = 472.42114981326106` for this standard-model run over the combined table.
- **Coverage/uncertainty:** The numeric score is a standard-model code output, not Figure 6.6's final extended-model score. Table rows shown are truncated.

## PDF page 85 — Appendix F displayed fit subset

- **Original image:** [page-85.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-85.png)
- **Printed page:** 79
- **Review status:** `checked_against_image` for filter, row count and comments
- **Visible text/code:** Heading `Optimisation`; prose says “Need to use: differential_evolution” and says catalysts are fitted separately because each has its own kinetics. Under `Start fitting with the "best" data`, code sets `df_fit = df_all[df_all["catalyst"] == "AgPd0"].copy()`. The `#All data` line and `#df_fit = df_all.copy()` are commented. Output footer: `41 rows × 26 columns`.
- **Coverage/uncertainty:** This page documents an AgPd0 standard-model fit subset. It does not expose a final Pd₂Ag/Pd₃Ag selection mask.

## PDF page 86 — Appendix F standard fit function

- **Original image:** [page-86.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-86.png)
- **Printed page:** 80
- **Review status:** `ambiguous` (function structure checked; small code and exact bounds partly unreadable)
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

- **Uncertain/omitted:** The remaining function lines are not fully retyped. These bounds belong to the six-variable standard model and cannot evaluate the later eight-element Figure 6.6 parameter vectors.

## PDF page 87 — Appendix F Differential Evolution output

- **Original image:** [page-87.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-87.png)
- **Printed page:** 81
- **Review status:** `checked_against_image` for configuration/output summary
- **Visible run settings:** Differential Evolution output shows 50 steps, population size 42, tolerance `1e-8`, seed 42 and a polishing step with `L-BFGS-B`.
- **Visible output:** Standard-model AgPd0 optimization prints a best overall RMSE of approximately `6.439535`; the optimizer output is for the six-variable model/subset on PDF page 85. Table E.1 variant 5 reports the same score to four decimals (`6.4395`).
- **Uncertain/omitted:** The tiny per-step objective values and all optimized parameter digits are not fully transcribed here; use the image for exact code/output.

## PDF page 88 — Appendix F Pd₀Ag comparison rows and parity code

- **Original image:** [page-88.png](../../../notebooks/benchmarks/source_renders/appendix_pages/page-88.png)
- **Printed page:** 82
- **Review status:** `ambiguous` (plot code settings checked; 41-row table cells not fully transcribed)
- **Visible source structure:** Remaining Pd₀Ag comparison output rows are shown, followed by conversion/selectivity parity-plot code. The code sets a relative band `band = 0.10`, calculates the fraction of predicted points inside the band, and separately calculates conversion and selectivity RMSE. Plot labels show experimental vs simulated values; the screenshot begins/continues a Pd₀Ag parity plot.
- **Uncertain/omitted:** The complete 41-row output table and complete plotting cell are not retyped.

## Transcriber notes — not source text

1. Table E.1–E.3 are standard-model variant comparisons. They are not the eight-parameter final vectors in main-text Figure 6.6.
2. Appendix F includes processed Pd₂Ag conversion/selectivity rows, despite the absence of a raw workbook/GC record in this repository. The Pd₃Ag table display is truncated; the displayed 77-row count comes from its DataFrame footer/combined count, not from a recovered raw workbook.
3. The Appendix F pages are only **partially transcribed**. Any claimed “complete Appendix E/F transcription” would be false until the omitted Appendix F table cells and code are transcribed or individually marked unreadable. Those completion gates remain blocked in the audit report and TODO.
