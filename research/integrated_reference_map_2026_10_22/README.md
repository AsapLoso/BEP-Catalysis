# Integrated BEP scientific reference map

This is the integrated, AI-authored reference dataset for the BEP on dynamic acetylene semi-hydrogenation in a packed-bed reactor. It replaces the proposed reconciliation taxonomy with a populated scientific graph, source ledger, evidence lineage, cross-disciplinary relations, concept disposition records and uncertainty register. It is data, not an application or a claim that the BEP model has been built or validated.

## Scientific hierarchy

The graph has 143 nodes under three discipline arms:

- **Physics:** reaction networks and products; catalyst identity, site ensembles and surface state; catalyst-specific kinetic closures; packed-bed, pellet and interphase transport; thermal/deactivation extensions; measurements and physical observables.
- **Mathematics:** stoichiometric and continuum balances; dimensionless groups and timescales; periodic response; discretization, stiffness and numerical verification; inverse problems, sensitivity and uncertainty; mathematical optimization.
- **Systems & Control:** plant boundary and input realization; periodic excitation and kinetic discrimination; cycle objective and best feasible steady comparison; measurement, observability and estimation; operational feasibility, robustness and validation.

The core connected threads are recorded in `interdisciplinary_links.yaml`:

1. Reaction pathways → catalyst/site inventories → adsorption and coverages → source-specific PSSA or explicit dynamic kinetics → conservative bed/pellet transport.
2. Stoichiometric and inventory balances → PDE/ODE/DAE coupling → spatial discretization → stiffness, stability, invariants and numerical verification.
3. Commanded and realized inputs plus physical measurements → reactor dynamics → identifiability and observability → periodic excitation → cycle-integrated comparison with the best matched steady feasible operation.

There are 59 typed scientific relations, including 35 cross-disciplinary connectors. Same-discipline relations are labelled separately. Every edge names its endpoints, interpretation, scope and source context; edges themselves are marked as AI-authored synthesis rather than direct observations.

The source-checked catalyst branches distinguish a one-site Pd PSSA, a deposit-associated Pd A/E model, Pd–Mn adsorption substitution, PdAg steady DFT/microkinetics, industrial Pd–Ag LHHW rates with campaign-scale activity decay, and a 2025 Pd/α-Al₂O₃ single-site closure scoped to near-atmospheric CO-free feeds. Their catalyst identities, evidence classes, units, assumptions, and limits on transfer to the BEP target remain explicit in the graph. Transport/numerics nodes derive variable-flow conservative balances, boundary-domain alternatives, finite-volume conservation, and a narrowly assumed explicit transport bound; target flow closure and solver convergence remain unknown. Identification/control nodes add local Fisher information and experiment-design criteria, a scoped persistency condition, and periodic-orbit closure while preserving target observability and performance as unknown.

## Files

- `nodes.yaml`: integrated hierarchical graph, explanatory content, equations with variable bases/units and assumptions, limitations, open questions, claim references and lineage pointers.
- `sources.yaml`: 66 source/context records with bibliographic identifiers, access status, locator, applicability and what each record cannot establish.
- `concept_mapping.yaml`: 171 old/proposed-record dispositions and the full 144-entry prior reconciliation crosswalk extended to integrated node IDs.
- `source_provenance.yaml`: source-record lineage, all 96 historical overlay attachments, local-resolution status and explicit citation-correction receipts.
- `interdisciplinary_links.yaml`: typed graph edges and evidence context.
- `claim_reconciliations.yaml`: 21 bounded claim decisions, corrections and disagreements.
- `uncertainties.yaml`: 29 open scientific or project-decision questions with evidence needed and linked concepts.
- `coverage.yaml`: coverage status and exact scientific boundaries for major areas.
- `method.md`, `progress.md`, `validation.md`: integration method, work status and structural validation.
- `evidence_audit.yaml`: ten source/derivation checks from the second pass, with source scope, node links and dispositions.
- `validate_data.py` and `validation_results.json`: reproducible graph/evidence-audit reference validator and result snapshot.

## Evidence and maturity

All graph content remains at `idea` or `ai_worked_out` maturity. No owner-understood or human-verified state is inferred. Claim references distinguish observations, source-model results, proposal hypotheses, derivations under assumptions and unverified legacy attachments. An attached source is not treated as proof unless a claim-specific locator and bounded support statement are recorded. A source with abstract-only or bibliographic-only access is not represented as full-text evidence.

The map does not demonstrate a periodic performance gain. It records conditional no-gain limits, the direct Pd/α-Al₂O₃ periodic acetylene precedent, competing catalyst-specific model classes, and what target-specific evidence would be needed to compare against an optimized steady operation.


## Research state

The catalyst/kinetics, transport/numerics, and identification/control research waves have substantive but partial source-backed additions. A representative same-agent second-pass audit is recorded; it is not an independent human review and the broader audit remains open. No target parameter estimation, solver/grid convergence study, target optimization, or target gain conclusion has been performed; see `progress.md`, `research_backlog.yaml`, and `coverage.yaml` for the remaining research boundary.


## Citation provenance mission

The passage-level evidence audit is tracked in `source_evidence/`. The starting inventory contained 340 current claim/source links and 96 historical overlay attachments. After B18 first pass, the ledger contains 349 current links, 166 passage records and 118 short quotations; 18 of 66 source records have been reopened, 48 remain unopened, 148 links have an AI evidence recheck, 146 links have passage IDs, and 203 have neither passage nor derivation. The B18 Waldron et al. (2020) record now includes eleven full-PDF passages across the local Fisher-information equations, bounded D-optimal design, model and parameter-prior assumptions, ramp-versus-steady parameter-precision results, validation caveats, fast-catalyst-response applicability, and HPLC sampling/dead-volume correction. It supports a bounded experiment-precision precedent in homogeneous esterification, not periodic BEP performance or an optimized-steady comparison. The RSC-listed SI and a local source hash remain uninspected/unavailable in this pass. Forty-two correction records include four B17 data-quality ledger repairs. Sixteen post-commit second-pass entries cover 154 passage outcomes; B18's separate second pass is pending. These counts are focused AI checks, not full validation or human review.
