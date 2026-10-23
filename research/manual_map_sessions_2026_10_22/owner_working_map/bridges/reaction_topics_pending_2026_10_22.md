# Reaction-science bridge register — pending placement

**Recorded:** 2026-10-22, from the owner's spoken navigation and scientific suggestions.  
**Role:** unplaced **bridge content**, not additional personal-map nodes, not owner-approved theories, and not a third investigative theme.  
**Current parent under discussion:** `physics → own_ph_reaction_chemistry_pathways → own_ph_net_hydrogenation`. The Tier-3 net-reaction Markdown is at [Our Reactions](../pages/bep/physics/reaction_chemistry_pathways/our_reactions/index.md).

## B-RXN-ADS — Surface adsorption, hydrogen activation, and desorption

**State:** placed as **Tier 5 — Adsorption (Idea; structure only)** under **Tier 4 — Microscopic Reaction Pathways (Idea)**, beneath **Tier 3 — Our Reactions**. The owner explicitly authorized these levels on 22 October 2026. Mechanistic details, site assumptions and source verification remain outside owner-approved understanding; use the existing AI [source reconnaissance](microscopic_pathways_source_recon_2026_10_22.md).

Concepts to retrieve from existing research: catalytic adsorption of acetylene/ethylene and hydrogen, possible H₂ dissociation, competition for surface sites, surface-bound intermediates, ethylene desorption and readsorption. Distinguish chemical surface residence from pellet/gas transport. The broad Adsorption subject has been placed at Tier 5, but its detailed subtopics have **not** been individually approved as child nodes.

**Existing bridges:** `B-P1-MICRO`, `B-ALT-01`, `B-ALT-02` in `../bridges.yaml`.  
**Existing AI reference pointers:** `c1_adsorption_desorption`, `c1_surface_sites`, `c1_dissociative_h2_adsorption`, `c1_hydrocarbon_site_competition`, `ph_surface_states`.  
**Evidence:** AI reference material, source-specific; no BEP-specific mechanism or human citation validation.

## B-RXN-RATE — Three mechanism families versus the number of fitted rates

**State:** Idea; **proposed placement:** undecided. The owner suggested treating three potentially distinct **reaction mechanisms** as three independent rates to fit. This is captured as a **candidate modeling hypothesis**, not settled experimental knowledge or a commitment to fit three rates.

If an independently contributing acetylene-to-ethane mechanism can be distinguished from acetylene-to-ethylene production and subsequent ethylene-to-ethane conversion, a three-rate bookkeeping model may be considered. But the number of stoichiometric equations, elementary routes, net-rate parameters and *identifiable* fitted rate laws are different counts. Because `ν₃ = ν₁ + ν₂`, species balances alone cannot uniquely determine all three rates without additional measurements or imposed kinetic structure. In a network defined on common rate basis:

```text
C₂H₂: -r1 - r3
C₂H₄: +r1 - r2
C₂H₆: +r2 + r3
H₂:   -r1 - r2 - 2r3
```

**Conditional suppression side note:** different mechanisms or effective rates may be negligible for specific catalyst, composition, partial pressure, temperature, and surface coverage regimes. No numerical regime or bound has been verified for the BEP catalyst; setting a rate approximately zero requires evidence or a declared modeling approximation.

**Existing bridge:** `B-P1-COND`, `B-R3`; related generic pathway tickets `B-R1`, `B-R2`.  
**Existing AI reference pointers:** `ph_reaction_network`, `ph_sequential_path`, `ph_mechanism_choice`, `c1_parallel_ethane_paths`, `c1_no_independent_direct_rate`, `c2_urmes_2019_net_rates`.  
**Source limits:** supported-Pd Urmès et al. (2019) uses a published two-rate closure; idealized Pd/PdAg Mei et al. (2009) discusses alternative pathways; historical Bos & Westerterp (1993) direct-route link lacks original full-text review. None establishes three separable fitted rates for BEP. The current owner direction was to **park** this content.

## Retained themes and navigation

The **two previously chosen downstream themes** are `Microscopic pathways` and `Viability & Conditions`, already available as `B-P1-MICRO` and `B-P1-COND`. This register does not add a third theme or insert R1/R2/R3 question-nodes.

**Next owner conversation:** continue dictating/editing the Tier-3 *Our Reactions* informal text, especially the meaning of a distinct R3 mechanism. Adsorption's Tier-5 location is decided; choose where any additional detailed adsorption subtopics or rate modelling belong only **after** discussing those subjects. Never assume owner reading, human understanding, verified citation, or model-specific evidence from this bridge.
