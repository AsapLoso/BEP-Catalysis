---
name: wayfinder
description: Chart and navigate a decision map for efforts too large or ambiguous for a single session. Use when an idea has a clear destination but the route through the fog of war is still unknown.
---

# Wayfinder

Wayfinder charts an effort whose **destination** can be named, but whose route is still in the fog. It maps the journey as a series of **decision tickets**, resolving them one by one until the path is clear.

**It plans, it does not do.** Every ticket holds a question whose resolution is a *decision*, not a slice of production code to write. The map is complete when there is nothing left to decide before building begins.

---

## When to Use

| Situation | What to Run |
|---|---|
| Well-scoped task, answerable in one sitting | `grilling` |
| Route unknown, ambiguous architecture, multi-session effort | `wayfinder` |
| All decisions already made, ready to build | Write the spec / wielder prompt directly (skip map) |
| Active session grows too big / hits a wall of unknowns | Hand off to `wayfinder` |

---

## Conversational Governance Doctrine

> **"The conversation is where meaning is negotiated. The map is where settled meaning is recorded."**

1. **Persistent conversational experience? YES. Persistent LLM memory as authority? NO.**
   Do not let a long-lived LLM context window become the canonical memory of the project. Every session negotiates meaning, drills assumptions, and ratifies choices conversationally, but writes settled conclusions atomically to disk (`[FACT:]`, `[DECISION:]`, `[UNVERIFIED:]`). Future turns reload fresh contexts from the map.
2. **Three Operational Modes:**
   - **Mode 1: Map Construction** (*"What are we actually trying to accomplish?"*) — turning fuzzy human intent into structured islands and decision tickets.
   - **Mode 2: Map Audit & Grilling** (*"Why is this ticket here? What authority? Contradictions?"*) — stress-testing and attacking the map before building begins.
   - **Mode 3: Map Advancement** (*"Ticket X is verified. Island Y is blocked. What's next?"*) — interpreting independent verification receipts to advance the active frontier.

---

## The Map Structure: One Map Per Goal & Islands in the DAG

Every wayfinder map lives in `research/wayfinder/<map_name>.md` (and is linked from `state.md`). 

### Core Doctrine: One Map Per Goal
A wayfinder map is strictly scoped to **exactly ONE verifiable destination**. Do not create monolithic mega-graphs covering unrelated systems. Multiple distinct efforts receive separate goal maps (e.g. `ui_v2_streaming.md`, `sentinel_daemon.md`).

### Islands in the DAG (Semi-Independent Clusters)
Real software development does not proceed as a single linear stack. Within a map, the Active Frontier and Fog of War are partitioned into **technical islands / clusters** (`### Island: <Name>`).
- **Parallel Momentum:** If one island is blocked or awaiting review, execution continues on other independent islands.
- **Localized Fog:** Fog of War clusters around specific technical domains. Fog in one island does not block clarity in another.
- **Dynamic Edges:** Edges between islands are dynamic hypotheses. Settling a ticket on Island A may reveal or invalidate dependencies on Island B.

```markdown
# Wayfinder: <Map Title>

## 1. Destination
The verifiable end state of this journey. Written first, before any ticket exists,
because every decision is measured against it.
**Runbooks:** <path(s) to procedure docs that govern execution, or "none yet">

## 2. Decisions So Far
- [x] **<Decision Title>**: <One-line summary of the decision made, date, and link to evidence/dossier/rapport>.

## 3. Active Frontier
The open, unblocked questions you can state precisely NOW, grouped by technical island:

### Island: <Island Name A>
- [ ] **<Ticket Title>** (`wayfinder:<type>`) — *Question: <Exact formulation of the question>*
  - Status: Open / In Progress
  - Dependencies: None (unblocked)

### Island: <Island Name B>
- [ ] **<Ticket Title>** (`wayfinder:<type>`) — *Question: <Exact formulation of the question>*

## 4. Not Yet Specified (The Fog of War)
Decisions you know are coming toward the destination, but cannot formulate precisely yet, clustered by island:

### Island: <Island Name A Fog>
- *<Vague topic or downstream area>* (will become tickets once the frontier advances).

### Island: <Island Name B Fog>
- *<Vague downstream area for Island B>*

## 5. Out of Scope
Work and directions explicitly excluded from this destination.
Fog only gathers toward the destination; out-of-scope items never promote.
```

---

## The Fog Test

> **"The test for fog versus ticket is whether you can state the question precisely NOW, not whether you can answer it."**

- **If you can ask the question precisely now:** It belongs on the **Active Frontier** as an open ticket under its respective island.
- **If the question itself is fuzzy or depends on unknown territory:** It belongs in **Not Yet Specified (Fog of War)**. Do not try to plan it yet. Resolving frontier tickets pushes the frontier forward and naturally dispels the fog, promoting new concrete questions.

---

## The Four Ticket Types

Every ticket on the frontier has a type and an interaction mode:

| Type | Mode | When to Use | Resolved By |
|---|---|---|---|
| `grilling` | **HITL** | The default. A trade-off or preference to talk through. | Calling `grilling` (ask the user, present options + recommendation). |
| `prototype` | **HITL** | "How should this look or feel?" Talking won't settle it. | A quick visual or interactive artifact in `scratch/`. |
| `research` | **AFK** | An external technical fact or API contract blocks a decision. | Exploring the codebase, docs, or running a diagnostic probe. **Consult the runbooks named in the map's Destination block first — and see the Fog Test's Runbook Doctrine below.** |
| `task` | **Either** | Non-code unblocking action (verify credentials, inspect schema). | Doing the small unblocking chore to reveal the answer. |

**The HITL Rule:** The agent **never answers its own grilling questions**. A grilling ticket resolves only through live exchange with the user.

### Runbook Doctrine

A **map is a decision structure; a runbook is a procedure corpus.** They are complementary and the coupling is **one-way: maps cite runbooks. A runbook is never converted into a map.**

That asymmetry is the whole reason both are needed. A runbook records what is already known, so it **cannot surface what was never verified.** Live proof: the TW3730TU grading runbook documents the grading sheet's `Z`/`AA`/`AB` formula columns and the paste-anchor derivation procedure in detail, and still never says *check that the normalisation is actually present* — `AA` was missing its `*10` factor, silently corrupting the final grade of all 18 students across two full grading cycles. Only the map, by asking "what have we never verified?", found it.

Three operating rules:

1. **Name the runbooks in the Destination block.** A map that cites nothing cannot be checked against anything.
2. **On a `research` ticket, consult them before you explore** — and use `grep`, never `glob`, to enumerate `.agents/resources/runbooks/`. A glob on that directory returns **nothing** while 20+ runbooks are present; a worker that trusts it concludes none exist.
3. **Absence is itself a finding.** If you solve a blocker and there is no runbook for the procedure you just performed or debugged, **record that gap.** An additive instruction ("look for runbooks that add to our goal") is structurally incapable of reporting a *missing* one, and that is the case that costs the most — the two neighbouring runbooks that look right and cover something else are the "right-looking wrong document" that absorbs attention while the real gap sits empty. Per **Rule 35**, a newly debugged non-trivial procedure **MUST** be formalised into `.agents/resources/runbooks/<topic>.md` — and if you edit a runbook, add its path to the phase's `scoped_commit_files`, or it gets no byte guard at all.

---

## Non-Destructive In-Place Repair & Demotion Protocol

1. **ACID as Crash-Recovery, Not Destructive Wipe:**
   ACID guarantees are designed for crash resilience and session resumability across daemon resets, NOT destructive `git reset --hard` wipes upon critique.
2. **In-Place Repair on Auditor Rejection:**
   When an `@auditor` rejects a ticket, written code is preserved in the worker workspace. The worker receives targeted benchmark critiques and up to **2 in-place repair rounds** (3 turns total per ticket) to adjust its implementation or backtrack its own steps.
3. **Demotion to Fog on Unresolvable Blockers:**
   If a ticket remains unresolvable after 2 repair rounds, it proves the question was not actually ready for the frontier. Rather than halting the marathon, the ticket is **demoted back into the Fog of War** with a warning label:
   `⚠️ [BLOCKED: Failed benchmarks X, Y. Missing prerequisite: Z. Logs: <ref>]`
   The engine immediately pivots to other independent ready frontier tickets on different islands.

---

## The Pocock Recon-Loop (Frontier Exhaustion)

When the Active Frontier is empty but Fog of War still remains toward the destination:
1. **Never Dispatch Blind Workers into the Fog:** The fog represents unknown territory; blind coding creates technical debt.
2. **Execute Recon Probe:**
   - The engine automatically spawns an AFK **`research`** probe to explore code, inspect schemas, or query documentation.
   - If the blocker is architectural, trade-off based, or requires preference, the engine prompts a concise **`grilling`** question (HITL).
3. **Formulate & Promote:**
   Once the recon probe or grilling settles the fact, the question passes the Fog-Test and is formulated as a concrete ticket on the Active Frontier.

---

## Lifecycle: From Map to Spec & Reconciliation

1. **Chart the Map:**
   - Define the single **Destination**.
   - Partition into **Islands** (Data Stream, Shell, Gate, etc.).
   - Note the **Fog of War** per island.
   - Write the first open questions on the **Active Frontier**.
2. **Work the Frontier:**
   - Execute unblocked tickets per island.
   - Verify via falsifiable test commands and `@auditor`.
   - On green approval: move the settled question to **Decisions So Far** with date, commit SHA, and rapport link.
   - Advance the 1-hop headlight: promote newly unblocked fog items to the active island frontier.
3. **The Collapse (Handoff to Spec):**
   - When frontier tickets are formulated and ready for autonomous worker execution, Wayfinder **compiles into an `ExecutionPromptSpec`** (the 4-part prompt contract for `run_wielder.py`).
   - State Engine Isolation is strictly enforced: workers never mutate `state.md` or `history.log`.

---

## Delegated Thinking & Autonomous Map Synthesis (Rule 43/44)

When charting an effort across complex codebases, multi-repo architectures, or massive documentation dossiers (such as the BEP Catalysis thesis):
1. **Never Exhaust Supervisor Context:** The supervisor session must NOT read dozens of reference files inline to author the initial map by hand.
2. **Delegate Recon to `/harness`:**
   - Supervisor frames the Destination and target document paths (`DOCUMENT_MAP.md`, `state.md`, `toc.yml`, repo trees).
   - Dispatches a synthesis worker to OpenCode on `:4001` via `/harness` (`prompt_async`).
   - Supervised at zero chat tokens via `/harness-guardian` (`sentinel_daemon.py`).
3. **Hard State Engine Isolation:** The worker writes strictly to `research/wayfinder/<map_name>.md` and is unconditionally forbidden from touching `state.md`, `history.log`, `conventions.md`, or `task.md`.

---

## The Sandwich Grilling Structure

1. **Opener Grilling (Scoping):** Brief, interactive `/grill-me` session to align on the single destination, invariant constraints, and island boundaries.
2. **Middle Phase (Pure AFK Execution):** Multi-file exploration, map authoring, spec compilation, and autonomous worker execution proceed strictly AFK with **zero mid-run chat interruptions**.
3. **Closer Grilling (Reconciliation):** When execution completes or halts at unresolvable forks, Antigravity engages the user in a consolidated `/grill-me` session on the final trade-offs, findings, and next active frontiers.

---

## 5-Tier Question Flow-Through & Asynchronous Quiescence (ACID Sleep)

1. **Hierarchical Flow-Through (The Chain of Command):**
   **Worker $\rightarrow$ Department Manager $\rightarrow$ CEO $\rightarrow$ Guardian Angel $\rightarrow$ God (Antigravity / Human)**.
   - A Worker with an unresolvable blocker asks its Department Manager.
   - If the Department Manager cannot answer, it escalates to the CEO.
   - If the CEO cannot resolve it, it escalates to the Guardian Angel.
   - The Guardian Angel checks whether unblocked tickets remain on other islands. If yes, it instructs the CEO/Managers: *"IDK, continue execution on unblocked islands; I will ask the user when you are FULLY stuck."* Managers relay this down to their workers, keeping autonomous execution alive without stalling the marathon.
2. **Asynchronous Quiescence (ACID Sleep & Zero-Compute Standby):**
   - When all islands are blocked and nothing remains across the entire fleet but unresolved questions for the human user, the engine initiates **Asynchronous Quiescence**.
   - Active run state and blocked questions are committed atomically to disk (`ACID state`), and all worker containers cleanly shut down into cold standby. Zero tokens and zero cloud compute are consumed while the human is away.
3. **Pydantic Question Dossiers & UI Grilling:**
   - Escalated questions are validated against `QuestionModel` and written to `research/questions/phase_<N>_questions.json`, merged into `master_questions.json`.
   - The Web Control Plane renders an interactive native Pydantic grilling widget (`/grilling`) directly in the browser.
   - When the user answers: the workforce in ACID sleep wakes up via **ACID Recovery**, rehydrating the fleet right where it left off. If the user cannot answer, the question is split or demoted back to the Fog of War.

---

## Ambient Graph RAG & Anti-Aimless Research Rule

1. **Dynamic RAG Graph Memory (`middleware/graph_memory.py`):** Serves as ambient domain soil across projects. Nodes carry both conceptual summaries and physical file references (`file:///...`).
2. **Differential Graph Traversal:** Research agents dive deeper into the graph ($k$-hop neighborhood expansion) than execution workers.
3. **No Aimless Research in Fog:** Broad academic crossovers (e.g. DCSC control theory applied to chemical reactors) remain as Fog of War nodes and ambient graph memory until a settled frontier ticket reaches them.
4. **Fog-Test Compliance:** A research ticket is only promoted to the Active Frontier when a precise, falsifiable question can be formulated under the Fog Test.
