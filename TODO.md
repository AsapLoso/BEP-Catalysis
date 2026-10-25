# Agent 5 — Evidence gates and conditional work checklist

**PAUSED (2026-10-25).** Agent 5 is not authorized to implement the PdAg–CO coupled model yet. The tasks below are an audit-controlled *future* research plan, **not evidence of completion** or permission to run the work. The owner's personal map and notebook are out of scope.

## 00 — Independent source audits (mandatory preconditions; other agents, separate branches)
- [ ] **Agent 1 Schbib audit:** [#10](https://github.com/AsapLoso/BEP-Catalysis/issues/10) produces verified source/parameter/units record, author-correction assessment, corrected or explicitly failed Table 6 notebook comparisons and exact execution receipts on `feat/schbib-co-benchmark`.
- [ ] **Agent 4 Larsen audit:** [#11](https://github.com/AsapLoso/BEP-Catalysis/issues/11) establishes primary Eq. 6.9–6.11, resolves/flags squared-versus-first-power `r₂` denominator, flow standard/reference conditions, fitted parameter units and source-faithful experimental comparisons on `feat/larsen-pdag-benchmark`.
- [ ] **Owner gate:** inspect BOTH audit results, limits and commits; obtain **explicit authorization** to resume Agent 5. A merged file-import PR alone is NOT authorization.
- [ ] **New source handoff:** if authorized, deliberately import/refer to approved corrected source snapshots without deleting or disguising original Agent 1/4 historical evidence.

## 01 — Source audit and parameter crosswalk (AFTER gate)
- [ ] Write `research/reports/pdag_co_synthesis_deep_research.md` comparing actual Schbib and Larsen catalyst domains, experiments, rate expressions, parameters, units and benchmark performance with page/equation/table provenance.
- [ ] Distinguish **published measured, fitted, direct transcription, digitized, calculated/inferred, assumed and unknown** per quantity. Report Larsen full-thesis access and unresolved fitted-unit conventions.
- [ ] Record original and any verified corrected Schbib `log10 A` adsorption pre-exponentials. **Do not use 13.6 directly as `K_{0,CO}`**; verify any claimed 10.16/10.2 correction, energy and units against primary material.
- [ ] Derive concentration to partial pressure conversion for a source-consistent CO term, e.g. `C_CO = p_CO/(R T)`; check dimensional consistency with the published adsorption coefficient.
- [ ] Derive common-denominator rate-ratio cancellation and discuss original Larsen `r₁` cap, rate-law differences, catalyst transfer and mechanistic identifiability.

## 02 — Exploratory steady-state model (AFTER source and unit checks)
- [ ] Implement **source-faithful no-CO Larsen baseline** first, including verified Eq. 6.11 and the `r₁` cap. Compare against independently measured/digitized experiment(s), not just imported code.
- [ ] Build `notebooks/benchmarks/pdag_co_synthesis.ipynb` with standalone inspectable calculations and **at least two distinct explicit CO hypotheses** plus no-CO control. Do not assume preferential inhibition or improvement.
- [ ] Run conditional comparisons at 373.15 K and 1 bar for all three PdAg catalyst cases over 0–1500 ppm CO, with He displacement maintaining feed total; use 60,000 `cm³(ref) h⁻¹ gcat⁻¹` mass-normalized flow only after reference-volume conditions are resolved. Include 40k, 80k, 120k flow and 0.01×–100× adsorption-strength sensitivities if practical.
- [ ] Verify stoichiometry, unit conversion, denominator positivity, `CO=0` identity with verified baseline, representative BDF/Radau and tolerance sensitivity, runtime, actual notebook outputs and all uncertainties.

## 03 — Transient dynamics (blocked unless separately justified and approved)
- [ ] **BLOCKED by missing validated dynamics data:** establish measured/source-backed gas-holdup/transport or finite-rate surface coverages before proposing a runnable transient CO model. If absent, explain the blocked gate in the report; do not improvise an adsorption memory constant.
- [ ] **CONDITIONAL ONLY:** a steady-state versus periodic dynamic Pareto comparison may be proposed only after both independent physical/model justification and new owner scope approval. No mandatory positive enhancement result.

## 04 — Final handoff (once work is authorized)
- [ ] Record independently rerun vs historically stored notebook outputs, limitations, dependency versions, tests, runtime and exact commit SHA.
- [ ] Provide concise supported / speculative / unknown / next-study summary and separate AI-reference report; no automatic promotions in the personal map.
- [ ] Commit/push only `feat/pdag-co-synthesis` after source gates; no force, PR or merge without further instruction.
