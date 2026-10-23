# Independent reference map — execution plan and acceptance checklist

**Goal:** scientifically useful, deeply structured AI reference data, centered on the original BEP proposal. The science is more important than the graph renderer or mechanical checklist completion.

## Phase 0 — Preflight and source comprehension

- [ ] Verify checkout and task branch descend from `experiment/bep-independent-science-map-20261021`.
- [ ] Read `WORK_GOAL.md`, `SOURCE_GUIDE.md` and `DATA_CONTRACT.md` in this directory.
- [ ] Read original proposal, its bibliography and standalone sections; explicitly reconcile different versions rather than silently mixing assumptions.
- [ ] Extract research question(s), physical system, manipulated variables, measured outputs, fundamental balances, planned methods and uncertainties.
- [ ] Build a source access/provenance ledger. Distinguish project intent from externally verified science.
- [ ] Do not alter the existing application or legacy scientific-data directories.

**Checkpoint:** `method.md` clearly states which proposal version and scientific premises are used.

## Phase 1 — Scientific hierarchy

- [ ] Level 0: scientific BEP root.
- [ ] Level 1: user-prescribed Physics / Mathematics / Systems & Control.
- [ ] Independently derive and explain Level 2 broad subject themes based on project science; do not force a predetermined number.
- [ ] Propose coherent deeper subtopics and interdisciplinary cross-links; avoid letter-shaped tree structure and arbitrary fixed depths.
- [ ] Analyze the scientific boundary of each Level-2 topic, rather than copying chapter headings.

**Checkpoint:** first populated `nodes.yaml` is connected, parseable and justifies thematic decisions.

## Phase 2 — Deep science research and content

- [ ] Develop detailed physics: catalysis/surface states, reaction paths, gas and pore transport, reactor physical assumptions, observable experimental quantities.
- [ ] Develop mathematical science: conservation laws, PDE/ODE/DAE formulations, boundary/initial data, nondimensionalization, numerics, stability, conditioning/inverse problems.
- [ ] Develop Systems & Control: dynamical inputs, outputs, controllability/observability, identification, forcing design, objective metrics, estimation and optimization with boundaries clear.
- [ ] Add supportive foundations or plausible extensions when there is a traceable connection to proposal; distinguish core from future/exploratory.
- [ ] Derive/interpret equations with definitions/units. Flag scientific uncertainty; cite exact original source or explicit derivation assumptions.
- [ ] Avoid presenting predicted periodic-selectivity advantages, microscopic dynamic rate constants or observability as verified without the relevant evidence.

**Checkpoint:** all three disciplines have **substantive developed content**, with more than a placeholder second layer; each topic's scientific significance and provenance can be inspected. There is no hard node quota or maximum tree depth.

## Phase 3 — Independent baseline freeze

- [ ] Validate YAML syntax, IDs/parents, links, cycles, status ceiling, sources/evidence locators.
- [ ] Compare committed data to the source materials for unsubstantiated scientific claims and conflicting assumptions.
- [ ] Clearly state coverage and unresolved gaps in `progress.md`; provide a source and uncertainty ledger.
- [ ] Commit the independently derived `nodes.yaml` and support files, verify remote readback and record **baseline v1 commit SHA**.
- [ ] Open a PR **into the experimental base branch**, no auto-merge. Keep its original independent baseline identifiable for later comparison.

**Stop here for the user's review.** Later source enrichment or comparison will be separate, explicitly labeled work; do not silently fold them into the original v1 frozen baseline.

## Quality and reporting

Deliver a compact but useful report explaining the scientific classification, strongest evidence-backed branches, key unresolved hypotheses, coverage/limitations, changed files, executed tests, Git commits and exact PR base/head. If stopped before Phase 3, say exactly where and why, commit only validated partial work, and do not claim the baseline complete.

**Git workflow:** small logical commits; inspect diff; push/fetch remote verification; no force-push; preserve independent commits at integration if individually reversible changes matter. Work in the cloud, no local PC dependency.
