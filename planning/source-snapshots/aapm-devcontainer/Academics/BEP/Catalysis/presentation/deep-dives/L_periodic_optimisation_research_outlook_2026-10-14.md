> **NIET BESPROKEN — NIET GEËVALUEERD — LETTER L**
>
> **DE GEBRUIKER HEEFT DEZE LETTER NOG HELEMAAL NIET INHOUDELIJK BESPROKEN OF GEËVALUEERD.** Deze Markdown bevat alleen door de assistant opgesteld onderzoeks- en conceptmateriaal. Presentatiekeuzes, prioriteiten en conclusies zijn **NIET DOOR DE GEBRUIKER BEOORDEELD OF GOEDGEKEURD**. Bespreek eerst de volledige inhoud voordat deze letter als afgerond wordt beschouwd.

# Deep dive L — From a predictor to a meaningful periodic experiment and input optimisation

**14 October 2026 · Scientific thinking material; NOT approved presentation slides or implemented optimisation.**  
Parent [A–M index §L](../RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [sub-story 02 (proposal → optimisation)](../sub-stories/02_proposal_to_predictive_optimization.md) · [sub-story 03 (future dynamic θ & radius distributions)](../sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md) · [sub-story 04 (noiseless identifiability first)](../sub-stories/04_model_fidelity_and_identifiability.md) · [K: no validated reactor result yet](K_results_validation_status_2026-10-14.md).

**Scope:** This note explores research questions and an experiment hierarchy, **not** a new software implementation, parameter fit, claimed yield improvement, novelty survey or automatic new slide. The user wants complete material for aloud reflection, with the assistant's **tentative editing choices above**. A parallel Work session is building the deck; it should draw only what the user later selects.

## 0. My provisional presentation selection

| Question | Presentation importance | Current status |
|---|---|---|
| **Can controlled periodic feeding outperform a fair constant-feed benchmark?** | **HIGH — core original BEP question** | Unanswered; K says no validated reactor result |
| **What counts as a fair performance measure and comparison?** | **HIGH — interesting mathematical question** | Objective/benchmark not implemented or ratified |
| **How much additional surface *memory* does non-PSSA actually provide versus a PSSA reactor with dynamic gas residence?** | **HIGH — scientifically discriminating comparison** | Two non-equivalent mechanisms/implementations; no verified matched run |
| **How to represent the inlet waveform (e.g. B-splines), without confusing input with state?** | **MEDIUM — mathematics supporting the main question** | In proposal only; no validated optimal control coefficients |
| **Parameter identifiability from clean synthetic cycles before noisy data** | **HIGH, already recorded elsewhere** | Optional [short sub-story 04](../sub-stories/04_model_fidelity_and_identifiability.md); do not duplicate slide |
| **Continuous distribution of particle radii in one shared-bulk reactor** | **CONSIDER / speculative outlook** | Deferred in [sub-story 03](../sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md) |
| Closed-loop MPC, observers, DeePC, wind-farm comparisons | **LOW now** | Separate future research, not the 2026 BEP baseline |

**Single scientifically useful sentence:** *Once we trust the predictor, we can test whether time-dependent inlet forcing increases cycle-averaged **net ethylene production** relative to a carefully chosen steady reference — and, separately, whether an explicitly dynamic catalyst surface is necessary to explain any advantage.*

## 1. What the written proposal promises — and what has not yet been shown

[Master proposal](../../0_Project_Management/main.tex) poses: *“How does periodic feed concentration forcing \(C_{\rm in}(t)\) alter spatial adsorbate dynamics and intermediary selectivity in a 1D packed-bed reactor?”* It distinguishes a **predictive open-loop reactor model** from subsequent **input-waveform optimisation**. It also proposes an **input B-spline basis** and a theoretical proof-of-concept. State observers and MPC are future avenues, not the primary deliverable.

The proposal's rhetoric that oscillating a feed **breaks** steady-state ethylene-yield caps, or that a specific desorption mechanism **must** explain such an effect, should be read as a **testable scientific hypothesis, not demonstrated fact**. A nonlinear PSSA reaction model with dynamic gas transport can respond in a time-dependent way and may show a changed cycle mean even **without** explicitly evolving surface coverages; such a result would **not** prove a special transient-surface mechanism.

**[FACT: source]** [Urmès 2019](https://doi.org/10.3390/catal9020180) fitted a physically interpretable LHHW/PSSA law for Pd/α-Al₂O₃ under steady intrinsic-kinetic conditions. [Urmès 2022](https://doi.org/10.1002/cctc.202101826) used **small-amplitude flow oscillations to identify elementary kinetic parameters**, and reported dynamic outlet composition reproduction with a single-site transient model. That published work is a relevant **precedent**, *not* our own result; **flow modulation and our proposed inlet concentration modulation are different experiments**. Do not claim a direct published demonstration of our specific waveform-optimisation objective from an abstract alone. Source 2022 publisher metadata/abstract verified 2026-10-14; full paper/SI mechanistic transfer is not verified in the current repository record.

## 2. Separate five questions that often get conflated

| Axis | Scientific question | Primary unknown / evidence | Here? |
|---|---|---|---|
| **Forward prediction** | What does a specified input \(u(t)\) produce? | A stable, conservative, appropriately calibrated PDE/MOL model; input→outlet trajectories | Essential prerequisite |
| **Inverse parameter estimation** | Which \(\mathbf p\) produce an observed outlet trajectory? | Identifiability, observational noise, sensitivity and independent benchmarks | Optional; [sub-story 04](../sub-stories/04_model_fidelity_and_identifiability.md) |
| **Open-loop input optimisation** | Which prescribed periodic \(u(t)\) improves an objective? | Tested forward model; objective; constraints; numerical optimiser | Original project ambition, not yet executed |
| **Closed-loop control/observer** | How do we update input using measurements during operation? | Sensors, dynamics, estimation, disturbances, control law | **Not** required now |
| **Implicit numerical time stepping** | How does the computer integrate the *same* ODE? | BDF vs RK/IMEX, stiffness/error/cost | Different mathematical axis entirely; [G](G_numerical_methods_jacobian_feasibility_2026-10-14.md) |

An **input control** \(u(t)\) is not a state \(x(t)\); the word *control* does **not** make an open-loop input programme a feedback regulator. [DECISION: terminology.]

## 3. Choose a physically meaningful periodic metric *before* optimising

Suppose the output includes inlet/outlet molar flow rates \(F_i(t)\) (mol/s). For an appropriately established **periodic steady regime** of period \(T\), a possible **net ethylene production-rate** objective per catalyst mass is

\[
J_{\rm net}=\frac{1}{T\,m_{\rm cat}}\int_{t_0}^{t_0+T}
\Big(F_{C_2H_4,\rm out}(t)-F_{C_2H_4,\rm in}(t)\Big)\,dt.
\]

Or define a **cycle-normalised net ethylene yield** on supplied acetylene:

\[
Y_{\rm net}=
\frac{\int_{t_0}^{t_0+T}(F_{C_2H_4,\rm out}-F_{C_2H_4,\rm in})\,dt}
{\int_{t_0}^{t_0+T} F_{C_2H_2,\rm in}\,dt}.
\]

These are **candidate definitions**, not a confirmed physical yield convention, implemented calculation, or experimental result. Actual gas **molar flow** should be used when inlet/outlet total flow can differ through reaction, pressure, etc.; \(Q\,C\) is appropriate only under clearly stated flow conventions. In this chemistry **ethylene is also abundant in the inlet** (70% at the Urmès source example), so gross ethylene *outflow* is **not** net production.

Also report cycle-integrated acetylene conversion and selective hydrogenation rather than collapsing the tradeoff into one magic scalar. Over a truly periodic state, initial and final bed and surface inventories match, so boundary integral differences are not secretly changes in stored material.

**Two legitimate but non-equivalent reference questions:**

1. **Same-mean reference:** compare selected \(u_{\rm periodic}(t)\) against \(u_{\rm steady}=\overline{u_{\rm periodic}}\), holding mean composition, offered acetylene/H₂ amounts, overall throughput and relevant physical constraints consistently fixed.
2. **Best steady competitor:** compare \(\max_{u(t)\text{ periodic}} J\) against \(\max_{u\text{ constant admissible}}J\). Only this stronger comparison directly supports a claim of periodic advantage **over the best steady operating condition under those constraints**.

**[UNRESOLVED human question]** Which performance criterion is the BEP's actual target: net yield, production rate, selectivity at a specified conversion, or a constrained multi-objective Pareto tradeoff? These differ and could select different waveforms. The user/supervisors must approve it. Do not announce a broken “steady-state cap” before both comparisons, and do not claim a global optimum from local optimisation.

## 4. Periodic forcing is an *experiment design*, not just a sine wave

A first input might be \(u(t)=\bar u+A\sin(2\pi t/T)\) for an acetylene feed fraction/concentration. Need to define **what is held fixed** (hydrogen, total pressure, total inlet molar flow, temperature) and which inert gas fraction compensates any altered reactive feed fraction so mole fractions remain valid. Actuator concentration, speed/slew, allowable hydrogen ratio, and positivity constrain the waveform.

Only measure the **periodic steady cycle** after transients die out (for each forcing condition), preferably check \(\|x(t+T)-x(t)\|\) and repeatability over consecutive cycles. A terminal-state difference between an oscillated and constant experiment proves neither periodic steady state nor a cycle-integrated yield change; the Hermes gate C does only this weaker comparison. [I optional bridge](../sub-stories/05_reacting_model_inlet_candidate.md).

Frequency matters: the gas residence, adsorption/desorption relaxation, pore diffusion, detector dynamics and **numerical advection/step errors** can give different gain/phase. Critically, [G](G_numerical_methods_jacobian_feasibility_2026-10-14.md) shows a pure-advection first-order-upwind *continuous-time MOL* example with ~28% amplitude attenuation at 60 cells and forcing period equal to the residence time. This is a **derived numerical artefact screen**, not the simulated reacting outlet, and Forward Euler at CFL=1 for *pure advection* is a special exact-cell-shift exception. Resolve/limit numerical errors before interpreting chemistry, optimiser response or parameter identifiability.

A good **scientific first experiment** is to sweep *input period and amplitude* for a small set of physically realistic cases, compare PSSA gas-only and calibrated non-PSSA site dynamics under otherwise matched conditions, and measure **cycle-averaged objectives plus harmonic phase/amplitude**. Do not confuse these separate outputs: a waveform can alter phase without improving a cycle mean.

## 5. What B-splines actually buy us

The proposal's finite-dimensional input parametrisation could be

\[
u(t;a,T)=\sum_{k=1}^{m} a_k\,B_{k}(t/T),\qquad u(t+T)=u(t),
\]

where \(a_k\) are design variables and \(B_k\) is a periodic B-spline basis. The optimisation seeks a set of input control points (and perhaps period \(T\)) that improve a *defined* objective subject to a solved dynamic model and constraints.

This is **not** a reduced model of reactor state space, and **not** evidence that the optimum has been computed. It simply makes the infinite-dimensional waveform search manageable. It supports bounded/continuous waveforms; chosen knots/control points and derivative constraints govern their smoothness, but periodicity requires periodic basis/endpoint matching. Even with a smooth waveform, a poorly resolved spatial grid or stiff ODE may generate a misleading objective.

**Question worth debating:** For an 8–10 minute research presentation, is an animated B-spline waveform or a sine→optimised-shape cartoon scientifically helpful, or would it imply a result we do not yet have? Likely **backup/one sentence**, not necessarily a dedicated slide.

## 6. Stronger experiment: does the surface need real memory?

A dynamic gas/PSSA reactor satisfies \(\dot C_b=f_{\rm flow}(C_b)+f_{\rm source}(C_b)\), while non-PSSA kinetics also contains evolving adsorbates \(\dot\theta=g(C,\theta)\) that *feed back* into gas rates.

At the same **instantaneous local gas composition** a non-PSSA catalyst may (under appropriate kinetics) have **different rates depending on prior occupation**. A PSSA closure cannot reproduce that particular state-dependence because it sets the coverages algebraically from instantaneous conditions. But the PSSA reactor's **outlet** can still show memory/phase lag from finite gas residence or pore transport. An outlet lag is therefore **not proof of dynamic θ**, nor is “PSSA responds to forcing” evidence that its chemistry is non-PSSA.

A matched thought experiment:
1. Construct a **source-supported**, atom- and site-conserving, calibrated dynamic-θ mechanism. The current **draft PR #3 is not that yet**: it has a local code seam and unsourced rate constants.
2. Test **identical** reactor, catalyst assumptions, mean feed, inlet waveform, flow, meshing and actual output definitions for PSSA vs transient-surface models.
3. Sweep periods around independently justified **surface timescales**, not arbitrary microsecond claims from proposal rhetoric.
4. Compare observable gain/phase, cycle-averaged ethylene production and **practical parameter distinguishability**. If both give essentially the same outputs in the physically relevant regime, adding surface states may be unnecessary for that question.
5. Decide whether new experimental evidence justifies the extra parameters and stiff computation.

**[UNVERIFIED]** Current available evidence does not show whether these models differ enough to affect predicted ethylene yield; do **not** claim PSSA fails or dynamic kinetics guarantees a periodic advantage.

## 7. Secondary speculation: pellet-size population in one reactor

[Sub-story 03](../sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md) is explicitly **future, not implemented**. The physically intended extension is **one shared bulk gas** coupled to a *mass-/surface-weighted continuous distribution* of pellet radii, not five independently simulated reactors. Diffusion times can scale as \(\tau_p(R)\propto R^2/D_{\rm eff}\) under simple conventions; a distribution of \(R\) gives a distribution of relaxation times and might broaden response, but it will matter only if radial diffusion/particle size is consequential in the chosen operating regime.

Use a normalised appropriate \(w(R)\) and source \(\bar q(z,t)=\int w(R)\,q(z,t;R)\,dR\). Careful: a *number-weighted* particle size distribution needs mass/area conversion before averaging catalytic source rates. Numerical quadrature can approximate a continuous integral without changing the scientific claim. **No actual size-distribution advantage/loss has been measured or computed.**

This is a good optional *outlook image*, **not** necessary for current scope or a slide decision.

## 8. Practical sequence — each gate has a distinct meaning

| Stage | Minimal scientific evidence needed | Status 14 Oct 2026 |
|---|---|---|
| A. Governing physics/kinetics accepted | Source-appropriate, stoichiometrically consistent forward model, pressure and catalyst transfer resolved | **OPEN**; original zero-kinetics scaffold; synthetic PSSA path needs model validity checks |
| B. Numerical result trusted | Conservation/positivity and mesh/time refinement for **outlet waveform amplitude/phase** and cycle-integrated metrics | **OPEN**; G/J issues outstanding |
| C. Ideal-input experiment | Sustained periodic state for a known waveform, measured cycle-integrated metric, equal-input steady comparison | **NOT DONE** |
| D. Inverse inference | Source-consistent parameters distinguishable under **noiseless** chosen forcing; only then noise/repeats | **NOT DONE**, optional [story 04](../sub-stories/04_model_fidelity_and_identifiability.md) |
| E. Modulation advantage | Candidate periodic inputs vs best admissible constant feed, correct normalisation and budget | **NOT SHOWN** |
| F. Optimised waveform | Input basis, physical constraints, optimisation algorithm, independent re-evaluation of candidate | **NOT DONE** |
| G. Experimental transfer | Hardware limits, analyser response, drift, independent measurements, validation of yield improvement | **FUTURE** |
| H. MPC / state estimation | Feedback measurements, observers, online optimisation/uncertainty | **BEYOND present scope** |

The scientific program may **stop early** if a reduced/PSSA model already suffices or if the data cannot identify more detailed chemistry. That would itself be a useful justified conclusion; the goal is not to maximise modelling complexity.

## 9. Editorial choice for the parallel deck

**The one likely-worthy outlook statement:** “Once a credible forward predictor exists, we can design controlled inlet cycles and test *fairly* whether periodic operation yields more net ethylene than steady operation — and whether the extra surface dynamics matter at all.”

**Possible on-slide/open-question graphic:** **constant mean feed** vs **equal-budget modulated feed** → both through same independently validated reactor → compare **cycle-integrated net ethylene**; dashed box **“compare with best allowed steady feed too”**.

**Optional supporting talking points:** the necessary distinction between PSSA outlet residence dynamics and true adsorbate history; B-splines as a bounded *input* parametrisation; separate parameter-estimation question from [story 04](../sub-stories/04_model_fidelity_and_identifiability.md). **No requirement to include any of these before user review.**

**Out of scope now:** implementing an optimiser, long control-theory exposition, numerical radius distribution integration, post-2022 citation/novelty surveys, assuming Damian/Zoë accepted the optimisation metric, or claiming successful periodic performance.

**Sources/links:** [master proposal](../../0_Project_Management/main.tex) · [2019 publisher](https://www.mdpi.com/2073-4344/9/2/180) · [2022 publisher](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cctc.202101826) · [SM-9 fair optimisation open decision](../../research/wayfinder/scientific_method_selection.md) · [sub-story 03](../sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md) · [G](G_numerical_methods_jacobian_feasibility_2026-10-14.md) · [K](K_results_validation_status_2026-10-14.md).
