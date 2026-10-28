# Notebook workspace

This folder separates the notebook you are actively developing from archived implementations and benchmark work.

## Personal work

- [unified_dynamic_reactor.ipynb](./unified_dynamic_reactor.ipynb) is the personal working notebook and the default notebook to edit.

## Reference implementations

- [reference/](./reference/README.md) indexes the preserved implementations and proposals.
- [reference/v3/](./reference/v3/) contains the V3 vertical slice and its pinned environment. It is a separate implementation for study, not the personal working notebook.
- [reference/v4/](./reference/v4/README.md) contains the V4 dynamic CO model snapshot and its isolated engine copy. It is a reference implementation, not the personal working notebook.
- [reference/legacy/](./reference/legacy/) contains older reactor-model artifacts.
- [reference/ai/](./reference/ai/) and [reference/snapshots/](./reference/snapshots/) hold AI proposals and saved drafts, with provenance described in the reference index.

## Benchmarks

- [benchmarks/](./benchmarks/README.md) indexes the historical V1/V2 snapshots and the imported Schbib (1996) and Larsen (2024) benchmark work.
- Audit reports, source transcriptions, and derived tables are indexed under [research/evidence/](../research/evidence/README.md) and [research/reports/](../research/reports/README.md).

See [research/](../research/README.md) for literature, model specifications, audit records, meeting notes, prompts, and planning maps.

## Owner-led science workflow

[`bep-guided-science-loop`](../.agents/skills/bep-guided-science-loop/SKILL.md)
governs discussion, *incremental approved map updates*, and eventual
implementation in this personal notebook. Reference output and passing
tests are not proof of experimental validity or owner understanding.
The owner map may be on another approved branch: verify before editing.
[Backend requirements](../research/workflows/bep_conversational_map_backend.md)
are specified, **not yet tested as a live editor**.
