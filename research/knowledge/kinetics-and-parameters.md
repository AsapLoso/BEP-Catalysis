# Kinetics and parameter provenance

## Kinetic model choices in the record

The older transient-model framework records Arrhenius temperature dependence and Langmuir coverage dependence as complementary parts of a rate expression. It also records a centered Arrhenius form and a literature-first forward simulation, with fitting as a later optional step. These are historical model-framework decisions in the September 2026 audit; they do not settle every model reduction or identify a final target-catalyst mechanism.

The main kinetic alternative is between an algebraic pseudo-steady-state closure and explicitly evolving surface coverages. A dynamic gas or pellet model with algebraic coverages can still show residence-time and transport lag. Outlet phase lag alone does not establish catalytic surface memory.

## Parameter sets are source-specific

The October 26 Schbib benchmark audit reports a source-checked fixed-temperature Pd/α-Al₂O₃ reference and keeps the printed parameter table separate from an author-shared correction. The report states that:

- the original printed set predicts at most 0.841% acetylene conversion where the cited Table 6 rows report 98.31–98.99%;
- the author-shared set brings acetylene conversion within 1.48 percentage points, while ethylene net-disappearance error remains as large as 10.763 percentage points;
- reproduction of both reported species remains blocked; and
- the correction’s author attribution is partial, while document integrity and publisher or erratum status remain unresolved.

Those are findings reported by the existing audit. This consolidation did not rerun the notebook. The report also says that no fit or parameter transfer to PdAg was performed.

The Larsen benchmark is a separate PdAg source study. The current benchmark index labels its audit as a selected-row review with unresolved conventions and data discrepancies, and explicitly says it does not model CO. Combining that parameterization with Schbib’s CO term is therefore a proposed synthesis, not an established target-catalyst rate law.

## CO and inhibition

The October 23 supervisor-meeting transcript frames CO as a reversible surface modifier that may trade activity for ethylene selectivity, and proposes testing periodic CO modulation. This is a supervisor discussion captured by speech transcription, not an independent kinetic measurement. The Schbib audit provides a source-specific CO-containing Pd/α-Al₂O₃ reference; it does not validate transfer to PdAg or demonstrate a periodic benefit.

## Owner understanding and open evidence

The owner-map handoff keeps source-linked chemistry at AI-attached status and records no human-verified claim/source links at its checkpoint. No parameter or rate law in these notes is promoted to personally understood or approved knowledge.

Open points include the target catalyst and site model, complete target-specific parameter values with units and covariance, the source basis of every adsorption constant, the effect of the author-shared Schbib correction, and whether a PdAg–CO synthesis is identifiable from available measurements.

## Sources

- [Transient-model framework audit](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md)
- [Model state and historical code audit](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/3_Model/state.md)
- [Schbib (1996) parameter and benchmark audit](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/research/reports/schbib_parameter_and_benchmark_audit.md)
- [Larsen benchmark status](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/notebooks/benchmarks/README.md)
- [Integrated AI reference-map source audit](https://github.com/AsapLoso/BEP-Catalysis/blob/4a419354837486f65e00f26236826125b97e9b5b/research/integrated_reference_map_2026_10_22/source_evidence/state.md)
