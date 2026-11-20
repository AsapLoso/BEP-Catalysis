# Microscopic Reaction Pathways — source reconnaissance

**Source-labelled visual:** [microscopic_pathways_schematic_2026_10_22.svg](microscopic_pathways_schematic_2026_10_22.svg) — a schematic separating the supported-Pd Urmès pathway from the model Pd/Pd–Ag Mei alternative; neither is shown as an experimentally validated BEP mechanism.

**Created:** 2026-10-22. **Role:** AI-worked scientific briefing for owner discussion; NOT a promotion of any personal node or verification by the owner.  
**User-approved topology:** `Our Reactions` (Tier 3, Human worked out for net stoichiometry only) → `Microscopic Reaction Pathways` (Tier 4, Idea) → `Adsorption` (Tier 5, Idea). Tier 4/5 placement approved in conversation, but scientific explanation remains unread/unreviewed.  
**Existing evidence reused:** old `bep_map.yaml` anchors, archived `B-P1-MICRO`, `B-ALT-01`, `B-ALT-02`, `B-P1-COND`, the adsorption/rates sidecar, and the pinned integrated AI reference `nodes.yaml` / `sources.yaml` on commit `1cd680f95902a0a79b17afb084fa29ab49c6b25f` (`reference_map.yaml`). No new primary-document full text or experimental target-catalyst validation is claimed.

## Conceptual picture: ONE model family, not universal experimental fact

The following schematic summarizes the **seven-step Horiuti–Polanyi-like single-site mechanism used by Urmès et al. (2019) for 0.05 wt% Pd/α-Al₂O₃ under tail-end conditions**. The source explicitly distinguishes adsorption from intermediate hydrogenations, desorption and rate-law assumptions (paper §2, Table 3; link below). An asterisk marks an adsorbed species; `*` by itself is a vacant site.

```text
Gas H₂   + 2* ⇌ 2 H*                     (hydrogen dissociation / adsorption)
Gas C₂H₂ +  * ⇌ C₂H₂*                   (acetylene adsorption)
                   |
                 + H* 
                   v
                 C₂H₃* (vinyl-like)
                   |
                 + H*
                   v
                 C₂H₄* (adsorbed ethylene)
                   | \
            desorb |  \ + H*
                   v   v
             C₂H₄(g) C₂H₅* (ethyl-like)
                       |
                     + H*
                       v
                     C₂H₆(g)
```

**A different input route** allows `C₂H₄(g) ⇌ C₂H₄*` and then further hydrogenation: pre-existing feed ethylene or ethylene that previously desorbed can return to the catalyst. The reaction-network stoichiometry alone does not distinguish these paths.

**Alternative model-specific ethane route** (Mei, Neurock & Smith, 2009): the first-principles-based kinetic Monte Carlo study of model Pd(111) and Pd–Ag/Pd(111) describes a competition after vinyl formation between a route toward ethylene and a **vinyl-to-ethylidene** route toward ethane; it also discusses further ethylidyne site-blocking. In its studied model Ag addition suppresses the ethylidene route and improves ethylene selectivity. Do **not** collapse ethylidene into the `C₂H₄*` adsorbed-ethylene intermediate from the other source as though they were identical geometries, or assert this bypass as a confirmed pathway in the BEP catalyst.

## Tier 5 Adsorption: what the first child encompasses

- **Adsorption** brings molecules from the gas phase onto available catalyst sites; `H₂` may dissociate into `H*`, while `C₂H₂` and `C₂H₄` can adsorb as intact carbon species. This is a chemical surface step, not the same as gas film/pellet mass transport.
- **Site availability/competition**: coverage of sites by acetylene, ethylene, hydrogen or other adsorbates can constrain rates and which paths are active. Vacancy and adsorbate inventories are not themselves measured coverages in the BEP.
- **Desorption** returns a surface species to gas phase, particularly important for `C₂H₄*` choosing between ethylene release and further hydrogenation.
- **Model dependence**: one-site versus two-site descriptions vary across catalysts, data and operating windows. Do not assume a universal PdAg surface or automatically impose an Urmès parameter set.
- **Next question to work through with owner**: What does `*` represent physically, and what distinguishes the adsorption of molecular acetylene from dissociative hydrogen adsorption? This can ground the first Tier-5 scientific explanation before any maturity promotion.

## Named primary sources and verified access boundary

1. **Urmès, Schweitzer, Cabiac & Schuurman (2019)**, *Kinetic Study of the Selective Hydrogenation of Acetylene over Supported Palladium under Tail-End Conditions*, *Catalysts* **9**, 180, DOI [10.3390/catal9020180](https://doi.org/10.3390/catal9020180). **Evidence:** Table 3 mechanism, 7 schematic steps, hydrogen adsorption and ethylene desorption / further hydrogenation, 0.05 wt% Pd/α-Al₂O₃. **Access:** existing AI full-text ledger; official article HTML/search index checked this turn. **Limits:** source-specific site assumptions, not a target PdAg mechanism or dynamic experiment.
2. **Mei, Neurock & Smith (2009)**, *Hydrogenation of Acetylene–Ethylene Mixtures over Pd and Pd–Ag Alloys: First-Principles-Based Kinetic Monte Carlo Simulations*, *Journal of Catalysis* **268**, 181–195, DOI [10.1016/j.jcat.2009.09.004](https://doi.org/10.1016/j.jcat.2009.09.004). **Evidence:** [PNNL institutional publication abstract](https://www.pnnl.gov/publications/hydrogenation-acetylene-ethylene-mixtures-over-pd-and-pd-ag-alloys-first-principles) explicitly reports vinyl and ethylidene alternatives, alloy-sensitive pathway competition and selectivity. **Access:** institutional abstract and publisher preview; *full article not inspected* in this review. **Limits:** ideal model surfaces and conditions; no BEP kinetic parameters or proof of bypass.
3. **Pachulski, Schödel & Claus (2012)**, *Kinetics and reactor modeling of a Pd-Ag/Al₂O₃ catalyst during selective hydrogenation of ethyne*, *Applied Catalysis A: General* **445–446**, 107–120, DOI [10.1016/j.apcata.2012.08.018](https://doi.org/10.1016/j.apcata.2012.08.018). **Evidence:** publisher abstract reports selected two-site Langmuir–Hinshelwood PdAg/Al₂O₃ description. **Access:** abstract only. **Limits:** no detailed elementary reaction diagram or periodic forcing validated. **Bibliographic caveat:** publisher indexed names appear as Axel Pachulski and Rainer Schödel; the pinned AI `sources.yaml` presently lists different forenames (Andreas / Sven), so **reconcile those names with the publisher before final bibliographic use**.
4. **Borodziński & Cybulski (2000)**, *The Kinetic Model of Hydrogenation of Acetylene–Ethylene Mixtures over Palladium Surface Covered by Carbonaceous Deposits*, DOI [10.1016/S0926-860X(99)00498-6](https://doi.org/10.1016/S0926-860X(99)00498-6). **Evidence:** existing AI full-text record supports another site-family explanation in a different supported-Pd regime; not proof of target catalyst site arrangement.
5. **Bos & Westerterp (1993)**, *Mechanism and kinetics of the selective hydrogenation of ethyne and ethene*, DOI [10.1016/0255-2701(93)87001-B](https://doi.org/10.1016/0255-2701(93)87001-B). **Access:** bibliographic/historical attachment; original full text not inspected. **Do not use** as primary proof of an independent R3 rate.

## Links to existing graph — avoid re-authoring or premature placement

- Previously archived broad theme: `B-P1-MICRO` (exact saved historical node snapshot `own_ph_alternative_surface_paths`), now *structurally* reused as Tier 4 with fresh Idea-only content.
- Subtopics still in bridges: `B-ALT-01` (hydrogenation sequences and intermediate branching), `B-ALT-02` (ethylene desorption vs continued surface hydrogenation), `B-P1-COND` (which mechanism is viable/dominant under which catalyst/conditions), plus `B-R1`, `B-R2`, `B-R3`, `B-V-R1/R2/R3` as historical proposed questions, NOT required personal nodes.
- Adsorption sidecar: `bridges/reaction_topics_pending_2026_10_22.md`, item `B-RXN-ADS`. The owner has now authorized **Tier-5 Adsorption** placement, while earlier surface subtopics remain parked until reviewed.
- AI reference IDs: `ph_sequential_path`, `ph_mechanism_choice`, `c1_microscopic_surface_path`, `c1_horiuti_polanyi_family`, `c1_vinyl_intermediate`, `c1_adsorbed_ethylene_fork`, `c1_ethylene_readsorption`, `c1_vinyl_ethylidene_alternative` (itself `Idea`), `c1_adsorption_desorption`, `c1_dissociative_h2_adsorption`, `c1_surface_sites`.
- **Maturity:** Two new placed nodes begin at **Idea**. Research from the above sources is an AI briefing only. The owner has neither endorsed the mechanism, worked out adsorption, nor verified claims/citations.

**Suggested short owner explanation when asked:** We know the three net reactions, but on the surface the catalyst first binds molecules and splits H₂; successive H additions can produce bound ethylene, which may leave as desired product or react further. Some published ideal-surface models propose another route to ethane through ethylidene. Which paths are real and significant on our catalyst remains an open scientific question.
