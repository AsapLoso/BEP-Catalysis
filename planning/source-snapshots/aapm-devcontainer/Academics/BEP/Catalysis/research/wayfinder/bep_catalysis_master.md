# Wayfinder: BEP Catalysis — Master Decision Map

**Author:** agent, 2026-10-06 · **Scope:** decision-map authoring only. This file touches no state-engine file.
**Destination owner:** `Academics/BEP/Catalysis/state.md:19` (the task that commissioned this map, `[DUE: 2026-10-05]`).

**Reading rules that bind every ticket below.** Rule 16 (no claim without a `file:line` I read), Rule 36 (no claim about the world without a source on disk), Rule 38 (the anchor type must match the evidence — an expired date stays expired), Rule 41 (the user is ground truth for their own supervision situation and availability), Rule 33 (no batch-collapsing — one decision, one ticket).

**A ticket is a question whose resolution is a *decision*.** Not a coding chore, not a file-reading errand, not a to-do item. Where an open item in a source file has a determined answer rather than a decision in it, this map says so explicitly instead of manufacturing a fake question.

---

## 1. Destination

A defended BEP thesis on packed-bed acetylene semi-hydrogenation that is (a) backed by a transport-and-microkinetics model whose governing equations have been reconciled against their source, (b) published through a reproducible public thesis build whose canonical source of truth is unambiguous, and (c) has a settled examination-committee and supervision structure that the user has confirmed.

This is one destination with one verifiable end state, not four. The four islands below are the four known decision clusters *inside* it. Each is measured against this sentence: does resolving it move the thesis closer to defended, reproducible, and governance-settled?

**What "defended" excludes.** A defended thesis does not require the transient model to be defect-free; it requires that every defect is either fixed or stated in the text as a limitation. The defect register is an input to the destination, not the destination.

---

## 2. Decisions So Far

Only items with a real on-disk source. Each cites a line I read in this session.

### Island 1 — Reactor Transport & Microkinetica

- [x] **Numerics fixed: MOL, bulk advection = upwind/backward, intra-particle diffusion = central, time = implicit BDF.** `3_Model/transient_model_framework_audit.md:23` (D7, "partly implemented"), restated as a standing rule at `Academics/BEP/Catalysis/conventions.md:177`. Not reopened; only the `r = 0` node violates it (`3_Model/state.md:60`).
- [x] **Forward simulation on literature values first; fitting is a later, optional stage.** `3_Model/transient_model_framework_audit.md:22` (D6) and `conventions.md:176`.
- [x] **Rate = Arrhenius × Langmuir as complementary axes, not alternatives.** `3_Model/transient_model_framework_audit.md:20` (D4).
- [x] **Centered Arrhenius (Berger Eq. 17) is retained together with Berger's reason** — the binary correlation falling below 0.71 — not the formula alone. `3_Model/transient_model_framework_audit.md:21` (D5); the number is at `Articles/analyses/dynamic_kinetics_berger2008.md:66`.
- [x] **Three coupled levels, with `C_b` and `C_s` structurally separate in code but equalised to recover Berger's collapsed form.** `3_Model/transient_model_framework_audit.md:17-18` (D1, D2) and `conventions.md:171-172`. The stated reason — Berger Eq. (1) has no film term, so pseudo-homogeneity *is* Berger's model — is at `3_Model/transient_model_framework_audit.md:18`.
- [x] **Intra-particle diffusion is explicit, never instantaneous.** User override of Gemini, `3_Model/transient_model_framework_audit.md:19` (D3). It is *our* extension: Berger's state count is `(N_gas + N_surf) × N_z`, no radial coordinate (`3_Model/transient_model_framework_audit.md:19`, `:17`).
- [x] **Three of four numeric thresholds are already settled against Berger: the chat's forms are wrong, not open.** Wheeler–Weisz is `< 0.1` not `< 0.05` (`3_Model/transient_model_framework_audit.md:37`); `t_in` is the reciprocal `(D_e/(ε_p R²))·t` and Berger wins (`3_Model/transient_model_framework_audit.md:38`, `:42`); `t_ex` loses the spurious `k₀` and gains `ε_b` (`3_Model/transient_model_framework_audit.md:39`). Carberry and both Prater numbers already agree (`3_Model/transient_model_framework_audit.md:34-36`).
- [x] **`Ca ≤ 0.15` / `Da_II ≤ 0.3` belong to a different paper and are forbidden for Berger.** `3_Model/transient_model_framework_audit.md:44`; also pinned as a veto at `state.md:57`.
- [x] **`Bim` is settled: the standard mass Biot number is `k_g R/D_e`; the reversed `D_e k_g R` is a transcription error and must not reach the code.** `3_Model/transient_model_framework_audit.md:106-108`. **This is not an open question** and must not be re-ticketed.
- [x] **The 13-vs-14 count discrepancy in the framework register is settled in favour of 14.** The register's own §3 contains nine defects (`3_Model/transient_model_framework_audit.md:7`, `:52`, `:72`, `:81`, `:87`, `:91`, `:102`, `:106`, `:110`, `:114`) plus the §2 threshold conflicts, and `state.md:52-66` enumerates FW-1 … FW-14 — **fourteen atomic bullets**, confirmed by reading lines 52 through 66. `Academics/BEP/Catalysis/state.md:52` announces "13 openstaande punten" in its own prose while listing fourteen; root `task.md:189` says fourteen. The *register* count of 14 is right; the prose "13" is the error.
- [x] **Cost figures, corrected 2026-09-30 and superseding every earlier number: one rhs call = 0.016 s; one finite-difference Jacobian = `DIM` = 1480 rhs calls = 23 s.** `3_Model/state.md:65` and the register row at `3_Model/state.md:83`. The superseded "~2.2 s per rhs" figure is explicitly retracted as `wall/nfev` folding in Jacobian work (`3_Model/state.md:65`). The durable claim is structural, not the seconds: rhs cheap, Jacobian dominant (`3_Model/state.md:87-90`).
- [x] **D2's correct value is known and settled: the exact spherical limit at `r = 0` is `6/dr²`, the code uses `(1+s) = 3`, and the script deviates 2× from its own spec.** `3_Model/state.md:60` and `:79`. The value is not a decision; whether the model may be *reported* with it open is (see Island 1 ticket I1-07).
- [x] **D5's earlier "double `C_t`" claim is retracted. Both `C_t` factors are correct; what remains is a wrong docstring and one symbol carrying two rate normalisations.** `3_Model/state.md:64` and `:82`; the same point is framework §3.9 at `3_Model/transient_model_framework_audit.md:114-116`.
- [x] **Larsen's Eqs. 4.6–4.9 and 6.9–6.11 are verbatim-confirmed, including the `r₂` asymmetry, which must not be "corrected".** `conventions.md:186-187`.
- [x] **The six Larsen parameter values from `run2`/`_consensus` are formally unusable, and must not be called fabricated.** `conventions.md:195-206`, escalated to veto at `state.md:25-26`. Two independent grounds: unverifiable from our text layer (`conventions.md:201`), and the set is *incomplete* — `r_{1,max}` and `n_{inh}` are missing (`conventions.md:202`).
- [x] **`bep_example_index.md` is demoted to a navigation aid, not a parameter or fact source.** `conventions.md:227-234`, veto at `state.md:27`. Verified faults: catalyst series reversed, Pd loadings wrong, fabricated process steps, invented geometry (`conventions.md:231-234`).

### Island 2 — Thesis MyST/Typst Pipeline & R-PUBLIC

- [x] **The external repo exists on disk, is a sibling of this workspace, and is the live public thesis artefact.** `Methanol-Catalysis` at `Misc\Gemini\Methanol-Catalysis`, remote `https://github.com/AsapLoso/Methanol-Catalysis`, GitHub Pages deployed from `main` with **no staging environment and no undo** (`Methanol-Catalysis/AGENTS.md:3-4`). Linked from `DOCUMENT_MAP.md:103-104` and `state.md:150`.
- [x] **`myst.yml` and `authors.yml` are already personalised. Author metadata is NOT to be re-planned.** Title set at `Methanol-Catalysis/myst.yml:4`, GitHub URL at `:8`, date at `:9`; all five role slots filled at `Methanol-Catalysis/authors.yml:11-28` (read via `bash`, outside the workspace root). The remaining personalisation chore is logged separately at `state.md:97`.
- [x] **A hard publication-boundary rule already exists and is not up for re-deciding: no personal names, no deadlines or exam dates, no committee/grading/contact data, no absolute Windows paths.** `Methanol-Catalysis/BEP_SOURCE_MAP.md:25-31`. The leak vector that already bit this repo is named there: Zotero auto-export writing `file = {%USERPROFILE%` into `references.bib` (`Methanol-Catalysis/BEP_SOURCE_MAP.md:31`).
- [x] **The repo enforces its own R-PUSH rule: no push without an explicit in-turn instruction naming both the act and the branch `main`.** `Methanol-Catalysis/AGENTS.md:11-20`, and `:23-30` states the load-bearing sentence — a task that cannot complete without a push is a blocked task, not a push.
- [x] **Chapter skeleton and build config are in place; the thesis is structurally MyST/Typst, built with `pixi`.** `Methanol-Catalysis/toc.yml:5-9` (chapter list), extended from `myst.yml`, `toc.yml`, `authors.yml`, `options.yml` (`Methanol-Catalysis/myst.yml:33-37`); stack conventions at `conventions.md:129-141`.

### Island 3 — Examencommissie & CaSE Formaliteiten

- [x] **TWN3002-24 requires a four-member standing-staff committee with a fixed composition.** Slot *a* TW1 DIAM, *b* TN2 TNW, *c* TW3 DIAM (different section from *a*, at least one of *a*/*c* BEP-senior), *d* TN4 TNW (at least one of *b*/*d* teaches BSc TN) — `committee_candidates.md:9-13`, restated at `conventions.md:123-125`. Voetnoot 3 and 4 spelled out at `conventions.md:106-107`. Submission is at the latest 3 months before the intended end date via `BoE-AM@tudelft.nl` (`committee_candidates.md:8`, `conventions.md:124`).
- [x] **The committee-exception quote that is genuinely on disk.** Bart van den Dries (BC-TW), at `Academics/meeting_transcript_bart_bc_tw.md:183`: deviations are approvable when the quality argument is substantiated — *"dan kan een examencommissie gewoon zeggen: je hebt er goed over nagedacht, we kunnen dit wel goedkeuren."* Quoted at `state.md:139`.
- [x] **The design constraint is a hoofd-begeleider on *both* TN and TW — an engineering problem, not an external blockade.** Bart, 29 May 2026, at `.agents/triage/review/Curriculum/BEP_regelingen.md:19`: *"het is belangrijk dat er zowel bij TN als TW een hoofdbegeleider is die je project goedkeunt."* Read at `state.md:137-138`.
- [x] **The mathematical half of the committee is confirmed; the physical half is the open piece.** `Academics/meeting_transcript_bart_bc_tw.md:202` ("the Mathematics portion … is confirmed … with Zoe acting as supervisor and Neil Budko approached") and `:211` (split-supervision strategy). Recorded as the residual risk at `state.md:140`.
- [x] **The CaSE secretariat email must NOT be sent. Two independent blockers stand, and the email is not a single blocker.** Missing portrait photo and an unfixed supervision line in the bio, `state.md:38`; independently `thread_els_arkesteijn.md:75`. The bio reaches **a public TU webpage and a printed poster board** (`thread_els_arkesteijn.md:27`, `state.md:38`) — a poster cannot be silently corrected.
- [x] **The earlier `COMMISSIE COMPLET` status was retracted because the ruling was never located, not because no ruling exists.** `state.md:5`. No file on disk contains the ruling text (`state.md:5`: the workspace stopped registering on 2026-09-02T17:20:55Z and the following 27 days exist neither on disk nor in the workspace).
- [x] **A standing instruction to hold further contact is on record from the programme side.** Paula Endeveld: *"Wacht alsjeblieft verdere berichten van de opleiding of de examencommissie af voordat je verdere stappen onderneemt"* — `thread_examencommissie_paula.md:41-42`. Lucas confirmed compliance at `thread_examencommissie_paula.md:98`.
- [x] **The `2026-09-29` PRIO-0/PRIO-1 anchor is EXPIRED and stays expired. It is not rolled forward anywhere in this map.** `state.md:13` ("⚠️ Doeldatum verstreken … **Niet automatisch herijken**"), recorded on the same line as the Rule 23/38 constraint that re-anchoring happens in consultation.

### Island 4 — Begeleiding & DCSC S&C Control Hub

- [x] **Island 4 is downstream of Island 3 and cannot be planned until the supervision question is answered.** `state.md:11` ("Niet gokken — gebruiker vragen") and the same ordering is stated on the SysCon track at `Academics/BEP/SysCon/state.md:11`, where the Roel Smit action is explicitly gated on asking the user first. **Every Island 4 ticket below inherits this dependency.**
- [x] **The committee-exception route is formally available and already on record as the strategy.** `Academics/meeting_transcript_bart_bc_tw.md:183`; the routing decision (math board first with an explanatory note, then forwarded to physics) at `Academics/meeting_transcript_bart_bc_tw.md:212`.
- [x] **The DCSC scope question is already chartered as a gating question on a sibling map, and its answer is NOT free.** `research/wayfinder/dcsc_thesis_relevance.md:22` poses it as the blocking scope decision (HITL, "the agent must not answer this") and `:24` notes it has the highest leverage on that map. That map's own findings stand as evidence: DCSC publishes **0/8** on `state estimation`/`Kalman`/`observer`, **0/8** on `CFD`/`flow`/`turbulence`/`FSI`, and **0/8** on `MPC` (`research/wayfinder/dcsc_thesis_relevance.md:16`).
- [x] **Carlas Smith's own recorded position, in his words, from the thread.** Conditional: *"Als ik inhoudelijk de beste ben, wil ik het wel doen!"* — `thread_carlas_smith.md:94`, header status at `thread_carlas_smith.md:5`, mirrored at `committee_candidates.md:25`. He also declined formal *quality-of-supervision* responsibility (`thread_carlas_smith.md:49`) and advised consulting Roel Smit (`thread_carlas_smith.md:50`).

---

## 3. Active Frontier

Open, unblocked-where-stated questions, partitioned by island. Each is a *decision*. **Ticket count: 27 tickets across the four islands — Island 1: 11, Island 2: 4, Island 3: 6, Island 4: 6.**

**Crosswalk-stand 2026-10-18:** 25 open — `I1-10` gesloten (telling gecorrigeerd in `state.md:112`), `I3-04` vervallen (user-reported verzending; `state.md` §STATUS RECONCILED). Classificatie per ticket: [map_state_crosswalk_2026_10_18.md](../notes/map_state_crosswalk_2026_10_18.md).

### Island 1: Reactor Transport & Microkinetica

- [ ] **I1-01 — Appendix E.1–E.3 admissibility** (`wayfinder:research`)
*Question: do the fitted parameter tables in Appendix E of the Larsen 97-page reference contain the full final-model parameter set (including `r_{1,max}` and `n_{inh}`), and is that set admissible as the kinetic basis for our packed-bed model — or does it fail on geometry/normalisation grounds regardless of what it contains?*
- Status: Open. Dependencies: none — this is the **root gate of Island 1**; it decides whether Island 1 has a parameter basis at all.
- Evidence: `conventions.md:212-214` names the exact mechanical route (render pages 71–76 as images, read via the vision subagent). Seven appendix pages have no text layer, and `p.81` / `p.87` — precisely the pages `run2` cites — sit among them (`conventions.md:214`). The thesis itself points to the tables: *"The parameters used in each variant can be found in Appendix tables E.1 to E.3"* (`conventions.md:201`, quoting `Ch6:436-437`).
- **Hard constraint: no numeric value may be invented.** If an image is unreadable, this ticket stays open with `UNVERIFIED`. The veto at `conventions.md:206` and `state.md:26` forbids both using and falsely accusing the `run2` values.

- [ ] **I1-02 — Appendix F geometric and numerical closure** (`wayfinder:research`)
*Question: do pages 77–88 of the reference define the cross-section `A` and support density `rho_support`, and do they fix the solver, grid, tolerance and Damköhler bounds — and if they do not, which of these become declared modelling assumptions?*
- Status: Open. Dependencies: none; runs parallel to I1-01.
- Evidence: `A` and `rho_support` are **nowhere defined** in Eqs. 4.6–4.9 — no cross-section, bed length, voidage or pellet size anywhere in the thesis (`conventions.md:210`). Without them the model is unnormalised and there is no conversion prediction (`conventions.md:210`). Route: `conventions.md:214`.

- [ ] **I1-03 — Resolve the `$u_s` / `ε` ambiguity at the source** (`wayfinder:research`)
*Question: does Berger Eq. (1) mean superficial or interstitial velocity — i.e. does `u_s/ε` denote a superficial flux with an interstitial reading layered on by the local annotation, or is `u_s` already interstitial with `ε` a second, different voidage?*
- Status: Open. **Blocks I1-04, and through it the transport-criterion derivation and every downstream `u_s` use.**
- Evidence: the dossier's Term-2 annotation calls `u_s/ε` the *"interstitial velocity"* (`Articles/analyses/dynamic_kinetics_berger2008.md:30`) while Eq. (1) itself carries no `ε_b` on the accumulation term (`Articles/analyses/dynamic_kinetics_berger2008.md:27`). The audit states the dossier **cannot settle it**: *"Check the PDF before coding — this changes what `u_s` means everywhere downstream, including the `f_max` derivation"* (`3_Model/transient_model_framework_audit.md:70`).

- [ ] **I1-04 — Which artefact survives as the bulk governing equation** (`wayfinder:grilling`)
*Question: given that the displayed bulk equation and the pseudocode in the same source document disagree by a factor `ε_b²` on the dominant term, do we delete the displayed equation and keep the pseudocode as the spec, or repair the displayed equation and demote the pseudocode?*
- Status: Open. Dependencies: **I1-03** — the audit's "term for term" claim holds *only* under the identification `ε ≡ ε_b` (`3_Model/transient_model_framework_audit.md:68`).
- Evidence: chat form `−ε_b u_s ∂C/∂z` vs Berger's `−u_s/ε`; at `ε_b ≈ 0.4` the chat form is `0.16×`, i.e. Berger is 6.25× larger (`3_Model/transient_model_framework_audit.md:60-62`). The pseudocode reproduces Eq. (1) term for term (`3_Model/transient_model_framework_audit.md:66`). The `R_i` volumetric source and the `k_g a` film flux are **two different closures, not two spellings of one** (`3_Model/transient_model_framework_audit.md:64`).

- [ ] **I1-05 — Readsorption: model it or scope TPD out** (`wayfinder:grilling`)
*Question: do we add the readsorption/TPD-desorption channel the source calls the *only* explicit modelling requirement of its Section 5, or do we declare TPD parameter extraction out of scope explicitly and accept that the transport-criteria story then does not close?*
- Status: Open. Dependencies: none on the frontier, but it gates the credibility of the whole transport-criterion narrative.
- Evidence: the same conversation that flags readsorption as required then delivers a model without it — *"The chat is internally inconsistent"* (`3_Model/transient_model_framework_audit.md:83`). Consequence stated at `:85`. **Silence is not an available option**: a silent omission leaves the transport story open (`state.md:59`).

- [ ] **I1-06 — Film closure: solve the flux balance or drop the film** (`wayfinder:grilling`)
*Question: with explicit film resistance retained, do we solve `k_g a (C_b − C_s) = −(3/R)·D_e·(∂c_p/∂r)|_{r=R}·(1−ε_p)/(1−ε_b)`, or do we drop the film and keep pseudo-homogeneity? There is no third option.*
- Status: Open. Dependencies: none.
- Evidence: under pseudo-homogeneity `C_s` is not a state and loop order is irrelevant; under explicit film resistance `C_s` is an *algebraic function of two states*, so it cannot be both equalised and solved (`3_Model/transient_model_framework_audit.md:95-98`). **This is a coupling question, not an ordering question** — picking the closure once dissolves the ordering problem (`3_Model/transient_model_framework_audit.md:100`, restated at `state.md:61`).

- [ ] **I1-07 — Correctness gate: what must be fixed before the model may be reported** (`wayfinder:grilling`)
*Question: which register entries must be closed before any number produced by this model may appear in the thesis, and which may be reported as stated limitations instead?*
- Status: Open. Dependencies: I1-03 (D2's fix depends on the `u_s` reading), I1-06 (the film switch determines whether D1's boundary-condition complaint is a real defect or a symptom).
- Evidence — the register, with the corrected cost figures: **D1** rhs mutates the solver's state vector through a `reshape` view, 80/1480 entries modified per call, A/B `max|Δ| = 5.1`, **blocking** (`3_Model/state.md:59`, `:78`); **D2** `r = 0` coefficient is half the exact value (code `3`, exact `6`), **blocking** (`3_Model/state.md:60`, `:79`); **D3** `θ` at the pellet shell never receives a derivative, `all(dTheta[:, -1, :] == 0)` is True, **blocking** (`3_Model/state.md:61`, `:80`); **D4** particle-volume quadrature is `O(dr)`, discrete/analytic sum `0.840`, particle-averaged rate **16% low** (`3_Model/state.md:62`, `:81`); **D5** `R_gas` docstring unit wrong, one symbol two normalisations (`3_Model/state.md:64`, `:82`); **D6** rhs 0.016 s but one Jacobian costs 1480 rhs calls = 23 s, blocking for any sweep but not for a single run (`3_Model/state.md:65`, `:83`).
- **This ticket is one, not six, by design.** D1, D2, D3 and D4 each have a *determined* correct answer — they are fixes, not decisions. What is genuinely undecided is the reporting gate. Rule 33 forbids collapsing distinct decisions; it does not require manufacturing a decision where an arithmetic result already exists.
- **Two register entries are deliberately NOT re-ticketed:** the reversed `Bim` is a settled transcription error (`3_Model/transient_model_framework_audit.md:106-108`), and the "all kinetic constants are `0.0`" row is marked *by design* in the register itself (`3_Model/state.md:85`) — it is the state of an unfilled model, not a defect.

- [ ] **I1-08 — Kinetic constant sourcing policy when Appendix E stays unread** (`wayfinder:grilling`)
*Question: if I1-01 returns unreadable or non-admissible tables, what is the acceptance criterion for the model's chemistry — and specifically, what replaces the impossible "reproduce RMSE 5.10", given there are no measurements to fit against?*
- Status: Open. Dependencies: I1-01.
- Evidence: the acceptance test was explicitly ruled out as *"geen 'reproduceer RMSE 5.10': er zijn geen meetdata om tegen te fitten"* (`state.md:51`). The `r₁` saturation / `r₂` collapse / GHSV selectivity qualitative battery is the fallback shape (`state.md:49`). The bridge linking the `r_{1,max}` cap to the transport criteria is tagged `llm_inferred` — a semantic association, **not** a sourced equivalence (`2_Courses/PDC/course_overview.md:87-93`).

- [ ] **I1-09 — Transport-model reduction: plug flow vs Danckwerts** (`wayfinder:grilling`)
*Question: do we keep the plug-flow / pseudo-homogeneous reduction as a *declared, justified* choice, or implement axial dispersion with Danckwerts boundary conditions — and what is the acceptance threshold on `Pe` that decides it?*
- Status: Open. Dependencies: I1-06 (film resistance is the same reduction decision on the other side).
- Evidence: the reference derivation retains `D_ax ∂²C/∂z²` and an external film coefficient `k_c` with Danckwerts BCs (`1_Transport_Phenomena/pbr_transport_phenomena.md:11`, `:101`); the code implements plug flow plus pseudo-homogeneity with no dispersion and no film (`3_Model/state.md:66`). That reduction is legitimate — it is exactly the `Pe ≫ 100` case — but it is a *choice* and must be stated as one (`3_Model/state.md:66`; the `Pe ≫ 1` regime is at `1_Transport_Phenomena/pbr_transport_phenomena.md:95-96`). Whether `D_ax` gets a switch is still open per the audit's undefined list (`3_Model/transient_model_framework_audit.md:144`).

- [x] **I1-10 — Resolve the 13-vs-14 count in the state files** (`wayfinder:task`)
*Question: which register does the canonical `state.md:52` prose count of "13 openstaande punten" refer to, given that the same bullet enumerates FW-1 through FW-14 and the root tracker says 14?*
- Status: **Answered 2026-10-13; closed 2026-10-18.** The count is **14**; the authorised state owner applied the correction (`state.md:112` → 14) and pruned the mirror bullet.
- Dependencies: none.
- **Evidence update 2026-10-13 (verified by enumeration, not inference):** the bullet at `Academics/BEP/Catalysis/state.md:69` announces "13 openstaande punten" and then lists the atomic items `FW-1` … `FW-14` beneath it — fourteen. Root `task.md:197` independently says fourteen. **The register's count of 14 is right; the prose "13" is the error.**
- **Note on authority:** resolution was a one-line correction to `state.md`, which this map and this mission were **not authorised to perform** (state-engine isolation). **Closed 2026-10-18:** the authorised state owner corrected `state.md:112` (13 → 14) and pruned the stale mirror bullet; see the [crosswalk](../notes/map_state_crosswalk_2026_10_18.md).

- [ ] **I1-11 — Verify-or-drop the eight UNVERIFIED claims** (`wayfinder:research`)
*Question: for each of the eight claims that appear in no `references.bib`, no dossier and no acquired PDF, does the source page actually say it — and for those that do not, is the claim deleted or replaced?*
- Status: Open. Dependencies: none.
- Evidence — the eight, as enumerated at `state.md:66` and tabulated at `3_Model/transient_model_framework_audit.md:126-133`: the *"Section 5"* vs Table-2 numbering disagreement; the "Dekker et al." author attribution; Gleaves' TAP criterion `H_p t_p ≤ 0.31`; the `ΔP < 0.1 bar` bed limit; Gorte's six dimensionless groups; the *"120 µm Cu–Cr, ≈1 ms"* example (the dossier has a *different* catalyst and a *different* number — do not merge, `:131`); the **8 ms valve / 0.1–1 s MS response** pair, load-bearing because it sets the fastest resolvable step (`:132`); and the SO₂/NOₓ → 3D-CFD pilot-plant-riser example with no paper in `acquired_pdfs/` (`:133`). **Eight, not nine** — the ninth row, the `< 0.71` correlation, *is* verified at `dynamic_kinetics_berger2008.md:66` and is listed only for completeness (`3_Model/transient_model_framework_audit.md:122`, `:134`).

### Island 2: Thesis MyST/Typst Pipeline & R-PUBLIC

- [ ] **I2-01 — Canonical source of truth** (`wayfinder:grilling`)
*Question: is the thesis written in the in-project BEP MyST tree and exported to the public repo, or authored directly in the public `Methanol-Catalysis` repository — and where exactly does the public/private boundary sit?*
- Status: Open. **This is the load-bearing ticket of Island 2.** Everything else — CI, deployment, archival, sync direction — is downstream of this one call and cannot be planned until it is made.
- Why it is a decision and not a default: the destination requires a *reproducible public build*, which requires knowing which tree is authoritative. Both candidates have real cost. The public repo has no staging environment and no undo (`Methanol-Catalysis/AGENTS.md:3-4`), and it is subject to a hard no-personal-names / no-dates / no-committee-data rule (`Methanol-Catalysis/BEP_SOURCE_MAP.md:25-31`) that the in-project tree does not need to obey — so the two trees are not interchangeable, and the choice of home changes what may be written at all.
- Explicitly **not** in this ticket: `authors.yml` and `myst.yml` are already personalised (`Methanol-Catalysis/myst.yml:4`, `:8`; `authors.yml:11-28`). Do not reopen author metadata.

- [ ] **I2-02 — Disposition of the unpublished divergence** (`wayfinder:grilling`)
*Question: what happens to the local commit that exists on disk but not on `origin/main` — publish it, hold it, or split it — given the repository auto-deploys and has no undo?*
- Status: Open. Dependencies: I2-01 (the answer depends on which tree is canonical), and I2-03 (publishing it would publish the supervision claim).
- Measured state, read via `bash` at session time: local `HEAD` is `e0663ba` — *"pbr: Complete transient PBR catalytic framework (TVD2, radial diffusion, stiff solver, 37 passing tests)"*, dated 2026-10-01, touching 19 files with 4885 insertions; `origin/main` is `24f0559` (*"Gitignore upstream reference manuals and templates"*). `git rev-list --left-right --count origin/main...HEAD` returns `0  1` — **one commit ahead, nothing behind**. The working tree is also dirty: **6 modified tracked files** (`content/Conclusion.md`, `content/Index.md`, `pixi.lock`, `pixi.toml`, `references.bib`, `toc.yml`) and **11 untracked paths** (including `.agents/`, `.opencode/`, `opencode.json`, `AGENTS.md`, `.githooks/`, `content/Detail1.md`, `content/Detail2.md`, `content/Leken.md`, `content/.obsidian/`, `content/CONSOLIDATED_OVERNIGHT_PROMPTSET.md`, `.gitattributes`).
- **Rule 42 caution:** this is a genuine trade-off (publishability vs. irreversibility of an auto-deployed public site), and the trade-off belongs to the user. This map states the decisive facts and poses the question; it does not resolve it.
- **R-PUSH reminder for whoever acts on this ticket:** a decision to publish is not itself authorisation. `Methanol-Catalysis/AGENTS.md:11-20` requires an explicit instruction in the current turn naming both the act and the branch, and `:23-30` states a task that cannot complete without a push is a blocked task.

- [ ] **I2-03 — The supervision claim currently baked into public-facing metadata** (`wayfinder:research`)
*Question: does the public-facing author/contributor metadata in the thesis repo assert a supervision structure that the in-project record does not support — and if so, what is the minimum correction that can be applied before any publication decision?*
- Status: Open. **Dependencies: Island 3 ticket I3-01.** This ticket cannot resolve before the user confirms the supervision structure; it can only establish *what the metadata currently says*.
- Evidence: the public repo's own rule forbids publishing personal names without a deliberate separate decision (`Methanol-Catalysis/BEP_SOURCE_MAP.md:26`), yet the contributor block is populated with named supervisors and examiners (`Methanol-Catalysis/authors.yml:11-28`) and the site renders them (`myst.yml`, `hide_authors: false`). In-project, four files give four mutually incompatible supervision lines and the user reported on 2026-09-29 that a ruling has long existed and that one named person is no longer main supervisor (`state.md:5-11`). **This map names nobody** (Rule 41) — the discrepancy is recorded, not adjudicated.
- **Do not silently edit the public metadata.** A published name is a published name; correction is a decision, and it is downstream of I3-01.

- [ ] **I2-04 — Resolve the broken chapter reference** (`wayfinder:task`)
*Question: should `content/Detail3.md` be created, or should the entry be removed from the table of contents — given the file is listed but does not exist on disk?*
- Status: Open. Dependencies: I2-01 (the tree layout follows from the canonical-source answer).
- Evidence: `Methanol-Catalysis/toc.yml:9` lists `content/Detail3.md` as a child of `content/Leken.md` (`toc.yml:5-9`). A filesystem existence check at session time returns **False** for `content/Detail3.md`, while `Detail1.md` and `Detail2.md` both exist. A build will fail on a missing include.
- This is a genuine *decision* despite looking mechanical: creating the chapter and deleting the entry commit the thesis to a different outline, and that outline choice belongs with I2-01.

### Island 3: Examencommissie & CaSE Formaliteiten

- [ ] **I3-01 — Current TNW draft fields recorded; TW3 seat still open** (wayfinder:grilling)
*Question: which eligible second DIAM staff member, if any, should fill the still-open TW3 seat, and what formal checks remain for the user-selected TNW draft fields?*
- Status: **TNW draft fields supplied by the user on 2026-10-20** (Urakawa responsible supervisor; Bera second TN examiner). This is not proof of a current signed form, formal appointment, consent, or Board approval. The TW3 seat remains open; no candidate is selected or approached, and outreach still requires the user decision.
- Historical proposal and committee-table role lines are preserved as dated records; they are not the current user-selected draft fields. The current form version and formal approvals remain unverified.
- User-reported 2026-09-29: a named person is no longer main supervisor and *"de uitspraak is er al lang"* regarding the Examencommissie. The user report establishes that the user says a ruling exists; its exact source, wording, and scope are not located in the saved correspondence. Do not turn this archive gap into a claim that no ruling exists.
- **The bio must not be sent until this resolves** (`state.md:38`, `thread_els_arkesteijn.md:75`).

- [ ] **I3-02 — Locate the exact user-reported Examencommissie ruling** (wayfinder:grilling)
*Question: where is the authoritative record of the ruling the user reports exists, and what does its exact wording cover?*
- Status: Open archive-source task. The user has already reported that a ruling exists; the saved Paula thread records an earlier hold, not the later ruling. Do not send a new request while the programme-side hold remains in force.
- Evidence: The August request lists three constructions (thread_examencommissie_paula.md:15-19); Paula later asked Lucas to wait (:41-42). That earlier hold does not contradict the later user report. The exact later text and scope remain an archive gap.
- A face-to-face route is on record as the adviser's own suggestion (`Academics/meeting_transcript_bart_bc_tw.md:183`).
- **Constraint carried forward:** the standing hold from the programme side is still live (`thread_examencommissie_paula.md:41-42`), so "request it" is not a free action.

- [ ] **I3-03 — Which of the three submitted constructions to pursue** (`wayfinder:grilling`)
*Question: once the user-reported ruling is located, which submitted construction does it address, and what remains unresolved for the current form?*
- Status: Open. Dependencies: I3-01, I3-02.
- Evidence: the three constructions are preserved at thread_examencommissie_paula.md:17-19. They are historical options; their current applicability depends on the located ruling text and current form version. Construction 3 matches the recorded split-supervision strategy (Academics/meeting_transcript_bart_bc_tw.md:211), but the archive does not establish that the Board approved it.

- [x] **I3-04 — The Els Arkesteijn email: what unblocks it** (`wayfinder:grilling`)
*Question: does the portrait photo get supplied and the supervision line settled by I3-01, or do we send the email with the photo and bio deliberately omitted and the confidentiality agreement alone?*
- Status: **Superseded 2026-10-18** (email user-reported sent 13/15-10; attachment details UNVERIFIED). Dependencies: none live; the remaining verification is the ADMIN action in `state.md`.
- Evidence: the secretariat asked for three things — a signed form, a portrait photo publishable **on the webpage and on the poster outside the secretariat**, and a short introduction (`thread_els_arkesteijn.md:26-28`). The photo is not on this device (`state.md:37`, `thread_els_arkesteijn.md:77`). The blocking status is recorded at `state.md:38` and `thread_els_arkesteijn.md:75`.
- **The poster is the reason this is a decision rather than a chore.** A published webpage can be corrected in a minute; a printed board cannot be corrected silently (`state.md:38`, `thread_els_arkesteijn.md:88`).
- The confidentiality agreement itself is signed and filed (`state.md:37`).
- **Closed 2026-10-18 as superseded:** the user reported the Els email sent (13/15-10; `state.md` §STATUS RECONCILED). Attachment/form details remain unverified and are tracked as ADMIN actions in `state.md`; see the [crosswalk](../notes/map_state_crosswalk_2026_10_18.md).

- [ ] **I3-05 — Re-anchor or retire the expired 2026-09-29 target** (`wayfinder:grilling`)
*Question: the PRIO-0 confidentiality mail and both PRIO-1 core deliveries carried a `[DUE: 2026-09-29]` target that has passed with every bullet still open — do we re-anchor them, split them, or retire them?*
- Status: Open. Dependencies: I3-04 for the PRIO-0 bullet.
- Evidence: the expiry is recorded verbatim at `state.md:13` with the instruction **not** to re-anchor automatically; re-anchoring happens in consultation. Root tracker duplicates both bullets with the same expired anchor (`task.md:177`, `:178`, `:179`).
- **Rule 38 applied:** this is an expired date, not a fresh deadline, and it is not silently rolled forward here. It is also *not* a breach report — the underlying work is incomplete, not late-and-abandoned, and the distinction matters for how the map reads it.

- [ ] **I3-06 — The missing evidence file** (`wayfinder:task`)
*Question: the file recorded as the source of the committee-exception quote does not exist on disk — where did that quote actually come from, and does the citation need repointing?*
- Status: Open. Dependencies: none.
- Evidence: `Academics/BEP/Catalysis/.agents/triage/user_messages_since_bijoy.txt` returns **False** on a filesystem existence check at session time. The committee-exception quote that *is* real and *is* on disk lives at `Academics/meeting_transcript_bart_bc_tw.md:183`. **This map cites the transcript, not the missing file.**
- The distinction matters under Rule 28 §5.6.7: a citation to a nonexistent path is a fabricated anchor. Recorded here so the next session repairs it rather than propagating it.

### Island 4: Begeleiding & DCSC S&C Control Hub

> **Dependency, stated once and inherited by every ticket below: Island 4 is DOWNSTREAM of Island 3.** The supervision question must be answered by the user (I3-01) before any of this can be planned, because every item here is a supervision-structure item. `state.md:11`, `Academics/BEP/SysCon/state.md:11`. Tickets are still formulated precisely now, because precision is available — only their *resolution* is blocked.

- [ ] **I4-01 — Formal supervision slots under TWN3002-24** (`wayfinder:grilling`)
*Question: with the TN main supervisor settled by I3-01, which of the four numbered slots does each named party occupy — and does the resulting committee satisfy voetnoot 3 and voetnoot 4 as written?*
- Status: Open. **Blocked by I3-01.**
- Evidence: the four-slot structure at `committee_candidates.md:9-13` and `conventions.md:123-125`; voetnoot 3 (slots *a* and *c* both DIAM, different sections, at least one BEP-senior) at `conventions.md:106`; voetnoot 4 (slots *b* and *d* both TNW, at least one teaching BSc TN) at `conventions.md:107`. The current status matrix at `committee_candidates.md:20-27` and `state.md:124-131` is the thing being tested — and it is exactly what I3-01 puts in question.
- **No agreement, acceptance or eligibility may be assumed.** Every status in that matrix is provisional (`committee_candidates.md:20-27`).

- [ ] **I4-02 — Is the DCSC-affiliated candidate eligible as slot *d*** (`wayfinder:grilling`)
*Question: does the DCSC-affiliated candidate satisfy voetnoot 4 — TNW standing staff, and does at least one of slots *b*/*d* teach in the BSc TN — and is the answer yes without depending on which person occupies slot *b*?*
- Status: Open. **Blocked by I3-01 and I4-01** (voetnoot 4 is a disjunctive requirement satisfied by *b* *or* *d*, so the answer genuinely depends on the other slot).
- Evidence: recorded as *Voorwaardelijk Akkoord* with the condition quoted in his own words — *"Als ik inhoudelijk de beste ben, wil ik het wel doen!"* (`thread_carlas_smith.md:94`, `committee_candidates.md:25`). He declined formal responsibility for supervision quality (`thread_carlas_smith.md:49`) and pointed at Roel Smit as the person who knows the frames (`thread_carlas_smith.md:50`, echoed `committee_carlas_smith.md:69`).
- **Also on record, and it cuts against the candidacy:** he advised looking for a second corrector *close to the specific research subject* rather than by affiliation (`thread_carlas_smith.md:92`). That is a substantive-fit argument, not a formality.

- [ ] **I4-03 — What does the user-reported ruling say about the physics half?** (wayfinder:research)
*Question: can the exact ruling source be located, and does its wording address the physics-side supervision separately from the mathematics-side arrangement?*
- Status: Open. Dependencies: I3-02.
- Evidence: the recorded meeting confirms the mathematics half (Academics/meeting_transcript_bart_bc_tw.md:202); the physics-side position remains separately unresolved in the archived meeting notes (:201, :211). The user reports a later ruling exists, but its exact text is not in the saved archive.
- Per Rule 41, the programme-side hold is user ground truth and is honoured as standing (`thread_examencommissie_paula.md:41-42`, confirmed at `:98`).

- [ ] **I4-04 — Scope of the DCSC / S&C component** (`wayfinder:grilling`)
*Question: is the control-theory side a deliverable of this thesis — system identification and data-driven control, properly argued and defended — or an interface to work owned by the S&C side that this thesis consumes but does not claim?*
- Status: Open. Dependencies: I3-01 (for who supervises it), but the scope question itself is answerable now.
- Evidence: already chartered as the **gating** question on a sibling map, and marked HITL there too — *"the agent must not answer this"* (`research/wayfinder/dcsc_thesis_relevance.md:22`), with the note that the answer sets the relevance criterion itself and therefore has the highest leverage on that map (`:24`). The controlling constraint is that the open-loop forward model is already the built baseline and the DCSC cluster pages publish **0/8** on each of state estimation, fluid/CFD, and MPC (`research/wayfinder/dcsc_thesis_relevance.md:15-16`). The project record also carries an explicit open-loop fallback if closed loop proves too costly (`thread_dylan_kalisvaart.md:95`).
- **This map does not duplicate the sibling map.** It carries the question because it is a destination-level decision; the 26-name membership matrix and the shortlist live in `research/wayfinder/dcsc_thesis_relevance.md`.

- [ ] **I4-05 — Meeting cadence with the TN-side supervisor** (`wayfinder:grilling`)
*Question: what frequency is actually committed to — weekly, fortnightly, or monthly — and who communicates it?*
- Status: Open. **Blocked by I3-01** (the cadence is owed to a specific person, and that person is the open question).
- Evidence: an explicit, unanswered request for concrete frequency commitments, on the grounds of a heavy upcoming period, asking what both parties expect (`thread_bijoy_bera.md:101-102`). The recorded intent to propose periodic rather than weekly is at `state.md:81` and `committee_candidates.md:59-60`. **No mail has been sent on this**, so per Rule 17 it is a 🔥 item, not a ⏳ row — the absence of a sent message is the reason the question is still open.

### Island 4 support ticket, filed separately because it is a coupling, not a committee question

- [ ] **I4-06 — Where does the PDC course track attach to this BEP** (`wayfinder:grilling`)
*Question: is the Process Dynamics & Control assignment a graded obligation that must be completed on its own terms, or is it the vehicle for the step-response benchmark and frequency-domain work the BEP needs — and does that change what we tell the course?*
- Status: Open. Dependencies: I4-04 (it depends on whether control-theory work is in scope for the thesis at all).
- Evidence: the assignment is 50% of the course grade with a stated submission cutoff and a separate oral-assessment window (`2_Courses/PDC/course_overview.md:235-238`); lumped-parameter identification is explicitly out of scope for the exam (`:243`). The benchmark target is well defined — `StepResponses.ipynb` cells 0–6 build the reference step response, cells 8/10/12/14 do the tangent-line FOPTD identification (`:126`) — and the recommended starting file is named (`:227-229`). But **the numeric bound on maximum multisine frequency is explicitly not yet derived**, and anyone quoting a Hz figure before the benchmark exists is quoting an unverified number (`:145-149`).
- Rule 38 note: the oral assessment date is an `[EVENT]`, not a cutoff; preparation must be finished before the submission date (`state.md:104`).

---

## 4. Not Yet Specified (The Fog of War)

Decisions we know are coming toward the destination but **cannot yet be formulated as precise questions**. Per the Fog Test: the question is not answerable now because the territory is unknown, not because it is hard. Fog is partitioned by island; it does not promote until the frontier advances.

### Island 1 fog
- **Periodic-excitation design as a deliverable.** Whether the multisine design becomes a thesis chapter depends entirely on I1-01 (is there a parameter basis?) and I1-09 (is the transport model reduced enough to be linearisable?). Cannot be stated as a question until both land.
- **The PSSA sensitivity comparison.** The benchmark is specced (`dynamic_kinetics_berger2008.md`, direct action item 3) but its *acceptance threshold* depends on the kinetic parameter set, which does not exist yet.
- **Grid/quadrature convergence as a thesis section.** D4 establishes an `O(dr)` bias of 16% at `N_r = 10` (`3_Model/state.md:62`); whether a convergence study is a reported result or an internal fix depends on I1-07's reporting gate.
- **The exothermic branch's modelling detail.** The scope question is answerable now (I1-09 adjacent, FW-13), but *which* lumped energy balance, coupled to *which* Prater test, is not formable until the scope decision is made.

### Island 2 fog
- **CI, deployment and archival policy.** Entirely downstream of I2-01. Cannot be specified while the canonical tree is undetermined — a CI pipeline must know what it is building.
- **Bibliography as single source of truth.** The repo declares Zotero as the source exporting into `references.bib` (`conventions.md:139`), and the sanitisation requirement is documented (`Methanol-Catalysis/BEP_SOURCE_MAP.md:31`). **How** to make that airtight across two trees cannot be specified before I2-01 decides whether there are two trees.
- **Whether the interactive/web artefact is a deliverable at all, or only the PDF.** Depends on the same boundary decision.

### Island 3 fog
- **Poster-board reprint logistics.** We know a poster exists and cannot be silently corrected (`thread_els_arkesteijn.md:27`, `state.md:38`). Whether a reprint is even possible, and on what lead time, is not on disk and cannot be asked until the bio content is fixed under I3-01.
- **The exact form-submission sequence** once a construction is chosen: the three-months-before deadline exists (`committee_candidates.md:8`) but the target end date is not fixed anywhere in the map, so the submission date cannot be computed.
- **Lab Servant / campus-card sequencing.** Strictly ordered after the form is in (`thread_els_arkesteijn.md:65-67`), so nothing about it is askable yet.

### Island 4 fog
- **The DCSC contact shortlist.** Cannot be finalised before I4-04 sets the relevance criterion; the sibling map already says the criterion depends on the scope answer (`research/wayfinder/dcsc_thesis_relevance.md:33`).
- **Whether a face-to-face meeting with the opleidingsdirecteur is the right instrument.** Named as the route (`thread_carlas_smith.md:50`, `state.md:80`) but its content depends on I3-01/I4-01.
- **Whether a second S&C-side examiner is needed at all**, as distinct from the current candidate. Raised by the candidate himself (`thread_carlas_smith.md:92`) but not formable until slot *d*'s requirement is settled under I4-01.
- **Whether the standby extra-supervision dossier is ever activated.** One additional supervision dossier is on file as standby, to be activated only if extra mathematical-inversion supervision is needed (`committee_candidates.md:115-116`). There is no open question about it today — it is a contingency with no trigger, and whether it activates is a *consequence* of I4-01, not a question that can be asked now.

---

## 5. Out of Scope

Work and directions explicitly excluded from this destination, each with one reason.

1. **Writing the transient PBR model.** This map decides *what the model must be true of*; it does not write it. D1–D3 fixes are determined corrections (`3_Model/state.md:59-61`), not decisions — they live in `3_Model/state.md`, not here.
2. **The Larsen Appendix E/F image reads themselves.** I1-01 and I1-02 are the decisions those reads inform. The reads are a mechanical route already specified at `conventions.md:214`.
3. **Fixing the `13` vs `14` count in `state.md`.** I1-10 identified it and the answer; the edit was a state-engine mutation this map is **not authorised to perform** — *resolved 2026-10-18 by the authorised state owner (`state.md:112` → 14).*
4. **Any mutation of the external `Methanol-Catalysis` repository.** Read-only reconnaissance only. No write, no commit, no stash — the dirty tree was left exactly as found.
5. **Pushing, publishing or deploying anything.** `Methanol-Catalysis/AGENTS.md:11-20` reserves this to an explicit in-turn instruction naming act and branch; `:23-30` states a task needing a push is a blocked task.
6. **Re-planning author and project metadata.** Already personalised (`Methanol-Catalysis/myst.yml:4`, `:8`, `:9`; `authors.yml:11-28`); the remaining chore is at `state.md:97`.
7. **Naming the supervisor, or picking a side among the four conflicting lines.** Rule 41. This map records that four lines exist and that the user owns the answer (I3-01). It does not name anyone.
8. **Re-anchoring the expired `2026-09-29` date.** Rule 38 and `state.md:13`. I3-05 poses the decision; this map does not roll the date forward.
9. **Reusing the six withdrawn Larsen parameter values.** Vetoed (`conventions.md:195-206`, `state.md:25-26`) — and equally, this map does **not** call them fabricated (`conventions.md:206`, `state.md:26`).
10. **Using `bep_example_index.md` as a parameter or fact source.** Demoted at `conventions.md:227-234`, vetoed at `state.md:27`.
11. **The Dynamic Hypertext Dashboard and the Knowledge-Graph pilot.** Both are `[IN PROGRESS]` tooling tracks (`state.md:94-95`), not decisions on the route to a defended thesis. The KG's `llm_inferred` provenance rule is already settled (`conventions.md:186`, `:196`) and needs no ticket.
12. **The Urakawa group-agenda ICS subscription.** An admin convenience at `[LOW]` (`state.md:96`), blocked by a tenant restriction unrelated to any decision on this destination.
13. **Unrelated course and job tracks carried in the root `task.md`.** The PDC track is included (I4-06) because it couples to the thesis; everything else in `task.md` outside `Academics/BEP/Catalysis/` belongs to other destinations.
14. **`DOCUMENT_MAP.md`.** It is a **document index** (`DOCUMENT_MAP.md:1`, `:15`) and already exists. Not duplicated here and not treated as a decision map.
15. **The sibling DCSC map's contents.** `research/wayfinder/dcsc_thesis_relevance.md` is its own destination with its own islands. I4-04 carries only the destination-level scope question that both maps share.

---

*Provenance: every `file:line` below was read in this session. External-repository lines (`Methanol-Catalysis/…`) were read via `bash`, because that path lies outside the workspace root and the `read` tool blocks there; the repository was left untouched — 6 modified tracked files and 11 untracked paths, exactly as found. Workspace-internal paths were read relative to the workspace root (Rule 37). No state-engine file was created, edited, or deleted by this task, and no git write command was run.*


## Focused delivery map: Wednesday presentation

The thesis-wide map above tracks decisions toward the defended BEP. The near-term presentation has its own bounded map and is not a substitute for this thesis-level destination:

- [Wednesday presentation Wayfinder — 14 October 2026](bep_presentation_2026_10_14.md)
- [Captured user planning dump](user_dump_capture_2026_10_13.md)
- [Wednesday research dossier](../dossiers/scientific_wayfinder_2026_10_13/README.md)
- [Scientific method-selection map](scientific_method_selection.md)
- [BEP Catalysis navigation hub](../../README.md) · [Master document map](../../DOCUMENT_MAP.md)


## Focused scientific follow-up map: dynamic numerical accuracy / attenuation

The thesis-wide destination remains unchanged. The numerical-accuracy questions are recorded as a focused, **parked** submap; creating the map does not assign work or raise priority:

- [Dynamic numerical accuracy / attenuation — parked decision map](bep_dynamic_numerical_accuracy.md)
- [Reconsolidation capture: raw user thoughts, evidence boundaries and approval log](../notes/reconsolidation_capture_2026-10-16.md)

