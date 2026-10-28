# Periodic operation, CO modulation, and hypotheses

## Two forcing questions are present

The written proposal centers periodic feed-concentration forcing of acetylene, C_in(t), and asks how it changes spatial adsorbate dynamics and ethylene selectivity in a one-dimensional packed bed. Its B-spline waveform and yield-optimization plans are proposal content, not completed computations.

The October 23 supervisor-meeting record introduces a second framing: modulate CO concentration to alter surface occupation and test whether activity and ethylene selectivity can be decoupled. The transcript says hydrogen-only modulation was expected not to beat steady operation. This is supervisor guidance captured by speech transcription, not a measured BEP result.

The two framings should remain separate until the owner confirms the project question. CO co-feed modulation changes the manipulated species and may require different kinetics, safety bounds, and comparison conditions from acetylene-feed forcing.

## What the hypotheses do and do not say

- **Proposal hypothesis:** periodic forcing may change intermediate selectivity through nonlinear chemistry and transient states. It is not an established yield improvement.
- **CO hypothesis from the meeting record:** changing CO surface coverage may trade conversion against selectivity. The fixed-temperature Schbib benchmark provides source-specific CO-containing kinetics, but the benchmark audit does not demonstrate periodic improvement or transfer the law to PdAg.
- **Surface-memory question:** explicit θ dynamics may produce history dependence at the same local gas composition. A PSSA model can still have outlet phase lag from finite gas or pore residence, so outlet lag alone does not identify surface memory.
- **Optimization hypothesis:** a periodic input may outperform a fair steady reference only after a target-appropriate forward model, shared constraints, an agreed objective, and a best-feasible steady comparator exist.

The 14 October periodic-outlook note labels itself assistant-written and not evaluated by the owner. Its net-ethylene objective, waveform discussion, and proposed comparison are useful candidate definitions, not an approved metric or result.

## Comparisons that remain candidate methods

Possible later comparisons in the source record include acetylene forcing versus CO forcing, PSSA versus non-PSSA surface kinetics, specified periodic inputs versus constant feed, and periodic input versus the best feasible steady operating point. Each comparison must use the same catalyst, reactor, feed basis, constraints, and output definitions. Gross ethylene outflow can mislead when ethylene is already present in the feed; the source note proposes net production as one candidate measure, not a confirmed convention.

## Current evidence boundary

The source record contains no target-catalyst periodic-gain result, no validated optimum, and no completed experiment showing that CO modulation beats optimized steady operation. Urmès 2022 is cited in the existing map as a modulation-excitation precedent, but its full paper and supporting information were reported inaccessible in the saved audit. Its reported experiment must not be described as the BEP CO-forcing result.

## Sources

- [Original proposal](https://github.com/AsapLoso/project-management-agents/blob/6cc49d86f8b5359a9f8826d36374ed3e29b727a1/Academics/BEP/Catalysis/0_Project_Management/main.tex)
- [Periodic-optimization outlook](../../planning/source-snapshots/aapm-devcontainer/Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md)
- [Supervisor meeting transcription](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/research/notes/meetings/2026-10-23_supervisor_meeting.md)
- [Integrated AI reference source-audit state](https://github.com/AsapLoso/BEP-Catalysis/blob/4a419354837486f65e00f26236826125b97e9b5b/research/integrated_reference_map_2026_10_22/source_evidence/state.md)
- [Schbib benchmark audit](https://github.com/AsapLoso/BEP-Catalysis/blob/884a5303adf112941b180cc7191cf8ef3c8604f7/research/reports/schbib_parameter_and_benchmark_audit.md)
