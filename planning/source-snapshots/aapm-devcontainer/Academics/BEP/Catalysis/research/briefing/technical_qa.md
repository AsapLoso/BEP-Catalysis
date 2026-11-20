# Lucas technical Q&A — defending the model

**Purpose:** the questions Damian is likely to ask, with answers Lucas can *explain*, not
merely recite. Every answer is short enough to say out loud, and every one is traceable to
a file or a command.

**Rule for using this document:** if you cannot explain the *why* in your own words, do not
use the answer. A plausible-sounding answer you don't understand is worse than "I'd have to
check that."

---

## A. The numerical machinery

### A1. Why Method of Lines at all, rather than discretising space and time together?

MOL keeps the spatial discretisation and the time integration as two separate, checkable
steps. You discretise space once, get an ODE system, and then any stiff ODE solver applies.
The alternative — full discretisation, e.g. OCFE — produces one large NLP, which is what
you'd want if you were optimising the whole trajectory at once.

`[FACT]` The proposal names OCFE as an alternative for the *optimisation* stage
(`main.tex:205`). For the open-loop predictor, MOL is the simpler and more debuggable route,
and it is what Berger's worked example does.

### A2. Why BDF and not an explicit method?

Because the system is stiff. The surface kinetics have time constants orders of magnitude
faster than the transport timescales, so the Jacobian's eigenvalues are widely separated. An
explicit method's step size is set by the *fastest* mode even when the interesting physics
evolves on the *slowest* one — so it would take absurdly small steps and get nowhere. BDF is
implicit, so its stability region covers the fast-decaying modes without resolving them.

`[FACT]` This is exactly the reasoning recorded in the code's own comment
(`c2h2_hydrogenation_transient_model.py:233-234`) and restated as a standing decision in
`conventions.md:177`.

### A3. Why upwind for the bulk and central for the pellet?

Different physics, different scheme.

- **Bulk advection** is transport-dominated with positive velocity. Upwind (backward
  difference) uses only upstream information, which is what the physics does, and it
  guarantees stability — a central scheme can oscillate on sharp fronts.
- **Intra-particle diffusion** is a smooth, diffusive field. Central differences are
  second-order accurate there and there is no directionality to respect.

`[FACT]` `conventions.md:177`; framework audit D7 (`transient_model_framework_audit.md:23`).

`[UNRESOLVED]` Upwind is only first-order accurate, so it introduces numerical diffusion of
about $v\,dz/2$. Whether that is acceptable is a mesh-refinement question, and it has not
been answered for this model.

### A4. How do the 1,480 coordinates arise?

Straight grid arithmetic:

| Block | Shape | Entries |
|---|---|---|
| Bulk gas `C_b` | 20 axial × 4 species | 80 |
| Pore gas `c_p` | 20 axial × 10 radial × 4 species | 800 |
| Surface `theta` | 20 axial × 10 radial × 3 coverages | 600 |
| | **total** | **1,480** |

`[FACT]` `c2h2_hydrogenation_transient_model.py:58-66`, and the state packing at `:131-136`.

`[FACT — and this is the honest caveat]` **Not all 1,480 are independent.** D1 makes the
shell entries get overwritten rather than integrated, and D3 means the shell coverages never
receive a derivative. So 1,480 is the *allocated* count, not the count of active dynamics.
If asked, say that.

### A5. Why does the cost sit in the Jacobian rather than the RHS?

Because `solve_ivp` has no supplied Jacobian, so it builds one by finite differences — one
extra RHS evaluation per state component. That is 1,480 RHS calls per Jacobian, versus ~62
solver RHS calls for a short integration.

`[FACT]` Measured today: one RHS ≈ 0.022 s, one FD Jacobian = 1,480 RHS ≈ 32.7 s, and the
probe run used 1 Jacobian with `nfev = 62`.

`[IMPORTANT]` **Do not quote the seconds.** They are load-dependent and the register says so
(`3_Model/state.md:88-91`). The durable claim is structural: *the RHS is cheap; the dense
finite-difference Jacobian dominates; the fix is a sparsity mask or an analytic Jacobian,
not vectorising the loop.*

`[FACT]` The earlier "~2.2 s per rhs" figure was wrong — it was `wall/nfev`, which silently
folded in the Jacobian work. That retraction is recorded at `3_Model/state.md:65`.

---

## B. The physics and the modelling choices

### B1. Why do surface coverages matter so much?

Because they are the mechanism by which the reactor has memory. The selectivity depends on
how much acetylene and ethylene sit on the surface *at that moment*, not just on what is in
the gas. In a sequential network, ethylene is both the product you want and the reactant of
the reaction you don't — so the surface composition at each instant decides which way the
next molecule goes.

`[FACT]` This is the proposal's core physical argument (`main.tex:111-119`).

### B2. Why does pore transport matter, if the pellet is small?

Because a small pellet does not automatically mean no internal gradient — that is what the
Thiele modulus and the effectiveness factor are for. If the reaction is fast relative to
diffusion, the pellet interior is starved and the apparent rate is lower than the intrinsic
one. Resolving the radial profile lets you *see* that rather than assume it away.

`[UNRESOLVED — and say so]` The radial coordinate is **our extension, not Berger's**.
Berger's state count is $(N_{gas}+N_{surf})\times N_z$, with no radial axis
(`transient_model_framework_audit.md:19`). So this is a modelling commitment we added, and
it is where three of the six defects live. Whether it is required for the BEP is an open
question for Damian.

### B3. What are the model's assumptions?

Stated plainly:

| Assumption | Status |
|---|---|
| Isothermal | `[FACT]` stated in the proposal (`main.tex:189`); justified because hydrogenation is exothermic and non-isothermal simulation is instability-prone |
| Plug flow, no axial dispersion | `[DECISION]` a *reduction*, legitimate for $Pe \gg 100$, but it is a choice and should be stated as one (`3_Model/state.md:67`) |
| Pseudo-homogeneous, $C_s = C_b$ | `[DECISION]` this *is* Berger's model — his Eq. (1) has no film term (`transient_model_framework_audit.md:18`) |
| No energy balance | `[UNRESOLVED]` the proposal says isothermal; an earlier record had "isothermal → exothermic" in scope. FW-13 is the open scope decision |
| Reversible adsorption for all three species | `[FACT]` present in the code (`:91`, `:94`, `:100`) |

### B4. What is *not* assumed?

`[FACT]` The pseudo-steady-state assumption (PSSA) for the surface is explicitly **rejected**:
$\partial\theta_i/\partial t \neq 0$. That rejection is the whole point — a PSSA model cannot
represent a surface that is still filling up, so it cannot represent the transient selectivity
mechanism the thesis is about.

`[FACT — and this is the sharpest critique of the newer package]` `pbr`'s *default* surface
closure is `AlgebraicEquilibrium`, which carries no surface states at all. Its optional
`Relaxation` closure carries states but is a linearised phenomenological extension whose
time constant is assumed, not derived (`pbr/closures.py:352-386`). Either way, `pbr` does not
yet implement the non-PSSA microkinetics the proposal calls for.

---

## C. The defects

### C1. What is the difference between a "fix" and a "choice"?

This is the question you should be able to ask *yourself*, and the register's own framing.

- **A fix** has one determined correct answer, and the code currently deviates from it.
  D1, D2, D3, D4 are fixes.
- **A convention question** has no physics answer — it is a units/notation discipline
  problem. D5 is one.
- **A choice** is a legitimate modelling reduction that must be *declared*, not silently
  assumed. Plug flow vs Danckwerts, film vs no film.

`[DECISION]` `3_Model/state.md:59` and `bep_catalysis_master.md:110-115`. Note that **which
of these may be *reported* with the defect open is a human call** — it is master ticket
I1-07, and it stays open.

### C2. Walk me through D1.

The RHS does `c_p[z, -1, :] = C_s` to impose the Dirichlet shell condition. But `c_p` is a
`reshape` **view** into the solver's own state vector `y`, not a copy. So writing the shell
modifies the caller's array.

**Why that matters:** `solve_ivp` assumes `f(t, y)` is a pure function of `y`. If it mutates
`y`, the solver's internal trajectory is not the trajectory the equations describe.

`[FACT]` Measured: 80 of 1,480 entries changed by one call, all in the `c_p` block, all at
`r=9` (the shell); A/B against a non-mutating wrapper gives `max|Δ| = 5.148`.

**The fix:** unpack `y` into fresh arrays instead of a view.

### C3. Walk me through D2 — and why is 6 right, not 3?

The radial operator is $\frac{1}{r^s}\frac{\partial}{\partial r}\big(r^s \frac{\partial f}{\partial r}\big)$.
At $r \to 0$ this is a removable singularity, and by symmetry the limit is
$(1+s)f''(0)$. The discrete reflected stencil gives the coefficient $2(1+s)$ in front of
$(c_1-c_0)/h^2$.

For a sphere, $s=2$, so the exact coefficient is $2\times3 = 6$. **The code uses $(1+s) = 3$**
— half the correct value.

`[FACT]` Verified against the analytic solution $f = r^2$: exact **6.0000**, code **3.0000**,
ratio **0.5000**. The code's own comment even says "voor sfeer is het 6 ipv 2" — so the
script deviates from its own stated intent by a factor of two.

`[DECISION]` **Not a decision** — the value is determined, and the master map says so
explicitly and forbids re-ticketing it.

### C4. What about D5 and the `C_t` thing?

`[CRITICAL]` **There is no double-`C_t` defect. That claim was retracted.** Both `C_t`
factors in the code are correct.

What is real: `R_gas` is built from products like $k\cdot c\cdot\theta^k$, so it carries
units of **per-site `1/s`**. The function docstring says `[mol/kg_cat/s]`, which is wrong.
And the same symbol `R_gas` is used for a site-normalised quantity in one place and a
volume-normalised one in another, with no units column.

`[FACT]` Verified: with $k$ in m³/(mol·s) and $c$ in mol/m³, `R_gas` evaluates to per-site
`1/s`.

**If you bring up the retraction yourself, it demonstrates you cross-checked two audits
rather than conflating them.** That is a finding, not an embarrassment.

### C5. What is D4's 16 % and is it a real error?

`[FACT]` The particle-volume average uses `r_radius**s * dr` as the weight and normalises by
the *analytic* $R_p^{s+1}/(s+1)$ instead of by the discrete sum. At $N_r=10$ the discrete
sum is 83.95 % of the analytic normaliser, so the averaged rate is biased ~16 % low. It
converges as $O(dr)$, not $O(dr^2)$.

`[IMPORTANT — the honest caveat]` **The 16 % is a constant-rate quadrature check on this
grid, not a universal trajectory error.** Do not claim "the model is 16 % wrong". The
defect is inconsistent endpoint quadrature/normalisation; the 16 % is its magnitude for a
constant field.

`[FACT]` An earlier version of the register said 2.9 %; that came from adding a trapezoid
half-weight the code does not apply. Corrected 2026-09-30.

---

## D. Validation, status, and the honest wall

### C6. Is there anything wrong with how `pbr` builds its feed?

`[FACT]` Yes, and it is the newest finding. `pbr` converts a mole-fraction feed to partial
pressures by dividing by the **reacting** mole fraction — `sum(y_reactive)` — which inflates
every reactive partial pressure by a factor of $1/0.753 = 1.328$ for the source's Ar-bearing
feed.

The paper settles it: it publishes its own partial pressures at 62 °C
($p_{C_2H_2} = 0.95$ kPa, $p_{H_2} = 5.5$ kPa) and states its total pressure (1.26 bar).

| Species | Source states | `y_i·P_total` | error | `pbr` path | error |
|---|---|---|---|---|---|
| C₂H₂ | 950 Pa | 1260.0 Pa | +32.6 % | 1673.2 Pa | +76.1 % |
| H₂ | 5500 Pa | 5418.0 Pa | **−1.5 %** | 7194.8 Pa | **+30.8 %** |

**The hydrogen row decides it:** the source's 5.5 kPa matches `y_i·P_total` to 1.5 % and
`pbr`'s own conversion to within 31 %.

**Why the docstring's defence fails.** It calls the division a "void-volume conversion". A
void-volume correction is real physics — but it does **not** change partial pressure. The gas
inside the voids has the same composition as the bulk stream. So the stated justification does
not establish the behaviour.

**Why it matters:** a 33 % inflation of the driving force propagates into every rate, hence
into any yield or selectivity number computed later. And it is invisible to the test suite —
all 37 tests pass with it present.

### C7. What about the pressure you use?

`[FACT]` The source states 1.26 bar (126000 Pa), **not** 1 atm. This is load-bearing and easy
to get wrong: at 1 atm, $\theta_{H_2}$ comes out at 0.00201 — just *inside* the published
lower bound of 0.002. At the correct 1.26 bar it is 0.00181 — just outside.

**We got this wrong ourselves on the first pass and reported 12/12.** The corrected result is
11/12. If you are asked how the verification was done, that correction is a *feature* of the
account, not an embarrassment: it shows the check was sharp enough to catch its own error.

### D1. What would it take to call this model validated?

Concretely, all of:

1. **Sourced kinetics** — constants traceable to a primary source, not placeholders.
2. **A conservation check** — elemental and inventory closure, including the bulk/pore
   transient balance that is currently open (§D3 below).
3. **Analytic limits** — zero-kinetics and fixed-inlet behaviour checked explicitly.
4. **Mesh and time convergence** — refinement studies showing the answer is not a grid
   artefact.
5. **A published or experimental transient benchmark** — a trajectory it must reproduce.

`[UNRESOLVED — HITL]` The *acceptance threshold* — which output, over which operating range,
at what error — is not defined. That is ticket SM-5, and it is a supervisor decision. Without
it, "validated" has no test.

### D2. What is the status of periodic forcing?

`[FACT]` **Not implemented.** The inlet is a fixed dictionary and the RHS never reads `t`.
There is no time-dependent forcing, no cycle-averaged yield metric, and no periodic-state
convergence check.

So the honest answer to "did forcing improve yield?" is: **the experiment has not been run,
and the capability to run it does not exist yet.**

### D3. What is the bulk/pore inventory question?

The bulk balance uses a volume-averaged gas production rate, while the pore gas has its own
transient accumulation. There is no term carrying the pore storage back into the bulk.

Integrating the pore balance over a spherical pellet gives
$\varepsilon_p\,d\langle c_p\rangle/dt = (3/R_p)J_{in} + \rho_s C_t\langle R_{gas}\rangle$,
so the bulk exchange should be
$\frac{1-\varepsilon_b}{\varepsilon_b}\big(\rho_s C_t\langle R_{gas}\rangle - \varepsilon_p\,d\langle c_p\rangle/dt\big)$.
**The code keeps the first term and drops the second.**

`[FACT]` A zero-reaction diagnostic makes this concrete: set the bulk uniformly to the inlet
but leave the pellet interior empty — every bulk derivative is zero while the interior pore
derivative is positive (H₂: 457.2 mol m⁻³ s⁻¹). Pore inventory fills without bulk uptake.

`[UNRESOLVED]` It may be an intended quasi-steady pellet approximation. If so it must be
**declared**. **Fixing D1 does not fix this** — it is a separate physics question.

### D4. Which implementation should you take forward?

`[UNRESOLVED — this is Damian's call]` The evidence, stated fairly:

**For `pbr`:** non-mutating unpacking, correct centre operator, normalised quadrature,
callable inlet forcing, sparse-integration plumbing — i.e. every one of the six old defects
has a structural answer. Its Urmès2019 parameters **now verify against the primary source**,
and its rate law **reproduces the paper's published coverages at 11 of 12 checks** (it misses
$\theta_{H_2}$ at the highest-acetylene feed by 9.5 % of the way to the bound — see the
briefing §5.2). Its test suite passes
(37 tests).

**Against `pbr`:** its surface does not feed back into the gas rates, so it is a PSSA model
with decoration, not the proposal's model. It has a reproduced broadcast defect in the
relaxation closure, a reproduced wrong-sized sparsity mask, and a feed conversion that
inflates every reactive partial pressure by 33 % relative to its own source. And its default
surface closure carries no surface states at all.

**Against the older scaffold:** six reproduced defects, zero kinetics, no forcing.

The honest summary: **`pbr` is architecturally ahead and has verified chemistry; neither is
the proposal's model yet.** The single change that would move `pbr` toward it is making
`rate.rates` accept and use `theta`.

### D5. What is the strongest thing you have?

`[FACT]` Not a yield curve — a **verified parameter transfer with its one miss stated**. This
week I confirmed that `pbr`'s Urmès2019 kinetic parameters match the primary paper's Table 5
on all eight constants, that the rate equations match term for term including the $K_1/K_5$
factor, and that the rate law reproduces the paper's own published surface coverages at
**11 of 12 checks** — missing $\theta_{H_2}$ at operating condition 1 by 9.5 % of the way to
the published lower bound.

**That is a check on the chemistry itself, independent of the reactor model.** It is the one
claim in this project that a supervisor can attack — and it survives, *including* the miss,
because a near-miss reported honestly is stronger than a rounded pass.

`[CRITICAL]` If you quote this, **quote the 11/12 and name the miss.** Do not say "it
reproduces the coverages" and leave it there. Two reasons: it is the truth, and a supervisor
who checks the paper's ranges will find the miss himself — at which point an unqualified claim
becomes a credibility problem rather than a scientific one.

**Be ready for: "why does it miss?"** The honest answer: $\theta_{H_2}$ scales with
$\sqrt{K_1 p_{H_2}}$ while the denominator is dominated by the acetylene term, so the
highest-acetylene feed competes hardest for sites and drives hydrogen coverage down. That is
physically sensible, and a 9.5 % miss against a published *range* may be inside the source's
scatter — but distinguishing that from a real deficiency needs the paper's per-condition
coverage figure, which we have not digitised. Say that, and say it is a next action.

### D6. What is the weakest thing?

`[FACT]` The bulk/pore transient inventory closure (§D3), and the absence of any forcing
implementation. The first is a physics question that fixing code will not answer; the second
means the thesis's central experiment has not been run.

---

## E. Likely ambush questions

| Question | Short answer |
|---|---|
| "So what have you actually proven?" | That the mathematical structure is built and audited, and that the transferred kinetics reproduce their source. Not that the reactor predicts anything. |
| "Why are the kinetics still zero?" | Because they must come from a source, and the repository forbids inventing constants. One source is now verified; wiring it in is the next step. |
| "Isn't 1,480 variables too many?" | The dependency structure is sparse, so ordinary Jacobian-aware implicit methods handle it. 1,480 is not itself a reason for model reduction. |
| "Do you need machine learning for this?" | No. The mission explicitly excludes new nonlinear control theory. Established numerical methods are sufficient. |
| "Is the 2022 paper relevant?" | Very — it's the direct periodic-operation comparator. It is **not in the library**; acquiring it is a concrete next action. |
| "Did you use AI for this?" | Yes, for reconnaissance and for building the verification probes. Every number in the briefing has a command that reproduces it, which is the point of the tagging. |
