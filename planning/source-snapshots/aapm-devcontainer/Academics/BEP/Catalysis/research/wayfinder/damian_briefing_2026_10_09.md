# Wayfinder: BEP Catalysis — Damian Briefing Map

**Author:** agent, 2026-10-08 · **Scope:** map authoring only; touches no state-engine file beyond the link in `state.md`.
**Relationship to the master map:** *sibling, not parent, not child.* [`bep_catalysis_master.md`](bep_catalysis_master.md) answers "what must be decided before a defended thesis can exist". This map answers "what must be true so that one specific person understands what we have built and learned, tomorrow morning". They are separate destinations under Wayfinder's One Map Per Goal rule (`SKILL.md:30`) because they have **different verifiable end states, different audiences, and different clocks** — the master's clock is the examination, this one's clock is the next morning. Neither map is edited by the existence of the other. Four master tickets are reused by reference in §2 below; the rest are not.

---

## 1. Destination

**Tomorrow morning, Lucas stands in front of Damian and explains what the BEP code is, what it does, what it has been shown to do, and what has been learned — including what is still wrong with it — and Damian is convinced that Lucas knows his own project rather than having received a script from a language model.**

This is one destination with one verifiable end state. It is not "understand the model" and not "finish the thesis"; it is *the supervisor leaves the conversation able to answer 'what did you actually establish?' in his own words, and Lucas answers without needing a slide to hide behind.*

**Completion criterion.** The briefing is done when all four of these hold simultaneously:

1. **Every number spoken aloud is re-derivable on demand.** Each figure has a command that regenerates it in front of Damian, not a citation to a document.
2. **The three blocking defects are presented as the strength, not the embarrassment.** Lucas can state which of D1–D6 are fixes with a determined correct answer, which is a convention question, and which is a stated modelling choice — without looking it up.
3. **The modelling choices are stated as choices.** Plug flow + pseudo-homogeneous reduction, all-zero kinetics, and the isothermal assumption are on the table as deliberate reductions with their trigger conditions, not as omissions.
4. **No vetoed claim is spoken.** Every one of the seven vetoes in `state.md:33-39` is checked against the script before the meeting.

**What "presented" excludes.** It does not require the model to be correct. It requires the defects to be *correctly characterised and honestly bounded*. A briefing that hides D1–D3 fails this destination even if Damian is impressed.

**Runbooks:**
- `.agents/resources/runbooks/html-slide-deck-build-and-grade.md` — governs any slide artefact (Island 4).
- `.agents/resources/runbooks/verifying-extraction-claims-against-pdf-text-layer.md` — governs every claim sourced from `Articles/2 meeting Damian + Zoë/extracted/` (Island 3).
- `.agents/resources/runbooks/preflight-verification-before-automated-runs.md` — governs the live-probe step (Island 2).
- `.agents/resources/runbooks/partial-grep-and-inference-discipline.md` — governs absence claims in the briefing script.
- `.agents/resources/runbooks/marathon-briefing-workflow.md` — governs multi-phase consolidation if the brief is graded by an auditor.
- **Gap recorded:** no runbook exists for *"how to present a numerical defect register to a supervisor as a positive result."* Per `SKILL.md:108` this gap is itself a finding. See §5.

---

## 2. Decisions So Far

- [x] **The existing master map does not cover this.** It is scoped to a defended thesis (`:14`) and states at `:279` that it decides what the model must be true of but does not write it. **Destination:** separate map, master untouched. 2026-10-08.
- [x] **Four master tickets are reusable by reference, not by duplication.** `I1-01` (Appendix E parameter admissibility), `I1-07` (the correctness gate — *which* register entries must close before any number may appear), `I2-01` (canonical source of truth), `I2-02` (disposition of unpublished commit `e0663ba`). Only **I1-07** is briefing-critical, and it is quoted verbatim into Island 2 as the grading criterion rather than answered here. **The agent never answers its own grilling questions** (`SKILL.md:96`), so I1-07 stays open and is inherited, not resolved. 2026-10-08.
- [x] **The defect register is reproducible today, on this machine.** `pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py` ran end-to-end on 2026-10-08 and regenerated all six blocks: D1 `max|Δ| = 5.148`, D2 `exact 6 / code 3`, D3 `all-zero = True`, D4 `16.0%` bias, D5 docstring wrong and *both* `C_t` factors correct, D6 rhs `0.0114 s` vs Jacobian `16.9 s`. **This is the strongest asset in the project** — the numbers are produced live, in front of Damian. 2026-10-08.
- [x] **D6's *structure*, not its seconds, is the claim — and today's run confirms why the number moved.** Today's probe reports rhs `0.0114 s` against the register's `0.016 s` (`3_Model/state.md:66`) and a Jacobian of `16.9 s` against `23 s`. This is **not** a contradiction: `3_Model/state.md:88-91` already states wall-clock figures are load-dependent and that the durable claim is the structure. The probe itself prints the structural finding — the 30-09 `~2.2 s per rhs` figure was `wall/nfev`, which folded in the Jacobian work. **Decision: the briefing speaks the structure, never a seconds figure.** 2026-10-08.
- [x] **D5 is a documentation defect, not a double-normalisation.** Today's probe confirms `R_gas` carries `1/s` (per site), that the `[mol/kg_cat/s]` docstring is wrong, and that both `C_t` factors in the code are therefore correct. This independently re-confirms the retraction already recorded at `3_Model/state.md:65`. **The briefing must not claim a `C_t` double-count** — that claim was withdrawn and re-introducing it in front of Damian would be a live error. 2026-10-08.
- [x] **Zero figures exist in the entire project.** A recursive extension sweep for `.png/.svg/.jpg/.jpeg/.gif` under `Academics/BEP/Catalysis` returns empty; `c2h2_hydrogenation_transient_model.py` imports only `numpy` and `scipy.integrate`. A visual narrative therefore requires *generating* figures, and generating figures requires *runnable chemistry*, which requires filling `ModelParams.kinetics` — all eight of which ship as `(0.0, 0.0)` (`3_Model/c2h2_hydrogenation_transient_model.py:34-43`). **Decision: the live defect audit, not a plot, is the centrepiece.** This is a finding about the destination, not a scheduling note. 2026-10-08.
- [x] **A 12-minute walkthrough route already exists and is adopted as the spine.** `3_Model/state.md:59` specifies: (1) the register table and the two-audits block, 2 min; (2) the model and its three discretisation choices, 3 min; (3) the audit probe **run live**, 5 min; (4) the four genuine overlap points between the framework audit and the register, 2 min. **Not shown:** the performance log and the D6 Jacobian costs — those belong to a parameter study, not an introduction. 2026-10-08.
- [x] **The two audits are not one audit, and the correction is itself demonstrable.** `3_Model/state.md:28-45` records that an earlier version of this file wrongly claimed the two audits overlap on one point and that their point 6 is "the same defect" as D2. They touch the same code line but carry two different diagnoses. **Decision: the briefing presents the distinction as a finding** — it demonstrates that the two audits were cross-checked rather than conflated. 2026-10-08.

---

## 3. Active Frontier

### Island: The Evidence Spine
*What the model is, and why it is built this way. Low fog — most of this is settled and needs only accurate restatement.*

- [ ] **SP-1 — Which three discretisation choices get stated, and against which trigger condition each is justified?** (`wayfinder:grilling`)
  *Question: the transcript confirms upwind/backward for bulk advection, central difference for intra-particle diffusion, and implicit BDF for stiffness. For each, what is the specific quantity that makes the alternative wrong — Peclet number for the first, radial mesh ratio for the second, rate-constant stiffness ratio for the third — so Damian cannot ask "why that scheme?" and get a shrug?*
  - Status: Open. Dependencies: None.
  - Evidence: `3_Model/state.md:53-55` states the three choices and their reasons; it does **not** state the numeric trigger values, and those must come from the reference, not from memory (Rule 16).

- [ ] **SP-2 — The model's honest current capability, stated in one sentence.** (`wayfinder:grilling`)
  *Question: what is the single sentence Lucas says about what the model can currently do — given that it integrates pure transport, every kinetic constant is `0.0`, and `E_a` is parsed but ignored so temperature is inert?*
  - Status: Open. Dependencies: None.
  - Evidence: `3_Model/state.md:16` (`🟡 SCAFFOLD ONLY`), `:64` (all eight kinetics zero; state stays identically zero), register row 8 (`E_a` parsed but unused, temperature inert).

- [ ] **SP-3 — `3_Model/transient_model_framework_audit.md` claim-status sweep.** (`wayfinder:research`)
  *Question: of the 8 model defects the framework audit raises against Berger (2008), which are now confirmed present in the script, which are already covered by the register under a different ID, and which remain UNVERIFIED?*
  - Status: Open. Dependencies: None.
  - Evidence: `3_Model/state.md:40-45` gives a partial overlap table covering four points and explicitly notes §3.3 (readsorption absent) and §3.6 (no energy balance) are "confirmed present, not yet registered". The remaining audit findings have not been reconciled against the register.

### Island: The Defect Register as Narrative
*Turning six defects into the strongest part of the talk instead of the weakest.*

- [ ] **DR-1 — The fix / choice / convention trichotomy, stated precisely.** (`wayfinder:grilling`) — **INHERITED AS MASTER `I1-07`**
  *Question: which register entries must be *fixed* before any number produced by this model may appear, which may be reported as stated limitations instead, and on what basis is that line drawn?*
  - Status: Open. Dependencies: None. **This ticket is inherited, not answered here.** The master states at `bep_catalysis_master.md:110-115` that D1–D4 each have a *determined* correct answer and are fixes rather than decisions, that D5 is a convention question, and that the film/dispersion trade-off is a choice that belongs in the text. **The agent does not close this ticket** (`SKILL.md:96`) — it is a judgement about what may be reported to an examiner, and that is the supervisor's and Lucas's call.
  - Evidence: register table `3_Model/state.md:77-86`; master `bep_catalysis_master.md:110-115`.

- [ ] **DR-2 — The one-page register sheet with per-number traceability.** (`wayfinder:prototype`)
  *Question: what exactly is on the single page Lucas holds during the walkthrough — which columns of the register, which of the six evidence figures, and what margin annotation answers "where does this number come from" without a second document?*
  - Status: Open. Dependencies: DR-1, because the fix/choice split determines what the sheet emphasises.
  - Evidence: `3_Model/state.md:88` states every register number is re-derivable via the probe; the walkthrough prep instruction at `:59` requires "one page with the register table plus the traceability of each number".

- [ ] **DR-3 — The four overlap points, compressed to one sentence each.** (`wayfinder:task`)
  *Question: for each of the four documented overlaps between the framework audit and the register, what is the one sentence that shows the distinction was seen — and in particular, how is the corrected D2 story (same line, two different diagnoses) put in one sentence?*
  - Status: Open. Dependencies: SP-3.
  - Evidence: `3_Model/state.md:39-45` table plus the correction paragraph at `:28-37`.

- [ ] **DR-4 — Anticipating Damian's hardest question about the register.** (`wayfinder:grilling`)
  *Question: the register proves the model is wrong in three blocking ways — so what does Damian ask next, and what is the honest answer? Specifically: if three defects are blocking, why does the model still produce plausible-looking trajectories, and what does that say about how such numbers should be used?*
  - Status: Open. Dependencies: DR-1.
  - Evidence: D1's `max|Δ| = 5.1` is a trajectory error, not a crash — the model runs, it is wrong. Nothing in the register addresses what a wrong-but-running model implies for interpretation.

### Island: The Research Layer
*What was learned from the literature and extraction work — the half that no existing document assembles.*

- [ ] **RS-1 — Was the finding-taxonomy extraction run ever completed?** (`wayfinder:research`) — **SUSPECTED INTERRUPTED PROCESS**
  *Question: `finding_taxonomy.md` describes the extraction procedure in future tense and lists "known starting members", while four `*_taxonomy.md` files were written 2026-10-08 05:54–08:14. Which taxonomy files exist, which documents are classified, and what is the next unclassified member?*
  - Status: Open. Dependencies: None. This is the highest-value unread file in the project and the most likely subject of the "interrupted by bug reports" the user describes.
  - Evidence: `Articles/analyses/finding_taxonomy.md` (§5, §6); four sibling `*_taxonomy.md` files, newest content in the project after `3_Model/state.md`.

- [ ] **RS-2 — What is presentable from the knowledge graph under the vetoes?** (`wayfinder:research`)
  *Question: given the seven vetoes in `state.md:33-39` — and specifically the veto barring 2-pass pipeline "Key Quotes" as automatically valid — which of the KG's 40 nodes and 30 edges, and which of the 8 files in `Articles/analyses/`, can Lucas say out loud to Damian without tripping a veto?*
  - Status: Open. Dependencies: None.
  - Evidence: `Articles/graph/knowledge_graph.json` (40 nodes / 30 edges, `state.md:103`); `Articles/graph/paper_kags/bridge_larsen_berger_run1.json` is `llm_inferred` `SEMANTIC_LINKS` and never citable (`conventions.md:161`); veto `state.md:39`.

- [ ] **RS-3 — Which of Larsen (2024) is citable, given both Appendix E and Appendix F are unread.** (`wayfinder:research`)
  *Question: Appendix F was never read (`conventions.md:212-214`), and until it is, the six Larsen parameters may neither be cited as a source nor called fabricated (`state.md:33-34`). What is the minimum read that would settle this, and does it change what the briefing can say?*
  - Status: Open. Dependencies: None.
  - Evidence: `conventions.md:212-214` ("nog niet gedaan"); two `[DUE: 2026-10-04]` bullets at `state.md:54-55` for it; vetoes `state.md:33-34`.

- [ ] **RS-4 — The one research finding that survives every veto.** (`wayfinder:grilling`)
  *Question: if exactly one thing from the literature and extraction work may be said to Damian tomorrow without qualification, which is it — and what is the sentence?*
  - Status: Open. Dependencies: RS-1, RS-2, RS-3.
  - Evidence: the four `*_taxonomy.md` files (2026-10-08); `Articles/analyses/dynamic_kinetics_berger2008.md` (the most substantive existing analysis, 7,512 B).

### Island: The Artefact
*What actually exists at 09:00 tomorrow that Lucas walks in holding.*

- [ ] **AR-1 — What medium is the one-pager?** (`wayfinder:prototype`)
  *Question: the walkthrough spec requires "one page with the register table plus the traceability of each number" but names no format. Is it a printed A4 sheet, a single HTML slide, a terminal-rendered table, or a file on a laptop that is not shown?*
  - Status: Open. Dependencies: DR-2.
  - Evidence: `3_Model/state.md:59` names the artefact's *content* and not its medium. Runbook `html-slide-deck-build-and-grade.md` exists if HTML is chosen.

- [ ] **AR-2 — Is there a script, or is it a conversation?** (`wayfinder:grilling`)
  *Question: does Lucas walk in with a 12-minute script he can deliver, or with the register in hand and an argument he can defend? The two are different preparation and only one survives an unexpected question.*
  - Status: Open. Dependencies: DR-4.
  - Evidence: `3_Model/state.md:59` describes a *route* with timings, not a script; the destination's criterion 2 requires answering without looking it up, which argues for the latter.

- [ ] **AR-3 — Language and register of the briefing itself.** (`wayfinder:task`)
  *Question: is the delivered artefact in Dutch, English, or bilingual, and does `conventions.md` §7 (Damian comms = English, natural, low-key) govern the spoken briefing as well as written messages?*
  - Status: Open. Dependencies: None.
  - Evidence: `conventions.md:90-93`; `3_Model/state.md:59` is written in Dutch while the walkthrough content is technical English.

---

## 4. Not Yet Specified (The Fog of War)

*Cannot be formulated precisely until the frontier advances. Per the Fog Test (`SKILL.md:78`), these are not tickets and must not be dispatched blind.*

### Island: The Meeting Itself
- What Damian will actually ask that no amount of preparation anticipates. The register invites the question *"so is the model usable?"*, and the honest answer depends on DR-1, which is itself open.
- Whether the supervision-structure conflict (`state.md:6-11`, four irreconcilable lines including whether Bera is still main supervisor) surfaces in a research conversation. If it does, it is a conversation to have, not a blocker — but the briefing must not accidentally assert a supervision line it has not verified.

### Island: Figures and Visual Evidence
- Whether any plot is possible at all. It requires runnable chemistry, which requires filling `ModelParams.kinetics` from literature with **no invented constants** (Rule 16, and veto `state.md:33`), and the transport-only reduction chosen at `state.md:67` produces nothing to plot. This fog clears only when the kinetics-fill task has an owner.

### Island: Beyond Tomorrow
- The public thesis build (`toc.yml:9` → `content/Detail3.md` missing, master `I2-04`), the committee form (master `I3-01`, blocked on a Rule 41 question only the user can answer), and the Eenvoudig Model. None of these gate tomorrow's briefing and none should consume tonight's run.

### Island: Procedural
- Whether this briefing should ever become a reusable artifact. If it does, the missing runbook named in §1 gets written, and the defect-register-presentation question generalises past BEP.

---

## 5. Out of Scope

- **Fixing D1–D6.** The register is the content. Fixing the defects before the presentation destroys the presentation and is not asked for. `3_Model/state.md:60-66` keeps the fix tasks as separate `[DUE: 2026-10-02]` items.
- **Filling `ModelParams.kinetics`.** A research task gated on Rule 16 and two vetoes. Not a briefing prerequisite.
- **The defended-thesis destination.** Owned by [`bep_catalysis_master.md`](bep_catalysis_master.md), all 27 tickets. This map neither answers nor duplicates them.
- **The committee form, the mail to Els Arkesteijn, the CaSE onboarding.** Blocked on the supervision-line question (`state.md:23`), which is the user's alone.
- **Any edit to the master map.** One Map Per Goal (`SKILL.md:30`): two destinations, two maps, no merge.
- **Sending anything to Damian.** The briefing is a conversation. Per Rule 12 no loop is closed until an outgoing message exists, and per Rule 17 nothing here becomes a `⏳` row until it is actually sent.

---

## 6. Anchor note (Rule 38)

The walkthrough item at `3_Model/state.md:59` carries `[DUE: 2026-10-07]`, which has passed. Per `state.md:13` the agent **may propose** a re-anchor but may not rewrite it, and per Rule 38 no anchor type may be inferred. The briefing is a **conversation that happens at an unknown time tomorrow**, not a submission with a cutoff, so `[EVENT: 2026-10-09]` is the type the evidence supports if the owner confirms one — and no source states a cutoff, which means **there is no deadline here to breach**. Preparation work is `[DUE: 2026-10-08]`, agent-proposed and freely settable.

---

## 7. Provenance

Every factual claim in this map is cited to `file:line` and was verified on 2026-10-08. The register reproduction in §2 was obtained by executing `pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py` from the workspace root; its output is quoted, not paraphrased. Absence claims (zero figures, no runbook for defect-register presentation) were established by recursive extension sweep and by reading the full runbook directory listing via `grep`, never `glob` (`SKILL.md:107`).