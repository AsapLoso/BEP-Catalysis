# Literature Grounding & Primary Benchmarks

This directory archives historical literature papers, extracted text, and parameter registers for reactor modeling and kinetics in the BEP-Catalysis project. **Archive presence does not establish source verification or current model relevance.**

**Current independent source audits:** Agent 1 = Schbib (1996); Agent 4 = Larsen (2024). Agent 5 remains paused. Gobbo (2004) is kept as a historical comparison only, not an assigned benchmark or a source for silent parameter transfer.

---

## 1. Historical archived comparison (NOT an active benchmark): Gobbo et al. (2004)

* **Full Title:** *Modeling, simulation, and optimization of a front-end system for acetylene hydrogenation reactors*
* **Authors:** R. Gobbo, R. P. Soares, M. A. Lansarin, A. R. Secchi, J. M. P. Ferreira (COPESUL & Universidade Federal do Rio Grande do Sul - UFRGS)
* **Journal:** *Brazilian Journal of Chemical Engineering*, Vol. 21, No. 04, pp. 545–556, October–December 2004.
* **DOI:** [`10.1590/s0104-66322004000400004`](https://doi.org/10.1590/s0104-66322004000400004)
* **Files:**
  - PDF: [`gobbo_2004_front_end_acetylene_hydrogenation.pdf`](gobbo_2004_front_end_acetylene_hydrogenation.pdf) (124 KB)
  - Full Extracted Text: [`gobbo_2004_extracted_text.txt`](gobbo_2004_extracted_text.txt) (44.6 KB)

### Key Equations & Locators in Gobbo (2004)
* **Mass Balance (Page 4, Eq. 1):**
  $$\varepsilon \frac{\partial C_i}{\partial t} = -\frac{\partial (u_z C_i)}{\partial z} + (1 - \varepsilon)\rho_s \sum_j \nu_{i,j} r_j$$
* **Energy Balance (Page 4, Eq. 2):**
  $$\left[\varepsilon \rho c_p + (1 - \varepsilon)\rho_s c_{p,s}\right] \frac{\partial T}{\partial t} = - u_z \rho c_p \frac{\partial T}{\partial z} + (1 - \varepsilon)\rho_s \sum_j (-\Delta H_{r,j}) r_j$$
* **Langmuir-Hinshelwood Kinetics with CO Moderation (Page 4, Eq. 3 & Eq. 4):**
  $$r_j = \frac{k_j C_i C_{\text{H}_2}}{\left(1 + K_{\text{H}}^{1/2} C_{\text{H}_2}^{1/2} + K_{\text{CO}} C_{\text{CO}}\right)^3}$$
  $$k_j = k_{0,j} \exp\left(-\frac{E_j}{R T}\right), \quad K_m = K_{0,m} \exp\left(-\frac{E_{a,m}}{R T}\right)$$
* **Table 1: Kinetic and Adsorption Constants (Page 5, Line 492):**
  - **Acetylene hydrogenation ($r_1$):** $\log_{10} k_{0,1} = 27.4\ \text{m}^6/(\text{kmol}\cdot\text{kg}_{\text{cat}}\cdot\text{s})$, $E_1 = 190.50\ \text{kJ/mol}$
  - **Ethylene hydrogenation ($r_2$):** $\log_{10} k_{0,2} = 23.3\ \text{m}^6/(\text{kmol}\cdot\text{kg}_{\text{cat}}\cdot\text{s})$, $E_2 = 179.78\ \text{kJ/mol}$
  - **$\text{H}_2$ Adsorption ($K_{\text{H}}$):** $\log_{10} K_{0,\text{H}} = 17.2\ \text{m}^3/\text{kmol}$, $E_{\text{H}} = 88.84\ \text{kJ/mol}$
  - **$\text{CO}$ Adsorption ($K_{\text{CO}}$):** $\log_{10} K_{0,\text{CO}} = 10.2\ \text{m}^3/\text{kmol}$, $E_{\text{CO}} = 41.66\ \text{kJ/mol}$
* **Numerical Method (Page 6):**
  - Discretized along axial coordinate $z$ via the Method of Lines (MOL) with 50 spatial nodes using backward finite differences.
  - Solved with variable-order, variable-step stiff ODE/DAE integrator (DASOLV in gPROMS, equivalent to `scipy.integrate.solve_ivp(method='BDF')` or `Radau`).

---

## 2. Secondary Benchmark & Periodic Operation: Urmès et al. (2022)

* **Full Title:** *Microkinetic Modeling of Acetylene Hydrogenation Under Periodic Reactor Operation*
* **Authors:** Caroline Urmès, Cécile Daniel, Jean-Marc Schweitzer, Amandine Cabiac, Carine Julcour-Lebigue, Yves Schuurman
* **Journal:** *ChemCatChem*, 14(9), e202101826 (2022).
* **DOI:** [`10.1002/cctc.202101826`](https://doi.org/10.1002/cctc.202101826)
* **Relevance:** Exemplifies periodic operation of acetylene hydrogenation over $\text{Pd}/\alpha\text{-Al}_2\text{O}_3$ and transient response under flow and concentration oscillations.
