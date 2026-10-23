# Hermes mission — Execute BEP Wayfinder frontiers (13 October 2026)

**Mission type:** autonomous ticket execution, verification, reconciliation and handoff. **NOT** another map-construction exercise or an unverified literature summary.

**Urgent outcomes:** prepare Lucas to explain the project to Damian van Berkel on Tuesday 13 October; supply scientifically defensible material and a presentation handoff before Wednesday 14 October 2026. Prioritize usable partial results when time or access is limited.

## 0. Load actual authority and inspect current state

Repository: `AsapLoso/project-management-agents` (private, default branch `devcontainer`). Start with `git status` and `git fetch`; inspect recent commits, active branches and parallel work before writing. Preserve local modifications. **Do not force-push or reset others' work.** Use a dedicated working branch for execution and push it; report the branch URL. Check the secondary repository `AsapLoso/Methanol-Catalysis` when relevant.

Read, **fresh and in order**:

1. `.agents/skills/wayfinder/SKILL.md`. Follow its governance, ticket types, evidence, runbooks, HITL and state-engine isolation rules. **Wayfinder plans and advances decisions; independent work must actually execute the needed investigations, prototypes and verifications.**
2. `WEDNESDAY_START_HERE.md`
3. `Academics/BEP/Catalysis/README.md`, `DOCUMENT_MAP.md`, `state.md`, `conventions.md` (where present).
4. Existing maps under `Academics/BEP/Catalysis/research/wayfinder/`: `bep_catalysis_master.md`, `damian_briefing_2026_10_09.md`, `bep_presentation_2026_10_14.md`, `scientific_method_selection.md`.
5. Relevant runbooks cited by those maps **before** running research/probes; the existing scientific dossier `research/dossiers/scientific_wayfinder_2026_10_13/`; proposal; actual modeling code, notebooks, audits and source papers.

These are navigation and historical claims, not automatic proof. Read primary sources for consequential claims. Some local-only work may be unavailable: record the access limit rather than pretending to have inspected it.

## 1. Execute, don't just describe, existing tickets

Make a **short private work queue** of unblocked, high-value tickets from the existing frontiers. Favor the Tuesday briefing evidence and Wednesday talk over long-term thesis redesign.

For each chosen ticket:

- State the concrete question, evidence needed and falsifiable acceptance test.
- For `wayfinder:research` or `wayfinder:task`, **perform** the research, code inspection, source comparison, numerical derivation or runnable probe. Consult the ticket's runbooks first.
- For `wayfinder:prototype`, build and inspect a minimal working prototype if feasible; leave appearance ratification to Lucas.
- For `wayfinder:grilling`, prepare trade-offs and a precise question for Lucas/Damian. **Never answer your own grilling ticket or mark it closed without human ratification.**
- Independently audit the work using the repository auditor/runbooks if available; otherwise reproduce via explicit commands and describe the missing independent audit.
- Only after verification: advance the map ticket with dated evidence, artifact path, command and commit reference. If genuinely blocked, record why, and continue on another island.
- Do not create a new Wayfinder or change one map's destination to bundle unrelated objectives. Respect the repo's state-engine isolation: delegated workers must not edit `state.md`, `history.log`, `conventions.md` or `task.md`. Let the authorized map/state workflow make such updates.

An essay, a file created, or a test command not actually run is **not** ticket completion.

## 2. Research and reconciliation priorities

**A — Scientific question and history.** Reconstruct original proposal → primary literature → evolving modeling assumptions → existing implementations → evidence → next decisions. Original aim: test whether periodic inlet forcing could improve the selectivity/yield of acetylene semi-hydrogenation toward ethylene. Immediate model target is a reliable **open-loop transient predictor**; downstream optimization, observers, MPC and expansive DCSC work do not take precedence.

**B — Relevant primary sources.** Evaluate Berger (2008), the direct transient/periodic acetylene work (including Urmès et al. 2022), Larsen and the catalyst-specific kinetic sources as warranted. Compare equations, closures, assumptions, data and portability; inspect relevant PDF pages/tables rather than blindly trusting text extraction. Cite exact source locations and distinguish compatible vs incompatible mechanisms or parameter sets. Do not invent missing values. Follow recorded source vetoes and investigate whether newer evidence resolves them.

**C — Actual implementations.** Inspect **both** the older 1,480-coordinate Method-of-Lines script and newer modular `pbr` candidate, plus any substantive notebooks. Compare bulk/particle/surface states, transport equations, film and dispersion assumptions, boundary conditions, reaction mechanisms, inlet forcing, solver/Jacobian, sparsity and conservation. Do not assume the old model is the sole implementation or the new one is validated.

**D — Numerical evidence.** Reproduce or properly qualify the older defect register D1–D6 and later audits: in-place state mutation, spherical-centre stencil (3 vs 6), frozen shell coverage, quadrature normalization, `C_t` units/docstring and expensive finite-difference Jacobian. Verify against current source and distinguish numerical defect, legitimate modeling choice, and unit convention. The alleged double-`C_t` defect was **retracted**; do not resurrect it without new proof. Avoid portable claims about load-dependent wall-clock timings. Check trivial zero-kinetics and fixed-inlet limits before asserting any reacting periodic behavior.

**E — Cross-source synthesis.** Confront contradictions across proposal, literature dossiers, code, audits, recent handoffs and diagrams. Settle each resolvable claim with primary evidence or clearly mark `[UNRESOLVED:]`. Preserve only source-backed numerical results. Distinguish `[FACT:]`, `[DECISION:]`, `[UNVERIFIED:]` and `[UNRESOLVED:]`.

## 3. Produce usable deliverables from verified work

Write one **canonical supervisor briefing** (not a collection of duplicative agent essays) that explains:

- The question, scientific motivation and what the project proposal set out to do.
- Literature insights and exactly how they changed the modeling approach.
- Physical balances → spatial discretization → state vector → stiff solver; modeling choices vs necessities.
- Both code candidates: what each actually runs and does not run.
- Demonstrable findings with re-derivable numbers/commands, unresolved defects and physical limitations.
- Why a validated reacting periodic simulation and measured yield improvement **have not** yet been established (unless genuinely proven during this run).
- Next concrete scientific milestones and questions for Damian.

Add a concise 60–90 second **spoken research update** and a substantial **Lucas technical Q&A** (why transients/MOL/BDF, how the 1,480 coordinates arise, why surface coverage and pore transport matter, model assumptions, defects, validation criteria, status of periodic forcing, choice between implementations). Answers must be explainable by Lucas, not merely sound plausible.

Create a short **Wednesday presentation handoff**: priority narrative, source-backed figures/equations, exactly what can appear on slides, suggested honest disclaimers, and links to the existing HTML mini-deck/notebook and presentation sub-stories. Do not rebrand illustrative plots as validated reactor output.

Use well-labeled files under the existing BEP research/briefing area or another established directory. Link final outputs and evidence from the **existing Wednesday Wayfinder/coordination page** using the repo's authorized change flow.

## 4. Execution discipline, commits and exit

- Prefer independent, high-information probes over broad additional literature searches. Don't exhaust time on infrastructure or endlessly rewrite prompts.
- Work across independent islands if a human decision blocks one. If all are blocked, persist the precise questions and halt cleanly rather than silently decide.
- Never claim test execution, source access, numerical validation or GitHub delivery without receipts.
- Commit coherent, scoped changes to your working branch, fetch/reconcile concurrent changes, and push. Do not silently overwrite other agents' work.
- Report the actual executed ticket IDs, whether tests passed, evidence paths, brief and Q&A links, Git branch/commits, unresolved human decisions and the **next 3 concrete actions**.
- A useful, verified partial briefing is preferable to a perfect plan without completed research.
- If your environment cannot run persistent background tasks, say so and execute as much as it can during the active session; do not pretend work continues.

**Begin by reading the Wayfinder skill and the existing frontiers. Then investigate, verify, reconcile, write the briefing, advance eligible tickets, commit and push. The success metric is defensible progress, not document count.**
