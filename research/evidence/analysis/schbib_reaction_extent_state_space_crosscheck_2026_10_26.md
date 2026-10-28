# Schbib (1996) — independent reaction-extent integration cross-check

**Date:** 2026-10-26. **Status:** independently executed *internal numerical verification*, **not** experimental validation or a new kinetic fit.
**Source-specific context:** audit [report](../../reports/schbib_parameter_and_benchmark_audit.md), [audited six-species notebook](../../../notebooks/benchmarks/schbib_1996_steady_state.ipynb), [results JSON](../derived/schbib_1996_audit_results.json). Original paper, Table 8 (printed p. 1502); Table 6 (printed p. 1499); author-shared correction **unverified visually**.

## Technique and state-space choice

Use a catalyst-mass coordinate \(W\), with two cumulative reaction extents \(\xi_1,\xi_2\) expressed as **kmol/s**, for:

1. \(C_2H_2 + H_2 \rightarrow C_2H_4\)
2. \(C_2H_4 + H_2 \rightarrow C_2H_6\)

\[
F(W) = F_0 + N\xi(W), \qquad \frac{d\xi}{dW} = \begin{bmatrix}r_A(F_0+N\xi)\\r_E(F_0+N\xi)\end{bmatrix},
\quad
N=\begin{bmatrix}
0&0\\-1&0\\1&-1\\0&1\\-1&-1\\0&0
\end{bmatrix}
\]

Species row order: CH4, C2H2, C2H4, C2H6, H2, CO. Thus
\(F_A=F_{A0}-\xi_1\), \(F_E=F_{E0}+\xi_1-\xi_2\), \(F_{Et}=F_{Et0}+\xi_2\), \(F_H=F_{H0}-\xi_1-\xi_2\). Both rate laws are evaluated **simultaneously from the same local flows**; do not update reaction 2 with a partially updated state from reaction 1. Symbolically check \(E N=0\) using element matrix \(E\), plus an independent numerical integration.

This reduces a six-flow ODE to a two-extent ODE **for this two-reaction isothermal case**, and provides a distinct state-space and stoichiometry cross-check. It is not a symplectic integration method: the reactor kinetics are dissipative and catalyst mass is not time.

## Scratch verification receipt

An independent Python script, implementing both source alternatives from their tabulated parameters and integrating extents rather than individual species, was executed in a separate Linux environment with Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0.

- SymPy verifies the element conservation matrix \(EN=0\) and exact production/consumption algebra.
- SciPy **Radau, BDF, LSODA, DOP853** give a maximum inter-method spread of **1.01×10⁻⁷ percentage point** over six source-set/CO cases.
- With the full printed Table 8: C2H2 conversions **0.840893%, 0.009865%, 0.001767%** (150/1400/5000 ppm).
- With the complete *author-shared but visually unverified* Table 8 alternative: C2H2 conversions **99.785357%, 99.998239%, 100.000000%** and **net C2H4 conversions −0.312667%, 0.093528%, 0.726408%**.
- These match the six-species audit report to its displayed precision. The source-independent test reproduces the numerical predictions, **not** Schbib's experimental Table 6 ethylene conversions.
- The scratch environment did not contain the Git repository, so comparison against the derived JSON was deferred there. The repository-local companion script below subsequently completed that check.

## Repository-local cross-check receipt

Executed after fast-forwarding `feat/schbib-co-benchmark` to `e27cb766d644de685d02f2fc8f11d2300aff909c`:

```bash
python notebooks/benchmarks/schbib_1996_extent_crosscheck.py
```

- **Result:** PASS; SymPy verified `E·N = 0`. Radau, BDF, LSODA, and DOP853 produced a maximum spread of **1.013×10⁻⁷ percentage points**. The largest difference from the recorded six-flow audit JSON was **4.934×10⁻⁶ percentage points**. The script thresholds are 1×10⁻⁶ pp and 1×10⁻⁴ pp, respectively.
- **Wall time:** 1.27 s.
- **Runtime:** Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. No dependency changes.
- **Script SHA256:** `4fbc273e706d7e42583d15751b31c1ed31071df8bfbbc8b9a9d1ef1d0dbc03d0`.

The repository run checked C₂H₂ conversion, net C₂H₄ conversion, and reaction-2 extent for each CO case and each of the two parameter sets against the derived JSON. Its printed values were:

| Parameter set | CO (ppm) | C₂H₂ conversion | Net C₂H₄ conversion |
|---|---:|---:|---:|
| Original printed Table 8 | 150 | 0.840893% | −0.008755% |
| Original printed Table 8 | 1400 | 0.009865% | −0.000105% |
| Original printed Table 8 | 5000 | 0.001767% | −0.000019% |
| Author-shared text transcription | 150 | 99.785357% | −0.312667% |
| Author-shared text transcription | 1400 | 99.998239% | 0.093528% |
| Author-shared text transcription | 5000 | 100.000000% | 0.726408% |

This verifies two numerical state-space implementations against each other within the declared tolerances. It does not validate the source correction or the experimental ethylene conversions; the all-species Table 6 gate remains **BLOCKED**.

## What this demonstrates / does NOT demonstrate

**Supported:** the stoichiometric coupling, sign convention and numerical integration of the currently implemented isothermal rate-law system are mutually consistent under two different state representations and four solvers.

**Usable fixed-temperature reference:** the visually checked original printed Table 8 law and Eqs. 24–25 can anchor a reproducible Pd/α-Al₂O₃ calculation at a prescribed temperature, with base-10 `log A` and the printed gcat-to-kg mass conversion explicitly stated. The cross-check verifies numerical consistency only; the original source set still fails the Table 6 conversion comparison.

**Not established:** publisher approval or visual/document authentication of the author-shared correction, including whether its kgcat labels are intended to change the original gcat rate basis; whether original Model III uses the same reactor physics, surface temperatures and boundary conditions; whether Table 6's C2H4 experimental observable is defined identically; or whether the Pd/Al2O3 kinetics transfer to PdAg. The all-species Schbib Table 6 benchmark remains **BLOCKED**.

## Source availability and next evidence question

Schbib **does publish kinetic parameter pairs** (Table 8: kA, kE, KH, KCO, KE, KEt, KA), complete and simplified kinetic expressions (Table 8 / Eqs. 24–25), gas feed/operating ranges (Table 3), catalyst characteristics (Table 4) and measured Table 6 conversions. His *Model III* equations for gas/particle film transfer, particle energy balance and a nonisothermal reactor also appear on printed pp. 1500–1501. Those equations refer to heat/mass-transfer coefficients and correlations (Crider–Foss, Dixon–Cresswell, Carberry), with experimental inputs/boundary profiles not all identified in the audit.

**Do not conclude "we have no parameter paper" or immediately replace Schbib.** First conduct a parameter-and-boundary inventory by the exact original Model III symbols, noting what is explicitly specified vs derivable from cited correlations vs genuinely missing (e.g. catalyst pellet *diameter* is not the same as the 1000 Å *pore* diameter). Only consult additional cited papers if needed to compute a specific correlation; no arbitrary parameter insertion or refitting to force Table 6 agreement.

**Owner map handling:** record the technique in the owner-led action queue as **Idea**, not as an approved personal-map concept. No changes to current_map.yaml, owner notebooks, or Agent 5 synthesis.
