# Wayfinder: Wednesday BEP Presentation — 14 October 2026

**Status:** The original provisional map now has a concrete first checkpoint: a ten-slide offline HTML deck, editable Word outline, cues, source ledger and QA report in [historical PR #4](https://github.com/AsapLoso/project-management-agents/pull/4), with its artifacts on `devcontainer`. The deliverable is usable for review but is not yet an owner-approved final talk and does not validate the reactor model. See the [session audit](../dossiers/presentation_checkpoint_audit_2026_10_14.md) and the later [M editorial review](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/presentation/deep-dives/M_editorial_synthesis_pr4_2026-10-14.md).

**Priority update (user-confirmed 2026-10-13):** This is the highest-priority active workstream, with a hard deadline of Wednesday 14 October 2026. Focus on scientifically defensible presentation deliverables and avoid infrastructure detours. This priority does not mark any open Wayfinder ticket complete or imply that a deck is ready.

## 2026-10-18 — gearchiveerd als event-record

- De kaartdatum (woensdag 14 oktober 2026) is verstreken. **Of het gesprek daadwerkelijk heeft plaatsgevonden is niet op schijf vastgelegd (UNVERIFIED).**
- De W-tickets worden niet als actief werk gemirrord; deze kaart blijft als historisch verslag staan. Live restpunten na de checkpoint-integratie zijn de owner-review en de F/G-discussievoorbereiding — beide nu `- [ ]` in [BEP state.md](../../state.md) §"BEP presentation — reconciled status".
- Classificatie: [map_state_crosswalk_2026_10_18.md](../notes/map_state_crosswalk_2026_10_18.md).

**START HERE for every contributing chat:** [repository-wide Wednesday entry point](../../../../../WEDNESDAY_START_HERE.md).  
**Hub:** [BEP Catalysis — Wednesday presentation hub](../../README.md)

## 1. Destination

The first checkpoint delivers a clear research story and an honest explanation of what the current model and code do and do not establish. The remaining destination is owner review, a decision on optional/compressed material, and any evidence-driven revision before the talk.

The user requested a self-contained HTML presentation with slide navigation and an editable text handoff. Both now exist as a first checkpoint. The actual audience, allotted slot, final content selection and ready-to-present criteria remain open. This is one presentation goal, distinct from the thesis-wide Wayfinder map and the scientific-method-selection work.

**Runbook:** [HTML slide-deck build and grade](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/.agents/resources/runbooks/html-slide-deck-build-and-grade.md).

## 2. Decisions and boundaries so far

- [x] **Presentation is a separate goal.** Do not conflate the Wednesday talk with completing or defending the full BEP thesis.
- [x] **Code must be explainable and defensible.** Show what is implemented, what is only proposed, and what has not been validated.
- [x] **Accuracy boundary.** The current research packet reports static code diagnostics; it does not establish a validated reacting-periodic prediction or measured yield improvement.
- [ ] **Format is not ratified.** Interactive HTML with next-slide navigation is the user's stated direction, but the delivery requirements and duration are not recorded.

## 3. Active frontier

### Audience and delivery

- [ ] **W1 — Audience and purpose** (wayfinder:grilling) — Who is the Wednesday audience, and what is the one thing they should leave understanding?
  - Status: Open; the draft opens with the periodic-feed question, but the target audience and intended takeaway still need owner confirmation.
  - Dependencies: None.

- [ ] **W2 — Duration and delivery format** (wayfinder:grilling) — How long is the presentation, and is the requested interactive HTML deck the required format?
  - Status: A concrete offline HTML/DOCX checkpoint exists and is allocated 9½ minutes; actual slot, rehearsal time and final delivery requirements remain open.
  - Dependencies: None.

### Scientific content and evidence

- [ ] **W3 — Evidence-backed content** (wayfinder:research) — *Which claims, equations, code findings, and figures are supported well enough to use, and what limitations must accompany them?*
  - Status: **Evidence map advanced; first claim set assembled.** The ten-slide draft checkpoint, now integrated into `devcontainer`, has a claim/source ledger and explicit boundaries. New M review is editorial, not a new scientific validation; source selection and final owner review remain open.
  - Dependencies: None for source inventory; selection depends on W1 and W2.
  - **Evidence update 2026-10-13 (executed, not read):** [`BEP_SUPERVISOR_BRIEFING_2026-10-13.md`](../briefing/BEP_SUPERVISOR_BRIEFING_2026-10-13.md) §7 splits the candidate content into "can appear on a slide" and "must not", each row tied to a source. Three new executed results back it:
    - `pixi run python 3_Model/probes/verify_urmes2019_source.py` → **24/24 PASS**, exit 0. The `pbr` Urmès2019 parameter set (8 constants + site density) matches the primary paper's Table 5, and the two LHHW rate equations match term for term including the $K_1/K_5$ factor. Also confirms the source's 1.26 bar operating pressure and its own published partial pressures. Receipt: `3_Model/probes/urmes2019_source_receipt.json`.
    - `pixi run python 3_Model/probes/verify_pbr_implementation.py` → **3/4 gates**, exit 1. GATE 1 **FAILS**: the rate law reproduces **10 of 12 numerical coverage-range checks** (four operating-point/temperature rows × three species). The same $\theta_{H_2}$ discrepancy at operating condition 1 (0.00181 against a published lower bound of 0.00200) fails at **both 51 °C and 62 °C** at 1.26 bar. These are not 12 independent experimental validations. GATE 1b/2/3 pass and reproduce three `pbr` defects, including its feed conversion inflating every reactive partial pressure by 33 %. Receipt: `3_Model/probes/pbr_implementation_receipt.json`.
    - `pixi run python 3_Model/probes/audit_2026_09_30.py` → all six defects D1–D6 reproduce on this machine today. Raw output: [`evidence/audit_2026_10_13.txt`](../briefing/evidence/audit_2026_10_13.txt).
    - The `pbr` test suite was **executed** for the first time: **37 passed** ([`evidence/pbr_pytest_2026_10_13.txt`](../briefing/evidence/pbr_pytest_2026_10_13.txt)). The commit message's claim is now a result.
  - **Correction produced by this ticket:** the Urmès **2022** periodic-operation paper (DOI 10.1002/cctc.202101826) is **not on disk**; the Urmès **2019** paper that *is* on disk is a different paper (steady-state kinetics, not periodic operation). It is the parameter source, not the periodic comparator. Earlier records that treated one as the other are corrected in the briefing §2.2 and [`evidence/README.md`](../briefing/evidence/README.md) §3.
  - **Limitation carried forward:** the coverage reproduction is a parameter-transfer check on one rate law at four steady operating points. It is **not** reactor validation, and the briefing says so wherever the result appears.
  - **[FACT: GitHub checkpoint 2026-10-13 22:12 CEST]** Development is not completely idle: branch [`hermes/reacting-vertical-slice-2026-10-13`](https://github.com/AsapLoso/project-management-agents/tree/hermes/reacting-vertical-slice-2026-10-13) contains unmerged commit [`1c0609ac`](https://github.com/AsapLoso/project-management-agents/commit/1c0609ac08d7923032e200cf157653029c10b179) (21:57 CEST), adding a reacting-reactor script and analytic-Jacobian note. This is source code, **not a verified reacting-run result**: the commit contains no run receipts or generated figures. Its runtime import points to local `pbr/` sources not tracked in either this repository or the public `AsapLoso/Methanol-Catalysis` main branch. No claims or curves from this branch are yet authorized for the talk. The corrected 10/12 count above was checked against committed `3_Model/probes/pbr_implementation_receipt.json`; earlier 11/12 wording in the supervisor handoff remains superseded.


- [ ] **W4 — Content priority** (wayfinder:grilling) — Which findings and limitations deserve the presentation's limited time?
  - Status: A provisional ten-slide story exists. Owner selection remains open; M suggests possible condensation and flags optional narrative 05 as unselected.
  - Dependencies: W1, W2, W3.

- [ ] **W5 — Narrative** (wayfinder:grilling) — In what order should the selected material be presented so the audience can follow the motivation, model, evidence, and limitations?
  - Status: A coherent draft arc is written; acceptance and possible slide compression remain open.
  - Dependencies: W4.

### Visuals and readiness

- [ ] **W6 — Visual approach** (wayfinder:prototype) — Which visual treatment best explains the selected story, including whether notebook-derived visuals or interactive elements help?
  - Status: Open; next-slide navigation is a preference, not a finished prototype.
  - **User update 2026-10-13:** The prior HTML/notebook prototypes are visually unsatisfactory; the next deliverable must be an actual coherent, polished, sendable slide deck rather than another concept note or notebook demo. Guy's [external presentation-skill](https://github.com/guy915/presentation-skill) was shared as a possible reference but is not installed; reuse the existing [HTML deck runbook](../../../../../.agents/resources/runbooks/html-slide-deck-build-and-grade.md) and do not block delivery on integration.
  - Dependencies: W4, W5.

- [ ] **W7 — Ready-to-present standard** (wayfinder:grilling) — What must be complete for the presentation to count as ready, including a speaking script and any live demonstration?
  - Status: Open.
  - Dependencies: W2, W5, W6.

## 4. Items from the user's dump

| Item | Current state | What remains |
|---|---|---|
| Brain dump and source capture | Older BEP brain-dump notes and conversation records exist in the repository; this map captures the new Wednesday dump. | Reconcile the new dump with evidence. Older notes contain hypotheses that later research does not establish. |
| Multiple chats / three screens | A 2026-10-12 handoff proposes separate research, presentation, and infrastructure lanes. | The current chats have not been assigned or coordinated here; treat the split as a suggestion. |
| Papers into a knowledge base | The GitHub repository has literature catalogues; a substantial literature synthesis is in the local research packet. | Select the final sources and claims for these slides; the newest packet is local-only. |
| Jupyter notebook and simulation | The repo has model code and earlier audits; the local packet adds a corrected static review. | Static review is not a validated simulation. The notebook path from the local snapshot is not in the linked GitHub project; confirm the exact notebook before using it. |
| Simple implementation | Existing code and a newer local implementation candidate have been inspected. | No implementation has been selected, repaired, or verified for this presentation. |
| Interactive HTML slides and speaker material | Ten-slide offline HTML checkpoint, editable DOCX outline, concise cues and source ledger exist on `devcontainer`. | Owner review, actual timing/audience confirmation and any evidence-driven revisions remain open; no written speech or live demonstration is assumed. |
| Control-theory overlap | DCSC and wind-control research leads exist. | Optional context, not a blocker; include only if it supports the selected story. |
| WhatsApp message to Guy | Captured from the user's dump. | Completion is unknown; this is a separate personal action. |

## 5. Cross-linked index of material

- [Captured user dump (13 October)](user_dump_capture_2026_10_13.md)
- [Research dossier overview](../dossiers/scientific_wayfinder_2026_10_13/README.md)
- [Dossier handoff](../dossiers/scientific_wayfinder_2026_10_13/wednesday_handoff.md)


### Adjacent maps and evidence

- [Scientific method-selection Wayfinder](scientific_method_selection.md) — thesis-method decisions and evidence questions; distinct from presentation readiness.

### 2026-10-13 research dossier

The full curated dossier and audit receipts are now preserved in this repository:

- [Literature and reusable methods](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md)
- [Simulator and numerics review](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md)
- [Source-coverage audit](../dossiers/scientific_wayfinder_2026_10_13/source_coverage_audit.md)
- [Scope and source provenance](../dossiers/scientific_wayfinder_2026_10_13/scope_provenance.md)
- [Alternate implementation review](../dossiers/scientific_wayfinder_2026_10_13/alternate_implementation.md)
- [Full dossier index and handoff](../dossiers/scientific_wayfinder_2026_10_13/README.md)

### GitHub repository

- Project landing page: [BEP Catalysis README](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/README.md)
- Navigation: [BEP Catalysis document map](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/DOCUMENT_MAP.md)
- Current status: [BEP Catalysis state](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/state.md)
- Separate long-term map: [BEP Catalysis master Wayfinder](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/research/wayfinder/bep_catalysis_master.md)
- Earlier presentation discussion: [12 October conversation handoff](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Technical_setup/Machine_Infrastructure/research/chatgpt_handoffs/2026-10-12/wayfinder_presentation_conversation_handoff_2026-10-12.md) · [archive index and provenance caveats](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Technical_setup/Machine_Infrastructure/research/chatgpt_handoffs/2026-10-12/INDEX.md)
- Existing presentation sub-stories (drafts): [01 — Three concentrations to state space](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/presentation/sub-stories/01_three_concentrations_to_state_space.md) · [02 — Proposal to predictive optimization](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/presentation/sub-stories/02_proposal_to_predictive_optimization.md)
- Reusable visual segment from recent commits: [five-slide HTML mini-deck](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/presentation/BEP_transient_state_mini_deck.html) · [speaker notes](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/presentation/BEP_transient_state_speaker_notes.md)
- Archived older brain dump: [BEP brain-dump notes](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/0_Project_Management/archive/transcripts/brain_dump_notes.md)
- Code and prior records: [transient model source](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/3_Model/c2h2_hydrogenation_transient_model.py) · [model state/defect register](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/3_Model/state.md) · [framework audit](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md)
- Control-theory context: [DCSC research exploration](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/research/dcsc_research_exploration.md)

## 6. Fog of War and out of scope

- Research topics that emerge after the presentation story and code evidence are reconciled.
- Whether the broader control-theory overlap belongs in this talk; it is not assumed to be necessary.
- Completing the full thesis, selecting the final reactor methodology, or implementing a new full simulator.
- Claiming a validated simulator, measured yield gain, or validated periodic prediction without evidence.

