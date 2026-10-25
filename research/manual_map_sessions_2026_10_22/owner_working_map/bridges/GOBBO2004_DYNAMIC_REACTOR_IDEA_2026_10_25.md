# B-GOBBO-2004-01 — Gobbo 2004: dynamic-reactor modeling, deactivation and temperature control

**Tag / maturity: IDEA (bridge only).** **Status: unplaced, owner has not read or personally verified the science.** Related open owner queue: **Q107**. This is a possible *future study link* across Physics, Mathematics and Systems & Control, **not** a live node, an active kinetic benchmark, a validated parameter source or a recommendation to use Gobbo's equations unchanged.

## What the original paper actually covers (source-bounded AI summary)

**Paper:** R. Gobbo, R. P. Soares, M. A. Lansarin, A. R. Secchi and J. M. P. Ferreira, *Modeling, Simulation, and Optimization of a Front-End System for Acetylene Hydrogenation Reactors*, *Brazilian Journal of Chemical Engineering* **21** (2004), pp. 545–556. DOI: https://doi.org/10.1590/S0104-66322004000400004.

- **Industrial context:** three adiabatic front-end packed-bed reactors in series, with interstage cooling. Unlike the smaller BEP PdAg experiments, this is an industrial multicomponent feed and a different catalyst/plant scenario. Source: paper abstract and Problem Description, journal pp. 545–547.
- **Dynamic model:** time- and axial-position-dependent species and energy balances, pseudohomogeneous approximation, neglected radial/axial dispersion under argued industrial assumptions, catalyst activity changing slowly. Source: Mathematical Modeling, journal pp. 547–549, Eqs. 1–2.
- **Numerics:** method of lines, 50 first-order-backward axial points in each reactor, stiff variable-step/order differential-algebraic solver in gPROMS/DASOLV. Source: Results and Discussion, journal p. 550.
- **Control/optimization:** dynamic selection of reactor inlet/intercooler temperature profiles to meet product constraints while compensating for catalyst deactivation over a long operating period; this is **not** a demonstration of improved selectivity from periodic CO feed. Source: paper abstract, Optimization and Results sections.
- **Kinetic limitation:** uses the functional form from Schbib 1996, but fits industrial constants to plant data and explicitly cautions that fitted parameters may have no physical meaning. Thus the rate parameters and the CO inhibition factor **must not be imported** as source-verified values for the current Schbib/PdAg experiments. Source: Mathematical Modeling, journal p. 549.

## Candidate idea bridges to existing personal map

| Possible learning topic | Bridge / current anchor | Why it might help later |
|---|---|---|
| Spatiotemporal reactor state and balance equations | **B-M1**, Mathematics → Mathematical Modeling (existing parent) | A concrete industrial example of time-and-space-dependent coupled balances |
| Spatial semi-discretization and stiff time solver | **B-M3** | A numerical method used for a real multiphysics reactor model; not automatically the best method for our geometry |
| Thermal effects, slow catalyst activity loss | **B-P4**, Physics → Thermodynamics & Thermal Dynamics (existing parent) | Keep energy storage/heat release distinct from deactivation dynamics |
| Boundary conditions and reduction choices | **B-MODEL-BC-01** | Compare why Gobbo's industrial assumptions may differ from another PDE model's dispersion and inlet/outlet conditions |
| Dynamic optimization and feedback for reactor operation | **Systems & Control (existing root; no selected child)** | Possible future question about manipulating temperature in response to slow activity loss, not periodic CO wave claims |

## Questions to answer before retaining more than a bibliographic pointer

1. Does our BEP actually need **catalyst deactivation over long times** or **industrial temperature optimization**? If not, is Gobbo useful only as contextual reading rather than a local PDF in the curated scientific source archive?
2. Is there anything in Gobbo's PDE/ODE numerical formulation beyond what the more directly relevant 2008/2009/2019/2022 sources already cover? Compare source-backed equations and validation cases, not superficial terminology.
3. What physical effects are deliberately omitted in Gobbo's industrial pseudohomogeneous closure, and which omissions cannot be carried into our laboratory catalyst/transport model?
4. Which part of its control objective is distinct from the proposed fast CO inlet modulation? Do not confuse long-run temperature adjustment for deactivation with rapid periodic selectivity enhancement.
5. If the archive is later pruned, what minimal reference should remain (citation, DOI, short exclusion rationale), and should repository binaries be deleted only after an explicit owner decision?

## Separation, limitations and next action

This is **AI reference prose** based on an inspection of the repository's extracted Gobbo paper. It is not an owner-understood scientific section and does not independently validate the paper's industrial simulations. The Gobbo PDF and extracted text currently remain in `research/literature/`; **do not delete, redistribute, reclassify as a key source, or copy coefficients into other models as a result of this Idea bridge**.

**Next owner-led step:** When dynamic control, slow deactivation or reactor-model simplifications become the topic of study, show the owner a short comparison against more directly relevant sources, and let the owner decide whether this Idea warrants its own concept or only a Zotero citation. No current-map node, status promotion, human source verification, personal prose or active Agent 1/4/5 GOAL change is authorized.
