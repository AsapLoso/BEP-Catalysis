# Larsen 2024 — preliminary independent source inspection (2026-10-25)

**Nature of this record:** AI source-audit observations, **not** an owner-approved interpretation, independent full-model reproduction, or complete image-page transcription. It is an earlier working note; see the [consolidated audit report](../../reports/larsen_2024_equation_and_baseline_audit.md) for current status and remaining requests.

## 1. Original document and searchable representation

- The owner uploaded a 97-page PDF named `Larsen - 2024 - Semihydrogenation of acetylene to ethylene with a PdAg catalyst.pdf`. The binary remains on the [pinned Larsen source branch](https://github.com/AsapLoso/BEP-Catalysis/blob/adf33269fadc2a70891a144ed6dd86f25c58db25/research/evidence/original/Larsen%20-%202024%20-%20Semihydrogenation%20of%20acetylene%20to%20ethylene%20with%20a%20PdAg%20catalyst.pdf); SHA-256 b5aaa2300ff9b64aca70e58cc5e4d8be30b3c12ee264e69af89e01c86f5120c9 matches the uploaded copy, not an authenticated official deposit. This establishes **exact equivalence to the uploaded copy**, not equivalence to an official 2024 deposit.
- The PDF metadata states `creationDate: D:20260626112625Z` and `producer: xdvipdfmx (20250410)`. A 2026 regeneration is plausible and does not establish a change in scientific content. Official repository/publisher authentication remains open.
- The long [native-text extraction](../transcriptions/larsen_2024_complete_native_text_unverified.txt) is searchable; it marks parsed PDF page boundaries. **Appendix E/F scans do not yield complete text from the native PDF text layer**. The existing 18 render PNGs and [page-transcription scaffold](../transcriptions/larsen_2024_appendix_E_F.md) remain necessary.
- The source inventory formerly misclassified a separate Gobbo paper as an active primary benchmark; it is historical only, outside A4's source reproduction.

## 2. Model-equation checks made directly against uploaded PDF

**PDF page 43 / printed page 37, Section 6.2.3:**

- Eq. **6.9** prints `r1_raw` proportional to `k1 * K_C2H2 * p_C2H2 * K_H2 * p_H2` divided by a **squared** sum of acetylene, ethylene and hydrogen adsorption terms: `(1 + K_C2H2 p_C2H2 + K_C2H4 p_C2H4 + K_H2 p_H2)^2`.
- Eq. **6.10** caps it as `r1 = r1_raw / (1 + r1_raw/r1_max)`.
- Eq. **6.11** prints `r2` proportional to `k2 * K_C2H4 * p_C2H4 * K_H2 * p_H2` divided by `(1 + K_C2H2 p_C2H2 + K_C2H4 p_C2H4) * (1 + K_inh p_C2H2)^n_inh`. **The first adsorption factor has NO square in Eq. 6.11**.
- The old `notebooks/benchmarks/larsen_2024_benchmark.ipynb` implements the first adsorption factor of `r2` **squared**. This is a verified disagreement between code and the printed thesis Eq. 6.11, not yet proof that the printed equation is the exact formula used during optimization. Distinguish the thesis main-body formula, prior notebook, source Appendix F *standard-model code* and any source author's actual final-fit implementation. **Do not silently repair by refitting; test both alternatives with unchanged parameters**.

## 3. Independent discrepancies warranting source audit

- **Temperature discrepancy:** The thesis's abstract (PDF p. 7 / printed p. 1) says catalysts tested at **100 °C and 1000 mbar**. The methods narrative in Section 4.2 (PDF p. 21 / printed p. 15) describes a reduction/pretreatment, then says that once an experiment starts the reactor is held at **80 °C**. Determine whether these describe different procedures, a textual inconsistency or a change between experiments; do not simply assume all measurements and fit parameters are at either T. Cross-check experimental tables and specific figure captions.
- **Model selection/row counts:** The abstract and source section 6.2.3 report overall RMSE near 5.10/5.43/7.14 percentage points for Pd0Ag/Pd2Ag/Pd3Ag respectively. Appendix F PDF p. 83 (printed p. 77) displays a cropped Jupyter output captioned **"160 rows × 4 columns"** spanning catalysts. Another cropped optimization table on PDF p. 85 (printed p. 79) states **"41 rows × 26 columns"** for selected Pd0Ag records. Neither caption alone proves how many unique Pd2Ag or Pd3Ag observations fed the *final extended* model. Map every experimental ID, catalyst, exclusion/filter, output table and figure sample count; do not infer that all 160 records were in the final fit. Examine Appendix F pages 83–88 directly.
- **Measurement definitions:** Section 4.2 (PDF p. 22 / printed p. 16), Eqs. 4.4–4.5, defines experimental conversion and selectivity from GC concentrations, acetylene consumed and byproducts including ethane and C4+; do not silently conflate with notebook's flow-based selectivity without proving equivalence under the actual data/assumptions.
- **RMSE definition:** Section 4.3 (PDF p. 23 / printed p. 17), Eqs. 4.14–4.15, defines a root-mean-square over the *pair* of conversion/selectivity errors for each experiment followed by an **arithmetic mean across experiments**. This is not generally identical to a root mean square across all errors. Reproduce precisely the source definition for any independently compared subset.
- **Missing fitted units:** The existing parameter CSV already labels pressure and rate units as **inferred**. Verify source explicitly, then derive dimensions from the chosen equation and reactor balance. Do not silently present inferred units as original units.

## 4. What has NOT been done here

This note does **not** certify all Figure 6.6 fitted vector entries from the plotted images, independently rerun simulations, verify the complete 18-page Appendix E/F table/code image transcription, resolve the Pd2Ag/Pd3Ag row counts, authenticate an official 2024 PDF, or justify transferring any CO mechanism. Agent 4's research report and audited notebook remain distinct future deliverables after owner plan approval.

**Owner scope:** These are AI reference notes. No personal science-map or owner-written notebook edits are authorized.
