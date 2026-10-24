# Validation and completeness report

- Extraction run: `2026-10-24`; baseline archive PR #2 head `53c7f4313dc1bbd709884ffe8cac79e9ce326911`; PR #1 supplemental head `0cd47473a93a71f6200a21e6b66c40d6e3bc7a77`; AAPM devcontainer root ref `8c48cf8a5ba5b3d02dcd1787f98abcd65b34c5c8`; PR #186 historical queue parent `d283f2ba6c05912a39b1a578fca03ab444491e9e`.
- Full imported archive files examined: **119 / 119**. Manifest original blob SHA and copied file content were verified earlier against all 119.
- Total source records in coverage: **180**; zero-action sources: **17**.
- Raw occurrences: **2940**. Distinct clusters: **2471**. Unclustered occurrences: **0**. Stable-ID collisions: **0**. Parsed exact/ticket status-conflict clusters: **0**.
- Original status classes: **{'unclear': 1725, 'open': 898, 'confirmed': 36, 'historical': 77, 'parked': 37, 'blocked': 15, 'recorded_completed_unverified': 152}**. Date-sensitive records flagged `needs_verification`: **126**.
- Confidence counts: **{'medium': 1455, 'low': 577, 'high': 908}**; medium/low items require review (**2032 uncertain occurrences**).
- Markdown parent-child links: **4**; orphan parent references: **0**; list containers: **6**.
- Item-kind counts: **{'list_action_candidate': 1189, 'prose_action_candidate': 403, 'checklist_item': 739, 'table_status_or_action': 61, 'list_decision_or_action': 196, 'prose_question_or_action': 20, 'wayfinder_decision_ticket': 105, 'deferred_proposal': 13, 'list_container': 6, 'BEP_scoped_status_or_action': 9, 'research_task': 23, 'pending_source_review': 59, 'pending_historical_source_review': 89, 'unresolved_claim_audit_action': 16, 'unresolved_audit_issue': 5, 'current_user_priority_directive': 1, 'pr_comment_action': 5, 'pr_comment_status_or_constraint': 1}**.
- Source-type counts: **{'archive_snapshot': 119, 'archive_branch_guidance': 5, 'archive_branch_plan': 1, 'AAPM_root_BEP_scoped': 2, 'PR1_supplemental_file': 26, 'PR186_historical_file_version': 1, 'pull_request_description': 19, 'current_user_instruction': 1, 'pull_request_comment': 6}**.
- Supplemental open-PR descriptions from the 2026-10-23 PR register: **19**; relevant discussions added as **6** separate occurrences.

## Quality-gate samples

- Wayfinder ticket: `O-27c3d81be49923d642b0` at `Academics/BEP/Catalysis/research/wayfinder/bep_catalysis_master.md` L81–L86; the full ticket block is retained.
- Nested Markdown task list: parent context `O-c776566e97b6b0ed8c22` (`- Tasks:`) links child `O-59c9ecb33bed03e9f69e` at `research/wayfinder/bep_tw3_senior_candidates_2026-10-18_prompts.md` L57. No indented `[ ]` checkbox rows were found in scanned Markdown sources; nested numbered tasks are preserved.
- Conflicting source status snapshot: PR #212 was `open` in the 2026-10-23 source PR register and is `closed/merged` in live metadata on 2026-10-24. The historical/live difference is retained in `CONFLICTS_AND_GAPS.md`; it does not rewrite a task status.
- PR-only source: `O-ec2a1880487a69476976` from the captured AAPM PR #198 body.
- Personal-map queue: `O-80346c641f9fd459ffa5` captures Q89 in PR #1’s owner action queue.
- Non-checkbox handoff action: `O-79c3cb5939e0b31492b4` captures a future-reply instruction in the owner-review handoff.

## Invariants checked

1. Every `raw_occurrences.jsonl` record has a stable occurrence ID, non-empty source path/ref or external source identity, source SHA or explicit no-Git-blob treatment, line/section evidence, exact original text, status, extraction method, and confidence.
2. Every occurrence ID appears in exactly one cluster, and every cluster reference resolves to a raw occurrence.
3. Every source path/ref in raw evidence is listed in `SOURCE_COVERAGE.md`; every counted source has a full-source examination record.
4. Occurrence IDs are unique. Cluster IDs are deterministic from exact normalized text or an explicit leading ticket ID plus filename family.
5. Source-native checkbox markers remain present in `original_text` and `original_checkbox_marker`; checked items are only labeled `recorded_completed_unverified` unless stronger source text says otherwise.
6. No scientific map file or supervisor-facing document was modified or copied into this branch.
7. No occurrence was removed through deduplication; exact duplicates retain one raw row per source occurrence.

## Scope and completeness limits

- The occurrence extractor is deliberately inclusive for checkboxes and conservative-but-broad for action-section lists, prose, markdown table rows, YAML research tasks, and unresolved source-review records. It does not perform full human semantic adjudication for every candidate.
- Semantic restatements with different text are linked only when a stable ticket identifier begins the item in the same filename family; other paraphrases remain separate. Dependencies are emitted only when explicitly stated. Status contradictions are flagged only from checkbox markers and explicit source status labels. A complete semantic union therefore remains **incomplete pending human review**.
- The source-ledger queue entries represent review work implied by explicit `not_reopened` / `historical_attachment_no_passage_yet` statuses; this is an extraction classification, not a scientific judgment.
- `current_map.yaml`, `reference_map.yaml`, and scientific graph datasets on PR #1 were not read as task sources. Their embedded knowledge-graph concepts are outside the task-occurrence corpus; the review queue and handoffs that point to them were included.
- 16 local path-prefix redactions, and the reported full-text access failures for Urmès 2022 and Zhu 2021 are documented in `SOURCE_COVERAGE.md`.
- This task did not validate model equations, notebooks, source correctness, frontend behavior, or owner understanding.

## Run the validator

Run `python3 planning/backlog/validate_backlog.py` from the repository root. The script checks source-reference coverage, unique IDs, exact 1:1 occurrence/cluster assignments, and traceability fields.
