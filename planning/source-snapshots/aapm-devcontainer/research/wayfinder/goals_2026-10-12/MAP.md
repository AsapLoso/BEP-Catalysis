# GOALS — 2026-10-12 (put this in `/goal`)

> **This file is the map.** Each goal has its own file beside it in this directory.
> **Charted:** 2026-10-12 · **Owner:** Lucas van Dekken · **Updated:** after owner corrections.

---

## Status board

| G | Goal | Status | File |
|---|---|---|---|
| **G1** | TN22010 — reconcile → targeted regrade → upload → mail | 🟡 **G1.1 complete** — ledger built: 1 Q1 + 7 Q8 affected (8 grades); stale 158-count falsified | `G1_tn22010_zesje_upload.md` |
| **G2** | BEP prep for Monday | ✅ **table written** | `G2_bep_monday_prep.md` |
| **G3** | ~~7-account migration~~ | ❌ **DELETED** — file removed, not to exist | — |
| **G4** | ~~Codex skills bridge~~ | ❌ **DELETED** — file removed, not to exist | — |
| **G5** | ~~TN22010 FlexDelft hours~~ | ⏭️ **SKIPPED by owner** | `G5_draft_mail.md` (draft kept) |
| **G6** | BEP Damian presentation + site update | ✅ **map charted** | `G6_bep_damian_presentation.md` · `G6_prompt_pack.md` · `G6_chatgpt_prompt.md` |
| **G7** | ~~OCR the LA slides~~ | ❌ **DELETED — removed from state.md and task.md entirely** | — |
| **G8** | ~~Commit the vendored skills~~ | ⏭️ **SKIPPED by owner** — marked done | `G8_commit_skill_vendoring.md` |
| **G8** | Notebook verification | ✅ **verified + report** | `G8_notebook_verification.md` |
| **G9** | Research → choices → narrative | ✅ **written** | `Methanol-Catalysis/content/SG3_Narrative.md` |

---

## Done tonight

- [x] **Site content rewritten** — `Theory.md` (8,922 B), `Methods.md` (6,484 B),
      `Conclusion.md` (3,268 B), `Detail2.md` (1,754 B), `Leken.md` (1,365 B),
      `Detail3.md` created (2,341 B, was missing).
- [x] **`toc.yml` broken reference fixed** — `content/Detail3.md` now exists; the build no
      longer reports `⛔️ Table of contents entry does not exist`.
- [x] **Build verified** — `pixi run myst build --html` → **14 pages built**, no toc error.
- [x] **OneDrive hydrated** — 52/52 in the working dirs; the root stragglers fixed
      (`errorlog.md`, `export latex.yml` pinned; `export typst.yml` replaced from the git
      object store).
- [x] **G5 mail drafted** — `G5_draft_mail.md`, awaiting sign-off.
- [x] **G3 / G4 / G7 removed** — files deleted; OCR purged from `state.md` and `task.md`.
- [x] **G6 SG-3 re-framed** — now states plainly it is the prose about the work, one source
      for both the deck and the site. Resolved.
- [x] **G1.4 post-regrade comparison written** — re-pull the live sheet, diff against our
      grades, overwrite from our record (DJ's 109 untouched).
- [x] **G2 BEP Monday table** — `G2_bep_monday_prep.md`: four-thread table, staleness flags,
      shortest path, delegation note.
- [x] **G7 BEP Damian map** — `Academics/BEP/Catalysis/research/wayfinder/bep_damian_presentation.md`:
      12 islands (I0–I11), 3 HITL tickets, 4 mechanical tickets. Wayfinder grammar correct.
- [x] **G8 Notebook verification** — `G8_notebook_verification.md`: 11 cells, 5-section convention,
      toc.yml registered, inlines by convention (not importing pbr/), no absolute paths,
      execution blocked by OneDrive in pixi env (not notebook logic).
- [x] **G9 SG-3 Narrative** — `Methanol-Catalysis/content/SG3_Narrative.md`: 17,369 B, four parts
      (Research with 9 threads from bib+crosscheck, 15 Choices with evidence from pbr/ + tests,
      Learned including interruption-driven test philosophy, 6 Gaps plainly stated), plus
      decision table (15 rows) and source map (13 modules). One source for deck + site.

---

## What remains for the owner

1. **G1 recalibration** — first build a fresh all-268 option-set reconciliation ledger; then derive the affected regrade worklist from documented formulation failures. No grading fleet is running yet.
2. **G1 scope decision** — do not rely on the stale `90/44/24` split; the comparison ledger determines whether a formulation defect reaches a subset or the entire cohort.
3. **G10 (user's #10) — HTML deck** — you build this with ChatGPT using `G6_chatgpt_prompt.md`
   fed with `SG3_Narrative.md` + `content/Detail1.md` + `pbr/` docstrings.
4. **G8 (vendored skills commit)** — crossed off by the owner.

---

## Rules that apply to every goal

- **⚠️ ONEDRIVE FIRST** on any `Methanol-Catalysis` work. `Errno 22` / `Permission denied` /
  `cloud file provider exited unexpectedly` = a placeholder, **not** an ACL problem. Start
  OneDrive → `attrib +P` → read-walk to `failed: 0` → verify → **stop OneDrive again**.
- **Real pixi tasks:** `editor preview pdf sanitise-bib test lint format smoke review`.
  No `run`, no `ipynb`. Registry is **`toc.yml`**.
- **Scoped staging only:** `git commit --only <paths>`. Never `git add -A`.
- **Read before you write.** Tag `[verified]` / `[inferred]` / `[uncertain]`. Never invent.
- **Delegate mechanical work** to OpenCode via `/harness`; watch with `/harness-guardian`.
- **Leave HITL/grilling tickets for the owner.** Never answer them in a worker session.
