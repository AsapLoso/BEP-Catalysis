# Wayfinder: BEP Integrated Scientific Knowledge Campaign

> **Noun locks:** “reference map” means the AI-authored, source-linked dataset at `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/`; it does not mean the owner’s personal/approved mind map. “Periodic gain” means a measured or model-supported improvement against the best feasible steady control under the same objective and constraints; it is not presumed.
> **Owning dossier:** `Academics/BEP/Catalysis/state.md`.
> **Charting trigger:** User correction on 2026-10-22: continue from the existing unmerged integrated-map PR into substantive, multi-wave research; use Wayfinder only for dependencies and actual decisions.
> **Frontier summary:** Four AFK research questions organize catalyst/kinetics, conservation/transport/numerics, identification/control, and an independent source audit. Scientific work and node edits live in the separate research backlog and dataset.
> **Hard stops:** Keep the owner’s personal graph untouched; do not edit software/frontend; do not invent target kinetics, experiments, or gains; do not promote AI content above `idea`/`ai_worked_out`; do not contact researchers or commit to project-specific model choices on the owner’s behalf.
> **Map syntax:** Parser-facing tickets, islands, decisions, fog, and Execution Contract must retain the exact Wayfinder grammar; scientific content belongs in the integrated reference dataset.

## 1. Destination

This campaign advances the integrated AI reference dataset and leaves explicit evidence boundaries for what is still unknown. It does not certify a project-specific model or answer the BEP performance question without target data.

| Check | Verifiable end state |
|---|---|
| D1 | The three requested scientific threads are connected through substantive node explanations, equations/units where applicable, assumptions, source-scoped alternatives, limitations, evidence locators, and open questions. No fixed node count or depth is imposed. |
| D2 | Every concept and source-content mapping inherited from the earlier maps has a traceable disposition; useful scientific distinctions and source provenance remain machine-readable. |
| D3 | The evidence ledger distinguishes source observations, source-specific model results, mathematical consequences under stated assumptions, proposed models, and unverified hypotheses. Target-specific constants or performance results appear only if supported by accessible target evidence. |
| D4 | Independent second-pass review records supported claims, citation corrections, unresolved disputes, source-access limits, coverage gaps, and structural validation results in the research dataset. |

## 2. Decisions So Far

- [x] **2026-10-22 — Use the user-requested Physics, Mathematics, and Systems & Control arms and retain unlimited conceptual depth.** Evidence: current user goal and the existing root/discipline hierarchy in `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/nodes.yaml`.
- [x] **2026-10-22 — Keep AI reference content at `idea` or `ai_worked_out`; no inferred human understanding or verification.** Evidence: `.agents/skills/bep-map-edit-review/SKILL.md` and the current dataset’s maturity validator.
- [x] **2026-10-22 — Preserve prior maps and use explicit dispositions rather than silently replacing source records.** Evidence: user’s execution context and current `concept_mapping.yaml` / `source_provenance.yaml` lineage.
- [x] **2026-10-22 — Treat a periodic performance advantage as conditional and unestablished for the target BEP.** Evidence: existing `claim_reconciliations.yaml`, `uncertainties.yaml`, and lack of target-specific operation/data in the dossier.
- [x] **2026-10-22 — Keep Wayfinder as coordination and maintain the scientific research backlog separately.** Evidence: user’s latest instruction and the companion `research_backlog.yaml`.

## 3. Active Frontier

**Open research tickets: 4.** Each ticket is a bounded scientific synthesis decision; the research backlog lists the source-level work and data artifacts.

### Island: Catalyst and Kinetics

- [ ] **C1 Bound the catalyst-specific mechanism claims** (`wayfinder:research`) — *Question: Which adsorption, site-ensemble, intermediate, coverage, and kinetic claims are supported for each studied catalyst class, and which must remain competing hypotheses for the unidentified BEP catalyst?*
  - **Status:** Open; source review in progress.
  - **Mode:** AFK.
  - **Dependencies:** Existing integrated graph; accessible primary catalyst and kinetics papers; target catalyst remains unspecified but does not block source-scoped comparison.
  - **Objective:** Extend the graph and claim ledger so mechanism, active-site assumptions, PSSA closures, and explicit dynamic-coverage models cannot be conflated or transferred across catalysts without evidence.

### Island: Conservation, Transport, and Numerical Mathematics

- [ ] **M1 Set conservation and transport conventions** (`wayfinder:research`) — *Question: Which packed-bed, pellet, boundary, and thermal balance forms are equivalent under explicit basis conversions, and which assumptions alter the model or its numerical invariants?*
  - **Status:** Open; source review in progress.
  - **Mode:** AFK.
  - **Dependencies:** Existing integrated balance equations; primary reactor-analysis and numerical-analysis sources; declared variable bases and units.
  - **Objective:** Connect stoichiometry and inventories to conservative flux forms, PDE/ODE/DAE reductions, method of lines, stiffness, and independent numerical verification criteria.

### Island: Identification and Control

- [ ] **S1 Bound dynamical and periodic-operation claims** (`wayfinder:research`) — *Question: What can input/output measurements identify about reactor dynamics, and which periodic-operation results actually establish performance against an optimized steady comparator?*
  - **Status:** Open; source review in progress.
  - **Mode:** AFK.
  - **Dependencies:** Primary modulation-excitation and periodic-reactor literature; explicit separation of input realization, plant response, measurements, and objectives.
  - **Objective:** Connect excitation design, identifiability, observability, transport/analyzer filtering, cycle accounting, and a fair steady-versus-periodic feasible-set comparison.

### Island: Independent Evidence Audit

- [ ] **A1 Recheck scientific claims against primary evidence** (`wayfinder:research`) — *Question: Which substantive integrated claims and cross-discipline links survive a claim-by-claim second pass through accessible primary source text, and which remain unsupported or source-limited?*
  - **Status:** Open; independent audit not yet complete.
  - **Mode:** AFK.
  - **Dependencies:** Source locators in the integrated map; actual PDFs/primary records; the first three waves’ proposed additions.
  - **Objective:** Audit a spread across the three scientific threads, correct or narrow claims, and make inaccessible evidence and residual uncertainty explicit.

## 4. Not Yet Specified (The Fog of War)

### Island: Target-specific project decisions

- Target catalyst composition, support, preparation, pretreatment, active-state distribution, and catalyst-age window have not been supplied in this research handoff.
- The performance objective, inlet/product accounting boundary, safety/quality limits, and shared resource constraints for “best feasible steady” versus periodic operation require target project specification.
- The realized bed-inlet waveform and measurement-chain transfer functions (flow controller, lines, bed residence-time distribution, and analyzer) are not yet characterized in the integrated source set.
- Target-specific kinetic data, transient experiments, parameter uncertainty, validated simulator outputs, and physical replication remain unavailable here. These unknowns block a target-specific gain conclusion, not source-scoped scientific research.

## 5. Out of Scope

- Editing the existing personal/canonical BEP mind map or recording any human-understood/human-verified status.
- Frontend, parser, simulator implementation, parameter fitting, numerical optimization, or reactor operation.
- Contacting authors/supervisors, selecting target operating conditions, or claiming experimental performance without authorization and evidence.

## 6. Execution Contract

- verification_cmd: `python Academics/BEP/Catalysis/research/wayfinder/validate_bep_integrated_scientific_campaign_2026_10_22_map.py`
- scoped_commit_files: `Academics/BEP/Catalysis/research/wayfinder/bep_integrated_scientific_campaign_2026_10_22.md, Academics/BEP/Catalysis/research/wayfinder/bep_integrated_scientific_campaign_2026_10_22_prompts.md, Academics/BEP/Catalysis/research/wayfinder/validate_bep_integrated_scientific_campaign_2026_10_22_map.py, Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/research_backlog.yaml, Academics/BEP/Catalysis/state.md, Academics/BEP/Catalysis/history.log, task.md`
- commit_message: "Chart BEP integrated scientific research campaign"
