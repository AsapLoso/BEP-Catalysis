# Review-required PDE / model concepts — withdrawn from personal placements

Date: 2026-10-23. Live-map preimage blob: `52ad87e12a12e876d644a8a429447ba4c33f44ff`. This is **AI reference / discussion archive only**, not the owner's personal scientific map.

The owner corrected the previous auto-placement practice. They had not actually seen/reviewed the proposed thermal balance, heat-generation title/position, or the exact reactor-model/assumption tree before they were placed. They requested a return to one-topic-at-a-time preview and review, with undecided content kept in the queue and bridges. Preserve this content, but **do not automatically restore these seven nodes to `current_map.yaml`**. The user did NOT request a blanket rollback of other work.

- Thermal Energy Balance Theory: explain physical thermal conservation theory first. The user said they had not heard of it. The material is AI reference only.
- Reaction Heat Generation: the name "Reaction Heat Generation — Enthalpy × Reaction Rate" was rejected as an awful display title. The user sees a possible chemistry/individual-reactions position, **not yet decided**.
- Mathematics: `Mathematical Modeling` remains an approved existing parent. Beneath it the proposed `Reactor Model`, `Model Assumptions & Approximations`, and exact three assumption entries (isothermal field, radial reduction, axial dispersion/plug-flow) need direct owner preview/refresh before inclusion. These reflect plausible future structure but the owner retracted assumed approval.
- Where code or physical reference material exists, retain it as AI notes but do not call it Informal Writing.
- Parent/sibling relation and maturity must be shown for **each exact proposed node** to the owner before future approval.

## Previously inserted data, preserved verbatim as JSON

```json
[
  {
    "id": "own_ph_thermal_energy_balance_theory",
    "parent": "own_ph_thermodynamics_thermal_dynamics",
    "title": "Energy Balance — Thermal Conservation Theory",
    "kind": "concept",
    "approval": "accepted",
    "structure_status": "owner_explicit_scoped_placement_2026_10_23",
    "maturity": "idea",
    "understanding_status": "idea",
    "human_understanding_review": "not_assessed",
    "owner_read_status": "not_assessed",
    "owner_content_approval": "idea_or_equation_only",
    "source_claim_review": "ai_attached_only",
    "summary": "The theoretical energy balance accounts for energy storage, convection, heat transport, chemical heat sources and wall exchange; the chosen BEP reactor equation is a distinct future Mathematics node.",
    "notes": "This is an owner-approved high-level Theory position. Conservation of thermal/enthalpy energy says accumulation equals net inward transport plus source, with definitions for solid/gas/bed bases, thermal coupling and BCs. Distinguish the full balance from heat-generation q'''_rxn and from imposing T=T₀. AI reference ph_energy_balance contains one illustrative pseudo-homogeneous non-isothermal balance including heat exchange, but the owner has not yet studied/selected an equation or material parameters. No source/model verification or maturity promotion. Future Reactor Model energy balance is separate mathematical representation/choice and cross-links here.",
    "sources": [],
    "claims": [],
    "equations": [],
    "open_questions": [],
    "related_ids": [
      "own_ph_isothermal_theory"
    ],
    "related_ai_reference_ids": [
      "ph_energy_balance",
      "u_ph_thermal"
    ],
    "related_bridge_ids": [
      "B-P4",
      "B-M1",
      "B-HEAT-LENSES-01"
    ],
    "reader_file": {
      "path": "owner_working_map/pages/bep/physics/thermodynamics_thermal_dynamics/energy_balance_theory/index.md",
      "kind": "working_explanation",
      "visibility": "node_detail",
      "status": "idea_later_theory",
      "human_review": "not_assessed"
    },
    "origin": "user_explicit_2026_10_23_PDE_map_split",
    "decision_receipt": {
      "date": "2026-10-23",
      "authority": "User: 'Part A and B ... human worked out'; 'those equations as ideas (or AI worked out if cited) below the actual physics'; 'Energy balance theory is definitely going to be a node under thermodynamics'.",
      "exact_scope": "User says energy-balance theory definitely deserves a Thermodynamics node, not an actual model equation.",
      "scientific_source_verification": "none",
      "owner_equation_derivation_approval": "none"
    }
  },
  {
    "id": "own_ph_reaction_heat_generation",
    "parent": "own_ph_reaction_chemistry_pathways",
    "title": "Reaction Heat Generation — Enthalpy × Reaction Rate",
    "kind": "concept",
    "approval": "accepted",
    "structure_status": "owner_explicit_Math_model_or_chemistry_placement_2026_10_23",
    "maturity": "idea",
    "understanding_status": "idea",
    "human_understanding_review": "not_assessed",
    "owner_read_status": "not_assessed",
    "owner_content_approval": "placement_only",
    "source_claim_review": "ai_attached_only",
    "summary": "Heat-generation rate combines the enthalpy change per mole of reaction with the rate at which each independent kinetic reaction proceeds; it connects chemistry to an energy balance but is not that balance.",
    "notes": "CHEMICAL/REACTION-KINETIC LENS. Heat from each channel is the product of its molar enthalpy change (J/mol reaction) and its reaction-progress rate (mol/(m³ s) on a consistent bed-volume basis); summed over independent channels, the conventional volumetric source is q'''_rxn=−Σ_jΔ_rH_j r_j^(V). The factor r_j is the reaction rate the owner identified; the stoichiometric coefficients ν_ij enter the construction of Δ_rH_j and of species source S_i=Σ_jν_ijr_j, but need not be inserted again as additional factors in the thermal sum. The R3 stoichiometric equality R3=R1+R2 does not imply an independent r3: avoid double counting heat if R3 is only a composite net accounting identity. The exact catalyst mass/void-bed-volume basis must be resolved from BEP code. This scientific *quantity* belongs with chemistry/rates; Thermodynamics gets enthalpy/energy balance theory; the eventual Mathematical Model gets the specific source term and closure. Detailed equation evidence is AI-only in bridge THERMAL_REACTION_HEAT_SOURCE_CONCEPT_2026_10_23.md, no actual BEP source term checked. Owner has approved the CONCEPT POSITION, but not a mature equation derivation.",
    "sources": [],
    "claims": [],
    "equations": [],
    "open_questions": [
      "Verify model-specific equation, physical justification and implementation before future stage promotion."
    ],
    "related_ids": [
      "own_ph_net_hydrogenation",
      "own_ph_thermal_energy_balance_theory"
    ],
    "related_ai_reference_ids": [
      "reaction_thermodynamics",
      "ph_energy_balance",
      "ma_stoichiometry",
      "ph_axial_balance"
    ],
    "related_bridge_ids": [
      "B-P1-NET",
      "B-LH-ARR-01",
      "B-HEAT-LENSES-01"
    ],
    "reader_file": {
      "path": "owner_working_map/pages/bep/physics/reaction_chemistry_pathways/reaction_heat_generation/index.md",
      "kind": "working_explanation",
      "visibility": "node_detail",
      "status": "idea_unverified_kinetic_basis",
      "human_review": "not_assessed"
    },
    "background_files": [
      {
        "path": "owner_working_map/bridges/THERMAL_REACTION_HEAT_SOURCE_CONCEPT_2026_10_23.md",
        "visibility": "hidden",
        "purpose": "Full heat source equation and rate/stoichiometry audit; not human verified"
      }
    ],
    "origin": "owner_2026_10_23_parallel_PDE_map_layout",
    "decision_receipt": {
      "date": "2026-10-23",
      "authority": "Owner: 'under math, you have the model, and then you have approximations, and then we put all our approximations'; reaction heat generation belongs in reaction/kinetic context; stage not promoted without review.",
      "approved_scope": "Owner: put reaction-heat generation under kinetics/reaction pathways, not under isothermal; idea stage, equation detail separate.",
      "human_understanding_approval": "none",
      "source_verification": "none"
    }
  },
  {
    "id": "own_ma_reactor_model",
    "parent": "own_ma_mathematical_modeling",
    "title": "Reactor Model — Concrete BEP Representation",
    "kind": "concept",
    "approval": "accepted",
    "structure_status": "owner_explicit_Math_model_or_chemistry_placement_2026_10_23",
    "maturity": "idea",
    "understanding_status": "idea",
    "human_understanding_review": "not_assessed",
    "owner_read_status": "not_assessed",
    "owner_content_approval": "placement_only",
    "source_claim_review": "ai_attached_only",
    "summary": "Mathematical home for the selected BEP reactor equations, boundary conditions, assumptions and kinetic closures, each linked to their independent physical theory.",
    "notes": "Owner explicitly decides that the concrete Reactor Model belongs within Mathematics under the existing Mathematical Modeling node. It is a structure for the representation chosen in the BEP, not a competing physical theory tree. Children include the model's assumptions/approximations, future conservation-balance equations, kinetic closures and mathematical BC requirements, as separately reviewed. The physical theories (thermodynamics, transport, LH kinetics, chemical reactions) remain elsewhere with crosslinks. Before asserting implementation, check current code/notebooks versus the historical proposal: the proposal presents a general axial dispersion PDE but hypothesizes high-Pe negligible dispersion. Model-level assumptions may be accepted as described in proposal without implying code-level confirmation. This parent remains IDEA despite highly worked AI reference PDEs, because owner has not studied the complete implemented equation set. Existing Surface Kinetic Equations is a separate Tier3 sibling; crosslink rather than reparenting while another agent edits it.",
    "sources": [
      {
        "id": "proposal_main",
        "title": "BEP original proposal — Dynamic Control of Acetylene Semi-Hydrogenation",
        "path": "Academics/BEP/Catalysis/0_Project_Management/main.tex",
        "locator": "Methodology §3.1, lines 175–192; plan/model not audited executable",
        "source_access": "local_project_document_checked",
        "review": "ai_attached",
        "human_verified": false
      }
    ],
    "claims": [],
    "equations": [],
    "open_questions": [
      "Verify model-specific equation, physical justification and implementation before future stage promotion."
    ],
    "related_ids": [
      "own_ma_surface_kinetic_equations",
      "own_ph_isothermal_theory",
      "own_ph_reaction_heat_generation"
    ],
    "related_ai_reference_ids": [
      "ma_gas_pde",
      "ma_pde_ode_coupling",
      "ph_axial_balance"
    ],
    "related_bridge_ids": [
      "B-M1",
      "B-M2",
      "B-M3",
      "B-LH-ARR-01",
      "B-MODEL-BC-01",
      "B-TP-REDUCTIONS-01"
    ],
    "reader_file": {
      "path": "owner_working_map/pages/bep/mathematics/mathematical_modeling/reactor_model/index.md",
      "kind": "working_explanation",
      "visibility": "node_detail",
      "status": "owner_scoped_structure",
      "human_review": "not_assessed"
    },
    "origin": "owner_2026_10_23_parallel_PDE_map_layout",
    "decision_receipt": {
      "date": "2026-10-23",
      "authority": "Owner: 'under math, you have the model, and then you have approximations, and then we put all our approximations'; reaction heat generation belongs in reaction/kinetic context; stage not promoted without review.",
      "approved_scope": "Owner explicitly: under Mathematics existing model branch, make Reactor Model and Approximations tree now; no automatic approval of details in notebook.",
      "human_understanding_approval": "none",
      "source_verification": "none"
    }
  },
  {
    "id": "own_ma_model_approximations",
    "parent": "own_ma_reactor_model",
    "title": "Model Assumptions & Approximations",
    "kind": "concept",
    "approval": "accepted",
    "structure_status": "owner_explicit_Math_model_or_chemistry_placement_2026_10_23",
    "maturity": "idea",
    "understanding_status": "idea",
    "human_understanding_review": "not_assessed",
    "owner_read_status": "not_assessed",
    "owner_content_approval": "placement_only",
    "source_claim_review": "ai_attached_only",
    "summary": "The explicit location for each chosen idealization in the BEP reactor model—temperature, cross-sectional spatial reduction and axial dispersion—linked back to the corresponding physical theory.",
    "notes": "Only a STRUCTURAL umbrella. Distinguishes model choices from physics and source-supported equations. Three starting candidate model assumptions: (1) globally fixed T as opposed to boundary-only T, (2) 1D axial representation discarding radial coordinate/gradients, and (3) whether or not the axial species dispersion D_ax∂²_z C_i is kept. These reductions are logically independent. Boundary data depend on the PDE spatial order; flux/Robin Danckwerts inlet with dispersion, Dirichlet inlet in ideal advection limit, and thermal wall boundary are different conditions. The exact chosen BCs and physical validity are in math bridge B-MODEL-BC-01 until reviewed. Turbulence is future/out-of-scope and cannot automatically imply no radial gradients. No claims about final solver implementation.",
    "sources": [
      {
        "id": "proposal_main",
        "title": "BEP original proposal — Dynamic Control of Acetylene Semi-Hydrogenation",
        "path": "Academics/BEP/Catalysis/0_Project_Management/main.tex",
        "locator": "Methodology §3.1 lines 180–185: radial 1D, D_ax term, Danckwerts, T=T0; hypotheses 129–134: high Pe",
        "source_access": "local_project_document_checked",
        "review": "ai_attached",
        "human_verified": false
      }
    ],
    "claims": [],
    "equations": [],
    "open_questions": [
      "Verify model-specific equation, physical justification and implementation before future stage promotion."
    ],
    "related_ids": [
      "own_ph_isothermal_theory",
      "own_ph_radial_temperature_reduction"
    ],
    "related_ai_reference_ids": [
      "ma_gas_pde",
      "ph_axial_dispersion",
      "ph_isothermal"
    ],
    "related_bridge_ids": [
      "B-M1",
      "B-P3",
      "B-P4",
      "B-MODEL-BC-01",
      "B-TP-REDUCTIONS-01"
    ],
    "reader_file": {
      "path": "owner_working_map/pages/bep/mathematics/mathematical_modeling/reactor_model/approximations/index.md",
      "kind": "working_explanation",
      "visibility": "node_detail",
      "status": "structural_scaffold",
      "human_review": "not_assessed"
    },
    "origin": "owner_2026_10_23_parallel_PDE_map_layout",
    "decision_receipt": {
      "date": "2026-10-23",
      "authority": "Owner: 'under math, you have the model, and then you have approximations, and then we put all our approximations'; reaction heat generation belongs in reaction/kinetic context; stage not promoted without review.",
      "approved_scope": "Owner explicitly requests Mathematics → Mathematical Modeling → Reactor Model → Approximations and all initial assumptions. No maturity approval of actual code.",
      "human_understanding_approval": "none",
      "source_verification": "none"
    }
  },
  {
    "id": "own_ma_assumption_isothermal",
    "parent": "own_ma_model_approximations",
    "title": "Assumption: Isothermal Temperature Field",
    "kind": "concept",
    "approval": "accepted",
    "structure_status": "owner_explicit_Math_model_or_chemistry_placement_2026_10_23",
    "maturity": "idea",
    "understanding_status": "idea",
    "human_understanding_review": "not_assessed",
    "owner_read_status": "not_assessed",
    "owner_content_approval": "placement_only",
    "source_claim_review": "ai_attached_only",
    "summary": "Model-specific assumption to prescribe a fixed reactor temperature T=T₀ rather than predict thermal evolution, cross-linked to physical isothermal theory and wall-condition distinctions.",
    "notes": "PROPOSED/PROPOSAL-DOCUMENTED MODEL CHOICE, implementation not audited. BEP proposal says strictly T=T0 baseline. This should not be conflated with wall Dirichlet T(R,z,t)=Tw nor with radial averaging T≈Tbar(z,t). A global isothermal closure can be seen as a further special case of a radial-averaged one-dimensional temperature model if axial and temporal temperature variations are additionally eliminated/neglected; it does NOT follow automatically just from averaging over r. Mathematically temperature is imposed, so no independent dynamic energy PDE is solved for T in the baseline. The alternative selected equation (if later non-isothermal) belongs in a separate model-energy-balance node with theory crosslink. Whether actual notebook imposed T=T0 is not yet confirmed by this entry.",
    "sources": [
      {
        "id": "proposal_main",
        "title": "BEP original proposal — Dynamic Control of Acetylene Semi-Hydrogenation",
        "path": "Academics/BEP/Catalysis/0_Project_Management/main.tex",
        "locator": "Methodology §3.1, main.tex line 185: strictly isothermal model T=T0",
        "source_access": "local_project_document_checked",
        "review": "ai_attached",
        "human_verified": false
      }
    ],
    "claims": [],
    "equations": [],
    "open_questions": [
      "Verify model-specific equation, physical justification and implementation before future stage promotion."
    ],
    "related_ids": [
      "own_ph_isothermal_theory",
      "own_ph_wall_temperature_boundary",
      "own_ph_radial_temperature_reduction"
    ],
    "related_ai_reference_ids": [
      "ph_isothermal"
    ],
    "related_bridge_ids": [
      "B-P4",
      "B-HEAT-LENSES-01"
    ],
    "origin": "owner_2026_10_23_parallel_PDE_map_layout",
    "decision_receipt": {
      "date": "2026-10-23",
      "authority": "Owner: 'under math, you have the model, and then you have approximations, and then we put all our approximations'; reaction heat generation belongs in reaction/kinetic context; stage not promoted without review.",
      "approved_scope": "Explicit model assumption placeholder; no code validation or human math promotion.",
      "human_understanding_approval": "none",
      "source_verification": "none"
    }
  },
  {
    "id": "own_ma_assumption_radial_reduction",
    "parent": "own_ma_model_approximations",
    "title": "Assumption: One-Dimensional Axial Reactor (Radial Reduction)",
    "kind": "concept",
    "approval": "accepted",
    "structure_status": "owner_explicit_Math_model_or_chemistry_placement_2026_10_23",
    "maturity": "idea",
    "understanding_status": "idea",
    "human_understanding_review": "not_assessed",
    "owner_read_status": "not_assessed",
    "owner_content_approval": "placement_only",
    "source_claim_review": "ai_attached_only",
    "summary": "The reactor model retains the long axial coordinate z but does not resolve bed-level radial gradients; this dimensional reduction is separate from axial dispersion or isothermality.",
    "notes": "Owner understands the physical axial/radial distinction (human-owned theory child under Isothermal). Here we document the MODEL CHOICE: a 1D tube model with concentration and optionally temperature fields depending on z and t; no resolved reactor-radius dimension r. This is not the same as setting D_ax=0 because D_ax is a dispersive term along the retained z direction. Thin-tube geometry is a motivation, not a proof of negligible gradients. Pellet-internal radial diffusion is a different spatial scale and may exist simultaneously with a 1D bed model. The actual final code and approximation error/transport regime have not been audited; use future TP theory crosslink.",
    "sources": [
      {
        "id": "proposal_main",
        "title": "BEP original proposal — Dynamic Control of Acetylene Semi-Hydrogenation",
        "path": "Academics/BEP/Catalysis/0_Project_Management/main.tex",
        "locator": "Methodology §3.1 lines 180–183: small-diameter 1D axial domain; no resolved radial bed gradients",
        "source_access": "local_project_document_checked",
        "review": "ai_attached",
        "human_verified": false
      }
    ],
    "claims": [],
    "equations": [],
    "open_questions": [
      "Verify model-specific equation, physical justification and implementation before future stage promotion."
    ],
    "related_ids": [
      "own_ph_radial_temperature_reduction"
    ],
    "related_ai_reference_ids": [
      "u_ph_transport",
      "ma_gas_pde",
      "ph_axial_balance"
    ],
    "related_bridge_ids": [
      "B-P3",
      "B-M1",
      "B-MODEL-BC-01",
      "B-TP-REDUCTIONS-01"
    ],
    "origin": "owner_2026_10_23_parallel_PDE_map_layout",
    "decision_receipt": {
      "date": "2026-10-23",
      "authority": "Owner: 'under math, you have the model, and then you have approximations, and then we put all our approximations'; reaction heat generation belongs in reaction/kinetic context; stage not promoted without review.",
      "approved_scope": "Owner explicitly requests radial reduction as separate Reactor Model approximation; exact code validation pending.",
      "human_understanding_approval": "none",
      "source_verification": "none"
    }
  },
  {
    "id": "own_ma_assumption_axial_dispersion",
    "parent": "own_ma_model_approximations",
    "title": "Assumption: Axial Dispersion / Plug-Flow Limit",
    "kind": "concept",
    "approval": "accepted",
    "structure_status": "owner_explicit_Math_model_or_chemistry_placement_2026_10_23",
    "maturity": "idea",
    "understanding_status": "idea",
    "human_understanding_review": "not_assessed",
    "owner_read_status": "not_assessed",
    "owner_content_approval": "placement_only",
    "source_claim_review": "ai_attached_only",
    "summary": "The model must specify whether axial species dispersion D_ax∂²_z C_i is retained or neglected; high Péclet number motivates a plug-flow limit but requires testing.",
    "notes": "This is the axial LONG-direction mixing term, distinct from radial bed reduction. The proposal writes a 1D advection-dispersion-reaction PDE with D_ax∂²_z C_i but separately hypothesizes negligible dispersion under high Pe. Thus the correct entry is an explicit unverified model approximation/choice, NOT 'the notebook definitely omits D_ax'. Removing axial diffusion changes the species PDE from second order to first order in z and changes appropriate boundary conditions; mathematical details remain in B-MODEL-BC-01 rather than being incorrectly promoted into an understood physics node. Pe screening depends on dimensions, residence-time distribution and forcing bandwidth; reference ph_axial_dispersion is AI-worked-out theory but this concrete model choice remains Idea.",
    "sources": [
      {
        "id": "proposal_main",
        "title": "BEP original proposal — Dynamic Control of Acetylene Semi-Hydrogenation",
        "path": "Academics/BEP/Catalysis/0_Project_Management/main.tex",
        "locator": "Hypotheses lines 129 and 133–134; displayed PDE lines 180–185 contains D_ax term",
        "source_access": "local_project_document_checked",
        "review": "ai_attached",
        "human_verified": false
      }
    ],
    "claims": [],
    "equations": [],
    "open_questions": [
      "Verify model-specific equation, physical justification and implementation before future stage promotion."
    ],
    "related_ids": [
      "own_ma_assumption_radial_reduction"
    ],
    "related_ai_reference_ids": [
      "ph_axial_dispersion",
      "ph_axial_balance",
      "ma_gas_pde"
    ],
    "related_bridge_ids": [
      "B-M1",
      "B-P3",
      "B-MODEL-BC-01",
      "B-TP-REDUCTIONS-01"
    ],
    "origin": "owner_2026_10_23_parallel_PDE_map_layout",
    "decision_receipt": {
      "date": "2026-10-23",
      "authority": "Owner: 'under math, you have the model, and then you have approximations, and then we put all our approximations'; reaction heat generation belongs in reaction/kinetic context; stage not promoted without review.",
      "approved_scope": "Owner explicitly wants separate axial dispersion approximation; term's implementation and Danckwerts BCs not owner-reviewed.",
      "human_understanding_approval": "none",
      "source_verification": "none"
    }
  }
]
```

## Existing reference material / bridges

`bridges/THERMAL_REACTION_HEAT_SOURCE_CONCEPT_2026_10_23.md`,
`bridges/TRANSPORT_AXIAL_DISPERSION_RADIAL_REDUCTION_2026_10_23.md`,
`bridges/BERGER2008_EQ1_BEP_LOCAL_PROVENANCE_2026_10_23.md`,
`B-MODEL-BC-01`, `B-HEAT-LENSES-01`, `B-P4`, `B-M1`.
