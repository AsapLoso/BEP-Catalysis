# Literature Grounding & Primary Benchmarks

This directory archives verified literature papers, extracted text, and parameter registers for reactor modeling and kinetics in the BEP-Catalysis project.

---

## 1. Primary Kinetic Benchmark: Schbib et al. (1996)

* **Full Title:** *Kinetics of Front-End Acetylene Hydrogenation in Ethylene Production*
* **Authors:** Noemí S. Schbib, Miguel A. García, Carlos E. Gígola (PLAPIQUI - UNS - CONICET)
* **Journal:** *Industrial & Engineering Chemistry Research*, Vol. 35, No. 5, pp. 1496–1503 (1996).
* **DOI:** [`10.1021/ie950600k`](https://doi.org/10.1021/ie950600k)
* **Files:**
  - Full Lossless Article HTML: [`schbib_1996_full_article.html`](schbib_1996_full_article.html) (2.75 MB, complete tables and text)
  - PDF: [`schbib_1996_front_end_acetylene_hydrogenation.pdf`](schbib_1996_front_end_acetylene_hydrogenation.pdf) (1.2 MB)
  - Full Extracted Text: [`schbib_1996_extracted_text.txt`](schbib_1996_extracted_text.txt) (39.5 KB)

### Key Equations & Parameters in Schbib (1996)
* **Rate Law with Competitive CO Adsorption (Table 8):**
  $$(-r_j) = \frac{k_j C_j C_H \rho_s (1 - \varepsilon_b)}{\left[1 + K_H C_H^{1/2} + K_{CO} C_{CO}\right]^3}$$
* **Kinetic and Adsorption Constants (Table 8):**
  - **Acetylene hydrogenation ($k_A$):** $\log A = 31.1\ \text{m}^6/(\text{s}\cdot\text{g}_{\text{cat}}\cdot\text{kmol})$, $E = 45.51\ \text{kcal/gmol}$ ($190.42\ \text{kJ/mol}$)
  - **Ethylene hydrogenation ($k_E$):** $\log A = 26.6\ \text{m}^6/(\text{s}\cdot\text{g}_{\text{cat}}\cdot\text{kmol})$, $E = 42.94\ \text{kcal/gmol}$ ($179.66\ \text{kJ/mol}$)
  - **$\text{H}_2$ Adsorption ($K_H$):** $\log A = 20.2\ \text{m}^3/\text{kmol}$, $E = 21.22\ \text{kcal/gmol}$ ($88.78\ \text{kJ/mol}$)
  - **$\text{CO}$ Adsorption ($K_{CO}$):** $\log A = 13.6\ \text{m}^3/\text{kmol}$, $E = 9.95\ \text{kcal/gmol}$ ($41.63\ \text{kJ/mol}$)
* **Experimental Benchmarks:**
  - Table 3: Feed mixture (0.52% C2H2, 43.99% C2H4, 22.1% H2, 150-5000 ppm CO), 100 STP cm3/min, 1-3 g catalyst.
  - Table 6: Experimental conversion benchmarks with CO inhibition.
  - Figures 1–4: Conversion, rates, and axial hotspot profiles.

---

## 2. Secondary Benchmark & Periodic Operation: Urmès et al. (2022)

* **Full Title:** *Microkinetic Modeling of Acetylene Hydrogenation Under Periodic Reactor Operation*
* **Authors:** Caroline Urmès, Cécile Daniel, Jean-Marc Schweitzer, Amandine Cabiac, Carine Julcour-Lebigue, Yves Schuurman
* **Journal:** *ChemCatChem*, 14(9), e202101826 (2022).
* **DOI:** [`10.1002/cctc.202101826`](https://doi.org/10.1002/cctc.202101826)
* **Relevance:** Exemplifies periodic operation of acetylene hydrogenation over $\text{Pd}/\alpha\text{-Al}_2\text{O}_3$ and transient response under flow and concentration oscillations.
