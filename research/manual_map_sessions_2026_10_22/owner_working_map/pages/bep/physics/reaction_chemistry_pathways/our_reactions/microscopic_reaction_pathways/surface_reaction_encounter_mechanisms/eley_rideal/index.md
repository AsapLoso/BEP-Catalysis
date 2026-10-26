# Eley–Rideal (ER) — stricter usage

In the stricter terminology of [Kiani & Wachs (2024)](https://doi.org/10.1021/acscatal.4c05188), **one partner is weakly physisorbed** near the surface and reacts with another partner that is **chemisorbed**. This differs from a *direct gas-phase collision with a chemisorbed species*, which the authors call **Langmuir–Rideal (LR)**.

### The three existing subtopics

**Elementary encounter:** `A* + B(phys) → products` is a pedagogical schematic: A is chemisorbed, B is weakly physisorbed. It is not an experimentally observed BEP elementary reaction.

**Illustrative surface rate:** A possible weak-adsorbate rate form is `r_s = k_ER θ_A θ_B,phys`. Only after an additional weak-adsorption equilibrium assumption (e.g. dilute `θ_B,phys ≈ K_B,phys p_B`) does this become proportional to `θ_A p_B`. This is a conceptual limiting derivation, not a published source's exact fitted equation.

**Assumptions:** Existence and residence of a weakly physisorbed species, the surface chemisorbed partner, compatibility of local site/area convention, low-coverage assumptions if converting to pressure, and the energy-transfer/reaction probability.

### Diagram warning and sources

The earlier original schematic `../assets/eley_rideal_type.svg` shows an incoming **gas-phase** reactant. It is retained in the [shared encounter-mechanisms overview](../index.md) to explain LR and to avoid silently discarding a requested image. **It is not an accurate illustration of strict ER physisorption.**

[Kiani & Wachs (2024), *ACS Catalysis* 14, 16770–16784, DOI 10.1021/acscatal.4c05188](https://doi.org/10.1021/acscatal.4c05188) gives the general physical taxonomy and derived-model caveats. The three personal ER subtopics are currently **Ideas** and have AI-authored technical notes; no experimental evidence places ER on our PdAg system. No human-verified citations.
