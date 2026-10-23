# Research progress — map comparison and reconciliation

**Date:** 2026-10-21
**Status:** AI-authored comparison and proposed structure; not merged, human-verified or personally approved.

## Scope and preserved inputs

This pass compared the original AI map on `devcontainer` at `f18682d97153251f23396ca7b82fd9dd38f0edf0` (canonical and overlay blobs recorded in the YAML) with independent map v2 at `ea391357ad8e4e03cfd27324d4b274513826b254`. The work is on a separate branch based on `work/bep-independent-reference-v2-20261021`, and its PR targets that branch. It does not edit either source map, rewrite history, merge the maps, or alter PR #173 / the v2 PR.

## Scientific work completed

- Compared taxonomy, depth, discipline balance, source records, maturity fields, equation/model distinctions and uncertainty treatment.
- Audited map-specific claims against primary/publisher records where available, including the contrary periodic-operation cases and direct periodic acetylene precedent.
- Identified the original overlay’s incorrect Berger DOI binding and narrowed the novelty claim in light of Urmès et al. (2022).
- Produced a semantic proposal retaining the shared root and three discipline IDs, adding 15 proposed theme nodes, and crosswalking every content record in both maps (69 original overlay records + 75 independent-v2 content records = 144 unique crosswalk rows).
- Recorded competing claims, evidence boundaries, cross-disciplinary links and project decisions that remain open.

## Validation performed

- Parsed the proposed reconciliation as YAML.
- Checked proposed IDs and parent references, root/discipline structure, cross-link endpoints, source-ledger references, and crosswalk coverage against the exact source snapshots.
- Checked that each original overlay and independent-v2 content ID appears once in the primary crosswalk; shared root and discipline IDs are represented directly in the proposal.
- Reviewed the scoped Git diff and whitespace before commit.

No reactor model, parameter fitting, waveform optimization, or experimental validation was run; those are outside this assignment. Validation confirms the artifact structure and reference integrity, not the scientific truth of every source claim.

## Important remaining uncertainties / decisions

1. Target catalyst composition, support, geometry, preparation, pretreatment and feed.
2. Objective definition, inlet ethylene treatment, conversion floor, campaign horizon and cost accounting.
3. Real actuator bandwidth, bed-plane input realization, total-flow coupling and process/safety limits.
4. Evidence-supported choice among PSSA and explicit dynamic coverage models, including transport and thermal states.
5. Required target-specific validation and uncertainty separation before a gain claim.

Additional source limits: Urmès et al. (2022) is represented from publisher abstract/preview access in v2; the accessible record does not resolve all spatial-model details or establish optimized performance gain. The v2 `sources.yaml` metadata edition remains `v1` while its node dataset says `v2-enrichment`; flagged for a later scoped correction, not modified here. The corrected Berger review still needs claim-specific page/section locators before reuse in an authoritative ledger.

## Files

- `comparison.md` — evidence-bounded structural and scientific comparison.
- `proposed_unified_map.yaml` — machine-readable semantic taxonomy, equations, assumptions, provenance, limitations, crosswalk, claim reconciliations and decisions.
- `progress.md` — this scope and validation record.
