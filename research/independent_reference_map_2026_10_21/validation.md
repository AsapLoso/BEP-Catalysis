# Validation — independent BEP scientific reference map v2

## Automated scientific-data structure and provenance checks

**Executed on the final graph/source content** with a scratch-only validator (not a product/software deliverable). Both files are JSON documents, a valid YAML subset.

- `json.loads` parsed `nodes.yaml` and `sources.yaml`; PyYAML `safe_load` values matched, and safe-dump/read round trips preserved both value trees.
- 79 unique scientific node IDs and 28 unique source IDs.
- Exactly one root (`bep`) and exactly three direct disciplines in prescribed order: Physics, Mathematics, Systems & Control.
- All parents resolve; every original v1 node remains in its original relative order; parent-before-child serialization; connected, acyclic, single-parent tree; maximum depth 4 from root (root depth 0).
- All `related_ids`, claim source IDs and source-to-source citations resolve.
- Required fields, maturity/relevance values, substantive node explanations, complete equation metadata and complete claim-reference metadata pass.
- Every source carries access status, applicability and a `does_not_support` boundary; source claims include a locator and support text.
- Dataset edition is `v2-enrichment`; maturity remains limited to `idea` and `ai_worked_out`; no personal/human-verified state is asserted.
- **Final validator result: PASS, zero structural or provenance-reference errors.** An earlier validator draft had an unjustified minimum-depth check; it was removed and the data were rerun successfully without that gate.

The scratch validator and result are ignored under `scratch/`; they are not committed.

## Manual scientific checks

- Checked the conservative gas-balance convention and stoichiometric source interpretation against the proposal’s units and stated basis.
- Checked the spherical pellet equation dimensions: pore and adsorbed inventories share amount per pellet volume; diffusion and catalyst-mass reaction sources share amount per pellet volume per time. The film boundary states its radial-flux sign convention.
- Checked cycle conversion/selectivity/net-yield identity algebraically and recorded the positive-denominator, feed-basis and carbon-closure conditions. The integrated selectivity ratio is not presented as an average of instantaneous ratios.
- Checked the stable-LTI, static-concavity and nested-feasible-set statements against their assumptions; they state limits or weak optimum ordering, not strict BEP gains.
- Checked source-specific catalyst/support/forcing scope and access labels against publisher/repository pages and accessible text. Full text was read for Urmès 2019, Berger 2008, Espinoza 2022 and Kaps 2026; Urmès 2022 remains publisher abstract/preview level, and full SI access failed.
- Reviewed cross-system null/gain examples, actuator/sensor confounding, heat/pellet extensions, catalyst aging and distinction between identification and performance evidence.

## Git and remote checks

- V2 branch `work/bep-independent-reference-v2-20261021` starts at frozen v1 `e330492418150103a219f49bb7e850ece4aac5b9`.
- Commit `244c322d60ee2424c54796477c7351b744ea61d9` contains only `nodes.yaml`, `sources.yaml`, and `method.md`.
- Commit `ac1ce1a80fa4a370a6dfa75d48d95506c06e3d86` contains only `claim_audit.md`, `uncertainties.md`, `progress.md`, and `validation.md`.
- The final status refresh records actual remote and PR readback. V1 still resolves to the frozen SHA; PR #175 targets that branch and is open/unmerged. Its seven changed files are exactly the map deliverables listed above.
- `git diff --check` passed before the first commit and on the final progress/validation record before staging. Remote v1/v2 heads and the PR base/head were read back after push. The complete seven-file PR diff was checked against the requested frozen-v1 base with `git diff --check` after the final record commit.
- The repository commit hook regenerated root `SESSION_MAP.md` and `workspace_inventory.md`; both unrelated files remain unstaged and excluded from all task commits and the PR.

## Not run — outside this scientific map pass

- No parameter fit, reactor simulation, solver benchmark, identifiability computation, waveform optimization, experiment or experimental validation was run.
- No target parameter set, predicted gain/no-gain result, optimum, observability result or validated model is claimed.
- No legacy visualization/parser compatibility check was run; application changes are outside scope.
