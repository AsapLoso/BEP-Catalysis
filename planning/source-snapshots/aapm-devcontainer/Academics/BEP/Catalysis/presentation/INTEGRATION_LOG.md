# Presentation integration log

## 14 October 2026 — first presentation checkpoint

- Initial refresh found source-map/index snapshot 17df41b14fceaeccf3ee2339d8e9fecc3e7c3eb6 (“Cross-link BEP concise identification sub-story with B/D/E evidence”).
- Read the current [presentation structure](PRESENTATION_STRUCTURE.md), [A–M research index](RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md), completed deep dives B–E, sub-stories 01–04, the earlier Wednesday plan, current README and notebook prototypes, plus the legacy mini-deck and speaker notes.
- Used the existing mini-deck’s spacious dark 16:9 stage and restrained mint/coral diagrams as visual inspiration. Reused its bed/pellet visual language selectively; the new deck has its own inline diagrams and does not rely on those prototype files.
- Consulted [Guy’s presentation skill](https://github.com/guy915/presentation-skill) as inspiration for a short throughline, one main point per slide, evidence-first claims, and offline presentation. No code, runtime, or assets were imported.
- Built the story around the research question, selectivity competition, two distinct meanings of dynamic, the legacy 1,480-coordinate scaffold, the source-backed reacting PSSA slice, evidence boundaries, a fair future periodic comparison, and the noiseless-first identifiability hypothesis.
- Reconciled the older evidence README’s 11/12 coverage statement against the implementation receipt and current research index, which support 10/12. The two H₂ values are recorded in the claim checklist. The scientific source file was not modified.
- Deliberately omitted model-output snapshots with incomplete standalone provenance, the conditional 0.12% external-film screening, and any periodic-yield benefit claim.
- Final refresh found current devcontainer commit 3941f4f583123e216461e4f0d45b6ef326638b23 (“Register F scientific conservation audit and cross-link presentation sources”) and a new completed F deep dive. The source map now records B–F as complete.
- Integrated F’s count correction: 140 of the legacy model’s 1,480 allocated entries are fixed, artificially set, or algebraically constrained; the other 1,340 receive assigned derivatives but are not proven independent physical modes. Added the newer PSSA slice’s 240-entry uniform default and 2,400-entry radial option.
- Integrated F’s conservation question as an **unverified closure concern**, not a reproduced numerical defect: resolved radial bulk–pore paths may book reaction sources in both inventories without explicit interfacial-flux coupling. F is a mathematical/code audit, not an executed nonzero-kinetics conservation residual. The reduced uniform PSSA closure has a different model structure.
- Updated the next-test slide to include balance and interfacial-flux checks before any radial-path performance comparison. No model code or deep-dive source was modified.
- Rendered and inspected all nine slides at 1920×1080 and 1366×768. Keyboard navigation, cue-panel toggle, no external asset/network requests, and a nine-page 16:9 PDF passed. A compact-height overflow found on slide 3 was corrected and rechecked.

## Update procedure

This branch does not need continuous fetch/pull updates. Before a meaningful presentation checkpoint, fetch devcontainer once, inspect its commit list and changed research files, reread the index/source map, then update the affected slide, outline, notes and claim ledger together. If a new source conflicts with a slide, record the conflict here and in the checklist before changing the claim.

Next likely integration points:

- New A–M findings on numerical verification and observed model results (especially G, I, J and K), plus execution of F’s proposed conservation residual check.
- A reproducible, pinned run of the newer PSSA slice with its dependency and reviewed operating conditions.
- Full-text and SI verification for Urmès 2022, which may change the literature framing or identifiability context.
- Any experimentally grounded parameter or catalyst-transfer result, which could alter the model comparison and periodic test design.

## 14 October 2026 — completed session checkpoint

- User requested a coherent story in **bullets with short elaboration**, then an editable text document (DOCX). Replaced the earlier minimal outline with ten linked sections: research question → nonlinear chemistry and internal state → both model approaches → kinetic information → numerical fidelity → evidence → future comparisons.
- Refreshed and merged current `devcontainer` research through `996781c`. Read completed G, optional narrative 05, K's result-status note and the newly arrived L outlook. Deep-dive documents were incorporated from upstream without rewriting their scientific content.
- G adds spatial-versus-temporal distinctions, stiffness/cost questions and a defined analytic transport example. K excludes diagnostic conversion/selectivity values from presentation findings. Narrative 05 is only a short transition inside the newer-model slide; no separate I research section was added.
- L adds a meaningful distinction between a same-mean steady comparison and comparison with the best admissible steady operating condition. Included this in the final outlook and its context; candidate objectives and constraints remain open.
- Rebuilt the deck as a fixed 16:9 stage with inline diagrams. Preserved the dark navy/mint/coral visual reference. No model-output curves or invented periodic gains were added.
- The user requested the **shift** on slide 8. Added an analytic zero-crossing zoom: lag 358.692644° versus ideal 360°, a 1.307356° phase lead error at unchanged forcing frequency. The example assumes exact time integration; frequency drift or time-integrator error is not fabricated. Forward Euler's pure-advection CFL=1 exception remains explicit.
- Primary document is now `BEP_Presentation_Outline.docx`: actual editable Word paragraphs, 30 native bullets and zero images. Markdown, HTML and PDF versions share the same content. Speaker cues remain short prompts.
- Centralized editable text and source pointers in `presentation_content.json`, with deterministic deck/document generators. Updated the claim ledger and figure provenance.
- All ten slides inspected, including a second independent review and a focused review of the phase inset. Rendered the complete deck at 1920×1080 and 1366×768, checked ten-page 16:9 PDF and native DOCX export. Isolated single-file renders match byte-for-byte with networking disabled; managed-browser file-protocol limitation is documented in `QA_REPORT.md`.
- No scientific question, Zoë communication, physical model validation, periodic performance comparison or parameter-recovery task is marked completed by this presentation checkpoint. Existing open scientific tasks remain open.

## 14 October 2026 — session audit and editorial review sync

- Re-read the current GitHub state before writing the retrospective. The presentation PR remains open and unmerged. The deck's last complete scientific snapshot is 996781c; devcontainer has since added M, an editorial reading of PR #4, but no newer scientific deep dive that changes the claims in the deck.
- M agrees with the throughline—question, physical state, balanced old/new model attention, numerical fidelity, evidence boundary, and a testable next comparison—while preserving owner choice. It flags potential compression of slides 3/4 and 5/6, asks whether optional narrative 05 belongs, and recommends keeping slide 10 focused on the performance comparison. These are now recorded as open review decisions in state.md, the presentation Wayfinder and the [session audit](../research/dossiers/presentation_checkpoint_audit_2026_10_14.md); they were not silently applied.
- The user’s feedback explains the final handoff: the outline grew from a thin skeleton into an editable Word document with meaningful bullets and brief context; the deck remained visual rather than becoming a written speech. The slide-8 “shift” is expressed as a phase/zero-crossing difference under the stated exact-time pure-advection assumptions; no frequency drift is claimed. If the request meant a time-discretization-induced frequency change from a common starting point, that effect remains unillustrated and is now an explicit review question.
- QA establishes slide rendering, navigation, offline self-containment and document editability. It does not establish model accuracy, physical validity, calibration or periodic-yield improvement.
- Updated the active state and Wayfinder so the completed production sprint is no longer described as still underway. Owner review and F/G scientific discussion remain open.
