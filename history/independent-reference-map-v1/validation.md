# Validation — independent BEP scientific reference map v1

## Automated data checks

**Executed before commit** against the exact staged bytes in an isolated scratch directory; the validator is not part of the research dataset.

- PyYAML `safe_load` parsed `nodes.yaml` and `sources.yaml` as YAML 1.2-compatible documents (the files use the JSON subset of YAML).
- Value-preserving `safe_dump` → `safe_load` round-trip passed for both documents.
- 63 unique node IDs and 20 unique source IDs.
- Exactly one root (`bep`) and exactly three direct disciplines, in the required order: Physics, Mathematics, Systems & Control.
- All parents resolve; graph is connected and acyclic; maximum edge depth is 4 from root (root depth 0).
- All `related_ids`, claim source IDs, cross-citation IDs, locators, evidence types, maturity values and relevance values resolve or match the declared contract.
- All maturity values are restricted to `idea` / `ai_worked_out`; no human-verified or personal-map state is present.
- Final result: **PASS, zero remaining structural or provenance-reference errors.**

The isolated validator is at `/tmp/bep_independent_v1/validate_graph.py` in the cloud session; it is not included as a product/software deliverable.

## Manual scientific checks

- Checked the 1D gas balance against a declared bed/void/catalyst basis and explicit signed stoichiometry; distinguished the proposal's compact equation from the clarified derivation.
- Checked unit conventions for Pe, Da, St and the cycle-integrated net ethylene objective.
- Checked the source-access level and catalyst/forcing applicability recorded for every cited primary article/review; proposal hypotheses are not described as experimental results.
- Audited novelty, thermal-pulse transfer, PSSA, hidden-state measurement, zero-redesign, resonance-window, square-wave/Fourier, local-search and stiffness claims in `claim_audit.md`.
- Reviewed source citations and internal links against the actual `sources.yaml` IDs.

## Git and remote verification

- Confirmed the specified base branch is `experiment/bep-independent-science-map-20261021` at base SHA `8ecde099de9d6eb10f85c1f68a2643056cace1af`.
- Created `work/bep-independent-reference-v1-20261021` from that exact base through the connected GitHub repository.
- Core graph/provenance/method commit: `19dfa318bbbacb0459f8f6258932efe61136cfc3`. Support/claim-audit commit: `710a832f392c4210fecc8c4b02d2ab28876792c7`.
- Fetched all seven deliverables from the remote work branch and verified exact byte-for-byte equality to the staged files.
- Git compare reports the work branch ahead by two commits, behind by zero, with exactly the seven intended files added under the task directory. No software or unrelated paths changed.
- A final commit will record this remote verification and will itself be read back before opening the PR.

## Not run — intentionally outside this data-only v1

- No kinetic calibration, reactor simulation, numerical solver benchmark, identifiability computation, waveform optimization, or experimental validation was run.
- The 2022 Urmès full article and Supporting Information remain inaccessible in this pass; the literature-gap audit is limited to its abstract and first-page preview.
- No legacy viewer/parser compatibility test was run because this task creates an independent data package and explicitly excludes software changes.
- No human review or scientific owner verification is claimed.
