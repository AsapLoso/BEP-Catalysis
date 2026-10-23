# Unplaced transport theory: radial reduction, axial dispersion and species boundary conditions

**Owner discussion 2026-10-23:** Do not confuse the absence of a resolved radial coordinate with neglecting axial dispersion; and do not identify a prescribed thermal wall temperature with uniform temperature in the entire reactor. This is a **bridge-only theory explanation**, not a new personal-map concept or a decision that the BEP solver already made any particular reduction. Proposed later home: Physics → Transport Phenomena → Mass Transport / Species Conservation, with links to a separately chosen Reactor Model's assumptions and balances.

## Geometry and two independent reductions

Let \(z\in[0,L]\) be axial distance, \(r\in[0,R]\) radial distance, \(t\) time.

1. **Radial approximation:** A real tube has a radial coordinate. If cross-sectional variation can be neglected for the task, one may replace \(C_i(r,z,t)\) with a cross-sectional average \(\bar C_i(z,t)\). This is a dimensional reduction from an \((r,z)\) model to a 1D axial model; thin-tube geometry can help but does not establish sufficient lateral mixing, mass/heat-transfer adequacy or absence of pellet-level gradients.
2. **Axial dispersion approximation:** The remaining 1D species balance may *still* contain an axial dispersive flux \(J_{i,z}^{disp}\propto-D_{ax}\partial_z C_i\). Neglect of this flux is a further, separate physical approximation for large advective-to-dispersive transport ratios (Péclet-number argument). This may lower the axial spatial derivative order from second to first.
3. **Thermal analog has different physics:** Effective axial heat transport/conduction \(\lambda_z\partial_z^2T\) belongs in an energy balance. It is not identically the axial *species* dispersion coefficient \(D_{ax}\). Likewise, a wall thermal Dirichlet condition at \(r=R\) does not set an inlet species condition at \(z=0\).

## Species PDE and boundary-limit example

One illustrative gas species balance using consistent normalized coefficients is

\[
\partial_t C_i + u\,\partial_z C_i =D_{ax}\,\partial_z^2 C_i + S_i(C,\theta).
\]

At \(D_{ax}>0\), total inlet advective-plus-dispersive molar flux continuity gives a Danckwerts-type boundary condition:

\[
u C_{i,in}(t)=u C_i(0^+,t)-D_{ax}\,\partial_z C_i(0^+,t).
\]

This requires the *same velocity/concentration/porosity basis* for all terms. A common outflow closure for that model is \(\partial_z C_i(L,t)=0\). These are model-specific idealized boundaries.

In the idealized unidirectional advection limit \(D_{ax}\to0\), the inlet condition simplifies toward \(C_i(0,t)=C_{i,in}(t)\) (for \(u>0\)), while an extra downstream spatial boundary condition is generally no longer independently prescribed for the first-order-in-\(z\) equation. This is a difference in **PDE order and flux treatment**, not evidence about temperature.

## What the original proposal says, and what it does not

Proposal `Academics/BEP/Catalysis/0_Project_Management/main.tex`:
- §1.3 / lines 129, 133–134: discusses a 1D transport model, high \(Pe\), *hypothesizes* negligible axial dispersion / plug flow.
- §3.1 / lines 180–185: explicitly states a small-diameter tubular 1D radial simplification, **still writes** \(D_{ax}\partial_z^2 C_i\) in its species PDE, invokes Danckwerts inlet/outlet boundary conditions, then states the additional isothermal baseline \(T=T_0\).

Thus there are several proposed *levels* of simplification. This document does not assert which limit the actual BEP notebook currently implements; that requires code review.

Relevant general published evidence:
- [Kaczmarski (2021), Engineering Reports](https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12370): Danckwerts inlet/outlet conditions for the axially dispersed bed.
- [Chemical Engineering Communications (2014), on Danckwerts conditions](https://www.tandfonline.com/doi/full/10.1080/00986445.2013.871708): discusses nuances of different open/closed boundary idealizations.
- [Improved one-dimensional tubular packed-bed reactor model (2006)](https://www.sciencedirect.com/science/article/abs/pii/S0009250905009188): separate axial/radial *mass* and *heat* transport, and 1D reductions.

**Owner taxonomy / unplaced links:** Future Transport Phenomena (theory) ↔ future Reactor Model (chosen radial and axial simplifications / species PDE). This bridge is separate from Thermodynamics → Isothermal physical theory ↔ Reactor Model → isothermal approximation. No owner science maturity or source verification is implied by this bridge.
