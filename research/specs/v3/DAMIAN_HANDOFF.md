# BEP V3 owner-review handoff for Damian

**Draft for owner review only. Not sent.** The scientific assumptions below have not been individually approved by the owner.

V3 now runs as a 64-cell transient gas plug-flow model with the Urmès et al. (2019) Table 5 PSSA rate law. It uses source-condition feed, pressure, molar flow, active catalyst mass and catalyst/tube descriptors. The baseline has four gas states, algebraic surface coverages, no pellet diffusion, no film, no axial dispersion and no energy equation. A 10% common 20 Hz sine illustrates gas transport through an assumed bed; it is not a published transient or a BEP/PdAg prediction.

The notebook executed with Python 3.12.14, NumPy 2.5.3, SciPy 1.18.0 and Pydantic 2.13.5. The baseline solver completed five periods; the minimum concentration was positive. The steady conversion changed by 0.00066% between 64 and 128 axial cells, and the tighter-tolerance outlet trace differed by 0.0077% relative RMS. Stoichiometric, input-mutation, inlet-boundary, geometry-basis and integrated source/outflow checks are included in the notebook.

The Urmès point comparison is mixed. At 51°C, V3 gives conversion 0.1312 versus the Table 1 pooled value 0.13, and ethane flow 0.0460 versus 0.07 μmol/s. At 62°C it gives conversion 0.2451 versus 0.23 and ethane 0.0994 versus 0.11 μmol/s. These are model-to-paper comparisons, not experimental validation; Table 1 aggregates repeats across two catalyst loadings and does not give individual values. No parameter was retuned to force agreement.

The original paper itself prints K₁=611 Pa⁻¹ on p. 5 and K₁=13 Pa⁻¹ in Table 5 on p. 6. V3 uses 13 for the fitted-model attempt and calculates the effect of 611 at the same feed; that changes the computed rates by roughly 46× and places H coverage above the paper's stated range. This exposes the consequence but does not resolve the paper's discrepancy or explain it as a unit conversion.

The 0.45 bed void fraction is borrowed from V2 and controls the transient lag. Bed length is reconstructed from Table 7's h/dₚ ratio and the midpoint of the source sieve interval. The no-transfer criteria belong to the Urmès Pd/α-Al₂O₃ experiments, not to the BEP catalyst. PSSA does not provide dynamic surface time constants.

Ready for review: the five-source theory map, bounded blueprint, executed V3 notebook, source manifest, theory crosswalk and proposed study questions. The next useful owner discussion is the K₁ source conflict and the limits of transferring the Urmès PSSA closure to the BEP catalyst. The personal map remains untouched. No message has been sent to Damian.
