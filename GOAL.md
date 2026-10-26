# Isothermal CO kinetics — source selection (independent research track)

**Assigned branch:** `feat/isothermal-co-kinetics-source-selection`  
**Tracking issue:** [#12 — Source selection](https://github.com/AsapLoso/BEP-Catalysis/issues/12)  
**Parent snapshot:** `feat/schbib-co-benchmark` at `e27cb766d644de685d02f2fc8f11d2300aff909c`. Its research report/notebook remain historical and must not be silently recast as validated.  
**Status (2026-10-26): PREPARED, PLAN FIRST.** No replacement source has been chosen or validated.

## Decision to resolve

Find the strongest available **isothermal, experimentally supported kinetic source** for acetylene semihydrogenation with **CO dependence** and relevant ethylene hydrogenation/selectivity. The owner does **not** want to reconstruct gas/particle/wall temperature gradients or Schbib's full thermal Model III. This source selection is about a **kinetic reference**, not the dynamic reactor implementation.

**Do not conclude Schbib publishes no parameters.** It publishes seven pairs of kinetic values in Table 8 and the full source laws. Yet its published constants were fitted using a more complex reactor; the executed isothermal audit matches author-shared acetylene conversion provisionally and fails Table 6 ethylene reproduction. See `research/reports/schbib_parameter_and_benchmark_audit.md` and the independent extent check `research/evidence/analysis/schbib_reaction_extent_state_space_crosscheck_2026_10_26.md`.

## Starting lead — Bos et al. (1993), **not yet selected**

A. N. R. Bos et al., *A kinetic study of the hydrogenation of ethyne and ethene on a commercial Pd/Al₂O₃ catalyst*, *Chemical Engineering and Processing* **32** (1993) 53–63, DOI [10.1016/0255-2701(93)87006-G](https://doi.org/10.1016/0255-2701(93)87006-G); [institution-hosted full PDF](https://ris.utwente.nl/ws/portalfiles/portal/6717590/Bos93kinetic.pdf).

Its **printed Table 3 (p. 60)** includes Model 8 fitted parameter values, and **p. 62** recommends and rewrites Model 8 as explicit CO-containing acetylene and ethylene/ethane rate laws. It uses an approximately isothermal Berty reactor, **Pd/Al₂O₃ rather than PdAg**, in tail-end feeds and a limited experimental envelope (**0–60 ppm CO, 299–330 K, 0.3–2.1 MPa**). The authors report that ethane formation is harder to fit and caution against extrapolation. Independently inspect the equation images and numerical units; don't inherit a transcription uncritically.

## Acceptance criteria and strict scope

1. **Plan, then work:** read [#12](https://github.com/AsapLoso/BEP-Catalysis/issues/12), `AGENTS.md`, `TODO.md`, original Schbib and new literature primary sources. Provide a short independently reasoned Plan Mode proposal before editing kinetic code/data. Once approved, execute autonomously on this branch.
2. **Compare evidence-backed alternatives:** select a shortlist, not only Bos. Each source must have primary access, catalyst and conditions, full rate law(s), actual numerical fitted values and units, CO range, reproducible experimental points, stated uncertainty/data limitations and explicit domain of applicability. Find PdAg + CO evidence if possible, but never invent parameter validation.
3. **Fixed-temperature kinetics only:** a source can use (k(T)), (K(T)) at specified uniform (T), but do **not** implement energy balances, particle/wall heat transfer, thermal model III, or transient CO dynamics. If source's parameter extraction or prediction demands thermal reconstruction, explain the **NO** without forcing it.
4. **Check independent quantitative predictions:** don't equate equation/source transcription, internal solver agreement, selected figures or PDF fit scores with reproduction of measured experimental results. A limited unit-consistent independent reproduction may support a **provisional YES** with stated restrictions.
5. **Decision matrix + recommendation:** rank eligible papers by scientific defensibility, practical reproduction, relevance to CO, and honest transfer limits to Larsen's **CO-free PdAg** source. One line per source: **YES** (supports a defensible isothermal reference for its stated domain) or **NO — improvement/missing evidence**. Neither verdict alone proves PdAg-CO improvement.
6. **Deliver:** `research/reports/isothermal_co_kinetics_source_selection.md`, page/equation/parameter/data provenance, small reproducible test only if justified, and an Agent 5 handoff listing source limits and possible future validation. Preserve all original source/parameter versions and notebook snapshots.
7. **Branch safety:** ordinary commits only to this branch, no PR, merge, force push, owner map edits, modifications of A1/A4/Agent5 branches or new integrated CO model. **Agent 5 remains PAUSED.**

## Disqualifying failures

Claims that Model III data are unnecessary without source support; using a non-CO fit as measured CO response; using Pd/Al₂O₃ parameters as PdAg measurements; inventing fit units or experimental points; retuning constants to make plots agree; silent temperature or reference-flow changes; treating a PDF stored result as a freshly independently executed benchmark.
