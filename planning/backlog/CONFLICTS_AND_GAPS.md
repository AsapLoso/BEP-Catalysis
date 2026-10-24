# Conflicts and gaps

## Snapshot and scope conflicts

- The 2026-10-23 `migration/SOURCE_PRS.json` snapshot recorded PRs #212, #199, and #188 as open. Live GitHub reads on 2026-10-24 show all three merged (#212 at 22:41:35Z on Oct 23; #188 at 22:43:54Z on Oct 23; #199 at 10:56:33Z on Oct 24). Preserve both states; do not rewrite the captured PR descriptions or backlog statuses.
- The October 23 manifest recorded PR #154 as open; live reads show it closed without merge and its comment directs readers to PR #214, which is merged. Treat the older PR as superseded evidence, not a current action.
- The PR #186 active queue says it is “unfinished work and decisions” only and that 36 previously completed items plus owner-triggered Q96 were removed. The immediately preceding queue version at parent `d283f2ba6c05912a39b1a578fca03ab444491e9e` is included as a distinct historical source; checked history is not discarded. Q96 remains explicitly gated on an owner trigger.
- The duplicate TW3 senior-candidate file copies and duplicate scientific-method snapshots remain separate occurrences where source paths differ, even when source blob/text matches. No independent task count is inferred from duplicates.
- Dated presentation, committee, and follow-up snapshots may be stale. Their recorded markers remain intact; older due/target/checkpoint dates receive a separate `needs_verification` freshness flag without replacing source status.
- PR #198 records 0 human-verified AI claim-source links. AI-source audit completion and scientific correctness remain separate questions.

## Automatically detected status conflicts

- No stable exact-wording or ticket cluster had different parsed status classes. This does not prove that there are no semantic contradictions; text variants are not automatically merged.

## Inaccessible material and unresolved gaps

- Full Urmès et al. (2022) article and SI and full Zhu et al. (2021) article were reported inaccessible (publisher/HTTP 403) in PR #198. The specific source-level claims that need those passages remain unverified; this extraction does not resolve them.
- Sixteen manifest path-prefix redactions prevent recovery of original local absolute paths from this archive, while source content and Git blob provenance are intact.
- `AsapLoso/Methanol-Catalysis` was not inspected. No numerical/model validation or notebook replay was performed; this remains a gap only for tasks that require that context.
- Current owner-map and AI-reference graph datasets were excluded from source inspection to respect the no-scientific-map-copy boundary. The occurrence union covers planning artifacts and explicitly actionable review metadata; it does not audit all claims/nodes in those graphs.
- This extraction recognizes checkbox/list/prose/table/YAML status records mechanically. Low- and medium-confidence items need human triage; there is no manual semantic pass over every one of the many task lines. See counts in VALIDATION.md.
- Semantic restatements, implicit dependencies, and contradictions with different wording are not automatically resolved. Exact duplicate normalization is conservative; the derived clusters are a review scaffold, not semantic truth.
- Original PR comments/reviews for historical closed PRs outside the explicitly open set were not collected.

## Questions reserved for owner review

- Which stale checklist occurrence is operational now, if any? No status is promoted from the occurrence ledger.
- Which candidate task restatements should become one canonical cluster, and which are distinct?
- Which unresolved owner-approved, AI-proposed, or unreviewed items should appear in a future active roadmap? This draft does not promote any.
- Confirm that the direct current priority instruction is represented separately from all historical checklists: Damian first with one personally understood notebook and a handful of previously discussed map questions after owner review; Zoë second; the weekend benchmark is a possible next slice without a validated due date.

