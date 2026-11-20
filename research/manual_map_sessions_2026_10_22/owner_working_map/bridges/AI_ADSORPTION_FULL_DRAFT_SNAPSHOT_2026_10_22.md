# Adsorption — archival full draft and AI technical additions

**Purpose:** hidden scientific/documentation history, NOT the owner-facing Tier-5 reading page. This retains the source-heavy user + AI draft exactly as saved before reworking the view to show only owner's text and questions. Original Git blob SHA: `5aee700aa5994bad6835bd153df05616792253a2`. Owner-approved conceptual prose stays in the lean Tier-5 `index.md`; one- versus two-site occupancy, LH/ER, citations and caveats remain AI-attached, not human-verified. This archive is not an additional personal-map node.

---

# Adsorption

There are only so many available sites on a catalyst surface. Molecules from the gas can stick to them (adsorption), and once they're there they might react with hydrogen or other surface species. You can get intermediates along the way; these can stay adsorbed and react further, or leave the surface (desorption). Even ethylene that has desorbed could later be adsorbed again if it encounters another active site.

In a simple model, I can count one effective site per adsorbed molecule. Of course that doesn't mean a molecule literally touches just one Pd atom or that all those sites are simply the atoms on the *outside* of a porous pellet. How many sites are actually accessible or occupied, and when the catalyst is saturated, needs its own discussion.

My colleague described adsorption as helping orient molecules so it's easier for them to react. That seems like part of it. The catalyst also changes the interactions/forces between the molecules and the surface: it can make some bonds easier to break or form, not only point things in the right direction.

**What I'd still like to discuss:** Could a gas-phase molecule penetrate into the pores and react directly with acetylene already adsorbed on an internal surface? How far does gas penetrate before diffusion and reaction limit its access? I shouldn't assume deep pores are inactive without checking the transport and reaction conditions. This is distinct from whether the microscopic reaction uses adsorbed reactants or a direct gas–surface encounter.

**Visual cross-reference:** The adsorption panels in **VIS-MICRO-20261022-A** and **VIS-MICRO-20261022-B** are useful pictures of H₂ dissociation and acetylene attachment. Both uploaded images are attached to the [parent Tier-4 Microscopic Reaction Pathways page](../index.md#visual-references-attached-to-this-subject-user-provided-not-verified) and registered by exact Library asset IDs in `current_map.yaml`. They remain AI-generated and **unverified**, not source evidence for our catalyst.

## AI model-specific clarification — not yet accepted as my own understanding

In the supported-Pd model described by **Urmès et al. (2019), Table 3**, acetylene occupies one **effective** model site, while hydrogen dissociates across two vacant sites:

- `C₂H₂(g) + * ⇌ C₂H₂*`
- `H₂(g) + 2* ⇌ 2H*`

Here `*` represents a vacant model site. A **Langmuir–Hinshelwood-type** step involves species adsorbed on the surface; an **Eley–Rideal-type** step involves a gas-phase species reacting with an adsorbed one. These are *possible mechanism classes*, not proof that Eley–Rideal is important for our PdAg catalyst. Neither a one-site model nor a simple orientation argument can identify the physical site geometry or the activation barrier by itself.

**Question to take to Damian (23 October 2026; discussion note, no calendar appointment):** Could gas-phase hydrogen (or another relevant gas-phase reactant) reach acetylene adsorbed on pore-internal catalyst surfaces and react directly with it, or is the supported-Pd mechanism with both partners adsorbed the appropriate description for our reactor? How should we evaluate gas penetration into a pellet versus adsorption onto an active surface? This asks about the relevance of a gas–surface mechanism, *not* whether the interior of a porous catalyst is necessarily inactive. As a secondary question, what do our effective site counts mean?

## Boundary, source and status

**Informal Writing — owner approved** the conversational text, with the colleague attribution and Damian question corrected here. This is not Formal Writing. The first paragraphs are an edited account of my description, and the orientation/bond-interaction explanation is included in my understanding; model-specific formulas, named encounter mechanisms and citation truth in the separate AI clarification remain to be verified against the actual catalyst and papers. **Catalyst saturation/site capacity, poisoning and sintering/agglomeration are separate bridge topics** linked to adsorption, not new child nodes here. No rate law, target-catalyst surface route, measured coverage or citation was verified by the owner.

- [Urmès et al. (2019), *Catalysts* 9, 180, Table 3](https://doi.org/10.3390/catal9020180) — supported Pd/α-Al₂O₃ mechanism, full text recorded as AI-checked; not BEP catalyst proof.
- [Existing AI reference node `c1_surface_sites` and `c1_dissociative_h2_adsorption`](../../../../../../../reference_map.yaml) — source provenance, not owner verification.
- `B-ER-01`, `B-ADS-GEOMETRY`, `B-SAT-01` in the bridge register — unresolved placement/review.
