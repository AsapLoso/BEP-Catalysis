# Independent Adversarial Audit: BEP Catalysis Modeling Views

**Audit date:** 2026-10-26
**Scope:** Larsen (2024) PdAg kinetics; Schbib et al. (1996) Model III and isothermal-PFR transfer; the available packed-bed code and the proposed V4 CO-modulation model.
**Readiness judgment:** The transport balance and the existence of a large Schbib inhibition denominator are sound. The specific Larsen equation summary contains transcription errors and an unresolved equation/code discrepancy. The Schbib isothermal underprediction is reproducible under the Table 6 conditions, but its proposed “severe concentration-gradient” explanation contradicts the paper. The PdAg–CO dynamic synthesis is still a hypothesis: this checkout has no tracked V4 implementation with CO or dynamic CO coverage.

## Evidence and limits

- The Larsen thesis PDF is linked in the [GitHub branch](https://github.com/AsapLoso/BEP-Catalysis/blob/feat/larsen-pdag-benchmark/research/evidence/original/Larsen%20-%202024%20-%20Semihydrogenation%20of%20acetylene%20to%20ethylene%20with%20a%20PdAg%20catalyst.pdf). I used its [page-checked equation and condition transcription](https://github.com/AsapLoso/BEP-Catalysis/blob/feat/larsen-pdag-benchmark/research/evidence/transcriptions/larsen_2024_main_source_excerpts.md), its [Appendix E/F transcription](https://github.com/AsapLoso/BEP-Catalysis/blob/feat/larsen-pdag-benchmark/research/evidence/transcriptions/larsen_2024_appendix_E_F.md), the [visible input-row CSV](https://github.com/AsapLoso/BEP-Catalysis/blob/feat/larsen-pdag-benchmark/research/evidence/transcriptions/larsen_2024_appendix_F_visible_table_rows.csv), and the [Appendix F p. 86 render](https://github.com/AsapLoso/BEP-Catalysis/blob/feat/larsen-pdag-benchmark/notebooks/benchmarks/source_renders/appendix_pages/page-86.png), which I inspected directly. The transcription identifies the PDF as an uploaded copy; equivalence to an official June 2024 deposit is not established.
- Schbib and Gobbo source PDFs and text extractions are in [research/literature](../literature/README.md): [Schbib PDF](../literature/schbib_1996_front_end_acetylene_hydrogenation.pdf), [Schbib extraction](../literature/schbib_1996_extracted_text.txt), [Gobbo PDF](../literature/gobbo_2004_front_end_acetylene_hydrogenation.pdf), and [Gobbo extraction](../literature/gobbo_2004_extracted_text.txt). The article page and table locators below refer to those primary PDFs.
- Code-state observations refer to repository commit <code>7df73825a55070103c7bf379a3b034e1e2af4795</code> on <code>unified-reactor-model</code>. The V4 design document is a plan, not an implementation.
- “Not verified” means the underlying formula, code, data, or correction needed to establish the claim was not available in the reviewed source set. It does not imply that the claim is false.

## 1. Validated strengths

### Reactor balance and boundaries

The proposed balance

\[
\varepsilon_b\frac{\partial C_i}{\partial t}
=-u_s\frac{\partial C_i}{\partial z}
+D_{ax}\frac{\partial^2 C_i}{\partial z^2}
+\rho_b\sum_j\nu_{ij}r_j
\]

is dimensionally consistent if \(C_i\) is concentration per bed void volume, \(u_s\) is superficial velocity, \(D_{ax}\) is the bed-scale dispersion coefficient, \(\rho_b\) is catalyst mass per total bed volume, and \(r_j\) is per catalyst mass per time. Dividing through by \(\varepsilon_b\) gives the interstitial velocity \(u_s/\varepsilon_b\) and dispersion \(D_{ax}/\varepsilon_b\), as used in the available solver.

The stated Danckwerts inlet sign is correct:

\[
u_s C_{i,in}=u_s C_i(0^+)-D_{ax}\,\partial_z C_i(0^+).
\]

Together with zero dispersive flux at the outlet, this gives \(C_i(0)=C_{i,in}\) as \(D_{ax}\to0\). The axial Peclet definition \(Pe=u_sL/D_{ax}\) is also consistent with these conventions.

First-order upwind finite-volume transport is conservative at the semidiscrete level because internal face fluxes telescope. Reactions 1 and 2 conserve carbon and hydrogen when their stoichiometric source terms are applied consistently. That does not make a finite-tolerance time integration exact: the full transient balance must include boundary fluxes, and any adsorbed CO inventory must be included if CO is stored on the catalyst.

### Stiff integration and state meaning

The available [solver.py](../../notebooks/reference/v3/vendor/pbr/solver.py#L279) integrates gas concentration states with <code>solve_ivp</code>, defaulting to BDF. The gas accumulation term is therefore active in this implementation; it is not a steady-state gas balance. BDF is a reasonable candidate for a stiff method-of-lines system, subject to tolerance, mesh, and discontinuous-input checks.

### Schbib inhibition scale

Schbib Table 8 uses a cubed denominator containing CO and the other adsorbed species. Recalculation with ideal-gas concentrations confirms that it is very large at the stated feed. The power-of-three scaling is real; the particular condition and arithmetic in the established view need correction (Section 2).

## 2. Deficiencies and traps

### Pillar 1 — Larsen (2024): equation, fit and applicability

#### The established transcription is not the printed model

The page-checked transcription of PDF p. 43 / printed p. 37 gives:

\[
r_{1,raw}=
\frac{k_1K_Ap_AK_Hp_H}
{(1+K_Ap_A+K_Ep_E+K_Hp_H)^2},
\qquad
r_1=\frac{r_{1,raw}}{1+r_{1,raw}/r_{1,max}},
\]

\[
r_2=
\frac{k_2K_Ep_EK_Hp_H}
{(1+K_Ap_A+K_Ep_E)(1+K_{inh}p_A)^{n_{inh}}}.
\]

Thus the supplied “established view” differs in two places: it omits \(K_AK_H\) from the \(r_{1,raw}\) numerator, and it replaces the printed \(K_Hp_H\) term with \(\sqrt{K_Hp_H}\). The square root is not the transcription of Eq. 6.9. In Eq. 6.11, the first adsorption factor is printed to the **first power**.

Appendix F’s standard LHHW implementation (PDF p. 81 / printed p. 75) instead uses a **squared** adsorption factor for reaction 2. The p. 86 render is an optimizer/comparison function with six fitted variables (<code>k1</code>, <code>k2</code>, <code>K1</code>, <code>K2</code>, <code>Kinh</code>, <code>KH</code>); it contains neither <code>r1max</code> nor <code>ninh</code>. It therefore does not document the eight-parameter Figure 6.6 fit. These are distinct source versions, not a resolved typo: retain the printed Eq. 6.11 and the standard-code form as separate candidates until the final extended-model fitting code is found.

The current [Larsen2024Rate](../../notebooks/reference/v3/vendor/pbr/chemistry.py#L126) implementation includes the \(K_A,K_H\) numerator factors and the linear \(K_Hp_H\) term in reaction 1. For reaction 2 it follows the printed first-power adsorption factor. It has no CO term.

#### Figure 6.6 does not establish eight well-conditioned parameters

Figure 6.6 reports these values; units are not printed beside the vectors:

| Catalyst | \(k_1\) | \(k_2\) | \(r_{1,max}\) | \(K_A\) | \(K_H\) | \(K_E\) | \(K_{inh}\) | \(n_{inh}\) | \(N\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Pd₁Ag₀ | 6.470e12 | 9.020e11 | 0.007809 | 2.407e-03 | 1.820e-19 | 1.800e-05 | 0 | -1966.78 | 41 |
| Pd₂Ag₁ | 6.82925 | 0.79396 | 0.014413 | 1.891e-03 | 1.170e-06 | 9.930e-06 | 1.890e-07 | 10.5927 | 42 |
| Pd₃Ag₁ | 670.788 | 578.54 | 0.0383402 | 4.819e-05 | 2.378e-07 | 8.709e-08 | 1.176e-04 | 4.89665 | 41 |

No covariance matrix, scaled Jacobian, profile likelihood, parameter confidence interval, or bootstrap interval is reported in the reviewed material. The values therefore do not establish conditioning. In particular:

- For \(r_1=r_{raw}/(1+r_{raw}/r_{1,max})\), low-rate observations mainly identify \(k_1\) times the adsorption factors; high-rate observations mainly identify \(r_{1,max}\). Both can be identified only if the data span the transition between those regimes. A strong \(k_1\)–\(r_{1,max}\) trade-off is structurally expected, but its numerical correlation has not been measured.
- For Pd₁Ag₀, \(K_{inh}=0\) makes \((1+K_{inh}p_A)^{n_{inh}}=1\) for every \(n_{inh}\). The reported \(n_{inh}=-1966.78\) is consequently unidentifiable in that vector. The near-zero \(K_H\) raises a similar practical-identifiability concern for the hydrogen adsorption contribution.
- \(k_1\), \(K_A\), and \(K_H\) also enter the numerator as a product. Their identifiability depends on independently varied pressures and denominator effects, not simply on a low RMSE.

The source distinguishes temperature statements: abstract, Table 6.1 and Appendix F code say 100 °C and 1000 mbar; Section 4.2 says the reactor is maintained at 80 °C. The fitted vectors have no verified Arrhenius activation energies. These vectors cannot support temperature extrapolation beyond the fitted conditions, and the temperature basis itself needs resolution first.

#### No CO response is established by the Larsen study

Appendix F’s input table contains a CO column. Every fully visible Pd₀Ag and Pd₂Ag row and the nine visible Pd₃Ag head/tail rows have <code>vol.% CO = 0</code>. The Pd₃Ag display elides its middle rows, while Figure 6.6 reports \(N=41\); the complete fitted row mask is not shown. Thus the published material contains no visible positive CO co-feed case or CO kinetic fit and cannot validate CO inhibition; the CO value of every hidden Pd₃Ag row cannot be certified from the display.

Appendix F’s displayed fit code sets 373 K and 100,000 Pa; Section 4.2 instead says experiments were maintained at 80 °C. The complete visible input rows for Pd₀Ag (41) and Pd₂Ag (42) span C₂H₂ 0.5–2 vol%, C₂H₄ 10–40 vol%, H₂ 5–25 vol%, He 54.5–74.5 vol%, and CO 0 vol%. Only nine of the reported 77 Pd₃Ag input rows are visible; those span C₂H₂ 0.5–2%, C₂H₄ 20–30%, H₂ 10–20%, He 58–59%, and CO 0%. The source does not identify the mass-flow-controller reference state for its mL/min values. These are the reported static-feed bounds visible in the appendix, not evidence for CO modulation or temperature extrapolation.

The alloy “ensemble” and “d-band” explanations are plausible mechanistic hypotheses, but the kinetic fits alone do not separate geometric site isolation from electronic effects or other changes in surface composition and catalyst structure. State them as hypotheses unless supported by matched surface-composition, adsorption, or spectroscopic evidence.

### Pillar 2 — Schbib Model III, isothermal transfer and Gobbo

#### Denominator calculation and the condition mix-up

Schbib Table 8 (printed p. 1502) gives \(\log_{10} A_{CO}=13.6\), \(E_{CO}=9.95\) kcal mol⁻¹, \(K_{CO}\) in m³ kmol⁻¹, and

\[
D=1+(K_HC_H)^{1/2}+K_AC_A+K_EC_E+K_{Et}C_{Et}+K_{CO}C_{CO},
\qquad \text{rate denominator}=D^3.
\]

The hydrogen term is \(\sqrt{K_HC_H}\), not \(K_H\sqrt{C_H}\). Using Table 3 feed fractions, ideal-gas concentrations, and \(R=1.987204\times10^{-3}\) kcal mol⁻¹ K⁻¹:

| Case | \(T\) | \(P\) | \(K_{CO}\) (m³/kmol) | \(C_{CO}\) (kmol/m³) | \(K_{CO}C_{CO}\) | \(\sqrt{K_HC_{H2}}\) | Full \(D^3\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| User-stated condition | 328.15 K | 16.3 bar | 9.405e6 | 8.961e-5 | 843 | 393 | 1.894e9 |
| Schbib Table 6 | 341 K | 16 atm | 1.671e7 | 8.577e-5 | 1,434 | 709 | 9.864e9 |
| 341 K, 16.3 atm | 341 K | 16.3 atm | 1.671e7 | 8.738e-5 | 1,461 | 716 | 1.03e10 |

The denominator exceeds \(10^9\) in all three cases. But \(K_{CO}C_{CO}\approx1460\) belongs to approximately 341 K and 16.3 **atm**, not 328.15 K and 16.3 **bar**. The stated \(3.1\times10^9\) is approximately \(1460^3\) and omits the hydrogen adsorption term; the full denominator cube at the 341 K / 16 atm Table 6 condition is about \(9.9\times10^9\).

I also independently integrated the Table 8 isothermal, pseudohomogeneous PFR at Table 6’s 150 ppm CO, 341 K, 16 atm and \(SV=100\) cm³(STP) g-cat⁻¹ min⁻¹. With Table 3 feed, 1 g catalyst, 0 °C / 1 atm for STP, and the printed Table 8 rate equations, RK4 with 1,000 versus 10,000 catalyst-mass steps gives \(X_{C2H2}=0.84037\%\) in both runs. At the user-stated 328.15 K / 16.3 bar it gives \(0.34527\%\). This reproduces the claimed approximately 0.85% **at the Table 6 temperature and pressure**, not at 328.15 K. The Table 6 measurements at 341 K and 16 atm are 98.31% C₂H₂ conversion and 10.45% C₂H₄ conversion (Schbib Table 6, printed p. 1499).

The same isothermal calculation gives \(X_{C2H4}=-0.00875\%\) at Table 6 conditions, i.e. slight net ethylene generation, rather than the measured 10.45% ethylene disappearance. This is a reproducible model/data mismatch, not evidence that the author-shared correction has been reproduced. Details and calculation assumptions are in [modeling_audit_calculations.py](./modeling_audit_calculations.py).

#### The proposed Model III root cause overstates concentration gradients

The paper says Model III includes gas–particle concentration and temperature differences. It then states that calculated concentration gradients inside particles were negligible for all runs, while the temperature differences and axial hot spot were significant (Schbib, printed pp. 1502–1503). That directly contradicts the claim that severe intraparticle concentration gradients offset the cubed denominator. Thermal gradients are a plausible contributor because the fitted activation energies are large, but the source and the calculation here do not isolate how much of the conversion gap they explain. Reproducing the gap with an isothermal PFR does not validate a single root cause; the coupled non-isothermal Model III is needed for that attribution.

#### Gobbo is not a unit-conversion workaround

The relevant values are in Gobbo et al. Table 1, not Table 2 (Table 2 reports deactivation parameters). Gobbo minus Schbib log-pre-exponent differences are −3.7 (acetylene), −3.3 (ethylene), −3.0 (hydrogen), and −3.4 (CO). The nearby text says acetylene/ethylene pre-exponents were adapted to industrial plant data, and that the fitted parameters may have no physical meaning. This is evidence of an empirical plant-data refit, not an author-stated SI conversion or correction for Model III denominator scaling. A pure conversion from per-gram to per-kilogram rate basis would shift a per-catalyst-mass rate coefficient by +3 log units, not −3.5; the hydrogen and CO adsorption constants also shift despite having the same m³/kmol units in both tables.

#### The author-shared correction remains unverified

No correction equation, parameter set, source file, or output was found in the reviewed workspace or repository search. I cannot determine whether it over-predicts \(r_2\) or how it produces the reported outlet response. Also, negative *net ethylene production* is not automatically unphysical: Schbib’s feed contains about 44 mol% C₂H₄, and the measured Table 6 case itself has 10.45% ethylene conversion. With only reactions 1 and 2,

\[
F_{E,out}-F_{E,in}=\int_0^{W_{cat}}(r_1-r_2)\,dW.
\]

Net disappearance occurs when the integrated \(r_2\) extent exceeds \(r_1\); it is physically possible with ethylene in the feed. Diagnose over-predicted \(r_2\) by comparing the correction’s ethylene conversion and both reaction extents with the measured Table 6 values and carbon balance. “Unphysical” would require a stronger violation, such as negative absolute concentration or an impossible elemental balance.

### Pillar 3 — spatial discretization, transients and PSSA

#### First-order upwind adds material numerical dispersion

For method-of-lines first-order upwind, the leading modified-equation estimate is \(D_{num}\simeq u_s\Delta z/2\), so

\[
\frac{D_{num}}{D_{ax}}\simeq\frac{Pe}{2N_z}.
\]

| \(Pe\) | \(N_z=50\) | \(N_z=100\) |
|---:|---:|---:|
| 17 | 0.17 \(D_{ax}\) | 0.085 \(D_{ax}\) |
| 400 | 4 \(D_{ax}\) | 2 \(D_{ax}\) |

At the high-\(Pe\) end, first-order upwind would dominate the physical dispersion on 50–100 cells. To keep this estimate below \(D_{ax}\) at \(Pe=400\) requires \(N_z\ge200\); below \(0.1D_{ax}\) requires \(N_z\ge2000\). These are estimates, not a substitute for grid convergence; a bounded higher-order flux is a candidate to evaluate.

#### Conservation and square-wave switching

The spatial finite-volume flux difference conserves each gas species across internal faces. Carbon/hydrogen conservation follows if the reaction stoichiometry and catalyst-mass basis are consistent. The time integrator only satisfies the corresponding transient control-volume balance to numerical tolerance. A square wave defined with <code>sgn(sin(...))</code> is discontinuous at every half-period; integrate separately between known switch times and restart from the boundary state at each switch. Do not let an adaptive BDF step straddle an unannounced discontinuity. Keep \(C_{CO,mean}\ge|\Delta C_{CO}|\) so the prescribed inlet never becomes negative.

The current [solver RHS](../../notebooks/reference/v3/vendor/pbr/solver.py#L306) injects the inlet through its advective face and uses zero-gradient dispersive ghost values at both ends. In the divided concentration equation the inlet flux is (u_s/epsilon_b) C_in, equivalent to u_s C_in in the original bed-volume balance, with zero dispersive outlet flux. However, the separate <code>inlet_flux</code>/<code>outflow</code> methods in [closures.py](../../notebooks/reference/v3/vendor/pbr/closures.py#L65) are documented as molar fluxes while accepting no velocity; the dispersive implementation also combines concentration with \(D_{ax}\partial_z C\), which is not dimensionally a flux. Those methods are not called by the current solver, but should be corrected before using them as the V4 boundary API.

#### Gas PSSA and surface PSSA are separate decisions

The available V3 <code>rhs</code> integrates gas storage. It supports four gases—H₂, C₂H₂, C₂H₄, C₂H₆—and has no CO species ([species.py](../../notebooks/reference/v3/vendor/pbr/species.py#L19)). Its surface options include algebraic equilibrium and a generic relaxation law \(d\theta/dt=(\theta_{ss}-\theta)/\tau\); the latter explicitly treats \(\tau\) as an unsourced assumption ([closures.py](../../notebooks/reference/v3/vendor/pbr/closures.py#L328), [closures.py](../../notebooks/reference/v3/vendor/pbr/closures.py#L352)). It is not an elementary-step CO adsorption/desorption model.

Low gas residence time alone cannot justify surface PSSA. PSSA is defensible only if a measured or mechanistically calculated surface relaxation time is much shorter than the shortest forcing timescale and the relevant gas/reaction timescales. If the proposed result relies on delayed CO coverage, phase lag, or a surface “memory,” the coverage state and its gas-phase CO sink/source must be dynamically integrated or replaced by a reduced model calibrated against transient data.

Finally, the currently reviewed checkout contains the V3 engine under <code>notebooks/reference/v3/vendor/pbr</code>; the [V4 reactor document](../wayfinder/bep_v4_reactor_model.md) describes planned work, and [notebooks/reference/v4/](../../notebooks/reference/v4/README.md) records that no V4 implementation is present. Do not present the V4 CO/PSSA claims as code-verified results.

### Pillar 4 — PdAg + CO and periodic Pareto claims

- **Alloy transfer:** Schbib’s CO constant comes from a commercial 0.04 wt% Pd catalyst on alumina, not the PdAg catalysts in Larsen. It is not a measured PdAg equilibrium constant. Alloy surface composition, Pd ensemble size, segregation, support and coverage can all change adsorption. A qualitative d-band argument alone cannot establish either the sign or size of the \(K_{CO}\) change on Pd₂Ag₁. Treat the pure-Pd value as a sensitivity reference, not an alloy parameter.
- **Model form:** Schbib Table 8 places the same CO-dependent denominator under acetylene and ethylene rates, and the paper says CO above 150 ppm affects their rates to a similar extent. Adding the same <code>K_CO p_CO</code> term to both Larsen laws therefore imposes common-mode inhibition at fixed state; it does not by itself establish selective suppression of <code>r_2</code>. There is also a direct unit mismatch: Schbib <code>K_CO</code> is in m³/kmol and multiplies <code>C_CO</code> in kmol/m³, whereas the proposed Larsen denominator is pressure-based. If the Larsen terms are pressure-based, convert the concentration-based constant at each temperature using <code>K_p = K_c/(R T)</code>; do not multiply a concentration-based constant by <code>p_CO</code>. Figure 6.6 does not establish all adsorption-constant units. Finally, the two Larsen equations have different denominator structures; a combined denominator needs a stated site balance and adsorption stoichiometry or should be labelled a phenomenological sensitivity model.
- **No dynamic adsorption from an algebraic term:** Adding \(K_{CO}p_{CO}\) to an instantaneous rate denominator creates no independent \(\theta_{CO}\), no adsorption/desorption time constant, and no CO inventory in the gas balance. A gas square wave may convect and disperse, but dynamic surface capacitance cannot appear unless CO adsorption is a state with a coupled material balance.
- **Phase and damping:** In an ideal nondispersive plug-flow limit a square wave is delayed by the residence time and keeps its shape. Axial dispersion and finite-rate adsorption attenuate its high-frequency components. For a linearized first-order surface relaxation, the response magnitude scales as \(1/\sqrt{1+(\omega\tau_{ads})^2}\) and phase lag as \(-\arctan(\omega\tau_{ads})\), where \(\omega=2\pi/\tau_{period}\). No \(D_{ax}\), period, alloy-specific adsorption time, or CO capacity is established here, so a numerical claim that 0.1–2 s bed residence smooths the input to a sinusoid is unsupported.
- **Pareto test:** Run to a periodic limit cycle after transients. Compute conversion and selectivity from cycle-integrated outlet/inlet molar flows using the same response definitions and carbon balance as the experiment; do not take an unweighted average of instantaneous selectivity. Compare against the globally optimized steady-state nondominated frontier under identical catalyst, temperature, pressure, feed, space velocity, CO admissible range, and the same mean CO dose. If claiming advantage over any static/time-sharing policy, also compare against the feasible convex hull of steady-state points at the same mean CO resource. A dynamic point must lie outside that benchmark by more than solver, mesh, and parameter uncertainty.

## 3. Actionable recommendations before supervisor review

1. **Separate source variants.** Preserve the printed Larsen Eq. 6.11 first-power form, Appendix F standard-model squared form, and any later extended-model implementation as distinct. Obtain the final eight-parameter fitting function, bounds, source units, and catalyst-specific row masks before calling Figure 6.6 reproduced.
2. **Quantify fit identifiability.** Refit only after the source law is fixed. Report a scaled sensitivity/Jacobian SVD, parameter profiles or bootstrap intervals, bounds-hit diagnostics, and the \(k_1\)–\(r_{1,max}\) correlation. Mark \(n_{inh}\) unidentifiable for Pd₁Ag₀ when \(K_{inh}=0\). Do not extrapolate the Figure 6.6 vectors in temperature without fitted activation energies and resolved source temperature.
3. **Correct the Schbib benchmark statement.** Use 341 K and 16 atm for the Table 6 comparison; show the full \(D^3\approx9.9\times10^9\) and the independently reproduced isothermal \(X_{C2H2}\approx0.84\%\). Describe this as an isothermal transfer failure, not as evidence of severe intraparticle concentration gradients. Reproduce the non-isothermal Model III before assigning the gap to heat transfer or any other single cause.
4. **Keep the author-shared correction open.** Do not report its ethylene behavior until its exact equation/code, feed basis, units, and run conditions are available. Compare integrated \(r_1,r_2\) extents, C₂H₄ conversion, and elemental balance against Table 6; a negative net ethylene yield alone is not a physical impossibility.
5. **Do not transfer \(K_{CO}\) silently.** Add a no-CO baseline and a transparent multiplicative sensitivity sweep of the Schbib value (for example, factors \(10^{-2}\)–\(10^2\), explicitly labeled exploratory). Mark alloy \(K_{CO}\) and \(\tau_{ads}\) as unknown until supported by PdAg-specific measurement or a clearly sourced microkinetic model.
6. **Build the actual CO model before discussing a traveling surface wave.** Add CO to the gas state, add a site-balanced dynamic CO coverage with adsorption/desorption kinetics, and couple its accumulation to the gas balance. If only an algebraic inhibition term is justified, describe it as instantaneous inhibition and make no surface-lag claim.
7. **Audit numerical transport at the intended regime.** Use conservative face fluxes; align solver segments with every square-wave edge; compare first-order upwind with a bounded higher-order candidate; report \(D_{num}/D_{ax}\), mesh convergence, solver tolerance convergence, non-negativity and integrated carbon/hydrogen residuals. Fix the dimensionally inconsistent boundary helper interface before wiring it into V4.
8. **Gate the Pareto claim.** Define the cycle metrics and CO resource constraint before parameter sweeps. Optimize the static frontier on the same basis, then accept a periodic “break” only if a converged limit-cycle point beats that frontier (and, if relevant, its feasible time-sharing hull) beyond combined numerical and parameter uncertainty.

## Reproducibility receipt

- **Audited code revision:** <code>7df73825a55070103c7bf379a3b034e1e2af4795</code>, branch <code>unified-reactor-model</code>.
- **Numerical environment:** Windows 10 build 19045; configured Conda Python 3.13.15; calculation script uses only the Python standard library; no packages installed or dependency files changed.
- **Command:** <code>&amp; "$env:USERPROFILE\tudelft-conda\python.exe" research/audits/modeling_audit_calculations.py</code> from the repository root. The concrete profile path used by this machine is omitted from this tracked report.
- **PFR calculation:** RK4 over 1 g catalyst using 1,000 and 10,000 mass increments; their acetylene-conversion results differ by less than \(10^{-12}\) percentage points. Isothermal ideal gas, constant total pressure and temperature, Table 3 feed, Table 8 Arrhenius parameters and kinetics, 100 cm³(STP) g-cat⁻¹ min⁻¹, STP interpreted as 0 °C and 1 atm. The unreported 0.125 mol% rounded feed balance is treated as inert.
- **Denominator and grid calculations:** direct deterministic arithmetic from the printed Arrhenius parameters and supplied \(Pe,N_z\); no reactor solver was used for those calculations.
- **Scope limit:** this receipt documents an independent arithmetic/PFR reproduction. It is not an experimental validation or a reproduction of Schbib’s coupled Model III. No repository test suite was run.
