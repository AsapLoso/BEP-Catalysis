# BEP Catalysis — Supervisor Briefing

**For:** Damian van Berkel · **Author:** Lucas van Dekken · **Date:** 2026-10-13
**Branch:** `hermes/bep-wayfinder-2026-10-13` · **Base commit:** `1898fe2` (`origin/devcontainer`)
**Status:** verified partial result, not a validated simulator

> **How to read this document.** Every number carries a command that reproduces it and a
> commit or file that contains the source. Claims are tagged `[FACT:]` (verified here, with
> receipt), `[DECISION:]` (settled, with the authority that settled it), `[UNVERIFIED:]`
> (asserted somewhere but not confirmed), or `[UNRESOLVED:]` (a live question with no answer
> yet). Anything without a tag is framing, not evidence.
>
> **The one-sentence version:** the mathematical structure is real and the audit trail is
> real; the *physics* is not yet switched on, and this document says exactly which of those
> two things is which.

---

## 1. The question and why it is worth asking

`[FACT: proposal]` The proposal's abstract (`0_Project_Management/main.tex:111`) sets out a
mathematical framework for **dynamic operation** of acetylene semi-hydrogenation in a
packed-bed reactor. The physical argument is specific and falsifiable:

- Industrial acetylene semi-hydrogenation runs at steady state, where surface coverages
  $\theta_i$ sit at fixed equilibrium. In a sequential network
  $\mathrm{C_2H_2 \to C_2H_4 \to C_2H_6}$, that locks in a conversion/selectivity trade-off:
  you cannot push acetylene conversion without also hydrogenating the ethylene you wanted.
- If the inlet is instead **modulated**, transient concentration waves can drive a
  desorptive flux of the intermediate ethylene into the gas phase *before* the second
  hydrogenation step consumes it. The yield cap is a property of the steady state, not of
  the chemistry — so a time-varying input may beat it with no reactor redesign.

`[FACT: proposal]` The proposal separates this into two deliverables: a **discretised 1D
open-loop predictive model** of the hidden intermediate states (primary), and an
**optimisation** over the input cycle as a theoretical proof-of-concept. `[FACT: proposal]`
Observers and MPC are explicitly reserved for later research
(`0_Project_Management/main.tex:284`).

**Why this framing matters for the presentation.** The project is not "build a reactor
simulator". It is "test whether the steady-state yield cap can be broken by forcing". That
question is what makes the missing kinetic parameters a real blocker rather than an
inconvenience — with zero kinetics you cannot demonstrate either the cap or its defeat.

---

## 2. What the literature changed about the modelling approach

Three literature findings are load-bearing, and one of them changes the code.

### 2.1 Berger (2008) supplies the framework, and one code decision follows from it

`[FACT: primary paper]` Berger, *Dynamic methods for catalytic kinetics*, Appl. Catal. A
348 (2008) 135–146, DOI 10.1016/j.apcata.2008.03.020. Figure 5 gives a **pseudo-homogeneous
axial gas balance coupled to time-dependent surface coverages**, solved by spatial finite
differences + method of lines + implicit BDF.

`[DECISION: framework audit §D1–D2, `3_Model/transient_model_framework_audit.md:17-18`]`
Because Berger's Eq. (1) carries **no film term**, pseudo-homogeneity *is* Berger's model.
That is why the code keeps $C_b$ and $C_s$ structurally separate but sets them equal: it
recovers Berger's collapsed form while leaving the film as a switch.

`[FACT: `3_Model/transient_model_framework_audit.md:19`]` The resolved **intra-particle
radial coordinate is our extension, not Berger's.** Berger's state count is
$(N_{gas}+N_{surf})\times N_z$ — no radial axis. This is worth stating plainly to a
supervisor: the radial dimension is a modelling commitment we added, and it is the source of
three of the six code defects (D2, D3, D4).

### 2.2 A directly relevant periodic acetylene paper exists — and it is *not* the one we have

`[FACT: literature search, verified against the repository]` Urmès, Daniel, Schweitzer,
Cabiac, Julcour & Schuurman (2022), *Microkinetic Modeling of Acetylene Hydrogenation Under
Periodic Reactor Operation*, ChemCatChem 14, e202101826, DOI 10.1002/cctc.202101826. This is
the closest published comparator to the intended work: a transient fixed-bed microkinetic
model under periodic flow.

`[FACT: repository inventory, this run]` **The 2022 paper is not on disk.** A search of the
literature tree returns the *2019* paper only. The two are different papers:

| | Urmès et al. **2019** | Urmès et al. **2022** |
|---|---|---|
| Title | Kinetic Study of the Selective Hydrogenation of Acetylene over Supported Palladium under Tail-End Conditions | Microkinetic Modeling of Acetylene Hydrogenation Under Periodic Reactor Operation |
| Venue | Catalysts 9(2):180, DOI 10.3390/catal9020180 | ChemCatChem 14, e202101826 |
| Content | steady-state kinetics, fitted LHHW rate law | transient model under periodic forcing |
| On disk? | **yes** — `Articles/acquired_pdfs/urmesKineticStudySelective2019.pdf` | **no** |

**This distinction is the single most consequential correction in this briefing.** The 2019
paper is the *parameter source* (verified in §4). The 2022 paper is the *periodic-operation
comparator*. Conflating them would put a steady-state kinetics citation under a
periodic-forcing claim.

`[UNRESOLVED:]` The 2022 paper's equations, supplementary material and any code remain
uninspected. Acquisition is a concrete, high-value next action (§8).

### 2.3 The centred Arrhenius form is a real choice with a real reason

`[DECISION: framework audit D5, `3_Model/transient_model_framework_audit.md:21`]` The
centred Arrhenius form $k = k_{ref}\exp\!\big(-\tfrac{E_a}{R}(\tfrac{1}{T}-\tfrac{1}{T_{ref}})\big)$
is retained **together with Berger's stated reason**: it decorrelates the pre-exponential
from the activation energy, because in the ordinary form the two are strongly correlated
when the data span a narrow temperature window. Berger's own binary correlation fell below
0.71 — the number is recorded at `Articles/analyses/dynamic_kinetics_berger2008.md:66`.

`[FACT: this run]` The `pbr` package documents the *opposite* choice for the Urmès set, and
it is right to: Urmès publishes $k_{04}$ as a **pre-exponential** and writes
$k_{04}\exp(-E_4/RT)$, so applying the centred form would multiply every rate by a spurious
factor. See `Methanol-Catalysis/pbr/parameters.py:482-494`. **Two sources, two conventions,
both justified in their own context** — this is a distinction worth having in your pocket,
because it is exactly the kind of thing a supervisor probes.

---

## 3. From physical balances to a stiff solver

This section is the "what is actually built" spine. The chain is:

```
physical balances  →  spatial discretisation  →  state vector x(t)  →  stiff implicit solver
```

### 3.1 The balances

`[FACT: `3_Model/c2h2_hydrogenation_transient_model.py`]` Three coupled levels:

| Level | Variable | Shape in code | What it represents |
|---|---|---|---|
| Bulk gas | `C_b` | `(N_z=20, N_gas=4)` | axial gas concentration in the bed voids |
| Pore gas | `c_p` | `(N_z=20, N_r=10, N_gas=4)` | gas concentration inside the pellet, radially resolved |
| Surface | `theta` | `(N_z=20, N_r=10, N_surf=3)` | fractional coverages $\theta_{H},\theta_{C_2H_2},\theta_{C_2H_4}$ |

`[FACT: code arithmetic]` $20\times4 + 20\times10\times4 + 20\times10\times3 = 80 + 800 + 600
= \mathbf{1480}$ state entries. The 1,480 figure is therefore a *grid arithmetic* result,
not a physical insight — and `[FACT: this run]` not all 1,480 are independent, because the
boundary treatment and the frozen shell are defective (D1, D3).

### 3.2 The three discretisation choices, and the trigger condition for each

`[DECISION: `3_Model/transient_model_framework_audit.md:23` (D7), restated as a standing rule
at `conventions.md:177`]`

| Choice | Scheme | Trigger condition that justifies it |
|---|---|---|
| Bulk advection | upwind / backward difference | advection-dominated ($Pe \gg 1$); upwind guarantees stability for positive velocity |
| Intra-particle diffusion | central difference | diffusion-dominated, smooth field; second-order interior accuracy |
| Time integration | implicit BDF | chemistry is stiff relative to transport — explicit steps would be limited by the fastest surface timescale |

**This is the answer to "why BDF?".** Not preference: the surface kinetics have time
constants orders of magnitude below the transport timescale, so the Jacobian of the system
has widely separated eigenvalues. An explicit method would take steps set by the fastest
(fastest-decaying) mode while the physics of interest evolves on the slowest. That is the
textbook definition of stiffness, and BDF is the standard implicit answer.

### 3.3 The state vector and the solver

`[FACT: code]` The RHS returns
`concatenate(dCb_dt, dcp_dt, dTheta_dt)` — one flat 1,480-vector. Time is **not** a state
component; it indexes the trajectory. After discretisation $x(t)$ is an instantaneous vector
of concentrations and coverages, and $x(t)$ evolves by $\dot x = f(x, u(t))$. `[FACT: this
run]` That is the correct Markov reading, and it is the honest version of the claim: the
*observable inputs* are still history-dependent, but the *augmented state* is not.

`[FACT: code `:238-244`]` Integration is `scipy.integrate.solve_ivp(..., method='BDF')` with
default tolerances, **no supplied Jacobian and no sparsity mask**. That last omission is
what makes D6 expensive.

---

## 4. The two code candidates: what each actually runs

This is the part most likely to be wrong in an earlier summary, so it is stated precisely.

### 4.1 `3_Model/c2h2_hydrogenation_transient_model.py` — the older scaffold

**What it runs.** `[FACT: this run, reproduced]` A complete, executable Method-of-Lines
scaffold: 1,480 ODEs, upwind bulk advection, radial pore diffusion, reversible adsorption
for H₂/C₂H₂/C₂H₄ and two hydrogenation steps, integrated with BDF.

**What it does not run.**

| Missing | Evidence |
|---|---|
| Any chemistry | all 8 kinetic tuples ship as `(0.0, 0.0)` (`:34-43`); `[FACT: this run]` with all-zero kinetics the state stays identically zero |
| Temperature response | `k = lambda name: p.kinetics[name][0]` — `E_a` is parsed and then ignored (`:87`) |
| Periodic forcing | the inlet is a fixed dict; the RHS never reads `t` |
| Yield or selectivity output | the script prints solver success, step count and wall time only |
| Axial dispersion, film resistance | plug flow + pseudo-homogeneous by construction |

`[FACT: this run]` **"Zero kinetics" does not mean "nothing happens".** With a non-zero
inlet, the first bulk H₂ derivative is $100\ \mathrm{mol\,m^{-3}s^{-1}}$ at $y=0$. Chemistry
and coverages stay inactive; gas transport does not. An earlier note claiming the full state
stays identically zero was wrong about transport.

### 4.2 `Methanol-Catalysis/pbr/` — the newer modular package

`[FACT: this run]` 3,423 lines across 11 modules, sibling repository
`AsapLoso/Methanol-Catalysis` at HEAD `e0663ba`, plus a `tests/` directory.

**What it genuinely fixes.** `[FACT: this run]` Every one of the six old defects has a
structural answer in the source:

| Old defect | `pbr` mechanism |
|---|---|
| D1 state mutation | `Layout.unpack` copies before use; `radial_diffusion` assembles a new array when replacing the shell |
| D2 centre coefficient | `centre_operator` returns the full $2(1+s)D/dr^2$ |
| D3 frozen shell | the relaxation branch evaluates the whole `theta` array |
| D4 quadrature | Simpson on odd grids / trapezoid on even, divided by the **discrete** sum |
| D5 units | explicit per-kg conversions and porosity factors |
| D6 Jacobian cost | analytic sparsity plumbing, enabled by default |

**What it does not do — and this is the honest core.**

`[FACT: `pbr/solver.py:274-341`, read this run]` **The evolving surface does not feed back
into the gas reaction rates.** `rate.rates(local_p, T)` computes gas rates from partial
pressures and temperature. Later, `rate.coverages(c_bulk*RT, T)` supplies a *relaxation
target*. Neither call accepts `theta`. All three rate laws return zero surface-reaction
derivatives, and those zeros are not used to evolve the carried surface.

> **Consequence:** `pbr` is a **steady-state / PSSA rate model with optional auxiliary
> relaxation states**, not the proposal's coupled transient adsorbate kinetics. Its own
> `Relaxation` class says so: the time constant is assumed, not microkinetically derived
> (`pbr/closures.py:352-386`).

`[FACT: this run, reproduced]` **Three** further defects, all executed:

- **The relaxation target does not broadcast.** `Layout` carries `theta` as
  `(N_z, N_r, 3)`; the target is evaluated from bulk concentrations as `(N_z, 3)`;
  `Relaxation.derivative` subtracts them directly. Reproduced as
  `ValueError: operands could not be broadcast together with shapes (20,3) (20,10,3)`.
- **The sparsity mask has the wrong size.** `Model.sparsity` passes
  `n_radial_effective` into `jacobian_sparsity`'s `n_surface` slot, while `Layout` uses three
  coverages. Reproduced: mask is `(294, 294)` where the state is `(234, 234)` — built with 5
  "surface species" instead of 3.
- **The feed conversion contradicts the source.** `OperatingPoint.concentrations()`
  (`pbr/parameters.py:164-183`) divides by the reacting mole fraction, inflating every
  reactive partial pressure by $1/0.753 = 1.328$. The source's own published partial
  pressures confirm `y_i·P_total` instead — see §5.2b. **Invisible to the test suite: all 37
  tests pass with it present.**

### 4.3 Which candidate should the project use?

`[UNRESOLVED — HITL]` This is a supervisor/owner decision, not an agent's. What the evidence
says: `pbr` is architecturally ahead and its **Urmès2019 parameter set is verified against
the primary source** (§5.1), which is a stronger position than the older scaffold has ever
been in. But `pbr`'s surface dynamics are a placeholder, so neither candidate is the
proposal's model yet. The precise question for Damian is in §8.

---

## 5. Demonstrable findings, with re-derivable numbers

### 5.1 `[FACT: NEW — verified this run]` The `pbr` Urmès2019 parameters match the primary paper

Every map and dossier in this repository previously recorded this provenance as
**unverified**. It is now verified, from the PDF.

```
pixi run python Academics/BEP/Catalysis/3_Model/probes/verify_urmes2019_source.py
→ 24/24 checks PASS, exit 0
→ receipt: 3_Model/probes/urmes2019_source_receipt.json
```

| `pbr/parameter_sets.py` value | Primary source, Urmès et al. 2019 Table 5 | Verdict |
|---|---|---|
| `K_H2 = 13.0` | $K_1$ (Pa⁻¹) = 13 (fixed) | ✔ |
| `K_C2H2 = 107.0` | $K_2$ (Pa⁻¹) = 107 ± 7 | ✔ |
| `k04 = 1.4e8` | $k_{04}$ = 1.4 ± 0.1 × 10⁸ mol/(mol Pdₛ s) | ✔ |
| `K_C2H4_des = 7.4` | $K_5$ (Pa) = 7.4 (fixed) | ✔ |
| `k07 = 3.6e9` | $k_{07}$ = 3.6 ± 0.6 × 10⁹ mol/(mol Pdₛ s) | ✔ |
| `E4 = 48.5` | $E_4$ = 48.5 ± 4.2 kJ/mol | ✔ |
| `E7 = 54.8` | $E_7$ = 54.8 ± 11 kJ/mol | ✔ |
| `site_density = 2.0e-3` | $N_S$ = 2 × 10⁻³ mol/kg (fixed) | ✔ |

The rate equations and the site balance also match term for term, including the
$K_1/K_5$ factor that the source keeps separate — a factor whose omission would cost a
factor of 1.8 Pa⁻¹ on **every ethane rate**, i.e. exactly the reaction whose selectivity is
the point of the study.

### 5.2 `[FACT: NEW — verified this run]` The rate law reproduces the source's coverages at **11 of 12** checks

The package's own docstring calls the published coverage ranges "the only independent check
on the Langmuir terms this model can make". That check is now made — **and it does not fully
pass**:

```
pixi run python Academics/BEP/Catalysis/3_Model/probes/verify_pbr_implementation.py
→ GATE 1 FAIL (11/12 in range); GATE 1b PASS; GATE 2 PASS; GATE 3 PASS
```

**At the source's own stated pressure of 1.26 bar** (`Urmès 2019`, p. 10 of 13: *"the reactor
was operated at 1.26 bar"*):

| Condition | $\theta_{C_2H_2}$ | $\theta_{H_2}$ | $\theta_{C_2H_4}$ |
|---|---|---|---|
| Published range | 0.62 – 0.95 | **0.002 – 0.01** | 0.04 – 0.36 |
| op 1 @ 51 °C | 0.91711 ✔ | **0.00181 ✘** | 0.08108 ✔ |
| op 1 @ 62 °C | 0.91711 ✔ | **0.00181 ✘** | 0.08108 ✔ |
| op 2 @ 51 °C | 0.86908 ✔ | 0.00285 ✔ | 0.12805 ✔ |
| op 2 @ 62 °C | 0.89849 ✔ | 0.00221 ✔ | 0.09929 ✔ |

**11 of 12. The single failure is $\theta_{H_2}$ at operating condition 1, and it misses by
9.5 % of the way to the published lower bound (0.00181 vs 0.00200).**

> **This corrects a claim made earlier in this same mission.** A first pass of the probe used
> **1 atm (101325 Pa)** instead of the source's 1.26 bar (126000 Pa) and reported 12/12. That
> was wrong: the wrong pressure put $\theta_{H_2}$ at 0.00201, just *inside* the range.
> At the correct pressure it falls just outside. **The correction is recorded here rather than
> silently fixed**, because the difference between "the rate law reproduces the source" and
> "the rate law reproduces the source at 11 of 12 checks, missing on hydrogen coverage at the
> high-acetylene feed" is exactly the kind of distinction this briefing exists to preserve.

**What the near-miss probably means (stated as a hypothesis, not a finding):**
$\theta_{H_2} \propto \sqrt{K_1 p_{H_2}}$ and the denominator is dominated by the acetylene
term. Operating condition 1 has the highest acetylene fraction (1.0 % vs 0.6–0.8 %), so it
competes hardest for sites and drives the hydrogen coverage down. That is physically sensible
behaviour, and a 9.5 % miss against a published *range* (not a point value) may sit within the
source's own experimental scatter — the paper reports 95 % confidence intervals on the fitted
constants, and $K_2$ alone carries ±7 on 107.

`[UNRESOLVED:]` Whether the miss is (a) within the source's scatter, (b) a consequence of
comparing a mean-over-conditions range against a single-condition evaluation, or (c) a real
deficiency in the transferred rate law. **Distinguishing these needs the source's per-condition
coverage data, which is a figure in the paper and not a table of numbers.** That is a concrete
next action, not a conclusion.

### 5.2b `[FACT: NEW — verified this run]` `pbr`'s own feed conversion contradicts the source it cites

`pbr` offers two mutually exclusive ways to turn a mole-fraction feed into partial pressures,
and **they disagree by 33 %**:

- `y_i * P_total` — the standard physical reading.
- `OperatingPoint.concentrations()` (`pbr/parameters.py:164-183`) — divides by the **reacting**
  mole fraction, `sum(y_reactive)`, inflating every reactive partial pressure by
  $1/0.753 = 1.328$ for the source's Ar-bearing feed.

The source publishes its **own** partial pressures at 62 °C (Figure 7 caption:
$p_{C_2H_2} = 0.95$ kPa, $p_{H_2} = 5.5$ kPa) and states its total pressure. Those numbers are
independent of our model, so they settle the question:

| Species | Source states | `y_i·P` | error | `pbr` path | error |
|---|---|---|---|---|---|
| C₂H₂ | 950 Pa | 1260.0 Pa | +32.6 % | 1673.2 Pa | **+76.1 %** |
| H₂ | 5500 Pa | 5418.0 Pa | **−1.5 %** | 7194.8 Pa | **+30.8 %** |

**The hydrogen partial pressure settles it.** The source's stated 5.5 kPa matches
`y_i·P_total` to **1.5 %**, and matches `pbr`'s own conversion to within 31 %. The acetylene
row is consistent with the same conclusion once one accounts for the source reporting
$p_{C_2H_2}$ to two significant figures at a *different* operating point (0.95 kPa against the
1.26 kPa implied by the 1.0 % feed).

**Consequence:** `pbr`'s `concentrations()` inflates the driving force for every rate by 33 %
relative to the source it transcribes. This is a **fourth reproduced `pbr` defect**, and it is
invisible to the test suite — all 37 tests pass with it present.

`[UNVERIFIED:]` The docstring defends the rescale as a "void-volume conversion". A void-volume
correction is real physics, but it does **not** change partial pressure: the gas inside the
voids has the same composition as the bulk stream. So the stated justification does not
establish the behaviour.

### 5.3 `[FACT: this run]` The older defect register reproduces in full

```
pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py
```

| ID | Claim | Measured today | Verdict |
|---|---|---|---|
| D1 | RHS mutates the solver's state vector | **80** of 1,480 entries changed in one call, all in the `c_p` block, `r=9` (the Dirichlet shell) only; A/B `max|Δ| = 5.148` | reproduces |
| D2 | `r=0` symmetry coefficient is half the exact value | `f=r²`, `s=2`: exact **6.0000**, code **3.0000**, ratio **0.5000** | reproduces |
| D3 | `θ` at `r=R_p` never receives a derivative | `dTheta/dt` at `r=9` is all zero: **True** | reproduces |
| D4 | particle quadrature is first-order and drops `r=0` | weight at `r=0` = **0**; discrete/analytic ratio gives **16.0 %** low bias | reproduces |
| D5 | `R_gas` docstring unit is wrong; **both** `C_t` factors correct | `R_gas` evaluates to per-site `1/s`; docstring `[mol/kg_cat/s]` is wrong | reproduces |
| D6 | cost is the Jacobian, not the RHS | 1 rhs ≈ **0.022 s**; one FD Jacobian = 1,480 rhs ≈ **32.7 s**; 1 Jacobian in the probe | reproduces |

`[DECISION: `3_Model/state.md:65` and `:82`; framework §3.9 at `:114-116`]` **D5 is a
documentation defect, not a double normalisation.** The earlier "double `C_t`" claim was
**retracted** and must not be resurrected. Saying otherwise in front of Damian would be a
live error, not a conservative one.

`[FACT: this run]` **The seconds are not the claim.** Today's RHS measured 0.022 s against
the register's 0.016 s, and the Jacobian 32.7 s against 23 s. That is not a contradiction:
wall-clock on this machine is load-dependent (`3_Model/state.md:88-91`). The durable,
portable claim is **structural**: *the RHS is cheap and the dense finite-difference Jacobian
dominates*. Quote the structure, not the seconds.

### 5.4 `[FACT: NEW — verified this run]` The `pbr` test suite passes

The commit message on `e0663ba` claims "37 passing tests". That was a metadata claim, not a
result. It is now a result:

```
cd Methanol-Catalysis && python -m pytest tests/ -q
→ 37 passed in 24.16s
```

`[UNVERIFIED:]` The dossier also notes comments referencing `tests/test_chemistry.py`,
`tests/test_sweep.py`, `tests/test_parameters.py` and a
`test_particle_average_reproduces_bulk_source` that **do not exist** in the tree. Those
references cannot be treated as verification receipts for anything.

### 5.5 `[FACT: this run]` The 13-vs-14 count discrepancy resolves in favour of 14

`Academics/BEP/Catalysis/state.md:69` announces **"13 openstaande punten"** and then lists
`FW-1` through `FW-14` — fourteen atomic bullets, confirmed by reading them. Root
`task.md:197` says fourteen. **The register's count of 14 is right; the prose "13" is the
error.**

---

## 6. Unresolved defects and physical limitations

### 6.1 The transient bulk–pore inventory closure is an open physics question

`[UNRESOLVED:]` The implemented bulk source is a volume-average *gas chemical production*,
while the pore gas has separate transient accumulation. There is no surface diffusive uptake
or pore-accumulation correction. For a closed two-inventory interpretation:

```
ε_p · d⟨c_p⟩/dt = (3/R_p)·J_in + ρ_s·C_t·⟨R_gas⟩
bulk exchange  = (1−ε_b)/ε_b · ( ρ_s·C_t·⟨R_gas⟩ − ε_p·d⟨c_p⟩/dt )
```

The code retains the first term of the last line and **drops the pore-storage correction**.
A zero-reaction static diagnostic sets bulk uniformly equal to the inlet but the pellet
interior empty: every bulk derivative is zero while the interior pore derivative is positive
(H₂: 457.2 mol m⁻³ s⁻¹). Pore inventory fills without corresponding bulk uptake.

`[UNVERIFIED:]` This may be a deliberate quasi-steady pellet approximation or an imposed-
reservoir treatment. If so it needs to be **stated as an approximation**; it has not been.
**Fixing D1 does not resolve this.** It is a separate, physical question, and it is the one
most likely to be asked and hardest to answer.

### 6.2 Why a validated reacting periodic simulation has not been established

Four independent reasons, in dependency order. Each is a wall, not a scheduling problem:

1. **No kinetics.** All eight constants are zero. Nothing chemical can happen.
2. **No forcing.** The inlet is a fixed dict and the RHS never reads `t`. Periodic operation
   is not merely unvalidated — it is **not implemented**.
3. **No output metric.** There is no yield or selectivity calculation, so even a working
   reacting run would not report the quantity the thesis is about.
4. **Defects block parameter studies.** D1 makes the solver's stored trajectory not the
   trajectory the equations describe; D6 makes a sweep cost hours.

`[FACT: proposal]` **Even the proposal's own numeric claims are hypotheses, not results.**
It cites "up to a 40-fold rate enhancement" from thermal pulsing
(`main.tex:117`, citing Zhu et al. 2021) and describes "microsecond responses". Both are
inherited claims about *other* systems. The mission brief flags these explicitly as needing
primary evidence rather than acceptance from proposal prose. Do not put them on a slide as
our findings.

---

## 7. What can go on a slide, and what cannot

**Safe to present (each backed by a command in this document):**

| Slide-able claim | Backed by |
|---|---|
| The steady-state yield cap argument and why forcing could beat it | proposal §1, `main.tex:111-119` |
| Berger's pseudo-homogeneous balance + MOL + BDF is an established framework | Berger 2008 Fig. 5 |
| 1,480 state entries decompose as 80 / 800 / 600 | code arithmetic, §3.1 |
| The three discretisation choices and their trigger conditions | `conventions.md:177` |
| The six defects reproduce live, on this machine | `audit_2026_09_30.py`, §5.3 |
| `pbr`'s Urmès2019 parameters match the primary source | `verify_urmes2019_source.py` 24/24, §5.1 |
| The rate law reproduces the published coverages 11/12 (miss on $\theta_{H_2}$ at op 1) | `verify_pbr_implementation.py` GATE 1, §5.2 |
| `pbr`'s test suite passes: 37 tests | §5.4 |

**Must NOT appear as results:**

- ❌ A validated chemical simulator, or reactor yield/selectivity curves from either codebase.
- ❌ A measured periodic yield improvement — no periodic run exists.
- ❌ The 40-fold enhancement or "microsecond" timescales as *our* findings (proposal's
  inherited citations).
- ❌ "Readsorption is absent" — it is present (`:91`, `:94`, `:100`).
- ❌ A "double `C_t`" bug — retracted.
- ❌ A universal 16 % trajectory error — the 16 % is a **constant-rate** quadrature bias on
  this grid, not a trajectory error.
- ❌ `pbr` as "the working model" — its surface does not feed back into gas rates.
- ❌ Monday's 12-minute no-slides route as Wednesday's confirmed format.

**Disclaimers worth putting on the slide itself** (the runbook's "carry uncertainty on the
slide" rule):

> Model architecture and verification work. Kinetic parameters are being sourced; the
> periodic-forcing capability is not yet implemented. Numbers shown are reproducible
> diagnostics, not reactor predictions.

---

## 8. Next concrete milestones and questions for Damian

### Milestones, in dependency order

1. **Acquire Urmès et al. (2022), DOI 10.1002/cctc.202101826.** The direct periodic
   comparator is missing from the library. Equations, supplementary material, and whether
   the corresponding author's data offer includes code.
2. **Close the inventory-closure question (§6.1).** Decide between a conservative
   surface-flux closure, a documented quasi-steady pellet approximation, or another
   justified effective-storage formulation — and write the choice down.
3. **Wire the surface feedback in `pbr`.** Make `rate.rates` accept `theta` and use the
   returned surface derivatives. This is the single change that turns `pbr` from a PSSA
   model with decoration into the proposal's model.
4. **Fix the two reproduced `pbr` defects** (broadcast, sparsity size). Both are small and
   both block a resolved-pellet run.
5. **Implement periodic forcing and a cycle-averaged yield metric**, then define the
   equal-feed steady reference the improvement is measured against.

### Questions for Damian — these are yours to ask, not ours to answer

1. **Which candidate?** `pbr` is architecturally ahead and its Urmès2019 parameters now
   verify against the primary source, but its surface dynamics are a placeholder. The older
   scaffold is self-contained but has six reproduced defects and no kinetics. Is
   repairing `pbr` the intended path, or is it a comparison target only?
2. **Scope of the radial dimension.** The resolved intra-particle coordinate is *our*
   extension, not Berger's, and it is the source of three of the six defects. Is radial
   resolution required for the BEP deliverable, or is Berger's
   $(N_{gas}+N_{surf})\times N_z$ form the honest baseline?
3. **Film resistance: solve it or drop it.** Pseudo-homogeneity *is* Berger's model, so
   dropping the film is defensible — but then the film switch should not exist in the code.
4. **What counts as a credible predictor?** Which measured output, over which operating
   range, at what error tolerance. Without this, "validated" has no test.
5. **Is optimisation still in scope for this BEP?** The proposal includes it; the current
   mission narrows to the open-loop predictor. If it stays, the cycle-averaged metric and
   the equal-feed steady reference need defining.

`[UNRESOLVED — HITL]` None of the five is answerable from the repository. They are recorded
as open questions in the Wayfinder maps and are **not** marked closed here.

---

## 9. Reproducing everything in this document

```bash
# from the workspace root
pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py
pixi run python Academics/BEP/Catalysis/3_Model/probes/verify_urmes2019_source.py
pixi run python Academics/BEP/Catalysis/3_Model/probes/verify_pbr_implementation.py

# the sibling package's own suite
cd "../Methanol-Catalysis" && python -m pytest tests/ -q
```

| Artefact | Path |
|---|---|
| Defect probe | `3_Model/probes/audit_2026_09_30.py` |
| Primary-source verification | `3_Model/probes/verify_urmes2019_source.py` |
| Receipt | `3_Model/probes/urmes2019_source_receipt.json` |
| `pbr` verification gates | `3_Model/probes/verify_pbr_implementation.py` |
| Receipt | `3_Model/probes/pbr_implementation_receipt.json` |
| Evidence bundle index | `research/briefing/evidence/README.md` |

**Hashes of the inspected sources** (so a later reader can tell whether anything moved):

| File | SHA-256 |
|---|---|
| `3_Model/c2h2_hydrogenation_transient_model.py` | `6764e1b663128e1c969ff990a73c8e3454600a1c7ae4f8323bf08f07bc948b25` |
| `3_Model/probes/audit_2026_09_30.py` | `bde32abd16562463e3cb695b57d991fd746d8de9ce676aab2843d5bc5a60df18` |
| `Articles/acquired_pdfs/urmesKineticStudySelective2019.pdf` | `8ad818fd2cc3c386457855b558c29af737d2b7b12bdaf3f399d551b6f5d10c01` |
| `Methanol-Catalysis/pbr/chemistry.py` | `339adb98ab0e471730699daa652e275c5231fc4be3f6be82918f873eb52e1b14` |
| `Methanol-Catalysis/pbr/parameter_sets.py` | `37b72e933ffb24c7c8f7ba2f473a7822a18b86e5181e73de93e055d0af9a73d7` |
| `Methanol-Catalysis/pbr/solver.py` | `f4ebb94e7f201a1ba63e4e1d28a24f1137f0519b6339087c2338cb8459643567` |
| `Methanol-Catalysis/pbr/closures.py` | `256027f425537c4dd4a7e869d76d248b6ce663035228e1151ec13783e213d968` |
| `Methanol-Catalysis` HEAD | `e0663ba9305086bcc3b9f0689270e93993316a9f` |

---

*Companion documents: [`spoken_update.md`](spoken_update.md) (60–90 s update),
[`technical_qa.md`](technical_qa.md) (Lucas technical Q&A),
[`wednesday_handoff.md`](wednesday_handoff.md) (presentation handoff).*
