# Transient PBR Model — Framework Audit vs. Berger (2008)

**Source artefact:** Gemini chat [`gemini_transcript_2026-09-29_83878835991845b5.md`](gemini_transcript_2026-09-29_83878835991845b5.md) (30 msgs, chat `83878835991845b5`, exported 2026-09-29 23:44 CEST) + its Canvas *"Transient Reactor Model Structure"*. The Canvas was exported by hand; this audit covers the transcript copy, which contains the full Canvas text at lines 347–886.

**Audit date:** 2026-09-30. **Baseline for every check below:** [`dynamic_kinetics_berger2008.md`](../Articles/analyses/dynamic_kinetics_berger2008.md) and [`bergerDynamicMethodsCatalytic2008_consensus.md`](../Articles/paper_analyses/bergerDynamicMethodsCatalytic2008_consensus.md).

**Verdict:** the model *architecture* in the Canvas is sound and the decisions taken in the conversation are good. The *equations as written* do not survive contact with Berger (2008): four numerical conflicts, one dimensional error, one hard contradiction inside a single response, and one missing requirement the same response insists on. Fix the **nine** items in §3 before any of this reaches code.

---

## 1. What the conversation settles

These are decisions, not open questions. They are now the model spec.

| # | Decision | Status | Note |
|---|---|---|---|
| D1 | Three coupled levels: bulk gas `C_b(z)` → film `C_s(z)` → intraparticle `c_p(z,r)` → surface coverage `θ(z,r)` | ✅ Confirmed | The `r` dimension is **our** extension; Berger Eq. (1) has no radial coordinate and no film term. |
| D2 | Keep `C_b` and `C_s` **structurally separate** in code, but **equalise** `C_s = C_b` to recover Berger's collapsed form | ✅ Confirmed | This is exactly right, and for a reason the transcript never states: Berger Eq. (1) has no film term at all, so pseudo-homogeneity *is* Berger's model. Separate-then-equalise buys the extension for free. |
| D3 | Intraparticle diffusion is **explicit**, never instantaneous | ✅ Confirmed (user override of Gemini) | Directly contradicts the Berger state count `(N_gas + N_surf) × N_z`. Costs a factor `N_r` in state count. Must be justified in the thesis as a deliberate upgrade, not smuggled in. |
| D4 | Rate = `[Arrhenius]` × `[Langmuir]` — complementary axes, not alternatives | ✅ Confirmed | Correct. Arrhenius = `k(T)`, Langmuir = coverage dependence. |
| D5 | Centered Arrhenius for `k_p(T)` | ✅ Matches source | Identical to Berger Eq. (17). The chat lost Berger's *reason* (binary correlation `< 0.71`) — keep the reason. |
| D6 | Forward simulation on **literature values first**; fitting is a later, optional stage | ✅ Confirmed | Correct sequencing. Nothing in the framework needs a fit to run. |
| D7 | Numerics: MOL; bulk advection = backward/upwind difference; particle diffusion = central difference; time = implicit BDF | ⚠️ Partly implemented | See §3, item 7 — the `r = 0` node breaks the central-difference rule. |
| D8 | Swapping a new chemical system = new elementary steps + stoichiometry + rate-law form, no engine change | ✅ Confirmed | True, *provided* the rate laws stay in the declared Langmuir/Arrhenius family. |

---

## 2. Numerical conflicts with Berger (2008)

Every threshold in the chat is checked against `dynamic_kinetics_berger2008.md:52-57` (Table 2, "Dekker/Berger transient criteria").

| Quantity | Chat says | Berger says | Verdict |
|---|---|---|---|
| Carberry `Ca` | `< 0.05` | `< 0.05` | ✅ agree |
| Extraparticle Prater `\|β_ex γ_E Ca\|` | `< 0.05` | `< 0.05` | ✅ agree |
| Intraparticle Prater `\|β_in γ_{E,s}(η_in φ²)\|` | `< 0.05` | `< 0.05` | ✅ agree |
| **Wheeler–Weisz `η_in φ²`** | **`< 0.05`** | **`< 0.1`** | ❌ **conflict — use 0.1** |
| **Transient time, internal** | `τ_in = (ε_p R²/D_e)·t ≥ 0.25` | `t_in = (D_e/(ε_p R²))·t ≥ 0.25` | ❌ **reciprocal, same threshold — one is wrong** |
| **Transient time, external** | `τ_ex = k₀·k_g a·t ≥ 2.9` | `t_ex = (k_g a/ε_b)·t ≥ 2.9` | ❌ **spurious `k₀`, missing `ε_b`** |
| Particle size window | 100–300 μm | `d_p ≤ 300 μm` fine; dossier uses ≈100 μm | ✅ consistent |

**On the internal transient time.** `(D_e/(ε_p R²))` has units of 1/s, so `t_in` as Berger writes it is *dimensionless* and a threshold of 0.25 is meaningful. The chat's `(ε_p R²/D_e)·t` is a *dimensional* time, so `≥ 0.25` is being compared against a quantity with units — the threshold does not transfer. One of the two is the reciprocal of the other, so this is not a rounding difference. **Berger wins; the chat's form is wrong.**

**On `Ca ≤ 0.15` / `Da_II ≤ 0.3`.** Those appear in `literature_analysis.md:40-41` — a *different* paper (the methanol one). Thresholds are paper-specific. Do not average them, do not cite them for Berger.

---

## 3. Defects in the model's own equations

Ordered by how expensive they are to find later.

### 3.1 The displayed bulk equation contradicts Berger's Eq. (1) by a factor `ε_b²`

Berger Eq. (1), as recorded at `dynamic_kinetics_berger2008.md:27`:

```
∂C_i/∂t = −(u_s/ε)·∂C_i/∂z + D_ax·∂²C_i/∂z² + (ρ_s/ε)(1−ε_b)·C_t·R_i
```

The chat's displayed equation instead shows `−ε_b·u_s·∂C/∂z` and `−ε_b·k_g a·(C_b − C_s)`, and drops the `R_i` source term entirely.

- Advection: the chat's coefficient is `−ε_b·u_s`, Berger's is `−u_s/ε`. The ratio chat/Berger is `ε_b²`; at `ε_b ≈ 0.4` that is `0.16×`, i.e. **Berger is 6.25× larger** on the dominant term. (Stated the other way round it reads as a contradiction, so keep it in this direction.)
- The film term needs `(1−ε_b)`, not `ε_b` — `ε_b = 0.4` vs `1−ε_b = 0.6`, and it is a different quantity entirely (void fraction vs. solids fraction), not a rounding.
- The `R_i` volumetric source and the `k_g a` film flux are **two different closures**, not two ways of writing one. Berger's Eq. (1) is lumped and has no film resistance; the chat's is an explicit film closure. They cannot share an equation.

**The pseudocode, by contrast, reproduces Berger Eq. (1) term for term** — `dCb_dt = −(u_s/ε_b)·(C_b[z]−C_b[z−1])/dz + (ρ_s(1−ε_b)C_t/ε_b)·∫R_i dr`, with `D_ax` dropped per the stated high-flow simplification. **So the two artefacts in the same document disagree, and the pseudocode is the correct one.** Delete the displayed equation, or fix it to Eq. (1) and put the film term in a clearly-marked alternative branch.

One qualification, so this is not read as a licence to code: "term for term" holds **only under the identification `ε ≡ ε_b`**, which is exactly the ambiguity left open below. Berger writes a bare `ε`; the pseudocode writes `ε_b`. That is the only difference, but it is the one that cannot be settled from the dossier.

**Open source ambiguity, not resolvable from the dossier:** the local annotation calls `u_s/ε` the "interstitial velocity" (`dynamic_kinetics_berger2008.md:30`). Taken literally, a superficial-flux balance with interstitial velocity and no `ε_b` on storage is inconsistent. Either Berger is loose in the annotation, or `u_s` in Eq. (1) already means interstitial. **Check the PDF before coding** — this changes what `u_s` means everywhere downstream, including the `f_max` derivation in the transport-criterion action item.

### 3.2 The `r = 0` branch is wrong twice

```
If r == 0:  dcp_dt = (D_e/ε_p)·6·(c_p[r+1] − c_p[r])/dr² + (ρ_s C_t/ε_p)·R_i
```

- The `6/dr²` factor is the spherical-centre limit, valid only for `s = 2`. The document presents `s` as a free geometry parameter (0 slab, 1 cylinder, 2 sphere), so for a slab or cylinder this branch is simply wrong.
- It reads `c_p[r+1]` from the centre node. The centre has no centred stencil at all — that is the *only* reason the special case exists — so this is necessarily a one-sided difference, and one-sided is not what was chosen. The correct treatment is the regular second-order central stencil for `r ≥ 1` and a ghost-node construction at `r = 0` (`c_{−1} = c_{1}`), which restores the factor-6 symmetry instead of approximating around it.

### 3.3 Readsorption is missing from a model whose source demands it

The same conversation, one message earlier, states that readsorption in TPD is **the only explicit modelling requirement** of the review's Section 5 and that it "should be incorporated in the particle and reactor modelling". The Canvas model contains no readsorption term, no TPD desorption channel, and no readsorption parameter. One response flags the requirement; the next delivers a model without it. **The chat is internally inconsistent.**

Consequence for the BEP: if a TPD step is ever used to extract parameters, the current framework is not the model the source asks for, and the transport-criteria story does not close.

### 3.4 `C_s = C_b` is a hard assignment, not a switch

§4.1 says the two concentrations are kept separate and equalised. The pseudocode performs `C_s[z] = C_b[z]` *inside* the `z` loop, so the film term is dead code — it cannot be re-enabled without editing the RHS. Make it a parameter (`film_resistance: bool`), evaluated once before the bulk RHS, so D2 stays true and D3 stays switchable.

### 3.5 "State-space ordering" is a coupling problem, not an ordering problem

The user's note in the transcript is *"I need to do the right order to remain within state space"*. Worth writing down precisely, because as stated it is not quite the issue:

- Under **pseudo-homogeneity** (`C_s ≡ C_b`), there is no ordering to get right. The film term is dropped, `C_s` is not a state, and the loop order is irrelevant.
- Under **explicit film resistance**, `C_s` is a *dependent* variable of `C_b` and `c_p|_{r=R}` — it is an algebraic function of two states, not a third state. It cannot be "equalised" and simultaneously be solved. Either solve the flux balance
  `k_g a (C_b − C_s) = −(3/(R))·D_e·(∂c_p/∂r)|_{r=R} · (1−ε_p)/(1−ε_b)`
  or drop it. There is no third option, and no loop ordering makes one exist.

So: pick the closure once, make it a flag, and the ordering question dissolves.

### 3.6 No energy balance, and the exotherm leg is in scope

`state.md:4` scopes the modelling as "isothermal **→ exotherm**". The Canvas states "No energy balance PDE is required" and drops both Prater numbers along with them. That is consistent *for an intrinsic-data PBR*, and inconsistent *with our own scope*. If the exotherm branch stays in scope it needs at least a lumped film/catalyst energy balance coupled to the Prater test, or that half of the project has no model behind it. Scope decision, not a coding bug — but it must be made explicitly.

### 3.7 `Bim` is defined twice, inverting

Same response: `Bim = k_g R/D_e` in the body, `Bim = D_e k_g R` in the summary table. The former is the standard mass Biot number. Transcription error; must not reach the code.

### 3.8 Scheme inconsistency across the two chats

Sibling chat [`7378843f85f483d1`](gemini_transcript_2026-09-29.md) fixes: bulk = backward/upwind, particle = central, time = BDF. This chat's pseudocode is backward/upwind in the bulk ✅, but breaks the central rule at `r = 0` (§3.2). The agreed scheme is not actually implemented.

### 3.9 One symbol, two rate normalisations

`R_j` is the surface balance RHS in `∂θ_j/∂t = R_j` (per site) and `R_i` is the gas balance source after multiplication by `ρ_s C_t/ε_p` (per volume). The Canvas uses `R` for both and never states the units. Write an explicit units column before coding, or the stoichiometry sum in §3.1 will silently carry a `C_t` error.

---

## 4. Unverified — must not be cited (Rule 16)

None of the following appear in `references.bib`, the local Berger dossier, or `Articles/acquired_pdfs/`. They are Gemini's rendering of a source we have not opened at the cited page. **Eight are `UNVERIFIED`; the ninth row is the one confirmed item and is listed for completeness.**

| Claim in chat | Status |
|---|---|
| Source paper is the review's "Section 5" | Substance matches Berger (2008) Table 2 (`dynamic_kinetics_berger2008.md:52-57`) and the project already calls it "Berger §5" (`conventions.md:161`). But the dossier numbers the criteria as **Table 2** and the equations as **Section 4 & Figure 5**, so the chat's "Section 5" and the dossier's numbering disagree. Low stakes, but fix one of them before quoting a section number. |
| "Dekker et al." transient criteria | Dossier says "Dekker/Berger". Author attribution unconfirmed. |
| "Gleaves et al." TAP criterion `H_p t_p ≤ 0.31` | Absent from the local dossier. Unverified. |
| `ΔP < 0.1 bar` bed pressure-drop limit | Absent from the local dossier (which uses `< 0.2 bar`, and for a *different* paper). Unverified. |
| Gorte's six dimensionless groups for TPD readsorption | Absent from the local dossier. Unverified. |
| "120 μm Cu–Cr, criteria met in ≈1 ms" | Dossier has a comparable claim for 100 μm PdAg/α-Al₂O₃ (`dynamic_kinetics_berger2008.md:80`). Different catalyst, different number. Do not merge. |
| Valve switching 8 ms; MS response 0.1–1 s | No source found. Unverified — and load-bearing, since it sets the fastest resolvable step. |
| "SO₂/NOₓ adsorption → 3D CFD pilot-plant riser" | No such paper in `acquired_pdfs/`. Unverified. Drop it unless it can be sourced. |
| Parameter-correlation figure "below 0.71" | In the dossier (`:66`) as Berger's claim. Chat omitted the number; keep it. |

---

## 5. Still undefined (Gemini agrees)

1. Elementary mechanism (adsorption / surface reaction / desorption set).
2. Stoichiometry matrix `ν`.
3. Rate-law functional form per step (Langmuir, LHHW, Elovich — the Larsen `r_{1,max}` cap and non-linear `n_inh` inhibition belong here).
4. Literature values: `ε_b, ε_p, ρ_s, C_t, D_e, k_g, k_p,ref, E_p, K_i`.
5. `D_ax` and its switch, if the high-flow simplification is ever relaxed.
6. **Energy balance**, per §3.6 — open scope decision.
7. **Readsorption closure**, per §3.3 — required if TPD enters.

---

## 6. Provenance

- Transcript: [`gemini_transcript_2026-09-29_83878835991845b5.md`](gemini_transcript_2026-09-29_83878835991845b5.md) — 30 msgs, `/u/3/`, `83878835991845b5`.
- Sibling chat, same session, 9 min earlier: [`gemini_transcript_2026-09-29.md`](gemini_transcript_2026-09-29.md) — 7 msgs, `7378843f85f483d1`, where the numerics and the `ModelParams` skeleton were set.
- Raw export: `.agents/triage/gemini_import/83878835991845b5_{transcript.md,messages.jsonl,dom.html}`.
- Code target: [`c2h2_hydrogenation_transient_model.py`](c2h2_hydrogenation_transient_model.py). ~~Not yet audited against §3~~ — **audited 30-09.** A second, independent audit ran the script and registered 6 code defects in [`state.md`](state.md) § Defect register. It **confirms** §3.3 (readsorption absent), §3.4 (`C_s = C_b` hard assignment, same line as its D1), §3.5 and §3.6 (no energy balance), and restates §3.9 as its D5. It **adds** findings this document does not contain: the RHS mutates the solver's state vector through a `reshape` view; $\theta$ on the pellet shell never receives a derivative; the particle-volume quadrature is first-order; the `r=0` factor is `(1+s) = 3` where the chat specified and this audit endorses `6`; and the rhs costs ~2.2 s per call. Still **not** a spec implementation.
