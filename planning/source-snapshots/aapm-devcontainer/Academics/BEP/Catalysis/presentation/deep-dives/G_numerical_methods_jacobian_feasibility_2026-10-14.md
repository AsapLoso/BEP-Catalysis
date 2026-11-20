# Deep dive G — Numerical methods, stiffness and computational feasibility

**Date:** 14 October 2026 · **Status:** Research inventory / full thinking material (not merely a retrospective). Scientific presentation selection is *provisional*.  
**Related:** [F: physics and state space](F_conservation_state_space_2026-10-14.md) · [H: older code spotlight (index)](../RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [I: reacting model (index)](../RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [J: verification (index)](../RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [Deck-level open questions for Zoë](../DECK_OPEN_QUESTIONS.md).  
**Evidence:** [old Python code](../../3_Model/c2h2_hydrogenation_transient_model.py) · [old executed audit](../../3_Model/state.md) · [new Hermes code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) · [reacting BDF note](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/research/notes/BUG_NOTE_bdf_jacobian_cost_2026-10-13.md) · [saved sensitivity receipt](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/evidence/vertical_slice/sensitivity_receipt.json).

## New user-proposed numerical thought experiment (14 October, later discussion)

**[USER CHOICE / HYPOTHESIS — NOT CODE ALREADY RUN]** First investigate a straightforward **Forward Euler explicit-time** method with **upwind axial advection** (and a separately specified radial spatial operator if enabled). The user's leading concern is **stiffness**, and alongside it **numerical spatial dissipation** affecting transient waves. These are separate failure modes.

For positive advection in the one-component, no-reaction limit,

\[
C_j^{n+1}=C_j^n-\nu(C_j^n-C_{j-1}^n),\qquad
\nu=u\Delta t/\Delta z.
\]

For **CFL \(\nu=1\)**, \(C_j^{n+1}=C_{j-1}^n\): the mesh solution shifts without damping, provided this pure-advection setup/step relation holds. That is an important **exception** to inferring inevitable upwind attenuation from the exact-in-time semi-discrete analysis in §G0a. The special cancellation need not survive reaction, diffusion, varying flow, mismatched forcing timing or step-size constraints imposed by stiffness; \(\nu<1\) generally introduces diffusive smoothing.

**Minimal fair test (not performed):** For matched advection-only inputs compare Forward Euler at CFL=1 and CFL<1 against exact delayed sine and (at the same spatial grid) high-accuracy BDF/RK solutions. Then add well-defined reaction/diffusion terms and test whether explicit stability requires steps smaller than the transport CFL step. Keep \(\Delta t\), \(N_z\), amplitude, phase, positivity and runtime visible. Compare with the existing **BDF implementation** before selecting an approach. If the user said “implicit for spatial”, clarify that spatial *upwind/central differences* and time *explicit/implicit* are distinct choices; a spatial operator may be treated implicitly at the next time level but this makes the **overall time step implicit**.

**Presentation edit:** rough method outline + **open question** (“Can a simple explicit scheme remain stable and sufficiently accurate for our actual fast chemistry?”), not a declaration that Forward Euler has replaced the BDF code. Discuss with Zoë; status remains OPEN.

## TOP — My provisional editorial choices (user can override)

| Candidate point | Presentation value | Why / condition |
|---|---|---|
| **Method of Lines: spatial PDE → dynamic ODE state vector** | **HIGH** | Physically meaningful bridge from F; helpful visualization, without complete PDE derivation |
| **Explicit vs implicit integration** | **HIGH** | A real applied-mathematics question; don't confuse an explicitly described *physical model* with an explicit *time integrator* |
| **What makes an ODE system stiff?** | **HIGH** | Fast vs slow physical modes and, in the optional resolved case, artificially fast boundary penalty; needs quantitative scale separation |
| **Jacobian structure, sparsity and performance** | **HIGH** | Existing executed probe identifies Jacobian construction as an expensive operation; possible algebraic remedy |
| Upwind1 vs high-resolution/advection schemes | **MEDIUM** | Only compelling if showing how phase/amplitude of cyclic forcing can be numerically altered |
| BDF vs Radau vs explicit RK vs IMEX | **MEDIUM** | Good **Zoë discussion question**; alternatives have not been benchmarked under matched conditions |
| Grid / tolerance refinement | **MEDIUM–HIGH** | Scientific credibility; source code has gates, but successful current-run receipts must be verified |
| Dense analytic Jacobian and resolved-pellet consistency | **HIGH as a research question**, maybe backup for talk | The newer analytic Jacobian is still **dense** and the resolved branch has unresolved derivative consistency and 1e12 shell penalty. Do not say the entire solver is verified |
| An exhaustive numerical-scheme literature review | **LOW for slides** | A–M source material, not a separate lesson in numerical analysis |

**The user requests full content to think aloud and select points; no automatic slide selection.** The eventual deck should be a global sequence of short bullets. The present file retains open questions for **Zoë Gromotka** at deck level and does not claim she has been contacted.

## G0a. New scientific/numerical lead — quantify **spatial** attenuation before blaming BDF or RK (user discussion, 14 Oct)

**[DERIVED — NOT an executed reacting-simulator result]** For pure positive advection with sinusoidal inlet, the exact PDE \(\partial_t C+u\partial_z C=0\) propagates \(C_{\mathrm{in}}(t-L/u)\): it introduces phase delay, but **no amplitude attenuation**. With first-order upwind in **space**, \(N\) uniform cells, and exact time integration of the semidiscrete ODEs,

\[
\dot C_j=(u/\Delta z)(C_{j-1}-C_j),\quad
\frac{\widehat C_N}{\widehat C_0}
=\left(1+i\omega\Delta z/u\right)^{-N}.
\]

Therefore \(|A_{\rm out}/A_{\rm in}|=[1+(\omega\Delta z/u)^2]^{-N/2}\). The Hermes code's illustrative [periodic gate C](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) uses \(f=1/\tau_{\rm residence}=u/L\), so \(\omega\Delta z/u=2\pi/N\). Derived, pure-transport harmonic response:

| Axial cells \(N\) | Amplitude retained | Numerical attenuation |
|---:|---:|---:|
| 20 | 39.01% | 60.99% |
| 30 | 52.52% | 47.48% |
| **60 (Hermes standard)** | **72.09%** | **27.91%** |
| 120 | 84.85% | 15.15% |
| 240 | 92.11% | 7.89% |
| 480 | 95.97% | 4.03% |

**Important:** This is the *infinite-time periodic steady solution of the **linear advection-only upwind MOL***, at one chosen forcing frequency and grid, with continuous-time-exact ODE evolution; it **does not** measure the response of the nonlinear reacting model, whose physical adsorption/transport/kinetic dynamics also alter output. The frequency is the specific illustrative residence frequency of gate C, **not** all candidate forcing frequencies.

**[DECISION / implication]** A smaller time step or RK4 instead of BDF **cannot remove upwind's intrinsic spatial attenuation** as the time error tends to zero. The leading semidiscrete numerical diffusivity for first-order upwind is \(D_{\rm num}\simeq u\Delta z/2\). Raising \(N\), changing the spatial scheme (e.g. carefully verified TVD2), and doing grid convergence on **amplitude and phase** are necessary to test this issue. **Time integration remains independently important:** large BDF steps can damp/shift waves; RK4 can be sufficiently accurate in time for a nonstiff or moderately stiff validated system provided its stability and error restrictions are met. RK4 is **not automatically cheap** if fast diffusion/adsorption or the radial \(10^{12}\) s⁻¹ shell-penalty mode makes the equations stiff. A special exception to simplistic “explicit always smears” language: forward Euler + first-order upwind for **pure advection at Courant number exactly one** can shift the discrete profile one cell per step without damping; reaction terms, other grid/time settings and mixed physics remove that idealized identity.

**[PROPOSED TEST, unrun]** First turn chemistry OFF, impose a periodic inlet, compare the numerically integrated advection-only solution against the exact delayed sinusoid with \(N=30/60/120/240\). At fixed spatial grid compare **RK45/DOP853, BDF, Radau** with carefully controlled maximum step and tolerances; then compare \`upwind1\` to the coded but unverified \`tvd2\` at fixed time accuracy. Track steady-periodic **amplitude ratio, phase error, max undershoot, wall time**, not only steady conversion. Only after numerical errors are bounded should physical reaction and fitting signals be interpreted. This is now a **strong mathematical candidate for the deck's “open scientific question”** and for Zoë.

## G1. What we actually wrote — side-by-side code provenance

| Feature | Legacy scaffold, \`devcontainer\` | Reacting vertical slice, Hermes branch |
|---|---|---|
| Mathematical form | Space-discretized coupled bulk/pore/site PDEs → ODE RHS | MOL: gas advection and source → ODE RHS, optional radial pore PDE → ODE |
| Physical states & mesh | 20 axial points; 10 radial nodes; 4+4 gas fields and 3 occupied site fractions → **1,480 allocated coordinates** | **60×4=240** bulk gas coordinates, **uniform-pellet PSSA default**; optional 60×(4+9×4)=**2,400** bulk + radial pore coordinates; no dynamic θ |
| Advection | First-order **backward/upwind** in z, with assumed positive flow | First-order upwind1 default; optional \`tvd2\` slope-limited path is coded but separately unvalidated |
| Pellet diffusion | Spherical radial finite-difference/flux-like operator; known centre-coefficient and quadrature defects | Optional spherical flux-form radial operator with corrected centre coefficient; **not engaged by standard uniform-pellet baseline** |
| Time stepping | SciPy \`solve_ivp(method="BDF")\`, no supplied Jacobian nor sparsity hint | SciPy \`solve_ivp(method="BDF",jac=reactor.jac,rtol=1e-7,atol=1e-12)\` in \`integrate\`; Jacobian is returned as a **dense ndarray** |
| Reaction kinetics | Explicit θ ODE forms, **8 zero kinetic prefactors by default**, no calibrated reacting baseline | Source-backed 2019 LHHW **PSSA effective** rate law, no θ ODE |
| Evolved shell boundary | Old code mutates \`y\` through a reshape view; pore shell derivative zero; site-shell derivative frozen | Resolved branch uses rapid shell \`pin=1e12\` relaxation, not elimination of algebraic constraint |
| Current evidence | Six executable numerical defects in stored audit, including performance bottleneck; no validated reactive kinetics | Source 24/24 transcription gate and saved numerical artifacts exist; opt-in resolved closure and Jacobian need separate verification |

**Important vocabulary:** An **explicitly written** ODE model \( \dot x=f(x,u;p)\) can use an **implicit** numerical solver. Neither inspected production path uses an explicit Runge–Kutta scheme as its main time integrator. If the user meant a *different* explicit implementation, identify that code before attributing it to one of the two scripts. [FACT: inspected code]

## G2. The mathematical path: PDE → MOL → stiff ODEs

A simple bulk balance, *per void gas volume*, in the uniform-pellet approximation is

\[
\partial_t C_i(z,t)=-u_i\,\partial_z C_i(z,t)+\sigma_i(C(z,t);p),
\]

with \(u_i=u_s/\epsilon_b\) and suitable chemistry source normalization. Spatial discretization at \(z_k\) with first-order positive-flow upwind gives

\[
\dot C_{i,k}= -\frac{u_i}{\Delta z}\left(C_{i,k}-C_{i,k-1}\right)+\sigma_i(C_k;p),
\]

where the inflow \(\,C_{i,0}(t)\,\) is an **input**, not an additional reactor-state variable. This is the **Method of Lines (MOL)**: discretize the *space* operators, **not** time; solve the resulting ODE system in continuous time using a separate integrator. Both Python paths implement this main principle.

A resolved spherical particle adds

\[
\epsilon_p\partial_t c_{p,i}= D_{\rm eff,i}\,r^{-2}\partial_r(r^2\partial_r c_{p,i})+\rho_p q_i,
\]

with centre symmetry and a boundary condition at the shell. This creates spatial modes on different timescales from bulk advection. A non-PSSA surface model then adds \(\dot\theta_j=g_j(c_p,\theta;p)\), potentially much faster or slower than either gas process.

**What the method does NOT do:** It does not turn an intrinsically time-dependent input into an autonomous physical experiment; does not make every retained coordinate independently identifiable from the outlet; does not establish convergence or physical validity by itself.

## G3. Spatial schemes: why these choices, what can go wrong?

**First-order upwind** for positive downstream flow is monotone/stable in many useful semi-discrete transport settings, avoiding spurious undershoots typical of naive central advection for sharp fronts. The cost is **numerical diffusion**: travelling waves are smeared as they traverse the discretized bed. That matters directly if the objective is **periodic inlet forcing** — phase and amplitude of the outlet waveform could be affected by the discretisation, not only chemistry. How important? **[UNRESOLVED]** Depends on grid spacing, inlet forcing frequency, flow speed, and measured observable.

**Second-order/TVD advection** can reduce numerical diffusion in smooth regions but requires a limiter near steep fronts and accurate boundary treatment; it is not automatically better at all frequencies or universally second-order at extrema. The Hermes file implements \`tvd2\` as an option; it has **not** been established as the working verified default. **This is a plausible A/B test, not an established improvement**.

**Radial spherical diffusion** demands a special central \(r=0\) treatment. For \(s=2\), the limit of \((1/r^s)\partial_r(r^s\partial_r c)\) is \(2(1+s)(c_1-c_0)/\Delta r^2=6(c_1-c_0)/\Delta r^2\) using the centre-grid convention. The older script uses \((1+s)=3\), **half** of the correct coefficient — a reproducible error from D2. The new optional radial function uses the corrected centre factor **in its code**; full radial converged reactor behavior remains open.

**Finite-volume vs finite difference:** conservation is a scientific requirement, not just a stylistic method choice. A radial finite-volume discretization can ensure that internal face fluxes cancel exactly when sum over cells and that bulk↔pellet exchange uses the **same signed interface flux**. F identifies a coupled-balance question in both optional resolved pathways. Treat any conservation verdict as a **future discrete residual test**, not an already executed numerical result.

**Other schemes** (collocation, spectral, higher-order upwind, DG) may be worth considering **only** if verified phase/accuracy/cost demands justify them; none of these is established as implemented in the named source scripts.

## G4. Explicit vs implicit time integration (the actual question)

An **explicit** forward Euler step uses only current state:

\[
x_{n+1}=x_n+h f(x_n,u_n;p).
\]

A basic **implicit** backward Euler step solves

\[
x_{n+1}=x_n+h f(x_{n+1},u_{n+1};p).
\]

BDF is a family of higher-order **implicit multi-step** schemes; these equations are illustrations, not an assertion that SciPy BDF is first-order backward Euler at every step. It generally uses nonlinear iterations and linear solves involving terms such as \(I-\gamma J\), where \(J=\partial f/\partial x\).

**Stiffness** roughly means that the dynamics include fast decaying modes that constrain a stable explicit time step even though the scientific trajectory of interest evolves more slowly. Relevant candidates here: **axial advection, intraparticle diffusion, surface adsorption/reaction/desorption**, and **very rapid numerical boundary penalties** in an optional implementation. **Do not call the old model's all-zero-kinetics run chemically stiff**: its intended coupled microkinetic rates are missing, so chemical time-scale separation hasn't been demonstrated there.

Illustrative explicit stability screens use \(\Delta t\lesssim\Delta z/u_i\) for the simplest positive-flow advection and \(\Delta t \sim \epsilon_p\Delta r^2/D_{\rm eff}\) (with method/geometry constants) for resolved radial diffusion. **These are order-of-magnitude stability relations**, not verified stable time steps for the actual nonlinear reactor code. The Hermes radial branch additionally pins its shell with a term \(10^{12}(C_b-c_{\rm shell})\) [s⁻¹], which introduces an artificial extreme fast mode that an explicit fixed step would have to resolve on ~\(10^{-12}\) s scales. This term is a *numerical design decision*, not measured chemical kinetics.

**Choice yet to be adjudicated:** BDF is a reasonable implicit default for a potentially stiff, sparse MOL reactor. We have not run an accuracy/cost comparison with **Radau**, explicit RK variants, or **IMEX** (implicit stiff diffusion/chemistry; explicit advection). The appropriate comparison must match physics, inputs, tolerances, outputs and computational budget rather than declaring one solver universally superior.

## G5. Jacobians: the empirically interesting computational insight

Define

\[
J_{ij}(x,u)=\frac{\partial f_i(x,u;p)}{\partial x_j}.
\]

The Jacobian describes the **local sensitivity of every state derivative to every other state**. In a finite-difference approximation to a dense \(N\times N\) Jacobian without sparsity/vectorization, perturbed RHS calls often scale with \(N\), even though almost every entry is physically zero.

**[FACT: saved old-model executed audit]** One old RHS evaluation was ~0.016 s in an audited run; a naive dense finite-difference Jacobian with **1,480 state perturbations** would cost order \(1,480\times0.016\approx24\) s, close to the audit's reported ~23 s (timings depend on system and test). This explains why dividing wall time by \`nfev\` gave the **wrong** impression that each RHS call took seconds; separate Jacobian RHS probes are not simply counted the same way. [D6 receipt and corrections](../../3_Model/state.md).

**[FACT: new code]** The Hermes reactor supplies an **analytic** \`reactor.jac\` to SciPy BDF. This avoids generic dense finite-difference perturbations, and the code constructs local chemistry derivatives including cross-species terms in the *uniform-pellet* branch. **Important caveat:** \`jac\` constructs and returns \`np.zeros((size,size))\` as a **dense NumPy matrix**, not a sparse CSR/CSC matrix; therefore it doesn't yet exploit the full potential of sparsity for large radial systems. **No validated end-to-end performance speedup factor is established by the inspected saved receipt**. The older narrative about a 6,240-state configuration describes an earlier **25-node** radial choice; the currently inspected optional 9-node/60-cell settings correspond to **2,400** entries.

**[UNRESOLVED: code-visible Jacobian issue for J]** In the optional resolved branch, bulk reaction rows use only \`dRdp[z,r,i,i]\` for derivatives with respect to particle concentrations, while \`R_i\` has **cross-species dependences** through the shared LHHW denominator and reaction numerator. Moreover the bulk Jacobian adds a direct bulk-shell derivative even while shell concentration is still an explicit state with its own \(10^{12}\) relaxation RHS. The full resolved analytic Jacobian therefore **should not be considered validated against its RHS** without a complete finite-difference column check. The existing D4b check samples **bulk columns on the uniform-pellet baseline**, not all resolved-pellet concentration columns. An internal gate comment claiming shell pin derivatives are 'deliberately NOT' RHS derivatives is stale: the present explicit pin RHS and \(\pm10^{12}\) Jacobian shell row appear algebraically consistent; other resolved terms remain questionable. **Avoid claiming a complete proven defect fix without running a verified check.**

**Why sparsity matters:** Physically, bulk advection couples neighboring axial cells; radial diffusion couples neighboring radial shells; and chemistry couples only local species. For a conservative formulation, this creates a sparse block-banded \(J\), not an arbitrary dense matrix. Sparsity-aware BDF (\`jac_sparsity\` for numerical derivatives, sparse Jacobian supplied directly, or matrix-free Newton–Krylov methods when justified) could reduce assembly and linear-solve cost, but the best option depends on the actual model topology, sparsity, tolerances and available solver stack.

## G6. Verification plan and alternatives — questions, not unearned answers

| Question | Smallest sensible comparison | What would count as evidence |
|---|---|---|
| Does spatial upwind smear a cyclic wave enough to bias inference? | Same physical forcing, compare \(n_z=30,60,120\) or more; inspect **outlet amplitude AND phase**, not just steady conversion | Quantitative convergence across spatial resolutions |
| Is BDF needed at target parameters? | Same validated RHS/tolerances/output; compare explicit RK, BDF and Radau at slow and fast physical parameters | Timings + error/step/rejection stats + sensitivity robustness |
| Is radial resolution physically needed? | Match uniform vs conservative resolved pellet model, same actual \(D_{\rm eff}\), radius and inlet frequency | Outlet discrepancy/effectiveness/transient-lag criteria; controlled nonzero kinetics |
| Is the analytic Jacobian correct in the resolved model? | Differentiate all relevant **columns** against RHS; include cross-species and shell constraints | Normed Jacobian residual + stable BDF run |
| Would sparse Jacobians materially help? | Sparse vs current dense (same physics, tolerances, hardware, model size) | Wall, memory, \`nfev\`, \`njev\`, \`nlu\` under matched runs |
| Do numerical tolerances stabilize claimed chemistry? | Coarse/tight \`rtol,atol\` and mesh variations, inspect outlet \(X,S\), carbon balance and wave phase | Named observable stability *and* conservation |
| Is the full coupled model conservative? | Conservative finite-volume face flux vs present separate compartment RHS | Carbon, hydrogen, gas/site inventories balanced including boundaries |
| Is IMEX worth exploring? | Only if BDF and Jacobian-aided alternatives remain unaffordable on validated model | Matched accuracy-cost evidence |

**[STATUS]** Hermes script includes D2 axial-grid and D3 ODE tolerance refinement gates for a **uniform-pellet, source-backed baseline**. The gates' **current pass status was not independently re-executed** in this turn; results must be read from the exact current saved receipt before use in presentation. Neither is proof of the optional radial solver, experimental reactor, or all future kinetic parameter regimes. Its \`tvd2\` option, \(10^{12}\) shell pin and full resolved Jacobian require further checks.

### Alternative methods in context

- **Explicit RK:** simpler to interpret and might be efficient when rates and grids yield a non-stiff effective system; its stability region can make resolved fast processes prohibitive.
- **BDF:** current implemented implicit baseline for stiff systems; numerical Jacobian cost/factorization can dominate.
- **Radau IIA:** implicit Runge–Kutta collocation with strong stability; a serious numerical comparator, not established as used.
- **IMEX:** separate non-stiff advection forcing from stiff diffusion/surface reaction; requires a provable operator split and tolerances and may add splitting error.
- **Finite-volume vs finite-difference:** conservative face fluxes can be especially valuable at bulk↔pellet coupling; finite differences remain legitimate if conservative discretization and convergence are demonstrated.
- **Sparse vs dense linear algebra:** likely major scalability lever because true local couplings are sparse; inspect Jacobian consistency first before optimizing.
- **Surrogate/reduced-order modelling:** relevant **only after** the full equations have credible benchmark results and training/validation regime; reducing state dimension is not equivalent to better source kinetics or identifiability.

## G7. Provisional slide selection and open supervisor questions

**Possible slide central claim:** “The hard part of making a transient physical reactor model usable is not just writing more equations — it is integrating many coupled timescales *accurately and affordably*.”

**Candidate visual:** three-layer physics/mesh diagram from F → \(\dot x=f(x,u)\) → split into advection + pore diffusion + kinetics → **BDF solve** → local **block-sparse Jacobian** picture. Include one small empirical audit badge (old dense finite-difference Jacobian ~23 s for 1,480 states on the recorded machine, one RHS ~0.016 s), clearly marked as an *old-model historical probe*, NOT a production benchmark for the new solver.

**Potential discussion for Zoë, still OPEN (not sent):** Which level of numerical detail deserves a slide? Is the **current explicit-in-physics, implicit-in-time** representation justified? Can a genuinely conservative sparse MOL system be integrated efficiently enough for repeated fitting/optimization? Should BDF remain baseline until verification, or is a controlled Radau/IMEX comparison justified? What error and cost tolerances are acceptable for outlet period/phase/yield? What is an adequate mathematical state and boundary closure (F)? See [deck-level questions](../DECK_OPEN_QUESTIONS.md) and [project state](../../state.md).

**DO NOT** turn this G note into a complete numerical-analysis lecture, declare an unrun solver comparison successful, or imply the source-fit PSSA chemistry demonstrates dynamically evolving θ. Leave specific choice of slide content to the user's running scientific reflection and the parallel deck workstream.

**Hand-off H/I/J:** H should assess the original code on its own terms, I the new reacting baseline on its own, and J should quantify the resolved Jacobian, conservative face coupling, source/geometry and grid/tolerance verification. Source audit and physically valid validation remain separate.
