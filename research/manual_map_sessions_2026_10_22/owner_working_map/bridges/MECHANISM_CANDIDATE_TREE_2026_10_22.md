> **NEWEST STRUCTURE SUPERSEDES CANDIDATE DRAWING — 2026-10-23:** User has approved and placed a **separate Tier5 Surface Reaction Encounter Mechanisms** grouping under Tier4 Microscopic Reaction Pathways, with Tier6 **Langmuir–Hinshelwood** and **Eley–Rideal-type** Ideas. Original mechanism family Route A is now **Informal Writing** (brief owner text), Route B Human worked out (qualitative). The previous Q14 'unplaced candidate' wording throughout this historical tree is obsolete; B-ER-01 is placed. The LH–Arrhenius bridge B-LH-ARR-01 and future Modeling hierarchy are undecided. Refer to `current_map.yaml`; do NOT treat historical diagrams as latest graph. The detailed 2024 review is a **queued AI reading** and not an approved personal node or citation verification.

> **2026-10-23 OWNER APPROVAL UPDATE (newest):** The Tier6 Route B `own_ph_vinyl_ethylidene_route` is **Human worked out** for the qualitative difference from Route A; the former *Idea* in the older checkpoint below is historical. Actual published structure drawings and viewer legibility remain open (Q40). Tier5 family is still Idea, Tier6 Route A Human worked out for successive H addition, Q14 unplaced; citations remain AI-attached only. Use `current_map.yaml` for authoritative maturity.

> **CURRENT STATUS — 2026-10-23 (supersedes the historical all-queued diagram below):** Owner has accepted `Reaction Mechanism Families` Tier 5 as a **placed Idea** sibling of Adsorption under Tier 4, with **Route A: Stepwise Hydrogenation via Adsorbed Ethylene** at Tier 6 **Human worked out for successive H-addition only** and **Route B: Vinyl–Ethylidene** at Tier 6 **Idea** (owner explicitly cannot yet distinguish the structures). The new live IDs are `own_ph_reaction_mechanism_families`, `own_ph_stepwise_hydrogenation`, `own_ph_vinyl_ethylidene_route`. All further Tier-7 children in the historical proposal remain **unplaced**; **Q14 LH/ER grouping remains queued and separate**. AI-only Cao et al. (2023) Figure 2 citation/linked image at the overarching Tier5 and children, with red crosses interpreted as *undesired pathways to suppress* rather than impossible reactions. Radical conjecture kept as owner hypothesis for Damian, not verified science. This is a historical candidate-tree document, so **do not use its older diagrams as actual live placement**; read `current_map.yaml` first.

# Candidate mechanism hierarchy — concrete queue, not live map nodes

**Status:** Owner-requested, source-qualified AI *candidate* structure. **Every item below is queued**, with provisional identifiers for conversation/auditing, not approved personal node IDs. To add them, inspect current map/bridge refs and obtain owner approval for specific parent/title/stage. Parent Tier 4 already exists: `own_ph_alternative_surface_paths` / **Microscopic Reaction Pathways — AI worked out**. Its present child Tier 5 **Adsorption** already exists (`own_ph_adsorption`).

## A. Different chemical pathways through the surface

```text
Microscopic Reaction Pathways                        [Tier 4 · existing]
└── Reaction Mechanism Families                     [Tier 5 · Q13 · candidate C-MECH-FAMILY]
    ├── Stepwise hydrogenation via bound ethylene   [Tier 6 · candidate C-STEP-H]
    │   ├── Adsorbed acetylene → vinyl → ethylene*  [proposed possible Tier 7 · not placed]
    │   └── Ethylene* desorbs vs adds more hydrogen [proposed possible Tier 7 · not placed]
    └── Alternative vinyl–ethylidene route          [Tier 6 · candidate C-ETHYLIDENE]
        └── Vinyl, ethylidene and possible ethylidyne surface intermediates
                                                    [Tier 7 · Q18 · candidate C-ETHYLIDENE-INTERMEDIATES]
```

**C-MECH-FAMILY** (Tier 5): A mechanism is a series of elementary adsorption, surface transformations and desorption steps, which can all lead to the same net R3 stoichiometry. This grouping would be a *sibling* of Adsorption under Tier 4, not a child of Adsorption.

**C-STEP-H** (Tier 6): Supported Pd/α-Al₂O₃ model from [Urmès et al. 2019, Table 3](https://doi.org/10.3390/catal9020180). Its species sequence is `C₂H₂* → C₂H₃* → C₂H₄* → C₂H₅* → C₂H₆(g)`, with **ethylene desorption** branching at `C₂H₄*`. Only one catalytic model, not a BEP PdAg assignment. Existing `B-ALT-01`, `B-ALT-02`, `ph_sequential_path`, `c1_horiuti_polanyi_family` apply.

**C-ETHYLIDENE** (Tier 6): Model-surface Pd/Pd–Ag KMC studies in [Mei, Neurock & Smith 2009](https://doi.org/10.1016/j.jcat.2009.09.004) discuss branching via **vinyl → ethylidene → ethane**, potentially competing with ethylene formation. Original full text not yet checked. Existing `B-R3`, `c1_vinyl_ethylidene_alternative` (pinned Idea) apply. Do **not** call ethylidene the same as ethylene, or declare a third fitted rate based only on the existence of this candidate route.

**C-ETHYLIDENE-INTERMEDIATES** (Tier 7 only if useful): The owner wants different chemical intermediates assigned to the **alternative** pathway, not lumped into the stepwise hydrogenation chain. Vinyl, ethylidene and ethylidyne may have different roles; the presence of the latter in a model does not prove target-pellet poisoning.

## B. Different reactant-encounter mechanisms (separate axis from A)

```text
Microscopic Reaction Pathways                        [Tier 4 · existing]
└── Surface Reaction Encounter Mechanisms           [Tier 5 · Q14 · candidate C-ENCOUNTER]
    ├── Langmuir–Hinshelwood-type encounter         [Tier 6 · candidate C-LH]
    └── Eley–Rideal-type gas/surface encounter       [Tier 6 · candidate C-ER]
```

**C-ENCOUNTER** (candidate parent): A reaction-mechanism **classification**, not a competing chemical product path. It concerns whether reacting partners are both adsorbed, or one enters from the gas phase.

**C-LH**: Both partners are surface-bound before their elementary surface reaction. The [Urmès 2019, Table 3](https://doi.org/10.3390/catal9020180) supported-Pd example uses adsorbed C₂H₂ and atomic H as the hydrogenation partners. This is a **model assumption for that catalyst**, not BEP proof.

**C-ER**: One reactant in the gas encounters a surface-bound species and reacts without the gas reactant first entering a long-lived adsorbed state. Such families exist in catalysis, but **Eley–Rideal acetylene hydrogenation on the BEP catalyst has not been established**. Existing `B-ER-01` tracks this as a bridge.

**Owner choice before placement:** Should the encounter-mechanism classification be a sibling of C-MECH-FAMILY under Tier 4 (cleanest separate-axis solution), or be explored under Adsorption as an explanatory subtopic first? Neither path has yet been authorized as a placed node.

## C. Other queued children of Adsorption, and exclusions

```text
Adsorption                                           [Tier 5 · existing]
├── Hydrogen activation / neighboring surface sites [Tier 6 · Q15 · queued]
└── Competition for available surface sites          [Tier 6 · Q16 · queued]
```

These are **not** placed. Both already have AI reference entries: `c1_dissociative_h2_adsorption`, `c1_adjacent_site_requirement`, `c1_hydrocarbon_site_competition`, `ph_surface_states`. *Desorption/readsorption* already exists in the Tier4 text and bridge `B-ALT-02`, not an automatically distinct additional node.

**Catalyst saturation, reversible inhibition, poisoning, sintering, pellet agglomeration and site-loss** stay outside the main mechanism-family classification as bridged catalyst condition/evolution/transport subjects, cross-linked to adsorption. The number of **fitted rates** likewise belongs to separate future kinetics/model identification work, not a child added because R1, R2, R3 were drawn.

## Source/review contract

- Urmès et al. 2019 `10.3390/catal9020180`: AI full-text / Table 3 evidence, supported Pd on α-Al₂O₃; **not yet owner/Damian scientifically approved**.
- Mei et al. 2009 `10.1016/j.jcat.2009.09.004`: abstract/preview, model Pd/PdAg; **not full-text verified**.
- More specific catalyst suitability and competing pathway dominance must be reviewed with Damian and original primary papers.
- **No claim here confers AI worked out or Human worked out on these candidate nodes**. They are queued Ideas until individually discussed and scoped.

**Decision still needed:** Shall the first Tier-5 sibling of Adsorption be **Reaction Mechanism Families** with C-STEP-H and C-ETHYLIDENE under it? If yes, decide explicitly before touching `current_map.yaml`.
