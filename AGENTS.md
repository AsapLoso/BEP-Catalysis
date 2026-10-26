# AGENTS.md — BEP-Catalysis Session & Operating Guide

Operating rules, execution standards, and workspace conventions for the **BEP-Catalysis** repository.

```yaml
project: BEP-Catalysis (TU Delft Double BSc Applied Mathematics & Applied Physics)
topic: Mathematical Modeling & Kinetics of Acetylene Semi-Hydrogenation in Packed Bed Reactors (PBR)
environment: Local Windows/PowerShell or cloud Linux; verified Python interpreter (Conda when present, otherwise compatible venv/Python)
derived_from: Aa Project management (core rules and operational invariants)
```

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

- **Environment-aware, not Conda-only:** Identify the actual OS, working directory, available `python`/`python3` and `conda`, and project dependency files *before* choosing an interpreter. The owner's **local Windows** default is the existing global Conda base **when installed and usable**; a remote Linux/cloud agent is **not required** to have Conda or access to OneDrive. Missing `conda` alone is **not** a reason to mark numerical work BLOCKED.
- **Choose a reproducible interpreter:** Prefer the project's declared environment if available. Otherwise, in remote/cloud work use a compatible installed Python or create a project-local, gitignored virtual environment (e.g. `.venv`) when permitted. Keep installs isolated to the selected environment; do not overwrite existing environments. Execute scripts with that same interpreter (`python <script.py>`, `python3 <script.py>`, or the virtual environment's Python executable). Never claim a numerical result was rerun without actual execution.
- **Never run inline multi-line Python:** Avoid `python -c "..."` for program logic; shell escaping and PowerShell newline handling can corrupt code. Write executable snippets as dedicated `.py` files (use gitignored `scratch/` for throwaways) and execute the script. Use the same chosen Python interpreter for Jupyter/notebooks and check that the active kernel matches.
- **Reproducibility receipt required for numerical work:** Record OS, interpreter path and version, selected environment, key package versions, install commands/dependency changes, exact script/notebook execution command, tolerances, and Git commit. Separate source inspections, historical saved notebook outputs, and genuinely new computations.
- **Dependencies and truthful blocking:** When packages are missing, install them *only in the selected isolated environment or the already-authorized local Conda base*, where permitted; prefer existing repository dependency specifications. If the necessary runtime genuinely cannot be made available, report the attempted alternatives and exact blocker, mark **numerical execution** BLOCKED, and continue source/transcription analysis independently. Do **not** silently change physical model assumptions, drop tests, or substitute old notebook outputs to claim PASS.
- **Windows/UTF-8 guardrail:** For scripts handling literature text, numerical files or diacritics, include when applicable:
  ```python
  import sys
  if hasattr(sys.stdout, 'reconfigure'):
      sys.stdout.reconfigure(encoding='utf-8')
  ```
  Platform-specific PowerShell, local-user-path and OneDrive instructions elsewhere in this file apply **only** in environments where those features actually exist.


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

