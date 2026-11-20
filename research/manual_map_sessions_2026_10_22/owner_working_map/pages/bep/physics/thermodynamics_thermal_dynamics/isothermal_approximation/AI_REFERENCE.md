> **AI RESEARCH REFERENCE — not owner-authored reader writing.** Preserved from an earlier auto-written index after the 23 October owner correction. Content may include unreviewed formulae, claims, questions or draft topology. The live node summary/maturity and approval decisions in `current_map.yaml` are authoritative; if the node was withdrawn, see `bridges/REVIEW_REQUIRED_PDE_MODEL_PROPOSALS_2026_10_23.md`. Treat this only as supporting reference, not a personal knowledge claim or an Informal Writing index.

# Isothermal approximation — physical theory and PDE meaning

An *isothermal* model does not calculate temperature as an independent changing field. For the strongest spatially uniform idealization of our tubular reactor, it imposes

\[
T(r,z,t)=T_0.
\]

This does **not** imply steady-state concentrations or adsorbate coverages: \(C_i(z,t)\) and \(\theta_i(z,t)\) may still vary during concentration pulses. *Steady temperature* (no time dependence) can also be spatially nonuniform; strictly uniform isothermal temperature is the stronger statement.

## Three things that should not be conflated

**1. Wall boundary condition.** In a two-dimensional \((r,z)\) thermal model of a tube, a prescribed wall temperature is a *Dirichlet* condition

\[
T(R,z,t)=T_w(z,t).
\]

That is only a condition at the radius \(r=R\). It does not guarantee that the center of an exothermically reacting bed also has temperature \(T_w\). A convective wall-coupling condition, such as \(-\lambda_r\partial_rT|_{R}=h(T(R)-T_w)\), is another possible choice, not equivalent to perfect wall-temperature prescription.

**2. No resolved radial variation.** If radial equilibration is sufficiently rapid and radial gradients small, a reactor may instead be represented by a cross-sectional average \(\overline T(z,t)\). Thin geometry can shorten the radial heat-transfer distance and increase the wall-area-to-volume ratio, but is not by itself proof of negligible gradients. Importantly, the wall influence can survive the radial reduction through a term like \(Ua(T_w-\overline T)\) in a one-dimensional balance.

**3. Entire field held isothermal.** Setting \(T(z,t)=T_0\) everywhere removes the temperature evolution equation as a predictive state equation (or makes it a constraint coupled to the heat removal needed). It cannot be obtained merely by imposing an inlet or wall Dirichlet value. The chemical reaction can still liberate heat; that energy must ultimately be removed/absorbed, or the resulting true temperature deviations must be small enough to neglect.

In particular, *isothermal* is not *adiabatic*: adiabatic means no heat exchange **through the chosen system boundary**, and a reacting adiabatic bed can heat up.

## What the unreduced thermal PDE would contain

A schematic, effective-property, single-temperature cylindrical equation is

\[
C_{\mathrm{eff}}\frac{\partial T}{\partial t}
+\rho_g c_{p,g}u_s\frac{\partial T}{\partial z}
=\lambda_z\frac{\partial^2T}{\partial z^2}
+\frac1r\frac{\partial}{\partial r}\left(r\lambda_r\frac{\partial T}{\partial r}\right)
+q'''_{\mathrm{rxn}}.
\]

Each term has units of power per reactor volume (W m\(^{-3}\)): thermal storage; gas-carried axial heat convection; effective axial heat transport; effective radial heat transport; reaction heat generation. This is **an illustrative theory equation**, not the BEP implementation. Gas–solid nonequilibrium, radial velocity and property profiles, wall-transfer treatment and other physical effects may require a different model.

The **heat-generation term** \(q'''_{\mathrm{rxn}}\) has its own independent physical meaning, so its stoichiometric/kinetic construction is recorded in a [separate unplaced concept draft](../../../../../bridges/THERMAL_REACTION_HEAT_SOURCE_CONCEPT_2026_10_23.md), rather than making its derivation part of the definition of “isothermal”.

## A different PDE simplification: axial **mass** dispersion

The proposal's gas species balance is of advection–axial-dispersion–reaction type:

\[
\frac{\partial C_i}{\partial t}
=D_{\mathrm{ax}}\frac{\partial^2 C_i}{\partial z^2}
-u\frac{\partial C_i}{\partial z}+S_i(C,\theta).
\]

The **radial reduction** discards the resolved radial coordinate; setting \(D_{\mathrm{ax}}\approx0\) discards the **second axial derivative in the species mass balance**. These are separate assumptions. Also, \(D_{\mathrm{ax}}\) is **not** the same coefficient as axial heat conduction/thermal dispersion \(\lambda_z\).

A model retaining nonzero \(D_{\mathrm{ax}}\) ordinarily needs inlet flux-based (Danckwerts/Robin-type) and outlet conditions. In the ideal plug-flow limit \(D_{\mathrm{ax}}\to0\) with positive downstream velocity, prescribing the entering concentration \(C_i(0,t)=C_{i,\mathrm{in}}(t)\) becomes a natural inlet condition for the first-order-in-\(z\) species equation. Boundary data must follow the *actual differential equation and flux formulation*, not be transferred from the thermal problem.

**Important proposal-versus-implementation distinction:** Our BEP proposal explicitly *writes* an axial-dispersion term, describes a one-dimensional radial approximation and Danckwerts conditions, and separately hypothesizes negligible axial dispersion for a large-Péclet plug-flow regime. That is a scoped proposal with alternative simplification steps, **not evidence that the notebook has already omitted the term**.

## Where this belongs in the scientific map

- **Here, in Thermodynamics & Thermal Dynamics:** meaning of isothermality, physical temperature field, energy storage/transport and theory behind boundary/reduction choices.
- **Future Transport Phenomena:** physical axial dispersion, radial averaging, mass-balance and boundary-condition theory; linked here, not nested under thermodynamics.
- **Future Reactor Model → Assumptions:** the **actual choices** made in a specific BEP equation set (isothermal, radial averaging, axial-dispersion negligible/retained, inlet/outlet conditions).
- **Future Reactor Model → balances/equations:** explicit chosen species and possibly energy balances, with defined units and boundary data. No model-tree parent has been fixed or placed yet.

## What evidence establishes

The original [BEP proposal](https://github.com/AsapLoso/project-management-agents/blob/docs/bep-theme-first-progress-units-20261022/Academics/BEP/Catalysis/0_Project_Management/main.tex) §3.1 (source lines 180–185) asserts a small-diameter 1D radial approximation, shows \(D_{\mathrm{ax}}\partial_z^2 C_i\), specifies Danckwerts mass-flux boundaries and states \(T=T_0\). Its hypothesis (source lines 129–134) proposes a high-Péclet plug-flow reduction. Neither proves which approximation is quantitatively valid for the experimental apparatus.

Further AI-consulted theoretical comparisons: [Improved one-dimensional model of a tubular packed bed reactor (Chemical Engineering Science, 2006)](https://www.sciencedirect.com/science/article/abs/pii/S0009250905009188) explicitly gives separate 2D and 1D heat/mass balances including a wall-transfer term; [Kaczmarski (2021)](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12370) describes inlet Danckwerts conditions for an axially dispersed bed model. These are **general supporting models**, not validated approximations for our BEP. Literature links are AI-attached, not human-verified.

## Owner-facing check

If we prescribe a constant wall temperature only, can the bed still be hotter in the middle? And if \(D_{\mathrm{ax}}\) is removed from the concentration PDE, does that by itself make the reactor isothermal? Those distinctions are the key test of whether the model assumptions are understood.
