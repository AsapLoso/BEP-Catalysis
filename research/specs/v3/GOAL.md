# BEP V3 — Goal and strict completion contract

**Destination:** a scientifically traceable, reproducible, coupled reacting packed-bed reactor **vertical slice**, built in the existing V3 workstream and reviewable by the owner before anything is shared with Damian. The five original artifacts, V0 scientific architecture, compatible existing `pbr` implementations, source evidence, AI reference graph and the *read-only* owner understanding map must all inform this result.

**This file governs completion; [TODO.md](TODO.md) governs the actual checklist.** Both are persistent, GitHub-backed mission authority. This is **not** an instruction to start over or to create yet another planning system.

The V2-compatible Urmès PSSA model is a **provisional implementation baseline**. Its physical assumptions remain subject to owner review. Urmès et al. (2019) reports both `K₁ = 611 Pa⁻¹` in the p. 5 text and `K₁ = 13 Pa⁻¹` in Table 5, p. 6; preserve and investigate this source conflict, using 13 only when attempting the published fitted model. A blocked literature comparison does not block a useful, runnable V3 notebook; it does block any claim of reproduction or validation.

## Start / resume

1. Use `AsapLoso/BEP-Catalysis`. The existing **local** worker branch was reported as `v3/bep-vertical-slice-20261023` at `2586777`, **not pushed as of that report**. Verify this checkout first. This GitHub documentation branch is based on `migration/bep-map-consolidation-20261023`; fetch/copy these two files into the *existing* V3 workspace without overwriting its local work. Do not create a fresh implementation just because these documents live on another branch.
2. Read `AGENTS.md`, scientific-map and reversible-change skills, the existing `notebooks/v3/GOAL.md`, **all** `notebooks/v3/goals/01–05`, `PROGRESS.md`, `SOURCE_MANIFEST.md`, `ARTIFACT_THEORY_MAP.md`, `MODEL_BLUEPRINT.md`, `THEORY_CROSSWALK.md`, `STUDY_PRIORITIES.md`, `DAMIAN_HANDOFF.md` and `README.md`, wherever they exist on the V3 checkout. Read the five pinned source artifacts and V0 framework audit as needed for each acceptance check.
3. **Preserve** all existing requirements. Reconcile this contract and `TODO.md` with every checkbox in the original full `BEP_V3_GOAL.md` (if accessible), current `GOAL.md`, phase files `goals/01–05`, and the current progress tracker. Add any missing requirement to the task register, retaining its original source reference. Do not silently replace the old goals with this shorter file.
4. Work from the earliest unverified requirement, subject to dependencies. Audit first, then **implement/verify** rather than stopping after writing a plan.

## Strict rules (non-negotiable)

**R1 — Full coverage.** Every checkbox, acceptance gate and mandatory output in every governing goal/checklist must have a unique tracked requirement ID. Do not omit inconvenient requirements, treat a heading as a completed item, or silently narrow the scope. If a source is missing, log the precise blocker and where it should come from.

**R2 — Evidence, not confidence.** A requirement can be marked `[x]` only after *all* its acceptance criteria have evidence: exact file, section/cell/function, observed command/test output or primary-source locator, and relevant Git revision. Existing documents, previous agent statements, file existence, green test suites and prior checkmarks are **not sufficient alone**.

**R3 — Four truthful states.** Use `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT STARTED` in the evidence register. `PARTIAL` and `BLOCKED` remain **unchecked**. A documented *attempt* can complete an attempt-specific criterion, but it cannot complete a different criterion requiring *successful reproduction* or a validated physical result.

**R4 — No unilateral scope reduction.** The 17-cell gas-only Urmès PSSA notebook is a **provisional baseline**, not proof that the V0 → V3 coupled-model goal was satisfied. Do not declare the whole mission done because a reduced subset executes. Restore/test source-supported bulk–pellet radial physics using the established V2 engine, unless concrete scientific evidence makes that impossible. Dynamic adsorbed surface states require identifiable elementary rates; never invent them. An infeasible feature is a tracked blocker or an owner-reviewed trade-off, not an automatically completed box.

**R5 — Scientific distinctions.** Explicitly distinguish (a) documented equation or citation, (b) correct parameter transcription, (c) code execution/numerical verification, (d) published-model reproduction, and (e) experimental validation. Distinguish PSSA from dynamic coverages; source-matched conditions from imported/assumed pellet or geometry values; physical model results from illustrative presentation traces.

**R6 — No self-approval.** A worker cannot grant itself a waiver, mark owner scientific understanding, promote personal-map nodes or approve source citations as human-verified. Record questions requiring the owner; continue independent unblocked work. An unresolved scientific question is not permission to fabricate an answer.

**R7 — Never false-close.** Do not invoke a goal-completion/stop action with outcome `complete`, or report "V3 complete", while *any mandatory requirement* is unverified, partial, blocked or missing from the register. If blocked after exhausting other available work, report **INCOMPLETE — BLOCKED**, with evidence and the exact next action. Keep the goal active/resumable rather than repeatedly closing it based on an old commit.

**R8 — No destruction or surprise publishing.** Preserve the local V3 baseline and pinned source snapshots; use isolated, scoped changes and sparse commits. Do not overwrite other workers, modify the owner map, push, open/merge PRs, or send supervisor materials without owner authorization. All supervisor-facing science needs owner review first.

## Definition of done

**All** original and newly enumerated *mandatory* checklist items are present in the register and independently `VERIFIED`; the source-to-theory crosswalk is complete; the selected coupled reactor configuration actually runs reproducibly with recorded numerical checks; published comparison is honestly categorized; study priorities and Damian handoff are prepared **for owner review**, and no science beyond evidence has been claimed. If an owner-approved scope waiver exists, cite the exact approval and keep the waived requirement visibly distinguished from `VERIFIED`.

At each checkpoint update [TODO.md](TODO.md), a detailed `REQUIREMENT_AUDIT.md` on the execution branch, and `PROGRESS.md`. Report counts (`VERIFIED/PARTIAL/BLOCKED/NOT STARTED`), newly reopened items, implementation receipts, and the next unblocked action. Do not stop after an audit or repeat the prior completion report.
