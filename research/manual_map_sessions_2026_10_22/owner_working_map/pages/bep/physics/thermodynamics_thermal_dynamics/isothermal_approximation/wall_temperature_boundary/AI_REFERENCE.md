> **AI RESEARCH REFERENCE — not owner-authored reader writing.** Preserved from an earlier auto-written index after the 23 October owner correction. Content may include unreviewed formulae, claims, questions or draft topology. The live node summary/maturity and approval decisions in `current_map.yaml` are authoritative; if the node was withdrawn, see `bridges/REVIEW_REQUIRED_PDE_MODEL_PROPOSALS_2026_10_23.md`. Treat this only as supporting reference, not a personal knowledge claim or an Informal Writing index.

# Prescribed wall temperature — the boundary is not the interior

A **Dirichlet boundary condition** supplies a value of a field at a boundary. For a cylindrical thermal problem it is possible to prescribe a wall temperature, for example \(T(R,z,t)=T_w\).

This fixes temperature **at the wall**, not everywhere in the tube. The center can remain hotter or colder if heat is generated, transported or removed in a spatially nonuniform way. Holding the outer ring at one temperature does not magically propagate that temperature throughout the reactor.

This is the physical distinction the owner explained and approved as **Human worked out**. The particular mathematical boundary equation, geometry, applicability and competing Robin/heat-flux closures are **separate candidate modeling details**, not automatically human understood or proven for the BEP apparatus.

**Links:** [Isothermal theory](../AI_REFERENCE.md) · Radial reduction (sibling) · future Reactor Model boundary conditions and heat-transfer assumptions (not yet placed).
