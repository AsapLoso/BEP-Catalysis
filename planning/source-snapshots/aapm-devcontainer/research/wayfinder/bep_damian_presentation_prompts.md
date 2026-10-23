# Prompt Pack — BEP Damian Presentation (overnight execution)

> **Companion to:** `bep_damian_presentation.md` (the map the executing chat charts — it does not exist yet).
> **Charted:** 2026-10-11 · **Owner:** Lucas van Dekken
> **Mode:** B orchestrator. One prompt per wave; a fresh session receives exactly one prompt, never two.

---

## 0. Ground truth the executing session must not re-derive

**Working dir (NOT inside Aa Project management):**
`%USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis`

**Run commands — the actual `pixi.toml` tasks are:**
`editor` · `preview` (`myst start`) · `pdf` (`myst build --pdf`) · `sanitise-bib` · `test` · `lint` · `format` · `smoke` · `review`
**There is NO `run` task and NO `ipynb` task.** Do not invoke them. To execute a notebook use
`jupyter nbconvert --execute` inside `pixi run`, or `preview`.

**The content registry is `toc.yml`, not `content.yml`.** `content.yml` does not exist.
`myst.yml` `extends: [toc.yml, export typst.yml, authors.yml, options.yml]`.

**Repo is PUBLIC on GitHub with Pages live off `main`.** `BEP_SOURCE_MAP.md` is the binding constraint:
- Reference only. Never copy private material in — not into `content/`, not "temporarily".
- **No personal names.** Not supervisors, not committee members, not "my supervisor".
- **No deadlines, submission dates, or exam dates.**
- **No committee/grading/contact data.** No emails, rooms, rosters.
- **No absolute Windows paths** — not in a file, not in `references.bib`, not in a notebook output, not in a commit message. The leak that actually bit us was Zotero auto-export writing `file = {%USERPROFILE%` into `references.bib`.

**What exists already:**
- `pbr/` — the simulation package, 10 modules, commit `e0663ba` *"Complete transient PBR catalytic framework (TVD2, radial diffusion, stiff solver, 37 passing tests)"*. Modules: `parameters` `discretisation` `model` `chemistry` `closures` `solver` `species` `sweep` `parameter_sets` `provenance`.
- `content/c2h2_hydrogenation_transient_model.ipynb` — **already built** (11 cells). This is the *pattern*, not the target.
- `content/Results.ipynb`, `content/{Index,Introduction,Theory,Methods,Conclusion,Cheatsheet}.md`
- `tests/` — `test_discretisation.py`, `test_solver.py` (37 passing)

**Notebook convention (copy it, don't invent):** one markdown cell of short prose explaining what the block does and *why the discretisation choices are what they are*, then one code cell. One cell per **logical block** (params → discretisation → kinetics → rhs → integration), never one per function. Original source order. No "Now let's…" narration.

**⚠️ ONEDRIVE — read this before diagnosing any read failure.**
This repo lives under OneDrive and most files are **cloud placeholders**. If you hit
`OSError: [Errno 22] Invalid argument`, `Permission denied` on a file that exists, or
`Error launching 'x': The cloud file provider exited unexpectedly (os error 404)` —
**it is not an ACL problem.** OneDrive is simply not running, so nothing hydrates.

Fix (and the user's standing rule — keep OneDrive OFF by default):
1. Start it: `Start-Process '%ProgramFiles%\Microsoft OneDrive\OneDrive.exe' -ArgumentList '/background'`
2. Pin the tree: `attrib +P '<repo>\*'` — **reading files alone does NOT reliably hydrate** (first attempt recalled only 14 of 52).
3. Walk + read every file, count `failed:` — pass condition is `0`.
4. Verify the real blocker is gone (`pixi run myst --version`), not just the file count.
5. **Stop OneDrive again when done** — hydrated files stay readable (verified 52/52 at 0 processes).

Known stubborn case: `export typst.yml` resisted every pin. Fix was replacing it from the
git object store: `git show HEAD:"export typst.yml"` → delete → rewrite bytes.

**The site DOES build.** Verified 2026-10-12: `pixi run preview` builds every page
successfully. It reports one real error to fix:
`⛔️ myst.yml Table of contents entry does not exist: content\Detail3.md`

**Site content state (verified):**
- `Theory.md`, `Methods.md`, `Conclusion.md` are **raw starterkit template text** — `E=mc²`, the Schrödinger equation, and *"whether and how scientific publishing is feasible through the use of Jupyter Book"*. They must be rewritten.
- `Detail2.md` = 0 bytes · `Leken.md` = 20 bytes (*"so in short we have"*) · `Detail3.md` = missing but referenced in `toc.yml`.
- Only `Index.md`, `Detail1.md`, and the two notebooks have real content. `Detail1.md` is the one real draft chapter (LHHM mechanism, 5 reactions, conservation PDE) and is the natural seed for `Theory.md`.

---

## 1. GOAL PROMPT (master — paste first, once)

```markdown
/goal BEP — Damian presentation, overnight autonomous run

Working dir: %USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis
(a sibling of "Aa Project management" on OneDrive, NOT inside it)

MISSION
Tomorrow I present to Damian. I need to show three things, honestly and in order:
  (a) the literature research we did — a lot of papers,
  (b) the thing we built — the `pbr/` simulation package and its notebook,
  (c) the choices we made along the way, and what we actually learned.
This is not a demo of working code. It is a research narrative with a build attached.

EXECUTE IN THIS ORDER
  SG-1  Chart the map (see bep_damian_presentation.md — it does not exist yet; create it)
  SG-2  Verify and finish the notebook + register it
  SG-3  Build the research → choices → implementation narrative
  SG-4  Assemble the presentation itself
  SG-5  Update the website (same substance as SG-3, aimed at the MyST book)
Then STOP at the HITL/grilling points and leave them for me in the morning.

HARD CONSTRAINTS (non-negotiable)
- The repo is PUBLIC on GitHub, Pages live off `main`. Read BEP_SOURCE_MAP.md first and obey it:
  no personal names, no deadlines, no committee/contact data, no absolute Windows paths,
  no private material copied in — not even temporarily.
- Real `pixi` tasks are: editor preview pdf sanitise-bib test lint format smoke review.
  There is NO `run` and NO `ipynb` task. The registry is `toc.yml`, not `content.yml`.
- Scoped git staging only: `git commit --only <paths>`. Never `git add -A` or a directory sweep.
- Read before you write. Every claim about this repo gets checked against the actual file.
- Tag findings: [verified] (I opened it) / [inferred] / [uncertain]. Never upgrade an inference
  to a fact by repetition. "Not found" is a valid answer.
- No file writes outside the map, `content/`, `toc.yml`, and the named narrative surfaces,
  until I approve.

HOW TO WORK
- You are the orchestrator, not the typist. Delegate mechanical work (reads, sweeps, conversions)
  to OpenCode through the harness; consume its summary. Read a file yourself only when a decision
  hinges on exact wording, and say why.
- Prefer /harness for dispatch and /harness-guardian to watch at zero token burn.
- Keep OneDrive paused during heavy I/O; leave daemons warm. Do not tear down.
- If something is genuinely ambiguous, put it in the map's Fog section rather than guessing.

BEGIN with SG-1.
```

---

## 2. SUBGOAL PROMPTS (one per wave — a fresh session gets exactly one)

### SG-1 — Chart the map

```markdown
SG-1: Chart the map.

Working dir: %USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis

TASK
Create `bep_damian_presentation.md` — a wayfinder map that gets me from where I am to a
presentation I can give Damian tomorrow. Do NOT overwrite any existing map; this is a new one.

The map's DESTINATION is the presentation, stated as verifiable end states. Candidate shape:
  D1  A presentation artifact exists, readable in one sitting, that tells the research → choices
      → build story without any private material leaking into the public repo.
  D2  Every claim in it is traceable: a paper in references.bib, or a module/test in pbr/.
  D3  It survives the BEP_SOURCE_MAP.md constraints (no names, no dates, no paths).
  D4  It is honest about what is NOT done and what we learned from the interruptions.

CONTEXT YOU MUST GROUND FIRST (do not assume)
- `pbr/` — 10 modules, newest commit e0663ba. Read module docstrings; that is where the
  design decisions are recorded.
- `content/c2h2_hydrogenation_transient_model.ipynb` — the existing notebook, already built.
- `content/{Introduction,Theory,Methods,Results,Conclusion}.md` + `Results.ipynb`
- `references.bib`, `bib_crosscheck_report.md`
- `AGENTS.md` (this repo's), `BEP_SOURCE_MAP.md`, `toc.yml`, `myst.yml`
- The 37 passing tests in `tests/` — these are evidence of what actually works.

SHAPE
- Tickets across islands. Use the exact grammar `WayfinderMap.from_markdown` parses:
  `- [ ] **Title** (wayfinder:type) — *Question: …?*` — no trailing text in the parens,
  no asterisk in a title or question.
- HITL/grilling tickets are the ones I answer tomorrow. Mark them clearly and leave them OPEN.
- A Fog section for what cannot be specified yet.

DELIVERABLE
The map file, plus a one-screen summary: island count, ticket count, how many are HITL
(those are mine tomorrow), and which are unblocked for tonight.
STOP after charting. Do not start executing.
```

---

### SG-2 — Notebook: verify, finish, register

```markdown
SG-2: Notebook — verify, finish, register.

Working dir: %USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis

TASK
1. `content/c2h2_hydrogenation_transient_model.ipynb` already exists (11 cells). Verify it:
   - Does it execute top-to-bottom? Run it for real:
     `pixi run jupyter nbconvert --execute --to notebook --inplace content/c2h2_hydrogenation_transient_model.ipynb`
     (There is no `ipynb` pixi task — do not invoke one.)
   - Report the real output. If a cell fails, FIX it rather than leaving it unrun.
2. Confirm it is registered in `toc.yml` under the right key names — read a sibling entry and
   copy its schema exactly. Do not invent fields. (`content.yml` does not exist; `toc.yml` is
   the registry.)
3. Check the notebook against the repo's public-repo constraints: no absolute paths in cell
   outputs, no personal names, no dates. Notebook outputs are committed and published.
4. If the notebook should reflect the `pbr/` package rather than inline code, say so as a
   finding with evidence — do NOT silently rewrite it. The existing 5-section inline structure
   (Parameters / Discretisation & Indexing / Kinetic Laws / ODE System / Execution) is the
   established convention; a rewrite is a decision for me.

CONSTRAINTS
- Real pixi tasks: editor preview pdf sanitise-bib test lint format smoke review.
- Scoped staging: `git commit --only <paths>`.
- If you must edit, keep the one-markdown-then-one-code block convention, one cell per logical
  block, original source order, no "Now let's…" narration.

REPORT: exact path(s) written · the exact command that ran it · pass/fail of the end-to-end
execution with the real output · any finding about inline-vs-package.
```

---

### SG-3 — Research → choices → implementation narrative

```markdown
SG-3: Build the research → choices → implementation narrative.

Working dir: %USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis

TASK
Produce the narrative spine of the presentation: what we read, what we decided, what we built,
and what we learned. This is the substance; SG-4 makes it presentable.

Produce, as markdown in `content/` (pick names that fit the existing convention):
1. **The research** — what the literature actually says. Source it from `references.bib` +
   `bib_crosscheck_report.md`. For each thread: the claim, the source, and whether we adopted,
   adapted, or rejected it.
2. **The choices** — the modelling decisions and WHY. The `pbr/` module docstrings are the
   record; `test_discretisation.py` is the evidence. Cover at minimum: the discretisation scheme
   (TVD2), the radial diffusion treatment, the stiff solver choice, and the closure assumptions.
   Each choice gets: what we chose · what the alternative was · why · how we know it works.
3. **What we learned** — including the interruptions. The process started and was interrupted by
   bug reports; that is part of the honest story, not something to hide. What did the bugs teach?
4. **What is NOT done** — stated plainly. Damian will respect this more than a polished fiction.

CONSTRAINTS
- Every claim traceable to a paper or a module/test. Tag [verified]/[inferred]/[uncertain].
- BEP_SOURCE_MAP.md: no personal names, no deadlines, no absolute paths, no private material.
- Do not invent results. If the tests do not cover something, say so.

REPORT: files written · the decision table (choice → alternative → why → evidence) ·
explicit list of gaps and what is uncertain.
```

---

### SG-4 — Assemble the presentation

```markdown
SG-4: Assemble the presentation for Damian.

Working dir: %USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis

TASK
Turn SG-3's narrative into something I can actually present tomorrow. Choose the form the repo
supports — it is a MyST book (`myst.yml`, `preview`/`pdf` tasks, typst export configured), so a
MyST page or a slide deck built from it both fit. State your choice and why.

Requirements
- Reads in one sitting. Leads with the research, then the choices, then the build, then what we
  learned. Ends with what is not done.
- Damian is a supervisor, not a reader of the code. Explain what the code MEANS, not how it is
  written. Every technical term earns its place or is cut.
- The existing notebook (`content/c2h2_hydrogenation_transient_model.ipynb`) is the visual
  centerpiece — reference it rather than duplicating it.
- If it builds, prove it: `pixi run preview` or `pixi run pdf`. Report the real output.

CONSTRAINTS
- BEP_SOURCE_MAP.md applies to every word: no names, no dates, no paths, no private material.
  This goes on a public site.
- Scoped staging only.
- No filler, no "Now let's…", no unearned enthusiasm. Direct register.

REPORT: the artifact path · the command that built it and its real output · what is still
missing that only I can supply.
```

---

### SG-5 — Update the website

```markdown
SG-5: Update the website.

Working dir: %USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis

The site is a MyST book, deployed to GitHub Pages on every push to `main`
(`.github/workflows/deploy.yml`, base URL `/Methanol-Catalysis/`). It builds today, but most
of `content/` is still the starterkit template.

⚠️ FIRST: this repo lives under OneDrive and most files are cloud placeholders. If you hit
`Errno 22`, `Permission denied` on a file that exists, or `cloud file provider exited
unexpectedly`, it is NOT an ACL problem. Start OneDrive
(`%ProgramFiles%\Microsoft OneDrive\OneDrive.exe`), pin with `attrib +P '<repo>\*'`,
read-walk and count `failed: 0`, verify `pixi run myst --version`, then STOP OneDrive again.
Reading alone does not hydrate — pinning is what works.

FIX THESE (all verified):
1. `toc.yml` references `content/Detail3.md` which does not exist. The build reports it:
   `⛔️ myst.yml Table of contents entry does not exist: content\Detail3.md`
   Either create it with real content or remove it from the toc. Do not leave it broken.
2. `Theory.md`, `Methods.md`, `Conclusion.md` are RAW STARTERKIT TEXT — `E=mc²`, the
   Schrödinger equation, and "whether and how scientific publishing is feasible through
   the use of Jupyter Book". Rewrite all three from real material.
3. `Detail2.md` = 0 bytes · `Leken.md` = 20 bytes ("so in short we have").
   Fill them or drop them from the toc. Never ship an empty page.

WRITE, from real sources:
- `Theory.md` — the physics. Seed: `Detail1.md` (LHHW mechanism, the 5 reactions, the
  conservation PDE). Add Danckwerts BCs and the dimensionless groups.
- `Methods.md` — the numerics. Seed: `pbr/` module docstrings + `test_discretisation.py`.
  Cover MOL, the TVD2 scheme, radial diffusion, and the stiff-solver choice.
- `Conclusion.md` — honest: what we learned, what is NOT done.
- `Leken.md` — the plain-language version, if it is meant to exist. Ask rather than guess.

VERIFY
- `pixi run preview` — every page builds, zero `⛔️` errors.
- Sweep for template residue: no starterkit strings left in `content/`.

CONSTRAINTS
- User has cleared names and paths for this public repo. Do not publish real secrets
  (there are none — verified). Everything else is the owner's call.
- Scoped staging only: `git commit --only <paths>`.
- Do not restructure the toc beyond fixing what is broken — the thesis shape is deliberate.

REPORT: files written · the build output · remaining toc errors (should be zero) ·
what still needs my decision.
```

---

## 3. HITL / grilling tickets — leave for the morning

Do **not** let a worker answer these. They are the owner's calls:

- Which literature threads to *lead* with vs footnote — the presentation's emphasis is a judgement call.
- How candid to be about the interruptions. (Owner's instinct: candid. Confirm the depth.)
- Whether the notebook should be rewritten to import `pbr/` instead of inlining, or left as the
  established inline pattern.
- The presentation form: MyST page vs slide deck.
- Anything in the map's Fog section.
- What, if anything, gets published vs stays local.

---

## 4. Handback

The executing session ends each wave with a **Phase Rapport**: deliverables · evidence
(real command output) · commit SHA if committed · the next prompt ready to dispatch.
Conclude only when the frontier holds nothing but HITL tickets.
