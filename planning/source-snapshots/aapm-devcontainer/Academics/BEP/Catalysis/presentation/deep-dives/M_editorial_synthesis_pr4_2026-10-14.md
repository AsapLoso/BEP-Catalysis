> **NIET BESPROKEN — NIET GEËVALUEERD — LETTER M**
>
> **DE GEBRUIKER HEEFT DEZE LETTER NOG HELEMAAL NIET INHOUDELIJK BESPROKEN OF GEËVALUEERD.** Deze Markdown bevat alleen door de assistant opgesteld onderzoeks- en conceptmateriaal. Presentatiekeuzes, prioriteiten en conclusies zijn **NIET DOOR DE GEBRUIKER BEOORDEELD OF GOEDGEKEURD**. Bespreek eerst de volledige inhoud voordat deze letter als afgerond wordt beschouwd.

# M — Assemble the BEP research presentation: editorial synthesis of PR #4

**14 October 2026 — FULL THINKING MATERIAL / PROVISIONAL EDITORIAL REVIEW. Not a final approved deck or instruction to merge PR #4.**  
Central index [§M](../RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [master structure](../PRESENTATION_STRUCTURE.md) · **[first ten-slide Work deck PR #4](https://github.com/AsapLoso/project-management-agents/pull/4)** · [actual global outline in PR branch](https://github.com/AsapLoso/project-management-agents/blob/codex/bep-presentation-2026-10-14/Academics/BEP/Catalysis/presentation/GLOBAL_PRESENTATION_OUTLINE.md) · [speaker cues](https://github.com/AsapLoso/project-management-agents/blob/codex/bep-presentation-2026-10-14/Academics/BEP/Catalysis/presentation/SPEAKER_NOTES.md).

## Status correction — 22 October 2026

The 14 October checks below correctly described PR #4 as open/unmerged at that time. GitHub confirms that it merged into `devcontainer` on 15 October 2026 at 22:40:12Z (merge commit `faa678b865e044188ecb827513e5079cc88ebcd2`). This records repository integration only; it does not imply owner approval, scientific validation, or approval of the editorial recommendations.

**Division of work:** The parallel Work session owns the **editable slide deck, DOCX, global bullet outline and rendering QA** on its **separate** branch \`codex/bep-presentation-2026-10-14\`. This M note on **devcontainer** is the scientific discussion/editorial review, **not a competing new deck or overwritten source**. When selected, editorial changes should be picked up in that branch/PR; keep unselected narratives optional. As of the 14 Oct ~08:56 local read, PR #4 was **OPEN/UNMERGED**; see the status correction above. Its snapshot is not a user-approved final talk.

## 0. My tentative presentation choices (to discuss with the user; not locked)

| Topic | Priority | Why |
|---|---|---|
| The original acetylene→ethylene→ethane question and **why timed feeding might help** | **CORE** | Makes the model scientifically motivated |
| **Physics of stored state** (bulk, pores, adsorbed sites) and state-space/MOL | **CORE** | Genuine mathematical/physical model; useful explanatory visual |
| The **two complementary code designs**: old 1,480 allocated coordinates/dynamic θ ambition vs new 240 gas states/source-backed PSSA chemistry | **CORE** | Scientific choices rather than winner/loser chronology |
| **Stiffness, spatial upwind and Jacobian** | **CORE / should be concise** | The numerical research question directly affects the reliability of a forced waveform |
| **Pure-advection wave amplitude+phase test**, with Euler CFL=1 exception | **STRONG OPTIONAL FEATURE** | Only fully defined, independently derivable example with an actual number; don't let it masquerade as reacting yield |
| Parameter correlation, detailed fitted coefficients, 2019/2022 and literature chain | **SUPPORT / backup** | Justify kinetic gaps; avoid an isolated literature lecture |
| **Current scientific status: no accepted reactor-performance result** | **CORE, concise** | Evidence boundaries; avoid implying simulator prints establish physical chemistry |
| How a **fair periodic-vs-steady performance comparison** would be done | **CORE closure** | The actual experiment that could answer the proposal |
| Noiseless-first identifiability + many noisy repeated cycles | **OPTIONAL one brief aside** | Scientifically interesting, already in [story 04](../sub-stories/04_model_fidelity_and_identifiability.md); not a separate mandatory slide |
| New reacting model with controllable inlet [story 05] | **🚩 OVERWEEG / NOT APPROVED** | Work PR #4 has it inside slide 5, but this is a *candidate bridge* and not yet owner-approved |
| Pellet-size distribution, full dynamic microkinetic research, MPC, control/observer, DCSC | **FUTURE / optional backup** | Open tangents, not demonstrated or compulsory |

**Editorial thesis:** This is the evolution of an **executable mathematical and physical test** of a hypothesis, not a chronological programming diary or proof of an improved yield.

## 1. What exists NOW in the separate Work PR #4 (checked on GitHub)

The branch contains a **ten-slide 16:9 offline HTML deck**, a **ten-page PDF**, an **editable 30-native-bullet DOCX**, global Markdown outline, concise cues, explicit scientific claim/source ledger, integration log, QA record and editable content JSON. PR body reports all ten slides rendered/inspected on two display sizes and offline behavior tested with a managed-browser limitation; this is **a reported QA checkpoint, not independently rerun by this M review**. At the 14 Oct 2026 check, the work branch was still **not merged** (see the status correction above).

The actual sequence (9.5 minute *editorial allocation*, not observed rehearsed timing):

| # | Current Work deck point | Editorial judgement |
|---|---|---|
| 1 | Can timing the feed favor ethylene? | **KEEP** opening question and intermediate/overhydrogenation chemistry |
| 2 | Two reasons timing could matter | **KEEP maybe shortened**: nonlinear effective rates vs independent θ memory; don't assert either gives a gain |
| 3 | Describe where the history lives | **KEEP core visual**, bulk/pore/site → x(t); might overlap slide 4 |
| 4 | 11 fields become 1,480 coordinates | **KEEP old model spotlight**, avoid repeating every state-space explanation from slide 3 |
| 5 | Reacting gas, quasi-steady surface | **KEEP equally serious new spotlight**, but flag optional [story 05](../sub-stories/05_reacting_model_inlet_candidate.md) as *proposed/consider* rather than user acceptance |
| 6 | More states need more kinetic information | **CONSIDER condensing into 5 or a Q&A backup**; the 5-fitted/3-fixed 2019 parameters are useful scientific caveat, not necessarily a complete slide |
| 7 | Compute the transient we mean | **KEEP G in rough mathematical terms**: MOL/upwind, BDF actually in code; Forward Euler is a proposed test; stiffness and Jacobian |
| 8 | The grid can change the pulse | **PROMISING mathematical highlight**, maybe show amplitude plus a small phase inset and no more than one key equation |
| 9 | Know what each result establishes | **KEEP but SHORT**: model components and source checks exist; conversion/selectivity values are not scientifically validated |
| 10 | Use the predictor to test and learn | **KEEP closing the loop** to fair steady vs periodic yield and needed physical/dynamic kinetics. Risk: this slide currently mixes optimisation, fit/noiseless experiment and noise/cycles; choose one main line, and put identification in a secondary cue. |

**Potential compression A:** merge slides 3 and 4 by using the same pellet visual and revealing old-model state dimensions only after explaining physical storage (saves ~1 minute).  
**Potential compression B:** merge 5 and 6 or turn 6 into a footnote/short spoken line; don't turn a parameter list into the centre of the talk.  
**Potential expansion if audience is mathematical/Zoë:** retain distinct numerical slides 7 and 8, with a clean *pure transport vs reacting physics* comparison; formulate a question about error control rather than enumerate defects.  
**Potential expansion if audience is catalysis/Damian:** give the 2019 vs 2022/PSSA distinction more voice, keep numerical exact-transport demonstration shorter.

The most compelling *transition between the two code spotlights*:  
> “The first model allowed us to write down the internal states we thought might matter, including a changing catalyst surface. But actually predicting chemistry needs reaction parameters. The second model takes the opposite emphasis: published effective reaction rates, with an intentionally simplified surface. Our scientific question is how much of the richer dynamics we need — and whether we have enough data to justify them.”

This is a **candidate bridging statement, not a verbatim script or established model winner**.

## 2. Three distinct meanings of 'dynamic' must not collapse

1. **Time-dependent inlet \(u(t)\).** A pre-specified sine or spline is an external input. This is not feedback control.
2. **Dynamical gas reactor**: concentrations \(C_b(z,t)\) evolve due to spatial advection and finite residence time. This is true even if reaction terms are PSSA.
3. **Dynamic adsorbate kinetics \(\dot\theta=g(C,\theta)\)**: catalyst site populations carry independent history and feed back into gas reactions. The old scaffold attempts this architecture with **zero default kinetic prefactors**; the new reacting PSSA baseline **does not have that independent θ memory**. Draft PR #3 is a **local, uncalibrated non-PSSA experiment**, not a validated third reactor.

The audience should see the distinction *before* interpreting periodic-response results. A nonzero outlet phase lag alone does **not** demonstrate any dynamic coverage storage. This is a good joint point for mathematics and physical chemistry.

## 3. The numerical example is real mathematics, but not a reactor measurement

At \(N=60\) first-order-upwind axial cells, **pure advection** without reaction/dispersion, forcing period equal to gas residence and **exact time integration** of the MOL system:

\[
|A_{\rm out}/A_{\rm in}|=\bigl(1+(2\pi/N)^2\bigr)^{-N/2}\approx 0.72094,
\qquad
\text{phase lag}=N\arctan(2\pi/N)\approx358.69^\circ
\]
versus exact PDE delay **360°** at unchanged amplitude.

This means **~27.91% upwind-only spatial amplitude damping** in this **carefully specified mathematical example**, and a **~1.31° lead in zero-crossing phase** relative to the ideal delay. The Work branch actually includes the derived figure and its phase zoom. This is *not* experimental data or a measurement of errors in the composite reacting model, and is not correct at arbitrary forcing frequency.

**Numerical nuance the user raised:** *Forward Euler explicit in time at CFL=1* can shift an ideal pure-advection first-order-upwind discrete wave one cell per step without attenuation. That is the **special cancellation** omitted by simplistic statements like “all explicit transport integrators inherently smear signals.” With reaction/diffusion or stiffness-driven \(\Delta t\ll\Delta z/u\), such a cancellation generally vanishes. The currently inspected legacy and Hermes codes use implicit **BDF**, not Forward Euler. Time integrator damping and spatial upwind damping are different contributions. The intended *experiment* is to isolate them, not assert that one solver is best.

This is one of the strongest concrete claims in the deck, but **it could overshadow the chemical question**: present as one reason to be cautious about interpreting later periodic selectivity, then return to the catalyst.

## 4. Presentation *outcome* must be epistemically clean

[Letter K](K_results_validation_status_2026-10-14.md) is an owner-level decision: preliminary reacting numerical outputs exist, but **none is yet sufficiently supported to be defended as a validated physical reactor result**, and no periodic yield gain is demonstrated.

This does not mean nothing has been accomplished:
- The older model's state architecture is built; its limitations and several numerics defects are documented with executed probes.
- Source-backed Urmès-2019 parameters/rate laws have been transcribed/check-audited, with known caveats.
- The newer PSSA reactor runs nonzero chemical reactions under an assumed composite set of conditions, and provides time-dependent inlet *capability*.
- The G pure-advection transfer function is independently derivable mathematics, not a chemistry claim.

**Suggested single sentence for slide 9:** “We have a richer physical scaffold, a source-backed reacting baseline and defensible numerical diagnostics — **but not yet a validated prediction of improved ethylene yield under periodic forcing**.”

**Avoid:** slide-long list of programmer bugs; source-paper conditions described as our actual catalyst; retracted double-\(C_t\) bug; reporting conversion/selectivity values as established measurements; calling 2008→2019→2022 an actual chronological coding plan; claiming the source's reported surface coverage fitted numbers are an independent full-reactor benchmark.

## 5. End on an *experimental design* rather than a future-tech catalogue

A meaningful comparison requires:
1. Agree on a physical, source-appropriate **forward model and observable**, including any necessary non-PSSA kinetic memory.
2. Validate what the calculation actually resolves: source/units, conservation, mesh/time convergence, output amplitude and phase, and physical calibration evidence where possible.
3. Drive the model with *periodic* \(u(t)\) and let it reach a settled cycle (not compare arbitrary terminal snapshots).
4. Compute a well-defined **cycle-averaged *net* ethylene performance**: subtract ethylene already present in inlet; use molar flows if reaction alters total flow.
5. Compare against a **matched-budget same-mean steady case**; a claim that forcing beats *all* steady options additionally needs comparison to the **best admissible steady** operating point under the same constraints.
6. Separately, ask the noiseless-first identification question: can the selected parameters be distinguished in **ideal simulated cyclic data** at all? Only then add noise and consider 8 vs 10,000 repeats. *A failed optimiser alone isn't a theorem of nonidentifiability.*

If slide 10 becomes crowded, **prioritize steps 1–5**; keep 6 as an optional final line, backup or supervisor discussion. Continuous pellet-size distributions, MPC/observers and post-2022 citation sweeps are **optional longer-horizon** only, not part of the immediate next decisive test.

## 6. Open discussion / questions, not silently closed

- **Zoë:** Physical state validity and necessary internal inventories (F); an appropriate coupled bulk/pore flux closure; Forward Euler-upwind test vs actual BDF, stiffness, sparse Jacobian and numerical waveform error (G). [Deck-wide Zoë agenda](../DECK_OPEN_QUESTIONS.md) remains **UNSENT / OPEN**.
- **Damian/owner:** What reaction/catalyst regime and data is the presentation about? What is the **scientific acceptance threshold** for saying the physical reactor prediction is valid? What performance metric/benchmark will count as proof of increased ethylene production? Which non-PSSA surface kinetics is justified?
- **Audience/time:** PR #4 assumes 10 slides/9.5 minutes; no recorded owner-approved slot or rehearsal; target differs for Zoë mathematical discussion vs Damian catalysis audience.
- **Content selection:** I [story 05](../sub-stories/05_reacting_model_inlet_candidate.md) remains **🚩 consider, not selected** even though PR #4 used it as a transition in slide 5. It may be kept, adapted or deleted on review. E stays background; A/H/J were not separately deep-dived; K has no validated performance.
- **Source snapshot:** PR #4 incorporated devcontainer through \`996781c\`, reported QA and generated a usable checkpoint; its own content must be reviewed for any changes committed later to research files. **Do not write to or merge the Work branch from M.**

## 7. Recommended action after discussion

Review the ten-slide deck and bullet outline **as a proposed story**, not a final script. For each slide mark **KEEP / SHORTEN / MOVE TO BACKUP / REMOVE**. Then let the Work PR author update the **same** editable outline, \`presentation_content.json\`, HTML, DOCX, PDF, speaker cues, claim ledger, and QA together. Do not create a second rival slide project and don't copy unverified equations/outputs from research files.

**Current editorial recommendation:** retain opening research question; use one understandable bulk→pore→surface/state-space visual; give both old and new modeling approaches honest representation; explain the numerical wave-fidelity issue clearly; state the validity boundary; conclude with one falsifiable next periodic experiment. *Everything else competes for time.*
