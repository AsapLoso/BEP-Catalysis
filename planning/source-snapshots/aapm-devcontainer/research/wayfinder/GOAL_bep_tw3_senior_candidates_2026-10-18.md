# Gemini Antigravity Prompt — Run TW3 Senior Candidates Map with Wielder and Stream It

Paste into **Gemini Antigravity** with the `Aa Project management` workspace open. The map, validator, and prompt pack are prepared; this prompt instructs Antigravity to run the map through Wielder via Harness and supervise it with Harness Guardian.

---

Read `/wayfinder`, `/wayfinder-maps`, `/wielder`, `/harness`, `/harness-guardian`, and `.agents/rules/harness_delegation.md`.
Read `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`, its companion prompt pack `research/wayfinder/bep_tw3_senior_candidates_2026-10-18_prompts.md`, the validator `research/wayfinder/validate_bep_tw3_senior_candidates_2026-10-18_map.py`, and the owning candidate dossier `Academics/BEP/Catalysis/committee_candidates.md`.
Treat the map's header hard stops and execution contract as binding.

## Dispatch and Streaming Protocol

1. **Environment & Health Pre-flight:** Confirm Harness (`127.0.0.1:4001`) and upstream OpenCode (`127.0.0.1:4096`) are alive and healthy.
2. **Validator Pre-flight:** Run Wielder's zero-token plan audit:
   ```powershell
   pixi run python Builds/OpenCode_Harness/scripts/run_wielder.py --audit --plan "research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md"
   ```
   Require 0 critical errors before dispatch.
3. **Dispatch Wielder Session:** Invoke Wielder directly:
   ```powershell
   pixi run python Builds/OpenCode_Harness/scripts/run_wielder.py --plan "research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md"
   ```
   Keep Wielder's live stdout attached to the terminal so progress streams visibly.
4. **Launch Standing Stream:** Start the documented Harness standing SSE sentinel once:
   ```powershell
   pixi run python Builds/OpenCode_Harness/scripts/event_sentinel.py launch
   ```
   Yield control immediately after dispatch; do not loop or set a polling timer.
5. **Attach Harness Guardian:** Locate the dispatched session:
   ```powershell
   pixi run python .agents/skills/harness-guardian/scripts/sentinel_daemon.py find "TW3 senior roster"
   ```
   Confirm session title and ID with Lucas ("right one?"), then attach the single per-session Guardian:
   ```powershell
   pixi run python .agents/skills/harness-guardian/scripts/sentinel_daemon.py watch <session_id> --idle-ticks 3
   ```
6. **Reactive Stream Wake:** When the event wake is delivered, inspect status once:
   ```powershell
   pixi run python Builds/OpenCode_Harness/scripts/event_sentinel.py status
   ```
   Act on `SESSION_COMPLETE`, `TOOL_HUNG`, or `TOOL_ERRORED`.

## Work & Screening Boundaries

- All 39 tickets are `grilling` (HITL). Never answer or resolve candidate selection decisions on your own. Present candidate groupings section-by-section to Lucas and end the turn.
- Do not contact candidates, submit official forms, sign documents, or assert willingness or consent.
- All 15 Mathematical Physics seniors (including Yves van Gennip) are strictly excluded (same section as Zoë Gromotka).
- Do not infer age, personal approachability, or kindness from seniority, titles, names, or public profile photos.
- Stage and commit only the explicit `scoped_commit_files` declared in the Execution Contract.
