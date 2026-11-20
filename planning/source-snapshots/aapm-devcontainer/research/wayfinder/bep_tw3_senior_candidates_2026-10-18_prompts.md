# TW3 Senior Candidates Roster Screening — Wielder Prompt Pack

This pack provides the master goal prompt and wave-ordered prompts for executing the candidate screening map (`research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`) using Wielder, Harness Guardian, and Harness.

---

## Master Goal Prompt

Read `/wayfinder`, `/wayfinder-maps`, `/wielder`, `/harness`, `/harness-guardian`, and `.agents/rules/harness_delegation.md`.
Read `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`, its companion validator, the owning candidate dossier `Academics/BEP/Catalysis/committee_candidates.md`, and the intake files in `Academics/BEP/Catalysis/Dossier/committee_forms_intake_2026-10-18/`.

Run the map through **Wielder**:
```powershell
pixi run python Builds/OpenCode_Harness/scripts/run_wielder.py --plan "research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md"
```

### Supervisory & Harness Streaming Protocol
1. Confirm Harness (`:4001`) and upstream OpenCode (`:4096`) health.
2. Run Wielder dry-run/audit to confirm pass (`--audit --plan "research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md"`).
3. Start the standing SSE stream once:
   ```powershell
   pixi run python Builds/OpenCode_Harness/scripts/event_sentinel.py launch
   ```
4. Attach the zero-token passive Harness Guardian:
   ```powershell
   pixi run python .agents/skills/harness-guardian/scripts/sentinel_daemon.py find "TW3 senior roster"
   ```
   Quote the session title and ID to the user with "right one?", and then watch:
   ```powershell
   pixi run python .agents/skills/harness-guardian/scripts/sentinel_daemon.py watch <session_id> --idle-ticks 3
   ```
5. On stream wake, check status once:
   ```powershell
   pixi run python Builds/OpenCode_Harness/scripts/event_sentinel.py status
   ```

### HITL & Candidate Screening Invariants
- **All 39 tickets are `grilling` (HITL):** Never resolve or answer candidate screening decisions on your own.
- **No external outreach or appointment:** This effort only screens and structures the candidate pool. Do not contact candidates, do not submit forms, and do not assert willingness or consent.
- **Section exclusion:** Zoë Gromotka (TW1) is in Mathematical Physics; all 15 Mathematical Physics seniors (including Yves van Gennip) are strictly excluded.
- **No age/niceness inference:** Do not infer age, personal approachability, or kindness from seniority, titles, names, or public photos.
- **Scoped commits only:** Never use `git add -A`. Commit only explicit files declared in the Execution Contract.

---

## Wave 1 — Analysis Section Candidates (T01–T10)

Fresh-session orientation:
- Workspace: `%USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Aa Project management`
- Read first: `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`, `Academics/BEP/Catalysis/committee_candidates.md`.
- Target island: `Analysis Section Candidates` (T01 through T10).
- Prerequisite: Validator passes (`pixi run python "research/wayfinder/validate_bep_tw3_senior_candidates_2026-10-18_map.py"`).
- Tasks:
  1. Inspect the 10 Analysis seniors (Bult, Caspers, Dries, Groenevelt, Janssens, Lorist, Neerven, Spandaw, Veraar, Vroegrijk).
  2. Note directory categories (Bult, van den Dries, Vroegrijk listed under Teachers; Neerven and Veraar under Scientific Staff).
  3. Formulate the concise grilling dossier for Lucas: highlight topic proximity (Analysis is 2/5 distance, closest to reactor PDEs/diffusion), flag teacher vs. scientific-staff status, and present trade-offs.
  4. End turn with the grilling questions for Lucas. Do not self-resolve.

---

## Wave 2 — Discrete Mathematics & Optimization Candidates (T11–T20)

Fresh-session orientation:
- Read first: `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`.
- Target island: `Discrete Mathematics & Optimization Section Candidates` (T11 through T20).
- Prerequisite: Wave 1 reviewed; validator passes.
- Tasks:
  1. Inspect the 10 DMO seniors (Aardal, Bishnoi, Essen, Gijswijt, Iersel, Laat, Murakami, Oliveira Filho, Verhulst, Weber).
  2. Note directory categories (Verhulst listed under Teachers; Aardal, Gijswijt are professors).
  3. Note topical distance: 5/5 (farthest from catalysis kinetics and continuum mechanics, focused on graph theory/combinatorics/integer programming).
  4. Formulate the grilling comparison: assess whether DMO offers beneficial methodological distance or excessive divergence from thesis themes.
  5. Present trade-offs to Lucas and end turn.

---

## Wave 3 — Numerical Mathematics Candidates (T21–T24)

Fresh-session orientation:
- Read first: `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`, `Academics/BEP/Catalysis/state.md`.
- Target island: `Numerical Mathematics Section Candidates` (T21 through T24).
- Prerequisite: Validator passes.
- Tasks:
  1. Inspect the 4 Numerical Mathematics seniors (Budko, Gijzen, Palha da Silva Clérigo, Vuik).
  2. Note specific statuses:
     - Neil Budko: Dr. N.V. Budko, Numerical Analysis Scientific Staff (older "Associate Professor" title unverified in current directory).
     - Kees Vuik: Listed under Emeritus on current people page.
     - Martin van Gijzen: Professor, scientific staff.
     - Artur Palha: Scientific staff.
  3. Topical distance: 3/5 (numerical simulation of physical models, finite elements, linear solvers).
  4. Formulate grilling questions for Lucas: evaluate Budko vs. Gijzen vs. Palha, highlighting eligibility checks needed for Vuik (emeritus).
  5. Present to Lucas and end turn.

---

## Wave 4 — Statistics Candidates (T25–T32)

Fresh-session orientation:
- Read first: `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`.
- Target island: `Statistics Section Candidates` (T25 through T32).
- Prerequisite: Validator passes.
- Tasks:
  1. Inspect the 8 Statistics seniors (Bierkens, Cabo, Derumigny, Jongbloed, Kekkonen, Parolya, Söhl, Vaart).
  2. Note specific statuses:
     - Geurt Jongbloed: Professor in Statistics, DIAM management team member.
     - Hanne Kekkonen: Retained in workbook pool; prior project records report repeated declines — do NOT re-approach without user direction.
     - Aad van der Vaart: Professor in Statistics.
  3. Topical distance: 4/5 (asymptotics, nonparametrics, uncertainty quantification).
  4. Formulate grilling presentation for Lucas: assess Jongbloed (management/prestige) vs. other statistics faculty.
  5. Present to Lucas and end turn.

---

## Wave 5 — Applied Probability Candidates (T33–T39)

Fresh-session orientation:
- Read first: `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`.
- Target island: `Applied Probability Section Candidates` (T33 through T39).
- Prerequisite: Validator passes.
- Tasks:
  1. Inspect the 7 Applied Probability seniors (Anderluh, Fokkink, Komjáthy, Kraaij, Kurowicka, Nane, Redig).
  2. Topical distance: 3/5 (stochastic processes, interacting particle systems, probabilistic modelling).
  3. Formulate grilling presentation for Lucas: compare Applied Probability profiles.
  4. Present to Lucas and end turn.

---

## Wave 6 — Shortlist Synthesis & Verification Close-out

Fresh-session orientation:
- Read first: `research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md`, all wave grilling responses from Lucas.
- Tasks:
  1. Synthesize the top candidate shortlist based on Lucas's grilling preferences.
  2. Advance settled candidates into `## 2. Decisions So Far`.
  3. If fog items become formulate-able (e.g. eligibility verification procedure for shortlisted candidates), promote them to fresh Active Frontier tickets and delete promoted fog lines.
  4. Keep validator constants in sync and run:
     ```powershell
     pixi run python "research/wayfinder/validate_bep_tw3_senior_candidates_2026-10-18_map.py"
     ```
  5. Record state update in `Academics/BEP/Catalysis/state.md` and append to `history.log`.
  6. Execute the scoped commit:
     ```powershell
     git commit --only research/wayfinder/bep_tw3_senior_candidates_2026-10-18.md research/wayfinder/validate_bep_tw3_senior_candidates_2026-10-18_map.py research/wayfinder/bep_tw3_senior_candidates_2026-10-18_prompts.md research/wayfinder/GOAL_bep_tw3_senior_candidates_2026-10-18.md Academics/BEP/Catalysis/state.md Academics/BEP/Catalysis/history.log -m "Wayfinder: chart TW3 senior candidate screening map and prompts"
     ```
