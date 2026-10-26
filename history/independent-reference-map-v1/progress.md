# Progress — independent BEP scientific reference map v1

**Status:** independent v1 package committed in two logical increments; all seven files were read back byte-for-byte from the remote branch. PR creation is the final action.  
**Scope anchor:** `Academics/BEP/Catalysis/0_Project_Management/main.tex`.  
**Base branch:** `experiment/bep-independent-science-map-20261021`.  
**Work branch:** `work/bep-independent-reference-v1-20261021`.  
**Snapshot date:** 2026-10-21.

## Completed

- Read the work goal, source guide, data contract and execution plan on the exact experimental base branch.
- Read repository operating rules and relevant map/reversible-change review guidance; made no edits outside this task directory.
- Read the integrated proposal, bibliography, standalone intro/literature/method drafts and roadmap. Selected main.tex as the baseline and documented revision differences.
- Built an independently organized 63-node graph: one root, exactly three first-level disciplines, evidence-linked scientific themes and deeper concepts across physics, mathematics, and systems/control.
- Created 20 source/provenance records spanning proposal revisions, direct acetylene kinetics/periodic operation, catalyst-specific mechanisms, transport, MES and relevant reviews.
- Audited the broad literature-gap claim against the directly relevant Urmès et al. 2022 periodic acetylene study; recorded scope uncertainty because only its abstract and preview were accessible.
- Added explicit equation/unit conventions, model boundaries, claim audit and unresolved scientific questions. No calibration, simulation result or performance gain was invented.
- Disclosed the limited blind-stage exposure: two old C1 topic names appeared in required repository governance; no prior map YAML, generated nodes or legacy dossiers were opened.

## Stage status

| Stage | Status | Evidence |
|---|---|---|
| 0 — source comprehension | Complete | Proposal revision choice, source-access ledger and claim audit |
| 1 — independent hierarchy | Complete | Three prescribed disciplines and derived themes in nodes.yaml |
| 2 — deep scientific content | Complete for v1 scope | 63 nodes with explanations, equations, provenance and open questions |
| 3 — source/claim audit | Complete at accessible-source level | sources.yaml, claim_audit.md, uncertainties.md |
| 4 — baseline freeze and remote PR | Baseline committed and remote readback passed; PR creation next | See validation.md and final PR report |

## Research coverage

Physics: sequential and competing chemistry; surface inventories and mechanism dependence; bed and pellet transport; heat/aging; boundary sensing and MES limits.

Mathematics: signed stoichiometry and unit bases; conservative PDE and boundary conditions; Pe/Da/St conventions; MOL, schemes and stiff integration; inverse identifiability; periodic orbits and stability.

Systems & Control: feasible feed inputs and sensor models; periodic excitation; waveform families; matched steady benchmarks; optimization/robustness; future observability/estimation; experiment and validation design.

## Exact next scientific cursor

Obtain and inspect the full Urmès et al. (2022) article and Supporting Information, then resolve whether its model has spatially distributed axial transport and how its periodic-flow experiment maps to the PdAg target. In parallel, retrieve the cited Larsen thesis/underlying PdAg dataset and determine which mechanism, rates, conditions and measurement bandwidth are actually available. Only then should the dynamic parameterization, identifiable states and fair steady/dynamic comparison be finalized.

## Freeze bookkeeping

Core graph/source/method commit: `19dfa318bbbacb0459f8f6258932efe61136cfc3`. Support audit/progress/validation commit: `710a832f392c4210fecc8c4b02d2ab28876792c7`. After the second commit, all seven deliverable files were fetched from the remote branch and matched the staged bytes exactly. The final freeze-record commit SHA is reported in the PR and delivery rather than embedded in this file.
