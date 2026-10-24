# 03 — Model blueprint

- [x] Before writing V3 simulation code, derive `MODEL_BLUEPRINT.md` from compatible, supported theory. The Urmès PSSA closure is provisional for implementation; physical choices remain open to owner review.
- [x] Specify equations, state vector, units, boundary/initial conditions, closures, kinetics, parameter provenance, numerical method and source choices. Separate source-transferred, borrowed and assumed values.
- [x] Justify reuse or changes from V0 and V1/V2. Defer dynamic coverages, external film, heat balance or other features where their theory/parameters are unsupported.
- [x] Define conservation, positivity, boundary, units and solver checks; identify a candidate paper-matched steady-state comparison or document its evidence gap.
- [x] Gate receipt: explicit assumptions, alternatives, rationale, acceptance tests and unresolved owner-review questions before implementation.
