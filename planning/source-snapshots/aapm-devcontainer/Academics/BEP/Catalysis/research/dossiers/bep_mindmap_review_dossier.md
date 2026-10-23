# BEP Mind Map: Executive Review Dossier & Question Portfolio
Date: 2026-10-20  
Status: Ready for Human Owner Review  
Target Application: `Academics/BEP/Catalysis/mindmap/`  
Live Preview: `pixi run preview` (http://127.0.0.1:8765)

---

## 1. Executive Summary

This dossier presents the consolidated ownership mind-map architecture and research synthesis for the Dual BEP (Applied Physics & Applied Mathematics), formulated in accordance with **PR #84** and **Catalysis Project Conventions §13**.

The mind map separates ground truth into two distinct layers:
1. **Canonical Map (`data/bep_map.yaml`):** Contains 4 current canonical records: the BEP root and the three selected discipline arms. This structural count does not certify scientific claims or approve draft-overlay nodes.
2. **Draft Overlay (`data/bep_draft_overlay.yaml`):** Contains 33 draft records: 15 preserved legacy research nodes, 15 proposed Level-2 themes, 1 PDC support concept, and 2 user-selected C1 child Ideas. The child Ideas use their own tier values; every overlay record remains draft, and C1–C15 scientific review remains open.

---

## 2. Structural Topology & Branch Inventory

```
bep (Dual BEP: Acetylene Semi-Hydrogenation Reactor Modeling) [Tier 2, ★★★]
├── physics [Tier 0]
│   ├── reaction_thermodynamics [Tier 1, ★★★]
│   ├── lhhw_kinetics [Tier 1, ★★★]
│   │   ├── centered_arrhenius [Tier 1, ★★☆]
│   │   └── surface_coverage_dynamics [Tier 1, ★★★]
│   └── transport_phenomena [Tier 1, ★★★]
│       ├── internal_diffusion_thiele [Tier 1, ★★☆]
│       └── external_film_transfer [Tier 1, ★★☆]
├── mathematics [Tier 0]
│   ├── pbr_governing_pdes [Tier 1, ★★★]
│   ├── method_of_lines_mol [Tier 1, ★★★]
│   ├── stiff_ode_solvers [Tier 1, ★★★]
│   └── parameter_sensitivity_jacobian [Tier 1, ★★☆]
└── systems_control [Tier 0]
    ├── reactor_operating_window [Tier 1, ★★★]
    ├── periodic_feed_forcing [Tier 1, ★★★]
    ├── cooling_jacket_control [Tier 1, ★★☆]
    └── state_observer_mpc [Tier 1, ★★☆]
```

---

## 3. Recommended Sequential Review Path (Guided Tour)

The interactive preview visualizer features an automated **Guided Tour Mode** (`#btn-tour`) that walks the owner through foundational dependencies in order:

| Step | Node ID | Topic Title | Branch | Key Evidence / Citation |
|:---:|---|---|---|---|
| **1** | `reaction_thermodynamics` | Reaction Exothermicity | Physics | Larsen Ch.4 (dH = -172, -136 kJ/mol) |
| **2** | `lhhw_kinetics` | Extended LHHW Kinetics | Physics | Larsen Eqs. 6.9–6.11; Conventions §12.1 |
| **3** | `centered_arrhenius` | Centered Arrhenius Scaling | Physics | Berger (2008) Eq. 17; Conventions §11.5 |
| **4** | `surface_coverage_dynamics` | Dynamic Coverage State $\theta(z,r)$ | Physics | Berger Sec. 2.1; 3_Model/transient_model_audit |
| **5** | `transport_phenomena` | Coupled 3-Level Transport | Physics | Conventions §11 Item 1-3 ($C_b \to C_s \to c_p$) |
| **6** | `internal_diffusion_thiele` | Intraparticle Pore Diffusion | Physics | Berger Sec. 5; Weisz-Prater / Thiele scaling |
| **7** | `external_film_transfer` | Fluid-Solid Film Resistance | Physics | Mears criterion; Sherwood-Reynolds correlation |
| **8** | `pbr_governing_pdes` | 1D Dynamic PBR PDEs | Mathematics | Larsen Eqs. 4.6–4.9; Berger Eq. 1 recovery |
| **9** | `method_of_lines_mol` | Method of Lines Discretization | Mathematics | Upwind convection + Central diffusion (MOL) |
| **10** | `stiff_ode_solvers` | Stiff DAE/ODE Solvers | Mathematics | BDF / Radau IIA via `solve_ivp` |
| **11** | `parameter_sensitivity_jacobian` | Sensitivity & Identifiability | Mathematics | Forward sensitivity equations $s_{ij}$ |
| **12** | `reactor_operating_window` | Operating Window & Runaway | Control | van Heerden thermal runaway boundary |
| **13** | `periodic_feed_forcing` | Periodic Flow Modulation | Control | Urakawa / Silveston modulated excitation |
| **14** | `cooling_jacket_control` | Multi-Zone Cooling Dynamics | Control | PDC tubular reactor jacket feedback |
| **15** | `state_observer_mpc` | State Observers & Nonlinear MPC | Control | Conventions §5 candidate methods framing |

---

## 4. Question Portfolio & Reversible Defaults

### Q-BEP-REVIEW-01: How should reaction rates be normalized in the 1D PBR given that cross-sectional area A and catalyst support density rho_support are omitted from Larsen (2024)?
- **Island / Domain:** Physics: Kinetics
- **Rationale:** Conventions §12.3 and §12.4 confirm Appendix F contains experimental setup details on non-OCR raster pages. Extracting primary facts preserves zero-hallucination ground truth.
- **Recommended Default:** (Recommended) Render raster pages 77–88 (Appendix F) as high-res images to extract experimental tube diameter and bed packing specifications.
- **Options:**
  - (Recommended) Render raster pages 77–88 (Appendix F) as high-res images to extract experimental tube diameter and bed packing specifications.
  - Adopt standard micro-reactor tubular geometry (e.g. 4 mm inner diameter, catalyst bed density 800 kg/m^3) and document as an explicit modeling assumption.

### Q-BEP-REVIEW-02: Which reference temperature T0 should be selected for the Centered Arrhenius parameter re-scaling?
- **Island / Domain:** Physics: Temperature Dependence
- **Rationale:** Minimizes covariance between pre-exponential factor k0 and activation energy Ea around the experimental data cluster (Berger Eq. 17).
- **Recommended Default:** (Recommended) T0 = 313.15 K (40 °C), matching the central isotherm of the Larsen catalyst kinetic screening tests.
- **Options:**
  - (Recommended) T0 = 313.15 K (40 °C), matching the central isotherm of the Larsen catalyst kinetic screening tests.
  - T0 = 323.15 K (50 °C), matching the midpoint of the industrial acetylene converter operating window.

### Q-BEP-REVIEW-03: Should hydrogen adsorption on the Ag-promoted Pd catalyst be modeled as associative or dissociative?
- **Island / Domain:** Physics: Adsorption Mechanism
- **Rationale:** Conventions §12.1 verified Larsen Eq. 6.9 verbatim against the thesis text; altering the rate denominator to sqrt(p_H2) would invalidate benchmark parameters.
- **Recommended Default:** (Recommended) Non-dissociative (associative) molecular adsorption as formulated in Larsen Eq. 6.9 (final fitted model).
- **Options:**
  - (Recommended) Non-dissociative (associative) molecular adsorption as formulated in Larsen Eq. 6.9 (final fitted model).
  - Dissociative adsorption with square-root hydrogen partial pressure dependence sqrt(p_H2).

### Q-BEP-REVIEW-04: Should fluid velocity in the 1D axial transport equations be superficial velocity u_s or interstitial velocity u_s / epsilon_b?
- **Island / Domain:** Physics: Velocity Definition
- **Rationale:** Conventions §12 open ambiguity confirms a factor of epsilon_b (~0.4) on the convective scale directly shifts characteristic residence time tau_res and Peclet number Pe.
- **Recommended Default:** (Recommended) Superficial velocity u_s with explicit bed voidage epsilon_b in the accumulation term (Berger 2008 Eq. 1).
- **Options:**
  - (Recommended) Superficial velocity u_s with explicit bed voidage epsilon_b in the accumulation term (Berger 2008 Eq. 1).
  - Interstitial velocity u = u_s / epsilon_b throughout all convective terms.

### Q-BEP-REVIEW-05: Which spatial discretization scheme should be prioritized for the hyperbolic convective advection terms in the 1D PBR?
- **Island / Domain:** Mathematics: Numerical Discretization
- **Rationale:** Conventions §11 Item 7 locks backward/upwind difference as the baseline MOL scheme. Flux limiters can be introduced as a second-order refinement.
- **Recommended Default:** (Recommended) First-order backward/upwind difference for unconditional monotonic stability without spurious oscillations.
- **Options:**
  - (Recommended) First-order backward/upwind difference for unconditional monotonic stability without spurious oscillations.
  - Second-order upwind with flux-limiter (e.g. Superbee or Minmod) to reduce numerical dissipation during steep front propagation.

### Q-BEP-REVIEW-06: What is the primary objective function for periodic feed concentration forcing in the dual BEP?
- **Island / Domain:** Systems & Control: Dynamic Operation
- **Rationale:** Industrial semi-hydrogenation is fundamentally selectivity-limited; over-hydrogenation to ethane consumes valuable product and triggers severe exothermic hotspots.
- **Recommended Default:** (Recommended) Maximize ethylene selectivity S_C2H4 while constraining maximum bed temperature below runaway limit T_max = 380 K.
- **Options:**
  - (Recommended) Maximize ethylene selectivity S_C2H4 while constraining maximum bed temperature below runaway limit T_max = 380 K.
  - Maximize total acetylene conversion X_C2H2 regardless of intermediate selectivity.

---

## 5. Owner Action Guide (Deterministic Promotion)

To promote any draft topic to **Tier 2 (Owner Critically Understood)**:
1. **In Browser:** Run `pixi run preview`, open the Guided Tour, review the supporting citations and notes, and click **"Promote to Approved"**.
2. **Via MCP / Python CLI:**
   ```powershell
   pixi run python Academics/BEP/Catalysis/mindmap/editor.py promote-node --id lhhw_kinetics --tier 2
   ```
   *The editor atomically transfers the node from `bep_draft_overlay.yaml` into `bep_map.yaml` without manual copy-pasting.*
