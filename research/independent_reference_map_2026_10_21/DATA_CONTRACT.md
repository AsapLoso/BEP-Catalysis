# Independent reference map — scientific data contract

This is a **fresh research dataset**, independent of current visualizer/parsing code. The first deliverable is information that can later be transformed into the viewer's accepted graph representation **without loss of scientific or provenance data**. Do not edit the existing app merely to display this prototype.

## Required artifacts

1. **`nodes.yaml`** — complete standalone tree of scientific concepts.
2. **`sources.yaml`** — bibliography/provenance ledger with source-access and applicability status.
3. **`method.md`** — scope, baseline proposal revision, hierarchy decisions, source methodology and reasoning about overlap.
4. **`uncertainties.md`** — unresolved empirical or theoretical claims, contradictions, source limitations and hypotheses.
5. **`progress.md`** — actual work completed, stage/discipline coverage, last tested commit, precise next science cursor.
6. **`validation.md`** — machine and manual checks with outcomes, error counts, and explicit **not run** labels.

Optional: `crosslinks.yaml`, `equation_index.md`, `claim_audit.md`, or a self-contained read-only Python validator if clearly helpful. The listed files form the minimum complete package.

## Suggested root document

```yaml
dataset:
  name: "BEP independent scientific reference"
  edition: "v1"
  role: "AI reference knowledge"
  scope_anchor: "Academics/BEP/Catalysis/0_Project_Management/main.tex"
  epistemic_ceiling: "ai_worked_out"
nodes:
  - id: "bep"
    parent: null
    title: "BEP scientific domain"
    kind: "root"
    maturity: "idea"
    relevance: "core"
    summary: "Research domain represented in this dataset."
    explanation: ""
    assumptions: []
    equations: []
    claim_refs: []
    related_ids: []
    open_questions: []
```

This is a **format sample**, not a proposed scientific taxonomy. Extend the schema consistently if needed and document extensions.

## Per-concept minimum

- Stable `id`, **exactly one tree `parent`**, precise `title`, kind, maturity (`idea` or `ai_worked_out` only).
- Explanation in actual scientific terms, not just a topic label; detail proportional to scientific complexity.
- Relevance `core` / `supporting` / `future_or_exploratory`, and for noncore content why it relates to the proposal.
- Theory/model equations with variable descriptions, units, assumptions and applicability where pertinent; do not force equations into a conceptual node.
- `claim_refs` identifying meaningful evidence by source ID and locator, plus `evidence_type` such as `source_observation`, `proposal_hypothesis`, `derived_under_assumptions`, `interpretation`, `unverified`.
- `related_ids` cross-links for genuine interdisciplinary connections; no duplicated subtrees needed simply because a topic spans physics and control.
- Open questions/limits, including model-specific versus generally accepted results.

**Never assign `human_worked_out` or human-verified claims.** The user did not request edits to their own understanding map.

## Per-source minimum

```yaml
sources:
  - id: "proposal_main"
    type: "project_proposal"
    path: "Academics/BEP/Catalysis/0_Project_Management/main.tex"
    title: "BEP project proposal"
    locator: "Introduction; Methodology; Research Questions"
    access_status: "full_text_read"
    verification: "ai_checked"
    applicability: "project intent, not experimental proof"
```

For primary literature include original DOI/URL and exact support details. Do not list a source as fully read when only its bibliographic entry or abstract was accessible. A missing source is better recorded as unresolved than fabricated.

## Structural checks

- One root; exactly three **user-prescribed** first-level disciplines: Physics, Mathematics, Systems & Control. They are the only predetermined subject-headings.
- No duplicate IDs, unresolved parents, cycles, orphan records, dead cross-links, or repeated node definitions with conflicting contents.
- Child depth is derived from ancestry; unlimited 7/8/9+ levels, but only where scientifically meaningful.
- Every cited source ID resolves; each significant scientific claim has source/assumption status; pressure/temperature/unit conventions are internally consistent.
- Structural and epistemic state stays AI-only; no accidental blue/personal promotion.
- YAML loads with a standard parser, remains unchanged by a read-only loader, and ideally round-trips in a **scratch copy** if a writer/parser is created.
- Changes after the first baseline must be traceable without quietly rewriting the frozen comparison baseline.

## Quality bar

Completeness is measured by **conceptual coverage and evidence**, not node count. A small number of deeply explained nodes is more valuable than a thousand shallow titles. Conversely, do not artificially stop at Level 6 or a fixed count of topics. Include explicit caveats on uncertain kinetics, dynamic memory, solver performance, and periodic-operation claims.
