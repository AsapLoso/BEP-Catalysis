# Schbib (1996) — visually checked operating and kinetic data

**Status:** `checked_against_image` for the transcribed text and numeric data below. This transcription covers the listed tables and equations only; it is not a model interpretation or evidence that the published model is independently reproducible.

## Source and method

- N. S. Schbib, M. A. García, C. E. Gígola, and A. F. Errazu, “Kinetics of Front-End Acetylene Hydrogenation in Ethylene Production,” *Ind. Eng. Chem. Res.* 35 (1996), 1496–1505, DOI [10.1021/ie950600k](https://doi.org/10.1021/ie950600k).
- Original file: [`research/literature/schbib_1996_front_end_acetylene_hydrogenation.pdf`](../../literature/schbib_1996_front_end_acetylene_hydrogenation.pdf); article HTML and extracted text are in `research/literature/`.
- PDF pages 4, 6, 7, and 8 were rendered locally and checked visually. Printed pages are 1499, 1501, 1502, and 1503 respectively. Page 4 was rendered at 180 dpi; pages 6–8 at 220 dpi.
- The extracted article text was used to locate passages. Ambiguous subscripts, superscripts, signs, and units were checked on the rendered PDF page.
- Source SHA256: `4b4c2728f1ac1d73acdf74eef1f247203f3aa5b8ab38cace45d1f6e513dbc60a`.
- Scope: Tables 3, 4, 6, and the original printed Table 8; Eqs. 22, 24, and 25; selected experimental/model statements on printed pp.1499–1503. The later author-shared correction is transcribed separately in [`schbib_1996_author_table8_correction.md`](schbib_1996_author_table8_correction.md) and is **not** part of original Table 8.

## Table 3 — feed and laboratory operating range

**PDF page 4; printed p.1499.** The table heading reads “Feed Mixture and Operating Conditions for the Laboratory Reactor”; composition is mol% (±0.02).

| Component / condition | Printed value |
|---|---:|
| CH₄ | 6.53 mol% |
| C₂H₂ | 0.52 mol% |
| C₂H₄ | 43.99 mol% |
| C₂H₆ | 26.72 mol% |
| H₂ | 22.1 mol% |
| CO | 150–5000 ppm |
| Flow rate | 100 cm³(STP)/min |
| Catalyst mass | 1–3 g |
| Pressure | 1–35 atm |
| Temperature | 288–393 K |

## Table 4 — catalyst characterization

**PDF page 4; printed p.1499.**

| Property | Printed value |
|---|---:|
| Support | α-Al₂O₃ |
| Palladium content | 0.04 wt% |
| BET surface area | 21 m²/g |
| Metal dispersion (H/Pd) | 0.15 |
| Apparent density | 1.61 g/cm³ |
| Real density | 3.61 g/cm³ |
| Average pore diameter | 1000 Å |
| Pore volume | 0.338 cm³/g |
| Porosity | 54.5% |

## Table 6 — CO effect at constant pressure

**PDF page 4; printed p.1499.** The caption specifies pressure = 16 atm and (SV=100\ \mathrm{cm^3(STP)\ g_{cat}^{-1}\ min^{-1}}). Columns are “conversion (%)”.

| CO content (ppm) | Temperature (K) | C₂H₂ (%) | C₂H₄ (%) |
|---:|---:|---:|---:|
| 150 | 341 | 98.31 | 10.45 |
| 1400 | 359 | 98.99 | 6.70 |
| 5000 | 393 | 98.62 | 6.08 |

## Eqs. 22, 24, and 25 — printed kinetic relations

**Eq. 22: PDF page 6; printed p.1501.** The page gives the dimensionless relation

\[
k_i^* = k_{si}/k_i \quad (\text{or }K_i^*=K_{si}/K_i)
=\exp\{-E_i^*(1/T^*-1)\}, \qquad E_i^*=E_i/(RT).
\]

This is reproduced as printed, retaining the paper’s notation. The text immediately following Eqs. 24–25 states that the positive tabulated adsorption energies for CO and H₂ imply those adsorption constants increase with temperature.

**Eqs. 24–25: PDF page 6; printed p.1501.** The article describes these as the simplification after neglecting (K_E), (K_{Et}), and (K_A):

\[
-r_A = \frac{k_A C_A C_H}{[1+(K_H C_H)^{1/2}+K_{CO}C_{CO}]^3},
\qquad
-r_E = \frac{k_E C_E C_H}{[1+(K_H C_H)^{1/2}+K_{CO}C_{CO}]^3}.
\]

## Table 8 — original printed parameters and complete rate law

**PDF page 7; printed p.1502.** The column labels read “kinetic parameters”, “log (A_i)”, and “(E) (kcal/gmol)”. The table prints:

| Parameter | Printed unit | log (A_i) | (E) (kcal/gmol) |
|---|---|---:|---:|
| (k_A) | m⁶/(s gcat kmol) | 31.1 | 45.51 |
| (k_E) | m⁶/(s gcat kmol) | 26.6 | 42.94 |
| (K_H) | m³/kmol | 20.2 | 21.22 |
| (K_{CO}) | m³/kmol | 13.6 | 9.95 |
| (K_E) | m³/kmol | 0.26 | 0.005 |
| (K_{Et}) | m³/kmol | −0.012 | 0.001 |
| (K_A) | m³/kmol | −16 | 0.001 |

The same page prints the following full rate expressions and coefficient definitions:

\[
-r_A = \frac{k_A C_A C_H}{[1+(K_H C_H)^{1/2}+K_A C_A+K_E C_E+K_{Et}C_{Et}+K_{CO}C_{CO}]^3},
\]

\[
-r_E = \frac{k_E C_E C_H}{[1+(K_H C_H)^{1/2}+K_A C_A+K_E C_E+K_{Et}C_{Et}+K_{CO}C_{CO}]^3},
\]

\[
k_A=k_3 S_t^3 K_A K_H, \qquad k_E=k_5 S_t^3 K_A K_H.
\]

The visible table heading says `log A_i`, without a printed base. The value-to-pre-exponential conversion and absolute Arrhenius form are therefore interpretive steps, not literal subscripted source text.

## Laboratory and figure-model statements

**PDF page 4; printed p.1499.** The laboratory apparatus is described as a stainless-steel tube of 10 mm internal diameter immersed in a diethylene-glycol bath. A thermocouple in contact with catalyst particles was located at an axial position to monitor reaction temperature, and the wall temperature was also measured.

**PDF page 5; printed p.1500.** The paper defines model II as a nonisothermal, isobaric, pseudohomogeneous plug-flow model. It describes model III as allowing temperature and concentration differences between the gas phase and catalyst-particle surface and introduces external transfer relations.

**PDF page 8; printed p.1503.** Figure 3 caption: model III; Table 3 feed; (T_0=325\) K; (P=16.3\) atm; (C_{CO}=1400\) ppm. Accompanying prose reports about 70.7% C₂H₂ conversion and an approximately 1.5 K hot spot. Figure 4 has the same feed, (T_0=345\) K, (P=16.3\) atm, and (C_{CO}=1400\) ppm; accompanying prose says C₂H₂ conversion was close to 98% and the temperature overshoot exceeded 3 K. Captions do not report catalyst mass or space velocity.

## Transcriber notes (not original source text)

- Table 3 non-CO mole percentages sum to 99.86%; this is a visible source-table total, likely due to rounding. No normalization is made in this transcription.
- Table 4's “porosity” is reported as a catalyst characterization property. The article does not label it as an interparticle packed-bed void fraction in the table.
- Printed Table 8's mass basis for (k_A,k_E) is visibly `gcat`; the separate author-shared text record gives a kgcat basis. Neither label is silently substituted for the other.
- Eq. 22, Table 8's log base, precise definition of tabulated (A_i), Table 6's ethylene-conversion convention, and the figure 3/4 catalyst mass remain interpretation questions rather than transcribed facts.
