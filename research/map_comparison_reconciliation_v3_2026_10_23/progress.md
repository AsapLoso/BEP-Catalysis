# Scientific research progress — map reconciliation v3

**Date:** 2026-10-23  
**Status:** AI-authored provisional map increment; review-only and unmerged. No owner choice was made or requested for this pass.

## Starting point and preservation

- New branch: `work/bep-map-reconciliation-v3-20261023`
- Branch parent: `work/bep-map-reconciliation-v2-20261023` at `e7cc9bf6da4ee7988eb00429ebd241de3995caa7` (PR #196 head).
- Preserved the v2 proposal's source snapshots, 144-row original/independent crosswalk reference, 143-row integrated-node crosswalk, claim reconciliations and unresolved questions.
- The original source datasets and their histories remain unchanged. V3 is a separate proposed edition and is not a merge or promotion of either map.

## Scientific work completed

- Expanded the proposed map from 21 to **37 nodes**, retaining the original 17 depth-two themes. Added 15 scientific subnodes plus one theme that catalogs choices for later selection.
- Expanded cross-links from 13 to **29**, with explicit connections among kinetic relaxation, forcing after transport filtering, metric definitions, control realization, numerical diffusion, model inference and evidence strength.
- Expanded source evidence from **20 to 24 records**, adding/clarifying Silveston 1995, Zhu 2021, the open-access Monai et al. 2026 perspective, and Schoukens et al. 1994.
- Added a **16-entry proposal claim audit** spanning steady-state/equilibrium language, universal gain claims, thermal-to-feed transfer, a proposed ethylene-desorption pathway, PSSA validity, hidden-state measurement/estimation, Pe and isothermal assumptions, frequency windows, upwind error, waveform bases, metric consistency, steady benchmark/global optimality, novelty and hardware redesign.
- Added an information-first choice guide covering five later project decisions: catalyst/working state; performance metric/accounting; manipulated variables/apparatus; model fidelity; and evidence threshold. Each contains alternatives and the evidence needed to compare them. No choice was selected.
- Rechecked primary-source records for periodic acetylene modeling (Urmès 2022), model-specific positive and null periodic-operation examples (Ziegelhoeffer 1972; Feimer et al. 1982), Pd/PdAg model-surface pathways (Mei et al. 2009), and pulsed CO oxidation on Pt (Zhu et al. 2021). Used the 2026 dynamic-catalysis perspective only for contextual synthesis and the quantitative 40-fold summary, clearly marked as secondary until primary full-text verification.

## Actual validation performed

The machine-readable receipt records a structural and reference-integrity validation of the map and audit: unique node and claim IDs, one root and three discipline arms, resolved acyclic parents, 17 preserved depth-two themes, valid cross-link endpoints, source references resolved, AI-only maturity, proposal snapshot pinned, deferred decisions still unselected, and no simulation or optimization execution.

This validation does **not** establish scientific truth, claim entailment for every source attachment, experimental applicability, a target-model result, or human understanding/source verification.

## Open research questions

1. Verify the 40-fold CO/Pt result against the primary Zhu paper's figure/table; currently the exact factor is rechecked in a 2026 review, while the accessible primary abstract reports a significant increase.
2. Trace the proposal's local PdAg dataset citation and confirm the material, data and condition lineage.
3. Establish the target catalyst working state, input realization, analyzers and feasible/safe frequency band.
4. Discriminate PSSA and dynamic-coverage alternatives and resolve transport/thermal fidelity with target evidence.
5. Select a cycle objective and optimize the steady benchmark under the same constraints before making any gain claim.

## Review destination

PR #197: https://github.com/AsapLoso/project-management-agents/pull/197\n\nTarget: `work/bep-map-reconciliation-v2-20261023` (the PR #196 head), not a protected/default branch. Current GitHub state: open, unmerged and mergeable. No auto-merge is enabled.
