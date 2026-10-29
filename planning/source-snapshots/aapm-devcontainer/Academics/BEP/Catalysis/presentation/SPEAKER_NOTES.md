# BEP presentation — concise speaker cues

**Can timing the feed favor ethylene?** · 14 October 2026 · approximately 9 min 30 s.

Use these as speaking prompts. The scientific elaboration and source links are in [the global bullet outline](GLOBAL_PRESENTATION_OUTLINE.md). The HTML deck contains these same cues behind **N**.

## 1. Can timing the feed favor ethylene? (40 s)

- Desired acetylene removal; avoid losing ethylene.
- Matched feed budget; timing is the variable.
- Hypothesis, with no demonstrated yield gain.
- **Transition:** Explain why the timing could matter before introducing a model.

## 2. Two reasons timing could matter (50 s)

- Nonlinear averaging can matter even under PSSA.
- Dynamic coverage adds its own timescale and history.
- Direction and size of any performance effect remain questions.
- **Transition:** Locate the internal inventories that could carry a transient response.

## 3. Describe where the history lives (60 s)

- State describes stored material, not just today's inlet.
- Retain fields only when justified for the question.
- Space is discretized; time still evolves.
- **Transition:** Show how those fields become the original numerical scaffold.

## 4. 11 fields become 1,480 coordinates (60 s)

- Four bulk + four pore + three coverage field types.
- 20 by 10 spatial representation; count is allocated.
- Architecture exists; zero default kinetics and audited defects remain.
- **Transition:** Separate the ability to write detailed dynamics from the kinetic information needed to calculate them.

## 5. Reacting gas, quasi-steady surface (60 s)

- 2019 chemistry is actually used; 240-entry uniform baseline.
- Gas evolves; coverage follows an algebraic closure.
- Periodic inlet exists; terminal snapshots do not establish a periodic benefit.
- **Transition:** Ask what can be inferred from effective fitted constants and what additional surface dynamics would require.

## 6. More states need more kinetic information (50 s)

- Effective constants compress mechanisms.
- Published fit: five quantities fitted, three fixed.
- Choose necessary fidelity against an observable and available evidence.
- **Transition:** Even a chosen, parameterized model must still be solved accurately and at a practical cost.

## 7. Compute the transient we mean (65 s)

- Upwind is spatial; BDF is temporal.
- Stiffness constrains stability; the relevant model must establish its scales.
- Local coupling motivates sparsity; no speedup claim.
- **Transition:** Make accuracy tangible by considering a pulse whose correct transport response is known.

## 8. The grid can change the pulse (65 s)

- Analytic, no-reaction transport example; exact time integration.
- 60 cells; T=residence time; 72.09% amplitude retained; lag 358.69° versus 360°.
- Phase error +1.31° at the same forcing frequency; exact time integration. Euler CFL=1 is a special exception.
- **Transition:** State what the existing evidence establishes and what checks remain before chemical inference.

## 9. Know what each result establishes (60 s)

- Preliminary outputs exist; no accepted reactor-performance number.
- Source checks and mathematical derivations establish their own bounded claims.
- Conservation, provenance and numerical accuracy precede physical inference.
- **Transition:** Return to the original question through the smallest defensible next comparisons.

## 10. Use the predictor to test and learn (60 s)

- Matched budgets; settled cycles; net ethylene. Distinguish same-mean from best admissible steady reference.
- Small optional hypothesis: noiseless distinguishability first.
- No periodic gain established; the next milestone is trustworthy dynamics.
- **Transition:** End on the research question and the concrete requirements for answering it.

## Optional questions / backup

- Legacy count: 1,480 allocated; 140 fixed/constrained/frozen shell entries. No claim of independent physical modes.
- New optional radial path: 2,400 entries; distinct boundary, conservation and Jacobian verification questions. Default uniform baseline has 240 gas entries.
- Source checks: 24/24 selected transcription checks; coverage-range receipt is 10/12, despite stale 11/12 prose in an older evidence README. Neither is experimental validation.
- G transport result: exact PDE delay versus exact-time semidiscrete upwind harmonic response; N=60, T=residence time, uniform positive flow, no reaction/dispersion. About 72.09% retained. Forward Euler at CFL=1 is a special pure-advection exception.
- K: saved synthetic reacting outputs and periodic inlet exist; terminal snapshots do not establish periodic convergence, harmonic gain/phase or cycle-averaged yield.
- E: source kinetic experiment and assumed composite reactor are different configurations; do not transfer source validation to the modeled bed or local catalyst.
- Urmès 2022: flow-oscillation identification precedent, abstract-level here. Full equations and SI remain unverified.
