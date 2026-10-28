# Subgoals & Gate Receipts — Schbib (1996) Steady-State Benchmark

## 01 — Literature & Parameter Extraction
- [ ] Inspect `research/literature/schbib_1996_full_article.html` and extract Table 3 (feed specs), Table 4 (catalyst morphology), and Table 8 (kinetic & adsorption Arrhenius constants).
- [ ] Record extracted constants in notebook preamble with explicit units.

## 02 — Differential PFR Model Formulation
- [ ] Implement molar balance ODEs: $dF_i/dz = A \rho_s (1 - \varepsilon_b) \sum_j \nu_{i,j} r_j$.
- [ ] Implement non-isothermal energy balance: $dT/dz = \frac{A \rho_s (1 - \varepsilon_b) \sum_j (-\Delta H_{r,j}) r_j}{\sum_i F_i C_{p,i}}$.
- [ ] Implement Schbib Langmuir-Hinshelwood rate laws with cubed denominator: $[1 + K_H C_H^{1/2} + K_{CO} C_{CO}]^3$.

## 03 — Figure Reproduction
- [ ] Replicate Figure 1: Conversion of C2H2 and C2H4 vs. Temperature (290–360 K).
- [ ] Replicate Figure 2: Reaction rates r1 and r2 vs. Temperature.
- [ ] Replicate Figures 3 & 4: Axial temperature and conversion profiles along the bed (thermal runaway suppression).

## 04 — Table 6 Benchmark Validation
- [ ] Simulate reactor at 150 ppm, 1400 ppm, and 5000 ppm CO at 341 K, 359 K, 393 K.
- [ ] Output validation table comparing simulated conversions against measured values from Table 6.

## 05 — Gate Receipt
- [ ] Notebook `notebooks/benchmarks/schbib_1996_steady_state.ipynb` executes top-to-bottom with 0 errors in < 60 seconds.
- [ ] Commit notebook and figures to branch.
