# Research progress — map reconciliation update

**Date:** 2026-10-23  
**Status:** AI-authored comparison and proposal; review-only, not merged or human-approved.

## Completed scope

- Reused exact source snapshots already recorded in the 21 October comparison: original AI map on `devcontainer` at `f18682d97153251f23396ca7b82fd9dd38f0edf0`; independent v2 at `ea391357ad8e4e03cfd27324d4b274513826b254`.
- Read the integrated research snapshot at `work/bep-integrated-reference-map-v1-20261022` commit `1cd680f95902a0a79b17afb084fa29ab49c6b25f`, including nodes, source registry, concept mapping, claim reconciliations, uncertainties, links, and validation receipt.
- Compared taxonomy, tree depth, unique contributions, source access, catalyst-model alternatives, mathematical derivations, evidence classes, and unresolved questions.
- Reused the prior 144-row source-map crosswalk by immutable path/blob reference and added an integrated-node crosswalk covering all 143 nodes.
- Added two depth-two themes to the earlier 15-theme proposal: physical measurements/instrumentation and mathematical optimization/optimal control.
- Reclassified the periodic gain question as conditional and unresolved; retained the K1 discrepancy, Berger DOI correction, target model alternatives, boundary uncertainty, and cross-system evidence limits.

## Source coverage and limitations

The integrated source registry contains 65 source/context records; its validation snapshot marks 19 full-text read, 3 abstract-and-preview, and 14 abstract-only. The original overlay has 96 historical source attachments; they do not represent 96 unique papers or claim-verified edges. Direct primary-source links and access limits for the main scientific comparisons are in `proposed_unified_map.json`.

The current map remains AI-only (`idea`/ `ai_worked_out`). The ten-entry integrated second-pass audit is a representative same-agent audit, not independent review. No target model, fit, periodic optimization, or experiment is part of this work.

## Structural validation

Programmatic checks run against the exact fetched integrated node snapshot and this proposal before publication:

- 143 integrated nodes parsed; 143 IDs unique; all parent IDs resolve; no ancestry cycles.
- One root, three discipline arms, and 17 depth-two themes are present in the integrated graph.
- The proposal contains 21 unique nodes and 13 cross-links with valid endpoints.
- The new integrated-node crosswalk contains 143 unique source nodes and maps every row to an existing proposed root, discipline, or theme.
- All source IDs used by proposed nodes/cross-links/reconciliation claims exist in the 65-record integrated source catalog.
- Every proposed node remains at `idea` or `ai_worked_out`; no human-understanding or citation-verification status is added.
- The prior source-map crosswalk reference accounts for exactly 69 original overlay + 75 independent-v2 content records.

Structural checks establish reference and schema consistency. They do not establish scientific truth, claim entailment for every attachment, parameter validity, simulation correctness, or target performance.

## Next scientific questions

1. Confirm the target catalyst/support/preparation and feed/operating window.
2. Select a cycle objective and define the optimized steady feasible set.
3. Identify actuator/analyzer dynamics and relevant total-flow/boundary closures.
4. Discriminate PSSA and dynamic-coverage alternatives with target evidence.
5. Define a robust, held-out evidence threshold for any gain claim.

## Review destination

Branch: `work/bep-map-reconciliation-v2-20261023`  
Proposed PR base: `work/bep-integrated-reference-map-v1-20261022`  
The branch will remain unmerged. Pull request: [#196](https://github.com/AsapLoso/project-management-agents/pull/196), open and unmerged, targeting `work/bep-integrated-reference-map-v1-20261022`. The PR is mergeable and remains unmerged.
