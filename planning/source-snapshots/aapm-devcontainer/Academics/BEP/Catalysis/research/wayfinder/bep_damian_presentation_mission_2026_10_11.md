# BEP Mission: Damian Presentation Prep & Methanol-Catalysis Notebook Conversion

**Date:** 2026-10-11  
**Target:** Presentation & progress briefing for supervisor Damian  
**Related Wayfinder Map:** [`damian_briefing_2026_10_09.md`](damian_briefing_2026_10_09.md) and [`bep_catalysis_master.md`](bep_catalysis_master.md)

---

## 1. High-Level Objective
Prepare a solid presentation/update for supervisor Damian:
- Explain what the code and research mean in physical and mathematical terms.
- Articulate what has been learned, verified, and what the known defects/modelling choices are (e.g. defect register D1–D6).
- Autonomous overnight execution path: Wielder / Harness / Harness Guardian (Mode B orchestrator, starting with `@explore`).

---

## 2. Concrete Starting Task: Methanol-Catalysis Simulation Notebook

**Working Directory:** `Methanol-Catalysis` (sibling repo to `Aa Project management` on OneDrive, NOT inside it).

### Step 1: Check Config
Read `Methanol-Catalysis/pixi.toml`.
- Note: `Aa Project management/pixi.toml` has an EMPTY `[tasks]` block (`pixi run preview` and `pixi run ipynb` fail there).
- Confirm which of the three invocations `Methanol-Catalysis/pixi.toml` actually defines (`run` / `preview` / `ipynb`) before assuming — do not guess.

### Step 2: Locate Simulation Script
Locate the new BEP simulation script in `Methanol-Catalysis` (the recently-added `.py` used for the catalysis simulation).
- Report its exact relative path and byte size first.

### Step 3: Convert `.py` to `.ipynb`
Split along natural sections — one cell per logical block:
- Parameters (`params`)
- Discretisation
- Right-hand side equations (`rhs`)
- Numerical integration
- Diagnostics & outputs
*(Not one cell per function; preserve original source order).*
- Add clear Markdown cells between sections with short prose explaining:
  - What each block does physically/numerically.
  - Why the discretisation choices were made.
- Strict anti-slop: No filler, no narrative fluff ("Now let's...").

### Step 4: Save Notebook
Save as `<script_name>.ipynb` INSIDE the `Methanol-Catalysis` map (alongside the `.py`, or in its `notebooks/` directory if one exists — follow the repo's existing convention).

### Step 5: Register in `content.yml`
Register the notebook in `content.yml` in `Methanol-Catalysis`:
- `title`
- `description` (one-line)
- `path`
- `run` command
*(Match existing entries' key names exactly — read a sibling entry and copy its schema, do not invent fields).*

### Step 6: Verify Execution
Execute top-to-bottom:
- Run via `pixi run <ipynb task>` or `jupyter nbconvert --execute`.
- Report real numerical output and diagnostics.
- If a cell fails, debug and fix rather than leaving it unrun.

### Output / Report Contract:
1. Exact paths written.
2. The exact command that executed the notebook.
3. Pass/fail status of the end-to-end execution with real numerical outputs.
