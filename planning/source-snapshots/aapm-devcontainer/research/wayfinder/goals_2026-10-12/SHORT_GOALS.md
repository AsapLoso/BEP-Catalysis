# SHORT GOALS — paste-ready `/goal` lines

> One block per subgoal, in the register of the G1 goal you wrote. Paste a single block;
> never two at once. Full specs live in the sibling `G*.md` files.

---

## G1 — TN22010 re-grade → upload (owned by another chat)

**G1.1 — Q1 re-grade**
```
/goal TN22010 Q1 re-grade. Zesje exam 2: Vraag 1 (problem ID 1, max 4.0), all 134 students. Current: 44/134 were done with the OLD lax prompts — ALL STALE, redo them; 90 never done. MUST use the 2-PASS architecture from grading/PROMPT_GUIDE.md: PAS 1 Literal Mechanical Transcript (zero judgment — extract verbatim, mark [DELETED], note explicitly whether the required conclusion is literally present), then PAS 2 Mathematical Rigor & Rubric Arbitrator (checks algebra and signs, applies the rubric, emits binary Keystroke Option IDs). Q1 rubric = opties 54-58 with the PROMPT_GUIDE edge cases; the three Golden Laws apply (Wet 1 Strict Consequence, Wet 2 No Follow-Through on Invalid Roots, Wet 3 Prerequisite DAG / Anti-Ghost) plus the four vangnet-regels. Metric = mismatched rubric item sets (symmetric difference), NEVER score deltas. Vision models are transcriptors only (PAS 1); all math scoring is PAS 2. Disputes >= 1.0 pt get a direct visual audit; 0.5 pt slordigheidscap. Record of truth = grading/data/api_exports/_api_exams_2.json. Do not upload, do not touch mail. Done = 134/134 Q1 evaluations produced with the calibrated 2-pass prompts and the ledger updated.
```

**G1.2 — Q8 re-grade**
```
/goal TN22010 Q8 re-grade. Vraag 8 (problem ID 9, max 5.0), 134 students. Current: 133/134 in Zesje — DJ van Heumen 109 = HUMAN GROUND TRUTH, 100% untouchable, never overwrite; my 24 were done with the OLD lax prompts and must be redone; Tijn de Nooijer Sub #19 is remark-only. Same 2-PASS architecture and scoring rules as G1.1. Q8 rubric = opties 26-32 with the PROMPT_GUIDE edge cases — note the hard blocks: no literal "not exact" conclusion => 0 pt on Toets 2 (optie 27); a wrong integrating factor => 0 pt on Toets 3 (optie 28) AND Toets 4, 5, 6 all blocked; Toets 6 (optie 31) can only be granted if opties 29 and 30 are substantively complete. Wet 1-3 + the four vangnet-regels. Symmetric-difference metric, NEVER score deltas. Done = my 24 re-evaluated with the calibrated 2-pass prompts and DJ's 109 untouched.
```

**G1.3 — arbitration + final ledger**
```
/goal TN22010 arbitration and final ledger. Reconcile every evaluation against the 20 ta_arbitration_dossier overrides. Record of truth = grading/data/api_exports/_api_exams_2.json — the dossier .md is narrative, the API dump is the record. Metric = mismatched rubric item sets (symmetric difference), NEVER score deltas. Done = 268/268 evaluations in the final master ledger, fully reconciled, every override applied, no unresolved dispute >= 1.0 pt.
```

**G1.4 — upload**
```
/goal TN22010 upload. run_uploader_tn22010.bat -> upload_tn22010_grades.py. Use auto-skip [2] — it is the standard and it preserves DJ's 109 assessments. [99] force-overwrite is hidden, protected, and ONLY for a deliberate justified overwrite — never reach for it to make something work. If it fails, report the exact error; do not retry-loop. Done = 268/268 synced in Zesje, verified by an independent count, not just exit 0.
```

**G1.5 — Bericht 16**
```
/goal TN22010 Bericht 16. Reply to Kateryna, Sven, DJ and Hidde answering the Friday chase (Bericht 12-15). Cancel the redistribution — Kateryna asked DJ to take Vraag 8 and Hidde Vraag 1 because Zesje showed 0%, which was only because the scoring was offline. Exact text is in thread.md §Bericht 16. Do not send without my sign-off. Done = the message drafted and awaiting my approval.
```

---

## G2 — BEP prep for Monday

```
/goal BEP prep for Monday. Anchors: Academics/BEP/Catalysis/ and Academics/BEP/SysCon/. Answer three things: what must be true by Monday, what blocks it, and the shortest path. Four live threads: (1) CaSE secretariat (Els Arkesteijn) onboarding reply — start/end date, bio, photo, BEP registration form for Building 58 + Lab Servant; (2) Carlas Smith follow-up — confirm Roel Smit is being asked about form TWN3002-24; (3) Dr. Neil Budko in-person — his substantive supervision role and the formal TW 2nd-examiner slot; (4) Carlas Smith 2nd-corrector — confirm Bijoy covers the transport physics. Two of these are queued as 2-minute emails and should not still be open. Delegate the reading to OpenCode via /harness; flag anywhere the BEP state files are stale against the 2026-10-11 handoff in LATEST_UPDATES.md. Done = a four-thread table: current state -> blocker -> next action -> owner, under 30 lines.
```

---

## G5 — TN22010 FlexDelft hours (unpaid work)

```
/goal TN22010 FlexDelft hours — I am grading unpaid. The 01-10 mail to Marynets & Aerts asked for two things: the question distribution (received 02-10) and my own FlexDelft dossier for TN22010 — that second ask was NEVER MADE. Without it the hours for 02-12 Oct are not declarable. The 29-09 draft contained the question but was never sent. Draft that mail: it must state the ask explicitly — a FlexDelft appointment for TN22010 so the 02-12 Oct grading hours can be declared. Dutch. Also confirm the rubric source is the grading model at Kateryna_Sven_Grading_Q1/exam/Tentamen_LinDiff_deel_2-12.pdf, NOT the 2025 normering 4 4 3 5 9 4 4 4 10 3 — that is a different per-question split. Do not reply to Bericht 9/10 (DJ and Kateryna's thread, I am only cc'd). Done = the drafted mail + the rubric confirmation + any other undeclared or stale item.
```

---

## G6 — BEP Damian presentation + site

**SG-1 — chart the map**
```
/goal Chart the BEP map. Create bep_damian_presentation.md in the Methanol-Catalysis repo — a NEW wayfinder map, do not overwrite any existing one. Destination = a Damian presentation, stated as verifiable end states. Ground first: pbr/ (10 modules, commit e0663ba — the module docstrings are where the design decisions live), content/c2h2_hydrogenation_transient_model.ipynb, content/{Index,Introduction,Detail1}.md, references.bib, tests/ (37 passing). Use the exact grammar WayfinderMap.from_markdown parses: - [ ] **Title** (wayfinder:type) — *Question: ...?* with no trailing text in the parens and no asterisk in a title or question. Mark HITL tickets clearly and leave them OPEN — those are mine tomorrow. Done = the map plus a one-screen summary: islands, tickets, how many HITL, what is unblocked tonight. STOP after charting.
```

**SG-2 — verify the notebook**
```
/goal Verify the notebook. content/c2h2_hydrogenation_transient_model.ipynb exists (11 cells, the right structure). Run it for real: pixi run jupyter nbconvert --execute --to notebook --inplace <path>. There is NO ipynb pixi task — do not invoke one. Report the real output; fix a failing cell rather than leaving it unrun. Confirm it is registered in toc.yml (NOT content.yml — that does not exist) by copying a sibling entry's schema exactly. Check its outputs for absolute paths. If it should import pbr/ instead of inlining, say so as a finding — do NOT silently rewrite it; the inline 5-section structure is the established convention. Done = the exact command, the real pass/fail output, and the inline-vs-package finding.
```

**SG-3 — research → choices → build**
```
/goal Build the research -> choices -> build narrative in content/. Four parts: (1) the research — what the literature says, from references.bib + bib_crosscheck_report.md, each thread with claim, source, and whether we adopted/adapted/rejected it; (2) the choices — the modelling decisions and WHY, sourced from the pbr/ docstrings (they ARE the record) and test_discretisation.py: the discretisation scheme (TVD2 vs upwind), the radial diffusion treatment, the stiff solver, the closures; each choice as what we chose / what the alternative was / why / how we know it works; (3) what we learned — including that the work was interrupted by bug reports, which is part of the honest story; (4) what is NOT done, plainly. Every claim traceable to a paper or a module/test, tagged [verified]/[inferred]/[uncertain]. No invented results. Done = the files plus a decision table (choice -> alternative -> why -> evidence) and an explicit gap list.
```

**SG-4 — assemble the presentation**
```
/goal Assemble the Damian presentation as an HTML deck. Form is decided: ask ChatGPT to build it — it knows HTML well. Use G6_chatgpt_prompt.md as the ask, feeding it SG-3's narrative plus content/Detail1.md and the pbr/ docstrings. Requirements: ONE self-contained .html file, no build step, opens by double-clicking, offline; keyboard navigation, slide counter, progress bar; no placeholders; no invented results or citations; each modelling choice gets a "we chose X / instead of Y" visual. Damian knows the chemistry deeply and the code not at all — explain what the code MEANS. Keep it LOCAL; do not commit it to the repo. Done = the artifact path, how it was produced, and what only I can supply.
```

**SG-5 — update the website**
```
/goal Update the Methanol-Catalysis website. MyST book, Pages live off main, base URL /Methanol-Catalysis/. FIRST: the repo is full of OneDrive placeholders — if you hit Errno 22, Permission denied on a readable file, or "cloud file provider exited unexpectedly", it is NOT an ACL problem. Start OneDrive (%ProgramFiles%\Microsoft OneDrive\OneDrive.exe), pin with attrib +P '<repo>\*', read-walk to failed: 0, verify pixi run myst --version, then STOP OneDrive again. Reading alone does not hydrate — pinning does. Then fix, all verified: (1) toc.yml references content/Detail3.md which does not exist — the build reports it; create it or drop it, do not leave it broken; (2) Theory.md, Methods.md and Conclusion.md are RAW STARTERKIT TEXT (E=mc2, the Schrodinger equation, "is Jupyter Book feasible") — rewrite from real material; (3) Detail2.md is 0 bytes and Leken.md is 20 bytes — fill or drop. Write Theory.md from Detail1.md (LHHW mechanism, the 5 reactions, the conservation PDE) plus Danckwerts BCs and the dimensionless groups; Methods.md from the pbr/ docstrings + test_discretisation.py (MOL, TVD2, radial diffusion, the stiff solver). Done = pixi run preview builds every page with zero toc errors and no starterkit strings remain in content/.
```

---

## G7 — OCR the LA slides

```
/goal OCR the LA lecture slides. Les 00 through Les 12 — all 13 LA slide decks in Academics/Curriculum_Left/TN22010_Voortgezette_LA_DV/content/ — are image scans yielding ~22 chars/page, so they are unusable as a theory source and uncitable. This is the only outstanding gap in the course dossier. OCR all 13 to searchable text alongside the existing extracts in content/text/, preserve page boundaries so a citation can name a slide, and update content/text/_extract_index.json so the 13 stop reading as failed scans. Report the real character yield per file — 22 chars/page is the baseline to beat. Check what OCR is already in the project environment before installing anything. Delegate via /harness; this is a script run, not orchestrator work. Done = 13 decks yielding usable citable text and the index updated.
```

---

## G8 — commit the vendored skills

```
/goal Commit the 48 vendored skills. On 2026-10-11, 48 Hermes skills were copied into .agents/skills/ (50 -> 98) and AGENTS.md was updated to describe the split (50 workspace-native + 48 vendored; 11 deliberately excluded: apple-notes, apple-reminders, imessage, findmy, hermes-agent, hermes-agent-skill-authoring, inspecting-hermes-desktop-dom, computer-use, opencode, codex, claude-code). git status shows 58 untracked entries there. Commit with scoped staging only — git commit --only <paths>, never git add -A and never a directory sweep. Keep the 48 vendored skills as one logical change; the three modified existing files (azure-cost/SKILL.md, humanizer/SKILL.md, harness-guardian/scripts/state.json) are a separate one. FIRST settle the doctrine question: is .agents/skills/ meant to hold verbatim upstream material, or should it go through the Builds/Skills_Vendor/ quarantine (Rule 27, hash manifest)? PORT_NOTES.md argues against bare copies ("waarom geen kale kopie") — ask rather than guess. Verify the AGENTS.md count (98) matches disk and the excluded 11 are absent. Done = committed scoped, git status clean of them, counts verifiable.
```

---

## Stashed — do not start

**G3** (7-account migration) and **G4** (Codex skills bridge) are deferred. Their specs are in
`G3_account_migration.md` and `G4_codex_skills_bridge.md`; leave them alone tonight.
