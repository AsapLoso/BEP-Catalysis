# Source access and coverage record

## Primary repository and Git refs

The primary working directory was on Windows at the BEP-Catalysis repository. Before writing, `git status` was clean on `unified-reactor-model`; `git fsck --full --no-reflogs` completed without object-corruption errors and reported three dangling commits. The C: volume reported about 163 GB free. The dangling commits were inspected and left untouched.

Available local refs at the start of the task:

| Ref | Observed commit | Use in this task |
|---|---|---|
| `origin/bep-lossless-task-union-20261023` | `3f1bdde20f391678e3393ace63bc7e5799e74fbc` | Staging lineage for this local knowledge-consolidation branch |
| `origin/migration/bep-map-consolidation-20261023` | `4a419354837486f65e00f26236826125b97e9b5b` | Read-only map, queue, handoff, and AI reference-map source |
| `origin/unified-reactor-model` | `884a5303adf112941b180cc7191cf8ef3c8604f7` | Read-only current notebook and benchmark cross-references |
| `origin/main` | `0cf25e8f055d056070b80663c188d44aa088a65b` | Target-base reference only; no merge performed |

The user identified dump PR #7 and map PR #1. Their private GitHub pages were not accessible: `gh` is not installed and the browser session showed a logged-out 404. No fetch or other synchronization was attempted, so current remote PR state is unknown.

## Existing archive and original project-management dossier

The dump branch contains the pinned archive catalogue, manifest, backlog coverage, conflicts, and source snapshots. The archive records 119 AAPM snapshot files from seven refs, plus supplemental map-branch evidence. I used the catalogue and source coverage to choose existing records rather than reproducing the inventory.

A local `AsapLoso/project-management-agents` checkout was also readable at `sync/20261018-bep-reconciliation`, commit `6cc49d86f8b5359a9f8826d36374ed3e29b727a1`. The dump’s scientific archive is pinned to the distinct AAPM `devcontainer` source snapshot `8c48cf8a5ba5b3d02dcd1787f98abcd65b34c5c8`; PR #50, #180, #182, #186, and #198 sources are retained under `planning/source-snapshots/`. The local checkout was read only.

Accessible conversation and handoff materials include:

- The archived [reconsolidation capture](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/notes/reconsolidation_capture_2026-10-16.md), which labels raw owner statements separately from AI inference.
- The archived [reactor-recovery thought capture](../../planning/source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/notes/user_thought_dump_2026_10_18_reactor_recovery.md) and [radial notebook handoff](../../planning/source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/notes/session_handoff_radial_notebook_and_parallel_work_2026_10_19.md).
- The local AAPM transcript `Academics/BEP/Catalysis/research/inbox/chatgpt_share_2026-10-19/transcript.md`, captured from a public share page. Its header excludes platform-hidden fragments; the saved record notes missing early assistant text and a truncated final utterance. It is not a complete ChatGPT history export.
- Gemini exports for the September 29 transient-model scaffold chats at `Academics/BEP/Catalysis/3_Model/gemini_transcript_2026-09-29.md` and `gemini_transcript_2026-09-29_83878835991845b5.md` in the local AAPM clone.
- The October 23 supervisor-meeting transcription in the local BEP-Catalysis repository, generated from audio using Gemini transcription. It is useful as a discussion record, not a primary scientific source.

## Maps and AI evidence

The migration branch was read without editing. It contains `MIGRATION_STATUS.md`, the owner `current_map.yaml`, `ACTION_QUEUE_2026_10_22.md`, the October 23 review-gate handoff, the independent reference map, and the integrated reference map with source-evidence ledgers. The map handoff says map maturity, owner reading, content approval, and source verification are separate fields. The integrated source-audit state reports zero human-verified claim/source links at its checkpoint.

## Methanol-Catalysis

The local `AsapLoso/Methanol-Catalysis` checkout was on `main` at `5785fa5f11289d72127457f9a3a25aa5c4e71be3`. I read its public-repository instructions, README, local-only `BEP_SOURCE_MAP.md`, and inspected the structure of `content/c2h2_hydrogenation_transient_model.ipynb` (11 cells: 5 code and 6 markdown). The notebook was not executed. The source map directs readers to private project-management records and consensus reports, warns that its synthesis is not a primary source, and says every thesis parameter must be checked against the paper. No file in Methanol-Catalysis was changed.

## Sessions and limits

The Agent Host listed four BEP-Catalysis workspace sessions, including this task. I could read partial context from two relevant prior sessions: `ahp-session:/2a08282b-fb6f-46a2-a997-45d71487c44c` (a branch and reference audit that distinguished planning-only workstreams from a branch removing V3 files, and raised personal-map review constraints) and `ahp-session:/e9f1214c-dcee-413e-ad5a-2128005f6f7a` (the unified notebook discussion, where an attached snapshot was empty and the repository notebook was described as placeholder pseudocode without executed cells). The session contexts are truncated and do not provide complete ChatGPT conversations.

No literature PDFs were reopened for this consolidation, no new source extraction or citation audit was run, no notebook or simulation was run, and no files in the supporting repositories were modified.
