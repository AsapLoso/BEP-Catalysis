# Execution plan — citation grounding in substantive waves

**Read [WORK_GOAL.md](WORK_GOAL.md) before following this plan.** This is not a standalone alternative goal.

## First access and preflight

1. Use connected GitHub/cloud Work; no local Windows checkout or university proxy required. Read `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/` on **latest** branch `work/bep-integrated-reference-map-v1-20261022`, including `nodes.yaml`, `sources.yaml`, `source_provenance.yaml`, `claim_reconciliations.yaml`, `uncertainties.yaml`, `progress.md`, `validation_results.json`, existing `validate_data.py` and evidence audit/ledger.
2. Also inspect `Academics/BEP/Catalysis/0_Project_Management/main.tex`, `references.bib`, and relevant `Articles/` PDFs; use the existing original-source catalogue, avoiding redundant discovery.
3. Inspect GitHub branch/PR status; branch fresh from **current** PR #180 head, never from `main`/`devcontainer` or from manual PR #182.
4. Enumerate **every current claim/source link**, detect missing precise claim identity, unresolved legacy attachment, page locator and direct citation quote; do not declare an unsupported quotation as present.

## Evidence record schema (illustrative; adapt without losing semantics)

```yaml
evidence_records:
  - evidence_id: ev_stable_slug
    reference_node_id: ph_sequential_path
    claim_id: claim_stable_or_new
    source_id: urmes2019
    bibliographic_identity:
      doi: "10.3390/catal9020180"
      source_file: "exact repo path if available"
      revision_or_hash: null
    passage:
      chapter: null
      section: "specific source section when inspected"
      printed_page: null
      pdf_page: null
      item: null # eq/table/figure/paragraph
      verbatim_short_excerpt: null # literal source words ONLY if directly inspected
      quote_access: "full_text_read | abstract_only | preview | inaccessible"
    claim_text: "bounded claim as AI map currently states"
    judgement:
      outcome: "pending"
      ai_explanation: null
      qualifications: []
      counterevidence_ids: []
    review:
      authority: "AI"
      ai_status: "attached_not_checked"
      owner_read: false
      human_verified: false
      inspected_at: null
      wave: null
    history: []
```

Do not blindly serialize this against `mindmap/schema.py`: its current unknown-field handling may discard metadata. Keep separate evidence YAML under `citation_audit/` and add stable references to existing graph nodes only through tested schema-compatible edits or a deliberate, reviewed migration.

## Research sequence

**Wave A — inventory and high-risk chemistry.** Ground the net C₂H₂/H₂ reactions and any extra ethane route; distinguish gas stoichiometry, surface intermediary paths, and independent reaction rates. Prioritize `u_ph_reaction`, `ph_reaction_network`, `ph_sequential_path`, `c1_parallel_ethane_paths`, `c1_vinyl_ethylidene_alternative`, related catalyst/site/kinetics nodes; start from Urmès 2019, Mei 2009, Bos & Westerterp 1993, Borodziński and relevant local PDFs. Record which full text was genuinely inspected and whether any exact quote/locator can be supplied.

**Wave B — kinetic/transport equations.** Cross-check source-specific site hypotheses, adsorption terms, rate units, pellet-vs-bed basis, finite-volume/conservation claims, Mears/Weisz-Prater screening assumptions, solver stability conditions. Note derivations rather than invent quotations.

**Wave C — measurements, identification and periodic comparison.** Inspect transient source claims, analyzer/MFC dynamics, FIM/PE scope, periodic orbit results, and conditional gain; ensure no result from methanol CSTR or idealized Pd surface is attributed to the target BEP reactor.

**Wave D — remaining citations and second-pass challenge.** Work through remaining source attachments and lower-risk claims with full coverage ledger. Run a fresh-pass challenge against a representative sample of claims from each wave, all previously corrected high-risk claims, and contradictory source pairs; then attempt complete closure of unresolved citations where access permits.

Waves are **actual research and data-edit cycles**, not just topic headings. If some sources are inaccessible, explicitly record unresolved links rather than mark them verified.

## After every batch

- Commit independently reviewable evidence records and claim corrections (one logical subject per commit).
- Recompute the inventory of `verified_source_passage`, `abstract_only`, `derivation_backed`, `unsupported`, `inaccessible`, `not_yet_checked`. Use deterministic IDs and avoid double-counting multiple snippets for one claim.
- Update a persistent `checkpoint.md` with last processed stable IDs, exact Git ref/SHA, source access changes, unresolved problems, next exact node/claim batch.
- Validate source IDs, node IDs, quote provenance fields, bibliographic integrity, claim states, historical attachments/crosswalk, and no accidental human approval. Review git diffs for unrelated edits.
- If resuming after compression, read checkpoint + source YAML first, then **reopen the original passages** before trusting a previously AI-approved conclusion.

## End state and reporting

Write a compact, substantive scientific report: total enumerated claim references; count truly passage-grounded; source-access-limited; derivation-backed; corrected/narrowed/contradicted; outstanding and their reasons; a real second-pass audit result; links to small commits and open unmerged PR.

**Completeness is evidence coverage, not a large number of checked boxes.** Do not substitute a status summary for source passages.
