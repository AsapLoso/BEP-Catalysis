---
name: bep-guided-science-loop
description: >-
  Run owner-led BEP scientific learning conversations with repeated incremental
  map updates and later human-in-the-loop Jupyter notebook implementation.
  Use for theory, reactor kinetics, equations, transport and numerical choices.
  Coordinate with bep-map-edit-review, reversible-change-review and session-handoff.
---

# Guided BEP science: discuss ↔ evolve the personal map → write notebook

## Purpose

The personal map is **continuously shaped during the conversation**, not
filled in only after the notebook is written. The owner may discuss, correct,
approve a precise map change, reconsider a theory point and repeat many times
before a single code cell is edited. A useful session may end with one
understood idea and zero Python. Avoid making frontend polish, repository
consolidation or clearing historical checklists a prerequisite for science.

## Source hierarchy and boundaries

- **Owner editable notebook:** [`notebooks/unified_dynamic_reactor.ipynb` on
  `unified-reactor-model`](https://github.com/AsapLoso/BEP-Catalysis/blob/unified-reactor-model/notebooks/unified_dynamic_reactor.ipynb).
  The owner writes; the agent helps explain, review, test and optionally
  make a requested *small* code edit.
- **Reference implementations:** `notebooks/reference/` (legacy, AI,
  V3, V4) and `notebooks/benchmarks/`. Preserve their historical output,
  provenance and limitations. Do not overwrite the personal notebook.
- **Owner scientific map:** find the latest owner-approved
  `owner_working_map/current_map.yaml`. One dated source is the
  [2026-10-22 snapshot on
  `migration/bep-map-consolidation-20261023`](https://github.com/AsapLoso/BEP-Catalysis/blob/migration/bep-map-consolidation-20261023/research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml).
  It might not be the newest approved copy. Use the [source map](https://github.com/AsapLoso/BEP-Catalysis/blob/codex/bep-source-map-archive-20261029/planning/SOURCE_MAP.md)
  to locate separate AI research and archived AaPM records.
- **AI research:** integrated/independent reference maps, papers, audit
  notes, bridges, unresolved hypotheses and their citations. They are not
  personal knowledge or automatic permission to edit the owner graph.

Use `bep-map-edit-review` for semantic authoring and approval;
`reversible-change-review` for safe Git transactions; and
`session-handoff` when a conversation ends. Before writing, inspect the
actual branch/ref, blob SHA, current node and authorization receipts.
Historical banners, source snapshots, PR titles and chat summaries are
not automatically live authority.

## Conversational loop — repeat freely

1. **Resume narrowly:** inspect one current map node, its immediate
   parent/siblings, a relevant reference and the precise open question.
   Do not begin by reading thousands of backlog items.
2. **Reason with the owner:** discuss mechanisms, assumptions, derivations,
   sources, alternatives and uncertainty. Invite corrections and use the
   owner's own explanation as primary evidence of their understanding.
3. **Propose a small map change whenever useful:** show exact node ID,
   title, parent/siblings, short owner-facing summary, proposed maturity,
   and before/after fields. Obtain explicit approval **even for a new Idea
   node**. An unambiguous, specific user instruction already grants that
   scoped approval; do not ask redundantly.
4. **Persist only approved personal changes:** patch the chosen node and
   decision/authorization receipt, verify the saved graph and indexes,
   and preserve unrelated work. If the user has not approved a placement,
   keep it in an explicitly *unplaced* AI bridge/queue/reference note.
5. **Return to discussion** rather than forcing code. Several small map
   corrections can precede one notebook edit. No automatic mass taxonomy,
   autonomous node creation or understanding promotion.

The owner stages are `Idea`, `AI worked out`, `Human worked out`,
`Informal Writing` and `Formal Writing`. Structural approval, reading,
understanding, owner-authored prose and claim/source `human_verified`
are distinct. Fluency, source citations, a numerical test or a Git merge
does not imply a status upgrade. Preserve the owner's concise wording in
`summary`/`notes` and deeper AI interpretation in labelled
`AI_REFERENCE.md`/background. An owner-facing `index.md` requires
approval of the *actual written prose* as Informal/Formal Writing.

## Gate into the notebook

Only when the owner chooses a **concrete equation or method to try**:

- Explain its variables, units, basis, conservation, closure, sources,
  applicability, alternatives and remaining assumptions. Label values
  published, transcribed, derived, fitted, assumed or unknown.
- Select a small section of `notebooks/unified_dynamic_reactor.ipynb`.
  Prefer the owner to type it in VS Code/Jupyter; the agent corrects,
  explains and helps with a bounded test. Make code edits directly only
  when delegated. Never autonomously replace the owner sketch.
- Report actual interpreter, notebook kernel, checkout, command, outputs
  and test limits if executed. Software consistency, reproduction of a
  paper and experimental BEP validation are different claims.
- Return to the same map/dialogue approval loop when implementation raises
  new questions. Code never silently changes personal-map status.

Example: discuss hydrogen activation, site availability and LH/LR/ER,
update approved concept notes, track competing unapproved rate laws,
choose one provisional kinetic form with the owner, *then* implement one
function and test its units/limiting behavior.

## Workspace and synchronization

A Codespace is a separate Git checkout. The remote VS Code editor, Codex
and Jupyter should use one **saved** remote workspace. Unsaved buffers are
not visible to other processes; OneDrive and Git do not provide live
two-way editing. Before syncing inspect local-only commits, unstaged,
untracked and ignored material, external PDFs and remote changes. No
blanket staging, blind pull, force push, reset or overwrite. The open
reference PRs are not automatically merged or validated.

Do not confuse this skill/contract with a tested writeback backend. Verify
UI, Git map persistence, approval behavior and notebook execution
end-to-end before claiming them operational.

## Durable checkpoint

Record approved owner-map changes with exact IDs and receipts, keep
tentative AI hypotheses separately, record only owner-chosen notebook
code and actual execution receipts, and hand off **one next scientific
question** with exact refs and uncertainty. If writing is unavailable,
provide a portable **NOT SAVED** patch/handoff instead of claiming the
conversation was committed.
## Proactive completion discipline (implementation vs discussion)

**Do not equate good explanations, a skill update, a PR description or an
action queue with a functioning learning workflow.** For engineering work
on the map backend/agent integration, the outcome is an actual
reviewable implementation and test receipt. Read
[`BEP execution handoff`](../../../research/workflows/BEP_EXECUTION_HANDOFF_2026_10_29.md)
and the existing backend contract. After identifying an executable next
action, **do it** (within tool access and authorization), then test and
read back before announcing progress.

The agent owns forward motion: inspect what exists; pick a small safe
technical step; implement, test, repair and checkpoint; repeat. Do not
stall on optional architecture questions or ask the owner to manage
ordinary engineering priorities. If blocked, record the exact failing
condition and pursue another independent safe step.

This proactivity does **not** authorize changing the personal science
map, deciding kinetics for the owner, fabricating approval, destructive
Git operations, or sending material to supervisors. Learning discussions
can remain open-ended when the owner wants them; an **engineering task**
has explicit done criteria and must be driven toward them. Stop
expanding the infrastructure once a usable thin slice exists; return
to actual BEP science with the user.
