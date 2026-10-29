# Deep dive F — What do our balance equations and state vectors *really* represent?

**14 October 2026** · Parent: [A–M index, F](../RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · Background [C reaction network](C_reaction_mechanism_2026-10-14.md), [D rate conventions](D_kinetic_parameters_identifiability_2026-10-14.md), [E reactor/transport scope](E_operating_regime_transport_2026-10-14.md) · Presentation idea [01 — concentrations to state-space](../sub-stories/01_three_concentrations_to_state_space.md).

**[STATUS] Documented model-structure/code audit, NOT new scientific validation, code fix, executed conservation test or proof of experimental periodic gain.** Preserve two distinct scientific models. A–M is not slide order; presentation-worthy part appears in §F7.

## F0. Executive result

**[FACT: code]** The old scaffold carries **four bulk-gas species, four radially resolved pore-gas species and three dynamic site coverages**. It allocates **1,480 solver entries** on a 20×10 spatial grid. The new source-backed reacting vertical slice has a **240-entry uniform-pellet PSSA baseline** (60 axial cells × four gas components) and an opt-in **2,400-entry radially resolved PSSA** branch (60 axial cells × (four bulk + 9×four pore fields)). A third experimental draft introduces **five dynamic coverages**, but **has not been integrated as a calibrated full reactor**. These differences are *physical model choices*, not just numerical sizes.

**[DERIVATION / scientific concern]** When pore gas and surface storage are actual dynamical inventories, the bulk↔pellet transfer must balance through **the interfacial flux**, *not* by independently adding the same pellet's chemical gas rate into both inventories. Both radial code paths currently put an intrapellet reaction source into the pore RHS **and** an independently volume-averaged reaction source into the bulk RHS. That is a potential **double-booking of a compartment source in the combined inventory**, distinct from the old audit's rejected accusation of duplicate **site-density \(C_t\)** multiplication. No fully coupled atom-/mole-conservation execution or corrected flux implementation was completed here. See §F4–F5 and explicit conservation acceptance tests.

**[DECISION]** This is a meaningful *next-model verification question* and possible scientific talking point, not permission to announce that a complete model is physically validated or fix the model inside the presentation workflow.

## F1. Conservation ledger and physically consistent reference equations

Use clear conventions to avoid quietly mixing a *pore-void concentration* with a *volume-of-particle concentration* or a *per-site turnover* with a *per-mass* reaction rate.

| Symbol | Meaning | Units |
|---|---|---|
| \(C_{b,i}(z,t)\) | gas species \(i\) concentration per gas **void** volume in bed | mol/m³ gas |
| \(c_{p,i}(z,r,t)\) | gas species \(i\) concentration per **pore gas** volume | mol/m³ pore gas |
| \(\theta_j(z,r,t)\) | occupied-site fraction, vacancy \(\theta_* = 1-\sum_j\theta_j\) | dimensionless |
| \(\epsilon_b,\epsilon_p\) | bed void fraction and intraparticle pore void fraction | dimensionless |
| \(u_s\), \(u_i=u_s/\epsilon_b\) | superficial and interstitial axial velocity | m/s |
| \(D_{\mathrm{eff},i}\) | effective **particle-area** pore diffusivity used in \(\epsilon_p\dot c=D_\mathrm{eff}\nabla^2c+\cdots\) | m²/s |
| \(\rho_p\) | assumed catalyst mass per particle-volume basis | kg catalyst/m³ particle |
| \(N_S\) or \(C_t\) | amount of catalytic sites per catalyst mass | mol sites/kg catalyst |
| \(\hat q_i\) | gas production rate per mol sites from elementary steps | mol gas/(mol sites·s) = s⁻¹ |
| \(q_i=N_S\hat q_i\) | gas source per catalyst mass | mol/(kg catalyst·s) |
| \(a_p=3/R_p\) | particle outer interfacial area per particle volume, spherical assumption | m⁻¹ |
| \(j_i^{\rm in}=D_{\mathrm{eff},i}(\partial_r c_{p,i})_{R_p}\) | **inward** molar flux at particle surface, from bed gas to pore gas (signed; positive consumption-driven inward) | mol/(m²·s) |

For an ideal, isothermal, constant-\(\epsilon_b\), constant-density particle, zero-film-resistance *but radially resolved*, physically consistent **gas inventory** balances are

\[
\epsilon_b\partial_t C_{b,i}+u_s\partial_z C_{b,i}
=- (1-\epsilon_b)\,a_p\, j_i^{\rm in},
\]

\[
\epsilon_p\partial_t c_{p,i}
= \frac{D_{\mathrm{eff},i}}{r^2}\partial_r\!\left(r^2\partial_r c_{p,i}\right)+\rho_p q_i(c_p,\theta),
\]

with \(\partial_r c_p|_{r=0}=0\) and \(c_p(R_p)=C_b\) (Dirichlet interface; assumes negligible external film). A nonzero-film formulation would solve the coupled boundary relation \(j_i^{\rm in}=k_{g,i}(C_{b,i}-c_{p,i}(R_p))\), not impose both an unrelated fixed surface value and an independently unrelated film flux. **The bulk exchange term is the boundary flux, not a second chemical production term.**

Integrating the pore equation over a sphere gives

\[
\epsilon_p\partial_t\bar c_{p,i}
=a_p j_i^{\rm in}+\rho_p\bar q_i.
\]

Summing with the bed balance (including particle volume fraction \(1-\epsilon_b\)) eliminates **the interface flux exactly**:

\[
\partial_t\bigl[\epsilon_b C_{b,i}
+(1-\epsilon_b)\epsilon_p\bar c_{p,i}\bigr]
+u_s\partial_z C_{b,i}
=(1-\epsilon_b)\rho_p\bar q_i.
\]

This is the appropriate species-level **gas inventory** statement. For adsorption/desorption, gas species are **not conserved individually** until you include **site storage**, and for hydrogenation the gas species are connected through reaction stoichiometry. For each conserved element \(\alpha\in\{C,H\}\), add the site inventory

\[
(1-\epsilon_b)\rho_p N_S\sum_j n_{\alpha,j}\bar\theta_j
\]

to the storage, and require locally

\[
\sum_i n_{\alpha,i}q_i+N_S\sum_j n_{\alpha,j}\,\partial_t\theta_j =0
\]

when the chemistry is a closed, site-conserving elementary network. With published **PSSA** gas rates the site derivative is *not an independently available dynamical source*; the intended approximation is that its rapid storage changes are negligible on the resolved timescale.

**[ASSUMPTIONS]** These are **reference conservation equations**, not a claim that the current code enforces their discrete integral identities. \(\rho_p\) is defined on a particle-volume basis here; a skeletal-density input needs a converted coefficient. The source kinetic units and model transport conventions must be checked before a numerical assertion.

## F2. Two annotated closure schematics (physics, not code-success claims)

### 1 — Old ambitious transient-surface scaffold, 11 physical field types

\`\`\`text
prescribed inlet u(t) (CURRENT OLD CODE: constant C_inlet)
                    |
                    v
  bulk gas C_b(z,t): 4 fields — axial advection
                    ||  c_p(Rp)=C_b (external film omitted)
                    vv
  pore gas c_p(z,r,t): 4 fields — radial diffusion
                    ||  adsorption/desorption and chemistry
                    vv
  surface θ(z,r,t): 3 coverages + algebraic vacancy θ*
                    |
           kinetics q_gas, dθ/dt
                    |
  NEED CONSERVATIVE CLOSURE: interfacial pore flux -> bulk exchange
\`\`\`

- [FACT: old code](../../3_Model/c2h2_hydrogenation_transient_model.py) builds 80 bulk, 800 pore and 600 coverage coordinates = **1,480 allocated**.
- [FACT: old RHS] The outer **20×4 = 80 pore-shell** entries are forcibly set from \(C_b\) by an *in-place mutation of the caller's solver state* and their RHS entries are zero. The **20×3 = 60 coverage-shell** entries also get zero RHS because the radial reaction loop skips the shell. Thus only **80 bulk + (20×9×4 = 720) interior pore + (20×9×3 = 540) interior θ = 1,340 entries** can evolve via assigned derivatives; **140 allocated shell entries are fixed/artificial or algebraically constrained**, not 140 independent physical internal modes. This count does **not** prove 1,340 independent observable chemical degrees of freedom.
- [FACT: old code] Three θ fields: H*, C₂H₂*, C₂H₄*. \(\theta_*=1-\sum\theta\). All eight kinetic prefactors default to 0 and stored \(E_a\) values are ignored, so the model's current chemistry has **no active reaction**.
- [FACT: old code] The source terms are constructed from per-site turnover-like rates (units **1/s**) and multiplied by \(C_t\) with \(\rho_p/\epsilon_p\) or \(\rho_p(1-\epsilon_b)/\epsilon_b\). **Do not falsely call that a double \(C_t\) multiplication**: [old model state, D5](../../3_Model/state.md) explicitly retracted that accusation. Whether the entire two-compartment inventory is conservative is a *separate* question.
- [FACT: old audit] Centre diffusion factor half the exact spherical-centre value, shell θ derivatives missing, first-order radial quadrature biases uniform rates ~16% on the grid and RHS state mutation; refer to [defect receipt/register](../../3_Model/state.md), not an unverified code run.

### 2 — New source-backed, gas-reacting/PSSA closure

\`\`\`text
known 2019 Table-5 composite kinetics q_i(C,T)   (NO θ ODE)
                           |
         +-----------------+------------------+
         |                                    |
  baseline: uniform pellet                 optional resolved-pore branch
  only C_b(z,t), 4 gas species             C_b(z,t) + c_p(z,r,t)
  60 axial cells = 240 coords              60*(4 + 9*4) = 2,400 coords
  bulk source +rho_b/eps_b q               radial diffusion + reaction
  no independent pore inventory           shell concentration pinned to bulk
         |                                    |
         +-----------------+------------------+
                           v
                   outlet C_b(L,t)
\`\`\`

- [FACT: branch code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py): baseline \`resolve_radial=False\` has \(\dot C_b=-u_i\partial_z C_b+\rho_p(1-\epsilon_b)\,q/\epsilon_b\), per the **single homogenized** gas inventory assumption.
- When \`resolve_radial=True\`, code creates \`dc_part += (rho_p/eps_p) * R_gas\` **and** \`dc_bulk += rho_p*(1-eps_b)/eps_b * avg_R\`. It imposes shell \`pin=1e12\` as a **rapid relaxation ODE**, rather than a mathematically eliminated algebraic degree of freedom or a directly calculated interfacial flux.
- The new resolved version therefore requires an explicit **conservation residual check under time-dependent pore storage**, even when steady pore gradients appear small. The code's own comments in different places alternately mention an older \(\phi\approx26.98\) and a corrected \(\phi\approx0.121\); E found a more recent receipt reports \(\phi\approx0.0853\). Do not use any as a global physical validation without reconciling definitions.
- The current branch imports \`pbr/\` externally, not supplied by the public sibling default branch; it cannot be declared independently runnable from the checked GitHub snapshot alone.

### Separate trial mechanism — NOT an accomplished third reactor

[Draft experiment/non-PSSA PR #3](https://github.com/AsapLoso/project-management-agents/pull/3) defines **5 occupied surface states** H*, C₂H₂*, C₂H₃*, C₂H₄*, C₂H₅* and \(\theta_*\) algebraically, **10 elementary kinetic coefficients plus a site density**, and local gas/site rates. [Code](https://github.com/AsapLoso/project-management-agents/blob/experiment/non-pssa-surface-2026-10-14/Academics/BEP/Catalysis/3_Model/transient_surface_kinetics.py). It computes \`inventory_residual\` for C/H and has a coherent **local** atom bookkeeping interface, but parameters are NOT supplied and it is **not yet a validated coupled PBR**. Calling it a replication of Urmès 2022 or a completed transient simulation is unwarranted.

## F3. What 'memory' really means in the state-space argument

\[
\dot{\mathbf x}(t)=F(\mathbf x(t),\mathbf u(t);\mathbf p),\qquad
\mathbf y(t)=H(\mathbf x(t),\mathbf p).
\]

- Four measured/estimated *bulk* concentrations can change over time and can store gas through axial advection even if the **surface is PSSA**. A time-dependent **input** \(\mathbf u(t)\) does **not** itself constitute a hidden catalyst state; the number of independent inlet controls is *not* the number of gas chemical species.
- Additional **pore concentrations** preserve spatial intraparticle delay/memory when gradients matter.
- Additional **site occupancies θ** preserve kinetic surface history. Two different θ states can, in a valid non-PSSA rate law, yield different future rates even with the **same instantaneous bulk concentrations**. The **current zero-rate legacy scaffold cannot demonstrate this experimentally or through an active chemistry simulation**.
- Once all *necessary* internal fields are included and a suitable constitutive closure is chosen, the ideal model is **Markovian in its state**: future evolution is determined by present \(\mathbf x\), inputs and parameters, not by the entire observed input-output past. This **does not** imply every chosen state model is automatically physically complete or validated.
- For **constant input** an autonomous idealization is possible. Under **periodically prescribed inlet**, \(F\) can remain time-invariant in formulation but the *forced trajectory* is time-dependent. Fitting parameters in an open-loop forced experiment is **not** automatically closed-loop feedback control.

## F4. The key local conservation trap — distinct from the \(C_t\) issue

### Old radial RHS as written

\[
\dot c_p=(D_{\rm eff}/\epsilon_p)\mathcal L_r c_p
+(\rho_p C_t/\epsilon_p)\hat q_i,
\]
\[
\dot C_b=-u_i\,\partial_z C_b
+\frac{\rho_p(1-\epsilon_b)C_t}{\epsilon_b}
\langle\hat q_i\rangle_p.
\]

With actual time-dependent **pore gas inventory**, the second equation is a **lumped reaction source** where an **interface exchange flux** should act. Adding the **separate** pore inventory to the bulk inventory then includes chemical exchange both as a pore source and as an independent bulk source; the interfacial flux that ought to cancel is not explicitly present. Shell state mutation further prevents treating the code's numerical trajectory as a faithful solution of a continuous coupled balance.

**Scope:** Since all \(k\) are zero by default, this problem is invisible in the shipped pure-transport chemistry and cannot be asserted as a *measured* failed conservation residual without a nonzero kinetics test. In a quasi-steady-pore approximation, one can sometimes eliminate pore storage and replace the bulk transfer by \(\rho_p\bar q_i\) using \(\nabla\cdot J +\rho_p q=0\), but **one must then not separately retain the pore accumulation as another independent gas inventory**. Do not confuse an approximation with a conservative time-dependent two-compartment derivation.

### New optional radial RHS

\[
\dot c_p=(D_{\rm eff}/\epsilon_p)\mathcal L_r c_p
+(\rho_p/\epsilon_p)q_i,\qquad
\dot C_b=-u_i\,\partial_z C_b+
\frac{\rho_p(1-\epsilon_b)}{\epsilon_b}\bar q_i.
\]

Same **closure question**: the code evolves pore storage but couples bulk to a **pellet-averaged reaction rate**, not \(j_i^{\rm in}\). Additionally the artificially imposed \(10^{12}\,\mathrm s^{-1}\) shell relaxation injects a fast numerical boundary exchange without using the **same and opposite** flux in the bulk RHS. The default **uniform** closure is *different*: it has only a bulk gas inventory, and a direct volume-normalized reaction source is a legitimate reduced/pseudo-homogeneous balance.

**Critical caveat:** This does NOT demonstrate \`C_t\` is counted twice. It demonstrates an **unresolved conservation/boundary closure** in the resolved *two-inventory* implementations. A conservative finite-volume implementation or explicit volume-integral residual test is needed to classify and quantify the defect.

## F5. Numerical and scientific acceptance checks to hand off

1. **Per-element, local elementary rates:** for any non-PSSA \(q_i,\dot\theta\), verify \(\sum_i n_{C,i}q_i + N_S\sum_j n_{C,j}\dot\theta_j=0\) and similarly for H with correct site occupancy atom counts. For steady/PSSA kinetics use the **gas reaction stoichiometry** directly. In both, verify \(\theta_*+\sum\theta=1\), bounds \([0,1]\) and nonnegative gas concentrations.
2. **Transport-only invariance:** with reaction sources suppressed, no flux through closed boundaries and equal equilibrium initial conditions, inventories remain stable; a prescribed inlet/outlet must balance total axial molar flux.
3. **Conservative radial exchange:** construct a radial finite-volume interface-flux discretisation: integrate pore accumulation + site inventory and compare the **negative** corresponding bulk surface flux; the discrete sum should cancel interface terms to numerical tolerances. This is the decisive test missing from the present two-inventory RHS.
4. **Rates and normalization:** check \(\hat q\) per mol sites vs \(q\) per kg catalyst vs volumetric \( \rho_p q\) with a unit ledger. **Neither a missing nor a duplicated \(C_t\)** is automatically implied by using the same physical reaction mechanism in bulk and pore algebra — it depends on the chosen reduced balance.
5. **Boundary as algebraic constraint:** eliminate the fixed \(c_p(R_p)=C_b\) shell node, or treat the boundary as a genuinely consistent DAE/exchange formulation rather than mutating \`y\` or imposing an unanalysed \(10^{12}\) penalty. Check true independent state count after doing so.
6. **Reacting PSSA / changing total moles:** hydrogenation reduces gas mole count; constant \(P,T,u\) with a prescribed inert fraction can be an approximation, but total-continuity consistency must be justified before high-conversion predictions. Inert Ar is part of feed normalization even if not an active ODE state.
7. **Repeatable proof:** test with explicitly nonzero, dimensionally consistent kinetics in an isolated harness, compare integrated carbon/hydrogen residuals and source-sink equality, store inputs and numerical receipt. Do not invent kinetics simply to get a green scientific fit; illustrative test constants may be used only in a clearly-labelled mathematical invariant unit test.

These are **requests for future verification**, not an instruction that this letter should modify the solver.

## F6. What is and is not a result

**[FACT: code]** The field counts, current RHS expressions, shell boundary implementation, 2019 PSSA closure, draft five-coverage local module and old audit defects are directly inspectable from the linked repository code. The existing preliminary 24/24 source audit is **source transcription**, not conservation verification.

**[DERIVED]** Conservation equations and the consequent flux-coupling condition are mathematical derivations under the stated model conventions.

**[UNVERIFIED]** The magnitude and experimentally material consequence of the resolved RHS conservation error, corrected reaction transients, source-to-new-catalyst kinetics transfer, claimed gain under periodic operation, and fitting benefits. The current GitHub files do **not** supply a fresh, independently executable full test receipt for those claims in this F dive.

## F7. Presentation-selection note (for parallel Work session)

**Strong candidate for ONE clear visual, not a lecture on equations:** "From concentrations to *where the reactor stores history*."

- Show three layers: **bulk** \(C_b(z,t)\) → **pellet pores** \(c_p(z,r,t)\) → **occupied sites** \(\theta(z,r,t)\), with inlet \(u(t)\) and outlet \(y(t)\). This is the origin of the 11 *physical field types* in the legacy ambition.
- Then an honest comparison: **old 1,480 allocated (some constrained/frozen) + dynamic θ but zero kinetic prefactors** **vs** **new 240 bulk coordinates + source-based reacting kinetics but instantaneous/PSSA θ**. These are **complementary strengths**, not "old failed, new succeeded."
- Bridge into the state-space expression \(\dot{\mathbf x}=F(\mathbf x,u(t);\mathbf p)\). Emphasise that state-space coordinates are a bookkeeping of *physically relevant internal memory*, **not** an extra chemical species or a promise of improved identifiability.
- **Do not put both long PDEs or the interfacial flux-conservation derivation on the main slide.** Those are appendix/supervisor-question evidence. If asked whether the fully resolved physical equations are validated, answer **not yet; a conservative interface-flux audit remains open.**
- The user requested a **single eventual global bulletpoint presentation outline**; presentation-building Work session may pull the above selective bullets but must **not equate A–M letters with required slides**.

**Suggested short speaker line:** "We began with gas concentrations, but the reactor can also store material in its pores and on its catalytic surface. Describing those inventories creates a state-space model. Our older code represents those hidden states explicitly; our newer reacting baseline is chemically better anchored but treats surface coverage as instantaneously equilibrated. The remaining challenge is combining the physics with a demonstrably conservative, calibrated solver."

**Source links:** [legacy 1,480 code](../../3_Model/c2h2_hydrogenation_transient_model.py) · [legacy actual audit](../../3_Model/state.md) · [framework model audit](../../3_Model/transient_model_framework_audit.md) · [1D/particle reference](../../1_Transport_Phenomena/pbr_transport_phenomena.md) · [new Hermes code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) · [draft θ bridge PR](https://github.com/AsapLoso/project-management-agents/pull/3) · [short existing 5-slide segment](https://github.com/AsapLoso/project-management-agents/blob/devcontainer/Academics/BEP/Catalysis/presentation/BEP_transient_state_mini_deck.html).
