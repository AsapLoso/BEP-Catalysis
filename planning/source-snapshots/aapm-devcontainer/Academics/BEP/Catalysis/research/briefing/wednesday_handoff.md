# Wednesday presentation handoff — 14 October 2026

**Status:** a handoff, not a deck. Audience, duration, format and ready-to-present criteria
are still the owner's open decisions (presentation map tickets W1, W2, W7).

**Companion material:** [supervisor briefing](BEP_SUPERVISOR_BRIEFING_2026-10-13.md) ·
[spoken update](spoken_update.md) · [technical Q&A](technical_qa.md)

---

## 1. The priority narrative

The story has one spine and three beats. It is deliberately **not** "here is my simulator".

> **Spine:** the steady-state yield cap is a property of the *steady state*, not of the
> chemistry — so a time-varying inlet may beat it. Building the model to test that is real,
> careful work; the physics is not switched on yet, and here is exactly what that means.

| Beat | Content | Why it earns its place |
|---|---|---|
| **1. The question** | Sequential network $\mathrm{C_2H_2 \to C_2H_4 \to C_2H_6}$; steady state locks coverages; transient waves could desorb ethylene before it is consumed | Gives the audience the *why* before any code. Without it, the model looks arbitrary |
| **2. The structure** | Three coupled levels → 1,480 state variables → stiff → BDF. Plus the three discretisation choices with their trigger conditions | This is the legitimate intellectual content: modelling choices, justified |
| **3. The honesty** | Six defects found by independent audit, all reproducing live. Kinetics still zero, forcing not implemented, no yield result | **This is the credibility move.** It is also what a supervisor actually wants to see |

**Beat 3 is not an apology.** An independently audited model with six documented, reproducible
defects is a *stronger* position than a model that has never been attacked. Say it that way.

### The one positive scientific result to land

If the audience takes away one number, it should be this: **the transferred kinetic
parameters match the primary source, and the rate law reproduces the paper's own published
surface coverages at 11 of 12 checks.** It is the one claim that
survives attack, and it is genuinely new this week.

---

## 2. Source-backed material, slide by slide

Each row is safe to put on a slide *with the stated framing*.

| # | Slide content | Source | Framing required |
|---|---|---|---|
| 1 | The sequential network and the yield-cap argument | proposal `main.tex:111-119` | As the *motivation*; the mechanism is a hypothesis |
| 2 | Berger's pseudo-homogeneous balance + MOL + implicit BDF as established practice | Berger 2008, Fig. 5 | As *reused framework*, not our invention |
| 3 | The three-level model → 1,480 entries (80 / 800 / 600) | `c2h2_..._model.py:58-66` | Add: 1,480 is the *allocated* count, not the active count (D1, D3) |
| 4 | The three discretisation choices + trigger condition | `conventions.md:177`, audit D7 | As justified modelling choices |
| 5 | The defect register table, D1–D6 | `audit_2026_09_30.py` output | As **verification work**, explicitly not reactor results |
| 6 | D2 live: exact 6.0000 vs code 3.0000 on $f=r^2$ | same probe | As a *numerical* demonstration |
| 7 | The parameter-transfer table (8/8 constants vs Table 5) | `verify_urmes2019_source.py` | As a **parameter-transfer check** |
| 8 | Coverage reproduction table (11/12 in range; miss on θ_H2 at op 1) | `verify_pbr_implementation.py` GATE 1 | As one rate law matching one paper at four steady points, **with the miss shown** |
| 9 | The honest status box: kinetics off, forcing absent, no yield result | this handoff §4 | **Mandatory.** Do not cut it for time |
| 10 | Next milestones + the questions for Damian | briefing §8 | As the plan, not as completed work |

### A note on slide 5

The strongest available live demonstration is running the defect probe **in front of the
audience**. The numbers appear on screen instead of on a slide. This is the single highest-
impact moment available and it costs about five minutes:

```bash
pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py
```

**Caveat:** it takes roughly 2–4 minutes wall-clock because of the D6 Jacobian. Either run
it before the talk and show the recorded output, or budget the time honestly. **Do not
promise a live run you have not timed.**

---

## 3. What can appear, and what must not

### ✅ Can appear (with the framing above)

- The yield-cap argument and the physical mechanism as a **hypothesis**.
- Berger's framework as **reused established methodology**.
- 1,480 state variables as **grid arithmetic**.
- The three discretisation choices and their **trigger conditions**.
- All six defects, as **reproducible verification findings**.
- The parameter-transfer verification and coverage reproduction, labelled as such.
- The `pbr` test suite result: 37 passed.

### ❌ Must NOT appear

| Must not | Why |
|---|---|
| Reactor yield or selectivity curves | No reacting run has been performed |
| A measured periodic yield improvement | Periodic forcing is not implemented |
| "Validated simulator" | Not validated; four independent blockers (§briefing 6.2) |
| The 40-fold thermal-pulsing enhancement as our result | It is someone else's system, cited in the proposal as background |
| "Microsecond responses" as established | An inherited proposal claim, not our measurement |
| "Readsorption is absent" | It is present in the code |
| A "double `C_t`" bug | **Retracted.** Raising it would be a live error |
| "The model is 16 % wrong" | 16 % is a constant-rate quadrature bias on this grid, not a trajectory error |
| `pbr` as "the working model" | Its surface does not feed back into gas rates |
| Monday's 12-minute no-slides route as Wednesday's format | Unratified; a different map's historical decision |

### Suggested on-slide disclaimer

Put this where it can be read, not in small print:

> Model architecture and verification work. Kinetic parameters are being sourced; periodic
> forcing is not yet implemented. Numbers shown are reproducible diagnostics, not reactor
> predictions.

---

## 4. The honest status box

If the talk needs exactly one slide about where the project stands, this is it:

| Component | Status |
|---|---|
| Mathematical structure (balances, discretisation, state vector, solver) | **Built** |
| Independent audit of that structure | **Done** — six defects, all reproducing |
| A newer modular implementation (`pbr`) | **Exists**; six old defects structurally addressed; **three new ones reproduced** (surface feedback absent, feed path, sparsity) |
| Kinetic parameters | **Verified against the primary source** for the Urmès2019 set (8/8) |
| Rate law behaviour | **Reproduces the source's published coverages at 11 of 12 checks** (miss on θ_H2 at op 1) |
| Surface feedback into gas rates in `pbr` | **Absent** — it is a PSSA model with optional decoration |
| Periodic inlet forcing | **Not implemented** |
| Yield / selectivity metric | **Not implemented** |
| Validated reacting periodic simulation | **Not achieved** |

**Read it aloud as written.** The pattern — structure done, audit done, chemistry verified,
capability not yet built — is a coherent story, and it is true.

---

## 5. Figures and equations available now

`[FACT]` There are **no figures in the project**. A recursive sweep for
`.png/.svg/.jpg/.jpeg/.gif` under `Academics/BEP/Catalysis` returns empty, and the model
imports only `numpy` and `scipy.integrate`. So a visual narrative requires *generating*
figures, which requires runnable chemistry, which requires filling the zero kinetics.

**Practical consequence:** any figure in the talk must be either (a) schematic/diagrammatic,
or (b) generated from the *diagnostic* probes rather than from a reactor run.

Available as real, reproducible content:

| Artefact | How to produce it |
|---|---|
| The 6 vs 3 centre-coefficient check | output of `audit_2026_09_30.py` §D2 |
| The quadrature normalisation ratio (0.840) | output of §D4 |
| The 80-of-1480 mutation count | output of §D1 |
| The parameter-transfer table | output of `verify_urmes2019_source.py` |
| The coverage table | output of `verify_pbr_implementation.py` |
| The architecture diagram (balances → discretisation → state → solver) | schematic; draw it, don't compute it |

### Equations that are safe to show

- The bulk balance with Danckwerts BCs — **as the proposal's general form**
  (`main.tex:183`).
- The surface balance $\partial\theta_i/\partial t = r_{ads,i} - r_{des,i} - \sum r_{rxn,i}$
  (`main.tex:193`) — **with the non-PSSA rejection stated**.
- The LHHW rate equations and the site balance — **verified verbatim against Urmès 2019**.
- The spherical centre limit $(1+s)f''(0)$ — and the discrete coefficient $2(1+s)$.

---

## 6. Existing material to reuse

| Asset | Path | Status |
|---|---|---|
| Five-slide HTML mini-deck (state-space segment) | `presentation/BEP_transient_state_mini_deck.html` | Insertable segment, **not** the complete Wednesday deck |
| Speaker notes for that segment | `presentation/BEP_transient_state_speaker_notes.md` | Aligned with this handoff's honest-status stance |
| Sub-story 01: three concentrations → state space | `presentation/sub-stories/01_three_concentrations_to_state_space.md` | Raw draft; not a settled sequence |
| Sub-story 02: proposal → predictive optimisation | `presentation/sub-stories/02_proposal_to_predictive_optimization.md` | Second draft; not approved |
| HTML slide-deck build-and-grade runbook | `.agents/resources/runbooks/html-slide-deck-build-and-grade.md` | The procedure if a deck gets built |

**A note on the mini-deck:** its speaker notes already carry the right stance ("we're
explaining its model architecture, not claiming that its predictions are correct"). It is
consistent with this handoff. If the deck is extended, extend it in that voice.

---

## 7. Open presentation decisions (not ours to make)

These are the presentation map's own tickets and they stay open:

- **W1 — Audience and purpose.** Who is in the room, and the one thing they should leave
  understanding.
- **W2 — Duration and delivery format.** How long, and whether the interactive HTML deck is
  the required format.
- **W4 — Content priority.** Which of the ten slide candidates above survive a time cut.
- **W5 — Narrative order.** The three-beat spine above is a *proposal*, not a ratified
  storyboard.
- **W6 — Visual approach.** Whether notebook-derived visuals or interactivity help.
- **W7 — Ready-to-present standard.** Including whether a speaking script is required.

`[UNRESOLVED]` None of these is answerable from the repository. This handoff supplies the
*evidence*; the owner supplies the *story*.

---

## 8. Next three concrete actions

1. **Acquire Urmès et al. (2022), DOI 10.1002/cctc.202101826.** The direct periodic-operation
   comparator is absent from the library, and it is the single most relevant paper to the
   thesis's central claim.
2. **Decide the two HITL questions** — which implementation to take forward, and whether the
   radial pellet dimension stays in scope. Both change what the next month of work is.
3. **Wire the surface feedback in `pbr`** (`rate.rates` must accept and use `theta`), then
   implement periodic forcing and a cycle-averaged yield metric. That sequence is what turns
   the project from "structure" into "experiment".
