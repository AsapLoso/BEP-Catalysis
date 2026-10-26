> **AI RESEARCH REFERENCE — not owner-authored reader writing.** Preserved from an earlier auto-written index after the 23 October owner correction. Content may include unreviewed formulae, claims, questions or draft topology. The live node summary/maturity and approval decisions in `current_map.yaml` are authoritative; if the node was withdrawn, see `bridges/REVIEW_REQUIRED_PDE_MODEL_PROPOSALS_2026_10_23.md`. Treat this only as supporting reference, not a personal knowledge claim or an Informal Writing index.

# Approximations & Assumptions — explicit model choices

This is the bookkeeping place for assumptions made when deriving or implementing the **particular BEP model**. Each entry should later cite a relevant physical theory node, the mathematical reduction and the actual implementation location.

The starting three assumptions to record independently are:
- **Isothermal model:** prescribe temperature rather than evolving a temperature PDE.
- **Radial reduction:** retain axial coordinate \(z\), do not resolve the radial \(r\) coordinate in the bed-level model.
- **Axial dispersion / plug flow:** decide whether \(D_{ax}\partial_z^2C_i\) is retained or neglected in the axial species balance.

These are **not interchangeable**. The proposal states a one-dimensional tubular model and strict isothermal baseline, *writes* a species equation containing axial dispersion, and separately hypothesizes a high-Péclet limit where dispersion is negligible. This does not settle the actual solver's implementation. Boundary-condition changes require separate mathematical review.

**Maturity: Idea.** This directory is not an assertion that each approximation has been physically validated.
