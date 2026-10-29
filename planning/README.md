# AAPM BEP — planning maps and checklists (historical imports)

This directory preserves the **existing decision maps, work maps, checklists, reviewer queues and supporting status records** from AAPM, before attempting to unify them.

**Phase 1 is deliberately mechanical**: do not update statuses, accept unreviewed claims, deduplicate competing research decisions, or treat merged and unmerged AAPM material as equivalent. **Exception:** local Windows user-home and program-file path prefixes were replaced with placeholders in 16 files for repository hygiene; the exact source originals remain available through the pinned GitHub URLs and original blob hashes in the manifest.

- [Full source file catalogue](CATALOGUE.md) — 119 files with original snapshot links
- [Machine-readable file manifest](SOURCE_MANIFEST.json) — pinned commits and copied blob hashes
- [Cross-repository source map](SOURCE_MAP.md) — branch ownership, navigation, and coverage limits
- [Suggested later consolidation procedure](INTEGRATION_PLAN.md) — *not executed by this PR*

## Important starting points

| Need | Start at |
|---|---|
| BEP master decisions and four islands | [BEP Master Wayfinder](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/bep_catalysis_master.md) |
| Scientific model alternatives | [Scientific Method Selection](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/scientific_method_selection.md) — note alternative on [unmerged PR #50](source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/wayfinder/scientific_method_selection.md) |
| Numerical accuracy and reactor limitations | [Dynamic Numerical Accuracy](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/bep_dynamic_numerical_accuracy.md), [14-item model audit](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md) |
| What has or has not been verified | [Verification milestones](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/notes/model_verification_milestones.md) |
| 47 reactor recovery questions | [Reactor recovery register (PR #50)](source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md) |
| Guided notebook delivery | [Notebook Wayfinder (PR #50)](source-snapshots/aapm-pr-050/Academics/BEP/Catalysis/research/wayfinder/bep_reactor_notebook_delivery_2026_10_19.md) |
| Personal-map 69-checkpoint plan | [Map taxonomy and review checklist](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/notes/bep_ownership_mindmap_taxonomy_2026_10_20.md) |
| Frontend architecture and remaining work | [Map development Wayfinder](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/bep_ai_mindmap.md), [frontend work goal (PR #186)](source-snapshots/aapm-pr-186/Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/FRONTEND_WORK_GOAL_2026_10_22.md), [export TODO (PR #199)](source-snapshots/aapm-pr-199/Academics/BEP/Catalysis/mindmap/FUTURE_FRONTEND_EXPORT_TASK_2026_10_23.md) |
| Literature and scientific citation campaign | [Integrated science campaign (PR #180)](source-snapshots/aapm-pr-180/Academics/BEP/Catalysis/research/wayfinder/bep_integrated_scientific_campaign_2026_10_22.md), [reaction evidence map (PR #182)](source-snapshots/aapm-pr-182/Academics/BEP/Catalysis/research/wayfinder/bep_reaction_pathway_evidence_2026_10_22.md) |
| Damian and Zoë | [Damian Wayfinder](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/damian_briefing_2026_10_09.md), [October 19 checklist](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/briefing/damian_checkin_checklist_2026-10-19.md), [deck open questions](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/presentation/DECK_OPEN_QUESTIONS.md) |
| Admin and dual-degree governance | [TW3 committee map](source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md), [SysCon state](source-snapshots/aapm-devcontainer/Academics/BEP/SysCon/state.md) |
| How to interpret the source Wayfinders | [Original Wayfinder skill](source-snapshots/aapm-devcontainer/.agents/skills/wayfinder/SKILL.md), [original follow-up rules](source-snapshots/aapm-devcontainer/.agents/skills/follow-up/SKILL.md) |

## Ownership and status rules

1. A historical checked box is evidence of a prior recorded state, not independent verification that its action was actually completed.
2. A draft/open AAPM PR is a source snapshot, not an integrated canonical scientific decision.
3. The owner-approved personal understanding map is **not** automatically updated from AI research or the reference map. Approval, comprehension, and citation verification are distinct.
4. Numerical code passing tests is not equivalent to source-matched results or experimental validation.
5. AAPM remains the provenance archive; all future changes to the new BEP work plan should be intentional and separately reviewed.
