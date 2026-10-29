# BEP Catalysis: Project Context & Technical Blueprint

Dit document beschrijft de fysisch-chemische en wiskundige kern van het onderzoek voor snel inhoudelijk begrip.

---

## 🎯 1. Onderzoeksvraag & Doelstelling
Het project onderzoekt de **dynamische modellering, kinetiek en periodieke excitatie** van selectieve acetyleen semi-hydrogenering:
$$\text{C}_2\text{H}_2 + \text{H}_2 \rightarrow \text{C}_2\text{H}_4 \quad (\text{gewenst: ethyleen})$$
$$\text{C}_2\text{H}_4 + \text{H}_2 \rightarrow \text{C}_2\text{H}_6 \quad (\text{ongewenst: overhydrogenering naar ethaan})$$

Industriële ethyleenstromen bevatten sporen acetyleen ($0.5-2\%$) die polymerisatiekatalysatoren vergiftigen. Het doel is maximale selectiviteit naar ethyleen te bereiken door dynamische pulsoperatie in een gepakte-bedreactor (Packed Bed Reactor, PBR).

---

## 🔬 2. Fysisch & Chemisch Model (TN Domein)

### Continuum Reactor Balansen
- **Massa-overdracht:** 1D spatiotemporele diffusie-convectie-reactie vergelijking:
  $$\varepsilon_b \frac{\partial C_i}{\partial t} + u_z \frac{\partial C_i}{\partial z} = D_{az} \frac{\partial^2 C_i}{\partial z^2} + (1 - \varepsilon_b) \rho_s r_i(C, T)$$
- **Fysische Dimensieloze Schaling:**
  - Péclet getal ($Pe_a = u_z L / D_{az}$): Kwantificeert de verhouding tussen convectief transport en axiale dispersie.
  - Damköhler getal ($Da$): Bepaalt de verhouding tussen reactiesnelheid en diffusiesnelheid.
  - Intra-pellet effectiviteitsfactor (Thiele modulus $\Phi$).
- **Energiebalans & Exotherme Dynamica:**
  $$\rho_g C_{p,g} \varepsilon_b \frac{\partial T}{\partial t} + \rho_g C_{p,g} u_z \frac{\partial T}{\partial z} = \lambda_{az} \frac{\partial^2 T}{\partial z^2} + (1 - \varepsilon_b) \rho_s \sum (-\Delta H_{r,j}) r_j - \frac{4 U}{d_{in}} (T - T_w)$$

### Langmuir-Hinshelwood-Hougen-Watson (LHHW) Kinetiek
- Competitieve chemisorptie op het katalysatoroppervlak (Pd-Ag/$\text{Al}_2\text{O}_3$):
  $$r_1 = \frac{k_1 K_{\text{C2H2}} C_{\text{C2H2}} K_{\text{H2}} C_{\text{H2}}}{(1 + K_{\text{C2H2}} C_{\text{C2H2}} + K_{\text{C2H4}} C_{\text{C2H4}})^2}$$

---

## 📐 3. Wiskundig & Numeriek Framework (TW Domein)

### 1. Ruimtelijke Discretisatie (Method of Lines)
- Omzetten van de niet-lineaire PDE's naar een stijf stelsel gekoppelde ODE's.
- **Upwind discretisatieschema** voor de convectieterm om oscillaties en numerieke dispersie bij scherpe concentratiefronten te beheersen:
  $$\left. \frac{\partial C}{\partial z} \right|_j \approx \frac{C_j - C_{j-1}}{\Delta z}$$

### 2. Tijdsintegratie voor Stijve Stelsels
- Door het grote verschil in tijdschalen tussen snelle oppervlakte-adsorptie en langzamere axiale stroming ontstaat een stijf ODE-stelsel.
- Oplossing via impliciete Runge-Kutta methoden (Radau IIA) of Backward Differentiation Formulas (BDF / `scipy.integrate.solve_ivp`).

### 3. Multi-Stage Inversie & Calibratie
- **Probleem:** Gelijktijdige fit van $K_i$ en $k_i$ leidt tot compensatie en onzekerheid.
- **Oplossing:** Getrapte calibratie: eerst evenwichtsconstanten $K_i$ isoleren via dynamische MES-PSD (Modulation Excitation Spectroscopy) adsorptiedata, vervolgens reactiesnelheidsconstanten $k_i$ fitten op macroscopische reactoropbrengst.

### 4. Traject- & Excitatie-optimalisatie
- Optimaliseren van periodieke concentratie- en flowpulsen via B-spline parameterisatie en optimalisatie-algoritmen (variabele gradiënt descent / Genetic Algorithms) om ethyleenselectiviteit te maximaliseren.

---

## 📚 4. Kernreferenties & Handboeken
- **Larsen (2024):** *Semihydrogenation of Acetylene to Ethylene: Mathematical Modeling and Parameter Estimation* (Benchmark BEP thesis).
- **Froment, Bischoff & De Wilde:** *Chemical Reactor Analysis and Design* (Klassiek handboek transport-continuümvergelijkingen).
- **Fogler:** *Elements of Chemical Reaction Engineering* (Kinetiek, PBR balansen en effectiviteitsfactoren).
- **Hundsdorfer & Verwer:** *Numerical Solution of Time-Dependent Advection-Diffusion-Reaction Equations* (Method of Lines & Upwind theorie).
