# Schbib 1996 — author-shared Table 8 correction (readable source-value record)

**Status:** **readable structured transcription of numeric table**, from a publicly accessible **author-shared document copy**, **NOT independently confirmed as a separately published ACS erratum**. Transcription was read from the document's machine-readable passage and must be checked against the visual source by Agent 1. No claim that the archived on-branch PDF includes the correction.

- Paper: N. S. Schbib et al., *Kinetics of Front-End Acetylene Hydrogenation in Ethylene Production*, *Industrial & Engineering Chemistry Research* **35** (1996) 1496–1505; DOI [10.1021/ie950600k](https://doi.org/10.1021/ie950600k).
- Author-shared copy containing correction note **after the article**: https://www.researchgate.net/publication/231391687_Kinetics_of_Front-End_Acetylene_Hydrogenation_in_Ethylene_Production
- On-branch paper archive: `research/literature/schbib_1996_front_end_acetylene_hydrogenation.pdf`; extracted text `research/literature/schbib_1996_extracted_text.txt`. That extracted text currently **does not include** this appended correction.

## Corrective note's parameter table (transcribed data; to be visually rechecked)

The table labels its second column `LOG A_i` and third column `E (kcal/gmol)`. Read the first numeric column as **logarithmic pre-exponential values**, not adsorption constants themselves. The author's note gives rates in `kmol/(kg_cat s)` with source species concentrations expressed in `kmol/m³`; agent must reconcile equation and pre-exponential dimensional conventions with the original paper.

| Parameter | LOG A_i | E (kcal/gmol) | Initial source-unit label / uncertainty |
|---|---:|---:|---|
| k_A | 31.1 | 45.51 | rate coefficient, printed m^6/(s kgcat kmol) |
| k_E | 26.6 | 42.94 | rate coefficient, same printed unit family |
| K_H | **17.2** | 21.22 | adsorption term, printed m^3/kmol |
| K_CO | **10.16** | 9.95 | adsorption term, printed m^3/kmol |
| K_E | -2.74 | 0.005 | adsorption term |
| K_Et | -3.012 | 0.001 | adsorption term |
| K_A | -19.0 | 0.001 | adsorption term |

**Dispute to investigate:** Agent 1's earlier `GOAL.md` and archived notebook use **20.2** for the hydrogen and **13.6** for the CO `LOG A_i` values from the printed Table 8. The author's later table lists **17.2** and **10.16** respectively; any external parameter fit belongs to a separate model and cannot replace these values without independent evidence.

**Why it matters:** `10^(13.6-10.16)` is a factor of roughly 2754 for a fixed Arrhenius energy and temperature. This does not establish that the large Table 6 mismatch is caused solely by this difference. Agent 1 must independently inspect source pages, check dimensions and reactor/energy assumptions, reproduce numerical results, and record when the source remains ambiguous.

## Status and provenance

- Source table present in publicly accessible author-shared copy: **yes** (not a source-file edit).
- Original PDF correction appended in this repository: **not established**.
- Journal-issued erratum: **not established**.
- Page/image-by-image comparison of this transcription: **pending Agent 1 audit**.
- Numerical benchmark after corrected constants: **not executed in this transcription**.
- This file is *source data transcription and provenance*, **not a merged validated kinetic model**, interpretation to be kept in `../analysis/`.
