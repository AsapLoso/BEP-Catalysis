# Isothermal CO kinetics — source selection worklist

**Branch:** `feat/isothermal-co-kinetics-source-selection`  
**Issue:** [#12](https://github.com/AsapLoso/BEP-Catalysis/issues/12)  
**Status:** SOURCE SELECTION PENDING — no primary replacement approved, no coupling/merge.

## 00 — Plan and source audit
- [ ] Present a concise source-first Plan Mode approach, for owner **YES** or **NO + improvement**; no code modifications before approval.
- [ ] Read Schbib's completed audit, original vs author-shared parameter distinction, C₂H₄ BLOCKED result and reaction-extent cross-check; retain audit history untouched.
- [ ] Visually audit Bos et al. 1993 original [PDF](https://ris.utwente.nl/ws/portalfiles/portal/6717590/Bos93kinetic.pdf), Model 8 equations, Table 3 (p. 60), rate-unit conventions (p. 62), experimental domain and measurable comparisons.
- [ ] Search and source-check additional credible primary kinetic sources, especially PdAg with CO and genuinely isothermal measured data. List candidate failures rather than defaulting to Bos.

## 01 — Model suitability and data
- [ ] Make source-by-source matrix: catalyst/metal/support; pressure and temperature; feed; CO ranges; reaction channels; kinetic expressions; parameter and unit completeness; transport closure; measured point access; direct reproducibility; suitability for possible PdAg extrapolation.
- [ ] Establish actual measurement observable(s): C₂H₂ disappearance, net C₂H₄ production/consumption, C₂H₆ generation and any additional pathways; avoid conflating selective and net conversion.
- [ ] Confirm unit/reference-temperature conventions, CO adsorption dependence, independent temperature applicability at fixed T and applicability to a PFR versus a well-mixed Berty reactor.
- [ ] Independently calculate source-native predicted rate(s)/conversion(s) at published measured conditions where complete; record actual residuals and solver receipts. Don't invent experiments or fit to observations.
- [ ] Classify **YES/NO + concrete limitation** per source, with bounded recommendation. Mark experimentally blocked sub-claims explicitly.

## 02 — Handoff and governance
- [ ] Write `research/reports/isothermal_co_kinetics_source_selection.md` with primary page/citation locators, numerical parameter inventory, comparison table, execution evidence and a concise recommended source or honest **NO SOURCE READY**.
- [ ] State how Schbib remains reusable as historical background and why the new source cannot automatically be used on Larsen's PdAg without CO observations.
- [ ] Update GOAL/TODO with verified receipts. Commit only this branch. No PR/merge, Agent 5 run, heat-transfer model or owner personal-map edit.
