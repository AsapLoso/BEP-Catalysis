# Wayfinder: BEP — Select an existing scientific modelling approach

> **BEP-onderzoeksscope (19–21 oktober 2026; geen validatieclaim):** De gekozen verkenningsreferentie is een radiaal niet-uniforme pellet, zonder externe filmweerstand en met eindige interne diffusie. De genoemde 5–30 ms is een schatting, geen kalibratie. De eerste vergelijking is invariantie bij gematchte \(R_p^2/D_{eff}\)-paren; een lognormale pelletverdeling is een latere hypothese. Outlet-observeerbaarheid/modelreductie is een afzonderlijke vervolgvraag. De eerdere lognormale SEM-fit betreft YBCO en is geen katalysatorbron. De beoogde notebook is een onderzoeksdeliverable, geen goedgekeurde deckkeuze. Zie [radiale testvolgorde](../notes/2026_10_19_radial_observability_and_reduction.md), [herkomstcorrectie](../notes/2026_10_19_erratum_log_normal_ybco_sem_vs_bep_pellets.md), [leesroute Berger §6](../notes/PRIORITY_reading_2008_s6_transport_vs_surface_memory_2026_10_19.md) en [notebook-wayfinder](bep_reactor_notebook_delivery_2026_10_19.md).
>
> De 240-state uniforme-pellet-PSSA is alleen een diagnostische baseline, niet het doelmodel met gekoppelde bulk-, porie- en dynamische oppervlaktegeheugens. De onafhankelijke auditreceipt bestaat maar is **INCOMPLETE**. `Methanol-Catalysis/main/pbr/` is publiek aanwezig (inhoud gecontroleerd op 21 oktober); er zijn in dit PR geen nieuwe modelcodewijzigingen, simulaties, testruns of Actions uitgevoerd. K is deels besproken; L/M en deckkeuzes blijven open. Zie [gebruikersnotitie](../notes/user_thought_dump_2026_10_18_reactor_recovery.md), [herstelregister](../dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md) en [auditreceipt](../dossiers/reactor_recovery_2026_10_18/independent_audit_receipt.md).
Construction date: 2026-10-13, Europe/Berlin. Mode: Map Construction and Audit. Source snapshot: `devcontainer` at `7e5aeccac2758f396c33b2398e34d2e1304d04c0`. This is an evidence-backed decision map; open selections remain open.

## 1. Destination

The owner and supervisors can select a credible, reusable mathematical model and numerical approach for spatially resolved, transient acetylene semi-hydrogenation under periodic inlet concentration forcing. The selection must identify the published equations, compatible kinetic evidence, existing software to reuse, required corrections or adaptations, and the evidence needed to trust predictions within the agreed bachelor scope.

The destination is scientific method selection. It is distinct from the thesis-wide destination in [the master map](https://github.com/AsapLoso/project-management-agents/blob/7e5aeccac2758f396c33b2398e34d2e1304d04c0/Academics/BEP/Catalysis/research/wayfinder/bep_catalysis_master.md), the earlier [Damian briefing](https://github.com/AsapLoso/project-management-agents/blob/7e5aeccac2758f396c33b2398e34d2e1304d04c0/Academics/BEP/Catalysis/research/wayfinder/damian_briefing_2026_10_09.md), and the Wednesday presentation destination. See [scope and provenance](../dossiers/scientific_wayfinder_2026_10_13/scope_provenance.md) for the map-overlap check, including local-only maps. This map does not replace those maps or their owners' decisions.

Completion requires an explicit selection, traceable source coverage, a justified verification standard, and live resolution of the relevant human gates. Constructing and auditing this map does not satisfy that completion criterion.

**Runbooks:**

- [Extraction verification](https://github.com/AsapLoso/project-management-agents/blob/7e5aeccac2758f396c33b2398e34d2e1304d04c0/.agents/resources/runbooks/verifying-extraction-claims-against-pdf-text-layer.md).
- [Partial reads and inference discipline](https://github.com/AsapLoso/project-management-agents/blob/7e5aeccac2758f396c33b2398e34d2e1304d04c0/.agents/resources/runbooks/partial-grep-and-inference-discipline.md).
- [Preflight verification](https://github.com/AsapLoso/project-management-agents/blob/7e5aeccac2758f396c33b2398e34d2e1304d04c0/.agents/resources/runbooks/preflight-verification-before-automated-runs.md).

Gap: the runbook inventory contains no dedicated BEP reactive-transport conservation, convergence, or parameter-transfer validation procedure. The existing harness and presentation procedures do not supply that scientific validation. No runbook or infrastructure changes are authorized by this mission.

## 2. Decisions So Far

- [x] **[DECISION: user scope, 2026-10-13] Reuse established science.** The [work mission](../dossiers/scientific_wayfinder_2026_10_13/raw/work_mission_2026_10_13.md) authorizes reconnaissance and map construction for physics-first prediction and periodic forcing; it excludes inventing nonlinear control theory and implementing a full MPC programme. Solver, proposal, and state-engine edits are excluded.
- [x] **[FACT: proposal and later records] Scope has layers.** The written proposal contains a forward model, calibration, waveform optimization, and experimental validation, while reserving observers and MPC for later research. Later conventions record literature-forward modelling with optional fitting and a specific MOL/upwind/central/BDF baseline. These records do not prove supervisor approval of a revised deliverable package. See [the authority comparison](../dossiers/scientific_wayfinder_2026_10_13/scope_provenance.md).
- [x] **[FACT: primary literature] Berger provides a reusable starting framework.** Figure 5 is a pseudo-homogeneous axial gas balance coupled to dynamic surface coverages. Its worked example uses spatial finite differences, MOL, and implicit BDF. It does not itself supply the resolved radial-pellet extension in this code or a complete acetylene parameter set. See [primary-paper coverage](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md).
- [x] **[FACT: search] Direct acetylene literature comes before the wind-control analogy.** Urmès et al. (2022), DOI [10.1002/cctc.202101826](https://doi.org/10.1002/cctc.202101826), directly studies microkinetic acetylene hydrogenation under periodic reactor operation. Its existence and reported scope are verified; inaccessible full equations, supplements, and software remain gaps. Other directly relevant models and theses are compared in [literature reuse](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md).
- [x] **[FACT: code and bounded diagnostics] The pinned older script is a scaffold.** It stores 1,480 components, uses BDF, and has zero default kinetic constants, a fixed inlet, an RHS that mutates boundary entries, and an incorrect radial-centre coefficient. No validated reacting periodic simulation has been established by this reconnaissance. See [simulator evidence](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md).
- [x] **[FACT: local implementation] A newer implementation is a reuse candidate.** The local sibling `pbr` package adds modular transport, rate laws, callable forcing, and a sparse implicit interface. Its optional surface coverages do not feed back into gas rates, and source checks identify numerical/closure problems. This is a more developed candidate, not evidence that the proposed transient microkinetic predictor is already validated. See [the alternate-implementation addendum](../dossiers/scientific_wayfinder_2026_10_13/alternate_implementation.md). SM-3 must assess this candidate rather than assume the older script is the only code.
- [x] **[FACT: corrections] Existing audit statements need selective correction.** Ethylene readsorption is implemented; zero chemistry does not imply zero transport; the particle-average error is quadrature bias rather than a missing spherical geometric factor; the two site-capacity factors are not a double normalization. The bulk/pore inventory closure also needs an explicit physical interpretation. Evidence and limits are in [the numerical report](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md). None of these findings silently closes a human ticket in another map.
- [x] **[FACT: representation] Time indexes the state trajectory.** After spatial discretization, `x(t)` is an instantaneous vector of concentrations and surface coverages at the retained spatial locations; time is not an extra state component. A matrix of time samples is a trajectory data array. Actual independent state count depends on boundary elimination and physical closure, not simply the script's allocated count. See [numerical representation](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md).
- [x] **[FACT: theorem scope] Willems is a conditional reuse result.** The 2005 trajectory-spanning result requires the stated linear-system and excitation assumptions; it does not make nonlinear reactive-transport trajectories exactly representable by a generic Hankel matrix. Wind-group software supplies modelling and validation examples, not reactor physics or BEP controller requirements. See [the transfer assessment](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md).
- [x] **[FACT: provenance] Recorded context is incomplete.** Archived source text is preserved separately from interpretation. The October 12 handoff is explicitly a reconstruction, and the uploaded wind-control slides are not established as accessible source material in this mission. Missing original conversation material remains named in [scope provenance](../dossiers/scientific_wayfinder_2026_10_13/scope_provenance.md).

## 3. Active Frontier

These are precise decision questions now. Dependencies indicate when evidence is sufficient to resolve them; a precise question awaiting evidence remains a ticket, not fog. Research tickets are AFK; grilling tickets require live human exchange. No ticket below is resolved by a recommendation in the dossier.

**Crosswalk-stand 2026-10-18.** Alle negen frontier-tickets (SM-1…SM-9) zijn `research`, `conditional` of gedeferd `requires user decision`; géén wordt nu scanner-actief. De state-link blijft gedeferd (zoals §6 al vastlegt); classificatie per ticket: [map_state_crosswalk_2026_10_18.md](../notes/map_state_crosswalk_2026_10_18.md).

### Island: Published mechanism and evidence

- [ ] **SM-1 — Acetylene mechanism transfer** (`wayfinder:research`) — *Question: Which equations and parameters from the directly relevant periodic acetylene models can be reused for the intended catalyst, feed, temperature, and operating range, and which require new evidence or recalibration?*
  - Status: Open. Dependencies: None; source access gaps are explicitly recorded.
  - Decision enabled: a compatible mechanism shortlist, with unit conventions and transfer limits.
  - Evidence: [literature reuse](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md). Papers lead; a thesis appendix is a bounded implementation or parameter check, never a gate on the whole literature search.

- [ ] **SM-2 — What predictions can the available evidence support** (`wayfinder:research`) — *Question: Which published or project-owned steady and transient observations can distinguish the candidate mechanisms and constrain their parameters, and which internal coverage predictions would remain unidentifiable from those observations?*
  - Status: Open. Dependencies: None for evidence inventory; discrimination depends on SM-1.
  - Decision enabled: literature-forward demonstration versus a justified calibration claim, and limits on hidden-state interpretation.
  - Evidence: [literature limitations](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md), [proposal versus later conventions](../dossiers/scientific_wayfinder_2026_10_13/scope_provenance.md). Synthetic trajectories cannot independently validate their generating physics.

### Island: Existing software and transport closure

- [ ] **SM-3 — Reusable implementation evidence** (`wayfinder:research`) — *Question: Among the identified paper supplements, thesis implementations, repository scripts, and research software, which obtainable implementation actually includes the required transient gas and surface dynamics, and what verified adaptation would each candidate require?*
  - Status: **Advanced 2026-10-13** — the two local candidates were executed against, not merely read. Not closed: scientific compatibility still depends on SM-1.
  - Dependencies: None for retrieval and inspection; scientific compatibility depends on SM-1.
  - Decision enabled: reuse a complete implementation, reuse components, or retain and correct the present scaffold.
  - Evidence: [newer local package inspection](../dossiers/scientific_wayfinder_2026_10_13/alternate_implementation.md), bounded search logs in [software and numerical methods](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md) and [literature reuse](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md). A model described in a paper is not automatically downloadable or verified code.
  - **Evidence update 2026-10-13 (executed, not read):** `pixi run python 3_Model/probes/verify_pbr_implementation.py` → 3/4 gates, exit 1 (GATE 1 fails: coverages 11/12).
    - **The decisive finding is negative, and now it is executable rather than static.** `pbr`'s `Model.rhs` (`pbr/solver.py:274-341`) computes gas rates from partial pressures and temperature and *separately* evaluates a coverage relaxation target; **neither call accepts `theta`**, so the evolving surface cannot feed back into gas chemistry. `pbr` is therefore a **PSSA/steady-state rate model with optional auxiliary relaxation states**, not the proposal's coupled transient adsorbate kinetics. Its own `Relaxation` docstring says the time constant is assumed, not microkinetically derived (`pbr/closures.py:352-386`).
    - **Three further defects reproduced by execution, not inference:**
      - relaxation target shape mismatch → `ValueError: operands could not be broadcast together with shapes (20,3) (20,10,3)` (carried `theta` is `(N_z,N_r,3)`; the target is `(N_z,3)`).
      - sparsity mask wrong size → `Model.sparsity` shape `(294, 294)` against a state of `(234, 234)`; `n_radial_effective` is passed into `jacobian_sparsity`'s `n_surface` slot while `Layout` uses three coverages.
      - feed conversion contradicts the source → `OperatingPoint.concentrations()` divides by the reacting mole fraction, inflating every reactive partial pressure by `1/0.753 = 1.328`. The source's own published partial pressures confirm `y_i·P_total` (its stated p_H2 = 5.5 kPa matches to 1.5 %, against 31 % for `pbr`'s path). Invisible to all 37 passing tests.
    - **Counterweight, also new:** the package's Urmès2019 parameter set **verifies against the primary source** (24/24, `verify_urmes2019_source.py`) and its rate law **reproduces the paper's published coverages at 11 of 12 checks** — missing $\theta_{H_2}$ at the highest-acetylene feed by 9.5 % of the way to the published bound. Its test suite **passes, 37 tests** ([`evidence/pbr_pytest_2026_10_13.txt`](../briefing/evidence/pbr_pytest_2026_10_13.txt)).
    - **Net for the reuse decision:** `pbr` is architecturally ahead and its chemistry is now source-verified, but the single change that would make it the proposal's model — letting `rate.rates` consume `theta` — has not been made. Selecting or repairing it remains a human decision (see SM-8). Receipt: `3_Model/probes/pbr_implementation_receipt.json`.

- [ ] **SM-4 — A coherent conservation model** (`wayfinder:research`) — *Question: Which established bulk, pore, surface, and boundary balances consistently represent the retained inventories, and does the current volume-averaged reaction closure conserve them under its stated assumptions?*
  - Status: **Advanced 2026-10-13** — the closure question is now stated as an explicit, falsifiable identity rather than a suspicion. Not closed: the choice of closure is a human decision.
  - Dependencies: None for balance reconciliation; experimental reduction evidence comes from SM-2.
  - Decision enabled: an explicit statement of the physical model being selected, with defects separated from deliberate reductions.
  - Evidence: Berger Figure 5 in [literature reuse](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md); the static pore-filling diagnostic and boundary-state findings in [simulator evidence](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md).
  - Authority: human selection of governing equation, film closure, and plug-flow/dispersion remains in master `I1-04`, `I1-06`, and `I1-09`; this research supplies evidence to those gates.
  - **Evidence update 2026-10-13:** the closure defect is written down as a checkable identity in [`BEP_SUPERVISOR_BRIEFING_2026-10-13.md`](../briefing/BEP_SUPERVISOR_BRIEFING_2026-10-13.md) §6.1. Integrating the pore balance over a spherical pellet gives `ε_p·d⟨c_p⟩/dt = (3/R_p)·J_in + ρ_s·C_t·⟨R_gas⟩`, so the bulk exchange should be `(1−ε_b)/ε_b·(ρ_s·C_t·⟨R_gas⟩ − ε_p·d⟨c_p⟩/dt)`. **The code keeps the first term and drops the pore-storage term.** A zero-reaction diagnostic makes it concrete: with the bulk set uniformly to the inlet and the pellet interior empty, every bulk derivative is zero while the interior pore derivative is positive (H₂: 457.2 mol m⁻³ s⁻¹) — pore inventory fills without bulk uptake.
  - **Explicitly not resolved by fixing D1:** the boundary-mutation defect and this physics question are independent. `pbr`'s bulk-average-versus-pore-storage accounting remains equally open ([`simulator_numerics.md`](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md):115), and its `atom_balance` helper ignores pore inventory and physical volume/site weights, so it is not full reactor mass accounting.

### Island: Credible prediction and computation

- [ ] **SM-5 — Prediction acceptance target** (`wayfinder:grilling`) — *Question: Which measured outputs, operating range, and acceptable prediction errors must the selected model reproduce before it is called a credible BEP predictor?*
  - Status: Open. Dependencies: SM-2 for available evidence; the question can be discussed now.
  - Required authority: owner and supervisors. No numerical tolerance, runtime target, or hidden-state accuracy is inferred.
  - Relationship: complements master `I1-07`, which governs reporting with defects; it does not replace or answer that gate.

- [ ] **SM-6 — Reusable verification evidence** (`wayfinder:research`) — *Question: Which analytic limits, conservation and positivity checks, mesh and time convergence comparisons, and published transient benchmarks can discriminate acceptable from misleading predictions for the selected balance and mechanism?*
  - Status: Open. Dependencies: None for benchmark inventory; applying the acceptance target depends on SM-1, SM-4, and SM-5.
  - Decision enabled: a finite, falsifiable verification corpus rather than solver-success messages or plausible plots.
  - Evidence: [static diagnostics and their limits](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md). Historic trajectory differences need matched output times; hardware-specific seconds are not a scientific benchmark.

- [ ] **SM-7 — Is the existing implicit route computationally sufficient** (`wayfinder:research`) — *Question: With a source-supported mechanism and coherent state definition, does a Jacobian-aware BDF or Radau implementation meet the agreed accuracy and cost targets, or does evidence justify evaluating an established IMEX scheme?*
  - Status: Open; benchmark resolution awaits prerequisites. Dependencies: SM-1, SM-4, SM-5, SM-6.
  - Decision enabled: evidence for retaining the recorded implicit baseline or a justified later method comparison. No solver change is authorized here.
  - Evidence: [Jacobian structure, solver APIs, and IMEX limits](../dossiers/scientific_wayfinder_2026_10_13/simulator_numerics.md). Spatial upwinding and downstream causality do not determine explicit versus implicit time integration. Chemistry and diffusion stiffness must be considered together.

### Island: Scientific selection

- [ ] **SM-9 — Define a fair optional optimization comparison** (`wayfinder:grilling`) — *Question: If open-loop yield optimization is retained by the scope gate, which cycle-averaged performance metric and equal-feed steady reference will define an improvement?*
  - Status: Open, conditional on the inherited scope decision. Dependencies: SM-2 and master `I4-04`.
  - Required authority: owner and supervisors. Yield, selectivity, conversion, and production rate are not interchangeable; unequal average feed or throughput can make a comparison misleading.
  - Decision enabled: a bounded optimization objective. Actuator bounds remain evidence to establish from actual hardware; waveform algorithms are not selected by this ticket.

- [ ] **SM-8 — Select the reusable methodology package** (`wayfinder:grilling`) — *Question: Which documented combination of published mechanism, transport closure, reusable implementation, and verification standard will the owner and supervisors adopt for the current BEP, with what bounded optional extensions?*
  - Status: Open. Dependencies: SM-1 through SM-7 and the inherited human gates below; SM-9 only if optimization is retained.
  - Required authority: live owner/supervisor selection. The dossier compares choices; it does not ratify them.
  - External gates remain owned by the master map: `I1-04` bulk governing equation; `I1-05` TPD/readsorption scope; `I1-06` film closure; `I1-07` reporting correctness; `I1-08` parameter sourcing; `I1-09` transport reduction; `I4-04` S&C deliverable scope. Appendix research tickets `I1-01`/`I1-02` receive bounded evidence and are not imposed as global prerequisites.

## 4. Not Yet Specified (The Fog of War)

### Island: Reduced prediction

- A useful MOR target cannot yet be specified: the operating envelope, outputs, accuracy target, and remaining computational bottleneck after ordinary sparse implicit methods are not established. POD, balanced reduction, and surrogates are candidate families, not selected projects.
- Multiple local linearizations remain an exploratory idea. Reference operating states, admissible excursions, switching/interpolation rules, and required validity region cannot yet be formulated for this model. The general local-linearization concept is known; the project-specific approximation problem is not.
- Simulation-based identification needs a defined reliable generating model and input/output dataset before a meaningful reduced-predictor question can be formulated. The assumptions of Willems' LTI result are already known and therefore are not placed in fog as an unanswered theorem question.

### Island: Periodic operation beyond the baseline

- Unanticipated periodic operating regimes and their scientific follow-up questions have not yet been identified by a trustworthy transient model. They may emerge from later evidence. Known questions about optimization scope and comparison metrics are already precise and remain in master `I4-04` and SM-9; they are not fog. The proposal's B-spline language and square-wave claims do not ratify an algorithm in this mission.
- Whether thermal dynamics materially change the selected transient experiment cannot yet be specified without the actual catalyst and operating window. An energy-balance extension remains conditional, not silently required or permanently excluded.
- A new detailed mechanism beyond the established candidates is not planned. Mechanism inadequacy might reveal a new research question; no speculative reaction network is dispatched into that fog.

## 5. Out of Scope

- Inventing new nonlinear control theory, a full MPC/DeePC/SPC programme, controller synthesis, or state-observer implementation.
- Treating wind-wake dynamics as equivalent reactor physics, or simulation-trained predictors as independent experimental validation.
- Changing the solver, kinetic parameters, proposal, `state.md`, `conventions.md`, `history.log`, or task engine.
- Choosing the Wednesday presentation's audience, duration, story, format, or visual design; these remain presentation-map HITL decisions.
- Thesis publishing infrastructure, committee administration, service deployment, or a new orchestration architecture.
- Declaring this destination complete while human selection, source gaps, or verification requirements remain unresolved.

## 6. Provenance and audit

Read [the dossier index and proposal/code/literature comparison](../dossiers/scientific_wayfinder_2026_10_13/README.md), [Wednesday handoff](../dossiers/scientific_wayfinder_2026_10_13/wednesday_handoff.md), [parser receipt](../dossiers/scientific_wayfinder_2026_10_13/parser_receipt.json), and [independent coverage audit](../dossiers/scientific_wayfinder_2026_10_13/source_coverage_audit.md).

The real repository parser assigns internal `WF-N` identifiers and does not parse dependency edges or enforce HITL authority. Visible `SM-N` identifiers and those governance checks are therefore independently audited. This construction is not compiled into an execution contract; no engine is authorized to resolve its grilling tickets autonomously. The state-file link prescribed by the skill is deferred because the user expressly prohibited state-engine edits.



## Cross-linked maps

- [Wednesday presentation Wayfinder — 14 October 2026](bep_presentation_2026_10_14.md) — near-term presentation readiness, separate from scientific method selection.
- [Thesis-wide BEP master map](bep_catalysis_master.md)
- [BEP Catalysis navigation hub](../../README.md) · [Master document map](../../DOCUMENT_MAP.md)
