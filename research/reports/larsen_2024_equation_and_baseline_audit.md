# Larsen 2024 PdAg — equation, data and baseline audit

**Status:** Executed source audit with a restricted selected-row numerical reproduction. The source equation and several numerical checks pass; exact reproduction of the final all-experiment fits remains blocked by missing final-model code, a partial processed-data display, unresolved source conventions, and plot/table response discrepancies.

**Scope:** This is an independent Agent 4 research record. It does not certify the uploaded PDF as the official June 2024 deposit, recover the missing workbook, refit the published parameters, or introduce CO.

## Source access and evidence classes

The primary file reviewed is the owner-uploaded 97-page PDF at *research/evidence/original/Larsen - 2024 - Semihydrogenation of acetylene to ethylene with a PdAg catalyst.pdf*, SHA-256 *b5aaa2300ff9b64aca70e58cc5e4d8be30b3c12ee264e69af89e01c86f5120c9*. That hash matches the uploaded copy and the tracked Git blob. Its internal metadata shows a 2026-06-26 compilation. An official 2024 repository copy or version history was not authenticated; a 2026 regeneration is possible, but equivalence of scientific content has not been established.

The searchable text file is machine-extracted and used as a page locator, not as authority for scan-only Appendix E/F text or mathematical superscripts. The appendix transcription links all 18 existing unmodified 300-DPI render images and records visually checked values, excerpts, and omissions. I checked targeted source pages for the questions below; I did not read every page of the thesis line by line.

| Source locator actually checked | What it supports | What it does not establish |
|---|---|---|
| Abstract, PDF p. 7 / printed p. 1; Section 4.2, PDF p. 21 / printed p. 15; Table 6.1, PDF p. 29 / printed p. 23 | Abstract and Table 6.1 say 100 °C; methods text says the reactor is held at 80 °C during experiments | Which temperature describes every reported experiment or the conditions used to fit Figure 6.6 |
| Eqs. 4.1–4.5, PDF p. 22 / printed p. 16; Eqs. 4.14–4.15, PDF p. 23 / printed p. 17 | GC-concentration response definitions and paired per-experiment RMSE followed by arithmetic averaging | Independent recomputation from raw GC response data, which are absent |
| Eqs. 6.9–6.11, PDF p. 43 / printed p. 37; Figure 6.6, PDF p. 44 / printed p. 38 | Printed model equations, all eight plotted parameter values, reported component/overall RMSE and N | The exact source code and row IDs used for the final extended-model fits |
| Appendix E tables, PDF pp. 73–75 / printed pp. 67–69 | Full standard-model variant comparison tables, visually transcribed | The final eight-parameter Figure 6.6 fit law |
| Appendix F, PDF pp. 78–88 / printed pp. 72–82 | All readable code; every displayed Pd0Ag/Pd2Ag/Pd3Ag processed-input row and legible cell; full 41-row Pd0Ag standard-model comparison display; geometry, flow conversion, RMSE, filter and optimizer settings | Raw workbook/GC data; Pd3Ag rows hidden by the source ellipsis; final extended Pd2Ag/Pd3Ag ID masks; elided columns and head/tail preview rows in intermediate DataFrames; marked unreadable/cropped cells |

The current GitHub issue #11 is the tracking reference for this audit. The new notebook, report and derived tables supersede earlier blanket-completion language. The historical benchmark notebook and its original parameter/curve files were not edited.

## Source transcription and model findings

### Equations and competing readings

Direct inspection of the equation image gives:

- Eq. 6.9 has the C₂H₂/C₂H₄/H₂ adsorption sum squared in the raw first-reaction rate.
- Eq. 6.10 caps the first rate as r₁ = r₁,raw / (1 + r₁,raw/r₁,max).
- Eq. 6.11 prints the first adsorption factor in r₂ without a superscript; the inhibition factor is raised to nᵢₙₕ.
- Appendix F's *standard* LHHW code instead uses a squared first adsorption factor and a first-power inhibition factor. The historical benchmark uses that squared factor and the later fitted inhibition exponent.

The final extended Figure 6.6 fit implementation is not shown. Plausible explanations remain a missing superscript in the main-text equation, an implementation change between standard and extended models, or a coding/formula mismatch. The fixed-vector numerical comparison below shows consequences; it cannot establish which formula generated Figure 6.6.

The displayed Appendix F Differential Evolution bounds on PDF p. 86 / printed p. 80 are six-variable bounds for k₁, k₂, K₁, K₂, Kᵢₙₕ and K_H: the first two upper bounds are 1 and the four adsorption/inhibition upper bounds are 1000, each with a lower bound of 1e-10. This standard-model function does not include r₁,max or nᵢₙₕ and cannot evaluate the Figure 6.6 vectors.

### Parameters, units and reactor conventions

Figure 6.6 visually reports all eight values per catalyst. The vectors and literature scores are transcribed in *research/evidence/transcriptions/larsen_2024_main_source_excerpts.md*; no unit table accompanies the vectors.

Appendix F PDF p. 81 / printed p. 75 shows R=8.314 J mol⁻¹ K⁻¹, D=0.5 cm, rho=2.65 g cm⁻³ labelled SiO₂, T=373 K labelled 100 Celsius, Ptotal=100000 Pa, A=πD²/4 and dW/dz=rho A × 100 g m⁻¹. The preceding PDF p. 80 / printed p. 74 instead describes a density of Al₂O₃=3.987 g cm⁻³. These source statements conflict; the audit notebook adopts the page-81 SiO₂ value as a candidate convention because it is the value used in the displayed geometry code and historical notebook.

Appendix F divides each partial pressure in Pa by `1e5` and comments “from Pa to bar”; that divisor is consistent with the stated conversion. The earlier audit sentence that said `1e3` was a transcription error, corrected against PDF p. 81 in the source transcript; the numerical audit was not rerun and its calculations were not changed. The Appendix F test parameters carry `/bar` comments, but the final Figure 6.6 parameter basis is not identified. The existing parameter CSV's Pa and mol kg-cat⁻¹ s⁻¹ fields remain inferred conventions, not source-certified units. This audit keeps the historical notebook's candidate basis fixed for controlled comparison; source code and Figure 6.6 alone do not prove the final fitted units.

Appendix F PDF p. 82 / printed p. 76 converts V from mL min⁻¹ to m³ s⁻¹ and computes Ftotal=P V/(R T) using the page-81 values. No mass-flow-controller standard/reference condition is named. Five flow conventions were run as sensitivity cases: source code's 100 °C and 100 kPa, methods' 80 °C and 100 kPa, and illustrative 0/20/25 °C standard-volume references at 1 atm. Reactor pressure was held at 100 kPa and no temperature correction was applied to kinetic coefficients. Across these cases the squared-variant selected paired RMSE spans 5.18–10.45 pp (Pd0Ag), 4.82–10.89 pp (Pd2Ag), and 20.30–33.04 pp (Pd3Ag). This sensitivity does not identify the actual MFC basis.

The source response definitions use GC-derived concentrations and subtract ethane and twice the C4+ concentration in the selectivity numerator. The reduced model computes net ethylene formation divided by acetylene consumed. Equivalence depends on complete product/byproduct and carbon-balance coverage, which cannot be verified without the raw chromatograms/workbook.

### Processed rows, plotted responses and final fit subsets

Appendix F calls its table fields conv, selec and C-balans and its source-code comments identify them as experiment responses. These are author-processed experimental responses, not raw GC peak areas. The original workbook and chromatograms are not present.

- Pd0Ag: 42 input rows include a header-like row; source code excludes EXP34, leaving 41 rows. Figure 6.6 reports N=41. Appendix F p. 85 shows a 41-row Pd0Ag **standard-model** fit subset. Final extended-fit row identity is not published.
- Pd2Ag: Appendix F prints all 42 processed rows across PDF pp. 78–79; Figure 6.6 reports N=42. All 15 selected curve operating conditions were condition-matched to displayed rows and response cells were transcribed to a separate CSV. A condition match is not proof that a plotted marker and table row are the same record.
- Pd3Ag: Appendix F's displayed DataFrame reports 78 rows including one header-like row, i.e. 77 processed rows, but prints only EXP1–4 and EXP73–77 around an ellipsis. Figure 6.6 reports N=41, leaving 36 processed rows outside the reported count with no final-fit inclusion mask. Four selected Figure 6.1 flow conditions map to visible head rows; other selected curve IDs cannot be recovered from the displayed table.
- Combined: Appendix F reports 163 rows × 13 columns before removing repeated header-like rows and 160 × 26 afterwards. Figure 6.6 counts sum to 124. Counts imply 36 Pd3Ag processed rows are omitted from the final reported fit population if all Pd0Ag/Pd2Ag rows were included, but the source does not identify those IDs.

The existing curve CSV remains a 45-row selected chart subset: 15 exact Pd0Ag processed-table values plus 15 visually digitized Pd2Ag and 15 visually digitized Pd3Ag points, with the original ±2 pp chart-reading uncertainty labels. The new crosswalk does not overwrite those digitizations.

The source-table cross-check found four displayed-response differences outside that ±2 pp band:

| Catalyst / figure / x value | Matched Appendix F ID | Existing plotted digitization | Appendix F processed response | Difference (plot − table) |
|---|---|---:|---:|---:|
| Pd2Ag, Fig. 6.2, p(C₂H₂)=10 mbar, conversion | EXP37 | 100.0% | 92.832456% | +7.167544 pp |
| Pd2Ag, Fig. 6.2, p(C₂H₂)=15 mbar, conversion | EXP36 | 100.0% | 92.487792% | +7.512208 pp |
| Pd2Ag, Fig. 6.4, p(H₂)=100 mbar, selectivity | EXP21 | 57.0% | 68.096788% | −11.096788 pp |
| Pd3Ag, Fig. 6.1, GHSV=30000 h⁻¹, selectivity | EXP4 | −32.0% | −82.203658% | +50.203658 pp |

Other mapped selected Pd2Ag/Pd3Ag responses fall within the prior ±2 pp chart-reading band. The mismatches may reflect digitization error, a non-identical plotted record, a source table/figure discrepancy, or an earlier processing choice. Without the original workbook or exact plot source arrays, they remain unresolved and the old digitizations are preserved.

## Numerical reproduction

The separate *notebooks/benchmarks/larsen_2024_source_audit.ipynb* holds Figure 6.6 vectors fixed and compares only the Eq. 6.11 first-power reading to the historical/Appendix F squared reading. There is no parameter refit. It evaluates the prior 15-point-per-catalyst selected chart subset and, separately, visible processed table rows (15 Pd0Ag, 15 Pd2Ag, and 4 Pd3Ag).

| Catalyst | Eq. 6.11 first-power RMSE | Squared alternative RMSE | Difference (first − square) | Selected chart rows |
|---|---:|---:|---:|---:|
| Pd0Ag | 13.4450 | 5.2680 | +8.1770 | 15 |
| Pd2Ag | 15.4886 | 5.4700 | +10.0185 | 15 |
| Pd3Ag | 21.2881 | 21.0815 | +0.2066 | 15 |

The squared-case scores reproduce the historical stored outputs within 4.3e-7 pp. The printed first-power form materially worsens Pd0Ag/Pd2Ag selected-chart agreement with the same vectors, but this is not evidence that the final published fit used the squared form. The historical model/data provenance and source table/plot discrepancies limit interpretation.

Against the condition-matched author-processed table responses, paired subset RMSE is:

| Catalyst | Eq. 6.11 first-power | Squared alternative | Mapped processed rows |
|---|---:|---:|---:|
| Pd0Ag | 13.4450 | 5.2680 | 15 |
| Pd2Ag | 16.3833 | 6.1663 | 15 |
| Pd3Ag | 9.7003 | 9.5815 | 4 |

These source-row checks use unequal and incomplete subsets and are not the final fit-population RMSEs. Figure 6.6's published all-experiment results remain literature values only: Pd0Ag 5.0962 pp (N=41), Pd2Ag 5.4320 pp (N=42), Pd3Ag 7.1353 pp (N=41). There is no independently computed all-experiment score.

Numerical verification passed on the candidate basis:

- The paired RMSE implementation agrees with a direct Eq. 4.14–4.15 expression within 1e-12 pp.
- Stoichiometric carbon, hydrogen and helium invariants are zero to machine precision.
- A consistent Pa-to-kPa transformation of all reciprocal-pressure adsorption constants changes selected predictions by at most 7.47e-10 pp. This checks dimensional invariance in the implementation; it does not determine which unit basis Larsen used.
- Across 90 candidate-law/selected-row simulations, BDF vs Radau maximum response difference is 1.73e-5 pp; BDF at base vs tight tolerances differs by at most 1.69e-5 pp.
- The most negative integrated state is −6.62e-17 mol s⁻¹; maximum absolute inlet/outlet elemental-flow residual is 2.89e-19 mol atoms s⁻¹. These are numerical-scale errors.
- All 90 predictions and 450 flow-sensitivity predictions were finite and the tests passed at the notebook's asserted tolerances.

All derived outputs, including pointwise differences and per-case flow scenarios, are indexed in *research/evidence/derived/README.md*.

## Verification gates

| Gate | Result | Evidence / remaining condition |
|---|---|---|
| Uploaded PDF identity and page locators | PASS for the uploaded copy | SHA-256 matches the supplied binary; official 2024 deposit/version is not authenticated |
| Eq. 6.9/6.10 and printed Eq. 6.11 notation | PASS | Visually checked PDF p. 43; Eq. 6.11 first adsorption term has no superscript |
| Main-text vs Appendix F/historical law comparison | PASS as a discrepancy finding | Main body first power vs standard code/historical square; final extended fit code absent |
| Figure 6.6 eight values and reported scores | PASS as visual transcription | Parameter units and fitted implementation remain unknown |
| Appendix E tables E.1–E.3 | PASS | All displayed rows transcribed and visually checked |
| Appendix F recoverable transcription | PASS with source gaps | All readable code on PDF pp. 78–88, all displayed processed input-table rows/cells that can be read, and the complete 41-row Pd0Ag standard-model comparison display are transcribed with page locators. Six cell values across five rows are `[unclear]`; the Pd3Ag middle rows are absent in the source; the p. 87 comparison row is partly cropped/unreadable; intermediate DataFrame previews have omitted rows or columns, and the p. 85 `df_fit` display elides columns. |
| RMSE formula and subset implementation | PASS | Paired per-row RMSE then arithmetic mean reproduced |
| Selected plotted-curve numerical reproduction | PASS as a restricted calculation | 45-point selected set; no refit; does not recreate full Figure 6.6 |
| Selected plot points versus Appendix F rows | BLOCKED for four material discrepancies | Four mapped responses exceed ±2 pp; preserve source and digitization separately pending workbook or exact plot array |
| Pd0Ag/Pd2Ag row counts | PASS for count reconciliation | 41/42 match Figure 6.6 N; exact final extended-fit masks not shown |
| Pd3Ag final experiment IDs | BLOCKED | 77 processed rows versus N=41; 36 IDs not identified |
| Full all-experiment experimental RMSE | BLOCKED | Original workbook, raw GC records, Pd3Ag middle table, and final fit masks unavailable |
| Flow/temperature/parameter unit basis | BLOCKED | 80/100 °C conflict; MFC reference basis absent; final fitted units not printed; Appendix F's `1e5` Pa-to-bar divisor is internally consistent but does not authenticate the final fit's unit basis |
| No-CO scope | PASS | Larsen feeds/model concern H₂/C₂H₂/C₂H₄ with He dilution; no CO effect is modeled or inferred |

## Remaining uncertainties and handoff

The most defensible source statement for a future baseline is to keep three objects separate: the printed Eq. 6.11 first-power law; the Appendix F standard-model squared law; and the historical extended-model squared implementation. For Figure 6.6's final eight-parameter vectors, neither code path is proven. Continue to label pressure/rate units as inferred, preserve the source's stated temperature disagreement, and do not treat the old selected digitizations as the full measured dataset.

Before using this benchmark to support a hypothetical CO mechanism, obtain (or confirm unavailable) the original workbook/GC records, resolve the four pointwise table/plot mismatches, identify the 41 Pd3Ag fit IDs, verify the final extended-model formula and pressure basis, and establish the reactor/MFC reference conditions. No Larsen CO data exist for validating a CO adsorption term.

## Reproducibility receipt

- **Branch:** feat/larsen-pdag-benchmark
- **Execution environment:** Linux 6.18.55-x86_64 (glibc 2.41); Python 3.12.14; NumPy 2.3.5; pandas 2.2.3; SciPy 1.17.0; Matplotlib 3.10.8; nbformat 5.11.1; nbclient 0.11.0.
- **Command:** python notebooks/benchmarks/run_larsen_source_audit.py
- **Notebook execution:** nbclient, Python 3 kernel, timeout 600 s, working directory notebooks/benchmarks, top-to-bottom. The executable notebook writes its derived CSV outputs to research/evidence/derived/.
- **Measured runtime:** 29.095 s for the documented runner invocation (one full notebook execution).
- **Numerical tolerances:** BDF/Radau and base/tight response deltas <1e-4 percentage points; unit-rescaling response delta <1e-4 pp; minimum state >−1e-10 mol s⁻¹; elemental-flow residual <1e-10 mol atoms s⁻¹; paired-score direct-formula comparison atol 1e-12 pp; stored historical selected-score regression absolute delta <0.02 pp.
- **Runtime and artifact hash:** the original execution receipt and implementation commit SHA are recorded in the [source-branch TODO](https://github.com/AsapLoso/BEP-Catalysis/blob/adf33269fadc2a70891a144ed6dd86f25c58db25/TODO.md). This central reference import did not rerun the audit.
