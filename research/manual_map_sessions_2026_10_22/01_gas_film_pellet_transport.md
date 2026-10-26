# M01 — From inlet waveform to gas inventory, film transfer and pellet reaction

**State:** Research-backed **AI draft** for owner discussion. **Not** a patch to the canonical or integrated map, not an approval or assertion of personal understanding.  
**BEP scope:** selectively hydrogenating acetylene to ethylene under time-dependent inlet composition in a packed bed.  
**Exact existing node IDs:** `sc_manipulated_input`, `sc_bed_input_realization`, `ma_stoichiometry`, `ma_gas_pde`, `ph_pellet_transport`, `external_film_transfer`.  
**Central question:** At each spatial scale, what quantity is conserved, what crosses the boundary, and what are the units?

## 1. Physical inventory — distinguish the boxes

```text
MFC commands         actuators/mixer/line         actual inlet gas
F_k,command(t)   -->  unknown filtering  -->    F_k,bed(t), C_i,in(t)
                                                     |
                                                     v
                      axial void-gas inventory  ε_b C_i(z,t)
                                                     |
                   interfacial film flux j_i  [mol m^-2 s^-1]
                                                     |
                                                     v
               porous pellet: ε_p c_i(r,z,t) and adsorbed q_i
                                                     |
                    catalyst sites / rate laws / reaction network
                                                     |
                          gas species production or consumption
```

**[SOURCE: proposal]** In `0_Project_Management/main.tex`, §1.3 and §3.1 the intended baseline is one-dimensional gas advection/dispersion plus a heterogeneous kinetic source, with Danckwerts-type boundaries and (initially) isothermal operation. The current proposal equation does not contain an intrapellet radial field.

**[DERIVATION / INTERPRETATION]** The boxes above are a bookkeeping decomposition. One need not resolve all of them in a baseline model. What matters is **not double-counting the same reaction/transport event** and keeping the mass basis explicit.

## 2. Inventory at the 1-D bed scale

Choose:
- `C_i(z,t)` = moles of gas species `i` per **void-gas volume**, mol m^-3_void.
- `ε_b` = bed void fraction, dimensionless.
- `u_s` = superficial volumetric velocity (referenced to the full tube cross-section), m s^-1.
- `D_ax,i` = effective axial gas dispersion in the chosen void-flux convention, m² s^-1.
- `ρ_cat,p` = catalyst mass per pellet-envelope volume, kg_cat m^-3_pellet.
- `r_j` = **extent of reaction** per catalyst mass and time, mol_reaction kg_cat^-1 s^-1.
- `ν_ij` = signed gas stoichiometry (positive for products, negative for reactants).

Then, for a volume-averaged locally reacting bed **without a separately resolved pellet-transfer boundary**, an internally consistent conservative model is

```text
∂t(ε_b C_i) + ∂z[ u_s C_i - ε_b D_ax,i ∂z C_i ]
    = (1 - ε_b) ρ_cat,p Σ_j ν_ij r_j
```

**[DERIVATION:]** Integrate the molar species balance over an infinitesimal total bed volume. The left-hand terms describe accumulation and divergence of gas flux; the right-hand term is a rate per catalyst mass multiplied by catalyst mass per **total bed volume**. Define `ρ_cat,b = (1-ε_b)ρ_cat,p` (kg_cat m^-3_bed) and equivalently write `ρ_cat,b Σ_jν_ij r_j`.

Dimensional check:

| Quantity | Unit per total bed volume |
|---|---|
| `∂t(ε_b C_i)` | mol m^-3_bed s^-1 |
| `∂z(u_s C_i)` | mol m^-3_bed s^-1 |
| `∂z(ε_b D_ax,i ∂z C_i)` | mol m^-3_bed s^-1 |
| `(1-ε_b)ρ_cat,p Σνr` | mol m^-3_bed s^-1 |

Only under **constant** `ε_b`, `u_s` and `D_ax` can one safely rearrange to a constant-coefficient advection–dispersion form with interstitial velocity `u_i=u_s/ε_b`. Feed modulation might change the total molar flow and properties, so do not silently assume these constants when modelling a real apparatus.

**[HYPOTHESIS:]** A 1-D pseudo-homogeneous closure may suffice under verified pellet/film/thermal conditions; this is not established by the proposal or an unknown target batch.

## 3. What changes when the pellet is resolved?

At the gas/solid interface, if `C_{i,b}` is gas bulk concentration and `C_{i,s}` concentration on the gas side of the pellet boundary (or corrected for a declared partition law), the **inward molar flux per pellet exterior area** is

```text
j_i,in = k_g,i (C_i,b - C_i,s)
```

where `k_g,i` is m s^-1. Hence `j_i,in` is **mol m^-2_surface s^-1**.

Let `a_b=A_pellet,outer/V_bed` (m²_surface m^-3_bed). For non-overlapping spheres with radius `R_p` and solid-envelope fraction `1-ε_b`, `a_b=3(1-ε_b)/R_p`. With a pellet explicitly resolved, the gas balance can instead use the **gas-to-pellet exchange term**

```text
∂t(ε_b C_i) + ∂z[ u_s C_i - ε_b D_ax,i ∂z C_i ]
    = - a_b j_i,in
```

For gas consumption, `j_i,in>0` is a gas sink. The corresponding gas **volumetric** transfer is `a_b j_i,in` in mol m^-3_bed s^-1; it is **not** an interfacial flux.

**[DERIVATION:]** This distinction exposes the current integration ambiguity: `external_film_transfer` labels `k_g a_v(C_b-C_s)` as "Flux J" even though the presence of area/volume makes it a bed-volume (or whatever volume `a_v` references) transfer **rate**. Repair should introduce separate quantities `j_i` and `R_{i,transfer}`, specify the denominator of `a_v`, and avoid attaching a blanket `verified` label to an inherited historical citation.

An illustrative spherical pellet balance, including pore-gas storage and optional adsorbed inventory, is

```text
∂t[ ε_p c_i + ρ_cat,p q_i ]
    = (1/r²) ∂r [ r² D_eff,i ∂r c_i ]
      + ρ_cat,p Σ_j ν_ij r_j
```

with `∂r c_i(0,t)=0`; in a simple Fickian film boundary convention,

```text
D_eff,i ∂r c_i(R_p,t) = k_g,i [ C_i,b(t) - c_i(R_p,t) ]
```

if outer pore-gas and bulk-gas concentrations use compatible units and no partition jump is imposed. Adsorption storage `q_i` must not be counted twice if the surface ODEs are explicitly represented elsewhere.

**Crucial dynamic insight:** at steady state (with no pellet inventory growth), the inward gas-to-pellet transfer can equal the integrated chemical consumption for a consumed component. During transients, **they need not match instantaneously**: the pellet can temporarily accumulate/release a component. Therefore **do not add both** `-a_b j_i,in` and `(1-ε_b)ρ_cat,p Σνr` as independent gas source terms in the *same resolved-pellet closure*.

## 4. Mears criterion — check units before declaring film resistance small

**[SOURCE: external literature]** D. E. Mears, *Tests for Transport Limitations in Experimental Catalytic Reactors*, *Ind. Eng. Chem. Process Des. Dev.* 10 (1971), 541–547, DOI [10.1021/i260040a020](https://doi.org/10.1021/i260040a020). This paper's bibliographic/first-page ACS preview was accessible, **not full text**. A published 2022 [AIChE Journal analysis](https://aiche.onlinelibrary.wiley.com/doi/10.1002/aic.17796), §3.1.1, explicitly writes the commonly used empirical criterion as

```text
M = |r_A,obs| ρ_cat,b R_p n / [ k_g,A C_A,b ] < 0.15
```

where `r_A,obs` is the observed reactant-consumption rate per catalyst mass, `ρ_cat,b` is catalyst mass per bed volume, `R_p` is particle radius, `n` is the relevant apparent reaction order, `k_g,A` is the film coefficient, and `C_A,b` is the bulk concentration. All must use the same reactant, length/volume conventions and rate basis. It is a **screening criterion** under its assumptions, not proof that the film resistance is negligible for an uncharacterized BEP pellet.

Dimension check: `(mol kg_cat^-1 s^-1) (kg_cat m^-3_bed) (m) / [(m s^-1)(mol m^-3)] = 1`; `n` is dimensionless.

**[OPEN:]** The correct mass-transfer correlation, external area, apparent order and criterion adaptation under rapid periodic forcing remain model/condition-specific. Source and secondary treatment should be checked before transplanting a 0.15 steady criterion to strongly dynamic, multicomponent, or coverage-dependent kinetics. Do not cite Berger 2008 §5.1 as verified direct support solely because the legacy map attached it.

## 5. The link to Systems & Control

**[SOURCE: proposal]** `main.tex` §3.4 plans MFC modulation; it does not demonstrate that the commanded waveform reaches the bed unchanged.

**[DERIVATION:]** For component molar feed flows `F_k(t)`, `F_T(t)=Σ_k F_k(t)`, `y_k(t)=F_k(t)/F_T(t)` for `F_T>0`. If one MFC varies a component while other flows stay fixed, the total flow and residence time can change as well as composition. The input in the gas PDE is the **realized** `C_{i,in}(t)` or equivalent molar-flux boundary, not necessarily the controller command.

This creates an essential distinction in a periodic test:

```text
command waveform -> actual boundary waveform -> reactor transport +
surface/pellet storage -> true outlet -> analyzer/sampling -> recorded output
```

An observed phase lag does not isolate catalyst storage until actuator, mixer, residence-time and measurement lags have been considered.

## 6. Proposed node-delta (NOT APPLIED)

A narrow later amendment to `external_film_transfer` (or a successor node if Work reorganizes the graph) should:

- Rename/define `j_i = k_g,i(C_i,b-C_i,s)` explicitly as **interfacial flux, mol m^-2 s^-1**.
- Define `R_i,transfer=a_b j_i` explicitly as **volumetric transfer rate, mol m^-3_bed s^-1**, and state how `a_b` is measured.
- Give the Mears screening expression with a declared catalyst-bed density, particle radius, rate basis, order, and source access caveat.
- Cross-link to `ma_gas_pde`, `ph_pellet_transport`, `ma_stoichiometry`, `sc_bed_input_realization`; record double-counting warnings and the transient storage difference.
- **Do not** assert source-verified kinetics or personal understanding. Check latest Work edits before integrating.

No original or integrated scientific YAML has been edited in this manual session.

## 7. One question for the owner

Suppose `j_i` is the molar flux of acetylene *into one square metre of pellet exterior*, and we want its contribution to a **one-dimensional PDE written per cubic metre of reactor bed**.

**Which additional geometric factor must we multiply by, and what units should the result have?**

This question is deliberately about understanding the physical inventory rather than memorizing a named equation.

## Sources and limits

- Repo proposal `Academics/BEP/Catalysis/0_Project_Management/main.tex`, §§1.3, 3.1 and 3.4 (the model and plan; not proof of target performance).
- Repo integrated graph `.../integrated_reference_map_2026_10_22/nodes.yaml`, exact IDs above (AI science and historical source lineage, not necessarily verified).
- Mears 1971, DOI 10.1021/i260040a020: publisher bibliography and preview only.
- Okoli et al. 2022, DOI 10.1002/aic.17796, published mass-transfer screening restatement in §3.1.1; different chemical process, does not validate target BEP.
- **No target catalyst measurements, kinetic constants, transport coefficients, or numerical reactor run were used.**
