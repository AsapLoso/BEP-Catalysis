# Schbib (1996) parameter and benchmark audit

**Date:** 2026-10-26 · **Branch:** `feat/schbib-co-benchmark` · **Plan:** owner-approved; execution completed independently · **Tracking issue:** [#10](https://github.com/AsapLoso/BEP-Catalysis/issues/10)

## Executive findings and gate receipt

The original printed Table 8 and the author-shared correction were kept as separate parameter sets. The original values and equations were checked visually against the archived article PDF. Public records support attributing the ResearchGate upload to the paper's first author: ACS identifies Noemí S. Schbib as an author, while ResearchGate lists Noemi Susana Schbib and says she uploaded the content. The correction text is also signed “Dr. Susana Schbib.” This is credible author attribution, but it does not authenticate the correction document's integrity or establish publisher approval. The linked PDF still returns 404, and no ACS correction record was found in the targeted DOI/issue checks.

The original printed set reproduces the historical Table 6 acetylene failure: the fresh mass-coordinate isothermal PFR predicts at most 0.841% C₂H₂ conversion where Table 6 reports 98.31–98.99%. The author-shared set brings all three acetylene conversions within 1.48 percentage points of Table 6, but its ethylene conversion remains far outside the provisional 2-point gate. Table 6 reproduction for both reported species is **BLOCKED**.

| Gate | Result |
|---|---|
| Original article Tables 3, 4, 6, 8 and Eqs. 22, 24, 25 | **PASS** for visual transcription; recorded in the checked transcription |
| Author-shared correction provenance | **PARTIAL** author attribution from ACS and ResearchGate records; **BLOCKED** for visual document verification and publisher/erratum confirmation |
| Distinct source sets and diagnostic sensitivities | **PASS**; no sensitivity row is presented as a physical source model |
| Numerical execution environment | **PASS**; compatible Python 3.12.14 runtime used under Rule 19; no install or dependency change |
| Internal implementation checks | **PASS**: stoichiometric element balance, finite/nonnegative accepted states, positive rate denominator, mol/kmol unit invariance, solver refinement, and Arrhenius/log sanity |
| Table 6 C₂H₂ alone, author-shared set | **PASS provisionally**: maximum absolute error 1.475 pp |
| Table 6 both species, author-shared set | **BLOCKED**: maximum C₂H₄ net-disappearance error 10.763 pp |
| Figures 1–4 | Figure 1 quantitative **BLOCKED**; Figure 2 partial rate-scale check only; Figures 3–4 partial C₂H₂ outlet checks, full model/profile reproduction **BLOCKED** |
| Agent 5 formulation handoff | **PASS** for the source-faithful Pd/α-Al₂O₃ reference formulation, with the corrected set marked unverified; combined PdAg–CO model remains gated on owner review and Agent 4's separate audit |

The 2 percentage-point acceptance threshold is a provisional engineering gate from the audit plan, not a confidence interval reported by Schbib. The article gives no Table 6 uncertainty bars and specifically cautions that ethylene conversion has large experimental error.

## Evidence classes and source audit

### Original article: visually checked source facts

The archived source is [`schbib_1996_front_end_acetylene_hydrogenation.pdf`](../literature/schbib_1996_front_end_acetylene_hydrogenation.pdf), SHA256 `4b4c2728f1ac1d73acdf74eef1f247203f3aa5b8ab38cace45d1f6e513dbc60a`. Rendered PDF pages 4, 6, 7 and 8 were checked at printed pages 1499, 1501, 1502 and 1503. The convenience text and article HTML helped locate source passages; they were not treated as visual verification. The article's primary record is [ACS DOI 10.1021/ie950600k](https://pubs.acs.org/doi/abs/10.1021/ie950600k).

- **Table 3, p.1499:** feed CH₄ 6.53%, C₂H₂ 0.52%, C₂H₄ 43.99%, C₂H₆ 26.72%, H₂ 22.1%, CO 150–5000 ppm; 100 cm³(STP)/min, catalyst mass 1–3 g, 1–35 atm, and 288–393 K.
- **Table 4, p.1499:** ICI 38-1 catalyst, α-Al₂O₃, 0.04 wt% Pd, apparent density 1.61 g/cm³, real density 3.61 g/cm³, 54.5% porosity, 1000 Å mean pore diameter, and the other characterization values in the checked transcription.
- **Table 6, p.1499:** 16 atm, `SV = 100 cm³(STP) g_cat⁻¹ min⁻¹`; the three CO/temperature/C₂H₂/C₂H₄ rows are 150/341/98.31/10.45, 1400/359/98.99/6.70, and 5000/393/98.62/6.08.
- The apparatus is a 10 mm internal-diameter stainless-steel tube immersed in a diethylene-glycol bath. A catalyst-contact thermocouple measured reaction temperature at an axial location, and wall temperature was also measured (p.1499).
- **Table 8, p.1502:** the printed table values and full common-denominator rate law were visually checked. The denominator exponent is 3. The printed adsorption parameters are `log A_H = 20.2`, `log A_CO = 13.6`, `log A_E = 0.26`, `log A_Et = −0.012`, and `log A_A = −16`, with energies shown in the transcription. Printed `k_A` and `k_E` units use gcat.
- **Eqs. 24–25, p.1501:** the simplified denominator retains `1 + sqrt(K_H C_H) + K_CO C_CO`. The preceding text says the three hydrocarbon adsorption terms have negligible effect. The source also says the positive tabulated H₂ and CO adsorption energies imply these constants increase with temperature; this agrees with the chosen Arrhenius interpretation `K = 10^(log A) exp(−E/(RT))`.
- **Table 6 and Figure 1 ethylene data:** the paper notes a large experimental error for C₂H₄ conversion due to its high concentration in the feed. No numerical uncertainties are given.
- **Internal source inconsistency:** p.1501 prose calls model `r_{2,35}` the best fit. Table 7 on p.1502 visibly marks the `r_{2,35}` rows with footnote `b`, which says “Rejected because E_act < 0.” This contradiction is not resolved here; Table 7 variance values were not used as validation evidence.

The exact source transcription is [schbib_1996_parameter_tables.md](../evidence/transcriptions/schbib_1996_parameter_tables.md). Original article HTML and extracted-text hashes were recorded as `c5e8a4aad1ba01a896e13bc51fd46e3df8cd02bcace4b252373e4f90dc4830c3` and `8b8bc1a142103cf0005b2f8d18b2d46c5b04b1d7ee665948fa457f2dfacc350c`; all three original files were left unchanged.

### Author-shared correction: text record, not confirmed erratum

The [ResearchGate record](https://www.researchgate.net/publication/231391687_Kinetics_of_Front-End_Acetylene_Hydrogenation_in_Ethylene_Production) lists Noemi Susana Schbib among the article authors and states that she uploaded the author content on 2021-01-25. The accessible note is signed “Dr. Susana Schbib” and gives `sschbib@plapiqui.edu.ar`. The [ACS article record](https://pubs.acs.org/doi/10.1021/ie950600k) independently lists Noemí S. Schbib as a coauthor at UNS-CONICET. Together these records make the note credibly author-attributed, but the uploader identity and appended document have not been independently confirmed by the publisher or an institutional repository.

The ResearchGate extracted text says incorrect values of `K_H`, `K_CO`, `K_E`, `K_Et`, and `K_A` appeared in Table 8 and gives replacement log values 17.2, 10.16, −2.74, −3.012, and −19.0. It labels `k_A` and `k_E` per kgcat, rates in kmol/(kgcat s), and concentrations in kmol/m³. The linked PDF returns 404, so the correction table and these unit labels cannot be checked against a rendered page. Targeted ACS DOI and issue checks exposed no correction record for this article; Crossref and direct ACS retrieval were inaccessible in this environment. These checks do not prove that no publisher correction exists.

The correction text is a credible author-attributed record, not an independently authenticated document or a confirmed erratum. The readable transcription preserves that distinction in [schbib_1996_author_table8_correction.md](../evidence/transcriptions/schbib_1996_author_table8_correction.md).

## Interpretation and controlled model comparisons

### Parameters, logs, units, and reactor basis

The source tables label their first parameter column `log A_i` without a base subscript. The implementation interprets this as base 10, sets `A = 10^(log10 A)`, and evaluates `p(T) = A exp(−E/(RT))`, with kcal/mol converted using 4184 J/kcal. This is the conventional interpretation for the tabulated kinetic pre-exponentials and is consistent with the source's stated positive-energy temperature trend; the base is still not printed explicitly. The distinction between the logarithm and its exponential is maintained in code and output.

Using kmol/m³, adsorption terms `K_i C_i` and `sqrt(K_H C_H)` are dimensionless. The printed rate coefficient units produce kmol/(mass·s) after multiplication by `C_A C_H` or `C_E C_H`. In the catalyst-mass coordinate `W [kg]`, a coefficient reported per gcat must be multiplied by 1000, equivalent to +3 in its log pre-exponential. The author-shared text gives the same numeric `log A` for `k_A` and `k_E` but labels those coefficients per kgcat, so its per-kg coefficient is 1000 times lower than the per-kg conversion of the printed gcat coefficient. The correction note's prose says the `K_*` values should change, yet its table also changes the `k_A`/`k_E` mass-unit labels without explanation. Because that table is not visually available, keep the parameter/unit combinations separate; do not silently treat the unit change as verified.

The model integrates `dF/dW = ν r`, avoiding an unsupported bed-length or packed-bed void assumption. At Table 6's 100 cm³(STP)/min flow and `SV = 100`, catalyst mass is 1 g. Table 4's porosity is a catalyst characterization value, not a measured interparticle bed void. The historical notebook multiplied real density by one minus this porosity to produce 1.64255 g/cm³, numerically close to apparent density 1.61 g/cm³; this is a particle-density estimate and does not identify packed-bed catalyst loading. Without interparticle void/loading, a physical `z` mapping cannot be inferred from Tables 3–4.

For Table 6 the primary comparison prescribes the listed temperature as uniform, an isothermal closure suited to isolating the kinetics in a glycol-bath experiment. A second adiabatic calculation is explicitly diagnostic only: it reuses historical reaction heats of −172 and −136 kJ/mol and NASA7 heat capacities from the old notebook. Those heats are not in the current GOAL or Schbib Tables 3, 4, 6, 8; the old notebook attributed the heat capacities to GRI-Mech 3.0 `gri30.yaml`, which was not independently audited here.

### Table 6 results

For the C₂H₄ comparison, the primary observable is net disappearance, `100(F_E,0 − F_E,out)/F_E,0`. Because reaction 1 produces ethylene, the separate reaction-2 extent is also reported. The paper does not give a formula beside Table 6 to settle this convention.

| CO (ppm) | T (K) | C₂H₂ measured | Original printed C₂H₂ | Author-shared C₂H₂ |
|---:|---:|---:|---:|---:|
| 150 | 341 | 98.31% | 0.8409% (−97.469 pp) | 99.7854% (+1.475 pp) |
| 1400 | 359 | 98.99% | 0.0099% (−98.980 pp) | 99.9982% (+1.008 pp) |
| 5000 | 393 | 98.62% | 0.0018% (−98.618 pp) | 100.0000% (+1.380 pp) |

| CO (ppm) | C₂H₄ measured | Original net disappearance | Original reaction-2 extent | Author-shared net disappearance | Author-shared reaction-2 extent |
|---:|---:|---:|---:|---:|---:|
| 150 | 10.45% | −0.00876% | 0.00118% | −0.31267% | 0.86688% |
| 1400 | 6.70% | −0.00011% | 0.00001% | 0.09353% | 1.27559% |
| 5000 | 6.08% | −0.00002% | 0.00000% | 0.72641% | 1.90850% |

The complete Table 6 gate fails for both source sets. The original set's maximum C₂H₂ error is 98.980 pp; the author-shared set passes only the C₂H₂ species gate, with maximum error 1.475 pp. Maximum absolute C₂H₄ errors for the original set are 10.459 pp (net disappearance) and 10.449 pp (extent); for the author-shared set they are 10.763 pp and 9.583 pp, respectively. Choosing between the two ethylene definitions does not satisfy the all-species gate.

The pre-audit notebook was preserved byte-for-byte as [`schbib_1996_steady_state_historical.ipynb`](../../notebooks/benchmarks/schbib_1996_steady_state_historical.ipynb); a temporary copy was freshly run before the audit. Its stored and freshly rerun Table 6 outputs agree: C₂H₂ predictions 0.8467%, 0.0099%, 0.0018%; the saved C₂H₄ output column reports reaction-2 extent as conversion (0.0012%, 0%, 0%), not net disappearance. The previous code used an adiabatic, simplified-law formulation. Its saved plots were not treated as fresh evidence; the old `schbib_fig1...fig4...png` files remain untouched.

### Failure isolation and coupled corrections

At 1400 ppm CO and 359 K, isolated changes from the original full-law model give:

| Diagnostic (not a source-consistent set) | C₂H₂ prediction |
|---|---:|
| Original printed full Table 8 | 0.00986% |
| Change only `log A(K_H)` to 17.2 | 0.01159% |
| Change only `log A(K_CO)` to 10.16 | 45.884% |
| Change only the three hydrocarbon adsorption entries | 0.00987% |
| Reinterpret the unchanged numeric kinetic coefficients on a kgcat rather than gcat basis | 0.0000099% |
| Change all adsorption entries but keep the original gcat rate basis | 100.000% |
| Complete author-shared set, including kgcat basis | 99.998% |

The CO pre-exponential change is `10^(13.6 − 10.16) = 2754.2`-fold downward at fixed temperature; the H₂ pre-exponential is 1000-fold downward. The one-factor CO diagnostic has the largest acetylene effect, while the H₂ and hydrocarbon-only diagnostics have little effect at this CO level. Changing the rate mass basis by itself reduces the predicted rate 1000-fold. The complete author-shared record couples all five adsorption entries with that mass-basis change; the denominator is cubed, so the effects are nonlinear and must not be assigned to a single correction. The deliberately mixed “all adsorption corrected, original gcat basis” diagnostic gives near-complete ethylene over-hydrogenation; it is not a candidate physical model.

The full Table 8 law and the paper's simplified Eqs. 24–25 produce less than 0.001 pp difference in each Table 6 conversion in these cases. Thus omitting `K_A`, `K_E`, and `K_Et` is not a credible explanation for the historical 98-point acetylene failure at these conditions.

### Common-denominator ratio and selectivity

At a common local state with positive `C_A`, both source laws share the same positive denominator, so `r_E/r_A = (k_E C_E)/(k_A C_A)`. The shared CO term cancels algebraically from this **local uncapped** ratio. CO can still alter an outlet/integrated result through the changing axial composition, rate history, and, with a nonisothermal closure, temperature trajectory. This cancellation does not demonstrate a preferential direct CO inhibition of one local rate; it also does not establish that overall outlet selectivity is invariant to CO.

## Figures 1–4 comparison and physical closure

| Source figure | Source facts checked | Computed comparison | Gate |
|---|---|---|---|
| 1, p.1499 | `SV = 33`, CO 800 ppm, 1 and 9 atm; plotted conversions vs temperature | Diagnostic uses 100 cm³(STP)/min from Table 3 to infer 3.03 g and an isothermal closure. No pointwise values were digitized. The old PNG has <1.2% C₂H₂ conversion while the paper's source panel spans roughly 70–100%. | **BLOCKED** quantitatively; prior PNG is not a reproduction |
| 2, p.1502 | Adiabatic rate-vs-temperature plot; Table 3 feed, `T0 = 325 K`, `P = 16.3 atm`, CO 1400 ppm; caption has no SV | Corrected-set feed/inlet rates at 325 K are `r_A = 4.6569×10⁻⁷` and `r_E = 6.6625×10⁻⁸` kmol kgcat⁻¹ s⁻¹ with `D = 14.2515`, on the plotted 10⁻⁸–10⁻⁶ scale. Full curve needs an unreported space velocity/residence condition. | **PARTIAL** inlet scale check; full curve **BLOCKED** |
| 3, p.1503 | Model III, `T0 = 325 K`, 16.3 atm, CO 1400 ppm; paper text reports 70.7% C₂H₂ and ~1.5 K overshoot | Borrowing 1 g from Table 6 gives corrected-set isothermal C₂H₂ 70.10% (−0.60 pp); this closure has zero temperature rise. | **PARTIAL** outlet check; profile **BLOCKED** |
| 4, p.1503 | Model III, `T0 = 345 K`, 16.3 atm, CO 1400 ppm; paper says close to 98% C₂H₂ and >3 K overshoot | Same borrowed 1 g condition gives 99.17% C₂H₂ (+1.17 pp from approximate text target); isothermal closure has zero temperature rise. | **PARTIAL** outlet check; profile **BLOCKED** |

Figures 3 and 4 specify model III, which includes gas-particle temperature and concentration differences. The source descriptions require external transfer coefficients and surface states; the audit did not establish the needed pellet diameter, measured wall-temperature profile, loaded catalyst mass/space velocity for the figure runs, or packed-bed void/length mapping from Tables 3, 4, 6 and 8. The 1000 Å entry is mean pore diameter, not pellet diameter. The near-match in outlet acetylene conversion under a borrowed Table 6 mass condition is a diagnostic cross-check only.

The historical heat assumption creates a strong boundary-condition difference. With the original set it changes the Table 6 conversions only slightly. With the author-shared set it predicts adiabatic outlet gas temperatures of about 468, 836 and 856 K for the three cases, far above the listed bath conditions. These are diagnostic outputs under unverified old heat/Cp inputs, not predictions for the glycol-bath reactor. They show why the adiabatic historical notebook is not a valid replacement for a source-matched laboratory heat model.

## Internal numerical checks and reproducibility

The notebook now uses `scipy.integrate.solve_ivp(method="Radau")` in catalyst-mass coordinates. A small zero floor is applied only when evaluating rates at negative implicit Newton trial concentrations near depletion; the accepted state and reported conversion are not clipped. Accepted Table 6 trajectory flows remain above −1×10⁻¹⁶ kmol/s.

- Stoichiometry conserves C, H, and O; relative elemental-flow drift is <9×10⁻¹⁶ across checked Table 6 trajectories.
- Minimum rate denominator is 23.612 for the author-shared cases and 2144.48 for the original cases across checked full/reduced trajectories.
- Rewriting the complete corrected 1400 ppm model in mol/m³ and mol/(kg s) changes C₂H₂ conversion by 3.19×10⁻¹¹ pp and net C₂H₄ conversion by 1.62×10⁻¹³ pp.
- Tightening solver tolerances and refining the grid changes C₂H₂ by 1.10×10⁻¹⁰ pp, net C₂H₄ by 1.52×10⁻¹² pp, and outlet temperature by 0 K at reported precision.
- The Arrhenius check verifies `A_kA = 10^31.1`, the 4184 J/kcal conversion, and increasing `k_A` with temperature under the positive-energy interpretation.
- A separate two-extent implementation, with symbolic `E·N = 0`, was run through Radau, BDF, LSODA, and DOP853. Maximum inter-solver spread was 1.013×10⁻⁷ pp, and the largest difference from the six-flow result JSON was 4.934×10⁻⁶ pp, within the script's limits of 1×10⁻⁶ pp and 1×10⁻⁴ pp, respectively. The run reproduced all six cases; it verifies numerical/state-space consistency, not experimental agreement.

**Execution receipt:** OS Linux x86_64 (kernel 6.18.55); Python executable `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python`; Python 3.12.14; NumPy 2.3.5, SciPy 1.17.0, pandas 2.2.3, Matplotlib 3.10.8, ipykernel 7.4.0, nbclient 0.11.0, nbformat 5.11.1. Conda is absent, but the active compatible Python and required packages were verified and used. No packages were installed and no dependency files changed. Kernel `python3` resolves to the active interpreter printed above.

The final top-to-bottom notebook execution completed in 13.27 seconds (wall clock); the run receipt records the measured duration.

The repository-local extent cross-check ran from the repository root as `python notebooks/benchmarks/schbib_1996_extent_crosscheck.py` in 1.27 seconds. It used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and SymPy 1.14.0; no packages were installed. Script SHA256: `4fbc273e706d7e42583d15751b31c1ed31071df8bfbbc8b9a9d1ef1d0dbc03d0`. Its JSON comparisons cover C₂H₂ conversion, net C₂H₄ conversion, and reaction-2 extent for both parameter sets and all three CO cases.

### Fixed-temperature reference status

The visually checked printed Table 8 full rate law and its reduced Eqs. 24–25 remain usable as an explicit **fixed-temperature Pd/α-Al₂O₃ reference calculation**, provided the inferred base-10 `log A` convention is stated and the printed gcat rate units are converted consistently when integrating over catalyst mass in kg. The two-extent check supports the implementation's stoichiometry and numerical integration against the six-flow code. It does not make the printed parameters experimentally validated: their Table 6 acetylene predictions fail by up to 98.980 pp and ethylene by up to 10.459 pp under the two definitions tested.

The author-shared text set can be retained as a separate fixed-temperature scenario, but its correction table is not image-authenticated and its unchanged `k_A`/`k_E` log values are paired with kgcat labels instead of the printed gcat labels. The intended physical mass basis, the formal correction status, and whether Table 6 ethylene means net disappearance or reaction-2 extent remain unestablished. This follow-up did not validate Model III thermal/transport behavior or transfer the constants to PdAg.

Run from the repository root:

```bash
cd notebooks/benchmarks
jupyter execute --inplace schbib_1996_steady_state.ipynb
```

Execution was performed from code based on branch commit `155a1e6ed00e92ed6f18535ae90708bf22c98584`; the notebook code-cell SHA256 recorded in `research/evidence/derived/schbib_1996_audit_results.json` is `ec7bb2f04a1346059ab3a1114f2d1a2df05b52574296c38f46636fffff63daf3`. The final commit SHA is reported in the task completion receipt.

The output record is [`schbib_1996_audit_results.json`](../evidence/derived/schbib_1996_audit_results.json). The notebook has 22 cells and executes top-to-bottom. Its four new diagnostic plots were opened and visually inspected; the four historical PNGs were also inspected and not modified.

## Uncertainty register and future Agent 5 handoff

### Open uncertainties

1. The correction is credibly attributed to the first author on ResearchGate, but its document integrity, visual values/units, and publisher status remain unverified. Do not call it a formal erratum.
2. The paper does not specify the base of Table 8 `log A`, and Eq. 22 is a relative surface/bulk relation rather than an explicit absolute `A_i` definition.
3. Printed Table 8 labels `k_A`/`k_E` per gcat while the extracted correction table labels them per kgcat, with unchanged numeric log pre-exponentials; the physical intended mass basis remains unresolved.
4. The Table 6 ethylene conversion remains unreproduced under both net disappearance and reaction-2 extent definitions; reported uncertainty is absent.
5. Table 7's `r_{2,35}` rejection marker conflicts with the p.1501 text naming that model as best fit.
6. STP reference conditions are not specified beyond the label `STP`; this audit uses 273.15 K and 1 atm. The rounded Table 3 feed was normalized to include the separate CO fraction.
7. Table 6 temperature spatial meaning, Figure 2 space velocity, Figures 3–4 catalyst mass/space velocity, and packed-bed void/length are incompletely reported for exact reproduction.
8. The full laboratory model III cannot be reproduced without justified transfer and wall-boundary inputs. Existing heat/Cp assumptions are not Schbib source data.
9. No fit or parameter transfer to PdAg has been performed.

### Agent 5 handoff

- **Reusable as a Pd/α-Al₂O₃ source reference:** the atom-balanced reaction bookkeeping `C₂H₂ + H₂ → C₂H₄` and `C₂H₄ + H₂ → C₂H₆`; ideal-gas concentration calculation; shared denominator and its local ratio cancellation; original printed Table 8 values and full/reduced equations with their explicitly noted unit conventions.
- **KCO interpretation:** treat printed `log A(K_CO) = 13.6` and author-shared `log A(K_CO) = 10.16` as separate alternatives. The author-shared value has a substantial effect on the Pd benchmark, but is not visually verified or formally confirmed as an erratum. Do not silently select or refit it for another catalyst.
- **Specific to the source catalyst/experiment:** rate constants, adsorption parameters, Pd/α-Al₂O₃ site interpretation, commercial ICI 38-1 support/dispersion, CO response, and laboratory operating envelope.
- **Uncertain for PdAg transfer:** adsorption/site competition and rate ratios may change with alloy composition and surface structure. No evidence in this audit validates the Schbib constants or common-denominator mechanism for PdAg. Agent 5 may use the source formulation as a provenance-labeled baseline after owner review, not as a validated PdAg law.
- **Readiness:** source-faithful original formulation is demonstrable (**PASS**); corrected parameter provenance and all-species experimental reproduction remain **BLOCKED**. Agent 5's combined PdAg–CO work remains gated on owner review of this report and Agent 4's separate audit, per GOAL.

## What is not claimed

This audit does not claim the author-shared note is an ACS erratum; that the Table 6 ethylene data are wrong; that any one parameter/unit correction alone explains the full discrepancy; that Figures 1–4 have been quantitatively digitized or fully reproduced; that the historical adiabatic energy model represents the glycol-bath experiment; or that Schbib parameters transfer to PdAg.
