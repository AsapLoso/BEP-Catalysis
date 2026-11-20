# Handoff — BEP presentation checkpoint

_Updated: 2026-10-14_

## Resume here

The first research-progress presentation is complete as a reviewable draft. The canonical project tracker remains [`../state.md`](../state.md); this handoff is scoped to the presentation work. Start with the [presentation README](README.md), then read the [session audit](../research/dossiers/presentation_checkpoint_audit_2026_10_14.md) for the narrative rationale and evidence boundaries.

- **Repository:** `AsapLoso/project-management-agents`
- **Branch:** `codex/bep-presentation-2026-10-14`
- **Review:** [PR #4 against `devcontainer`](https://github.com/AsapLoso/project-management-agents/pull/4), open and unmerged at the time of this handoff.
- **User review is still needed:** the deck is a draft, not an approved final talk. Keep the research branch and presentation PR distinct; do not merge without the owner's decision.

## Delivered files

- [Single-file offline HTML deck](BEP_Dynamic_Acetylene_Progress.html)
- [Editable Word outline with text bullets and context](BEP_Presentation_Outline.docx)
- [Slide-by-slide Markdown outline](GLOBAL_PRESENTATION_OUTLINE.md) and [short speaker cues](SPEAKER_NOTES.md)
- [Claim/source checklist](CLAIM_SOURCE_CHECKLIST.md), [integration log](INTEGRATION_LOG.md), and [render/visual QA report](QA_REPORT.md)
- HTML and PDF reading versions of the outline, plus PDF export of the deck

## Story and evidence boundary

The red line is: research question → possible physical memory → two complementary model approaches → kinetic and numerical limits → evidence status → the comparison needed to test periodic operation fairly. The 1,480-coordinate scaffold and the newer reacting PSSA simulator have different physical ambitions and limitations; neither is presented as experimentally validated. No periodic ethylene-yield gain, parameter recovery, or completed matched-budget performance comparison is claimed.

The user's slide-eight clarification remains open: the intended effect is a different apparent frequency despite the same start point, caused by integration. The current slide instead shows a phase/time offset in a pure-advection example with exact time integration, so it does not yet depict that requested integration-induced frequency change. Resolve this before presenting the slide as satisfying the request.

## Next review items

1. Review the slide-eight interpretation and update the figure, explanation, outline, notes, and claim checklist together if needed.
2. Decide whether slides 3/4 and 5/6 should be condensed, whether optional narrative 05 belongs, and whether slide 10 should prioritize the periodic-performance test over the identifiability aside. See the open questions in the [project tracker](../state.md) and [deck register](DECK_OPEN_QUESTIONS.md).
3. Incorporate new research only when it changes a supported claim; check the source map and integration log first. The most consequential likely updates are F conservation, J numerical verification, K result status, a reproducible pinned PSSA run, and verification of the Urmès 2022 comparison.
4. The planned F/G discussion with Zoë remains unsent. Do not record it as sent or resolved until that happens.

## Clean-session status

At handoff, the presentation work and this note are committed to the presentation branch and pushed to GitHub. The local Git working tree is clean, the Git stash is empty, and no work is being kept only in an untracked local file. A future session should check the PR and current research index before editing, because parallel research may have advanced `devcontainer`.

This compact handoff follows the portability idea in the public [Handoff skill](https://github.com/kurosaki-sol/Handoff): keep a cold-start path and active work state in the project. Project-specific status remains governed by `state.md` and `history.log`.
