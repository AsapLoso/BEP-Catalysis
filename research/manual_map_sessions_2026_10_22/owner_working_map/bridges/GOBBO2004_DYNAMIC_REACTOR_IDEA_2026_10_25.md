# B-GOBBO-2004-01 — Concept destinations to consider (Idea), with Gobbo as an optional reference

> **Bridge ≠ paper summary.** The bridge says **where we might eventually bridge to in the owner's knowledge map**. It does **not** assert that Gobbo deserves a modeling chapter or that these concepts have been personally learned. Status: **IDEA / UNPLACED**. Owner queue **Q107**. No live map node, maturity promotion or owner-written text is authorized.

## Destination ideas — not approved nodes or guaranteed locations

| Target concept to discuss later | Candidate location / existing bridge | When it would be useful | Is Gobbo specifically needed? |
|---|---|---|---|
| **Dynamic reactor species and energy balances** | **Mathematics → Mathematical Modeling → Dynamic Reactor Balances** (candidate), cross-reference existing **B-M1** | When actually deriving the chosen \(C_i(z,t)\) and possibly \(T(z,t)\) PDE rather than merely plotting a reactor | **Only potentially**: Gobbo (2004), Eqs. 1–2, prints a time-dependent 1D pseudohomogeneous mass/energy model with specified omissions. Prefer the equations/geometry of our own original proposal and more directly relevant reactor sources for our model. |
| **Method of lines / discretization and stiff time integration** | **Mathematics → Mathematical Modeling → Numerical Solution / Method of Lines** (candidate), existing **B-M3** | When turning our own spatial PDE into ODEs and checking discretization, stiffness and solver convergence | **Possible concrete example:** Gobbo discretizes with 50 backward-difference axial points/reactor and solves an ODE/DAE system using DASOLV. A numerical methods reference and our actual implementation are better for the *method itself*. |
| **Catalyst deactivation / slow activity loss** | **Physics → Catalyst Surface & Active Sites → Catalyst Activity Loss** (candidate; exact parent to be discussed), nearby existing **B-P4** | Only if our BEP scope includes deactivation, green-oil formation or long-time catalyst aging | Gobbo presents a **plant-fitted empirical decay law** (Eq. 5, Table 2). This is not physical proof of a molecular poisoning pathway, not a CO coverage time constant, and not necessarily appropriate for PdAg. |
| **Dynamic, constrained reactor-temperature optimization** | **Systems & Control → Dynamic Reactor Optimization → Manipulated Temperature Inputs** (candidate; no approved S&C child) | If we investigate objectives and constraints over operation rather than only simulating kinetics | Gobbo optimizes temperature programs over slow catalyst lifetime in a three-bed industrial configuration. This is *not* evidence for periodic CO selectivity improvement. Prefer a more directly relevant control theory source if we pursue it. |

**Important:** These are alternative destinations to **review one at a time**, not four compulsory future nodes, not branches that must all be created, and not assignments for Agents 1, 4 or 5. The personal-map tree and all understanding states remain unchanged.

## What concrete mathematical material Gobbo does and does not supply

- **Genuinely concrete:** its source **Eqs. 1–2** are coupled, time-dependent species and energy conservation equations for a spatially varying industrial fixed-bed reactor. It documents why, under *its particular plant conditions*, it neglects axial/radial dispersion and pressure drop; those simplifications are not transferred automatically to the BEP reactor.
- **Genuinely concrete:** its **Method of Lines discretization** uses first-order backward spatial finite differences with 50 points per reactor, integrated using a stiff variable-order/step DAE solver; these details could help us formulate a convergence *question* but do not constitute evidence that 50 points suffice for our own model.
- **Distinct but outside likely immediate scope:** a separately fitted **slow catalyst activity function** and an **optimal temperature schedule** under product constraints; neither validates a PdAg+CO mechanism.
- **Not useful as our kinetic foundation:** Gobbo adopts Schbib's functional form but **refits kinetics** on different industrial operating data, explicitly warning fitted coefficients may lack physical meaning. Do not transfer rates or constants into the Schbib benchmark, Larsen, Agent 5 or owner notebook.

**Original reference:** [Gobbo et al., *Modeling, Simulation, and Optimization of a Front-End System for Acetylene Hydrogenation Reactors*, BJCE 21 (2004), 545–556](https://doi.org/10.1590/S0104-66322004000400004). Source verified against the [SciELO publisher article](https://www.scielo.br/j/bjce/a/6WsJzKqRwSHR9kQbQcHc9Qk/?lang=en), especially its Mathematical Modeling and Results and Discussion sections. No independent numerical reproduction performed.

## Source-selection rule: choose the *concept* first, then the best supporting paper

Gobbo is **not the default reference for mathematical modeling** simply because it contains equations.

- For **periodic acetylene-hydrogenation measurements and transient kinetic identification**, compare [Urmès et al. (2022)](https://doi.org/10.1002/cctc.202101826), which experimentally studies a fixed bed under small-amplitude flow oscillations. Different catalyst/conditions still matter; it is *more directly aligned in question*, not automatically superior in all mathematics.
- For **industrial dynamic reactors, disturbances and independent validation**, consider [Rijo et al. (2020)](https://doi.org/10.1016/j.cej.2019.122390), which reports measured industrial disturbances and a dynamic reactor model. We have checked its published abstract, not conducted a formula-by-formula comparison.
- For **our own mass/energy PDE, boundary conditions, approximation hierarchy and MOL implementation**, prioritize the BEP proposal, relevant original 2008/reactor theory already collected, and a numerical method reference. Test the exact model/units and compare actual code rather than transplanting Gobbo's plant assumptions.
- For **Larsen PdAg kinetics**, the Larsen original thesis and its audited implementation remain primary; **Schbib** is the separate CO adsorption audit. Neither is validated by Gobbo's adjusted industrial parameters.

**Open comparison gate:** If an alternative source supports the same mathematical idea more directly, rigorously and with better matching assumptions, prefer that source. Gobbo may then remain at most a DOI/Zotero pointer instead of a Git-tracked PDF.

## Later owner decision

1. Choose **one actual target concept** to discuss, starting where the user's existing understanding ends (B-M1 and B-M3 are already queued; do not duplicate them).
2. Compare only the concrete formulas/assumptions needed for that target against the best candidate reference; show source, units, limitations and one test/derivation if appropriate.
3. Decide whether that concept merits an exact preview for owner approval and whether Gobbo has any distinct value worth local archiving. Until then, retain the existing paper bytes **unchanged**.
4. Do not write owner prose, place a node, promote knowledge status, or modify science/agent GOAL files based on this bridge.

**This note is AI background for the Q107 decision, not owner-understood science.**
