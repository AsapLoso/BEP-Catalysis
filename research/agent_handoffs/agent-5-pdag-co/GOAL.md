# Agent 5 — PdAg + CO Exploratory Synthesis (AI Reference Track)

**Assigned branch:** `feat/pdag-co-synthesis`  
**Status (2026-10-25): PAUSED — NOT AUTHORIZED TO START CO COUPLING OR CREATE THE NEW MODEL YET.**  
**Owner decision:** Run two **separate independent source/benchmark audits** first; review their evidence, then request an explicit **go / no-go** from the owner. Preparing this goal and importing reference files is not that approval.

## 0. Mandatory upstream gates: separate work, no premature synthesis

1. **Agent 1 — Schbib 1996:** [Issue #10](https://github.com/AsapLoso/BEP-Catalysis/issues/10), branch `feat/schbib-co-benchmark`. Verify the original Table 8 and any author/journal correction, common-log pre-exponentials, catalyst/adsorption units, actual rate expressions, reactor conditions and the severely discrepant **Table 6 benchmark**. Supply an independently executed, source-faithful baseline, or a documented BLOCKED result with sources and exact reasons.
2. **Agent 4 — Larsen 2024:** [Issue #11](https://github.com/AsapLoso/BEP-Catalysis/issues/11), branch `feat/larsen-pdag-benchmark`. Verify original Eq. 6.9–6.11 against the *full thesis*, especially the denominator power in `r2` and `r1` cap; investigate flow-rate reference conditions (actual vs standard volume), fitted parameter units and the no-CO experimental comparisons. Supply an independently executed source-faithful baseline or a documented BLOCKED result.
3. **Review/approval gate:** Read both audited reports and concrete outputs, compare unresolved source ambiguities and original-vs-corrected artifacts; the owner must then explicitly decide whether and how to proceed with Agent 5. **Neither issues closing nor a successful Git merge alone is permission.**

**Until this gate is satisfied:** do not start a PdAg–CO synthesis agent run; do not produce or modify `notebooks/benchmarks/pdag_co_synthesis.ipynb`, and do not treat imported A1/A4 notebooks as validated inputs. The existing imports from [PR #9](https://github.com/AsapLoso/BEP-Catalysis/pull/9) are read-only **historical snapshots** at their pinned SHA; they do not automatically update when agents correct their own branches. A later targeted, inspected import of corrected results must be separately planned.

## 1. Conditional research objective (AFTER explicit owner go-ahead)

Develop a **deep, source-grounded AI reference report** comparing the actual Schbib and Larsen mechanisms, experimental conditions, equations, units, parameter provenance and reproduction quality. Identify which rates and observations are genuinely source-supported, which were fitted, digitized, inferred, or assumed, and where transfer between different catalyst systems cannot be defended.

**Primary research artifact:** `research/reports/pdag_co_synthesis_deep_research.md`.  
**Secondary exploratory artifact:** `notebooks/benchmarks/pdag_co_synthesis.ipynb`, only if a defensible candidate comparison can be implemented. Neither is owner writing or personally approved theory.

Separate at minimum:

- **Source-faithful, CO-free Larsen baseline**: use verified Eq. 6.9–6.11 (including capped `r1`), checked feed/flow/pressure/mass conventions, independent numerical/experimental validation receipts, and explicit uncertainty. Never inherit the imported squared `r2` denominator without checking its agreement with the actual source.
- **Schbib CO adsorption**: verify primary and corrected parameter sets and dimensional meaning; `13.6` is *not* an adsorption coefficient when it denotes a logarithm, and correction leads (e.g. approximately `10.16`) require primary-document verification before choosing values.
- **Candidate CO coupling(s)**: formulate at least a common-denominator control and one mechanism-differentiated hypothesis, each explicitly conditional. If concentrations are in mol/m³, derive `C_CO = p_CO/(R T)` with consistent `R`, pressure units, temperature and adsorption units. Do not treat transfer from Schbib's Pd catalyst to Larsen's PdAg alloys as experimentally validated.
- **Selectivity countercheck**: where the two original Schbib rate expressions share exactly the same denominator, it cancels in their local *uncapped* rate ratio. Examine what a Larsen `r1` cap, different denominators, axial conversion and genuinely different CO site mechanisms would do. Never assume CO selectively inhibits overhydrogenation or breaks a Pareto frontier.

## 2. Conditional computational exploration

After source and unit gates, consider an **isothermal, steady** reference comparison at `373.15 K` and `1 bar`, across all three Larsen catalyst cases. A nominal feed series `0–1500 ppm CO`, replacing He at fixed total molar feed, may be compared at a **mass-normalized** flow of `60,000 cm³(ref) h⁻¹ gcat⁻¹`. Only call it STP when the original reference volume convention has actually been verified. The `40,000/80,000/120,000` flow sensitivities and `0.01–100×` transferred adsorption-strength sensitivities are exploratory assumptions, **not** confidence intervals, calibration evidence or per-alloy experimental validation.

Verify: stoichiometry/element balance, dimensional factors, positive denominators, exact zero-CO recovery of the *source-faithful* rate law, solver convergence and comparison with **independent original data** (not just self-consistency). Report null/negative results and source limitations. Record whether the target <90s runtime was met; do not sacrifice source checks for that performance target.

**Transient forcing is OUT OF THE RUNNABLE SCOPE by default.** Reconsider it only if measured/source-backed gas holdup/transport or valid finite-rate surface-coverage kinetics can justify a scientifically meaningful model. A time-dependent gas inlet with equilibrium surface coverages is not proof of independent surface kinetic memory.

## 3. Knowledge ownership and branch constraints

- This assignment is **agent-generated reference research only**. Do not edit the user's `current_map.yaml`, approved personal map nodes, verified citations, owner reader documents, or personally authored notebook. There is a separate, detailed **review queue Q99–Q106**, not an approved knowledge expansion, on `AsapLoso/project-management-agents` / `docs/bep-theme-first-progress-units-20261022`.
- Preserve Agent 1/4 outputs in their independent branches until reviewed. **Do not merge their branches wholesale** or silently overwrite an imported historical snapshot.
- Once the owner explicitly reauthorizes Agent 5, the agent may research, experiment, commit and push **only** to `feat/pdag-co-synthesis` without per-commit approval, while preserving branch ancestry. Do not force-push, rewrite other work, merge to another branch, create a PR or modify another branch without instruction.
- Report the exact branch/commit SHA, claims verified against primary sources, notebook execution environment, tests and unresolved questions. Mark each acceptance gate as **completed, unverified or blocked** in `TODO.md`. No speculative finding is promoted automatically into human understanding.

**Historical note:** Prior revisions of this `GOAL.md` asserted a specific combined rate law and dynamic selectivity enhancement before the two source baselines were re-audited. Those are superseded hypotheses and remain recoverable in Git history, not presently approved physical conclusions.
