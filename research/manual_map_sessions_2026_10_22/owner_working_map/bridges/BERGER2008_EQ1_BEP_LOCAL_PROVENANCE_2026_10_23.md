# Berger (2008) transient equation — local provenance and open verification

**Status:** AI research/history crosswalk only, NOT a new personal node, NOT human-verified paper transcription, NOT a settled BEP model closure. Requested by owner 2026-10-23, no new external literature search.

## Confirmed files already in GitHub

- `Academics/BEP/Catalysis/Articles/analyses/dynamic_kinetics_berger2008.md`, lines **22–44**: local research dossier labels Berger et al. (2008), *Dynamic methods for catalytic kinetics*, *Applied Catalysis A: General* 342, pp. 3–28, DOI `10.1016/j.apcata.2008.03.020`. It writes Eq. (1) as `∂t C_i = -(u_s/ε) ∂z C_i + D_ax ∂²_z C_i + (ρ_s/ε)(1-ε_b) C_t R_i`, Eq. (2) for surface coverage and an inlet `C_i(0,t)=C_i^0(t)` called Eq. (4b).
- `Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md`, lines **52–70**: explicitly contrasts the dossier's Berger Eq. (1) with an earlier chat equation, flags an erroneous factor-of-`ε_b²` in the advection coefficient and **unresolved notation ambiguity** between Berger's `ε` and project `ε_b` / superficial versus interstitial velocities; cautions to check the paper PDF before coding.
- Pinned integrated AI reference `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/nodes.yaml` includes `ma_gas_pde`, `ph_axial_balance`, `ph_danckwerts`, `ph_axial_dispersion`, and `ph_energy_balance`. The `ma_gas_pde` node carries a **legacy** attachment `legacy_ref_159cf51de0` titled `Transient Model Framework Audit §1` with locator 'Berger Eq. 1 recovery and axial balance formulation'. Per `sources.yaml` this is **historical provenance only**, not an independently verified scientific claim.
- The original BEP proposal `Academics/BEP/Catalysis/0_Project_Management/main.tex` §3.1 lines 180–185 displays a *related*, not manifestly identical, simplified 1D axial dispersion equation and mentions Danckwerts conditions, with a separate hypothesized high-Pe plug-flow reduction.

## Exact issue before using it as a model

The dossier attributes a **Dirichlet inlet condition** to Eq. (4b) alongside a PDE retaining `D_ax ∂²_zC_i`. For a finite-axial-dispersion bed model, **inlet flux continuity and the outlet boundary treatment must be checked against the original model geometry and PDE formulation**. A Dirichlet entry from one simplifying limit should not automatically be pasted into another model's Robin/Danckwerts boundary specification. This is neither proof the paper is wrong nor reason to override the author's conventions: inspect the actual source and exactly what its `u_s`, `ε`, `C_t`, `ρ_s`, `R_i`, inlet/outlet and `D_ax` denote.

Likewise the dossier's `Eq. (1)` is a GAS species and surface-reaction equation, **not** the reactor thermal energy balance. A thermal equation/heat source is a separate cross-link.

## Placement and action

Link to **B-MODEL-BC-01** and the live Idea nodes
`own_ma_assumption_radial_reduction` and `own_ma_assumption_axial_dispersion`, plus the mathematical Reactor Model parent. The physical axial-versus-radial distinction has already reached Human worked out in `own_ph_radial_temperature_reduction`, but the **Berger equation and its boundary derivation are not owner verified**.

Future action: compare PDF equations against local dossier, quote exact source pages/coordinate/bases, reconcile the 2008 equation with the BEP proposal and actual notebook, then decide whether equation-level Math nodes can rise from Idea to AI worked out. Avoid treating the user's recollection alone as citation verification.
