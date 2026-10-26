# Isothermal CO kinetics — source selection worklist

> **CURRENT OWNER REQUIREMENT (2026-10-26): PFR, NOT BERTY.** Plan already approved with this correction. Prefer **fixed-T CO-sensitive PFR/packed-bed kinetic experiments** with reproducible measured outlet conversions/selectivities and complete inputs. Bos Berty data can support a bounded rate-law discussion, not direct PFR validation; do not make Berty replication a mandatory preparatory step. Compare any PFR calculation against **actual PFR observations at matching conditions**; otherwise mark predicted PFR curves as unvalidated. No thermal model or refitting. If no suitable published benchmark, report **NO SOURCE READY**.


**Branch:** `feat/isothermal-co-kinetics-source-selection`  
**Issue:** [#12](https://github.com/AsapLoso/BEP-Catalysis/issues/12)  
**Status:** SOURCE SELECTION COMPLETE — **NO SOURCE READY**. See [`research/reports/isothermal_co_kinetics_source_selection.md`](research/reports/isothermal_co_kinetics_source_selection.md). No coupling, Agent 5 work, PR or merge.

## 00 — Plan and source audit
- [x] Present and receive approval for the source-first plan with the corrected PFR requirement; do not edit kinetics code/data.
- [x] Read Schbib's completed audit, original versus author-shared parameter distinction, C₂H₄ BLOCKED result and reaction-extent cross-check; retain audit history untouched.
- [x] Inspect Bos et al. 1993 original [PDF](https://ris.utwente.nl/ws/portalfiles/portal/6717590/Bos93kinetic.pdf), Model 8, Table 3 (p. 60), rate units/nomenclature (pp. 60, 62), domain and observed selectivity.
- [x] Search and source-check additional primary kinetic sources, including PdAg/CO and fixed-temperature bed data; document why each candidate does not meet the full PFR gate.

## 01 — Model suitability and data
- [x] Make the source-by-source matrix: catalyst, conditions, CO range, rate laws/parameters, transport closure, measured outputs and PFR fit.
- [x] Track measured C₂H₂ conversion, C₂H₄ conversion/net disappearance, C₂H₆/selectivity and confounded comparisons separately.
- [x] Check unit/reference-temperature conventions, CO dependence, fixed-temperature assumptions and reactor mismatch.
- [x] Review the executed isothermal Schbib PFR predictions from the completed parent-branch audit; do not run a Bos-to-PFR transfer without comparable PFR data.
- [x] Classify each screened source **YES/NO** for the target benchmark and record the concrete missing requirement.

## 02 — Handoff and governance
- [x] Write `research/reports/isothermal_co_kinetics_source_selection.md` with primary locators, parameter/data provenance, source matrix and **NO SOURCE READY** recommendation.
- [x] Record Schbib as bounded historical evidence and state why Pd/Al₂O₃ or CO-free PdAg parameters do not validate PdAg+CO PFR behavior.
- [x] Update GOAL/TODO with the disposition. Commit only this branch; no PR/merge, Agent 5 work, heat-transfer model or owner personal-map edit.
