# Owner-led BEP science map — corrective handoff for parallel/new chat

**Corrective checkpoint:** Friday 23 October 2026 afternoon (Amsterdam), written after explicit owner objections to over-generating nodes and pages. **Canonical branch:** `docs/bep-theme-first-progress-units-20261022`; **canonical current status:** always fetch `owner_working_map/current_map.yaml` on latest branch HEAD, not a dated count/banner. In the checked correction transaction, the map went from **57 nodes to 50** by targeted withdrawal of seven over-eager PDE/Model placements. **All 50 remaining IDs have maintained approval-index entries.** Other catalyst/surface science worker's additions were preserved.

## Read first: authority

1. `.agents/skills/bep-map-edit-review/SKILL.md` **§H** (strict owner preview gate + no AI `index.md`), and `.agents/skills/reversible-change-review/SKILL.md`.
2. Live `current_map.yaml` and `dataset.approved_personal_nodes`; compare latest commit/blob SHA before/after each scoped write. Check `bridges.yaml` and `ACTION_QUEUE_2026_10_22.md`, especially **Q86–Q95**. Prior Q57–Q68 and past runbook/SESSION_STATE banners are historical; they described placements since corrected.
3. Pinned integrated AI reference `work/bep-integrated-reference-map-v1-20261022` for source research, and existing GitHub local files. Owner **explicitly does not want new online theory searching now**. Exact 2008 Berger source study is queued for later; don't treat a dossier or prior AI excerpt as paper-level verified.
4. AI-only notes under `pages/.../AI_REFERENCE.md` and `bridges/REVIEW_REQUIRED_PDE_MODEL_PROPOSALS_2026_10_23.md`. These are **not** user writing, **not** default reader material and **not** their scientific knowledge stages.

## Extremely important user correction

- **No personal node—not even Idea—without that exact proposed node having been shown to the owner once, with immediate parent, siblings, short summary and stage, and accepted.** Do not interpret "yeah, work out the hierarchy" as approval of a dozen invisible children. One clear owner-directed node may be edited without redundant reconfirmation, but don't create its adjacent nodes.
- **The owner's spoken/revised explanation comes first**. A tiny personal `summary` and limited `notes` may paraphrase their understanding. Extensive AI deductions, equation details, PDFs and provenance live in separate `AI_REFERENCE.md` (or clear AI named note) and `background_files`. **Use `index.md` only for Informal Writing or Formal Writing after the owner approves the actual prose**; neither AI worked out nor Human worked out automatically means they have written a document for Damian.
- **A, B, C corrected stages** (exact meanings):
  - **A** — wall-temperature BC vs interior: `own_ph_wall_temperature_boundary` **Idea**. Fixing T at wall r=R doesn't alone set interior T. Not claimed Human. Mathematical formula child `own_ph_wall_dirichlet_equation` is an **Idea**: `T(R,z,t)=T_w(z,t)`; owner saw and tentatively accepted formula but placement/scope could use discussion.
  - **B** — neglecting resolved radial temperature variation while retaining axial z: `own_ph_radial_temperature_reduction` **AI worked out**. Owner understands the axes, but not the full averaging/validity derivation. Idea child `own_ph_radial_temperature_average_equation` represents \(\bar T(z,t)=2/R^2\int_0^R T(r,z,t)r\,dr\) (the user recognized meaning). Not Human yet.
  - **C** — uniformly prescribed fixed T for the modeled reactor: `own_ph_isothermal_theory` **Human worked out ONLY for that simple physical special case**. It is stronger than radial averaging (B) because axial/time variation must also be removed or fixed. Wall Dirichlet (A) does not imply C. Deep thermal PDE derivations and detailed claims remain AI-only.
- **Hierarchy caution:** A and B were previously placed as children of C. This is **visually/semantically confusing** because an imposed wall temperature is not a deduction or direct child of globally isothermal physics, and B is a more general dimensional approximation. **Do not silently reparent**; show owner a single local proposed correction with sibling layout first. They did not approve a replacement arrangement in this turn.
- **Owner does NOT want a wholesale Git revert.** Targeted correction already made without touching unrelated catalyst work. Seven unreviewed placements were moved from the personal map to structured AI archive/queue; historical Git commits remain.

## Relevant local tree as actually placed at checkpoint

```text
BEP                                      Tier 0
└── Physics                              Tier 1
    ├── Reaction Chemistry & Pathways    Tier 2 · Idea
    │   └── Our Reactions                Tier 3 · Informal Writing
    │       └── ... existing pathways / adsorption / active chemistry
    └── Thermodynamics & Thermal Dynamics Tier 2 · Idea
        └── Isothermal approximation — physical theory Tier 3 · Human worked out [C, only fixed-T core]
            ├── Prescribed Wall Temperature — Boundary vs Interior Tier 4 · Idea [A]
            │   └── Wall Dirichlet Mathematical Form           Tier 5 · Idea [equation]
            └── Neglecting Radial Temperature Variation        Tier 4 · AI worked out [B]
                └── Radial Average / 1D Reduction Formula      Tier 5 · Idea [equation]

BEP → Mathematics Tier 1
└── Mathematical Modeling                 Tier 2 · Idea [existing owner/other worker]
    └── Surface Kinetic Equations          Tier 3 · Idea [existing other worker, plus its separately authored children]
    [Proposed Reactor Model subtree withdrawn, review required]
```

The tree is **a current inventory, not endorsement of the A/B child-parent topology**. On every future reply, show parent and immediate siblings, then the direct children relevant to the discussion; don't dump the whole 50-node map unless explicitly asked.

## Seven previously overapproved placements now archive/queue ONLY

Preserved exact original records as JSON in `bridges/REVIEW_REQUIRED_PDE_MODEL_PROPOSALS_2026_10_23.md`. Source material still in former page directories under `AI_REFERENCE.md`, so no science is lost. Each needs individual exact owner preview/reacceptance before reinsertion:

- Former Thermodynamics Tier3 `Energy Balance — Thermal Conservation Theory`: owner says "never heard of it", so **explain first**, then perhaps propose a short Idea. AI reference `ph_energy_balance` is not personal knowledge.
- Former Chemistry Tier3 `Reaction Heat Generation — Enthalpy × Reaction Rate`: title rejected; exact placement open, maybe nearer/parallel to *Our Reactions*, not one node per reaction by default. Physics/kinetic formula remains AI bridge.
- Former Math subtree `Reactor Model → Model Assumptions & Approximations → Isothermal / One-Dimensional Axial / Axial Dispersion (Plug-Flow Limit)`: owner recognizes the concepts but wanted to **refresh one at a time before adding**. Mathematical Modeling existing parent remains. None of five model nodes are live now. Retain proposals and crosslinks in queue.
- No new Transport Phenomena parent; axial dispersion and its BC requirements remain AI bridges.

## Untouched and preserved mathematical/scientific bridges (NOT live topics unless separately placed)

- `B-M1` axial/time spatiotemporal structure; `B-M2` autonomy, forced state dependence; `B-M3` method of lines, spatial/temporal integration and stiffness.
- `B-MODEL-BC-01` PDE boundary requirements: finite axial species dispersion vs ideal advective inflow, Danckwerts/Robin, outlet/initial conditions. The source PDE/BC ambiguities are in `bridges/BERGER2008_EQ1_BEP_LOCAL_PROVENANCE_2026_10_23.md`.
- `B-TP-REDUCTIONS-01` future Transport Phenomena mass/radial averaging; `B-HEAT-LENSES-01` now review-required, separate enthalpy/reaction-rate versus energy conservation and a possible model equation.
- `B-LH-ARR-01` and `B-P3` contain other real related reference material, but the catalyst worker is independently handling site/adsorption/encounter topics.
- Turbulence/zero-gradient physical arguments remain OUT-OF-SCOPE hypotheses, not verified effects or user-approved nodes.

## Files renamed rather than AI-written indexes

Prior PDE-session auto-created `index.md` pages for Tier2/3 and withdrawn concepts were preserved as `AI_REFERENCE.md` and removed as `index.md`: thermodynamics parent, isothermal theory, wall boundary, radial reduction, energy balance concept, reaction heat, Reactor Model and Approximations. Live retained nodes point to the relevant `AI_REFERENCE.md` through hidden `background_files`. Only owner-approved real prose is allowed in future `index.md`. This convention is in the map-edit skill §H. **Do not claim TeX equations render in GitHub Markdown**; references are for research, not a polished reader.

## Cold-start work assignment

**Start by explaining the tiny actual local subtree above, acknowledging the awkward parent/child relation**, and ask the owner which ONE node to work through or which exact reparenting they want to preview. Candidate first discussion: decide whether A, B and C should be siblings under Thermodynamics or whether a more meaningful theory umbrella is needed. Do not alter anything else before that decision.

Review queue Q86–Q95 afterwards and use short live `summary` in personal graph; keep discussion, candidate positions, mathematical derivations and all unapproved nodes in the queue/reference. When the owner actually dictates a personal explanation, keep their version, only lightly polish with their permission; promote to Informal Writing only when the exact prose is approved.

## Parallel-writer / CAS rules

- Another agent may advance the source map from 50 at any time; refetch map blob SHA and compare current structure for every write. No blind updates, force pushes, default merge of experimental branches or whole file overwrite from an outdated snapshot. This handoff's count is a timestamped checkpoint only.
- Preserve the existing catalyst/surface/H₂/kinetic Math branches authored in the other chat; no reparenting or status changes to their nodes.
- New Idea nodes require the SAME preview and permission as Human. If no owner approval, draft at a separate bridge/queue path and report it unplaced.
- Each approved change: minimally patch its exact node, decision receipts and approval index in a single logical GitHub transaction; read back and verify other IDs/maturity/citations unchanged.
- Handoff updates and old banners are supporting historical records, not the canonical graph.
