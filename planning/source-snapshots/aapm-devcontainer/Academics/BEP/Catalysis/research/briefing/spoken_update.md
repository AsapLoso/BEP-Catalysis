# Spoken research update — 60–90 seconds

**For:** Lucas, to deliver. **Target:** ~75 seconds at a normal speaking pace (~130 wpm).
**Where it fits:** opening the meeting with Damian, or opening the Wednesday talk.

> Practice it once against a timer. The two bracketed lines are the ones to slow down on.

---

## The script

> The project asks whether we can beat the steady-state yield cap in acetylene
> semi-hydrogenation by **modulating the inlet** instead of running at a fixed operating
> point. The argument is that the cap is a property of the steady state, not of the
> chemistry: if you drive transient concentration waves through the bed, ethylene can
> desorb into the gas phase before the second hydrogenation step eats it.
>
> **[SLOW DOWN]** So far I have built the mathematical structure, not the physics. The
> model discretises the packed bed axially, the pellet radially, and the catalyst surface
> into **1,480 coupled state variables**, and integrates them with an implicit BDF solver
> because the surface kinetics are stiff.
>
> I audited that model independently and found **six defects, three of them blocking** —
> and every one reproduces live on this machine. The most serious: the right-hand side
> silently writes into the solver's own state vector, so the trajectory the solver stores
> isn't the trajectory the equations describe.
>
> **[SLOW DOWN]** Two things I want to flag honestly. First, **the chemistry is not
> switched on** — all eight kinetic constants are still zero, and the periodic forcing
> isn't implemented at all. So there is no yield result yet, and I'm not going to show you
> a curve that doesn't exist.
>
> Second, the useful progress: there's a newer implementation in my thesis repository, and
> this week I verified that its **kinetic parameters match the published source paper
> exactly** — all eight constants. Then I went further and checked whether the rate law
> **reproduces the paper's own published surface coverages**, and it gets **eleven of twelve
> checks** — with hydrogen coverage at the highest-acetylene feed landing just below the
> published range.
>
> That's a real check on the transferred chemistry, and I'm reporting the one miss rather
> than rounding it to a pass.
>
> What I'd like to settle with you is which implementation to take forward, and what
> "validated" has to mean for this model before I can call it one.

---

## Delivery notes

| Beat | Purpose | Trap to avoid |
|---|---|---|
| ¶1 — the question | Gives Damian the *why* before any code | Don't start with the architecture; he'll ask why it exists |
| ¶2 — the structure | 1,480 + stiff + BDF in one breath | Don't explain MOL/uniform grids here; that's the Q&A |
| ¶3 — the defects | The credibility move: audited, not built-and-hoped | Don't read out all six; D1 is the one that lands |
| ¶4 — the honest wall | Chemistry off, forcing absent, no yield result | **This is the paragraph that earns trust.** Do not soften it |
| ¶5 — the real progress | Parameters verified + coverages reproduced 11/12 | Say "the paper's published coverages", not "validated the model" — and **volunteer the one miss** |
| ¶6 — the ask | Hands the meeting a decision | Ask one question, not five. Which implementation? |

## If interrupted

- **"So it doesn't work?"** → "The structure works and is audited. The chemistry isn't
  switched on yet, because the kinetic constants have to come from a source rather than
  from me guessing. That's the next step, not a failure."
- **"Why 1,480?"** → "20 axial cells × 4 gas species, plus 20×10 radial cells × 4 species,
  plus 20×10×3 coverages. It's grid arithmetic — 80 plus 800 plus 600."
- **"Why BDF?"** → "The surface kinetics are orders of magnitude faster than the transport.
  Explicit steps would be set by the fast modes while the physics I care about evolves on
  the slow ones. That's stiffness, and BDF is the standard implicit answer."

## What not to say

- Do **not** call it a validated simulator, or imply the newer package is finished.
- Do **not** mention a double-`C_t` bug — that claim was retracted.
- Do **not** quote the 40-fold thermal-pulsing figure as our result; it's someone else's
  system and it's cited in the proposal as background.
- Do **not** quote a wall-clock seconds figure for the Jacobian. Say "the dense
  finite-difference Jacobian dominates the cost" and let the number be structural.
