# Hermes execution mission — First defensible reacting reactor vertical slice

**Date:** 2026-10-13. **Mode:** autonomous implementation + reproducible science, not map-building or audit-polishing. **Owner:** existing BEP Catalysis scientific Wayfinder. This supersedes the *priorities*, not the evidence or safety rules, of [the overnight Wayfinder mission](HERMES_EXECUTE_WAYFINDERS_2026-10-13.md).

## Where you are now — do not restart from zero

The overnight run has already added the [scientific briefing](BEP_SUPERVISOR_BRIEFING_2026-10-13.md), [evidence bundle](evidence/README.md), [implementation probes](../../3_Model/probes/), a source-verification runbook and updates to `research/wayfinder/scientific_method_selection.md`. Source-linked Urmès 2019 kinetics, historical D1–D6 checks, reported **37 passing `pbr` tests**, and known `pbr` deficiencies exist. The package's current behavior is **not** validated transient microkinetics; do not conflate optional coverage relaxation with reaction-rate feedback.

Important intake: [scientific synthesis → Wayfinder deltas](synthesis_to_wayfinders_2026_10_13.md). Its three proposed research probes are candidates, **not** new decisions or tasks automatically assigned.

**One bookkeeping correction:** `3_Model/probes/pbr_implementation_receipt.json` holds four operating-point/temperature rows × three species. H₂ is below the paper's reported coverage range at OP1 at 51 °C and 62 °C, hence **10/12 numerical range checks pass** (one distinct discrepancy, two failed evaluations). Correct the headline once via a programmatically derived count, record the two misses as backlog, and move on. These checks are **not** 12 experimental validation points. The defect-register cleanup and a perfect dashboard are **not** this mission.

## Start correctly — GitHub and scope

1. First read the current `.agents/AGENTS.md`, `.agents/skills/wayfinder/SKILL.md`, `WEDNESDAY_START_HERE.md`, this mission and the evidence files. Inspect the actual current code before assuming anything is still missing.
2. Safeguard any uncommitted work. **Fetch `origin/devcontainer` and pull its latest changes**: on a clean local `devcontainer`, use `git pull --ff-only origin devcontainer`; otherwise work from fresh `origin/devcontainer` in a separate clean worktree/branch. Do not reset or overwrite ongoing Luna presentation work or the existing execution branch.
3. Work on a **dedicated implementation branch** in `AsapLoso/project-management-agents`, or follow repo-authorized branch policy. The sibling `AsapLoso/Methanol-Catalysis` may be used for component reuse **but do not push to its public `main`** without explicit user authorization. Do not commit hidden local data, absolute private paths, secrets or sensitive metadata.
4. The immediate deliverable is **one executable scientific vertical slice**, not a repaired full 1,480-coordinate model, not an MPC design, not parameter fitting and not a new Wayfinder map. Independent scientific-method selection decisions remain human-only.

## Target physical model

Implement the smallest coherent **isothermal transient 1D axial packed-bed reactor** for
`C2H2 + H2 → C2H4` and `C2H4 + H2 → C2H6`, with published **Urmès et al. (2019) LHHW** kinetics as a **quasi-steady surface-equilibrium baseline**.

- Derive explicitly the time-dependent axial gas balances, advection, local reaction source terms, porosity/catalyst-loading factors, inlet/outlet boundary conditions and units. The equations must agree with the executable implementation.
- Use the *actual imported* source-backed kinetic parameters; assert source correspondence in code/tests rather than comparing two hand-entered copies. Confirm Arrhenius temperature conventions and dimensions. Keep argon/inert dilution in the mole fractions and partial pressures (`p_i=y_i P_total`); do not silently renormalize reactive species.
- Declare geometry, bed voidage, loading, flow, temperature, pressure and feed composition, stating precisely which are from the paper, from a known implementation or **illustrative only**. Do not invent literature provenance.
- Start with the simpler physically consistent transport/chemistry coupling. Pellet-scale radial diffusion and explicit dynamic coverages belong to later milestones unless essential for mathematical consistency of the chosen reduction. State clearly that this baseline is **not** the final dynamic-coverage hypothesis.

## Measurable acceptance gates

**A — Source + physics gate.** Supply the exact governing equations and numerical mapping; audit units for every gas/source term and stoichiometry for both reaction steps. Executed tests must check source-to-**runtime** parameter consistency and atom conservation (C and H) of the source terms. Wrong pressure normalization, inventory accounting, kinetic sign or dimensions **blocks scientific claims** until resolved.

**B — Nonzero steady-inlet reaction.** From a documented initial condition, run an executable fixed-inlet simulation with nonzero reaction rates. Save actual concentration arrays and plots of spatial profiles and the outlet transient. Assert meaningful acetylene consumption and correct-direction ethylene/ethane terms or explain a source-supported regime in which a term is negligible. Report conditions and final integration time; a solver-success flag alone does not pass.

**C — Periodic inlet demonstration.** Run a modest sinusoidal **acetylene feed perturbation** under documented physically admissible conditions, with a constant-inlet baseline at the **same average feed** and all other relevant conditions held fixed. Save time traces, input and outlet plots, and explicitly distinguish initial transient from any periodic regime; only call a periodic steady cycle if tested. Demonstrate the outlet response to forcing. **Do not assert yield enhancement** without a defined, fair, cycle-averaged comparison and convergence evidence.

**D — Numerical sanity gate.** Execute and archive:
- A zero-reaction / zero-rate limit with a physically expected transport response;
- Carbon/hydrogen stoichiometric consistency and appropriately formulated reactor inventory checks;
- Nonnegative physical concentrations within a documented absolute numerical tolerance, and a clear outcome if violated;
- A controlled axial-grid and ODE-tolerance refinement study on a named outlet observable. Target <5% relative change where the observable is bounded away from zero; if it fails, report the actual variation and **restrict the conclusions**, rather than tuning away or hiding the failure.

**E — Reproduce and communicate.** Provide a minimal run command in a clean supported environment; deterministic parameter/config snapshot; executable tests with machine-readable pass/fail receipts; real saved figures; a brief evidence-led interpretation (what is supported, what is illustrative, what remains unverified); and a short handoff pointing Luna to the figures and their scientific caveats. No invented simulator outputs or paper measurements.

## Execution policy / stop condition

- Known legacy code bugs and the two H₂ coverage-range misses go to the backlog if they **do not affect the specific result being claimed**. Critical new conservation, units or rate-law defects must be fixed or the relevant output must be marked invalid.
- Make the smallest version work first, then test it. Do not spend time converting the entire prior audit into a report, reopening already settled numerical conventions or implementing every sophisticated feature.
- Follow Wayfinder governance: update the **existing** scientific-method map with dated execution receipts; do not self-answer `wayfinder:grilling` decisions or let a delegated worker edit state-engine files. Never mark a prototype or predictive model scientifically validated merely because its scripts run.
- Respect the separate Wednesday presentation workflow: Luna owns slide design; this worker provides only **reproducible figures, interpretations and caveats**. Existing briefing prose can remain except for the 10/12 factual correction.
- Preserve meaningful partial results if a gate fails and continue independent work. Explain which result is trustworthy versus blocked.

**Definition of done:** From the pushed implementation commit, another worker can run the documented command, reproduce both simulations, inspect source-to-runtime parameter assertions, obtain the figures and test outputs, and understand each claim's validation limits.

**Final answer:** link implementation branch/commit, entrypoint and figures; give exact commands and a compact table of gates A–E (PASS / FAIL / PARTIAL + evidence paths); identify known exceptions, human decisions, and the next smallest scientific extension. **Do not report “Goal done” solely because a checklist was created or reports were written.**
