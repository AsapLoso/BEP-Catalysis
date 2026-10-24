---
name: reversible-change-review
description: >-
  Use when editing and persisting any file, dataset, code, document or configuration
  whose changes must be reviewable, pushed or synchronized, recoverable or reverted.
  Applies to local and external repos and pull/push/pull workflows: inspect diff,
  checkpoint a logical change, verify the remote state, report the patch, and
  revert only the intended change. For BEP scientific mind-map edits, also invoke
  bep-map-edit-review, which governs semantic authoring and owner approvals.
---

# Reversible change review — general-purpose transaction workflow

**Purpose:** leave an inspectable history for a change to a repository, dataset, document, spreadsheet export, generated artifact or synced configuration. Git is one implementation; the principle is **read current → small intended edit → inspect diff → checkpoint → synchronize → read back → inspect diff → repair/revert if needed**.

## 1. Identify the persistence system

- Establish **authoritative source**, branch/ref/version, remote destination, other writers, and exact files/records affected. A local copy may not be the source of truth; never overwrite other writers without comparing.
- Check the system's actual diff/version/undo facilities. For a spreadsheet or service, prefer native version history/record diffs when Git is not the source of truth.
- Work in an isolated feature branch or copy unless the user explicitly requests an in-place edit and it is safe. **Do not infer consent for business/domain decisions from permission to commit.** Defer to project-specific skill for what can be changed.

## 2. One coherent change at a time

- Gather a stable preimage: file content + blob SHA/version and, if possible, a known-good baseline. Make only the requested logical edit. Protect unknown fields, metadata, formatting, local modifications and unrelated files.
- Validate using the domain-specific checker. For changing file formats or parsers, check round-trip preservation; a visual frontend reading successfully is insufficient to prove data integrity.
- For interactive graph/layout changes, capture the default overview, focus/tour states, and a narrow viewport. Check that panels either reserve visible canvas space or can be moved, and inspect the rendered screenshot for hidden nodes or clipped controls.
- Inspect the full change set **before** committing/pushing: exact old/new values, `git diff -- <paths>`, or native record-difference view. Unexpected modifications mean **STOP, investigate, do not bury them in a larger change**.

## 3. Checkpoint, push, pull, compare

- Stage exact paths only: `git add -- <paths>`, `git diff --cached -- <paths>`, `git commit -m "..."` (one independent logical edit or a small coherent unit). Never globally stage unrelated work.
- If using GitHub's contents API, capture a file's actual blob SHA, write with expected preimage SHA, then fetch and compare the postimage; those API writes typically create a commit.
- For a repository with remote changes, **fetch/pull carefully** and reconcile if divergence or a dirty tree exists; do not blindly force-push. Push the specific branch; verify remote head, then fetch/pull/read back **from the remote** and inspect the actual remote diff against the intended base. A successful push is not itself verification.
- In Git: `git status --short`, `git log -1`, `git show --stat HEAD`, `git diff <base>...HEAD -- <paths>`; share the commit/PR Files/compare link. For spreadsheet workflows: pull/export current authoritative version → edit → push/import → pull/read back → compare values, formulas and structure.
- **Preserve rollback granularity through integration.** If several separate logical commits need separate one-command reverts on the target branch, do **not squash-merge them**. Choose a merge commit or non-squashing rebase after conflict review; squash collapses those revert boundaries. Squash is fine when the entire PR is one logical reversible change.

## 4. Corrections, complaints and rollback

- If the user says "wrong", "what happened?", "not like that", or challenges a change: **do not panic, perform wholesale rollbacks, or assume an unspecified replacement**. Identify the exact complained-of commit/record; show the narrow before/after diff and a concise explanation of the likely mismatch; preserve untouched data and working copies.
- If the correction is clear and within an approved scope, make the smallest new corrective edit and run the workflow again. If intent is ambiguous, ask **one focused question** before altering the authoritative record. Distinguish *review feedback* from a command to revert.
- Prefer a new revert commit (e.g. `git revert <commit-that-exists-in-target-history>`) or targeted reverse patch after checking dependencies and later edits. For merged squashes, a single pre-squash feature-commit may need a **selective inverse patch**, not `git revert` on the target branch. Never run destructive reset, mass deletion, forced push or history rewrite without explicit user authorization and recovery analysis.
- Report what is **still unverified**. Diff correctness means *change traceability*, not scientific truth, source validation, or owner's comprehension.

## 5. Completion receipt

Provide source and destination versions, exact files/records, edit summary, tests actually run, **real** diff link or concise diff excerpt, push/pull or remote-readback verification, independent rollback instructions, unresolved conflicts and next action. If the file is not synced, was not committed, or the tests were not run, say so.

**Project-specific skills override this generic workflow when domain authorization or integrity is stricter.** Do not infer all future writes are approved merely because the user authorized one class of change.


## 6. BEP mind-map frontend evidence

For graph-layout changes, inspect the full diff and prove that the owner-map, AI-reference, and citation source files were not edited. Add data-driven regression fixtures for unequal subtree sizes, changing root-child counts, collapse/expand, and arbitrary depth; do not treat the current owner snapshot's theme and question structure as a fixed production taxonomy. Verify overview node positions and routed ELK edges, horizontal focus, level-order guided navigation, overlay placement, read-only API behavior, and the Windows one-click launcher. Existing screenshots are evidence for their capture revision only; label missing post-change browser captures explicitly.
