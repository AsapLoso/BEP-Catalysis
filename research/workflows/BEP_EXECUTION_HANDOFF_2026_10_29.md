# BEP — execute the conversational science workflow, not another plan

**Handoff date:** 2026-10-29 · **Session ID:** UNKNOWN (plain ChatGPT)
**Repository:** `AsapLoso/BEP-Catalysis`
**Work base:** `unified-reactor-model` (check live head before branching)
**Status:** implementation **NOT COMPLETE**; the guidance from [PR #22](https://github.com/AsapLoso/BEP-Catalysis/pull/22) was merged, but not the operational backend.

## User's objective — the actual finish line

The user wants to enjoy working on BEP theory again. The agent and user
discuss catalysis, reaction/kinetic equations, physics and numerics across
as many turns as needed. **During the dialogue**, the personal understanding
map is amended through exact, owner-approved small changes. AI explanation,
hypotheses, sources and open questions are recorded separately. Only when
the user understands and chooses a specific mathematical formulation do
they begin writing its Python in the personal Jupyter notebook; the agent
helps correct and test it in their VS Code workspace. This must be a
**repeatable, working flow**, not a pretty description.

The user's central complaint: agents repeatedly produce persuasive plans
and workflows, then stop, hand back ambiguity, or declare document
completion as project completion. **Default to finishing the next
engineering step and demonstrating it**, not asking what to do next.
The infrastructure is a means to getting back to actual BEP science.

## Authority and inputs (verify afresh, do not blindly trust this snapshot)

- `unified-reactor-model`: `AGENTS.md`,
  `.agents/skills/bep-guided-science-loop/SKILL.md`,
  `.agents/skills/bep-map-edit-review/SKILL.md`,
  `.agents/skills/reversible-change-review/SKILL.md`,
  `.agents/skills/session-handoff/SKILL.md`, and
  `research/workflows/bep_conversational_map_backend.md`.
- User-owned notebook: `notebooks/unified_dynamic_reactor.ipynb`.
  Reference implementations: `notebooks/reference/` and
  `notebooks/benchmarks/`, with model/evidence audits in `research/`.
- The personal map's **dated** GitHub snapshot is under
  `research/manual_map_sessions_2026_10_22/owner_working_map/` on
  `migration/bep-map-consolidation-20261023`. Its
  `current_map.yaml` is JSON-formatted despite the suffix, and includes
  approval/index information. The current owner copy may be newer or
  locally modified; determine actual authority before edits.
- The existing `mindmap/` Python application, viewer, schema, editor,
  MCP bridge and tests are present in that **migration branch**, but
  `mindmap/schema.py` is **not** on the present reactor-model base.
  The viewer reads owner snapshots; the legacy editor explicitly blocks
  personal approval writes and its promote endpoint is disabled.
  Preserve these safety boundaries, do not re-enable old promotions.
- [PR #13](https://github.com/AsapLoso/BEP-Catalysis/pull/13) has the
  Codespace setup, but its recorded env path is `notebooks/v3`
  whereas the organized reactor branch uses `notebooks/reference/v3`.
  The earlier handoff reports unpublished local commits and untracked
  work; verify today, do not assume the local copy is on GitHub.
- Draft reference PRs #14–17 point at `unified-reactor-model`. They are
  source/reference pointers, not merger approval, and may contain
  removals due to age. Keep them intact.

## Agent behavior: proactive, bounded, and actually goal-seeking

1. **Own the engineering next action.** After recovering the actual
   state, choose the smallest safe implementation slice; code it,
   run the relevant tests, inspect the diff, fix failed tests, and
   record evidence. Don't end after "here's a plan" when a code/test
   operation is available. If a blocker prevents one route, try a
   safe alternative and make progress on a separate independent step.
2. **Keep a live completion ledger** with `DONE / IN PROGRESS /
   BLOCKED / NOT STARTED`; each item has evidence and a next
   executable action. Status must distinguish documented, implemented,
   tested locally, and verified end to end.
3. **Default choices:** prefer an isolated implementation branch,
   scoped code edits and lossless node-level operations over wholesale
   repo merging; preserve the existing viewer; prefer a small agent-
   callable backend/CLI with tests before inventing another frontend.
   Do not require fully resolved scientific modeling choices to build
   review and persistence infrastructure.
4. **Ask the user only at a true decision boundary:** a specific
   personal-map placement/maturity/text approval, a scientific modeling
   choice, destructive/in-place operations, or external sending. Present
   one narrow proposal, context and a recommended reversible default.
   Never manufacture human approval from agreement about general goals.
5. **Do not use the user's energy as a task scheduler.** Choose and
   perform the next engineering step without asking which subtask to
   tackle. After a partial success, keep working within the current
   authorized scope. Don't expand into unrelated UI polish, literature
   campaigns or the 2,471-cluster backlog.

## Work packages — perform in this order unless evidence requires reordering

### A. Reconcile the executable environment and authoritative files

Inspect current refs, dependency manifests, owner-map schema and editor,
test suite, working tree and local/remote divergence. Find the actual
owner-approved map. If only remote snapshots are accessible, state
exactly what is verifiable and protect unobserved local changes.
Choose an isolated branch against the right source. **Do not merge**
the migration branch wholesale into the reactor branch just to obtain
the map writer.

**Output:** a short path/ref/source-of-truth receipt and a selected
non-destructive implementation location, not an indefinite audit.

### B. Implement an owner-safe, agent-callable map edit path

Build the smallest useful mechanism that can:
- read a selected approved owner map and focused node + parent/siblings;
- produce an exact, readable before/after proposal including node ID,
  hierarchy, owner summary, stage and source uncertainty;
- distinguish **unapproved AI proposal** from **explicitly approved**
  personal-map edit (including an Idea);
- perform scoped field/node writes with expected blob/commit SHA,
  fail on stale state, preserve unknown fields and concurrent branches,
  and update the authorization receipt/index consistently;
- read back the result and report a precise revert/PR link.

Use fixture data to simulate approvals rather than fabricate an actual
human decision. Maintain the separate AI reference map and the legacy
owner-promotion veto. If existing code already supports a step,
reuse/test it instead of rewriting. Do not change real owner scientific
nodes without their specific approval.

**Minimum usable result:** an agent can safely propose a map refinement
and persist it *after an explicit human choice*, without copying/pasting
the whole map or mangling unrelated nodes.

### C. Prove the back-and-forth workflow end to end

Write tests demonstrating: two consecutive approved **fixture** map
edits with zero notebook changes; one rejected/unapproved node staying
AI-only; a simulated stale concurrent edit rejected; an unknown schema
field preserved; separate understanding/source/prose approvals; a
reversible targeted correction; durable readback and resumption.

Fix the Codespace/environment layout mismatch if it affects test
execution, preserving PR #13 and unpublished local files. Check that
the VS Code/agent/Jupyter arrangement can observe **saved** changes in
a shared remote checkout. A demonstration may use a scratch/fixture
notebook and must not overwrite the user's own cells. A live user
interaction may remain gated; document that specifically rather than
calling the entire loop verified.

### D. Integrate only after proof

Update relevant skills, tests and README *with the implementation*
where needed. Produce a reviewable scoped PR with exact test commands,
results, unchanged scientific assets, known limits and one immediate
user action (if truly required). Merge only when authorized and safe.
Mark the task DONE only when an actual user-guided map session can
persist an approved change, return to theory, and hand off with a usable
notebook environment. Documentation alone, a mock-only test, or a
browser screenshot cannot satisfy this gate.

## Explicit non-goals and vetoes

- Never silently promote `Human worked out`, `Informal Writing`,
  `Formal Writing` or `human_verified`; no blanket permission for
  new personal nodes, including Ideas.
- No autonomous supervisor email, no invented data, no claim that
  published model or BEP experiment is validated by code tests.
- No bulk stage, force reset/push, deletion of historic PR branches,
  wholesale graph regeneration, accidental commit of large PDFs,
  ignored local research, credentials or scratch files.
- No recursive replanning and no self-declared completion because a
  proposal, handoff, issue or skill has been written.

## Handoff / completion receipt required from executing agent

`STATUS`: operational / partially operational / blocked.
`EVIDENCE`: exact branch/commit, changed paths, runnable commands,
actual test outcomes and link to reviewed diff.
`OWNER MAP`: which ref was used, whether any **real** owner nodes
changed, exact permission, and how to undo.
`NOTEBOOK`: what was run against saved files and what remained a mock.
`OPEN`: up to three **concrete** blockers, who controls them and the
next independent action.
`NEXT`: the one action the agent will take if continuing, or the
one narrowly specified human decision genuinely needed.

Never hand back "tell me what you'd like me to do next" when another
safe, testable engineering action is available.
