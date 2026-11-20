# BEP model verification milestones

**Scope:** Reference-model and thesis-evidence checkpoints. This is a progress checklist, not a new project or ticket system. Status reflects evidence located on 16 October 2026; completion of one stage does not imply completion of the next.

## 1. Numerical verification — PARTIAL

- [x] Source transcription receipt checks 24 Urmès-2019 items against the paper text.
- [x] The PR #3 prototype has five isolated algebra checks, including carbon/hydrogen inventory identities, using explicitly illustrative parameters.
- [ ] Verify the coupled reactor implementation: solver behavior, positivity/site balance, conservation across the full state, mesh/tolerance convergence, and the affected 2019 implementation gates.
- **What this establishes:** component-level consistency checks exist.
- **What remains open:** neither receipt nor the five toy-fixture tests verify numerical accuracy of a complete reactor prediction. The implementation receipt reports its published-coverage gate as failed (3/4 gates pass); the legacy scaffold still lists six code defects.

## 2. Reproduction of published model results — OPEN

- [ ] Reproduce a clearly identified published model result using the paper's equations, parameters, initial/boundary conditions and output definition.
- **Evidence:** the 24-item source receipt is transcription evidence, not an output reproduction. The PBR implementation receipt does not pass its coverage-reproduction gate and records a different reactive-pressure path for an argon-bearing feed.
- **Completion means:** a numerical model output is matched to a reported model result under the same defined assumptions, with discrepancies explained. This is a milestone, not by itself experimental validation.

## 3. Agreement with experimental data under matched conditions — OPEN

- [ ] Compare predicted and measured reactor outputs at matched catalyst/support, feed, pressure, temperature, bed and pellet geometry, and measurement definition.
- **Evidence:** the repository records no validated matched-condition reactor result; the current presentation status treats saved simulator outputs as diagnostic rather than validated physical findings.
- **Completion means:** discrepancies and uncertainty are reported against an identified experimental dataset. A paper's fitted data do not automatically validate a separate code implementation.

## 4. Independent validation or prediction — OPEN

- [ ] Validate against an independent dataset or make a prediction for a condition not used to set or tune the model, then compare with the held-out measurement.
- **Evidence:** no independent holdout or predictive result is documented in the reviewed BEP materials.
- **Completion means:** the condition and data are independent of model construction/calibration, and predictive error and limitations are reported.

## Timing

The user's **tentative aspiration** is to make progress on numerical verification and the experimental comparison in the coming week or the week after, if feasible. There is **no hard date**. These checkpoints should be completed by the end of the thesis at the latest, with sequencing adjusted as source data and guided paper discussions allow. The near-term wording is a planning preference, not a deadline or a claim that stages 1–3 are already complete.
