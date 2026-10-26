# Encounter mechanisms — personal tree, pinned AI reference, queue and bridges

**Read-only comparative view (23 October 2026), not an additional personal-map node or a source of authorizations.** Built exclusively by inspecting the existing repository files. In particular, don't turn labels or arrows in this view into new `current_map.yaml` children, owner understanding, or source verification.

## 1. Personal owner map — actual parent/child positions

```text
BEP — Acetylene semi-hydrogenation                  [Tier 0 · Idea]
└─ Physics                                         [Tier 1 · Idea]
   └─ Reaction Chemistry & Pathways                [Tier 2 · Idea]
      └─ Our Reactions — Net Reaction Network      [Tier 3 · Informal Writing]
         └─ Microscopic Reaction Pathways          [Tier 4 · AI worked out]
            ├─ Adsorption                         [Tier 5 · Informal Writing]
            ├─ Reaction Mechanism Families        [Tier 5 · Idea]
            │  ├─ Stepwise Hydrogenation Route A  [Tier 6 · Informal Writing]
            │  └─ Vinyl → Ethylidene Route B       [Tier 6 · Human worked out]
            └─ Surface Reaction Encounter Mechanisms [Tier 5 · Idea]
               ├─ Langmuir–Hinshelwood (LH)       [Tier 6 · Idea, SVG stored]
               └─ Eley–Rideal-type (ER)            [Tier 6 · Idea, SVG stored]
```

The **other root children** `mathematics` and `systems_control` still have **no placed descendants** in this personal map. The above is 12 of the 14 live personal nodes (root + Physics branch); all 14 are retained. Source: [current_map.yaml](current_map.yaml). The new encounter-family reader [page with both SVGs](pages/bep/physics/reaction_chemistry_pathways/our_reactions/microscopic_reaction_pathways/surface_reaction_encounter_mechanisms/index.md) is AI-authored **supporting material**; no new human writing/understanding approval follows from including illustrations.

## 2. Independent pinned AI reference — matching subject, different topology

Pinned source graph: [`nodes.yaml` at `1cd680f`](https://github.com/AsapLoso/project-management-agents/blob/1cd680f95902a0a79b17afb084fa29ab49c6b25f/Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/nodes.yaml) (**143 AI reference nodes**). All nodes below are **AI worked out**, with their source-specific qualifications; not personally read/promoted by their existence.

```text
Physics
├─ Catalyst identity, active sites and working-surface state       u_ph_catalyst
│  └─ Surface states and site inventory                             ph_surface_states
│     ├─ Elementary Rates & Langmuir–Hinshelwood Reduction          ph_lh_rates
│     └─ Mechanism choice and catalyst specificity                   ph_mechanism_choice
└─ Kinetic law, thermal dependence and surface-memory closures     u_ph_kinetics
   ├─ Urmès 2019 effective single-site PSSA kinetics                 c2_urmes_2019_effective_rates
   └─ Larsen BEP thesis extended empirical LHHW closure             lhhw_kinetics
      └─ Centered Arrhenius parameterization                         centered_arrhenius

Mathematics
└─ Conservation and balance modeling [via u_ma_conservation]
   └─ Surface-state ODE and algebraic closure                        ma_surface_balance
```

The AI graph also has the **chemical** Horiuti–Polanyi sequence `c1_horiuti_polanyi_family`, hydrogen dissociation `c1_dissociative_h2_adsorption` and neighboring vacancy `c1_adjacent_site_requirement`, which live in different *AI* subtrees and should be cross-linked rather than force-moved into the above local comparison.

**Important asymmetry:** There is a fully authored LH-derived-rates topic in the pinned AI graph (`ph_lh_rates`); there is **no explicitly titled Eley–Rideal node or Eley–Rideal mention** in that pinned 143-node `nodes.yaml`. ER was discussed later and lives as a **personal Idea + bridge provenance**, not as a missing personally understood source. Do not pretend the AI graph has a matched ER leaf.

## 3. Crosswalk — separate axes, no automatic promotion

| Personal location | Matching pinned AI reference node(s) | Queued question or status | Bridge |
| --- | --- | --- | --- |
| Tier5 Adsorption | `ph_surface_states`, `c1_dissociative_h2_adsorption`, `c1_hydrocarbon_site_competition` | Q15 (hydrogen activation), Q16 (competition) open | B-P2 catalyst structure/kinetics candidate |
| Tier5 Reaction Mechanism Families → Routes A/B | `c1_horiuti_polanyi_family`, `c1_vinyl_ethylidene_alternative`, `ph_sequential_path` | Route structures placed; Q40 published-figure viewer check and Q41 radical hypothesis open | B-ALT-01 partially covered |
| Tier5 Encounter Mechanisms → LH | `ph_lh_rates`, `ph_mechanism_choice`, `c2_urmes_2019_effective_rates` | Q14 **completed structurally**; source/catalyst applicability still uncertain | B-ER-01 **placed** |
| Tier5 Encounter Mechanisms → ER-type | No direct ER-labelled pinned AI reference node | Optional 2024 terminology reading deferred as Q42, **not** a personal claim | B-ER-01 **placed**, source qualifiers preserved |
| LH ↔ rate/temperature modeling | `u_ph_kinetics`, `lhhw_kinetics`, `centered_arrhenius`, `ma_surface_balance` | Q21 kinetics/identifiability and modeling parent undecided | **B-LH-ARR-01 open/unplaced** |

**Meaning:** owner progress, AI scientific explanations, next questions, and structural bridges are different relationship types; showing them side by side **does not merge their datasets**.

## 4. Exactly what the pinned AI map says about LH — no new research

From `ph_lh_rates` (**AI worked out**): for an **illustrative** surface reaction with adsorbed partners, a rate may be represented as `r_s = k_s θ_A θ_H`. Under additional **quasi-equilibrium adsorption, site balance and rate-determining-step assumptions**, coverages can be eliminated to yield a pressure-dependent Langmuir–Hinshelwood-type rate. The resulting denominator and hydrogen-pressure exponent depend on the adsorption/site mechanism; these are **not** universal formulas for the BEP catalyst.

From `ph_mechanism_choice`: studies differ in one-site versus two-site supported-catalyst representations, and fit/model labels do **not automatically establish** the real microscopic mechanism of the particular BEP catalyst.

From `u_ph_kinetics`, `lhhw_kinetics`, and `centered_arrhenius`: temperature dependence enters the kinetic coefficients (and potentially adsorption parameters). An Arrhenius factor for `k(T)` does not mean the entire pressure-dependent adsorption term is temperature independent, and a choice of rate law is distinct from the physical LH encounter class.

Cross-discipline parallel: `ma_surface_balance` describes dynamic coverage ODEs versus quasi-steady algebraic closure and rate normalization. There is **no owner-approved Math/Modeling subtree yet**; keep the link to those reference nodes via **B-LH-ARR-01**.

## 5. Status and provenance

- Personal source: `current_map.yaml` on branch `docs/bep-theme-first-progress-units-20261022`, 14 nodes. Owner-facing notes stay short; reader pages can contain illustrations without implying Informal Writing.
- AI source: `reference_map.yaml` pins branch `work/bep-integrated-reference-map-v1-20261022` at `1cd680f95902a0a79b17afb084fa29ab49c6b25f` (143 nodes, 65 sources). Do not alter the pinned AI graph or confuse its parents with personal parents.
- Questions: `ACTION_QUEUE_2026_10_22.md` lists 42 actions (22 completed, 20 open at this snapshot). “Q” numbers are internal navigation labels, **not** tree node IDs.
- Bridges: `bridges.yaml` has 26 historical/current records, some already placed. `B-ER-01` is **placed**; `B-LH-ARR-01` is **open and unplaced**. “Bridge count” must not be interpreted as 26 unplaced nodes.
- No new scientific research, user-understanding promotion, new personal or AI map node, source verification, diagram generation or frontend edit was performed to create **this view**. It is a static snapshot rather than an implemented combined graph UI.
