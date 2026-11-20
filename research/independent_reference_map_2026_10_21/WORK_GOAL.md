# Work goal — Independent BEP scientific reference map (complete package)

**Use this work package as the primary task specification:**
- [Source guide](SOURCE_GUIDE.md) — verified exact source paths, reading order and source reliability.
- [Data contract](DATA_CONTRACT.md) — complete machine-readable graph, scientific provenance and validation criteria.
- [Execution plan](EXECUTION_PLAN.md) — phased research, acceptance checkpoints, deliverables and stopping condition.

**Repository:** `AsapLoso/project-management-agents` (private).  
**Base branch:** `experiment/bep-independent-science-map-20261021` **only**.  
**Cloud Work head branch:** create a fresh `work/bep-independent-reference-v1-...` branch *from this experimental branch* and commit there.  
**PR target:** `experiment/bep-independent-science-map-20261021` **not** `main` or `devcontainer`. Do **not** auto-merge.  
**Output directory:** `Academics/BEP/Catalysis/research/independent_reference_map_2026_10_21/`.

## Mission

Build a **new, intellectually independent, deeply organized, evidence-grounded AI scientific reference map** from the original Bachelor End Project proposal and relevant primary science. The BEP concerns dynamically forced selective acetylene semi-hydrogenation in a packed-bed reactor.

**The result is scientific DATA and explanatory scientific knowledge, NOT a rewritten UI, a parser migration, a visual demonstration, an administrative inventory, or a superficial heading list.** Author substantive physical and mathematical nodes whose science can be inspected, challenged, expanded and later visualized.

## Start by reading these exact files

1. `Academics/BEP/Catalysis/0_Project_Management/main.tex` — main proposal, its research problem/questions, embedded literature and methodology, modelling, scope, planned validation.
2. `Academics/BEP/Catalysis/0_Project_Management/references.bib` — bibliography and research-paper locators.
3. `Academics/BEP/Catalysis/0_Project_Management/section1_intro.tex` — standalone intro.
4. `Academics/BEP/Catalysis/0_Project_Management/section2_lit.tex` — standalone literature section.
5. `Academics/BEP/Catalysis/0_Project_Management/section3_method.tex` — standalone methodology.
6. `Academics/BEP/Catalysis/0_Project_Management/bep_proposal_roadmap.md` — contextual scope and planning only, not independent scientific evidence.

The main proposal embeds its own sections, so the standalone files can represent **different revisions**. Compare and report differences where relevant. Investigate original papers pointed to by the bibliography rather than using the proposal's claims as unquestioned experimental facts. Follow `SOURCE_GUIDE.md` for source reliability.

Read root `AGENTS.md` and `.agents/AGENTS.md` for repository operational rules; use the map authoring and general reversible-change skills for authorization, scoped commits, diff/revert mechanics and safe remote synchronization. Treat operational/project-management context as workflow instructions, **not as evidence about the scientific taxonomy**.

## Research plan

**Stage 0 — reconstruct the scientific problem.** Extract the reactor physics, inputs/outputs, hidden variables, reaction network, conservation principles, assumptions, mathematical structure, proposed temporal control and experimental evidence limits. Identify source-specific model claims and hypotheses.

**Stage 1 — establish the first two layers.** The user specified precisely three scientific first branches: **Physics**, **Mathematics**, **Systems & Control**. Independently derive appropriate second-layer themes directly from proposal/scientific research; no prescribed fifteen themes or fixed count. Provide boundaries and cross-links.

**Stage 2 — build increasingly deep, meaningful scientific nodes.** Develop the underlying science of all three disciplines, not just topic labels. Explain governing equations/variables/units, surface mechanism and coverage assumptions, transport and reactor model, PDE numerics, stability/inverse problems, measurements/experimental validation, inputs/identifiability/optimization, and pertinent supporting foundations. Use arbitrarily many levels where conceptually warranted. Do not invent numerical calibration or measured performance.

**Stage 3 — attach and audit evidence.** Populate source references and exact locators, label claims as published/derived/proposal-hypothesis/inference/open, identify contradictions and missing source access, and explain catalyst/operating-regime applicability. AI reference nodes may be **Idea (grey)** or **AI worked out (yellow)** only; never mark as owner understood or human-verified.

**Stage 4 — freeze and report independent v1.** Validate the graph, sources, cross-links, model assumptions and statuses; commit a versioned baseline, push and read back the remote state. Open a PR from your fresh Work branch **to this experiment branch**. Report structured scientific coverage, major gaps, tested checks and the actual frozen commit SHA. Stop without merging.

This research sequence is a **guideline**, not a rigid waterfall. Revise the taxonomy if physics or source material reveals a better classification. No fixed node quota or depth ceiling; stay closely anchored to the original BEP rather than creating an arbitrary encyclopedia.

## Required artifacts

Write scientific files **only in this directory** (except optional isolated test tools/validation needed for these files):

- **`nodes.yaml`** — new stable-ID, single-parent, source-linked scientific hierarchy across all three disciplines.
- **`sources.yaml`** — bibliography, exact claim support, access/applicability status.
- **`method.md`** — independent taxonomy rationale, model boundaries, source and proposal revision selection.
- **`uncertainties.md`** — unresolved evidence and scientific hypotheses/assumptions.
- **`progress.md`** — actual completion, stage milestones and next substantive science cursor.
- **`validation.md`** — syntax, integrity, evidence and test results, with unrun tests acknowledged.

Use `DATA_CONTRACT.md` for machine-readable field meanings, source IDs and optional additional science artifacts. Preserve a readable, self-contained dataset with unlimited natural depth, not a hard-coded app-specific representation.

## Non-negotiable execution conditions

- Work **solely from the experiment branch**; create a fresh Work head branch from it. **PR base must be this experiment branch.**
- Use cloud/GitHub; no local-PC sync necessary.
- Do not change existing frontend/parser/editor, unrelated science source files or personal understanding data.
- No human/blue upgrades, human citation verification claims, or personal-map write without explicit owner permission.
- Produce **one substantial, scientifically meaningful initial v1**, not merely a plan or unpopulated schema. Make useful progress across all three disciplines, with a clear quality/coverage report.
- Diff-check and commit logically; validate YAML IDs/parents, graph connectivity, no cycles, no bogus cited claims, and compatibility of source IDs. Don't assert a test ran unless it actually did.
- **STOP after creating the PR and reporting the frozen independent v1.** Any later comparison or dataset reconciliation will be a separate assignment.

**Deliverable standard:** a traceable, original scientific understanding of the proposal's research territory, expressed as well-structured reusable data.
