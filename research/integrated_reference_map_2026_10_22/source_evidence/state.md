# Citation provenance mission state

## Current checkpoint

- Active continuation branch: `work/bep-citation-provenance-audit-v2-20261023`, created from latest head `21043c63cefcd64cb80280176927c49769ead459` of the exact requested base/PR target `work/bep-integrated-reference-map-v1-20261022`. No Git objects were fetched or downloaded; GitHub API file and metadata access is used.
- Current data after B18 first pass: 143 nodes; 66 source records; 349 current claim/source links; 96 historical overlay citation attachments; 167 passage records; 118 short quotation records; 18 sources reopened; 48 source records unopened; 148 links AI-rechecked with receipts; 16 separate post-commit second-pass entries cover 154 passage outcomes; 0 human-verified links. B18 adds ten full-PDF passages and six short quotations, and its three source-linked claims are partially supported at the stated source scope. The separate B18 second pass is pending. B17 data-quality work corrected the stale source-review count and restored six claim receipt links plus six first-pass checkpoint references; 42 correction records are addressable and all 24 prior unique receipt IDs resolve.
- Prior batches B0–B10 remain preserved in the parent history and detailed sections below. B11 reopened the official Urmès et al. (2022) publisher page: four abstract excerpts now ground 14 claim-source links; two theme attachments are unsupported by the abstract and corrected as such. The full-text link redirected to the abstract and SI access returned HTTP 403. The B11 first-pass snapshot had 115 passage records and 77 short quotes. Its separate post-commit re-audit is recorded after commit cc08dee26004ecd50d3bc141422e39cf6fd48859: four passages and 16 claim links rechecked, with zero additional corrections. Current cumulative counts are listed in validation_results.json; AI-only assessments remain provisional and human verification remains not_verified. All human review remains `not_verified`.

## B16 Rosa et al. (2025) checkpoint

The primary article XML for PMCID PMC12442368 was retrieved twice from Europe PMC after the first-pass commit; both 137258-byte captures have SHA-256 `b953c19f28a2b1459471c601b3b10b61cf4d6efaeff2e59b94930706d1c933d4`. Eight claim-grounded passages were added across §§1, 2.1.3, 2.1.6, 2.2, 3.2–3.3 and §4; seven exact brief quotations total 20 words. Nine current claims and their reciprocal passage links were confirmed on the second pass with zero corrections. Findings include a conditional single-site Pd/α-Al2O3 closure (1–2 bar, no CO), reversible ethylene adsorption in a steady model, source-specific transport screening and a steady PFR workflow. The cited SI (including Tables S3–S4 and Eqs. S13–S14) was not retrieved. This evidence does not establish PdAg transfer or periodic benefit over an optimized feasible steady benchmark. All records remain AI-authored and not human-verified. Full graph validator and full-file YAML validation remain pending.

## Resume procedure

1. Read `coverage_ledger.yaml`, `source_review_ledger.yaml`, `research_batches.yaml`, then open the listed original source at the exact locator.
2. Recheck the source passage and the linked AI interpretation; do not treat earlier map summaries or this state file as source evidence.
3. Add brief verbatim quotes, precise source locators and scoped interpretations to `passage_records.yaml`; record source hashes when source bytes are captured, and update exact claim IDs in `claim_passage_register.yaml`.
4. Record corrections and competing interpretations without deleting historical wording; never change any `human_verification_status` from `not_verified`.
5. Run both graph and evidence validators where the source/file environment allows, inspect the focused diff, and commit the batch.
6. Select the next source from the unreviewed claim/attachment queue and continue with already-local files. Do not fetch, pull, clone, or otherwise download Git objects. The current user instruction allows a Git push if the task requires it; use GitHub API checks for remote refs/PR metadata and do not access the moved OneDrive checkout.

## Current batch and next action

B1–B17 first passes and separate post-commit AI second passes are complete; B18 Waldron et al. (2020) has a first-pass source and claim audit, with its separate post-commit second pass pending. Eleven passages and six quotations (23 words) ground three existing links. The full published-version PDF was reopened via UCL Discovery and bibliographic metadata cross-checked at RSC; no local source hash or ESI review is claimed. The source supports local information-design and source-specific esterification parameter-precision results, not reactor-performance gain or BEP transfer. No Git objects were fetched or downloaded. PR #198 remains open and targets `work/bep-integrated-reference-map-v1-20261022`. Next, commit the first-pass dataset and separately reopen the full article for B18's post-commit audit.

## B1 source findings

Dehghani et al. (2019) was reopened as a full local PDF and visually checked at printed/PDF pp. 3–8, 11, 17–21. The S1 workbook archive already present in the workspace was hash-checked and all three sheets were reread. See `passage_records.yaml`, `dehghani_supplement_summary.yaml`, `correction_ledger.yaml`, and `research_batches.yaml`. The B1 claims received a separate post-commit AI second pass; no human source verification is claimed. That pass corrected the literal Table 5 row-2 numerator (`p_C2H2^1.4`) and preserved its conflict with the ethylene-hydrogenation row label as unresolved.

## B2 Urmès et al. (2019) first-pass findings

The local source PDF was reopened and hashed. Thirteen passage/equation records cover 15 substantive current claim links; 18 generic or historical link records remain queued. The audit distinguishes the source's six-term and reduced four-term site balances, its algebraic quasi-equilibrium rate closure, coverage estimates derived from reaction orders versus the fitted model, and its laboratory PFR transfer checks. It records two unresolved source inconsistencies: K1=611 Pa^-1 in printed p. 5 versus 13 Pa^-1 in Table 5, and the intermediate r7 expression's acetylene pressure versus the final ethane rate's ethylene pressure. It separately reconciles K5=7.4 Pa with an ethylene adsorption strength of 0.14 Pa^-1 as reciprocal-consistent to rounding. A separate post-commit second pass confirmed all 13 records, eight quotations and 15 claim links, and found no additional transcription correction. No human verification is claimed.

## B3 Borodziński sources, first and second passes

The local 2000 primary article and 2006 review were hash-checked and selectively inspected. The first pass added 15 records across all 14 current links; the separate post-commit second pass re-read all 15 records, all 11 quotes and all 14 links from fresh extraction and page renders. It corrected the first-pass Table 1 equation attribution and added a separate record for Appendix A Eq. (A.45): Table 1 model 5 prints denominator power 2, while Eq. (A.45) prints power 3 for the k2-prime ethylene term. Independently, dimensional analysis and Table 3 require k2-prime in kPa^-2 under the printed basis while the Table 1 footnote says kPa^-3. Both source conflicts remain open. The total is now 16 B3 passage records; across B1–B3, evidence validation reports 46 records, 28/28 verified quotations, 34 current links with passages and 306 without. Both validators pass with 143 nodes, 65 sources, 340 claim links, 96 historical attachments and 24 uncertainties. The 2006 review remains secondary synthesis; its cited primary studies have not yet been reopened. No human verification is claimed.

## B10 Wang et al. (2023) PdAg descriptor and microkinetic audit, first pass

The local ACS Catalysis primary article was hash-identified at `Articles/acquired_pdfs/ref_17.pdf`; the identical Zotero-backup file has the same SHA-256. Fresh extraction and visual review cover printed pp. 434–441. Twelve passage records recheck all three current claim/source links, with nine brief exact quotations; no local Supporting Information file matching the article was found.

The main text states the DFT slab setup, L–H unit site balance, equilibrated C2H2/H2 adsorption, and `dtheta/dt=0` coverage closure. This is a steady PSSA model and gives no surface relaxation time. The pathway includes competing ethylene and over-hydrogenation branches; first C2H2 addition is a modeled rate-determining step for most sampled surfaces. The source also reports that C2H2 precoverage changes calculated absolute rates by orders of magnitude even where relative rank changes little in the tested subset.

The source-supported catalyst tests used 1 wt% Pd/Al2O3 with XPS surface Pd:Ag 1:1, 1:3 and 1:5 compositions at a reported 0.2 MPa total pressure; its measured highest plotted yield is the 1:3 composition in the tested series. The paper defines yield from acetylene consumption and outlet ethane, but the metric alone does not establish a full carbon balance. Descriptor/energy calculations list 0.2/4/9 atm partial pressures at 333 K, a different pressure scale from the bed test. Descriptor fit tables and exact microkinetic rates are in absent SI; phi_CH3 also divides by an empirical radius whose unit convention is unstated in the main article. This is qualitative within-set steady evidence, not matched-condition rate validation, target-specific kinetics, periodic operation, or a best-steady comparison.

The B10 separate post-commit review is complete. It did not recover the local Supporting Information, exact rate tables, numerical descriptor-radius convention, matched-condition rate validation or target catalyst identity. All new AI source evidence remains `not_verified` by a human.


## B11 Urmès et al. (2022) publisher-abstract first pass

The official Wiley page identifies the article and exposes abstract lines 158–161. Reopening the full-text link redirected to the same abstract page, and the listed SI download returned HTTP 403. Passage records URM22-B11-P01 through P04 capture the dynamic-identification context, single-site parameter-estimation statement, outlet transient-model reproduction, and model-interpreted conversion-controlling steps. The paper-specific result is a kinetic-identification/model-reproduction precedent on Pd/α-Al2O3; it is not evidence of a periodic performance gain, target PdAg transfer, stable periodic closure, or optimized-steady superiority.

Fourteen claim links receive scoped partial support. Two links, on cycle-metric/steady-benchmark and hardware-feasibility themes, are unsupported by the accessible abstract; this does not establish that the inaccessible paper body contains no relevant material. First-pass quote matching and ID/reciprocity checks were executed in-memory through the GitHub API; full validator and separate second pass remain open.


## B11 Urmès et al. (2022) post-commit second pass

After the first-pass evidence and formatting repair commits, the official publisher abstract was reopened and all four excerpts, locators, and claim interpretations were checked again. The abstract text remained stable. A repeat full-text click timed out; the listed SI again returned HTTP 403. The two unsupported theme links remain scoped to the abstract and do not imply the inaccessible article body lacks relevant material. All 16 claim links and four passage records have a separate same-agent AI audit receipt. Human review remains not_verified.

Focused validation parsed the changed B11 record subset and checked passage/claim reciprocity, unique IDs, quote-to-capture matching, unchanged 340-edge inventory and human-status separation. The complete `validate_source_evidence.py` was not run because this continuation used GitHub API files and had no local repository/source PDF tree; the old full validation result on parent commit `21043c63cefcd64cb80280176927c49769ead459` predates B11 and is retained as historical evidence only.


## B12 BEP proposal selected-line first pass

The project proposal was reopened through its repository source file at GitHub blob `759c86c068ec4dadaaa65f5a4f48878d4a11d54a`, selecting lines 95–310. Ten passage records cover the research question, steady-state yield rationale, gas and coverage equations, proposed forcing window, isothermal assumption, B-spline choice, optimization baseline, validation plan and hidden-state/observer boundary. Thirty of 78 proposal-linked claims now have passage-level provenance. Each assessment is limited to what the proposal states; none establishes scientific validity, implementation, experimental completion or performance gain.

Three corrections preserve the distinctions that matter: steady operation is not automatically thermodynamic equilibrium, the desorption/pulse/residence inequality is an unverified heuristic, and the theoretical steady baseline is not yet a best-feasible matched steady policy. The proposal's novelty and categorical measurement-impossibility statements remain unverified. The separate B12 second pass is recorded in SP-B12-20261023-PROPOSAL; external-source checks continue in B13 and later batches.


## B13 Zhu et al. (2021) and proposal-citation audit

The TU/e author-institution record was freshly reopened for the article abstract and metadata; ScienceDirect full text returned HTTP 403. Five abstract passages support only a thermal-pulsing precedent for Pt/Al2O3 CO oxidation: microsecond heater response, increased reaction rate, lower power input and a simulation-attributed surface desorption/repopulation explanation. These results do not establish acetylene concentration forcing, PdAg transfer or ethylene yield/selectivity gain. The proposal's attribution of an “up to 40-fold” enhancement is directly documented as proposal wording, but that magnitude is absent from the accessible abstract and remains unresolved pending the article body or the cited underlying source. Four claim-source links and six total passages were rechecked in a separate post-commit pass (SP-B13-20261023-ZHU), with no new corrections.

## Post-PR claim-register repair and review status

After PR #198 was created, diff review found four duplicate `access_level_reopened_this_mission` entries in four claim records. Commit `0f3b7b9e049595b26086be1d9caf4532f60fb324` removes the superseded `not_reopened` entries. A fresh focused scan found 340 claim rows, 340 unique claim IDs, and exactly one access-status field in each row. This repairs a YAML duplicate-key defect; it does not replace full repository validation.

PR #198 remains open, unmerged, and based on `work/bep-integrated-reference-map-v1-20261022` at `21043c63cefcd64cb80280176927c49769ead459`. Current head at the repair checkpoint is `0f3b7b9e049595b26086be1d9caf4532f60fb324`. No auto-merge is configured.


## B14 Di Giuliano and Pellegrino (2019) selected-excerpt source audit

The primary PMC full-text index was reopened for selected original-article sections on variable superficial velocity, method-of-lines discretization, explicit-Euler stability and the CO2-capture model comparison. The indexed article metadata identifies Heliyon 5(9), e02040, DOI 10.1016/j.heliyon.2019.e02040. Direct PMC HTML opening returned a CAPTCHA, so this was not a sequential read of the full article and no PDF page render or source-file hash was available. Four brief passages now cover four existing claim-source links. Access and scope are recorded explicitly.

The article's general ADPFR equation keeps uC_i inside the conservative flux divergence; its constant-u form is conditional on negligible flow variation, such as strongly inert-diluted feed. Its own spatial scheme is method of lines with central finite differences and false-boundary ghost-point closure, not the separate finite-volume derivation in the map. In its own dimensionless carbonation case, Eq. (45) constrains explicit-Euler time integration; reported simulations use ode23tb, while a separate forward spatial difference calculates u(z,t). This separation is recorded as CORR-B14-DG19-001. The CO2-capture constant-u versus variable-u comparison remains simulated, material-specific evidence rather than experimental validation or a BEP prediction.

A conditional summation of the two BEP gas-reaction balances records DRV-B14-STOICHIOMETRIC-SUPERFICIAL-VELOCITY: at spatially uniform ideal-gas P,T, fixed gas holdup and consistent rate/concentration bases, each forward hydrogenation step reduces total gas moles by one, yielding ∂u/∂z = −(r1+r2)/C_T. This is a stoichiometric model derivation only. It does not quantify the actual BEP flow profile. Pressure/temperature gradients, voidage changes, side reactions and mismatched rate bases remain open conditions.

B14 adds four passage records, four short excerpts, four claim rechecks, one derivation and one interpretation correction. The B14 post-commit second pass is pending and will record its exact commit before the batch is treated as second-pass complete. All source and claim human-review fields remain not_verified.


## B14 separate post-commit source re-audit

After first-pass commit 9ea3568fc9ead5b67c5aeb8d8bd4aac98901ced2, the four passages and four linked claim interpretations were re-opened against fresh source-specific queries on the primary PMC full-text index. The selected quotes and equation/method transcriptions were confirmed; source indexing still did not provide a sequential article reading or PDF page render. The audit also rechecked the one conditional stoichiometric derivation and its assumptions. All remain AI-only, with human status not_verified.

The second pass found a wording compression in the B14 summary. The source reports that outlet CO2-profile differences and the constant-u inert-N2-flow artifact increase at higher inlet CO2 mole fraction (less dilution), while the constant-u cumulative CO2-balance deviation has the opposite trend and is greater at lower inlet CO2 mole fraction. This metric-specific correction is CORR-SP-B14-DG19-001; the source author's variable-u preference remains a model-based interpretation, not independent experimental validation. B14 now has four passage rechecks, three unchanged and one corrected, with one new correction record. The complete graph/PDF-page validator has not yet run.


## B14 focused validation record

A focused PyYAML 6.0.3 parse succeeded for the four B14 passage records, four updated claim records, stoichiometric derivation, two related corrections, B14 batch, SP-B14 audit, and updated source/coverage rows. In-memory full-register scans confirmed 340 unique claim IDs, one access-status field per claim, 135 unique passage IDs, B14 reciprocity, derivation association and not_verified status on all touched records. This is excerpt-level YAML parsing and targeted structural validation. The full repository graph validator and full-file YAML/PDF-page checks were not run.


## B15 — Pachulski et al. (2012) first-pass source audit

Reopened the publisher metadata and abstract for the direct Pd–Ag/Al₂O₃ kinetic/reactor precedent, plus selected publisher-indexed article text. Direct ScienceDirect page opening returned HTTP 403; the complete paper, supplementary information, and PDF pages were not reviewed sequentially. This access boundary is recorded in all affected provenance records.

Corrected the source metadata: the publisher author line gives Axel Pachulski, Rainer Schödel, and Peter Claus. The integrated ledger had listed Andreas Pachulski and Sven Schödel. Correction CORR-B15-PACHULSKI-METADATA-001 updates the source record, source review ledger, and all 13 linked claim identities; it changes no scientific interpretation.

Added six passages: the article's three overall reaction routes; the integral fixed-bed kinetic-measurement context; the selected two-site-type LH rate representation; source-specific candidate-model comparison and statistical/thermodynamic selection; Mears, Weisz–Prater and higher-order Damköhler transport checks; and an industrial bypass-reactor calculation. Reaudited all 13 linked claims as partially supported within their specific scopes. The two-site representation is not direct structural observation, the transport checks do not transfer automatically to the BEP, and the bypass calculation is not evidence of periodic benefit.

B15 first-pass counts: 141 passage records, 98 brief quotation records, 130 current links with passage evidence, 9 links with derivations, 219 links without passage or derivation, 132 AI-rechecked links, 125 partially supported links, 4 unsupported/disputed links, 15 sources reopened, 20 research batches, and 38 correction records. Human-verified claim links remain 0. The post-commit source re-audit is pending.

Open source questions: the publisher full text/PDF and SI; the exact catalyst loading and characterization; full candidate equations and fitting criteria; parameter uncertainty and identifiability; passage-level details of the transport criteria; and validation residuals for the bypass calculation. These must not be inferred from the abstract. The source supplies no evidence about periodic operation or a matched optimized steady-state benchmark.


### B15 post-commit source re-audit

After first-pass commit 03b75c6293eac6f197922c27ba2af62d962b2ebc, fresh source-specific publisher searches reopened the author line, article abstract, and selected indexed text for the same paper. The publisher again identifies Axel Pachulski, Rainer Schödel, and Peter Claus; the five short quotations match the abstract, and the selected reaction-network excerpt remains within its indexed-text boundary. Rechecked all six passage records, 13 claim-source links, and the metadata correction. No second-pass correction was required. The publisher's direct full-text route still returned HTTP 403, so the complete article, SI, and PDF pages remain unreviewed. AI-only status; human verification remains not_verified.


## B17 Urmès et al. (2020) first-pass checkpoint

The publisher-indexed ScienceDirect result was freshly reopened for the abstract, highlights, and selected Introduction, numerical-tools, and Experimental results excerpts. Direct opens of the article page and abstract route returned HTTP 403; no complete paper, PDF pages, SI, or local byte-hash capture is available. Seven short excerpts (25 source words) now support four current claim/source links. The passage set distinguishes the identification motivation, modeled gain/phase and mass-transfer analysis, small-amplitude linearization assumption, acquisition rate versus analyzer bandwidth, equilibrium-adsorption parameter estimate, and bypass-based inlet reference. The experiment is molecular ethylene adsorption over Ni/Al2O3. It does not establish Pd/PdAg acetylene kinetics, target identifiability, periodic gain, or superiority to an optimized feasible steady operation. The count correction records 219, 210, and 206 links with neither passage nor derivation at B15, B16, and B17 respectively; all nine derivation-bearing rows also have passages. A separate post-commit AI second pass, SP-B17-20261023-URMES2020, followed first-pass commit e713656953a8bfa20d7e9b0498fbdcc5cf777d15 and confirmed all seven passage records, quotes, and four claim interpretations without scientific correction. Direct publisher-page access still returned HTTP 403; human verification remains not_verified.
