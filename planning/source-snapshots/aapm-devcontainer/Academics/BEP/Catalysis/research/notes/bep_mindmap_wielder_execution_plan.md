# BEP Mind Map: Wielder Multi-Phase Execution Plan

This execution plan compiles the Wayfinder decision map (`Academics/BEP/Catalysis/research/wayfinder/bep_ai_mindmap.md`) into executable phase specifications conforming to `ExecutionPromptSpec` and `PlanParser`.

---

### PHASE 1: YAML Schema & Deterministic Editor Surface

````markdown
/wayfinder /harness /harness-guardian
**PHASE 1: YAML SCHEMA & DETERMINISTIC EDITOR SURFACE**

**GOAL:** Implement the core YAML graph schema validation, deterministic Python modification engine, and local stdio MCP server for the BEP mind map.

**INVARIANTS & CONSTRAINTS:**
- STATE PURITY: Dispatched workers must NEVER modify state.md, history.log, conventions.md, or task.md.
- PR #84 ADHERENCE: Node schema must support id, parent, title, tier (0–4), importance (0–3 stars), rationale, notes, sources list, and open_questions.
- ATOMICITY: All file writes must be atomic (write to temp file, flush, replace). Schema validation must fail closed without writing if a cycle or missing parent is detected.
- UTF-8 GUARDRAIL: All Python entry points must configure UTF-8 output.

**CONTEXT & TECHNICAL CONSTRAINTS:**
- Work directory: `Academics/BEP/Catalysis/mindmap/`.
- Schema validator must enforce: root 'bep' node, three primary branches ('physics', 'mathematics', 'systems_control'), unique IDs, valid parent references, and no cyclic graphs.
- Provide a clean CLI and stdio MCP server exposing deterministic tools: `add_node`, `edit_node`, `reparent_node`, `delete_node`, `set_tier`, `set_importance`, `attach_source`.

**STEP 1: DISPATCH & EXECUTE:**
1. Create `Academics/BEP/Catalysis/mindmap/` package with `schema.py`, `editor.py`, and `mcp_server.py`.
2. Seed canonical map file `Academics/BEP/Catalysis/mindmap/data/bep_map.yaml` with the root node and the three main arms (Physics, Mathematics, Systems & Control).
3. Build comprehensive test suite in `Academics/BEP/Catalysis/mindmap/tests/test_editor.py` covering schema enforcement, atomic rollback on invalid mutations, and cycle detection.

**STEP 2: SUPERVISOR VERIFICATION:**
`pixi run pytest Academics/BEP/Catalysis/mindmap/tests/test_editor.py`

**STEP 3: SCOPED COMMIT:**
```powershell
git commit --only Academics/BEP/Catalysis/mindmap/schema.py `
                  Academics/BEP/Catalysis/mindmap/editor.py `
                  Academics/BEP/Catalysis/mindmap/mcp_server.py `
                  Academics/BEP/Catalysis/mindmap/data/bep_map.yaml `
                  Academics/BEP/Catalysis/mindmap/tests/test_editor.py `
          -m "feat(bep-mindmap): implement YAML schema validator and deterministic MCP editor"
```

**OPERATIONAL LIFECYCLE PROTOCOL:**
- Keep substrate warm! Daemons (:4001, :4096) stay running.
- Write the structured Phase 1 Rapport to `Academics/BEP/Catalysis/research/rapports/phase_1_rapport.md` with YAML frontmatter (`status: verified_complete`, `commit: <sha>`, `title: "Phase 1 - Editor Engine"`).
- Save any escalated questions to `Academics/BEP/Catalysis/research/questions/phase_1_questions.json` (validated against QuestionItem).
- Cleanly terminate the CEO session to prevent context leaks.
- Conclude with `<!-- GOAL_COMPLETE -->`.
````

---

### PHASE 2: Interactive Visualizer & `pixi run preview`

````markdown
/wayfinder /harness /harness-guardian
**PHASE 2: INTERACTIVE VISUALIZER & LIVE PREVIEW**

**GOAL:** Implement the browser-based mind-map visualizer with pan/zoom/collapse, details drawer, and live file-watch reloading via `pixi run preview`.

**INVARIANTS & CONSTRAINTS:**
- STATE PURITY: Never edit state.md, history.log, conventions.md, or task.md.
- LIGHTWEIGHT VISUALIZATION: Use a self-contained, established browser graph library (e.g., D3.js or Cytoscape.js via local static bundle or CDN-cached assets). No heavy multi-gigabyte node frameworks.
- COLOR TIER CONSISTENCY: Node fill color strictly follows Tier 0 (Grey), 1 (Amber), 2 (Blue), 3 (Teal), 4 (Green). Stars and sources render as badges, not background colors.
- LIVE RELOAD: Modifying `bep_map.yaml` or draft overlay files triggers automatic browser refresh without manual server restarts.

**CONTEXT & TECHNICAL CONSTRAINTS:**
- Configure `pixi.toml` task or small Python HTTP/WebSocket watcher server (`preview.py`) so `pixi run preview` starts the server and opens the browser.
- Implement clickable node interaction: compact node block on canvas; clicking opens a right-hand details drawer displaying Title, Tier, Stars, Rationale, Notes, Sources, and Open Questions.

**STEP 1: DISPATCH & EXECUTE:**
1. Create static frontend in `Academics/BEP/Catalysis/mindmap/static/` (`index.html`, `app.js`, `style.css`).
2. Implement tree layout with smooth zoom, pan, fit-to-view, branch toggle (expand/collapse), and details sidebar.
3. Implement `preview.py` with SSE/WebSocket live reload watching `data/*.yaml`.
4. Add unit and visual integration tests in `Academics/BEP/Catalysis/mindmap/tests/test_preview.py`.

**STEP 2: SUPERVISOR VERIFICATION:**
`pixi run pytest Academics/BEP/Catalysis/mindmap/tests/test_preview.py`

**STEP 3: SCOPED COMMIT:**
```powershell
git commit --only Academics/BEP/Catalysis/mindmap/static/index.html `
                  Academics/BEP/Catalysis/mindmap/static/app.js `
                  Academics/BEP/Catalysis/mindmap/static/style.css `
                  Academics/BEP/Catalysis/mindmap/preview.py `
                  Academics/BEP/Catalysis/mindmap/tests/test_preview.py `
          -m "feat(bep-mindmap): add interactive tree visualizer and live preview watcher"
```

**OPERATIONAL LIFECYCLE PROTOCOL:**
- Keep substrate warm! Daemons (:4001, :4096) stay running.
- Write the structured Phase 2 Rapport to `Academics/BEP/Catalysis/research/rapports/phase_2_rapport.md` with YAML frontmatter.
- Save any escalated questions to `Academics/BEP/Catalysis/research/questions/phase_2_questions.json`.
- Cleanly terminate the CEO session.
- Conclude with `<!-- GOAL_COMPLETE -->`.
````

---

### PHASE 3: Scientific Research Synthesis & Proposed Draft Overlay

````markdown
/wayfinder /harness /harness-guardian
**PHASE 3: SCIENTIFIC RESEARCH SYNTHESIS & PROPOSED DRAFT OVERLAY**

**GOAL:** Autonomously ingest existing BEP scientific research, models, and analyses A–M into an AI-proposed draft overlay across Physics, Mathematics, and Systems & Control.

**INVARIANTS & CONSTRAINTS:**
- PROPOSED DRAFT SEPARATION: Ingested nodes must be written to `Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml`. The canonical `bep_map.yaml` remains unpolluted.
- ZERO-HALLUCINATION CITATIONS (Rule 16): Every attached source must point to an examined paper/DOI, section, repository path, notebook cell, or analysis file. Never fabricate DOIs or author claims.
- TIER RESTRICTION (Rule 36): All AI-synthesized nodes start at Tier 1 (Amber). Tiers 2–4 require explicit owner confirmation. Do not treat numerical simulation success as physical validation.
- NO INTERACTIVE GRILLING: Unresolved scientific trade-offs or categorization ambiguities must be logged to the phase questions dossier, not asked mid-turn.

**CONTEXT & TECHNICAL CONSTRAINTS:**
- Inspect primary research sources:
  - Agent A synthesis: `Academics/BEP/Catalysis/research/` (Wayfinders, notes, literature reviews, analyses A–M).
  - Agent B reactor model: `Methanol-Catalysis` notebook PR #2 and model scripts.
  - Scientific coordination notes: Issue #58 and related dossiers.
- Populate coherent branch hierarchies under the three main arms:
  - **Physics:** Kinetics (Langmuir-Hinshelwood-Hougen-Watson), Thermodynamics (heat of reaction, phase equilibrium), Transport phenomena (intraparticle diffusion, external mass/heat transfer, Thiele modulus, effectiveness factor $\eta$).
  - **Mathematics:** Governing differential equations (1D/2D pseudo-homogeneous/heterogeneous models), stiff ODE/DAE solvers, numerical stability/discretization, parameter sensitivity.
  - **Systems & Control:** Reactor operating window, runaway sensitivity, parametric sensitivity, feed control, cooling jacket/heat exchange dynamics.

**STEP 1: DISPATCH & EXECUTE:**
1. Build synthesis pipeline `Academics/BEP/Catalysis/mindmap/synthesize_research.py`.
2. Extract verified topics, rationales, importance ratings (0–3 stars), source links, and status notes from repository materials.
3. Generate `Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml` validated against schema.
4. Verify visual rendering of the overlay in the UI (distinct styling for proposed vs. approved nodes).
5. Build verification script `Academics/BEP/Catalysis/mindmap/tests/test_synthesis.py` checking schema validity, branch assignment, and zero empty/dangling source fields.

**STEP 2: SUPERVISOR VERIFICATION:**
`pixi run pytest Academics/BEP/Catalysis/mindmap/tests/test_synthesis.py`

**STEP 3: SCOPED COMMIT:**
```powershell
git commit --only Academics/BEP/Catalysis/mindmap/synthesize_research.py `
                  Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml `
                  Academics/BEP/Catalysis/mindmap/tests/test_synthesis.py `
          -m "feat(bep-mindmap): synthesize BEP literature and simulation into proposed draft overlay"
```

**OPERATIONAL LIFECYCLE PROTOCOL:**
- Keep substrate warm! Daemons (:4001, :4096) stay running.
- Write Phase 3 Rapport to `Academics/BEP/Catalysis/research/rapports/phase_3_rapport.md` with YAML frontmatter.
- Save scientific ambiguities to `Academics/BEP/Catalysis/research/questions/phase_3_questions.json` (validated against QuestionItem).
- Cleanly terminate the CEO session.
- Conclude with `<!-- GOAL_COMPLETE -->`.
````

---

### PHASE 4: Collaborative Review Path & Question Dossier

````markdown
/wayfinder /harness /harness-guardian
**PHASE 4: COLLABORATIVE REVIEW PATH & QUESTION DOSSIER**

**GOAL:** Create a guided review path in the mind-map interface and compile a consolidated review dossier and question portfolio for the owner's evaluation.

**INVARIANTS & CONSTRAINTS:**
- STATE PURITY: Dispatched workers must NEVER touch state.md, history.log, conventions.md, or task.md.
- REVERSIBLE DEFAULTS: Every question presented to the owner must supply a recommended default option grounded in repository evidence.
- DETERMINISTIC PROMOTION: UI must support single-click promotion from draft overlay into canonical map, generating a precise MCP edit instruction for the user to confirm.

**CONTEXT & TECHNICAL CONSTRAINTS:**
- Guided Review Sequence: Group nodes into foundational dependencies first (Thermodynamics & Kinetics $\to$ Transport phenomena $\to$ Numerical discretization $\to$ Operational Control).
- Build the Guided Tour / Review Mode in `static/app.js` allowing the owner to step through proposed nodes sequentially, view supporting evidence, and accept, reject, or reparent each node.
- Compile all open scientific questions into `Academics/BEP/Catalysis/research/dossiers/bep_mindmap_review_dossier.md`.

**STEP 1: DISPATCH & EXECUTE:**
1. Implement Guided Tour component in `Academics/BEP/Catalysis/mindmap/static/app.js` and `style.css`.
2. Add "Promote to Approved" staging action in the details drawer that triggers the Python/MCP API.
3. Generate the master review briefing `Academics/BEP/Catalysis/research/dossiers/bep_mindmap_review_dossier.md`.
4. Run full end-to-end integration test suite `Academics/BEP/Catalysis/mindmap/tests/test_e2e_mindmap.py`.

**STEP 2: SUPERVISOR VERIFICATION:**
`pixi run pytest Academics/BEP/Catalysis/mindmap/tests/test_e2e_mindmap.py`

**STEP 3: SCOPED COMMIT:**
```powershell
git commit --only Academics/BEP/Catalysis/mindmap/static/app.js `
                  Academics/BEP/Catalysis/mindmap/static/style.css `
                  Academics/BEP/Catalysis/mindmap/research_review.py `
                  Academics/BEP/Catalysis/mindmap/tests/test_e2e_mindmap.py `
                  Academics/BEP/Catalysis/research/dossiers/bep_mindmap_review_dossier.md `
          -m "feat(bep-mindmap): add guided review mode and owner question dossier"
```

**OPERATIONAL LIFECYCLE PROTOCOL:**
- Keep substrate warm! Daemons (:4001, :4096) stay running.
- Write Phase 4 Rapport to `Academics/BEP/Catalysis/research/rapports/phase_4_rapport.md` with YAML frontmatter.
- Save consolidated questions to `Academics/BEP/Catalysis/research/questions/phase_4_questions.json`.
- Cleanly terminate the CEO session.
- Conclude with `<!-- GOAL_COMPLETE -->`.
````
