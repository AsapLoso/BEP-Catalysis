> **AI RESEARCH REFERENCE — not owner-authored reader writing.** Preserved from an earlier auto-written index after the 23 October owner correction. Content may include unreviewed formulae, claims, questions or draft topology. The live node summary/maturity and approval decisions in `current_map.yaml` are authoritative; if the node was withdrawn, see `bridges/REVIEW_REQUIRED_PDE_MODEL_PROPOSALS_2026_10_23.md`. Treat this only as supporting reference, not a personal knowledge claim or an Informal Writing index.

# Radial thermal reduction — retaining the axial direction

A cylindrical reactor has a **longitudinal/axial** coordinate and a **cross-sectional/radial** coordinate. Our one-dimensional model retains the **axial (long) direction** and does not resolve the entire radial profile.

The physical approximation behind this is that radial differences can be **small enough for the question being studied**. Then a model can use a cross-sectional representative temperature (or other averaged field) that varies with axial position and time. This is **not** automatically a spatially uniform temperature: a one-dimensional temperature field may still develop axial gradients or vary over time.

A narrow reactor, strong radial mixing or sufficiently effective heat transfer may help, but geometry or turbulence alone does not prove that the radial gradient vanishes. A wall value by itself is still only a boundary condition. Those further justifications and quantitative equations are **AI/Idea details** until examined separately.

The owner directly recognized and corrected **axial versus radial** and approved the elementary reduction distinction as **Human worked out**. The *actual notebook* and parameter regime have not been checked.

**Links:** [Isothermal theory](../AI_REFERENCE.md) · future Transport Phenomena radial reduction · future Reactor Model → Approximations (separate modeling choice).
