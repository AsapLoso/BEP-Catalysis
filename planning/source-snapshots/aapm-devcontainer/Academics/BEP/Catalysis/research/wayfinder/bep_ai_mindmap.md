# Wayfinder: BEP AI-Controlled Ownership Mind Map

## 1. Destination
A working, interactive, local BEP mind-map application with live browser preview (`pixi run preview`) and deterministic Python/MCP editing, pre-populated with an AI-synthesized research proposal overlay (covering Physics, Mathematics, and Systems & Control) grounded in existing scientific work, ready for owner-guided review.

## 2. Decisions So Far
- [x] (2026-10-19) PR #84 specification approved: root BEP node with exactly three main arms (Physics, Mathematics, Systems & Control).
- [x] (2026-10-19) Color represents a single maturity/ownership tier (0: Idea, 1: AI Proposal, 2: Owner Understood, 3: Informal Notes, 4: Formal Derivation).
- [x] (2026-10-19) Node importance uses 0–3 stars; sources and stars are displayed as badges/metadata, not competing colors.
- [x] (2026-10-19) Storage of record is a human-readable, git-tracked YAML file with atomic writes.
- [x] (2026-10-19) Deterministic Python/MCP tool handles graph mutations (add, rename, reparent, delete, set tier/stars, attach sources).
- [x] (2026-10-19) Preview experience mirrors Methanol-Catalysis via `pixi run preview` with file watching and auto-reload.
- [x] (2026-10-19) Dual-layer map separation: canonical owner-approved nodes remain unpolluted; AI research synthesis is stored in a separate proposal overlay.

## 3. Active Frontier

### Island: Platform & Core Engine
- [ ] **WF-01: YAML Schema & Deterministic Python/MCP Editor** (`wayfinder:task`) — *Question: How to implement atomic, schema-validated node additions, edits, and parent-child integrity without corrupting the YAML file?*
- [ ] **WF-02: Interactive Graph Visualizer & Live Preview** (`wayfinder:prototype`) — *Question: How to render a directed, pan/zoomable, collapsible tree in the browser via `pixi run preview` that automatically updates when the YAML changes?*

### Island: Research Synthesis & Draft Overlay
- [ ] **WF-03: Synthesize BEP Scientific Material into AI Draft Overlay** (`wayfinder:research`) — *Question: How to partition existing Agent A/B findings, analyses A–M, and reactor models into Physics, Mathematics, and Systems & Control without promoting unverified claims to Tier 2+?*

### Island: Review Flow & Question Dossier
- [ ] **WF-04: Guided Exploration & Question Dossier Preparation** (`wayfinder:task`) — *Question: How to structure the review path and format owner-facing ambiguities into a validated Pydantic QuestionItem dossier?*

## 4. Not Yet Specified (The Fog of War)
- *[Island: Remote Integration] Direct remote ChatGPT-to-local-stdio-MCP tunneling.*
- *[Island: Voice Interface] Local speech-to-text brainstorming transcription.*
- *[Island: Automated Promotion] Rules for promoting nodes from Tier 1 to Tier 2 based on conversational owner signals.*

## 5. Out of Scope
- Direct mutation of canonical owner-approved nodes without explicit owner instructions.
- Modifying Agent A or Agent B repository outputs or simulations.
- Global git staging (`git add -A` / `git add .`).
- Interactive mid-run grilling questions during overnight autonomous execution.
- Complex database servers, cloud hosting, or multi-user access control.

## 6. Execution Contract
- verification_cmd: `pixi run pytest Academics/BEP/Catalysis/mindmap/tests/`
- scoped_commit_files: `Academics/BEP/Catalysis/mindmap/`, `Academics/BEP/Catalysis/research/rapports/`
- commit_message: "feat(bep-mindmap): implement mind map engine, preview, and research draft overlay"
