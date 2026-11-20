# G6 — BEP Damian presentation + site update (the overnight one)

**Status:** 🟢 **LIVE — the big one**
**Anchors:** `Methanol-Catalysis` repo · `research/wayfinder/bep_damian_presentation_prompts.md`
**Working dir:** `%USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis`
**(a sibling of `Aa Project management` on OneDrive — NOT inside it)**

---

## The goal

Tomorrow the owner presents to **Damian**. He must be able to show, honestly and in order:

1. **The literature research** — a lot of papers
2. **The thing we built** — the `pbr/` simulation package and its notebook
3. **The choices we made**, and what we actually learned

This is **not** a demo of working code. It is a research narrative with a build attached.
The process started and was **interrupted by bug reports** — that is part of the honest story.

## Full prompt set

**`research/wayfinder/bep_damian_presentation_prompts.md`** — one goal prompt + SG-1…SG-5,
plus a Ground Truth section. A fresh session receives exactly one prompt, never two.

| Subgoal | What |
|---|---|
| SG-1 | Chart the map (`bep_damian_presentation.md` — does not exist yet) |
| SG-2 | Verify + register the notebook |
| SG-3 | Research → choices → implementation narrative |
| SG-4 | Assemble the presentation |
| SG-5 | Update the website |

## Verified state — do NOT re-derive

- **The site builds.** `pixi run preview` builds every page. One real error:
  `⛔️ Table of contents entry does not exist: content\Detail3.md`
- **Template residue:** `Theory.md`, `Methods.md`, `Conclusion.md` are **raw starterkit** —
  `E=mc²`, the Schrödinger equation, *"whether and how scientific publishing is feasible
  through the use of Jupyter Book"*.
- **Empty stubs:** `Detail2.md` = 0 bytes · `Leken.md` = 20 bytes (*"so in short we have"*).
- **Real content:** `Index.md`, `Detail1.md`, `Results.ipynb`,
  `c2h2_hydrogenation_transient_model.ipynb` (11 cells, already the right structure).
- **`pbr/`** = 10 modules, commit `e0663ba`, 37 passing tests. **That is the simulation.**
- **`Detail1.md`** is the one real draft chapter (LHHW mechanism, 5 reactions, conservation
  PDE) — the seed for `Theory.md`.

## Hard constraints

1. **⚠️ ONEDRIVE FIRST.** The repo is full of cloud placeholders. `Errno 22`, `Permission
   denied` on a readable file, or `cloud file provider exited unexpectedly` = **not an ACL
   problem**. Start OneDrive (`%ProgramFiles%\Microsoft OneDrive\OneDrive.exe`), pin with
   `attrib +P`, read-walk to `failed: 0`, verify `pixi run myst --version`, then **stop OneDrive
   again**. Reading alone does not hydrate — pinning does. Stubborn case: `export typst.yml`
   resisted every pin; fix was rewriting it from `git show HEAD:"export typst.yml"`.
2. **Real pixi tasks:** `editor preview pdf sanitise-bib test lint format smoke review`.
   **No `run` task, no `ipynb` task.** Registry is **`toc.yml`**, not `content.yml`.
3. **Repo is PUBLIC**, Pages live off `main`. Names and paths are cleared by the owner.
   Real secrets are off-limits — and there are none (verified).
4. **Scoped staging only:** `git commit --only <paths>`.
5. **Read before you write.** Tag `[verified]` / `[inferred]` / `[uncertain]`.

## Definition of done

D1 site builds with zero toc errors · D2 no template residue · D3 every `toc.yml` entry
resolves · D4 `Theory.md`+`Methods.md` state the real physics/numerics · D5 a Damian artifact
exists and builds · D6 nothing left dehydrated.

**Then STOP.** Leave every HITL/grilling ticket for the morning — emphasis, candour depth,
inline-vs-import `pbr/`, page-vs-deck, what gets published.
