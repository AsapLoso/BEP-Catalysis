# /goal — Tonight's execution (paste into a fresh chat)

> **Reference this file with `/goal`.** It is the master goal; the subgoal prompts live in
> `bep_damian_presentation_prompts.md` (SG-1 … SG-5) and in `hermes_bep_site_map.md`.
> **Charted:** 2026-10-12 · **Owner:** Lucas van Dekken · **Mode:** B orchestrator, autonomous overnight.

---

## THE GOAL

By tomorrow morning I can present to Damian — and my site reflects real work instead of the
starterkit template. Everything else is scaffolding around those two outcomes.

**Working dir (NOT inside `Aa Project management`):**
`%USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis`

---

## SUBGOALS (in order — do not jump ahead)

| # | Subgoal | Prompt |
|---|---|---|
| SG-1 | Chart the map (`bep_damian_presentation.md`) | `bep_damian_presentation_prompts.md` §SG-1 |
| SG-2 | Verify + register the notebook | §SG-2 |
| SG-3 | Research → choices → build narrative | §SG-3 |
| SG-4 | Assemble the Damian presentation | §SG-4 |
| SG-5 | Update the website | §SG-5 |

**Then STOP.** Leave every HITL/grilling ticket for the morning. Do not answer them yourself.

---

## END STATES (verifiable)

| # | End state | How it's checked |
|---|---|---|
| D1 | The site builds with zero toc errors | `pixi run preview` → no `⛔️` |
| D2 | No starterkit template text survives | grep `content/` for template strings → 0 |
| D3 | Every `toc.yml` entry resolves | each `file:` exists on disk |
| D4 | `Theory.md` + `Methods.md` state the real physics/numerics | cite `Detail1.md` + `pbr/` |
| D5 | A Damian presentation artifact exists and builds | it compiles |
| D6 | Nothing left dehydrated | hydration walk → `failed: 0` |

---

## HARD CONSTRAINTS

1. **⚠️ ONEDRIVE FIRST.** This repo is full of cloud placeholders. `Errno 22`, `Permission
   denied` on a readable file, or `cloud file provider exited unexpectedly` = **not an ACL
   problem**. Start OneDrive (`%ProgramFiles%\Microsoft OneDrive\OneDrive.exe`), pin with
   `attrib +P`, read-walk to `failed: 0`, verify `pixi run myst --version`, then **stop
   OneDrive again**. Reading alone does not hydrate — pinning does.
2. **Real pixi tasks:** `editor preview pdf sanitise-bib test lint format smoke review`.
   There is **no `run` task and no `ipynb` task**. The content registry is **`toc.yml`**,
   not `content.yml` (which does not exist).
3. **The repo is PUBLIC** on GitHub, Pages live off `main`. Names and paths are cleared by
   the owner. Real secrets are off-limits — and there are none (verified).
4. **Scoped git staging only:** `git commit --only <paths>`. Never `git add -A`.
5. **Read before you write.** Tag findings `[verified]` / `[inferred]` / `[uncertain]`.
   "Not found" is a valid answer. Never invent a path, a date, or a result.
6. **You are the orchestrator, not the typist.** Delegate mechanical reads to OpenCode via
   `/harness`; watch with `/harness-guardian` at zero token burn. Read a file yourself only
   when a decision hinges on exact wording, and say why.

---

## KNOWN STATE (verified tonight — do not re-derive)

- **The site builds.** `pixi run preview` builds every page. One real error:
  `⛔️ Table of contents entry does not exist: content\Detail3.md`
- **Template residue:** `Theory.md`, `Methods.md`, `Conclusion.md` are raw starterkit
  (`E=mc²`, the Schrödinger equation, *"is Jupyter Book feasible"*).
- **Empty stubs:** `Detail2.md` = 0 bytes · `Leken.md` = 20 bytes.
- **Real content:** `Index.md`, `Detail1.md`, `Results.ipynb`,
  `c2h2_hydrogenation_transient_model.ipynb`.
- **`pbr/`** = 10 modules, commit `e0663ba`, 37 passing tests. That is the simulation.
- **`Detail1.md`** is the one real draft chapter (LHHW mechanism, 5 reactions, conservation
  PDE) — it is the seed for `Theory.md`.

---

## HAND-BACK

Each wave ends with a **Phase Rapport**: deliverables · real command output as evidence ·
commit SHA · the next prompt ready to dispatch. Conclude only when the frontier holds
nothing but HITL tickets.
