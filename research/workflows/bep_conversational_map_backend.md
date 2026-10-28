# BEP guided science — conversational map backend contract

**2026-10-29: specification, not a verified working backend.**

The existing frontend may suffice. A backend must support many small,
owner-reviewed map edits **during** theory discussion, before notebook
implementation. Do not build a new frontend or auto-merge reference PRs
to satisfy this contract.

## Required behavior

1. Read the *latest owner-approved* map/ref/blob SHA, approval receipts,
   and focused node with immediate parent/siblings. Distinguish live
   owner map, migration snapshots and AI reference maps.
2. Propose an exact node/field patch (ID, parent, summary, maturity,
   relationships), show before/after, and obtain specific approval even
   for an Idea. Pending work goes to *unplaced AI-only* bridges/queue.
3. Keep structure approval, owner reading, understood stage,
   owner-approved writing and source `human_verified` independent.
4. Before writing, re-read the branch/blob; reject/reconcile concurrent
   changes, preserve unknown schema fields and other authors' nodes;
   update scoped authorization receipts and necessary indexes.
5. Read back the saved paths, stage, links, unrelated records and diff.
   Report commit/PR and safe revert; detect partial multi-file writes.
6. Return to science discussion. Only the owner-chosen equation goes to
   `notebooks/unified_dynamic_reactor.ipynb`; V1/V2/V3/V4, AI and
   benchmark notebooks remain references.

## End-to-end acceptance scenarios

- Approved *Idea* insertion at shown parent/siblings with decision receipt.
- Unapproved proposed node stays AI-only; no personal graph mutation.
- Targeted correction is reversible; other approved nodes remain unchanged.
- Stale writer cannot discard a concurrent edit or unknown schema field.
- Human understanding, authored prose and citation verification remain
  unchanged after an AI explanation or passing numerical test.
- Two owner-approved map revisions with **zero notebook edits**.
- Later, owner types a small rate-law function in VS Code; saved remote
  file is visible to Codex/Jupyter, and a bounded test has a real receipt.
- Plain chat without OpenCode session logs uses `session-id: UNKNOWN`,
  not a fabricated ID, and labels unavailable writes **NOT SAVED**.

Codespaces, OneDrive and Git do not synchronize unsaved notebook cells.
Do not assume local-only commits, ignored literature or external files are
available remotely. This contract does not install or validate live
backend writeback.
