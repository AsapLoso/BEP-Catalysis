# Independent audit prompt — 18 Oct 2026 BEP reactor scientific recovery

> **AUDIT RESULT 21 OCT 2026: INCOMPLETE.** A bounded non-author review is recorded in [independent_audit_receipt.md](independent_audit_receipt.md). The original visible user turn was unavailable, so that receipt cannot certify verbatim completeness. This file remains the criteria for a future reviewer with access to the original turn.

## Copy-ready mission

You are the **skeptical independent audit reviewer** for the user's Applied Physics/Applied Mathematics BEP reactor-research restart.

**Do not write code, accept scientific assumptions, approve a deck or merge anything. Audit first.** The user explicitly complains that the assistants spent time validating a reduced reacting gas baseline while the core model goal — radial pellet transport, dynamic catalytic surface states and reliable periodic response — was no longer represented in its default simulation.

### Read in this exact order

1. Current **visible original user message dated 18 October 2026**, beginning “Dus op dit moment zitten we niet echt meer met de presentatie in gedachten” and ending “Antwoordt niet veel.” If the original ChatGPT turn is not accessible, **do not claim verbatim accuracy**; mark a limitation and use [transcript-near note](../../notes/user_thought_dump_2026_10_18_reactor_recovery.md) with that caveat.
2. [47-point claim-to-action register](decision_and_implementation_register.md).
3. [Full K baseline interpretation](../../../presentation/deep-dives/K_full_results_interpretation_2026-10-18.md), [K status](../../../presentation/deep-dives/K_results_validation_status_2026-10-14.md).
4. [Existing scientific-method Wayfinder](../../wayfinder/scientific_method_selection.md), [dynamic-numerics Wayfinder](../../wayfinder/bep_dynamic_numerical_accuracy.md), [E operating regime](../../../presentation/deep-dives/E_operating_regime_transport_2026-10-14.md), [F bulk–pore conservation](../../../presentation/deep-dives/F_conservation_state_space_2026-10-14.md), [G time/space numerics](../../../presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md).
5. Source code from exact branches: [legacy on devcontainer](../../../3_Model/c2h2_hydrogenation_transient_model.py), [Hermes reacting code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py), [Hermes sensitivity code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/sensitivity_study.py), [Hermes frequency code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/frequency_response.py), [pbr/ local snapshot audit](../../dossiers/scientific_wayfinder_2026_10_13/alternate_implementation.md) and current [AsapLoso/Methanol-Catalysis/main](https://github.com/AsapLoso/Methanol-Catalysis/tree/main).
6. Primary source evidence: [2019 Urmès](https://doi.org/10.3390/catal9020180) and [2022 Urmès](https://doi.org/10.1002/cctc.202101826) abstract/full text/SI if available; 2008 Berger/Urakawa paper only with verified bibliographic identity and equations. Cite table/equation/operating-condition rather than loose recollection.

### Required checks (NO rubber stamp)

**A — COMPREHENSIVENESS (the main audit):**
- Create a matrix of **every independently actionable utterance** from the original user message, with source quote/position and Uxx register ID. Identify **missing, merged incorrectly, softened or misattributed** criticisms; explicitly report count and severity. The original contains voice-recognition hesitations, doubts, rhetorical language and proposals, not settled technical decisions. Keep them.
- Verify that the raw thought-dump note is **not falsely called exact transcript** and that the user's non-presentation priority and desire to own the science are preserved.
- Check that *no* K, L or M slide decision has been retroactively called approved: **K partially evaluated, L/M not user-evaluated**.

**B — PHYSICS AND NUMERICS:**
- Independently derive correct bulk + pore + dynamic-θ conservation equations, interface-flux source normalization, and physical variable units. Check F's alleged double-booked reaction source against actual radial RHS; if not reproducible, mark HYPOTHESIS, not defect.
- Check what 11 and 13 physical field-types refer to versus state-vector allocated size, time samples, and experimental/operating parameters. Verify the 'one PDE' description is *scoping criticism*, not the literal count of equations.
- Compare 2019 source reaction/catalyst/feed conditions (especially α vs γ alumina, 0.1 g vs 75 mg, 4 vs 5 mm, 0.5 g diluent, flow reference T/P) to Hermes source config. Are same source condition IDs compared, or are 950 Pa and 1.260 Pa different experimental points?
- Verify why the 10/12 coverage intervals fail: **not** merely 'outside fit T/P' without exact source rows. Confirm whether all 12 are *in-domain* even when the computed coverages miss bounds.
- Differentiate linear steady sinus transfer vs nonlinear response/DC shift/harmonics; state observable-specific sample and periodic-settling criteria. Check circular claims about '8 cycles enough' and '50 ms response'.
- Verify analytic pure-advection upwind harmonic transfer \(H=(1+i\omega\Delta z/v)^{-N}\) and its N=60 attenuation vs Forward Euler CFL=1 fully discrete exception. **No claim that reducing Δt alone cures exact-time spatial error.**
- Check stationarity X=0.0930497, 30→120 mesh change, analytic Jacobian gates and what they actually establish. If extra numeric residuals aren't executed, mark NOT RERUN.
- Reproduce the claimed **factor-six sensitivity-figure** τ_p discrepancy from code algebra and inspect alleged frequency-response sol.y reshape failure; if no runnable env, mark STATIC CODE EVIDENCE ONLY.
- Confirm public remote \`Methanol-Catalysis/main\` actually has/doesn't have pbr/ and don't confuse local Git refs or branches with remote publication.

**C — SPEC / ROADMAP SOUNDNESS:**
- Are Kα–Kθ small, disjoint enough for scoped agents? Show blockers vs parallelizable efforts.
- Which **smallest valid scientific vertical slice** would establish (i) exact 2019 benchmark, (ii) coupled radial dynamics and conservation, (iii) published dynamic-θ, (iv) valid periodic observables without conflating them?
- Is within-domain DOE physically constrained (mole fractions, H2 budget, fixed mass vs volume flow, source pressure and temperature window)? Are grids/LHS compared without invented validation beyond empirical data?
- Check governance: the desired Methanol-Catalysis CI can be developed only after actual pbr package is available and reviewed; no unapproved public publication of private/sensitive code or paths.

### Output: exact form

Write **\`independent_audit_receipt.md\`** (read-only first, PR later if user permits), containing:

1. **Verdict:** COMPLETE / INCOMPLETE / UNSAFE-TO-EXECUTE; counts of Uxx checked/covered/missed/distorted.
2. **Missing user points** with precise proposed text; no silent edits.
3. **Claim/uncertainty corrections** citing exact code lines/source tables and calculation assumptions.
4. **Top five blocking scientific issues**, prioritized; separate user decisions from source research.
5. **Proposed next implementation tickets** each with exact acceptance test and boundary; no arbitrary 10-second/50-ms integrations or solvent/source assumptions.
6. **Exact files examined, refs/SHAs, date, reviewer identity**, and what could not be independently verified.
7. **Required redlines** against the thought-dump note and the 47-point register without executing code.

A reviewer who has not opened original sources may only say **NOT VERIFIED**, never PASS.

**The auditor must not be the author automatically re-reviewing their own conclusions.**
