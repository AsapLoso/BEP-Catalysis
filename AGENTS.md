# AGENTS.md — BEP-Catalysis Session & Operating Guide

Operating rules, execution standards, and workspace conventions for the **BEP-Catalysis** repository.

```yaml
project: BEP-Catalysis (TU Delft Double BSc Applied Mathematics & Applied Physics)
topic: Mathematical Modeling & Kinetics of Acetylene Semi-Hydrogenation in Packed Bed Reactors (PBR)
environment: Windows (PowerShell 5.1), OneDrive workspace, Python (global conda base)
derived_from: Aa Project management (core rules and operational invariants)
```

## BEP scientific-map and migration boundaries

This repository's general operating rules below remain in force. For the migrated BEP mind maps and interactive viewer, also observe these project-specific requirements:

- Start with [README.md](README.md), [STATUS.md](STATUS.md), and [MIGRATION_STATUS.md](MIGRATION_STATUS.md) when working on migrated content. Treat this as a scientific-understanding and reactor-notebook repository, not a general task tracker; original AAPM links preserve source review history.
- For scientific-map changes, follow `.agents/skills/bep-map-edit-review/SKILL.md`; for reversible Git changes, follow `.agents/skills/reversible-change-review/SKILL.md`.
- The personal map and AI reference maps are separate. Before creating, approving, reparenting, or promoting any personal-map node, show the exact proposed change and obtain explicit, scoped owner approval. Keep AI-only research and interpretations separately labelled.
- Preserve existing owner review records and source/claim provenance. An AI-attached reference is **not** a human-verified citation or proof of owner understanding.
- Distinguish derivation, passing code tests, reproduction of published model output, and experimental validation. Do not publish or send supervisor-facing scientific material without owner review.
- Migrated viewer files may still contain AAPM module paths or untested execution assumptions. Port and test them explicitly; copying code into this repository is not evidence that it runs.

---

## 1. What This Repo Is

A research, modeling, and scientific thesis repository for the Bachelor End Project (BEP) at TU Delft, bridging:
- **Chemical Engineering / Catalysis Engineering (TNW):** Transport phenomena, intra-pellet diffusion, Péclet/Damköhler scaling, and non-linear Langmuir-Hinshelwood kinetics.
- **Applied Mathematics / Numerical Analysis (EEMCS / DIAM):** Dynamic 1D spatial + 1D temporal continuum reactor modeling, Method of Lines (MOL), stiff ODE/DAE solvers (BDF/Radau), and parameter sensitivity.

---

## 2. Core Operating Principles & Verification

### Rule 16 — Zero-Hallucination Citations & Literature Grounding
- **Never generate, suggest, or cite a paper, author, or reference key without verifying it** against a primary source (PDF, file search in repository, Zotero library, or academic database).
- **No blind citations:** When citing a mechanism or numerical parameter, extract and verify the exact passage from the source document first.
- Placeholder citations, plausible-looking author lists, and invented DOIs are strictly prohibited.
- If a citation or parameter cannot be verified, state the gap explicitly. A documented unknown is standard science; an invented citation is catastrophic.

### Rule 36 & Rule 41 — Verify Before Asserting & Grounded Claims
- Never state claims about system parameters, kinetics, model outputs, file contents, or test results without directly verifying them via live commands, code execution, or primary files.
- External feeds, web search summaries, and LLM outputs are **reference context, not ground truth**. Verify claims against primary code and source files before committing to them.
- Do not assert that a file was modified, a script succeeded, or a value was corrected without having observed the actual tool/command output.

### Rule 15 — Anti-AI Humanized Writing
When authoring scientific prose, proposals, documentation, or commit messages:
- **Eliminate AI buzzwords:** *delve, tapestry, pivotal, crucial, robust, landscape, beacon, testament, fostering, comprehensive*.
- **No significance inflation:** Avoid trailing participle clauses (e.g. *"...highlighting the pivotal importance of X"*), empty throat-clearing, and formulaic conclusions.
- **Clean academic voice:** Use plain verbs, active voice, and concise sentences.
- **Structure over fluff:** Use clean LaTeX/Markdown markup (`itemize`, `enumerate`, headers, bold parameter names) to structure arguments cleanly rather than filling pages with dense prose.

### Rule 43 — Operational Agency & Anti-Helplessness
- **You are not helpless.** Never instruct the user to manually run commands, inspect directories, or start background processes if execution tools are available.
- Discover executables, invoke PowerShell/CLI commands directly, inspect outputs, and resolve obstacles autonomously.
- At turn completion, report verified findings with clear, actionable next steps.

### Rule 42 — Trade-offs Belong to the User
- Present technical, mathematical, and modeling choices with explicit trade-offs and alternatives.
- Do not make unilateral assumptions or silent design shifts on project scope, model assumptions, or research direction without user confirmation.

### Candidate Methods Framing
- When proposing mathematical or physical techniques (e.g., Method of Lines, flux limiters, Upwind schemes, BDF vs. Radau solvers, Langmuir-Hinshelwood formulations), **always frame them as candidate methods / potential frameworks to evaluate**, not as locked-in commitments.

---

## 3. Python Execution & Environment (Rule 19)

- **Standard Environment Tool:** Python runs directly via the global conda base environment. Execute all Python scripts via:
  ```powershell
  python <script.py>
  ```
- **Never run inline Python:** Never execute multi-line code via `python -c "..."`. Shell escaping and PowerShell newline handling introduce subtle errors. Always write to a dedicated script (use a gitignored `scratch/` folder for throwaways) and execute the file.
- **Windows UTF-8 Guardrail:** Any script handling file I/O, literature data, or text with diacritics must start with:
  ```python
  import sys
  if hasattr(sys.stdout, 'reconfigure'):
      sys.stdout.reconfigure(encoding='utf-8')
  ```
- **Package Installation:** Adding required scientific packages via `conda install` or `pip install` inside the global conda base environment is permitted when needed.

---

## 4. Mechanical Tool Safety & Editing Hygiene (Rules 37 & 39, §5.3)

### Edit Anchor Integrity (Rule 37)
- The `edit` tool matches `oldString` **byte-for-byte**.
- **Anchors:** Prefer single-line anchors. Re-`read` the file immediately before editing. Never include trailing whitespace in an anchor.
- If `edit` fails with `Could not find oldString`, **re-read the file immediately** to inspect current line endings and formatting—do not guess or retry cosmetic variations.

### Prefer `edit` Over `write` (Rule 39)
- `edit` enforces optimistic concurrency: if the file changed since it was read, the edit safely fails.
- `write` blindly overwrites the entire file and can silently destroy concurrent work. Reserve `write` exclusively for creating new files.

### Windows Path Hygiene
- Never type a Windows user profile path from memory. `$env:USERPROFILE` is authoritative (`Write-Output $env:USERPROFILE`).
- Always prefer **relative paths** for repository targets (`filePath`, `workdir`, scripts).
- Keep all paths portable across environments.

### PowerShell Byte Guard on File Writes (§5.3)
- Writing markdown or LaTeX through PowerShell double-quoted here-strings (`@"..."@`) will expand backslash-letter sequences into real control bytes (e.g. `` `a `` becomes `0x07`, `` `t`` becomes `0x09`, `` `r `` becomes `0x0D`), silently corrupting equations and text.
- Use native file creation tools (`write_file`, `edit_file`) or verbatim single-quoted here-strings (`@'...'@`).

### PDF Extraction
- LLM text-read tools cannot read raw binary PDF files. Use Python utilities (`pypdf`, `pdfplumber`, `pypdf2`) or command-line extractors (`pdftotext`) to extract text and tables before reading.

---

## 5. Git Discipline & Repository Hygiene (Rules 13, 27, 40)

- **Scoped Staging Only:** Stage explicit paths. Never use indiscriminate global staging (`git add .`, `git add -A`).
  ```powershell
  # Correct
  git add Code/solver.py README.md
  git commit -m "model: implement BDF time-stepping for packed bed reactor"

  # Forbidden
  git add -A
  git add .
  ```
- **Stop-List / Secret Hygiene:** Never stage or commit:
  - Credentials, tokens, or environment files (`.env`, `*.env`).
  - Machine-specific absolute local paths containing user profile or organisation names (e.g. `C:\Users\...`, `OneDrive - Delft...`).
  - Large binary data, temporary solver caches, or untracked scratch scripts.
- **Push Protection:**
  - Never push without explicit instruction from the user naming the action and branch.
  - Never run destructive flags: `--force`, `-f`, `--mirror`, `--delete`.
  - Never perform history rewrites (`rebase -i`, `filter-branch`, `commit --amend` on pushed commits) without explicit direction.
- **Never Assert an Unproven Mutation (Rule 40):** Verify state mutations using `git status` or file checks before reporting them as completed.
- **Commit Frequency:** Commit at the end of turns following verified state changes. Omit git commits on purely informational or read-only turns.

---

## 6. State vs. Knowledge & Finding Persistence (Rules 2, 9, 25, 26)

- **State vs. Knowledge (Rule 9):** Keep active task and status trackers strictly focused on current open loops and immediate next actions. Reference material, literature data, equation derivations, and meeting notes belong in dedicated reference files (e.g. `resources.md`, `conventions.md`, or topic subfolders).
- **Finding Persistence (Rule 26):** When a key physical parameter, numerical tolerance, kinetic rate constant, or architectural decision is verified, record it in the appropriate persistent documentation file—never leave it buried in a transient chat transcript.
- **Draft Provenance (Rule 25):** Retain generated drafts and record rationale for substantial revisions so scientific context is never lost.

---

## 7. Language Policy

- **English by default:** All code, docstrings, mathematical derivations, commit messages, agent documentation, and scientific thesis text are strictly in **English**.
- **Dutch strictly for Dutch institutional correspondence:** Dutch is permitted exclusively when drafting formal correspondence directed to Dutch university contacts (e.g., Board of Examiners / Examencommissie, TU Delft departmental coordinators) as appropriate.

