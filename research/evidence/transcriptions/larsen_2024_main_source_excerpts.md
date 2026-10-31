# Larsen 2024 — checked main-text model and benchmark excerpts

**Source:** User-provided copy of Victor Larsen, *Semihydrogenation of acetylene to ethylene with a PdAg catalyst* (TU Delft BEP, June 2024), PDF SHA-256 `b5aaa2300ff9b64aca70e58cc5e4d8be30b3c12ee264e69af89e01c86f5120c9`. The PDF binary's creation metadata is 2026-06-26; identity with an official 2024 repository version has not been established. These excerpts were visually checked against rendered PDF pages; the native extraction is used only as a locator.

## Experimental response definitions and RMSE

**PDF p. 22 / printed p. 16, Eqs. 4.1–4.5.** The thesis calculates concentrations from GC peak areas using catalyst/compound-specific calibration factors. Its printed responses are:

\[
X_{C_2H_2}=\frac{C_{C_2H_2,feed}-C_{C_2H_2}}{C_{C_2H_2,feed}}\times100\%,
\]

\[
S_{C_2H_4}=\left(1-\frac{C_{C_2H_6}+2C_{4+}}{C_{C_2H_2,feed}-C_{C_2H_2}}\right)\times100\%.
\]

**PDF p. 23 / printed p. 17, Eqs. 4.14–4.15.** For each experiment `i`, the printed combined score is

\[
RMSE_i=\sqrt{\frac{(conv_{sim}-conv_{exp})^2+(selec_{sim}-selec_{exp})^2}{2}},\qquad
RMSE_{overall}=\frac{1}{N}\sum_{i=1}^{N} RMSE_i.
\]

This is a paired per-experiment root-mean-square followed by an arithmetic mean across experiments. The printed definition was compared directly with the Appendix F implementation on PDF p. 84.

## Final extended LHHW model

**PDF p. 43 / printed p. 37, Section 6.2.3, Eqs. 6.9–6.11.** The equation typography was checked from the page render.

\[
r_{1,raw}=\frac{k_1K_{C_2H_2}p_{C_2H_2}K_{H_2}p_{H_2}}
{(1+K_{C_2H_2}p_{C_2H_2}+K_{C_2H_4}p_{C_2H_4}+K_{H_2}p_{H_2})^2},
\]

\[
r_1=\frac{r_{1,raw}}{1+r_{1,raw}/r_{1,max}},
\]

\[
r_2=\frac{k_2K_{C_2H_4}p_{C_2H_4}K_{H_2}p_{H_2}}
{(1+K_{C_2H_2}p_{C_2H_2}+K_{C_2H_4}p_{C_2H_4})(1+K_{inh}p_{C_2H_2})^{n_{inh}}}.
\]

**Transcriber note:** Eq. 6.11 visibly prints the first adsorption factor without a superscript. Appendix F's *standard* LHHW code on PDF p. 81 instead prints/implements a squared adsorption factor and a first-power inhibition factor. The historical benchmark notebook also uses the squared adsorption factor while including the later inhibition exponent. Source formula and code are therefore not identical; this transcript does not infer which exact implementation generated the final Figure 6.6 vectors.

## Figure 6.6 parameters and reported scores

**PDF p. 44 / printed p. 38, Figure 6.6.** The eight displayed values per catalyst are transcribed below in the CSV order; units are not printed next to these coefficients in the figure.

| Catalyst | k₁ | k₂ | r₁,max | K_C₂H₂ | K_H₂ | K_C₂H₄ | K_inh | n_inh | Overall RMSE | Conversion RMSE | Selectivity RMSE | plotted N |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Pd₀Ag | 6.470e+12 | 9.020e+11 | 0.007809 | 2.407e-03 | 1.820e-19 | 1.800e-05 | 0.000e+00 | -1966.78 | 5.0962 | 7.37 | 3.45 | 41 |
| Pd₂Ag | 6.82925 | 0.79396 | 0.014413 | 1.891e-03 | 1.170e-06 | 9.930e-06 | 1.890e-07 | 10.5927 | 5.4320 | 4.50 | 9.63 | 42 |
| Pd₃Ag | 670.788 | 578.54 | 0.0383402 | 4.819e-05 | 2.378e-07 | 8.709e-08 | 1.176e-04 | 4.89665 | 7.1353 | 4.06 | 15.62 | 41 |

The Figure 6.6 caption calls this the addition of `r₁,cap` and a fitted `n_inh` inhibition term. The Pd₀Ag fit reports `K_inh=0` and a large negative `n_inh`; in that parameter vector, the inhibition factor equals one and `n_inh` cannot be identified from predictions.

## Temperature and operating conditions

- **PDF p. 7 / printed p. 1, abstract:** says tests were conducted at 100 °C and 1000 mbar.
- **PDF p. 21 / printed p. 15, Section 4.2:** says after pretreatment the reactor is cooled to 80 °C and that the reactor is maintained at 80 °C when experiments run.
- **PDF p. 29 / printed p. 23, Table 6.1:** lists the three catalyst reaction conditions at 100 °C and 1000 mbar.
- **Appendix F, PDF p. 81 / printed p. 75:** code sets `T = 373` K (annotated “100 Celsius”), `P_total = 100000` Pa, and converts listed mL/min using the ideal-gas relation on PDF p. 82 / printed p. 76.

The method prose, abstract/results table, and code do not establish one unambiguous experimental-temperature/flow-reference story. The MFC standard/reference state for the tabulated mL/min is not named. Figure 6.6 parameters have no printed unit definitions in the figure; the Appendix F standard code comment calls a `/1e3` pressure scaling “Pa to bar,” although division by 1000 gives kPa from Pa. These are preserved as unresolved source details in the audit report.
