# BEP scientific knowledge notes

This folder organizes selected scientific reasoning already present in the BEP record. It is a synthesis layer; the pinned source archive and lossless task ledger remain the provenance layer.

## Reading labels

- **Owner statement or direction** means the source record attributes the wording or choice to the owner. A dated handoff can still be an agent's summary of that statement.
- **Recorded decision** means a source explicitly records a choice. It does not imply that every later model or map adopted it.
- **Source audit** means an existing dossier reports a passage check or execution receipt. This consolidation did not repeat that source extraction or run.
- **Agent interpretation** means an AI-authored synthesis, proposal, or map entry. It is not owner understanding or approval.
- **Hypothesis / unresolved** means the question remains open. Do not rewrite it as a result.

Nothing in this folder changes the personal map, review queue, AI reference datasets, source approval states, or thesis scope.

## Theme index

| Theme | Start here | Main cross-references |
|---|---|---|
| Reaction network and catalyst surface chemistry | [Reaction chemistry](reaction-chemistry.md) | [R1–R3 source-evidence note](../../planning/source-snapshots/aapm-pr-182/Academics/BEP/Catalysis/research/wayfinder/bep_reaction_pathway_evidence_2026_10_22.md); [owner review handoff](https://github.com/AsapLoso/BEP-Catalysis/blob/4a419354837486f65e00f26236826125b97e9b5b/research/manual_map_sessions_2026_10_22/owner_working_map/OWNER_REVIEW_GATE_HANDOFF_2026_10_23.md) |
| Kinetic closures and parameter provenance | [Kinetics and parameters](kinetics-and-parameters.md) | [framework audit](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md); [Schbib benchmark audit](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/research/reports/schbib_parameter_and_benchmark_audit.md) |
| Reactor balances, transport, and assumptions | [Reactor transport](reactor-transport.md) | [scientific method selection](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/scientific_method_selection.md); [19 October owner-direction handoff](../../planning/source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/notes/session_handoff_radial_notebook_and_parallel_work_2026_10_19.md) |
| Numerical implementation and notebook history | [Numerics and notebooks](numerical-and-notebooks.md) | [model verification milestones](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/notes/model_verification_milestones.md); [benchmark notebook index](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/notebooks/benchmarks/README.md) |
| Periodic operation, CO modulation, and hypotheses | [Periodic operation](periodic-operation.md) | [proposal-derived periodic outlook](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md); [V4 reactor wayfinder](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/research/wayfinder/bep_v4_reactor_model.md) |
| Owner decisions and supervisor deliverables | [Decisions and deliverables](decisions-and-deliverables.md) | [reconsolidation capture](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/notes/reconsolidation_capture_2026-10-16.md); [meeting transcript](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/research/notes/meetings/2026-10-23_supervisor_meeting.md) |

Use the [open-question and contradiction register](open-questions.md) for unresolved scope and evidence conflicts, the [source-access record](source-access.md) for what was available on this PC, and the [handoff](HANDOFF.md) for the preserved state and next review points.

## Existing indexes and maps

- The lossless archive and its navigation are in [planning/README.md](../../planning/README.md), [the source catalogue](../../planning/CATALOGUE.md), [the coverage ledger](../../planning/backlog/SOURCE_COVERAGE.md), and [the conflicts and gaps record](../../planning/backlog/CONFLICTS_AND_GAPS.md). The 2,471 clusters and 2,940 raw occurrences are not repeated here.
- The personal map and review queue are on the migration snapshot at commit `4a419354837486f65e00f26236826125b97e9b5b`: [current map](https://github.com/AsapLoso/BEP-Catalysis/blob/4a419354837486f65e00f26236826125b97e9b5b/research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml), [action queue](https://github.com/AsapLoso/BEP-Catalysis/blob/4a419354837486f65e00f26236826125b97e9b5b/research/manual_map_sessions_2026_10_22/owner_working_map/ACTION_QUEUE_2026_10_22.md), and [migration provenance](https://github.com/AsapLoso/BEP-Catalysis/blob/4a419354837486f65e00f26236826125b97e9b5b/MIGRATION_STATUS.md).
- The independent and integrated AI reference maps remain separate at [independent reference v2](https://github.com/AsapLoso/BEP-Catalysis/tree/4a419354837486f65e00f26236826125b97e9b5b/research/independent_reference_map_2026_10_21) and [integrated reference map](https://github.com/AsapLoso/BEP-Catalysis/tree/4a419354837486f65e00f26236826125b97e9b5b/research/integrated_reference_map_2026_10_22). Their claim/source status is not owner verification.
- Current notebook and benchmark references were read from the local `unified-reactor-model` ref at `884a5303adf112941b180cc7191cf8ef3c8604f7`. They are cross-references, not content copied into this archive-lineage branch.

## Branch proposal and integration rule

This work is staged on `bep-knowledge-consolidation-20261028`, based on the locally available dump ref `origin/bep-lossless-task-union-20261023` at `3f1bdde20f391678e3393ace63bc7e5799e74fbc`. The historical dump branch and its source snapshots remain unchanged.

Suggested follow-up topic branches, if later work needs independent review:

1. `bep-theme-chemistry-kinetics` for reaction pathways, catalyst-specific rate laws, and parameter provenance.
2. `bep-theme-reactor-model-verification` for transport assumptions, balance equations, numerical behavior, and notebook evidence.
3. `bep-theme-periodic-operation` for acetylene-feed and CO-modulation hypotheses, objectives, and experimental comparison.

These topic branches are proposals only. The notes share source boundaries and are reviewed together in this first pass. Any later selective integration should start from the chosen target base and carry only the specifically reviewed files or isolated content commits. Do not merge a dump-lineage branch directly into `main`; nothing is promoted automatically.

## Work not performed

No notebook or simulation was run, no literature passage was re-extracted, no software tests were added or run, no map file or approval state was changed, no remote synchronization was attempted, and nothing was merged or pushed.
