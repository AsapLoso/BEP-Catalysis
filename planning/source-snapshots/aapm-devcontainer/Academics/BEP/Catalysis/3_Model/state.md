# 3_Model — Transient PBR Model: State

Parent: [BEP Catalysis (Urakawa Group)](../state.md) · Transcript: [`gemini_transcript_2026-09-29.md`](gemini_transcript_2026-09-29.md)

## Source chats (Gemini, exported)

| Chat | Link | Transcript | Msgs |
|---|---|---|---|
| **Primary** — the `.py` came from here | <https://gemini.google.com/u/3/app/7378843f85f483d1> | [`gemini_transcript_2026-09-29.md`](gemini_transcript_2026-09-29.md) | 7 |
| Sister chat — framework/derivation theory | `83878835991845b5` | [`gemini_transcript_2026-09-29_83878835991845b5.md`](gemini_transcript_2026-09-29_83878835991845b5.md) | 30 |

Both exported 2026-09-29 via `.agents/triage/gemini_import/gemini_chat_export.py` (Selenium/Firefox).
The `/u/3/` segment is a real account path, **not** part of the chat ID — it must be preserved to
reopen the chat. Raw exporter artifacts (untracked): `.agents/triage/gemini_import/7378843f85f483d1_{transcript.md,messages.jsonl,dom.html}`.

- **Status:** 🟡 SCAFFOLD ONLY — runs, but every kinetic constant is `0.0`.
**Open:** **6 code defects, 3 blocking** (D1, D2, D3), plus 2 low-severity notes in the register.
**Last audit:** 2026-09-30 · **Corrected:** 2026-09-30 (post-audit; see `history.log`)

> **Twee audits, niet één — lees beide voordat je `c2h2_hydrogenation_transient_model.py` aanraakt.**
> 1. [`transient_model_framework_audit.md`](transient_model_framework_audit.md) — het **framework**
>    (de 30-berichten zusterchat `83878835991845b5`) tegen Berger (2008) gehouden: 8 *model*-defecten
>    ($\varepsilon_b^2$ in de bulkbalans, reciproke $t_{in}$, ontbrekende readsorption, geen energiebalans)
>    plus een UNVERIFIED-citeerlijst. Dat is een **papier-versus-bron**-vergelijking.
> 2. **Onderstaande register** — het **script uitgevoerd** in plaats van gelezen: 6 *code*-defecten.
>    Dat is een **numerieke** vergelijking, tegen analytische oplossingen en een A/B-run.
>
> **Correctie (30-09, na audit):** een eerdere versie van dit bestand stelde dat de twee audits
> "overlappen op één punt" en dat hun punt 6 "hetzelfde defect" is als D2. **Dat was onjuist.**
> Ze raken dezelfde coderegel maar stellen **twee verschillende diagnoses**:
> §3.2 van de framework-audit bekijkt de **chat-pseudocode** en zegt dat de daar hard-coded `6/dr²`
> alleen geldig is voor $s=2$ en éénzijdig is in strijd met de central-difference keuze; het
> noemt `(1+s)` of `2(1+s)` niet. **D2** ziet het **script** en stelt vast dat het `(1+s) = 3`
> gebruikt waar de exacte sferische limiet `6` is. Dat de audit §3.2 juist `6` als correct
> beoordeelt is een **bevestiging** van de richting, geen duplicaat van de bevinding — en het
> feit dat het script `3` gebruikt waar de chat `6` voorschrijft is een **eigen** afwijking die
> geen van beide audits eerder had opgemerkt.
>
> **Echte overlap is er wél, op vier punten** — geen één:
> | Framework-audit | Register | Aard |
> |---|---|---|
> | §3.9 één symbool, twee snelheidsnormalisaties | **D5** | **Zelfde onderwerp** (de `C_t`-vraag) |
> | §3.4 `$C_s = C_b$` is een harde toewijzing | deels **D1** | Zelfde coderegel (`c_p[z,-1,:] = C_s`), verschillende klacht: begrenzingsconditie vs. state-mutatie |
> | §3.3 readsorption ontbreekt | — | Bevestigd **aanwezig** in het script; nog niet als register-item geadministreerd |
> | §3.6 geen energiebalans | — | idem |

## What the model is

`c2h2_hydrogenation_transient_model.py` — Method-of-Lines PBR model, 1480 ODEs
(`N_z=20` axial × `N_gas=4` bulk, `N_r=10` radial × 4 pore, `20×10×3` surface coverage),
`BDF` on `solve_ivp`, default span `t ∈ [0, 10]` s.

Discretisation choices, as confirmed in the transcript: **upwind/backward difference for the bulk
advection**, **central difference for intra-particle diffusion**, **implicit time stepping** because
the chemistry is stiff. Those three choices are correct for their stated reasons.

## 🔥 Direct Action Items (Ball in User's Court)

- [ ] **[DUE: 2026-10-07] 🔥 WALKTHROUGH — demo "wat ik heb gebouwd en bewezen", ~12 min, klaar voor morgen.** Het verhaal is sterker dan "ik heb een script": je hebt een Gemini-gegenereerd model **onafhankelijk numeriek geaudit** en er **6 defecten uit gehaald, 3 blokkerend, elk met reproduceerbaar bewijs** — en daarna de literatuur eronder gelegd. Route: (1) deze `state.md` — vooral de register-tabel en het blok over de twee audits (2 min); (2) `c2h2_hydrogenation_transient_model.py` — 1480 ODE's en de drie discretisatiekeuzes mét hun reden (3 min); (3) **`pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py` live draaien** — dit is het sterkste moment, de cijfers ontstaan ter plekke in plaats van uit een slide (5 min); (4) de vier échte overlap-punten framework-audit ↔ register (2 min). **Niet tonen:** de performance-log en de D6-Jacobian-kosten — die horen bij een parameterstudie, niet bij een introductie. **Voorbereiden:** één pagina met de register-tabel plus de herleidbaarheid van elk getal, en antwoord op de vraag die je zelf moet kunnen stellen: *"welke van deze zes is een fix en welke een keuze?"* — D1/D2/D3/D4 zijn fixes met een bepaald juist antwoord, D5 is een conventievraag, en de film-/dispersie-afweging is een keuze die je in de tekst moet staan.
- [ ] **[DUE: 2026-10-02] D1 — Make the rhs non-mutating (correctness, blocking):** `reactor_model` writes the Dirichlet shell into the caller's state vector (`c_p[z, -1, :] = C_s` on a `reshape` **view** of `y`). Measured: **80 of 1480** state entries are modified by a single rhs call, and A/B against a `y.copy()` wrapper gives `max|Δ| = 5.1` at `t=0.2` s. The solver's stored trajectory is therefore not the trajectory the equations describe. Fix by unpacking `y` into fresh arrays instead of a view. [D1](state.md)
- [ ] **[DUE: 2026-10-02] D2 — Correct the `r=0` symmetry factor (2× error):** the centre node uses `(1+s)(c₁−c₀)/dr²`, i.e. `3` for `s=2`. The exact limit of $\frac{1}{r^s}\frac{d}{dr}(r^s f')$ at $r\to0$ is $2(1+s)(c_1-c_0)/dr^2$, i.e. `6` — **the code is half of correct**. Verified against the analytic solution `f = r²` (`f''=2`, exact operator value `6`, code gives `3`); the file's own comment (`"voor sfeer is het 6 ipv 2"`) also states `6`. **Note:** the chat's pseudocode specified `6/dr²` and the framework audit's §3.2 endorses `6` as the correct spherical limit, so the script **deviates from its own spec by a factor 2** on top of being `s`-dependent and one-sided (§3.2). Distinct finding from §3.2, same line. [D2](state.md)
- [ ] **[DUE: 2026-10-02] D3 — Surface coverage at the pellet shell is frozen:** `dTheta_dt[z, N_r-1, :]` is never assigned, so the `N_r` radial nodes of $\theta$ keep only `N_r-1` live layers. Confirmed: `np.all(dTheta[:, -1, :] == 0)` is `True`. The shell is where the gas actually touches the catalyst, so this deletes the surface kinetics where they matter most. [D3](state.md)
- [ ] **[DUE: 2026-10-03] D4 — Volume quadrature drops the `r=0` node and the `4π` (convergence):** `volume_gewicht = r_radius**s * dr` is zero at `r=0` for `s=2`, so the centre node carries no weight, and the left-endpoint sum is normalised by the *analytic* `R_p^(s+1)/(s+1)` instead of by the discrete sum. Measured at `N_r=10`: the discrete sum is **83.95%** of the analytic normaliser, so the particle-averaged rate is **biased ~16% low**. Converges as `O(dr)`, not `O(dr²)`. *(Corrected 30-09: the register previously said 97.1%/2.9%; that came from adding an untrapezoid half-weight the code does not apply. See `history.log`.)* [D4](state.md)
- [ ] **[HORIZON: 2026-10] Fill `ModelParams.kinetics` from literature:** all 8 entries ship as `(0.0, 0.0)`, so the model integrates pure transport and the chemistry never switches on (verified: state stays identically `0`). Every value must come from a `resources.md` row — **no invented constants** (Rule 16). Arrhenius `$E_a$` is stored but the `k` lambda ignores it and uses `k_ref` flat, so temperature has no effect until that is written. [resources.md](resources.md)
- [ ] **[HORIZON: 2026-10] D5 — Settle the `$C_t` normalisation question (unit question, NOT a fix):** `transfer_term` uses `rho_s*(1-eps_b)*C_t/eps_b * R_gas` and the intra-particle term uses `rho_s*C_t/eps_p * R_gas`, with the same `R_gas`. `R_gas` is built as `k·c·θ^k` type products, so it carries units of **`1/s` (per site)** — the `[mol/kg_cat/s]` in the function docstring is **wrong**. On that reading **both** `$C_t$` factors are correct and there is no defect here. What *is* real is the docstring error and the fact that the same symbol denotes site-normalised and volume-normalised quantities without a units column — which is the framework audit's **§3.9**, verbatim. **Earlier claim retracted:** this file previously asserted `$R_gas$` "is already site-normalised, so the bulk term carries a second `$C_t$`". That premise was self-contradictory (a `[1/s]` rate is not site-normalised) and the conclusion does not follow. Verify the intended convention against Berger Eq. (1) before touching code. [D5](state.md)
- [ ] **[HORIZON: 2026-10] D6 — Make the run affordable (blocking for any parameter study):** the cost is **not** the rhs, it is the **finite-difference Jacobian**. One rhs call is **0.016 s**; one Jacobian costs `DIM = 1480` rhs calls = **23 s**, and `BDF` needs a fresh one as the state moves. A `t ∈ [0, 0.2]` s probe took 46 s wall with `nfev=62`, `njev=1`. The shipped `t_span` of `[0, 10]` s needs orders of magnitude more, so it is **hours** — and the fix is `jac_sparsity=` (the system is block-tridiagonal) or an analytic Jacobian, not vectorising the `for z` loop. *(Corrected 30-09: the register previously said "~2.2 s per rhs call". That figure was `wall/nfev`, which silently folded in the Jacobian work. See `history.log`.)* [D6](state.md)
- [ ] **[HORIZON: 2026-10] Reconcile with the `1_Transport_Phenomena` reference:** the reference PDE carries axial dispersion $D_{ax}\partial^2 C/\partial z^2$ and an external film coefficient $k_c$ with Danckwerts BCs. The code implements **plug flow + pseudo-homogeneous** ($C_s = C_b$, no film resistance, no dispersion). That is a legitimate candidate reduction — it is exactly the `$Pe \gg 100$` case — but it is a *choice*, and it should be stated as one rather than silently assumed. [pbr_transport_phenomena.md](../1_Transport_Phenomena/pbr_transport_phenomena.md)

## ⏳ Open Communication Lines (Ball in External Court)

*None.* The `3_Model` submap has no outstanding external dependency. (Whether the supervisor
Bijoy Bera accepts the Upwind/Central/BDF reduction is a **conversation to be had**, not yet a
pending question — no mail has been sent, so per Rule 17 it does not belong in this table.)

## Defect register

| ID | Defect | Severity | Evidence | Fixed? |
|---|---|---|---|---|
| D1 | rhs mutates the solver's state vector (`reshape` view written in place) | **Blocking** | 80/1480 entries mutated; A/B `max|Δ| = 5.1` | ☐ |
| D2 | `r=0` symmetry coefficient is ½ of the exact value (code `3`, exact `6`) | **Blocking** | analytic `f=r²`: exact `6`, code `3` | ☐ |
| D3 | $\theta$ at `r = R_p` never receives a derivative | **Blocking** | `all(dTheta[:, -1, :] == 0)` | ☐ |
| D4 | particle-volume quadrature is `O(dr)` and drops `r=0` | Medium | discrete/analytic sum = `0.840` → **16% low** | ☐ |
| D5 | `R_gas` docstring unit wrong; same symbol used for site- and volume-normalised rates (= framework §3.9). **No double-`C_t` defect — earlier claim retracted** | Medium | dimensional reading | ☐ |
| D6 | rhs is 0.016 s but a finite-difference Jacobian costs `1480` rhs calls = 23 s | **Blocking for any sweep** (not for a single run) | `t∈[0,0.2]`s: 46 s wall, `nfev=62`, `njev=1` | ☐ |
| — | `$E_a` parsed but unused; temperature inert | Low | `k = lambda name: p.kinetics[name][0]` | ☐ |
| — | all kinetic constants are `0.0` | By design | state stays identically `0` | n/a (see fill task) |

**Every number in this register is re-derivable:** [`probes/audit_2026_09_30.py`](probes/audit_2026_09_30.py)
(`pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py`). Wall-clock
figures are load-dependent on this machine — the *structure* (rhs cheap, Jacobian dominant)
is the durable claim, not the seconds.

## Performance log

| Run | Grid | Span | `nfev` | `njev` | Wall (s) | Note |
|---|---|---|---|---|---|---|
| shipped defaults | 1480 | `[0, 10]` | — | — | 17.1 | all-zero kinetics, trivial |
| `ads_H2=5` | 1480 | `[0, 1.0]` | 98 | — | 219.2 | `θ` still ~`1e-36` at 1 s |
| `ads_H2=5` | 1480 | `[0, 0.2]` | 62 | 1 | 45.7–224.4 | 45.7 s unloaded, 224 s under parallel-session load |
