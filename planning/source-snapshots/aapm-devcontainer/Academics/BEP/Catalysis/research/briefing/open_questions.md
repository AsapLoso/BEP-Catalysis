# Open Questions — Grilling Tickets Unblocked by Tonight's Findings

**Companion to** [`afk_findings.md`](afk_findings.md) and [`veto_crosswalk.md`](veto_crosswalk.md).
**Session:** CEO, autonomous overnight workstream, 2026-10-08.

**These are not closed.** Per `.agents/skills/wayfinder/SKILL.md:96` the agent does not answer its own grilling
questions, and per the session's scope no `wayfinder:grilling` ticket was answered. What follows is each question,
verbatim from the map, plus **the specific finding that makes it answerable now** — that is, the missing input that
did not exist on 2026-10-07 and does exist as of this session.

| Ticket | Map line | Type | Was it unblocked? | By which finding |
|---|---|---|---|---|
| **RS-4** | `damian_briefing_2026_10_09.md:107-110` | `grilling` | **Yes, fully** | RS-1, RS-2, RS-3 |
| **SP-1** | `:51-54` | `grilling` | **Partly** — one of three triggers now has a candidate, unsourced | RS-1 |
| **DR-1** | `:69-72` | `grilling`, inherited as master `I1-07` | **No — blocked on a human judgement** | SP-3 |
| **DR-4** | `:84-87` | `grilling` | **Yes** | SP-3 |
| **AR-2** | `:120-123` | `grilling` | **Partly** | SP-3, AR-3 |

---

## RS-4 — The one research finding that survives every veto · FULLY UNBLOCKED

**Question, verbatim (`damian_briefing_2026_10_09.md:108`):**

> if exactly one thing from the literature and extraction work may be said to Damian tomorrow without qualification,
> which is it — and what is the sentence?

The map records this ticket as depending on RS-1, RS-2 and RS-3 (`damian_briefing_2026_10_09.md:109`). All three are
now closed, so the input is complete. **The choice itself is still the human's** — "which one" is a judgement about
what matters, and that is a grilling question by construction.

**What the three tickets produced that makes it answerable:**

1. **The candidates that survive every veto.** RS-2 established that all 23 grounded KG edges are clean against all
   seven vetoes. Three stand out, because each is a *sentence from a source* rather than a number from our own files:
   - Berger's transport-criteria premise (`berger2008:sec:5:para:1`): *"In order to ascertain that the obtained data
     represents the intrinsic kinetic information, it should be free from deviations due to nonideal reactor
     behavior and interference by transport phenomena."*
   - Berger's plug-flow statement (`berger2008:sec:4:para:1`): *"For the plug-flow reactor a set of coupled partial
     differential equations (PDEs) is obtained."*
   - Larsen's own reactor statement (`larsen2024:sec:4-3:para:1`): *"The packed bed reactor is the reactor used
     throughout the regular experiments."*

2. **The best numerical candidate, and its exact boundary.** The RMSE triple **5.10 / 5.43 / 7.14 %** is the only
   surviving *number*. `conventions.md:191` states these "bestaan en zijn correct" at `Ch6:678`, `Ch7:35`,
   `Ch1:21`; `literature_index.md:262-265` records them at Larsen's Section 6.2.4, p. 43. But `conventions.md:220-221`
   records the same fragments cross-contaminated into Wang / Zhang / Ball / Borodzinski extraction files, so the
   sentence is speakable **only** attributed to Larsen and never sourced from the pipeline files. That boundary is
   now written down; it was not before.

3. **The one thing that must not be chosen.** V1 and V2 block the six Larsen values in both directions — not as a
   source, and not as "gefabriceerd" (`state.md:34-35`). RS-3 additionally showed those values live in **Appendix E,
   pages 71–76**, not Appendix F as V2 assumes, so no amount of citing will clear them tonight.

**The decision, restated as a single question for the human:** *which of the three grounded sentences above, or the
bounded RMSE figure, is the one you want to be able to say without qualification?*

---

## SP-1 — The three discretisation choices and their trigger values · PARTLY UNBLOCKED

**Question, verbatim (`damian_briefing_2026_10_09.md:52`):**

> …the transcript confirms upwind/backward for bulk advection, central difference for intra-particle diffusion, and
> implicit BDF for stiffness. For each, what is the specific quantity that makes the alternative wrong — Peclet
> number for the first, radial mesh ratio for the second, rate-constant stiffness ratio for the third — so Damian
> cannot ask "why that scheme?" and get a shrug?

The map notes the blocker: `3_Model/state.md:53-55` gives the three choices and their reasons but **not the numeric
trigger values**, "and those must come from the reference, not from memory (Rule 16)" (`:54`).

**What changed.** RS-1 turned up a Peclet trigger that did not appear in the map's evidence list:

- `silvestonPeriodicOperationCatalyticReactors1995_taxonomy.md:27` — the pseudo-homogeneous plug-flow reduction is
  defensible *"at high Peclet numbers ($Pe \gg 100$) and high superficial velocities where film and axial resistance
  are negligible compared to surface reaction rates."*
- Repeated at `:28` and `:48`, where `:48` adds the condition *"provided $Pe \gg 100$ and external mass transfer
  limitations are experimentally or numerically bounded."*

So one of the three trigger values now has a candidate: **$Pe \gg 100$** for the bulk/film reduction. It matches the
wording already in `3_Model/state.md:67` ("it is exactly the $Pe \gg 100$ case").

**Why it is still only partly unblocked.** The candidate's provenance is a *taxonomy report*, not the consensus file
and not the PDF. RS-1 found that `silvestonPeriodicOperationCatalyticReactors1995_taxonomy.md` carries **zero
line-level citations** — the only one of the four taxonomy reports that does. So under `conventions.md:159-160` and
Rule 16, `$Pe \gg 100$` is currently `UNVERIFIED` at source. The radial mesh ratio and the stiffness ratio remain
with no candidate at all.

**The question that remains, now narrower:** *is $Pe \gg 100$ the trigger you want to state for the bulk scheme — and
if so, may it be cited from Silveston at page level, or does it need the consensus file read first?*

---

## DR-1 — The fix / choice / convention trichotomy · NOT UNBLOCKED, AND NOT MINE TO CLOSE

**Question, verbatim (`damian_briefing_2026_10_09.md:70`):**

> which register entries must be *fixed* before any number produced by this model may appear, which may be reported as
> stated limitations instead, and on what basis is that line drawn?

**Still blocked, for a reason this session confirmed rather than resolved.** The map is explicit that this ticket is
inherited as master `I1-07` and *"The agent does not close this ticket"* (`damian_briefing_2026_10_09.md:71`) — it is
a judgement about what may be reported to an examiner.

SP-3 sharpened the input without answering it. Concretely, the sweep produced three facts that bear directly on where
the line falls, and the human now has them all in one place:

- **§3.7 and §3.1 are two audit findings that never reached the code** (zero `Bim` hits; the script uses Berger's
  `−(u_s/ε_b)` at `c2h2_hydrogenation_transient_model.py:206-208` and `(1−ε_b)` at `:203`, matching the audit's
  "correct" pseudocode). These are neither fixes nor choices — they are findings already banked.
- **§3.3 and §3.6 are confirmed present in the script and unregistered as register items** (`3_Model/state.md:44-45`).
  Readsorption absent: zero `readsorp`/`TPD` hits. Energy balance absent: zero `Prater`/`exotherm`/`dT_dt` hits.
  `transient_model_framework_audit.md:104` already calls §3.6 a *"Scope decision, not a coding bug"* — which is
  **textbook DR-1 material**: a scope choice that must be stated, not a fix.
- **D1–D4 all now carry file-and-line proof** rather than probe output alone, because SP-3 read the script directly:
  D1 at `:135` + `:158`, D2 at `:179`, D3 at the `:164` loop bound, D4 at `:195` + `:199`.

**The decision, unchanged and the human's:** *on what basis is the fix/choice line drawn — per-entry judgement, or a
single stated criterion applied to all eight register rows?*

---

## DR-4 — Damian's hardest question about the register · UNBLOCKED

**Question, verbatim (`damian_briefing_2026_10_09.md:85`):**

> the register proves the model is wrong in three blocking ways — so what does Damian ask next, and what is the
> honest answer? Specifically: if three defects are blocking, why does the model still produce plausible-looking
> trajectories, and what does that say about how such numbers should be used?

The map records the gap: *"Nothing in the register addresses what a wrong-but-running model implies for
interpretation"* (`damian_briefing_2026_10_09.md:87`).

**What changed.** SP-3 closed the "are there more defects hiding?" half of the question, and the answer is the good
one: **the framework audit's nine model defects are now fully adjudicated, and there is no seventh blocking defect.**
Four are confirmed present and already accounted for, two never reached the code, and the remainder are FW-bullet
items. The sweep table is in `afk_findings.md` § SP-3.

So the honest answer to Damian now has a factual spine it did not have before:

- D1 is a **trajectory** error, not a crash — the solver returns a clean result that is not the solution of the stated
  equations, `max|Δ| = 5.1` at `t = 0.2 s` (`3_Model/state.md:60`). Plausible-looking is exactly what a
  non-mutating-violation produces.
- D3 deletes the surface kinetics **at the pellet shell** (`:164` excludes `N_r-1` from the θ loop), so the model runs
  with the reaction switched off precisely where the gas touches the catalyst.
- And because all eight kinetic constants ship as `(0.0, 0.0)` (`c2h2_hydrogenation_transient_model.py:34-43`), the
  model currently integrates **pure transport** — which is the honest answer to "why does it produce plausible
  trajectories": because the chemistry is currently inert and `y0` is all zeros (`:225`), so there is very little for
  the defects to distort yet.

**The question that remains, and it is the human's:** *given that, what do you say about how numbers from this model
should be used until the kinetics are filled and D1–D3 are fixed?* SP-1/DR-3 give the material; the position is a
judgement.

---

## AR-2 — Script or conversation · PARTLY UNBLOCKED

**Question, verbatim (`damian_briefing_2026_10_09.md:121`):**

> does Lucas walk in with a 12-minute script he can deliver, or with the register in hand and an argument he can
> defend? The two are different preparation and only one survives an unexpected question.

The map notes the evidence pulls both ways: `3_Model/state.md:59` describes a *route* with timings, not a script,
while the destination's criterion 2 requires answering without looking anything up, "which argues for the latter"
(`damian_briefing_2026_10_09.md:123`).

**What changed.**

- **AR-3 settles the register, which the two options differ on.** `conventions.md:92` fixes English, natural,
  low-key for Damian-facing content; `:86-88` requires structure rather than dense prose; `:93` limits bullets to
  summations and specific cases. So the one-page artefact is a **table plus a margin note per number** — which is
  the "register in hand" option, prepared in a defined register, and not a script.
- **DR-3 supplies the six sentences that only a conversation needs.** Four overlap sentences plus the two-part D2
  sentence, drafted and ready, are in `afk_findings.md` § DR-3. These are exactly the material that survives an
  unexpected question and that no 12-minute script would contain.

**The question that remains:** *which do you rehearse — the six sentences, or the route?* AR-3 also leaves open
whether anything is written down after the conversation at all, which depends on this same answer.

---

## Not unblocked, and reported for completeness

| Ticket | Map line | Why it is still open |
|---|---|---|
| **SP-2** | `damian_briefing_2026_10_09.md:56-59` | The single-sentence capability claim needs no new evidence and none was produced. Its inputs are `3_Model/state.md:16`, `:64` and register row `:85` — all confirmed by SP-3, but the sentence is the human's. |
| **DR-2** | `:74-77` | `wayfinder:prototype`, not AFK. Depends on DR-1, which is not unblocked. |
| **AR-1** | `:115-118` | `wayfinder:prototype`, not AFK. Medium of the one-pager; depends on DR-2. |
| **DR-1 / master `I1-07`** | `:69-72` | Inherited and explicitly not answerable by the agent (`SKILL.md:96`). See above. |