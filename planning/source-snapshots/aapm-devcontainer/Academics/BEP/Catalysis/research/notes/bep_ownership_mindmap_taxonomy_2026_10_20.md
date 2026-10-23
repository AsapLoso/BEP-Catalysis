# BEP Ownership Mind Map — Canonical working taxonomy, layout conventions and next steps

**Captured from user/AI design conversation:** 19–20 October 2026  
**Status:** **DRAFT SCIENTIFIC BACKBONE FOR CONVERSATIONAL REVIEW**, not an approved Level-2 taxonomy. **A web/Python mind-map implementation and canonical/draft YAML already exist** at `Academics/BEP/Catalysis/mindmap/`; local runtime, latest unpushed state, test outcomes and migration compatibility remain unverified. See [the node contract](bep_mindmap_node_contract_2026_10_20.md).  
**Relationship:** [**Cloud Work two-stage handoff (21 Oct)**](bep_mindmap_work_handoff_2026_10_21.md) · [**UI wishlist & focus-path concept (20 Oct)**](bep_mindmap_ui_wishlist_2026_10_20.md) · [**Node record contract + PDC reference (20 Oct)**](bep_mindmap_node_contract_2026_10_20.md) · [Implementation/interaction specification (19 Oct)](bep_ai_mindmap_spec_2026_10_19.md) · [BEP state](../../state.md) · [root tracker](../../../../../task.md)  
**Scientific source context:** [BEP proposal `main.tex`](../../0_Project_Management/main.tex), [proposal methodology `section3_method.tex`](../../0_Project_Management/section3_method.tex), [proposal roadmap `bep_proposal_roadmap.md`](../../0_Project_Management/bep_proposal_roadmap.md), [A–M index](../../presentation/RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md), [A–M structure/status](../../presentation/PRESENTATION_STRUCTURE.md).

> **Authority split.** The structural principles explicitly voiced by the user are decisions. The names and scientific contents of the **15 Level-2 themes** are an **AI proposal** grounded in the proposal and broader discussion; the user said "Second layer, I guess", and requested this layout be *persisted*, **not that every node has been approved for the live map**. Do not promote this draft into actual YAML/verified scientific understanding or mark the fifteen themes human-worked-out without another approval.

## START HERE — concrete execution checklist (2026-10-20)

**This section is the canonical compact/re-entry checklist, not just a summary.** Read it FIRST after chat compaction or a new session, along with any updated user instructions. Follow exact checkboxes, source locations and the **Next action** below; never reconstruct completion from chat memory. All boxes below start unchecked unless a completion receipt/owner approval is explicitly documented. **Keeping the plan in GitHub is authorized; populating/reorganizing the live map without a specific owner command is not.**

**Goal correction from user:** **RETROFIT the existing/currently-being-built mind-map application** with this scientific taxonomy and interaction contract. **Do not build a second mock, greenfield demo or competing viewer**. Any "make a prototype/seed app" language in the older spec is superseded. **GitHub code location now identified:** `Academics/BEP/Catalysis/mindmap/` on `devcontainer`: 4 canonical YAML nodes and 15 separate older AI-draft overlay nodes, with editor/MCP/preview/tests present. See [the node contract and code audit](bep_mindmap_node_contract_2026_10_20.md). Local unpushed work, runtime and tests are **still UNVERIFIED**. Do not reset or overwrite a working tree. Current five-tier `tier` and implicit promote-to-owner-status need a semantic retrofit, **not** replacement with another app.

**Confirmed structural decision (user, 20 Oct):** **NO MAXIMUM DEPTH.** Six layers was *only* an example; the map may descend to 7, 8, 9+ whenever the scientific concepts warrant it. **C1 Catalytic Chemistry must contain two major first-generation child nodes:** `c1_reaction_chemistry_pathways` (Reaction Chemistry & Pathways) and `c1_catalyst_active_site_chemistry` (Catalyst Chemistry & Active Sites). Both are especially important. This approves their **relative structural placement**, not the underlying chemical explanations, citations, all of C1's boundaries or any scientific maturity. The child nodes are currently `tier: 0` / `is_draft: true`. **A–M L4/L5/L6 checkboxes are coverage checkpoints, NOT a prescribed limit**; the letters need not always sit at exactly Level 3, and each can have several intermediary categories and unlimited descendants. No renderer/editor may enforce a depth-6 cap. The map depth is calculated from parent pointers.

**UX design wishlist (owner, 20 Oct):** Current screenshot exposes a too-dense layout, an inappropriate parallel `Deep Dive Letters (A–M)` root and additional administrative root material. Owner requests top-branch padding and is considering a **one-line/focused path view**: single ancestry back to root, selected branch and children to right, hiding unrelated subtrees. **Wishlist only**; [prioritized UI review and assistant alternatives](bep_mindmap_ui_wishlist_2026_10_20.md) include an Overview + Focus design, letter-index/cross-link lens, breadcrumbs, search, status legend fixes, responsive controls and a source/runtime preflight. Screenshot may reflect newer local WIP than GitHub `devcontainer`; do not assume the extra root branches originate in the current checked-in YAML. No app code changed or node approval implied.

**UI clarification (21 Oct, owner):** The focused view stays within the **existing graphical canvas**, with **real nodes connected by edges** from root through selected node and immediate descendants to the right. The earlier suggested **Miller-columns/list layout is explicitly rejected**. Click a node to focus; hover snippet and separate explanatory popup are low-priority speculation, not this iteration's requirement. Use GitHub/cloud Work without PC synchronization by default; [handoff/read-only first, then separate goal](bep_mindmap_work_handoff_2026_10_21.md). No science node approvals follow from this UI discussion.

**Working cursor — next human/AI dialogue:** **C1–C5, Physics Level-2 themes** (review names, boundaries, missing content); then C6–C10 Mathematics, C11–C15 Systems & Control. Level 1 is settled as three disciplines; 15 exact Level-2 themes remain an **AI draft** until accepted. No Level 3/4/5/6 scientific review marked complete by this checklist. Retrofits may proceed in a parallel implementation lane *only* on located source and approved changes, not by regenerating a mock.

### A. Implementation reconnaissance and retrofit (not a greenfield build)

- [ ] **R1 — Locate existing work:** identify actual repo, checked-out branch, relevant worktree/PR, source files, persisted graph, runner, editing tool/MCP, and local changes. **Read-only preflight**; do not sync/reset/overwrite a live unsaved implementation. Record exact verified paths and commit SHA or "LOCAL-ONLY / NOT ACCESSIBLE".
- [ ] **R2 — Audit the existing implementation against the scientific contract:** which parts already work (rendering, zoom, pan, collapse, details, YAML, editing, citation statuses, live reload)? Mark gaps; preserve functioning features.
- [ ] **R3 — Write minimal retrofit changes**, not a parallel prototype: preserve actual node IDs/data and API contracts, migrate formats if needed, and keep the actual code's ownership and host constraints.
- [ ] **R4 — Verify integration:** test both approved and rejected/ambiguous edits, citations independent of maturity, deep nested nodes, local `pixi run preview` where relevant, live file reload, no source invention; capture executable receipts.
- [ ] **R5 — Reconcile to GitHub:** record actual branch/path/commit/PR and status; avoid discarding unpushed work, cross-worktree changes or concurrent modifications. Do not claim the application complete just because these design notes are merged.

**Implementation pointer:** **GitHub** `devcontainer:Academics/BEP/Catalysis/mindmap/` with `schema.py`, `editor.py`, `mcp_server.py`, `preview.py`, `static/`, `tests/`; **4 canonical nodes, 33 draft-overlay records** (15 older AI research nodes, 15 theme proposals, one PDC foundation, **two new C1 children**). **Local worktree / unpushed changes / tests / execution = UNVERIFIED**. No actual application modification recorded by this discussion. See [node contract](bep_mindmap_node_contract_2026_10_20.md).

### Draft-overlay staging receipt (not approval)

- **Stage:** `feat/bep-mindmap-level2-draft-2026-10-20` — actual data file `Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml` (no change to `bep_map.yaml`). This is the project's pre-existing visualization, NOT a mock.
- **Added Level-2 idea nodes:** `physics_catalytic_chemistry`, `physics_reaction_kinetics`, `physics_transport_phenomena`, `physics_reactor_thermodynamics`, `physics_experiments_measurements`; `math_mathematical_modelling`, `math_numerical_analysis`, `math_dynamical_systems`, `math_inverse_problems`, `math_optimization_theory`; `system_modelling_reduction`, `system_identification`, `system_filtering_estimation`, `system_input_experiment_design`, `system_control_optimization` — **each tier 0 / is_draft true, C1–C15 still unchecked**.
- **Proposed PDC foundation:** `pdc_process_dynamics_foundations` under `system_modelling_reduction`, **tier 1 AI worked out / draft**, citation path to the archived course overview. It is NOT a new Level-2 theme or validated reactor evidence.
- **Original AI nodes:** all fifteen retained with original IDs, descriptions and citations; eleven top-level draft children were reparented beneath the matching proposed Level-2 themes. Their internal children were retained. This reorganization is explicitly **provisional**, not owner-approved.
- **Known implementation mismatch:** old tier 0–4 model and promotion defaults still present. Do not infer scientific ownership from the existing root's old `tier: 2`, and don't use the old UI Promote action as a shortcut. Full schema migration/verification is a separate retrofit task.
- **Validation level:** static ID/parent/cycle/expected-count verification during write, and committed Git diff inspection. Python tests and live browser behavior have not been run in this session. 

### C1 discussion receipt — AI research drafted, OWNER APPROVAL PENDING

- **2026-10-20 | status:** Existing draft node `physics_catalytic_chemistry` enriched with substantive AI notes, two AI-attached sources, three boundary questions, and changed **tier 0 Idea → tier 1 AI worked out**. **Draft remains `is_draft: true`; canonical `bep_map.yaml` is unchanged.** User acknowledged we are *currently building an AI/idea-level map*, **not** that C1 classification or its science is personally reviewed.
- **Boundary proposal:** C1 handles net chemical network, catalysts/site chemistry, candidate parallel pathways, ethylene/ethane selectivity. C2 handles mathematical rate laws, parameters and transient site ODEs. Transport/reactor conditions and experimental measurements retain separate homes. These are AI-proposed boundaries for the user's C1 review.
- **Source pointers:** [Deep dive C mechanism/code audit](../../presentation/deep-dives/C_reaction_mechanism_2026-10-14.md), [Urmès 2019](https://doi.org/10.3390/catal9020180); all citations AI-attached in this graph until owner verifies an exact claim/source linkage.
- **Next exact decision:** Does the C1/C2 division stand? Should `Catalyst Surface / Active-Site Chemistry` remain in C1, or be its own Level-2 theme? **C1 checklist remains unchecked until user explicitly accepts/revises.** C2–C15 remain unchecked.
- **Verification:** Node count still 31 in overlay; only C1 node changed; no program code was modified or browser/Python tests run in this edit.

### 2026-10-21 — C2 science-data pass, independently diff-reviewable

**Science data ONLY.** Added **eight new AI-worked-out/yellow nodes** beneath C2 `physics_reaction_kinetics`: four nodes on Urmès 2019 effective PSSA kinetic rates, adsorption denominator (including pressure units), net rate expressions, and fixed-versus-fitted parameter ledger; four on PSSA versus explicit dynamic surface closures, reactor-versus-surface memory, elementary-parameter calibration gap, and transient identifiability. Corrected existing `centered_arrhenius` node to retract the unsupported blanket claim that centering automatically eliminates parameter correlations and to clarify (k(T_ref)) versus the uncentered pre-exponential (k^0).

**Independent reversible logical checkpoints:** each four-node topic group was committed separately, and the Arrhenius correction was a third separate commit. Each GitHub commit's patch was fetched and inspected, confirming only `data/bep_draft_overlay.yaml` changed in each. The full C2 branch diff is reviewable in the PR Files view. The [map edit skill](../../../../.agents/skills/bep-map-edit-review/SKILL.md) documents the diff/revert cycle; **a Git diff is not scientific proof**.

**Result:** **69** AI draft nodes (previous 61 + 8), plus **4 unchanged** canonical root/arm nodes. No old node removed or reparented; only the old centered Arrhenius explanation changed. Deepest graph depth remains **8**. Added nodes `c2_urmes_2019_effective_rates`, `c2_urmes_2019_adsorption_denominator`, `c2_urmes_2019_net_rates`, `c2_urmes_2019_parameter_ledger`, `c2_surface_kinetic_closure_choices`, `c2_pssa_not_steady_reactor`, `c2_dynamic_theta_model_calibration_gap`, `c2_transient_parameter_identifiability`. All remain `tier:1` /`is_draft:true`, sources AI attached from [D deep dive](../../presentation/deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md) and the C mechanism audit, with explicit unverified applicability and no personal-maturity promotion. The broader C2 theme remains only an **Idea** and its human review checkbox OPEN.

**Checks:** read-only structural checks for IDs, parent existence, acyclicity, draft flags and quoted notes; commit patches checked for node-only additive changes and targeted correction. **No Python/Pydantic round trip, browser or full tests executed**; continue to avoid E2E promotion tests on real YAML.

**Next scientific data cursor:** independent C2 source applicability / fitting correlation questions and the existing Larsen extended LHHW node need review; then C3 Transport Phenomena, with proposal-anchored evidence and A–M scientific cross-links. Do not turn this AI data pass into owner approval.

### 2026-10-21 — C1 backend scientific data pass (AI-generated, not owner-reviewed)

**Scope:** scientific data only; **NO frontend/preview/schema edits**. The existing `Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml` now has **61 draft nodes** (33 previous + **28 new C1 chemistry descendants**), alongside the unchanged 4-node canonical map. Three added nodes are Tier 0 **Idea**, 25 are Tier 1 **AI worked out**. The existing two large C1 child nodes remain Tier 0; their placement had been structurally selected by the user. No human-understood status and no human-verified citations created.

**Scientific concept organization; these are independently recorded nodes, not mere parent-note paragraphs:**

```text
C1 — Catalytic Chemistry
├─ Reaction Chemistry & Pathways [user-selected branch, draft idea]
│  ├─ Net stoichiometric network
│  │  ├─ Acetylene → ethylene
│  │  ├─ Ethylene → ethane → inlet ethylene relevance
│  │  └─ Gas source vector, plus warning about transient site storage
│  ├─ Microscopic surface pathway
│  │  └─ Horiuti–Polanyi family → vinyl* → adsorbed ethylene*
│  │                              ├─ ethylene desorption [depth 8]
│  │                              └─ ethyl* continuation [depth 8]
│  ├─ Alternative ethane routes → conditional omission → ethylidene idea
│  └─ C4+/coke/deactivation idea
└─ Catalyst Chemistry & Active Sites [user-selected branch, draft idea]
   ├─ Catalyst identity → Urmès 2019 Pd/α-Al2O3 source
   │                   └─ PdAg/SiO2 transfer → multisite/hydride idea
   └─ Surface sites → six-term / reduced site balances
                   → adsorption/desorption → H2 dissociation → adjacent vacancies
                                            → acetylene/ethylene competition → readsorption
                   → chemical-mechanism vs kinetic-closure boundary
```

**Source basis:** [C mechanism deep dive](../../presentation/deep-dives/C_reaction_mechanism_2026-10-14.md) §C.1–C.5.1, with its references to Urmès 2019 (DOI 10.3390/catal9020180), Bos & Westerterp 1993, Mei et al. 2009 and Borodziński & Bond 2006. Each node has a scoped **AI-attached** source or paper link, substantive notes, rationale and a concrete open question; direct source verification is not implied. Preserve limits: 2019 is fitted effective PSSA kinetics under source-specific conditions, not a calibrated dynamic surface θ model; the alternative ethylidene / coke / multisite paths are open scientific ideas, not source-fitted third rates. Avoid conflating gas-only source vector with gas+site inventory.

**Backend structural checks:** 61 unique overlay IDs, all existing parent IDs resolvable, no parent cycles, 61 `is_draft: true` flags, 4 canonical nodes unchanged. Deepest current descendant is at graph **Level 8**. YAML parsing and runtime/Python tests **NOT executed** in this session; current schema supports the existing source fields but lacks independent per-citation review state, so that AI-attached caveat is recorded in `section`/notes until a backend metadata migration.

**Status/next:** this is a **completed AI-authored data pass**, not completed C1 owner review; **C1 and the A–M owner-review checkbox passes remain unchecked**. Next scientific expansion: C2 Reaction Kinetics & Surface Dynamics, separating algebraic LHHW/Arrhenius parameters from explicit θ dynamics; then C3 transport and other Level-2 themes. No science or frontend change outside C1 is authorized merely by this record.

### C1 structural decision receipt — two high-priority children, recursive depth

```yaml
checkpoint: C1
date: "2026-10-20"
action: accept_structure
parent_id: physics_catalytic_chemistry
user_decision: >-
  Keep BOTH Reaction Chemistry & Pathways AND Catalyst Chemistry & Active Sites
  as major child branches beneath C1. They matter substantially. The tree is not
  limited to six levels; 7+ levels are permissible and naturally expected.
child_nodes:
  - id: c1_reaction_chemistry_pathways
    parent: physics_catalytic_chemistry
    approval_scope: structural_child_only
    maturity: idea
  - id: c1_catalyst_active_site_chemistry
    parent: physics_catalytic_chemistry
    approval_scope: structural_child_only
    maturity: idea
source_review: ai_attached_or_none
graph_mutation: draft_overlay_only
scientific_ownership_promoted: false
```

- **Real file updated:** `mindmap/data/bep_draft_overlay.yaml`; C1 parent annotated, both child records added as `tier: 0` (Idea), `is_draft: true`. The child examples in their notes (Horiuti–Polanyi / intermediate chemistry; catalyst/adsorption/site competition) remain **illustrative AI suggestions**, **not constructed deeper child nodes** or verified science.
  - **UPDATE 21 Oct:** Selected deeper mechanism concepts were **subsequently added as individual AI-draft nodes** in the scientific-data pass above. The original two-child structural receipt is kept as history, but its then-current 'not constructed' status is superseded.
- **C1 theme checklist stays OPEN** pending full agreement on C1's scope and relation to C2; acknowledging these two important subbranches is not acceptance of every proposed C1 scientific boundary.
- **No fixed level per letter:** a subject/category may intervene between thematic Level 2 and research-letter anchor, so the original “letters at L3; children at L4–6” is *illustrative*, not mandatory. Review each letter through progressively deeper checkpoints regardless of actual numeric depth. Do not pad the map merely to hit a quota.
- **Next conversational checkpoint:** review remaining C1 boundaries, then C2–C5 Physics; the two important C1 children are now explicit, not lost to chat compaction.

### B. Level 0–1 invariants

- [x] **C0 — Scope and discipline decision:** one BEP project root; exactly **Physics**, **Mathematics**, **Systems & Control** as its three Level-1 arms. Scientific scope covers the *whole project*, including unfinished, experimental and future work, not just letters or completed presentations. **This is a user design decision, not populated YAML evidence.**

### C. Level 2 — review all 15 proposed broad themes; one topic per checkbox

**Tick a C-box only when the user has accepted/renamed/merged that theme and its boundary.** Record the accepted name and any reassignment in Section 3; checking a theme does not make its scientific notes "Human worked out".

#### Physics
- [ ] **C1 — Catalytic Chemistry:** mechanisms, catalysts, competing reaction paths, selectivity (distinguish from kinetics). **AI notes drafted in actual `bep_draft_overlay.yaml` (node `physics_catalytic_chemistry`, tier 1), NOT HUMAN APPROVED; decide C1/C2 boundary with owner before checking this.**
- [ ] **C2 — Reaction Kinetics & Surface Dynamics:** rate expressions, surface states, PSSA vs dynamic kinetics.
- [ ] **C3 — Transport Phenomena:** axial transport, intra-pellet diffusion, film transport, scaling.
- [ ] **C4 — Reactor Physics & Thermodynamics:** conditions, geometry, timescales, pressure, heat/energy assumptions.
- [ ] **C5 — Experiments & Measurements:** catalyst/apparatus, GC, spectroscopy, MFCs, measurement uncertainty, experimental validation.
#### Mathematics
- [ ] **C6 — Mathematical Modelling:** governing PDE/ODE/DAE equations, boundary and initial conditions.
- [ ] **C7 — Numerical Analysis & Simulation:** discretization, stiffness, solvers, consistency/error and convergence.
- [ ] **C8 — Dynamical Systems & Stability:** fixed points, Jacobians, spectra, periodic solutions.
- [ ] **C9 — Inverse Problems & Uncertainty:** well-posedness, identifiability, regularization, error bars.
- [ ] **C10 — Optimization Theory:** objective/constraint formulations, algorithms, numerical optimality.
#### Systems & Control
- [ ] **C11 — System Modelling & Reduction:** grey-box state-space, reduced representations, model–plant mismatch; **PDC Process Dynamics foundation** (dynamic modelling, linearisation/transfer functions) as candidate lower-level subject/cross-link, not an automatically approved Level-2 addition.
- [ ] **C12 — System Identification:** input/output fitting, parameter recovery, informative identification experiments; compare PDC step response/FOPTD techniques as course background, not direct physical evidence.
- [ ] **C13 — Signal Processing, Filtering & State Estimation:** signals/noise, observers, EKF/UKF, RTS smoothing.
- [ ] **C14 — Input & Experiment Design:** forcing profiles, informative excitation, observability and experiment planning.
- [ ] **C15 — Control & Performance Optimization:** open-loop/feedback/MPC, periodic optimization, product-yield objectives; PDC SISO PID, feedforward, dead-time and IMC modules as supporting course concepts (MIMO/optimization course modules not evidenced by archived notebooks).

**C-stage exit criterion:** all fifteen classified as accepted/revised/split/rejected with resulting names explicitly documented; missing broad themes checked against the *proposal*, experiments and S&C scope. Do not simply tick unchanged suggestions by default.

### D. Level 3 — position subjects, letters and cross-cutting links

- [ ] **P1 — Survey all A–M dossiers** from [the research index](../../presentation/RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md); distinguish AI documents, partially owner-reviewed modules, deferred dives, and proposals. Do not infer human scientific maturity from document existence.
- [ ] **P2 — Place A–M as subject anchors only where appropriate**, with cross-links rather than duplicating source claims. A/B/M are project-wide; D/F/K cross disciplines. A letter is not required to be the *only* Level-3 child; include non-letter subjects such as filtering and experiments.
- [ ] **P3 — Owner review of canonical parent/aliases:** record stable IDs, canonical node home and secondary references. Resolve overlaps before editing a live graph.

### E. Per-letter conceptual checkpoints — 39 baseline tasks, unlimited actual depth

**One letter at a time.** The task labels **L4 / L5 / L6 are three *review passes beneath each letter***, NOT a promise that the letter is graph Level 3 or that review terminates at graph Level 6. Pass 1 = coherent major subtopics; pass 2 = explanatory mechanisms/methods; pass 3 = precise claims, mathematical statements, model assumptions, tests and/or detailed open questions. Each pass can create multiple nodes and additional intermediary/deeper branches. **No maximum graph depth exists: levels 7, 8, 9+ are supported in the knowledge contract, and further review passes can be added freely.** A depth box is checked only after its proposed content is discussed and the owner accepts that structural/content selection; record any unresolved science without promoting it to human-worked-out. The *actual app incorporation* is tracked separately under R3/R4.

#### D — Kinetic models and parameter identification (suggested first)
- [ ] **D4:** propose subtopic branches for rate-law alternatives, parameter provenance and identifiability.
- [ ] **D5:** expand fitted vs fixed parameters, correlations, parameter transfer, observation/excitation.
- [ ] **D6:** attach explicit parameter-group algebra, examples, sensitivity questions, caveats, verifiable source locators.
#### B — Literature and provenance
- [ ] **B4:** sources by research question and origin of modelling decisions.
- [ ] **B5:** source → physical assumption → code/notebook mapping, conflicting literature.
- [ ] **B6:** exact paper/page/equation pointers, unverified claims and intellectual provenance corrections.
#### C — Reaction mechanism
- [ ] **C4:** elementary steps, reaction network, competing product pathways.
- [ ] **C5:** adsorption/desorption, site balance, coverages, intermediate states and PSSA.
- [ ] **C6:** model-specific equations, retained/omitted steps, site/catalyst applicability checks.
#### I — New reacting-model track
- [ ] **I4:** separate `pbr` kinetic-package concepts from newer reacting-reactor code.
- [ ] **I5:** expand actual source law, model closures, dependencies, configuration and experiments.
- [ ] **I6:** map executable evidence, known dependencies, tests, and precise limitations—not unverified reacting/yield claims.
#### E — Physical regimes and conditions
- [ ] **E4:** operating points, catalyst/feed, bed geometry and transport regimes.
- [ ] **E5:** scale analysis, timescale comparisons, external vs internal transport criteria.
- [ ] **E6:** source-specific values/units, calculations, uncertainty, disputed assumptions.
#### F — Physical balances and state space
- [ ] **F4:** bulk gas, pellet pore gas, and surface coverage balances.
- [ ] **F5:** source/sink coupling, conservation, boundary conditions and stored-state choices.
- [ ] **F6:** exact governing equations, units, closure defects and conservation tests.
#### G — Numerical schemes and stiffness
- [ ] **G4:** spatial schemes, integration schemes, stiffness and computational architecture.
- [ ] **G5:** MOL, upwind/diffusion, implicit/explicit options, Jacobian structure.
- [ ] **G6:** consistency/convergence, periodic amplitude/phase attenuation, benchmark receipts.
#### H — Original-model track
- [ ] **H4:** scope, physical intent and numerical structure of the older model.
- [ ] **H5:** state allocation, surface equations, spatial discretization and solver wiring.
- [ ] **H6:** code anchors, limitations, reproduced defects and *what is not validated*.
#### J — Verification and corrections
- [ ] **J4:** separate numerical verification, physical consistency and experimental validation.
- [ ] **J5:** test matrix: conservation, source law, parameter units, convergence, reproducibility.
- [ ] **J6:** concrete receipts, retracted claims, unresolved tests and falsifiable pass criteria.
#### K — Results and their validity
- [ ] **K4:** separate computed outputs, sensitivity studies, periodic forcing tests and incomplete work.
- [ ] **K5:** distinguish reacting vs transport-only figures, baseline and model assumptions.
- [ ] **K6:** plot/evidence pointers, numerical uncertainty and bounded scientific claims; **K only partly discussed**.
#### L — Periodic operation and outlook
- [ ] **L4:** periodic inputs, fitting, optimization and physical extensions.
- [ ] **L5:** frequency/amplitude choices, performance metrics, identification/control options.
- [ ] **L6:** constrained comparisons and assumptions, experiments needed; **L deep dive not yet human-reviewed**.
#### A — Scientific objectives
- [ ] **A4:** scientific question, conversion/selectivity/yield distinctions and success criteria.
- [ ] **A5:** model-versus-measurement objectives, validation and periodic-vs-steady comparison.
- [ ] **A6:** falsifiable targets and explicit *proposal vs achieved result* boundaries.
#### M — Research synthesis/presentation
- [ ] **M4:** story architecture, source provenance and why models differ.
- [ ] **M5:** result/limitation framing, diagrams and connections to other letter branches.
- [ ] **M6:** actual claims/figure links and unresolved editorial decisions; **M AI draft not human-reviewed**.

**Suggested discussion order (revise as needed):** D → B → C → I → E → F → G → H → J → K → L → A → M. **Each letter is an entire mini-project; do not tick all three levels merely because an AI deep dive exists.**

### F. Cross-cutting completeness and scientific honesty

- [ ] **Q1 — Node quality:** approved nodes have substantial hierarchical notes, sub-notes, reason-for-inclusion, optional importance stars, source anchors, and relevant outstanding questions.
- [ ] **Q2 — Meaningful three-state colors:** only **Idea**, **AI worked out**, **Human worked out**; owner agreement with tree placement ≠ personal scientific review.
- [ ] **Q3 — Independent citation status:** **AI-attached** vs **human-verified** per specific claim/passage, never auto-promoted by AI.
- [ ] **Q4 — Science coverage:** revisit experimental data/apparatus, spectroscopic methods, signal processing/filtering, model reduction and future control even when absent from A–M.
- [ ] **Q5 — No false results:** proposal hypotheses, AI deductions, experimental measurements, code functionality, solver benchmarks and physically validated results stay separately labeled.
- [ ] **Q6 — App/source link reconciliation:** each accepted section reachable in current app or explicitly marked "draft/unintegrated", with stable IDs and no missing links.

### G. Compact-session checkpoint / handoff receipt

After every meaningful review or implementation step, **update this block** (not just the surrounding narrative):

- **As of:** 2026-10-20 (initial checklist capture).
- **Accepted Level-2 themes:** NONE CONFIRMED individually; fifteen AI proposals recorded in Section 3.
- **Accepted Level-3 placements:** NONE CONFIRMED individually.
- **C1 backend knowledge:** 28 new descendant science nodes (three Ideas, 25 AI worked out) are recorded in the draft overlay; 61 draft total, deepest graph Level 8. **No C1 scientific user-review approval or citation verification.**
- **Approved per-letter L4/L5/L6 branches:** NONE CONFIRMED in this checklist; AI deep dives exist independently.
- **Current app/data update integrated:** real `Academics/BEP/Catalysis/mindmap/` code; **4 canonical nodes unchanged**, older 15 AI-draft nodes preserved, **15 Level-2 ideas + 1 PDC support node + 2 C1 children** in `data/bep_draft_overlay.yaml` (**33 draft records total**), 11 older draft nodes reparented as proposals. **Nothing promoted**, no owner-reviewed science claimed. On merge, reflect these as *AI draft overlay*, not approved tree. Local WIP/runtime/tests unverified. See [node contract](bep_mindmap_node_contract_2026_10_20.md).
- **Most recent checkpoint completed:** documentation checklist and portable node contract. **Draft-only actual YAML update**: 15 idea themes C1–C15, one PDC course-support node, 11 legacy draft reparents. Structure checked for duplicate IDs/parent references/cycles, but **runtime tests not executed**. None of the Level-2 owner-review boxes C1–C15 are checked.
- **Next exact conversational action:** review **C1 Physics / Catalytic Chemistry**, followed by C2–C5; the themes are now visible as *draft idea nodes* in the map but **NOT user-approved**. Update titles, parents, scientific statuses and citation reviews only on specific user instructions. Then Mathematics and S&C; Level 3 and A–M deeper work follow review.
- **Open blocker for implementation lane:** inspect local/unpushed WIP and run Python/browser tests non-destructively; GitHub code/data directory identified. **Do not invoke old Promote button** until five-tier vs three-state maturity, citation review fields and implicit `promote_node(new_tier=2)` are corrected. Preserve existing IDs and notes.
- **Evidence rule:** each checked box needs a dated [USER DECISION], exact citation/commit or short linked verification receipt; never infer "done" from a checkbox in some other tracker.

---

## 1. Purpose and organizing principle

The map is a **scientific knowledge/ownership map of the entire BEP territory**, not a presentation outline, task dashboard, completed-work inventory or direct mirror of the A–M research modules. It should include **unexplored but relevant** domains alongside completed work: experiments, apparatus, measurements, reaction science, transport, dynamics, estimation, filtering, numerical analysis, inverse problems, control and optimization.

The scientific project concerns **dynamic acetylene semi-hydrogenation in a catalytic packed-bed reactor**, not methanol chemistry; the separate `AsapLoso/Methanol-Catalysis` repository is a local Pixi/MyST workflow reference, despite its historical name.

The conversational process comes first: AI suggests concept names, branch positioning, precise subquestions and source references; user accepts, corrects or rejects them. Only explicit authorized edits modify the future graph. Discussions and proposals do **not** imply scientific verification.

This taxonomy is **separate** from the paper-extraction knowledge graph under `Articles/graph/` and from the Wayfinder (which organizes **decisions**). Existing A–M dossiers stay intact and linked.

## 2. Level numbering, depth and branching

| Level | Role | Example |
| --- | --- | --- |
| **0** | One project root | BEP — Dynamic Catalytic Reactor Modelling |
| **1** | **Exactly three scientific disciplines** | Physics; Mathematics; Systems & Control |
| **2** | **Broad scientific themes** (15 candidates below) | Systems & Control → System Identification |
| **3** | Specific subject / A–M module **when it fits** | D — Kinetic Models & Parameter Identification |
| **4** | First layer **below a letter**; substantive subtopic | Parameter Identifiability |
| **5** | Second layer **below a letter**; more specific concept | Parameter Correlations |
| **6** | Third layer **below a letter**; an equation/observation/assumption | Combined `K2 K5` factor in the `r2/r1` rate ratio |

Six edges from root to Level 6 are normal; **not a ceiling**. Not all paths have to reach Level 6, and a subject may have one extra intermediary layer before its letter. The user emphasized *two to three nested layers BELOW the letter*, **not** a global maximum of three layers. Each sub-note is a **real expandable node** with its own full notes and citations, not merely a paragraph on the parent. Branching is allowed but keep Levels 0–2 comprehensible.

**Root/level-1 decisions:** Exactly Physics (includes chemistry), Mathematics and Systems & Control. Main edges are directional parent → child; single canonical parent per V1 node. Cross-disciplinary connections should later be links/references, **not duplicated scientific claims**. Whether one letter should have multiple visible references or a single canonical home remains an **open UI/design decision**.

## 3. Level-2 working backbone — 15 proposed themes

The following is the full **AI-suggested second layer** after reviewing the proposal, not a mechanically imported schema. Preserve the exact theme names as the **current discussion baseline**, freely revisable by the user.

### Physics

1. **Catalytic Chemistry** — reaction networks, catalysts, adsorption, ethylene selectivity and competing pathways.
2. **Reaction Kinetics & Surface Dynamics** — rate laws, kinetic constants, occupied/vacant sites, transient adsorption/desorption and dynamic/PSSA closures.
3. **Transport Phenomena** — advection, axial dispersion, intraparticle diffusion, external mass transfer and dimensional scaling.
4. **Reactor Physics & Thermodynamics** — geometry, pressure/feed, thermal effects, operating regimes, physical timescales and simplifying assumptions.
5. **Experiments & Measurements** — laboratory reactors, catalysts, experimental protocol, GC/outlet measurements, spectroscopy, MFCs, instrument response, uncertainty and physical validation.

### Mathematics

6. **Mathematical Modelling** — coupled PDE/ODE/DAE formulation, conservation equations, geometry, state variables, initial and boundary conditions.
7. **Numerical Analysis & Simulation** — spatial discretization, Method of Lines, upwind/central/FE schemes, stiffness, integration, Jacobians, solver correctness and error/convergence verification.
8. **Dynamical Systems & Stability** — equilibria, eigenvalues, local stability, linearization, transient dynamics, periodic solutions/trajectories.
9. **Inverse Problems & Uncertainty** — identifiability and ill-posedness, parameter recovery, statistical uncertainty, sensitivity, and regularization.
10. **Optimization Theory** — objectives, constraints, waveform parametrization, optimization algorithms, local/global optimality, numerical conditioning.

### Systems & Control

11. **System Modelling & Reduction** — state-space descriptions, control-oriented/grey-box models, reduced-order representations and model–plant mismatch.
12. **System Identification** — input/output modeling, kinetic parameter estimation, structural/practical identifiability, model fitting and excitation for inference.
13. **Signal Processing, Filtering & State Estimation** — measured signals, noise, online causal filters (e.g. EKF/UKF), offline smoothing/RTS, observers, hidden surface states.
14. **Input & Experiment Design** — excitation waveforms, pulse periods, information content, observability, persistent excitation and experiment planning.
15. **Control & Performance Optimization** — open-loop forcing/trajectory optimization, selectivity/yield objectives, feedback, MPC and scope boundaries.

### Related themes and overlap rules

- **Filtering is not optional simply because A–M underrepresents it.** Give it a visible Systems & Control branch with mathematical foundations linked from Mathematics where helpful.
- **Experiments are not optional simply because the existing conversations have been model-heavy.** Put the real apparatus, evidence generation, sensors, GC and spectroscopy under Physics; the *design of informative experimental inputs* belongs under S&C, with links.
- **Inverse problems (Mathematics)** versus **system identification (S&C)**: distinguish mathematical properties of recovering parameters from the engineering task of learning a model from input/output data.
- **Optimization (Mathematics)** versus **control optimization (S&C)**: mathematical algorithms/theory versus plant objectives and control architecture.
- **Dynamical stability (Mathematics)** versus **surface dynamics (Physics)**: mathematical phase-space properties versus the kinetic mechanism.
- **Literature provenance, scientific objectives, reporting/presentation** span domains. Do **not** force them under S&C merely to place a letter; they may be project-level annotations or cross-links while the scientific root retains exactly three arms.
- A proposal's plan, a user's research hypothesis, implemented code, measurements and verified experimental results are different evidence classes. A map location does **not** mean work is done, model is validated, or scope is committed.

## 4. The A–M modules belong INSIDE this wider taxonomy

The older A–M research/presentation modules are useful **anchors** or linked dossiers, but are **not a complete subject taxonomy** and must not dictate Level-2 names. Map down to a letter, then **two or three levels of genuine sub-notes beneath it**. The exact placements are suggestions subject to review.

| Letter | Existing dossier subject | Candidate home or cross-reference |
| --- | --- | --- |
| **A** | Scientific objective and success criterion | Cross-cutting project-purpose link; S&C → Control & Performance Optimization for objective formulation |
| **B** | Literature and origin of decisions | Cross-cutting provenance links across branches, no artificial single disciplinary claim |
| **C** | Reaction mechanism and surface physics | Physics → Catalytic Chemistry / Reaction Kinetics & Surface Dynamics |
| **D** | Kinetic models and parameter identification | S&C → System Identification, linked to Physics → Reaction Kinetics and Math → Inverse Problems |
| **E** | Reactor operating regime, catalyst/feed, transport | Physics → Reactor Physics & Thermodynamics / Transport Phenomena |
| **F** | Gas/pellet/surface balances and state architecture | Physics → Transport Phenomena; linked to Mathematics → Mathematical Modelling |
| **G** | Numerical schemes, stiffness and computational methods | Mathematics → Numerical Analysis & Simulation |
| **H** | Original transient model | Mathematics → Mathematical Modelling; cross-link to physical closure and implementation |
| **I** | New reacting model | Mathematics → Mathematical Modelling / Numerical Analysis; cross-link to kinetics |
| **J** | Verification, bugs and corrections | Mathematics → Numerical Analysis & Simulation; linked to experimental model validation |
| **K** | Results, sensitivities and validity | Math → Numerical Analysis / Inverse Problems; scientific results are cross-disciplinary |
| **L** | Periodic operation, identification and optimization | S&C → Input & Experiment Design / Control & Performance Optimization |
| **M** | Scientific narrative and presentation synthesis | Cross-cutting report/presentation navigation, not automatically S&C |

**Review flags retained from existing A–M dossiers:** B–G and L/M have individual AI-produced deep dives; K has a **partially discussed** results-validity record; I's full technical deep dive was deferred; A/H/J lacked separate completed dives in the reviewed index. **L and M were not evaluated with the user** as of the referenced record. Written AI material is not a human-verified understanding tier; avoid auto-promoting any letter.

### Deep example: six edges / three below-letter layers

```text
0  BEP — Catalysis
1  └─ Systems & Control
2     └─ System Identification
3        └─ D — Kinetic Models & Parameter Identification
4           └─ Parameter Identifiability
5              └─ Parameter Correlations
6                 └─ Combined K2 K5 in the r2/r1 relation
```

The last item is a **candidate, narrowly scoped algebraic insight** already discussed in D's working dossier, not a new experimental finding or a human-approved graph item. Another branch of D could be **Dynamic Excitation → Sensitivity → Parameter Recovery**, explicitly as a *hypothesis/question* until supported.

### Illustrative deeper paths (proposed, not populated)

- Physics → Catalytic Chemistry → C → Reaction Pathways → Competing Hydrogenation → Ethylene/Ethane Selectivity.
- Physics → Transport Phenomena → E → Internal Mass Transport → Pellet Diffusion Timescales → Screening Assumptions.
- Mathematics → Numerical Analysis → G → Spatial Discretization → First-Order Upwind → Numerical Damping of Periodic Input.
- S&C → Signal Processing, Filtering & State Estimation → Nonlinear State Estimation → EKF → Hidden-Coverage Reconstruction (scope idea, not an implemented claim).
- Physics → Experiments & Measurements → Experimental Reactor → Gas Chromatography → Calibration/Measurement Errors (idea, not automatically a completed procedure).

## 5. Node metadata, notes and source verification

**Single node maturity color:**
- **Grey / Idea:** proposed, unworked, unknown or incomplete.
- **Amber / AI worked out:** AI has supplied substantial interpretation/research, **human scientific review outstanding**.
- **Blue / Human worked out:** only when user has personally reasoned through or specifically affirmed the actual content; approving placement or asking to persist a draft does **not** automatically qualify.

The previous Oct 19 suggestion of five stages (including separate informal/formal written tiers) is **superseded for this working taxonomy** by the user's three categories. Textual notes can record whether material is drafted/published instead of demanding extra colors.

**Citation status is independent of node maturity** and has two visible colors/icons:
- **AI-attached/source suggested**: AI identified or checked/linked the paper, code, experiment or reference, but **human has not verified its support for the claim**.
- **Human-verified**: user has explicitly inspected the relevant claim/passage/experiment and affirmed the support. Never infer this merely because a citation exists, a model read the paper, or a node was moved to Blue.

Optional/candidate data per node: stable opaque ID independent of title/path; parent, title, extensive free-form notes, concise description, **sub-note child nodes** of arbitrary depth, 0–3 **importance stars**, rationale for inclusion relative to parent, linked sources (title, DOI/URL/repo path, locator/page/section, source-verification status, scoped claim), unresolved questions, links to equations/implementations, and potential cross-references. Parent blocks are readable at a glance; rich information appears on click. **Stars are not source quality or scientific validation.** Unknown values remain unknown. Every sub-node can have its own substantive notes and citations.

## 6. Preview and editing architecture — retrofit existing WIP; status to verify

- Human + AI **brainstorm** the graph collaboratively. User issues specific editing instruction or approval. AI routes only those approved changes through local deterministic Python/MCP. No autonomous source extraction/branch inflation, no implicit human tier promotion.
- Persist one human-readable, git-versioned YAML graph rather than an unnecessary database or giant JSON dump. Optional local stdio MCP operations: inspect/search/add/rename/reparent/delete/set maturity/set importance/set notes/attach source, with target validation, no orphan parents, no cycles and atomic writes.
- Read-only interactive browser tree: **zoom with wheel, click-and-drag pan, expand/collapse, automatic directed layout, click for full notes and source list, fit to view**. A file-save updates an already-open preview automatically.
- Local developer command **`pixi run preview` from mind-map folder**. `AsapLoso/Methanol-Catalysis` already uses `preview = "myst start"`; borrow the *experience* and inspect the watcher, but MyST is not required for this different visualization.
- App/file locations, graph library and local ChatGPT bridge are **not yet settled**; do not make guesses about built or deployed features.
- **Do not create a second mock or parallel app.** Identify the currently in-progress program and retrofit it with this schema, interaction, source statuses and taxonomy; then test it using terminal/browser in that actual worktree. If current source is local-only or inaccessible, keep the technical state explicitly **UNVERIFIED**, not 'not implemented'. Avoid a heavyweight multi-agent harness for a narrow retrofit.
- `Wayfinder` planning is optional for any genuinely outstanding implementation decisions; it is **not this scientific knowledge map**. Repo Wayfinder records decision tickets, not the generated application.

## 7. Conversation-first work plan — current frontier

### Phase A — Agree Levels 0–2 first (CURRENT)

1. Keep the fixed three disciplines (Level 1).
2. Review the proposed **15 themes at Level 2**: missing science, overlaps, naming, where experiments and filtering go. **Do not descend into A–M yet.**
3. Record each user-accepted/changed theme and the rationale. A suggestion remains an Idea until accepted as a *structural change*; acceptance of names still does not certify its scientific notes.
4. Keep the second layer broad and manageable; breadth here is intentional because the map covers the whole science, not only the work performed.

### Phase B — Place Level 3 subjects and A–M anchors

1. Discuss Level-3 subjects within the newly approved Level-2 taxonomy.
2. Attach each A–M module where conceptually meaningful. Allow cross-references and mark incomplete/deferred modules explicitly.
3. Decide how to present cross-disciplinary B/M/A and shared D/F/K without copying research claims or forcing artificial ownership.

### Phase C — Per-letter deep dives, Levels 4–6+

1. Return to the earlier **proposed** deep-dive sequence **D → B → C → I**, then E/F/G/H/J/K/L/A/M; this order is **not a fixed user deadline** and may change based on the Level-2 review.
2. For one letter at a time, propose 2–3 levels of expandable conceptual nodes; each has extensive notes, rationale, stars, linked sources and outstanding questions.
3. Present AI-supported findings as **AI worked out** and speculative leaves as **Idea**; discuss with user, adopt only their explicit corrections/affirmations. Source verification tracked at the **citation**, independent of nodes.

### Phase D — Retrofit existing implementation with accepted graph, then verify

1. Only after specific explicit owner approval, write approved branches into the actual YAML through local editor/MCP; do not confuse this working *document* with a live graph.
2. **Inspect/retrofit the existing WIP**, preserving current source code, graph data, stable IDs and working features. Avoid generating a new mock; test preview/editor in the real implementation once accessible.
3. Validate changes with automated tests and browser preview; test invalid edits and no-unapproved-changes invariant. Preserve git history and source references.

### Phase E — Reconcile coverage

Check for gaps vs the proposal, experiments and the original A–M dossiers. Flag unreviewed/unimplemented/unsupported leaves; do not conflate a proposal target with a achieved result. Iterate without a hard node-count/depth quota.

## 8. Current decisions, proposals and open questions

**[USER DECISION]** Exactly three first arms; physical sciences include chemistry; broad complete BEP knowledge scope beyond existing outputs; plenty of sub-notes under each letter (two or three additional levels initially, **without any depth ceiling**); **C1 two major child branches (Reaction Chemistry & Pathways; Catalyst Chemistry & Active Sites)**; extensive per-node notes; zoom/pan viewer; AI controlled edits only by owner instruction; two independent citation statuses; three node-ownership states; persist discussion/planning in GitHub.

**[AI PROPOSAL — NOT APPROVED GRAPH]** Fifteen Level-2 themes; the names/number of subjects; home/cross-links for A–M letters; examples of deeper leaves; fixed 0–3 star scale and UI choices; proposed implementation path; illustrative diagram.

**[OPEN]** Exact Level-2 acceptance/renaming/merging; whether to distinguish observational/experimental science more finely; where cross-cutting literature/objective/narrative links live; single vs referenced A–M modules; exact initial graph location; final UI and MCP interface; actual literature/citation human verification.

**[UNVERIFIED IN THIS DOCUMENT]** Actual live map implementation, local MCP, preview and current unpushed work; the user reports an in-progress implementation. **[NOT COMPLETED HERE]** Full taxonomy owner review, human verification of scientific claims, physical validation and integration check of the WIP. Documentation PR #84 was merged into `devcontainer` on 20 October 2026.

## 9. Re-entry instructions

1. **Start at the checkbox section at the very top of this file, including the handoff receipt (Section G).** It is the canonical actionable tracker; do not use the short phases below it as a substitute. Read the rest of this taxonomy note selectively for Level-2 proposals, statuses, depth conventions and remaining decisions.
2. Read [the portable node record and transaction contract](bep_mindmap_node_contract_2026_10_20.md) before writing ANY proposed node/record; it documents actual existing app/YAML, PDC and migration traps. Then read [the implementation spec](bep_ai_mindmap_spec_2026_10_19.md) for mechanics; note that the **three-tier ownership/color convention in this document supersedes the older five-tier proposal**.
3. Read primary [project proposal](../../0_Project_Management/main.tex) as **intent/proposed methods**, not proof of completed work; compare against [BEP state](../../state.md) for current reality.
4. Consult [A–M index](../../presentation/RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) only once placing Level 3 or exploring individual letters.
5. **Next conversational action**: inspect the fifteen themes **one discipline at a time**, starting with Physics, without automatically modifying the actual map. Ask for specific changes and record accepted structures, preserving unresolved items.
