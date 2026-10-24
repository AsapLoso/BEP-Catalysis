# BEP V3 — Persistent actionable checklist

**Scope:** V3 *execution* in `AsapLoso/BEP-Catalysis`. [GOAL.md](GOAL.md) defines strict completion. This document is a **seed register, not a replacement for local `goals/01–05`**. Reconcile *every* original mandatory checkbox before considering this list exhaustive.

**Important:** All checkboxes below start open because this GitHub docs branch cannot independently audit the **unpushed** local V3 checkout (reported commit `2586777`). Existing work may satisfy some items; mark them only after verification. Do not delete these tasks or count a `BLOCKED` as done.

### A. Recover the original requirements and actual state

- [ ] **A01** Verify local `v3/bep-vertical-slice-20261023` branch, reported `2586777`, actual HEAD, clean/dirty state, existing deliverables and parallel work; preserve all changes.
- [ ] **A02** Read and enumerate *every* requirement in original full `BEP_V3_GOAL.md`, current `notebooks/v3/GOAL.md`, `goals/01–05`, and `PROGRESS.md`. Add missing ones **without deleting originals**; record their exact source and acceptance conditions.
- [ ] **A03** Create/update `notebooks/v3/REQUIREMENT_AUDIT.md`: one row per unique criterion with ID, original source, priority, `VERIFIED|PARTIAL|BLOCKED|NOT STARTED`, files/lines/cells, reproducible proof, limitation and next action. Reconcile item counts with source checklists.
- [ ] **A04** Re-audit every previously green gate and previously checked item against the actual acceptance condition; reopen unsupported claims. Specifically explain why the 17-cell gas-only PSSA baseline was called "complete" relative to the coupled-reactor mission.
- [ ] **A05** Keep `PROGRESS.md` and this TODO synchronized: recorded science decisions, external blockers, live frontier, receipts and next action. Any original goal requirement not listed below must become an additional tracked item; no disappearing checkboxes.

### B. Inventory: five scientific inputs and engine dependencies

- [ ] **B01** Locate, snapshot immutably and SHA-pin **V0 script**: `AsapLoso/project-management-agents/Academics/BEP/Catalysis/3_Model/c2h2_hydrogenation_transient_model.py`.
- [ ] **B02** Locate, snapshot and SHA-pin **legacy migrated notebook**: `AsapLoso/Methanol-Catalysis`, `main`, `content/c2h2_hydrogenation_transient_model.ipynb`.
- [ ] **B03** Locate, snapshot and SHA-pin **V1**: `AsapLoso/Methanol-Catalysis`, `feat/bep-dynamic-reactor-response-notebook`, `notebooks/bep_dynamic_reactor_response.ipynb`.
- [ ] **B04** Locate, snapshot and SHA-pin **V2**: `AsapLoso/Methanol-Catalysis`, `feat/bep-dynamic-reactor-response-v2`, **same path, different ref**.
- [ ] **B05** Locate, snapshot and SHA-pin **presentation notebook**: `AsapLoso/project-management-agents/Academics/BEP/Catalysis/presentation/BEP_Catalysis_Presentation_v1.ipynb`; label its illustration vs simulation status.
- [ ] **B06** Check `SOURCE_MANIFEST.md` against **all five exact blob hashes** and recorded upstream refs, and independently inspect each artifact's states, equations, parameter origins, boundaries, discretization, solver, observed outputs and known issues.
- [ ] **B07** Read V0 `3_Model/transient_model_framework_audit.md` and `3_Model/state.md`; map **each** known model and code defect to V0/legacy/V1/V2/V3: fixed, inherited, inapplicable with reason, or unverified.
- [ ] **B08** Establish reproducible pinned `pbr` engine and environment (especially V2 `pbr/` code, provenance, tests, `TECHNICAL_HANDOFF_V2.md`). Independently execute the necessary tests and preserve commands/outputs; distinguish inherited tests from new V3 tests.

### C. Theory first: artifact map and personal learning coverage

- [ ] **C01** For **each of five input artifacts**, independently populate `ARTIFACT_THEORY_MAP.md`: exact section/cell/function → equations/states/closures/parameters/boundaries → primary source and locator → exact existing AI node ID (or `UNMAPPED`) → relevant personal node/actual approval scope (or `NOT REVIEWED`).
- [ ] **C02** Verify every AI reference node ID in `research/integrated_reference_map_2026_10_22/nodes.yaml`, and relevant `sources.yaml`, `uncertainties.yaml`, `claim_reconciliations.yaml` and `concept_mapping.yaml`; never invent node IDs or promote AI evidence to human verification.
- [ ] **C03** Check `research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml` and relevant reader pages **read-only**. Distinguish owner placement approval, basic concept understanding, owner prose, and individual source verification; document learning gaps explicitly.
- [ ] **C04** Compare the five artifacts' scientific incompatibilities: PSSA vs dynamic surface kinetics; uniform vs finite pellet diffusion; external film vs no-film; axial dispersion vs pure advection; catalyst identities; temperatures, flows, units, rate bases, and original V0 state-space choices.
- [ ] **C05** Produce an actionable evidence/contradiction/gap register linked to specific model features and owner discussion priorities, not a vague summary. Complete a traceable theory-to-code crosswalk for **every essential chosen V3 component**.

### D. Model blueprint — mandatory prior to claims of completion

- [ ] **D01** Review `MODEL_BLUEPRINT.md` against the actual V0 framework and all verified theory. Identify source-supported retained fields, removed fields and explicitly unsupported states; explain every V0 → V1/V2 → V3 departure.
- [ ] **D02** Specify a coherent coupled vertical slice with inlet, axial bulk inventory, **resolved radial pellet transport** and reaction/outlet behavior where supported by V2 code and evidenced kinetics. If disabled, record why this still satisfies *or fails* the original objective; only the owner can approve a permanent reduction.
- [ ] **D03** Specify source-supported kinetics and full provenance: primary source table/equation, gas/rate/site units, temperature, partial pressures, catalyst identity, reactor and pellet assumptions, and exactly which parameters were transferred from other studies.
- [ ] **D04** Specify the surface-coverage closure: whether algebraic PSSA or dynamic differential states; justify via available elementary rates, identifiability, source conditions and resulting state count. **Never invent missing elementary constants.** Record the unfinished dynamic-coverages ambition as a visible decision/limitation.
- [ ] **D05** Specify numerical scheme, grid/state layout, initial/boundary conditions, interphase flux and reaction bookkeeping, conservative balances, solver approach, positivity, sensitivity/convergence tests, and acceptance thresholds; cite source and existing code for each.
- [ ] **D06** Identify a precise published steady-state test case and minimum evidence for comparability, including parameter values, reactor geometry/catalyst/feed match and uncertainties; no fake source-matched benchmark.
- [ ] **D07** Ensure `MODEL_BLUEPRINT.md` is an independently inspectable *design decision with tests* rather than a retrospective justification of a pre-selected reduced implementation.

### E. Implementation and verification

- [ ] **E01** Preserve the existing `bep_v3_vertical_slice.ipynb` as a demonstrable baseline; audit its 17 cells, model configuration, inline plots, outputs and dependencies against the actual blueprint.
- [ ] **E02** Implement or demonstrate the **source-supported bulk+radial pellet coupled** configuration with meaningful radial and inlet/outlet plots (use existing V2 infrastructure where appropriate), documenting what changes relative to uniform gas-only V3. No unapproved scientific additions.
- [ ] **E03** Check physically meaningful behavior: units, bulk/pore exchange conservation, reaction stoichiometric/elemental accounting, zero/finite diffusion sanity, boundary conditions, negative concentrations and solver diagnostics. Add tests targeted at V3-specific choices; don't cite only inherited 63 engine tests.
- [ ] **E04** Run both reduced baseline and coupled configuration reproducibly from a clean checkout; preserve versions, exact commands, elapsed status and figures. Test at least one grid/tolerance refinement or explain evidenced numerical limits.
- [ ] **E05** Evaluate periodic forcing only to the extent actually supported. Differentiate “5 simulated periods” from **verified periodic settling**; do not claim periodic-orbit convergence without checking.
- [ ] **E06** Independently inspect any local changes to `vendor/pbr` and keep exact source hashes, test receipts, dependency lock and clean-checkout instructions. Preserve source snapshots, don't casually fork numerics.
- [ ] **E07** Audit Urmès 2019 **K₁ = 611 Pa⁻¹ text versus 13 Pa⁻¹ Table 5** using primary evidence; record calculations/sensitivity and the remaining unresolved interpretive question without presuming a units conversion.

### F. Published comparison, learning map and supervisor review

- [ ] **F01** Attempt a *genuinely comparable* published steady-state benchmark and report conversion/selectivity/flow discrepancies and source-condition mismatches quantitatively. Mark comparison/reproduction/experimental validation as distinct evidence levels.
- [ ] **F02** Resolve or explicitly retain blockers for material source transfer, pellet properties, reactor residence-time assumptions and catalyst system mismatches. A documented blocker is not a completed scientific validation.
- [ ] **F03** Complete `THEORY_CROSSWALK.md` for **all essential implemented equations, closures and parameters**, with existing AI IDs, primary-source locators, owner-map node references or gaps, and code cells/modules.
- [ ] **F04** Create/verify `STUDY_PRIORITIES.md` with at most five *specific owner discussion questions* prioritized by what blocks understanding of V3. **Do not edit, approve or auto-populate the personal map.**
- [ ] **F05** Complete `README.md`: clean-checkout reproduction, recommended notebook reading path, interpretation of figures and explicit model/validation limits.
- [ ] **F06** Complete `DAMIAN_HANDOFF.md`: short, accurate model explanation, actual output and scientific limitations, two–three specific questions, and distinct verified vs unverified claims. **Prepare for owner review only**; no autonomous send.

### G. Honest closure

- [ ] **G01** Cross-check that every line/item in *all* source checklists (`goals/01–05`, original goals, this file and `PROGRESS.md`) appears in `REQUIREMENT_AUDIT.md` with proof and a consistent status.
- [ ] **G02** Verify that **every mandatory item** is `VERIFIED`. For owner-authorized waivers, retain original item and link exact owner decision; do not mark a waiver as a verified implementation.
- [ ] **G03** Report quantitative `VERIFIED/PARTIAL/BLOCKED/NOT STARTED` totals; exact changes/test outputs; scientific outcomes and limits; source/engine SHA; branch/commit; next unblocked step.
- [ ] **G04** Use goal-completion action **only** if G01–G03 pass and no mandatory requirement remains open. Otherwise report **INCOMPLETE — BLOCKED/IN PROGRESS**, checkpoint and continue unblocked tasks. Never stop as “complete” based on a prior completion label, clean Git status, running notebook or duplicated completion report.

## Audit register row format

`ID | original file + location | mandatory? | acceptance criterion | status | observed evidence (file/cell, command, result, SHA) | unresolved gap | next action`

**Reconcile first, then execute.** Keep the full detailed evidence in `REQUIREMENT_AUDIT.md`, not as long repetitive chat messages. Maintain checkboxes in this file as a compact working index. A row with `BLOCKED`, `PARTIAL` or `NOT STARTED` remains `[ ]`.

## Scope / safety

No silent downgrading of coupled science to gas-only as a *completed* goal; no invented adsorption dynamics or literature values; no automatic human scientific approval; no personal-map mutation; no unapproved push/PR/merge; no Damian send. This document may grow as original local `goals/01–05` are reconciled, but source commitments may not disappear.
