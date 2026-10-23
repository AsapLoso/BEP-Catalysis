# Citation provenance and source re-audit

This evidence layer connects immutable AI claim/source attachment IDs to inspected original passages, scoped support assessments, source-review receipts and an explicit human-review boundary. It does not modify the owner's personal map or promote scientific maturity.

## Files

- `claim_passage_register.yaml`: one stable `CLM-{node_id}-{claim_ref_ordinal}` record for every current graph claim/source edge.
- `historical_attachment_queue.yaml`: all 96 pre-integration overlay attachments, retained with their prior disposition; seven now have source-specific passage records and the remainder stay queued.
- `passage_records.yaml`: exact source locators, brief quotes or structured equations/tables/data extracts, source resource identity, scientific scope and connected claim IDs.
- `source_review_ledger.yaml`: per-source access and review status.
- `coverage_ledger.yaml`: complete current and historical queues by source.
- `research_batches.yaml`, `correction_ledger.yaml`, `second_pass_audit.yaml`, and `state.md`: durable checkpoints and re-audit status.
- `validate_source_evidence.py`: verifies graph/source references, stable IDs, reciprocal claim-passage links, historical attachment coverage, quote text on specified local PDF pages, and the no-human-verification rule.

The source access state inherited from `sources.yaml` is historical context, not evidence that this mission reopened the source. AI rechecks and owner verification are independent fields. All human verification remains `not_verified`.
