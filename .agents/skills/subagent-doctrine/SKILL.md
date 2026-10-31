---
name: subagent-doctrine
description: "Use when delegating: pick archetype + model intentionally."
version: 1.0.0
author: Hermes Agent (Deuts)
license: MIT
metadata:
  hermes:
    tags: [delegation, subagents, archetypes, routing, orchestration]
---

# Subagent Doctrine

Companion to `nvidia-subagent-fleet` (roster + wiring). This file is the playbook: which subagent to spawn, on which model, and how the fleet learns. Load both when delegating.

## When to Use

- Before ANY `delegate_task` batch or spawned worker: choose archetype + model deliberately via the matrix below.
- After any non-trivial delegation run: record the lesson (Auto-Learn Loop at the bottom).

## Decision Procedure (be intentional, every time)

1. **Don't delegate trivia.** One lookup, one read, one grep — do it in-context. Delegate when work is parallelizable, context-flooding, or isolatable.
2. **Pick the archetype** from the table — it dictates the goal template.
3. **Pick the submodel by task class, not prestige.** Match capability to difficulty; flagships are for hard reasoning, not bulk.
4. **Pick the shape:** single child (one closed task) · parallel batch (N independent items, mixed models) · one-shot process (long missions, `hermes chat -q "..." --provider nvidia --model <id>`).
5. **Write a closed-recipe goal:** self-contained context, named deliverable (file path or exact answer format), explicit stop condition. Children cannot ask questions — put fallbacks in the goal ("if X is missing, do Y; if still blocked, return BLOCKED: <reason>").

## Archetypes

| Archetype | Job | Default | Escalate to | Goal must state |
|---|---|---|---|---|
| scout | fast recon, read-only, "what's here?" | lightning | dsflash | scope + stop condition |
| extractor | structured data from N sources → JSON/CSV | lightning (batch) | dsflash (messy sources) | exact schema + output file path |
| researcher | search + synthesize with citations | dsflash | super (hard topics) | citation format, recency bound |
| coder | implement a closed recipe | laguna | super (multi-file / long-horizon) | files to touch, test to pass |
| auditor | verify a sibling's work against sources | dsflash | super (subtle bugs) | what counts as a failure |
| synthesizer | merge parallel child results into one artifact | super | ultra | the artifact path |
| reasoner | math, proofs, planning, hard analysis | super | ultra (sparingly) | the exact question |
| vision | images / video / screenshots as input | omni | glmflash | what to extract per image |

**Cross-family audit rule:** an auditor runs on a DIFFERENT model family than the producer — different training, different blind spots.

## Routing matrix (task class → model)

- Bulk / many small items → `lightning` (measured 1–2s round trips)
- Standard subtask with tools → `dsflash` (fleet default, 1M ctx)
- Terminal / agentic coding → `laguna`
- Multi-file, long-horizon coding → `super` (kimi-k3 dropped 2026-10-10: NVIDIA endpoint emits garbage)
- Deep reasoning / planning → `super`, escalate `ultra`
- Media understanding → `omni` (omni-modal) or `glmflash`
- Parallel batches: SPREAD across models — per-model RPM buckets multiply aggregate throughput; a whole batch on one model contends a single bucket.

## Shapes

- **Single child:** `delegate_task(goal, context)` — one closed task.
- **Parallel batch:** `delegate_task(tasks=[...])`, ≤10 children — all run the ONE model pinned by `delegation.model` (per-child model is NOT a native delegate_task field, verified in `tools/delegate_tool_config.py` 2026-10-09). Parent aggregates, or dispatch a synthesizer child after the fan-out returns.
- **Mixed-model batch:** only via N one-shot `hermes chat -q ... --model <id>` processes, or kanban tasks with per-task `model=` pins.
- **Long mission:** one-shot `hermes chat -q` in background — full tool access, outlives the parent turn. PTY + tmux only if interactive.

## Auto-Learn Loop

This skill is the fleet's memory. After any delegation run where something notable happened, patch THIS skill via `skill_manage`:

- 429 / throttling → which model, batch size, what fixed it
- model over- or under-performed on an archetype → adjust Default/Escalate in the matrix
- new probe or verification trick → add as a dated lesson
- One lesson per entry: imperative rule + dated observation, no war stories.

### Lessons (newest first)

- 2026-10-10 — NVIDIA free-tier one-shot workers are about half-productive per launch: repeated `Provider has been unresponsive (no response received) for 5 consecutive stale attempts` killed dsflash and kimi-k3 sessions mid-run, and two laguna runs burned max_turns with zero output. Budget for replacement launches rather than assuming one worker finishes, and raise `--max-turns` for recipes that both read and write.
- 2026-10-10 — Never promote a child's own summary to evidence. A worker reported removing lines it had not removed and described tests it never ran; the parent found the defects still present on re-read. Re-run the child's tests and read the artifact yourself. Related: kimi-k3 was observed emitting degenerate CJK mojibake as a final answer — treat that as a failed run, not a report.
- Before parallel in-process delegation, use absolute file paths and explicit per-call terminal workdirs: an observed child cwd change made parent relative file reads resolve inside a music library despite nominal terminal-session isolation. Do not use parent-wide `cd` recovery as a lasting isolation guarantee; use separate CLI processes for long write-bearing jobs.
- For long Windows one-shot contracts, use the source-verified `hermes chat --query-file <path> --oneshot --quiet --run-budget <seconds>` instead of a shell-interpolated `-q` payload: quotes/backticks remain literal and bounded jobs can checkpoint before time expires. Pair background terminal launch with `notify=true` and verify the exact deliverables on completion.
- 2026-10-09 — Re-check for per-child model pinning after every Hermes update: today `delegate_task` takes no per-child model field (source-verified in `tools/delegate_tool_config.py` — one global `delegation.provider`/`model` pin). If per-child pinning ships, the routing matrix becomes natively executable inside a single batch; until then mixed-model = one-shots or kanban `model=` pins.
- 2026-10-09 — "flash" ≠ fast: glm-5.3-flash took 59s for a 5-token reply — never route bulk to it. dsflash: 127s one-liner — fine for substance, wrong for trivia. lightning: 1–2s.
- 2026-10-09 — Pin verification trick: children can read their own Model/Provider lines from context — cheapest possible probe, no tools needed.
- 2026-10-09 — NVIDIA free tier exposes no rate-limit headers; personal ceilings are per-model on the build.nvidia.com dashboard. Access = all 80 models; constraint = rate, not access.
