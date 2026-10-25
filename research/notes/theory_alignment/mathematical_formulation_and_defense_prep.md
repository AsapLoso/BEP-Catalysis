# Mathematical formulation and defense preparation

**Scope.** This note derives the transport scalings for the ranges in Agent 3's mission and identifies which values can be calculated from them. It distinguishes textbook screening values from measured reactor properties. It does not approve a BEP model choice.

**Conclusion from the supplied data.** The geometric and velocity ranges allow a conditional estimate of mass Peclet numbers. They do not specify the rate law and rate basis, gas properties, bed porosity, pellet diffusivity, pellet shell depth, heat-transfer properties, temperature, pressure, or measured residence-time distribution (RTD). Therefore numerical Damköhler numbers, Biot numbers, Thiele moduli, effectiveness factors, and thermal Peclet numbers cannot be calculated for the BEP apparatus from the supplied data.

## 1. Definitions and bases

Use \(z\in[0,L]\), bed void fraction \(\epsilon_b\), superficial gas velocity \(u_s=Q/A\), and interstitial velocity \(u_i=u_s/\epsilon_b\). Let \(C_i\) denote concentration in the bed gas voids. The axial dispersed species balance, on a bed-volume basis, is

\[
\epsilon_b\frac{\partial C_i}{\partial t}
=-\frac{\partial}{\partial z}
\left(u_s C_i-\epsilon_bD_{ax}\frac{\partial C_i}{\partial z}\right)
+\rho_b r_i,
\]

where \(D_{ax}\) is the effective axial dispersion coefficient on this convention, \(\rho_b\) is catalyst mass per bed volume, and \(r_i\) is a net species rate per catalyst mass. For constant \(\epsilon_b\), division by \(\epsilon_b\) gives the convective velocity \(u_i\). The Peclet definitions below use \(u_i\). If the mission's \(u\) is instead superficial, replace it by \(u_s/\epsilon_b\) in these definitions.

The reaction source must use the same volume basis as the accumulation and flux terms. A quoted \(k\) is not meaningful in a Damköhler number until its units, catalyst-mass basis, and rate law are specified.

## 2. Mass transport screening over the stated window

For packed spheres, Froment, Bischoff, and De Wilde report that a design value \(Pe_p=u_i d_p/D_{ax}\) of roughly 1–2 is representative (2011, p. 560). Treat this as a screening envelope, not a fitted correlation or a BEP measurement. Then

\[
Pe_{m,p}=\frac{u_i d_p}{D_{ax}}\approx1\text{--}2,\qquad
Pe_{m,L}=\frac{u_iL}{D_{ax}}=Pe_{m,p}\frac{L}{d_p}.
\]

Here \(Pe_{m,L}\) is the mission's \(Pe_{m,ax}\), and \(Pe_{m,p}\) is its particle-scale \(Pe_p\).

The geometry gives \(L/d_p=16.7\text{--}200\). The corresponding envelopes are:

| \(L\) (m) | \(d_p\) (mm) | \(L/d_p\) | Screened \(Pe_{m,L}\) |
|---:|---:|---:|---:|
| 0.05 | 3 | 16.7 | 16.7–33.3 |
| 0.05 | 1 | 50 | 50–100 |
| 0.20 | 3 | 66.7 | 66.7–133 |
| 0.20 | 1 | 200 | 200–400 |

Across the corners of \(u_i=0.01\text{--}0.1\ \mathrm{m\,s^{-1}}\) and \(d_p=1\text{--}3\ \mathrm{mm}\), that design envelope implies \(D_{ax}=u_i d_p/Pe_{m,p}\approx5\times10^{-6}\text{--}3\times10^{-4}\ \mathrm{m^2\,s^{-1}}\). This is a back-calculated range from a textbook design estimate. It is not an apparatus measurement. A tracer RTD is the direct way to estimate the target-bed dispersion coefficient.

A large bed-scale Peclet number does not alone guarantee negligible dispersion in a reacting bed. Froment et al. give a screening criterion for a first-order reaction in a simple bed:

\[
\frac{L}{\ell} >
\frac{1}{\delta Pe_{\ell,a}}\ln\!\left(\frac{C_{A0}}{C_A}\right),
\]

where \(\ell\) is the characteristic local dispersion length, \(Pe_{\ell,a}=u_i\ell/D_{ax}\), and \(\delta\) is the allowable conversion error (Froment et al., 2011, pp. 707–708, Eq. 12.7.2-15). Setting \(\ell=d_p\) and \(\delta=0.05\) only for illustration, a 50% conversion requires \(L/d_p>6.9\text{--}13.9\); 90% requires \(>23.0\text{--}46.1\); and 95% requires \(>30.0\text{--}59.9\), with the larger threshold corresponding to \(Pe_{p}=1\). The supplied \(L/d_p\) window includes values below these thresholds for high conversions. This criterion assumes the simple steady first-order setting; periodic operation, nonlinear kinetics, wall effects, and strong thermal coupling need separate comparison.

Froment et al. also report the rough design rule that axial dispersion often has little effect when bed depth exceeds about \(50d_p\), then present the Young–Finlayson gradient criteria (2011, pp. 560–561). In the specified window, \(L/d_p\) ranges from 16.7 to 200, so the rough rule is not met everywhere. Use a measured RTD or report plug-flow and dispersion-model sensitivity before selecting a closure. Danckwerts' residence-time analysis motivates measuring departure from ideal plug flow; the packed-bed dispersion equation and its boundary conditions require the additional reactor-model assumptions in the next section.

Levenspiel and Bischoff review plug flow, back-mixing, and non-ideal flow patterns as alternatives for representing measured reactor flow (1963, pp. 95–198). This supports using tracer evidence to select the flow closure; it does not prescribe the BEP reactor's dispersion coefficient. [7]

For a fixed \(u_i,d_p\), the mission window also gives \(u_i d_p=10^{-5}\text{--}3\times10^{-4}\ \mathrm{m^2\,s^{-1}}\), \(u_iL=5\times10^{-4}\text{--}2\times10^{-2}\ \mathrm{m^2\,s^{-1}}\), and nominal \(L/u_i=0.5\text{--}20\ \mathrm{s}\). The latter is a gas transit-time scale only under constant velocity and this interstitial-velocity convention. If the provided \(u\) is superficial, the void residence time is \(\epsilon_bL/u_s=L/u_i\), and \(\epsilon_b\) is needed to convert between the two velocities.

## 3. Heat transport groups

With effective axial thermal conductivity \(\lambda_{ax}\), gas density \(\rho_g\), and heat capacity \(c_{p,g}\),

\[
Pe_{h,p}=\frac{\rho_gc_{p,g}u_i d_p}{\lambda_{ax}},\qquad
Pe_{h,L}=\frac{\rho_gc_{p,g}u_iL}{\lambda_{ax}}.
\]

These are dimensionless. The analogous mass and heat dispersion values may be similar under a validated heat–mass analogy, but the mass estimate \(Pe_{m,p}\approx1\text{--}2\) is not a measured thermal value. Froment et al. note limited data for \(\lambda_{ax}\) and describe Bischoff's use of the heat–mass analogy (2011, p. 560). No \(\rho_g,c_{p,g},\lambda_{ax}\), temperature, pressure, or gas composition is supplied here, so numerical \(Pe_h\) values are not available.

## 4. Reaction, film, and pellet groups

### 4.1 Axial Damköhler number

For a first-order volumetric bed rate \(r_{v,A}=k_v C_A\),

\[
Da_I=\frac{k_v L}{u_i}
=\frac{k\rho_bL}{u_i},
\]

where \(k\) is per catalyst mass and \(k_v=k\rho_b\) is per bed volume. The supplied geometry gives \(L/u_i=0.5\text{--}20\ \mathrm{s}\), so \(Da_I=(k\rho_b)(0.5\text{--}20\ \mathrm{s})\), but \(k\rho_b\) is unknown. For a nonlinear rate law, use the local ratio \(Da_I(z)=\rho_b r_A(z)L/[u_iC_A(z)]\) or a clearly defined differential pseudo-first-order coefficient. If \(u\) is superficial, the algebraic form contains \(u_s/\epsilon_b\), not \(u_s\) alone, when the balance is written per gas void volume.

### 4.2 External mass-transfer Damköhler number

Schbib et al. define an interphase Damköhler number as maximum intrinsic surface rate divided by maximum film-transfer rate (1996, p. 1500, Eq. 14):

\[
Da_{II}=\frac{r_{\max}}{k_g a_m C_A},
\]

where numerator and denominator must share the same catalyst-mass basis; \(a_m\) is external particle area per catalyst mass. On a bed-volume basis the equivalent ratio is

\[
Da_{II}=\frac{\rho_b r_{\max}}{k_g a_{v,b}C_A},
\]

where \(a_{v,b}\) is external particle area per bed volume. For first-order per-mass kinetics \(r_{\max}=kC_A\), these reduce to \(k/(k_ga_m)\) and \(k\rho_b/(k_ga_{v,b})\). The mission form \(k\rho_b d_p/(k_g a_v)\) has units of length if \(a_v\) is the usual area per bed volume; if \(a_v\) means another basis, it must be defined before the group can be used. Do not carry the extra \(d_p\) without a stated definition.

Froment et al. give packed-sphere gas-film correlations for \(\epsilon=0.37\): \(j_D=1.66Re_p^{-0.51}\) below \(Re_p=190\), and \(j_D=0.983Re_p^{-0.41}\) above it (2011, pp. 157–158, Eqs. 3.2.1-5 to -6). Here \(Re_p=d_pG/\mu\), \(G=\rho_g u_s\), and \(Sc=\mu/(\rho_gD_m)\); the mass-transfer coefficient follows the stated \(j_D\) relation for the selected driving-force basis. These correlations need gas properties, void fraction, and driving-force convention. The supplied \(u\) and \(d_p\) alone do not determine \(Re_p\), \(k_g\), or \(Da_{II}\).

### 4.3 Biot numbers

With pellet radius \(R_p=d_p/2=0.5\text{--}1.5\ \mathrm{mm}\),

\[
Bi_m=\frac{k_gR_p}{D_{eff}},\qquad
Bi_h=\frac{h_gR_p}{\lambda_{p,eff}}.
\]

Here \(D_{eff}\) and \(\lambda_{p,eff}\) are intrapellet effective diffusivity and conductivity. These radius-based conventions compare external film resistance with internal pellet transport resistance. Some lumped-capacitance heat analyses use \(V/S=R_p/3\); state the length convention when quoting a Biot threshold. No \(k_g,D_{eff},h_g,\lambda_{p,eff}\) values are supplied, so neither Biot number is numeric.

Froment et al. express packed-bed gas-to-particle heat transfer as \(h_f=j_Hc_pGPr^{-2/3}\), with \(j_H=f(Re_p)\) (2011, pp. 158–159, Eq. 3.2.2-2). This still requires flow and gas-property data. A value for \(Bi_h\) cannot be inferred from \(Bi_m\) without an explicit heat–mass analogy and solid properties.

### 4.4 Thiele modulus and effectiveness

For a homogeneous sphere with an isothermal first-order reaction and constant \(D_{eff}\), define the radius-based modulus

\[
\phi_R=R_p\sqrt{\frac{k\rho_p}{D_{eff}}},
\qquad
\eta_{sphere}=\frac{3}{\phi_R^2}\left(\phi_R\coth\phi_R-1\right),
\]

where \(k\) is per catalyst mass and \(\rho_p\) is catalyst mass per pellet volume. Froment et al. derive this sphere result (2011, pp. 195–196, Eqs. 3.6.1-9 to -11). It does not directly describe an eggshell particle.

For an eggshell of depth \(\delta_s\), the active region is \(R_p-\delta_s<r<R_p\). Even for a one-component first-order approximation, one must solve

\[
\frac{1}{r^2}\frac{d}{dr}\!\left(r^2D_{eff}\frac{dC_A}{dr}\right)
-k\rho_p\mathbf{1}_{[R_p-\delta_s,R_p]}C_A=0
\]

with regularity at \(r=0\), concentration/flux matching at \(r=R_p-\delta_s\), and an external-film condition at \(R_p\). The eggshell effectiveness factor is total reaction in the active shell divided by the rate if that shell were at the chosen surface concentration. Its value depends on \(\delta_s/R_p\), film resistance, and the rate and diffusivity. The BEP files inspected for this note do not supply shell depth or radial Pd activity. Schbib et al. describe homogeneous Pd distribution in their Pd/α-Al₂O₃ pellets (1996, p. 1502), so that paper cannot supply an eggshell profile.

The first-order Weisz–Prater check is

\[
\Phi_{WP}=\frac{(r_A\rho_p)_{obs}L_c^2}{D_{eff}C_{A,s}}\ll1,\qquad L_c=V_p/S_p=R_p/3
\]

for a sphere in the Froment convention (2011, pp. 214–215, Eq. 3.9-5). This is an observable screening criterion, not a substitute for a measured rate and diffusivity. Schbib et al. applied their criterion after fitting rates and reported a concern only at very high acetylene conversion, where the surface concentration is low (1996, p. 1504, Eq. 26 and following text). That result applies to their catalyst and conditions; it does not establish negligible diffusion in the BEP pellets.

## 5. Danckwerts boundary conditions from flux balance

For the balance in Section 1, the axial molar flux is

\[
N_{i,z}=u_sC_i-\epsilon_bD_{ax}\frac{\partial C_i}{\partial z}.
\]

At an inlet interface where the upstream feed is convective and has concentration \(C_{i,in}(t)\), conservation requires the bed-side total flux to equal the feed flux:

\[
N_{i,z}(0,t)=u_sC_{i,in}(t).
\]

Therefore

\[
u_s\left[C_{i,in}(t)-C_i(0,t)\right]
=-\epsilon_bD_{ax}
\left.\frac{\partial C_i}{\partial z}\right|_{0}.
\]

This is the Danckwerts inlet condition on the stated convention. It holds during a pulse as well as at steady state because it is an interface flux balance. It does not require the bed concentration at the boundary to equal the upstream feed concentration.

A Dirichlet value \(C_i(0,t)=C_{i,in}(t)\) is not automatically nonconservative. It becomes inconsistent if the model also counts only \(u_s C_{i,in}\) as entering flux while the dispersed equation carries the boundary contribution \(-\epsilon_bD_{ax}\partial_zC_i\). A conservative finite-volume model can impose a Dirichlet state and still conserve mass if it uses the actual total numerical flux. The boundary should match the physical upstream domain: feed reservoir, valve, tubing, and inlet distributor may need their own states or transfer functions. Sharp pulses make a flux mismatch more visible, but do not change the conservation derivation.

At the outlet, the common closed-to-diffusion condition is

\[
\left.\frac{\partial C_i}{\partial z}\right|_{L}=0.
\]

It sets the dispersive flux to zero at the exit, leaving convective outflow. It is a convenient boundary closure for a reactor discharging to a non-dispersive downstream region. Large \(Pe_{m,L}\) supports a thin outlet dispersion layer and often reduces sensitivity to outlet details. High Peclet number alone does not make the Neumann condition exact for every geometry or downstream domain. Compare boundary alternatives if predictions depend on the outlet. Froment et al. discuss Danckwerts, Wehner–Wilhelm, Pearson, and Bischoff boundary work and give these commonly used conditions (2011, pp. 560–561); Danckwerts (1953) provides the residence-time framework and historical context.

The thermal analogue matches total heat flux at the inlet,

\[
\rho_gc_{p,g}u_s[T_{in}(t)-T(0,t)]
=-\lambda_{ax}\left.\frac{\partial T}{\partial z}\right|_0,
\qquad
\left.\frac{\partial T}{\partial z}\right|_L=0,
\]

only when the energy balance and \(\lambda_{ax}\) use the same area and phase basis.

## 6. Spatial discretization and numerical Peclet number

For the one-dimensional convection–dispersion equation, a centered second-order approximation to the first derivative has spatial truncation error \(O(\Delta z^2)\); centered second differences for axial diffusion have error \(O(\Delta z^2)\). First-order upwind convection has error \(O(\Delta z)\) and adds numerical diffusion of order \(u_i\Delta z/2\). Upwind can smear a pulse even when it stays non-oscillatory.

For standard centered convection–diffusion finite differences, a monotone stencil requires the cell Peclet number

\[
Pe_{\Delta z}=\frac{u_i\Delta z}{D_{ax}}\le2.
\]

With \(N\) equal intervals, \(Pe_{\Delta z}=Pe_{m,L}/N\). Since the screened \(Pe_{m,L}\) envelope is 16.7–400, satisfying this condition over that full envelope requires at least \(N=200\) intervals. This is a conservative envelope calculation, not a mesh prescription. If using superficial velocity, write \(Pe_{\Delta z}=u_s\Delta z/(\epsilon_bD_{ax})\). A flux-limited or TVD finite-volume method is a candidate for preserving steep fronts, but its order and limiter behavior must be checked on the chosen grid. Implicit time integration does not remove spatial oscillations from a non-monotone stencil.

A grid study should compare outlet pulse amplitude, phase, integrated species balance, and conversion against a refined mesh. If axial dispersion is omitted, upwind numerical diffusion must not be presented as a physical estimate of \(D_{ax}\). Gobbo et al. report a 50-point method-of-lines discretization with first-order backward spatial differences for their industrial front-end model (2004, p. 550); that is a method precedent, not evidence that the BEP grid is converged.

## 7. Physical inputs needed for numerical evaluation

| Quantity | Needed input |
|---|---|
| \(Pe_m\) | Measured tracer RTD or \(D_{ax}\), bed void fraction if velocity is superficial |
| \(Pe_h\) | Gas density, heat capacity, effective axial thermal conductivity, temperature, composition |
| \(Da_I\) | Rate law and rate basis, \(T,P\), composition, catalyst mass per bed volume |
| \(Da_{II}\) | Gas \(Re,Sc\) or \(k_g\), pellet shape and external area basis, intrinsic rate at bulk concentration |
| \(Bi_m\) | \(k_g,D_{eff}\), pore structure, temperature and mixture |
| \(Bi_h\) | \(h_g,\lambda_{p,eff}\), pellet geometry |
| \(\phi_R,\eta\) | Kinetic law and local rate, active density, \(D_{eff}\), shell depth and Pd radial profile |
| Pressure drop | \(\epsilon_b,\mu,\rho_g,u_s,d_p,L\), with regime check |

The universal gas constant is \(R=8.31446261815324\ \mathrm{J\,mol^{-1}\,K^{-1}}\), the exact SI product of the defining Boltzmann and Avogadro constants. Use \(R\) when \(E\) is in \(\mathrm{J\,mol^{-1}}\) and \(T\) in kelvin. If the source reports \(E\) in \(\mathrm{kJ\,mol^{-1}}\), convert units before evaluating \(e^{-E/(RT)}\). [6]. Do not mix catalyst-mass rates with bed-volume accumulation.

## 8. Oral defense bank

### Cluster 1 — Reactor transport and non-idealities

#### 1. Why retain axial dispersion instead of using plug flow?

**Supervisor Trap:** Treating a large \(Pe_L\) as proof that dispersion is irrelevant.

**Model Answer:** \(Pe_L=u_iL/D_{ax}=Pe_p(L/d_p)\). The sphere-bed design estimate \(Pe_p\approx1\text{--}2\) gives \(Pe_L\approx17\text{--}400\) over the stated geometric range, but the short-bed/high-conversion cases can fail the 5% first-order screen. A tracer RTD estimates \(D_{ax}\); I would compare dispersed and plug-flow predictions at the actual conversion before dropping the second derivative. [2, pp. 560–561, 707–708]

#### 2. How can wall effects or channeling invalidate the one-dimensional average?

**Supervisor Trap:** Assuming the cross-section is uniform because the reactor is narrow and the model has one axial coordinate.

**Model Answer:** A 1D model averages radial velocity and concentration structure. Wall packing, a small tube-to-particle ratio \(d_t/d_p\), nonuniform loading, or bypass paths can create channeling and radial gradients. I need the tube diameter, pellet distribution, and a tracer or multi-point temperature/concentration check. If those show persistent radial structure, a radial 2D or multi-zone model is a candidate.

#### 3. What does the Ergun equation require, and what would it tell you?

**Supervisor Trap:** Inserting particle size and velocity alone into a pressure-drop formula.

**Model Answer:** In the standard packed-bed form,
\[
-\frac{dP}{dz}=150\frac{(1-\epsilon_b)^2}{\epsilon_b^3}\frac{\mu u_s}{d_p^2}
+1.75\frac{1-\epsilon_b}{\epsilon_b^3}\frac{\rho_gu_s^2}{d_p}.
\]
I need \(\epsilon_b,\mu,\rho_g,u_s,d_p,L\). Compare \(\Delta P/P_{in}\) with a declared tolerance before treating pressure as constant. The correlation is from Ergun's packed-bed relation as presented by Froment et al. [2, p. 508, Eq. 11.5.1-13]

#### 4. Why are there two Danckwerts conditions?

**Supervisor Trap:** Calling the inlet and outlet both “zero-gradient boundaries.”

**Model Answer:** The inlet equates the upstream convective feed flux with bed-side convective plus dispersive flux: \(u_s(C_{in}-C_0)=-\epsilon_bD_{ax}C_z(0)\). At the outlet \(C_z(L)=0\) sets dispersive flux to zero, so material exits convectively. They express different interfaces. [1; 2, pp. 559–561]

#### 5. Does \(Pe_L\gg1\) make the outlet Neumann condition exact?

**Supervisor Trap:** Confusing an asymptotic approximation with a universal boundary theorem.

**Model Answer:** No. It often makes outlet details less influential because dispersion is confined to a short length scale \(D_{ax}/u_i\). The Neumann condition represents an outlet with no axial diffusive flux into the downstream region. A coupled downstream pipe or another boundary condition may be needed if the outlet influences the result. [2, pp. 703–704]

### Cluster 2 — Kinetics and surface adsorption

#### 6. How do you derive a Langmuir–Hinshelwood rate law?

**Supervisor Trap:** Writing an adsorption denominator without showing the site balance or rate-determining step.

**Model Answer:** State adsorption equilibria, for example \(\theta_A=K_Ap_A\theta_*\) and dissociative hydrogen adsorption \(\theta_H=(K_Hp_{H_2})^{1/2}\theta_*\). Apply a site balance, such as \(\theta_*+\theta_A+\theta_H+\theta_{CO}=1\), solve for \(\theta_*\), then substitute the coverages into the proposed surface-reaction rate. Every exponent and denominator power follows from those assumptions. A fitted effective rate law does not establish that this elementary mechanism is true.

#### 7. Does CO necessarily increase ethylene selectivity?

**Supervisor Trap:** Treating competitive adsorption as proof of selective poisoning.

**Model Answer:** No. In Gobbo et al.'s shared-denominator model, \(r_A=k_A C_A C_H/D^3\) and \(r_E=k_E C_E C_H/D^3\), where \(D\) contains \(K_{CO}C_{CO}\). The ratio \(r_A/r_E=k_A C_A/(k_E C_E)\) cancels the CO term. That model predicts CO suppresses both rates equally at fixed reactant concentrations. A differential effect needs a different mechanism or independently supported rate equations. [4, p. 548, Eqs. 3–4; Schbib et al., 1996, p. 1502, Eqs. 24–25]

#### 8. Why might hydrogen modulation fail to outperform a steady feed?

**Supervisor Trap:** Repeating “it cannot” as a universal theorem.

**Model Answer:** The result depends on the objective and rate law. If the rate is linear in \(C_{H_2}\) at fixed state, a zero-mean sinusoid leaves the mean rate unchanged. If a static rate \(f(C_{H_2})\) is concave over the full cycle, Jensen's inequality gives \(\langle f(C_{H_2})\rangle\le f(\langle C_{H_2}\rangle)\). Neither condition proves the claim for a coupled adsorbing reactor with changing composition, temperature, and surface coverage. State the model assumptions, then compare cycle-averaged objective under equal mean feed and constraints.

#### 9. Can a common CO denominator improve a rate ratio?

**Supervisor Trap:** Assuming any poison term changes selectivity because it lowers activity.

**Model Answer:** If \(r_A=a_A/D(C_{CO})\) and \(r_E=a_E/D(C_{CO})\), then \(r_A/r_E=a_A/a_E\); the common factor cancels. CO can change a rate ratio only if its effect differs between pathways, changes local reactant concentrations or temperature, or enters the balances through another mechanism. Check the actual algebra before making a selectivity claim.

#### 10. How should the Arrhenius term be evaluated?

**Supervisor Trap:** Using the wrong energy units or treating a fitted pre-exponential as universal.

**Model Answer:** Use \(k(T)=k_0\exp[-E/(RT)]\), with \(R=8.31446261815324\ \mathrm{J\,mol^{-1}\,K^{-1}}\). Convert \(E\) to joules per mole and \(T\) to kelvin. Report the catalyst, rate normalization, pressure/composition range, and parameter source; values fitted to Pd/α-Al₂O₃ do not automatically transfer to PdAg.

### Cluster 3 — Numerical analysis and stiff solvers

#### 11. What does the stiffness ratio mean?

**Supervisor Trap:** Claiming a system is stiff because a solver is slow.

**Model Answer:** For a local linearization \(J=\partial f/\partial y\), widely separated stable eigenvalue time scales can produce a stiffness ratio such as \(\max|\Re\lambda_j|/\min|\Re\lambda_j|\) over decaying modes. The ratio depends on state, scaling, and the active modes. Solver step restrictions and convergence diagnostics provide practical evidence; the ratio alone does not select a solver.

#### 12. When would you choose BDF over explicit Runge–Kutta?

**Supervisor Trap:** Saying BDF is always better for reactor models.

**Model Answer:** Explicit Runge–Kutta is a reasonable candidate when the problem is nonstiff and the stability-limited step remains useful. BDF or Radau is a candidate when fast adsorption/reaction modes coexist with slow gas residence or thermal modes. Compare accuracy, steps, Jacobian work, and conservation at the required tolerances. Implicit methods do not correct an incorrect model or spatial discretization.

#### 13. Is an algebraic PSSA closure a dynamic surface model?

**Supervisor Trap:** Calling an instantaneous algebraic coverage calculation “surface memory.”

**Model Answer:** No. Under PSSA, \(\theta(t)\) is calculated from current gas conditions through an algebraic relation. It has no independent time derivative, so it cannot lag the gas. A dynamic model needs \(d\theta/dt=f(\theta,C,T)\) and supported kinetic constants. Keeping algebraic constraints inside an implicit solver may form a DAE; explicitly eliminating them can leave an ODE.

#### 14. When can centered differences oscillate?

**Supervisor Trap:** Believing second-order accuracy guarantees a physical transient.

**Model Answer:** For standard centered convection–diffusion differences, monotonicity requires \(Pe_{\Delta z}=u_i\Delta z/D_{ax}\le2\). Above that, coefficients can change sign and produce oscillations near sharp fronts. Upwind is first-order and diffusive; a limiter is a candidate, but I would verify its conservation, order, and grid sensitivity.

#### 15. What is a mass matrix, and why scale the equations?

**Supervisor Trap:** Treating every discretized model as \(\dot y=f(y)\) with a well-conditioned identity mass matrix.

**Model Answer:** A semidiscrete balance can be written \(M(y)\dot y=f(y)\), where \(M\) contains accumulation capacities such as bed void fractions and solid heat capacities. Small or badly scaled capacities can make the system numerically ill-conditioned. Scale states and residuals, inspect units and condition estimates, and retain algebraic constraints only when the solver formulation supports them.

### Cluster 4 — Periodic forcing and dynamic catalysis

#### 16. Which time scales should be compared?

**Supervisor Trap:** Assuming \(\tau_{ads}\ll\tau_{res}\) without defining either one.

**Model Answer:** Under constant velocity, \(\tau_{res}=L/u_i=\epsilon_bL/u_s\), which is 0.5–20 s under the mission's interstitial convention. Surface relaxation time must come from a mechanism or measurement. For forcing frequency \(\omega\), also compare \(\omega\tau_{ads}\) and \(\omega\tau_{res}\). No adsorption time is supplied for the target catalyst.

#### 17. What phase lag follows from one first-order surface relaxation mode?

**Supervisor Trap:** Calling any phase lag a resonance.

**Model Answer:** For \(\dot x=(x_{eq}(t)-x)/\tau\) and sinusoidal input, the transfer function is \(H(i\omega)=1/(1+i\omega\tau)\). The amplitude ratio is \([1+(\omega\tau)^2]^{-1/2}\), and phase is \(-\tan^{-1}(\omega\tau)\). This single-pole response attenuates with frequency and has no resonant peak.

#### 18. When can a periodic reactor show resonance?

**Supervisor Trap:** Tuning the period to \(\tau_{ads}\) and assuming a performance maximum must follow.

**Model Answer:** A forced response may peak only if the full linearized dynamics contain suitable interacting modes or if nonlinear kinetics and constraints create an optimum. A single stable first-order relaxation law has no resonance. Calculate the linearized transfer function or perform a validated nonlinear periodic sweep; distinguish a response-amplitude peak from a maximum in cycle-averaged selectivity or productivity.

#### 19. How should cycle-averaged selectivity be defined?

**Supervisor Trap:** Averaging instantaneous selectivity values when the thesis objective is a cycle yield.

**Model Answer:** Use a ratio of integrated molar rates, for example
\[
S_{C_2H_4}^{cycle}=
\frac{\int_0^{\tau_p}\dot n_{C_2H_4,formed}(t)\,dt}
{\int_0^{\tau_p}\dot n_{C_2H_2,consumed}(t)\,dt}.
\]
This is generally not equal to the time average of the instantaneous ratio. State the averaging window, periodic steady-state criterion, conversion constraint, and equal-mean-feed comparison.

#### 20. What evidence would support “CO modulation beats steady operation”?

**Supervisor Trap:** Inferring a process benefit from a coverage plot or one transient.

**Model Answer:** I would need a CO-dependent kinetic law with differential pathway effects, calibrated actuator and transport dynamics, a periodic steady state, and cycle-integrated selectivity/productivity at equal mean feed and within safety/conversion constraints. The present shared-denominator equations do not support a CO-induced rate-ratio change. The claim remains a hypothesis until a different mechanism or data support it.

### Cluster 5 — Experimental feasibility and validation

#### 21. How do GC and MS response times enter the measured outlet signal?

**Supervisor Trap:** Assigning a universal sampling lag to either instrument.

**Model Answer:** The measurement is a convolution of reactor outlet with sample-line, chromatographic, detector, and data-acquisition responses. A GC separates species but samples discretely; a mass spectrometer can provide faster compositional signals, but its inlet and detector still have response times. Calibrate the complete line with a tracer and report the instrument transfer function or measured step response.

#### 22. How does valve-to-bed dead volume distort a pulse?

**Supervisor Trap:** Treating the command time as the catalyst inlet time.

**Model Answer:** For ideal plug flow through dead volume \(V_d\) at volumetric flow \(Q\), the delay is \(\tau_d=V_d/Q\). Mixing and dispersion broaden the pulse, so a tank or measured transfer function may be more appropriate. Measure the concentration at the bed entrance or calibrate the full actuator–line path.

#### 23. How would you assess thermal inertia?

**Supervisor Trap:** Assuming isothermal operation because the feed is held at constant temperature.

**Model Answer:** A lumped estimate is \(\tau_T=C_{th}/(UA)\), where \(C_{th}\) is the effective gas-plus-solid heat capacity and \(UA\) the heat-transfer conductance for the chosen boundary. This estimate is valid only if internal gradients are small; check \(Bi_h\) using \(V/S\) or the declared characteristic length. Measure bed and wall temperature during forcing and compare \(\tau_T\) with the forcing period and gas residence time.

#### 24. What observations validate the transport model?

**Supervisor Trap:** Treating a good fit to one outlet trace as proof of the internal model.

**Model Answer:** Fit an inert tracer RTD across multiple flow rates to estimate \(D_{ax}\) or compare alternative flow models. Check pulse arrival, width, tails, and integrated recovery. Validate gas properties and bed geometry separately, then compare reactive data without refitting the tracer transport coefficient to conceal kinetic error.

#### 25. What should be reported before claiming a successful dynamic experiment?

**Supervisor Trap:** Showing periodic outlet oscillations without establishing actuator, thermal, and analytical bandwidth.

**Model Answer:** Report the commanded and measured bed-inlet waveform, flow and pressure, bed temperatures, catalyst identity and loading, sample-line volume, GC/MS response calibration, and repeated cycles at periodic steady state. Compare measured outlet with the instrument-filtered model prediction. If the sample system attenuates the forcing frequency, the reactor response is not identifiable from those data alone.

## References

1. P. V. Danckwerts, “Continuous flow systems: Distribution of residence times,” *Chemical Engineering Science* 2(1) (1953), 1–13. DOI: 10.1016/0009-2509(53)80001-1. The local primary PDF contains the article; the DOI record confirms issue and page range. Danckwerts establishes the RTD framework; the dispersed-bed boundary equations below are cited to the textbook source.
2. G. F. Froment, K. B. Bischoff, and J. De Wilde, *Chemical Reactor Analysis and Design*, 3rd ed., Wiley, 2011. Printed locators used here: pp. 157–159 (packed-bed mass/heat transfer), pp. 195–196 (sphere effectiveness), pp. 214–215 (Weisz–Prater), p. 508 (Ergun), pp. 559–561 (axial dispersion and packed-bed boundaries), and pp. 703–708 (axial-dispersion Peclet and neglect criterion). The book's bibliography lists K. B. Bischoff, *Chemical Engineering Science* 16 (1961), 131, among the boundary-condition discussions.
3. N. S. Schbib, M. A. García, C. E. Gígola, and A. F. Errazu, “Kinetics of Front-End Acetylene Hydrogenation in Ethylene Production,” *Industrial & Engineering Chemistry Research* 35 (1996), 1496–1505. Eq. 14 is on p. 1500; the selected kinetic equations are on p. 1502; Eq. 26 and the Weisz–Prater discussion are on p. 1504. DOI: 10.1021/ie950600k.
4. R. Gobbo, R. P. Soares, M. A. Lansarin, A. R. Secchi, and J. M. P. Ferreira, “Modeling, simulation, and optimization of a front-end system for acetylene hydrogenation reactors,” *Brazilian Journal of Chemical Engineering* 21 (2004), 545–556. Eqs. 1–4: p. 548; method-of-lines description: p. 550. DOI: 10.1590/s0104-66322004000400004.
5. C. Urmès, J.-M. Schweitzer, A. Cabiac, and Y. Schuurman, “Kinetic Study of the Selective Hydrogenation of Acetylene over Supported Palladium under Tail-End Conditions,” *Catalysts* 9 (2019), 180. DOI: 10.3390/catal9020180. Source-model scope is 0.05 wt.% Pd/α-Al₂O₃; it is not evidence for BEP PdAg or dynamic surface times.
6. NIST CODATA 2022, “molar gas constant,” exact value R = NA kB, https://physics.nist.gov/cgi-bin/cuu/Value?r%7Csearch_for=R. The Avogadro and Boltzmann constants are SI defining constants.
7. O. Levenspiel and K. B. Bischoff, “Patterns of Flow in Chemical Process Vessels,” *Advances in Chemical Engineering* 4, 95–198. Froment et al. cite the chapter as 1963; the publisher record dates it 1964. DOI: 10.1016/S0065-2377(08)60240-9.
