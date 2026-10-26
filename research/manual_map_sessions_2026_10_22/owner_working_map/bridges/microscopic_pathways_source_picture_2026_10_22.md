# Microscopic Reaction Pathways — sourced scientific picture (AI reference, 2026-10-22)

**Status:** Research for owner discussion; **not** Human worked out or verified by the owner. This document is **not** the personal Tier-4/Tier-5 writing page and does not authorize promotion. The owner chose the *structure* `Our Reactions → Microscopic Reaction Pathways (Tier 4) → Adsorption (Tier 5)`; scientific content below remains AI-interpreted.

## The working picture — NOT a verified BEP surface mechanism

```text
                   adsorption                     H addition         H addition
C₂H₂(g)       →     C₂H₂*                 →         C₂H₃*          →   C₂H₄* (ethylene-like)
                                                                      ├── desorb → C₂H₄(g)  [desired]
                                                                      └── add more H → C₂H₆(g) [overhydrogenation]

C₂H₄(g)       →     C₂H₄*  → further H addition → C₂H₆(g)            [gas ethylene can readsorb]

Model-dependent alternative:
C₂H₃* (vinyl) → ethylidene* → further H addition → C₂H₆(g)           [2009 ideal-surface KMC hypothesis]
                              └→ ethylidyne* (site blocker in model)
```

`*` means an adsorbed species/site-binding shorthand; actual elementary arrows, vacancies, H-atom accounting and reversibility are **deliberately omitted** from this conceptual sketch. Full site-balanced reactions must be verified against the chosen mechanism. A **direct gas-phase net R3 label** does not uniquely identify a microscopic pathway or a separately identifiable fitted rate.

## Four sources and the exact evidence boundaries

1. **Urmès, Schweitzer, Cabiac & Schuurman (2019),** *Kinetic Study of the Selective Hydrogenation of Acetylene over Supported Palladium under Tail-End Conditions*, *Catalysts* 9, 180, DOI [10.3390/catal9020180](https://doi.org/10.3390/catal9020180). **Evidence:** published full text, reaction mechanism/Table 3 and kinetic discussion, recorded as full-text inspected in integrated source ledger `urmes2019`. A Horiuti–Polanyi-derived single-site kinetic description treats H₂ adsorption, acetylene/ethylene adsorption, and hydrogenation of surface intermediates. **Limit:** 0.05 wt% Pd/α-Al₂O₃, specific tail-end temperatures/pressure and fitted steady kinetics, not direct evidence of PdAg target catalyst or a universal pathway. Seven-step transcription in [C research dossier](../../../presentation/deep-dives/C_reaction_mechanism_2026-10-14.md) is explicitly *schematic*, not citation-ready verbatim arrow directions. (DOI may be followed externally; repo relative dossier link is given for navigation, not proof.)

2. **Mei, Neurock & Smith (2009),** *Hydrogenation of acetylene–ethylene mixtures over Pd and Pd–Ag alloys: First-principles-based kinetic Monte Carlo simulations*, *Journal of Catalysis* 268, 181–195, DOI [10.1016/j.jcat.2009.09.004](https://doi.org/10.1016/j.jcat.2009.09.004). **Evidence:** author-institution [abstract](https://experts.umn.edu/en/publications/hydrogenation-of-acetylene-ethylene-mixtures-over-pd-and-pd-ag-al/) explicitly discusses (a) vinyl → ethylene (selective), (b) ethylene overhydrogenation and (c) vinyl → ethylidene → ethane (competing) on *idealized* Pd(111) and Pd–Ag/Pd(111). Also discusses ethylidyne site blocking and Ag effects. **Limit:** DFT/KMC model observations do not prove all three operate in target supported PdAg/SiO₂ powder or establish individual kinetic constants; article full text not inspected in the integrated ledger (`mei2009`: abstract/preview).

3. **Pachulski, Schödel & Claus (2012),** *Kinetics and reactor modeling of a Pd–Ag/Al₂O₃ catalyst during selective hydrogenation of ethyne*, *Applied Catalysis A* 445–446, 107–120, DOI [10.1016/j.apcata.2012.08.018](https://doi.org/10.1016/j.apcata.2012.08.018). **Evidence:** publisher [abstract](https://www.sciencedirect.com/science/article/abs/pii/S0926860X12005406) reports a best-fitting Langmuir–Hinshelwood kinetic model involving two active sites for hydrogenating ethyne and ethene on an industrial PdAg/Al₂O₃ catalyst. **Limit:** an effective kinetic model and comparison, not a direct measurement of every microscopic intermediate; abstract only in the existing ledger. **Metadata audit flag:** publisher lists **Axel Pachulski and Rainer Schödel**; current integrated ledger incorrectly appears to list **Andreas Pachulski and Sven Schödel**. Verify authoritative metadata before reusing names or changing pinned research files.

4. **Urmès et al. (2022),** *Microkinetic Modeling of Acetylene Hydrogenation Under Periodic Reactor Operation*, *ChemCatChem*, DOI [10.1002/cctc.202101826](https://doi.org/10.1002/cctc.202101826). **Evidence:** publisher [abstract](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cctc.202101826) uses small periodic flow oscillations to calibrate a single-site transient microkinetic description for Pd/α-Al₂O₃; it identifies H adsorption and vinyl→adsorbed-ethylene hydrogenation as influential in the reported fit. **Limit:** this is source-specific transient identification, *not* experimental proof of an increased cycle-averaged ethylene yield for BEP; abstract/preview in ledger.

## Project source crosswalk — earlier documents checked, no duplicate science subtree

- Original BEP proposal `Academics/BEP/Catalysis/0_Project_Management/main.tex`, Methodology, `Microscopic Surface Dynamics`: *proposes* explicit adsorbate coverages and site conservation for non-PSSA modelling, but is not evidence that each surface intermediate has been observed or calibrated for the present catalyst. The proposal's kinetic-memory and periodic benefit assertions are research hypotheses.
- Legacy overlay `Academics/BEP/Catalysis/mindmap/data/bep_draft_overlay.yaml` at `devcontainer` snapshot `5816807c2d3077e367d3a3bb9ce014a76b3112fe`: `c1_microscopic_surface_path`, `c1_horiuti_polanyi_family`, `c1_adsorption_desorption`, `c1_vinyl_intermediate`, `c1_adsorbed_ethylene_fork`; these were AI research drafts, not owner understanding.
- `Academics/BEP/Catalysis/presentation/deep-dives/C_reaction_mechanism_2026-10-14.md`, §§C.1–C.5: explicit comparison between published 2019 quasi-steady kinetic model, legacy three-coverage code and an uncalibrated five-coverage experimental model. Do **not** confuse illustrative seven steps with a verified reactor implementation.
- The pinned integrated scientific graph `reference_map.yaml` → commit `1cd680f95902a0a79b17afb084fa29ab49c6b25f` → `nodes.yaml` has AI nodes `ph_sequential_path`, `ph_mechanism_choice`, `c1_microscopic_surface_path`, `c1_adsorption_desorption`, `c1_dissociative_h2_adsorption`, `c1_hydrocarbon_site_competition`, `c1_vinyl_ethylidene_alternative`. `sources.yaml` records access/locators; both source truth and owner reading must be checked separately.
- Exact older Tier-4 idea preserved in `bridges.yaml` as `B-P1-MICRO`, historical snapshot `own_ph_alternative_surface_paths`; `B-ALT-01`, `B-ALT-02`, `B-R1`, `B-R2`, `B-R3` remain lower-detail **bridges**, not automatically restored in the new personal subtree.
- Adjacent `B-P1-COND` (Viability & Conditions) remains a **different, unplaced theme**. Rate laws, their identifiability and operating regimes are also not auto-added as live pathway descendants.

## Next owner-led learning step: Tier 5 — Adsorption

Start from first principles: a gas species can attach to a vacant active site, hydrogen may dissociate to adsorbed H, site occupation can impede other reactants, and molecules may later desorb. **Different surface/site models are possible.** Only after the owner reviews this concept should any science stage beyond Idea be proposed for Tier 5. Clarify the exact Pd versus PdAg site/coverage assumptions as a separate source-bounded question rather than assuming the first model is universally correct.

**Review status:** AI-source comparison only; no claim-level owner verification, human-understood promotion, chosen adsorption rate expression, or experimentally established BEP-specific microscopic mechanism.
