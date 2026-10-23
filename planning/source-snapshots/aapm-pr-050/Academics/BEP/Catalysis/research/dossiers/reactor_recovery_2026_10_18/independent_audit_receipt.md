# Independent audit receipt — BEP reactor recovery

**Audit date:** 2026-10-21 (Europe/Berlin)  
**Verdict:** **INCOMPLETE**  
**Review target:** [PR #50](https://github.com/AsapLoso/project-management-agents/pull/50), head `e58d804bb365806b1676b9b4de02f1466b77d118`, based on `devcontainer` at `bb705c0dadb9813044654ab5f2ef1f7f84348173` when reviewed.  
**Reviewer:** Codex, sync executor for this task. I did not author the PR’s research files during this task. I reviewed related BEP synchronization work in this conversation, so this is a non-author review with limited independence, not a second human or clean-room review.

## Why the verdict is incomplete

The original visible 18 October user turn is not available in this task. The available [thought-dump note](../../notes/user_thought_dump_2026_10_18_reactor_recovery.md) labels itself a manual, transcript-near reconstruction and explicitly disclaims verbatim accuracy. I therefore cannot certify a word-by-word audit, count omitted original utterances, or call the audit complete.

I reviewed all 47 register IDs against that note and the linked evidence. The register itself still marks U01–U47 open. This audit did not run code, tests, simulations, or GitHub Actions; it does not approve presentation decisions or close scientific questions. The 2022 supporting-information file was inaccessible in the prior source review, so its detailed mechanism and parameter values remain unverified. K remains partly discussed; L and M remain unevaluated.

### Counts

- **47/47** register IDs found and checked against the available transcript-near note.
- **47/47** IDs remain open in the source register; **0/47** can be marked complete for the intended scientific/notebook outcome on the evidence reviewed here.
- **0/47** can be certified as exact-original wording coverage; the original message is unavailable. The number of missing or merged original utterances is therefore **unknown**, not zero.
- **4** cross-document redlines are required: the 11/13 layout description (U09), the meaning of dynamic surface states (U14), the 10/12 coverage result (U18), and stale “pbr absent” claims (U35/B3).
- No tests, simulations, or Actions were run for this receipt.

## Evidence-backed findings

### 1. The public `pbr/` package exists now; the missing-package statement is historical

A live remote-ref check returned `AsapLoso/Methanol-Catalysis/main` at `5400881b3d06164db10488abae27b110ac618258`. Its tree contains eleven `pbr/` modules, `tests/test_solver.py`, `tests/test_discretisation.py`, and only `.github/workflows/deploy.yml` plus `deploylatex.yml`. The package is published; that proves neither a scientific CI run nor a working notebook.

The PR’s 18 October “pbr absent” observation can remain as dated history. The active register statements in §0 and B3 must say that the package is present now and that scientific Actions are absent. The 19 October correction already records this in the project state.

### 2. “11 or 13” counts fields, not solver entries; 13 is not the actual Hermes layout

The legacy scaffold has four bulk gas fields, four pore gas fields, and three adsorbate coverages: eleven field types. Its historical 20 × 10 grid allocates 1,480 entries, including boundary entries that are constrained or have zero derivatives; 1,480 is not 1,480 independent physical states.

The **13-field** count is only the hypothetical combination 4 bulk + 4 pore + 5 coverages. The inspected Hermes five-coverage branch actually stores four bulk gas fields plus five coverages and has no radial pore-gas field in that branch (nine field types). Its separate radial branch uses four bulk plus four pore-gas fields. In the current Methanol-Catalysis package, the layout has four reactive gases, optional radial pore-gas states, and optional three coverage states; its catalogued Urmes2019 configuration enables radial diffusion but selects algebraic surface equilibrium. Argon is an inert feed component and is not a gas state in these layouts. Do not treat time samples, inputs, or run parameters as states.

### 3. Urmès 2019 source conditions are not reproduced by one unambiguous configuration

The primary [Urmès et al. 2019 paper](https://doi.org/10.3390/catal9020180) reports a 0.05 wt.% Pd/α-Al₂O₃ catalyst, 0.1 g catalyst plus 0.5 g α-Al₂O₃ diluent, a 4 mm tube, 200 mL/min total flow, 1.26 bar, and 51/62 °C. Its standard condition 1 gives whole-stream fractions 1.0% C₂H₂, 4.3% H₂, 70% C₂H₄, and 24.7% Ar. At 1.26 bar these imply 1,260 Pa C₂H₂ and 5,418 Pa H₂. The separate 62 °C Figure 7 caption gives 950 Pa C₂H₂ and 5,500 Pa H₂; those are not the same acetylene point. The code must name which paper condition it reproduces rather than compare these values as one case.

The current package’s `urmes_geometry()` labels its diameter as the source diameter but sets 5 mm, and uses 75 mg catalyst with no 0.5 g diluent. Those are not the source’s 4 mm / 0.1 g + 0.5 g benchmark geometry. The package’s parameter docs partly label these as assumptions, but the code comment and benchmark naming need correction before claiming a source-matched case.

There is a separate current-code feed issue. `OperatingPoint.concentrations()` computes `P / reacting_mole_fraction` when Ar is present. For the documented whole-stream composition, the reactive fraction is 0.753, so the package yields approximately 1,673 Pa C₂H₂ and 7,195 Pa H₂ instead of 1,260 Pa and 5,418 Pa at condition 1. The composition documentation says these are whole-stream mole fractions and pressure is total pressure; the rescaling removes the inert pressure and conflicts with that definition. This needs a corrected feed basis or an explicitly different, fully documented pressure convention before the Urmès benchmark is accepted.

### 4. The 10/12 coverage check is not explained by being outside the temperature or pressure range

The preserved `pbr_implementation_receipt.json` checks four declared operating cases at 324.15 K and/or 335.15 K and 126,000 Pa, and compares three coverages for each case. Ten comparisons are inside the quoted coverage ranges. The two failures are both H₂ coverage for standard feed condition 1, at 51 °C and 62 °C: `0.0018053364` versus the quoted lower bound `0.002`. The other two operating cases pass all three coverage comparisons.

Those two rows are not outside the paper’s 51–62 °C or 1.26 bar conditions. The receipt does not establish that they are outside the source’s valid operating domain. Keep the result **10/12** and investigate whether rounding, the precise measured rows, or the coverage-range interpretation explains the small shortfall. Do not relabel it as 10/10 or exclude those points without primary-source evidence and a criterion chosen in advance. Also keep this older receipt distinct from current public-main code, whose inert rescaling changes its evaluated partial pressures.

### 5. The current optional “surface dynamics” does not couple surface state back into gas rates

In the current public package, `Model.rhs` calls the gas rate law with local gas partial pressures and temperature. If coverage states are carried, it separately computes a target coverage and advances `dtheta/dt = (theta_target - theta)/tau`. The gas-rate call does not receive `theta`. The `Relaxation` closure itself calls this a phenomenological extension with an assumed, unsourced `tau`; it is not an elementary-step microkinetic model.

The [Urmès et al. 2022 article](https://doi.org/10.1002/cctc.202101826) supports a dynamic single-site microkinetic study under small-amplitude flow oscillations and names controlling steps. The detailed SI/equations/parameter availability was not verified here. Do not equate the current relaxation trace with the published 2022 mechanism, or claim that coverage memory affects the gas outlet.

### 6. Radial/pore conservation remains a blocking question; the existing source-factor check is insufficient

The current package declares separate transient bulk and pore-gas balances. Its RHS adds the volume-averaged chemical rate to the bulk equation and also includes the chemical rate in the radial pore equation. With transient pore storage, integrating the pore balance gives reaction plus pore accumulation balanced by shell flux; the shell flux is not instantaneously identical to the volume-averaged reaction. The inspected bulk RHS does not show the equal-and-opposite shell-exchange term. Under the documented interpretation of distinct bulk and pore inventories, this is a likely conservation defect or a model-equation mismatch. It must remain a **blocking hypothesis** until the state basis and full global inventory equation are reconciled.

The existing code documentation’s equality of source prefactors establishes a unit conversion, not the full transient bulk + pore inventory balance. No end-to-end conservation test or radial transient run was performed in this audit. The user-selected exploratory boundary condition—no external film, (c_p(R_p)=C_b), finite internal radial diffusion—is a model assumption, not measured evidence.

### 7. Numerical claims checked statically

- The Hermes receipt reports the steady baseline (X_{C2H2}) change from 0.093092 at 30 axial cells to 0.093028 at 120 cells (0.0687%). That is a steady conversion refinement check, not a transient waveform or periodic-convergence result.
- The same receipt compares only 40 bulk columns for one assembled Jacobian check. It does not establish correctness of all columns or a radial/surface Jacobian.
- For a pure-advection semi-discrete first-order-upwind chain, one cell has transfer ( (1+iomegaDelta z/v)^{-1}), hence (H=(1+iomega	au_{res}/N)^{-N}). At the recorded residence-frequency (fapprox84.2) Hz, (omega	au_{res}approx2pi), and (N=60), (|H|=[1+(2pi/60)^2]^{-30}approx0.721): about **27.9% amplitude loss**. It persists as (Delta t	o0) for this semi-discrete spatial operator. Forward Euler at CFL=1 is a distinct pure-advection exception: the grid solution shifts one cell without damping. Reaction, diffusion, forcing timing, and stiffness can remove that special case.
- The sensitivity-figure error follows directly from its algebra. The saved baseline is (	au_{p0}=1.166104) ms, (epsilon_p=0.5), (R_0=75,mu m), and baseline tortuosity 3. The plotting code computes (k=	au_{p0}/(epsilon_pR_0^2)) then (	au_{plot}=	au_{tort}R^2k). At the baseline radius and tortuosity this gives (6	au_{p0}=6.9966) ms, while the receipt reports 1.1661 ms. This is static code/algebra evidence; it was not rerun.
- The frequency-response script passes the full two-dimensional SciPy `sol.y` array (states × times) to `bulk_outlet`, whose helper reshapes a single state vector to `(n_axial,4)`. For more than one saved time, the element counts are incompatible. This is a static shape proof, not an execution. Even after repair, taking max–min over the last 25% of adaptive solver output points is neither a set of complete cycles nor a phase/gain estimate.
- The prior 17/17 gate receipt establishes only its selected gates on its recorded baseline. Its “periodic” gate compares terminal periodic and constant-feed snapshots; it does not establish (x(t+T)) convergence, last-cycle means, phase, harmonic content, or periodic yield.
- Current public-main tree has two test files and no scientific PBR workflow. Tests were not run.

The 2008 Berger citation is bibliographically identifiable as *Dynamic methods for catalytic kinetics* (DOI [10.1016/j.apcata.2008.03.020](https://doi.org/10.1016/j.apcata.2008.03.020)); the full paper’s cited equations were not independently reopened here, so equation-level transferability remains **NOT VERIFIED**.

## Traceability crosswalk: U01–U47

The paragraph numbers below refer to the quoted paragraphs in the transcript-near note, not to the inaccessible original chat. “Open” means represented in the register but not substantively completed by this audit.

| ID | Note paragraph(s) | Audit disposition |
|---|---:|---|
| U01 | 1 | Research ownership and the non-presentation priority are represented; owner-level scientific understanding remains open. |
| U02 | 1, 9, 20 | Earlier E/F/G material exists, but why it did not gate the selected default is not proven; workflow diagnosis remains a hypothesis. |
| U03 | 2 | Metric definitions are documented; receipts were not independently recalculated end-to-end. |
| U04 | 2, 13 | Per-species full response and cycle observables remain unimplemented/unverified. |
| U05 | 2 | Linear sinusoidal response versus nonlinear harmonics/DC shift is the right distinction; no response waveform was measured here. |
| U06 | 13 | Settling criterion and complete-cycle convergence remain open; no (x(t+T)) check is evidenced. |
| U07 | 2, 13 | A cycle mean may answer yield; fit/harmonics are separate gain/phase questions. No implementation is evidenced. |
| U08 | 3, 7 | Residence time is a useful axis; flow basis and the feed pressure conversion must first be fixed. |
| U09 | 7 | Correct the 13-field claim as described above; 11 and 13 are field-type hypotheses, not vector sizes. |
| U10 | 7 | State/configuration/input distinction is conceptually sound; exact config table remains open. |
| U11 | 7 | Composition DOE is open; require simplex closure, inert balance, H₂ budget, and fixed flow/pressure basis. |
| U12 | 4, 10, 18 | Current public package has radial states; default physics and validated scope are not equivalent to the user’s complete target. |
| U13 | 10 | “Turn radial on” is not an acceptance test; coupled conservation is still a blocker. |
| U14 | 15 | Current relaxation is not source-derived microkinetics and does not feed back into gas rates; 2022 SI/equations remain unverified. |
| U15 | 15 | 2022 was published in 2022 (2021 was its submission year); Berger equation-level application remains unverified. |
| U16 | 5 | 66–86 °C is not the verified 2019 measurement window; source conditions are 51/62 °C. Plot axes were not rebuilt. |
| U17 | 5 | Negative net selectivity can follow the stated net definition; no defect claim is made without feed/stoichiometric checks. |
| U18 | 6 | Keep 10/12. The two H₂ comparisons are 0.001805 at condition 1 and 51/62 °C; they are not shown to be outside source T/P. |
| U19 | 6 | Broad LHS/grid remains deferred until admissible ranges and feasibility filters are source-grounded. |
| U20 | 7 | Pressure/flow/residence plots require fixed volumetric or molar-flow basis; current inert rescaling is a blocker. |
| U21 | 8 | Pressure enters LHHW partial-pressure terms; the current package’s partial-pressure conversion prevents a trusted trend claim. |
| U22 | 8 | Exponential simplification remains an idea, not new physical evidence. |
| U23 | 16 | The source benchmark and the current 5 mm/75 mg package geometry differ; reconcile before comparing. |
| U24 | 11 | Existing tests cover selected code properties; no current-main test run or broad physics gate was established here. |
| U25 | 11 | Finite/nonnegative outputs and solver success are distinct from stability and physical validity; broad checks remain open. |
| U26 | 11 | The recorded 30→120 comparison concerns steady (X) only; no transient tolerance/cost study was repeated. |
| U27 | 12 | Selected-column finite differences are partial evidence, not full Jacobian validation. |
| U28 | 13 | Complete-cycle settling/means remain unverified; the frequency script has a static shape mismatch. |
| U29 | 13 | Adaptive solver-point tails do not equal exact final cycles; no arbitrary 9-of-10-second window is accepted. |
| U30 | 14 | The semi-discrete attenuation and CFL=1 exception are distinguished; no new integration was run. |
| U31 | 13, 14 | Timeseries, phase, amplitude, harmonics, and net cycle yield remain open. |
| U32 | 18, 20 | The reduced baseline can answer limited forced-gas questions, but not validated radial/surface-memory yield. |
| U33 | 18 | Treat the reduced model as a diagnostic baseline, not a full research conclusion. |
| U34 | 16, 13 | Sensitivity plot is statically sixfold high at its baseline; frequency extraction is statically shape-incompatible. Neither fix was executed. |
| U35 | 4, 16 | Public (pbr/) now exists; the “absent” statement is historical. No scientific Action is present. |
| U36 | 4, 16 | Repository has deploy workflows only; scientific PBR CI remains future work after model gates. |
| U37 | 17 | The note correctly discloses that it is manual and non-verbatim; no exact transcript was recovered. |
| U38 | 17 | This receipt is a limited non-author audit, not the requested original-wording audit. |
| U39 | 9 | Kα–Kθ is a useful work breakdown; model/data/numerics dependencies still need a dependency graph. |
| U40 | 15 | A sourced explanation for supervisors remains a future artifact; no messages were sent. |
| U41 | 19 | Preserve the request for non-defensive technical discussion; this is not a scientific result. |
| U42 | 10, 18 | “One PDE” is a scoping analogy, not a literal equation count; model equation/state inventory is required. |
| U43 | 20 | Target observables, forcing domain, and accepted error have not been owner-finalized. |
| U44 | 10 | Radius/porosity/tortuosity must affect the actual physical model, not only postprocessed diagnostics. |
| U45 | 6, 16 | Split source reproduction, extrapolation stress, numerical sanity, and physically supported DOE; no range was silently narrowed. |
| U46 | 7, 20 | Publish exact layouts by configuration, including frozen/eliminated boundary entries and inert handling. |
| U47 | 1, 9 | E/F/G/J/K backward trace is partial; the exact original and full decision history were not independently available. |

## Five blocking issues

1. **Source-matched 2019 configuration:** fix whole-stream partial pressures and identify one exact source case; reconcile 4 mm/100 mg + diluent with the package’s 5 mm/75 mg assumptions.
2. **Bulk–pore conservation:** write the global inventory in declared concentration/density bases and demonstrate that interfacial transfer cancels and reaction is counted once, including transient pore storage.
3. **Dynamic surface model:** obtain the 2022 primary equations/data and make rates depend on the evolving coverage state; the current `Relaxation` closure is not sufficient.
4. **Periodic readout:** fix the state-matrix shape handling, then prove periodic settling and compute observables over complete cycles. The current terminal-snapshot gate is inadequate.
5. **Review and reproducibility gates:** correct the two static code findings, predefine the supported domain/error metric, then add a source-limited physics CI. No Action or test has been run in this audit.

## Smallest defensible implementation sequence

1. **Exact 2019 benchmark ticket.** Pin one named condition and source rows; assert feed fractions sum to one, (p_i=y_iP_{total}), matching total pressure/temperature/flow reference and catalyst/tube/diluent metadata. Acceptance: an independent calculation reproduces the declared input table and reports prediction-vs-source residuals without converting coverage-range failures into out-of-domain cases.
2. **Conservative radial gas ticket.** Use the user’s no-film boundary (c_p(R_p)=C_b) with finite internal diffusion. Acceptance: a derived global elemental/species inventory balances inlet, outlet, pore storage, and reaction over transient and steady runs; mesh refinement changes named observables within an owner-set tolerance.
3. **Dynamic-coverage ticket.** Retrieve the 2022 equations/parameters and experimental modulation conditions. Acceptance: rate expressions consume (	heta(t)); source constants and units are traced; elemental/site balances hold; a coverage perturbation changes the predicted rate. If SI/data remain unavailable, state the unsupported quantities and do not invent constants.
4. **Periodic-observable ticket.** Acceptance: successive complete cycles meet scaled state and output convergence criteria selected for the BEP; the last complete cycles report mean, and separately measured amplitude/phase/harmonics where needed; comparisons use a matched-mean steady case and report solver/grid sensitivity.
5. **Notebook ticket.** Begin after the preceding acceptance contract is concrete. Acceptance: a clean environment executes the notebook from a named configuration and reproduces its plots/receipts without claims beyond validated source and model limits.

No code, tests, integrations, notebooks, or Actions were run as part of this receipt.

## Required redlines to the source records

1. In the register’s §0 and B3, replace present-tense “remote main has no `pbr/`” with: “That was true at the 18 October check. Current main at `5400881b3d06164db10488abae27b110ac618258` contains `pbr/` and two test files; only deployment workflows are present, and no scientific run is proven.”
2. In U09, distinguish the hypothetical 4+4+5=13 combination from the actual Hermes five-coverage branch (4 bulk +5 coverages, no radial pore field).
3. In U14 and any model summary, distinguish the current assumed-(	au) relaxation trace from source-based 2022 microkinetics; state explicitly that the gas-rate path does not take (	heta).
4. In U18, retain 10/12 and identify the two H₂ comparisons as standard condition 1 at 51/62 °C. Do not classify them as out-of-domain without evidence.
5. Correct the current package’s “source diameter” comment or its 5 mm value; state clearly that its 75 mg/5 mm setup is not the cited 100 mg/4 mm + 0.5 g diluent experiment.

## Files and evidence examined

### PR #50 at reviewed head `e58d804bb365806b1676b9b4de02f1466b77d118`

- `INDEPENDENT_AUDIT_PROMPT.md` (blob `6ca389a9b92018d182b3f02c9b9891a864c9bd0b`)
- `decision_and_implementation_register.md` (blob `97814c993404f38b296871583eeeeff95d016c51`)
- `user_thought_dump_2026_10_18_reactor_recovery.md` (blob `c84e2ba5b53bd156591c60b7867ad7b32366878a`)
- `K_full_results_interpretation_2026-10-18.md` (blob `4d2bd4e375ae298018e2ba367ea2e9b887a3d326`)
- `K_results_validation_status_2026-10-14.md` (blob `7b4b96057ceae0b8c525b8722154637ebbf20183`)
- `E_operating_regime_transport_2026-10-14.md` (blob `fc106656375e04c167f134e9ce0b45f937b591ce`)
- `F_conservation_state_space_2026-10-14.md` (blob `cbeceb12992375133e1898496ad144d91aa0bb3d`)
- `G_numerical_methods_jacobian_feasibility_2026-10-14.md` (blob `068e966a0acb0744efab08057ddb8cad50c1b2cf`)
- `bep_dynamic_numerical_accuracy.md` (blob `64b38201733d102e49dc22223f193f38829e7cc5`)
- `source_coverage_audit.md` (blob `a3959c70455154e58f52832958fc594ca29472b5`), `pbr_implementation_receipt.json` (blob `cc3f1e05ef6f9b197a70b6e1d8d9a56f5e145fa2`), and `verify_pbr_implementation.py` (blob `b0f37bcc2e93d2ed1483dbfb901566e1731524e2`) on Hermes ref `hermes/reacting-vertical-slice-2026-10-13`
- `vertical_slice_reacting_reactor.py` (blob `db67605334ebcd0f2e6387b83e0ddefbf34c74c5`), `sensitivity_study.py` (blob `6ee83921d03c5d68306c4763001cc1bb8e9921a0`), `frequency_response.py` (blob `ba5e0b06b4fcc917e366cce29a6171011b163ccd`), and receipts `vertical_slice_receipt.json` (blob `bfd3a6a89cbb958d64640f9b34fca0ef25999bf1`) / `sensitivity_receipt.json` (blob `845bed41727518327be407ed3a098623d6b52a6c`).

### Current public `AsapLoso/Methanol-Catalysis/main`

- Ref `5400881b3d06164db10488abae27b110ac618258`; `pbr/parameters.py` blob `4bcc64bcefe366bce50f115734178b766ab40788`
- `pbr/parameter_sets.py` blob `fc5bdc88be1db105ed0d02e02edd26a6efcf1274`; `pbr/model.py` blob `1cbef7096ada01f1038cbc28e7265d8fa35a7b78`
- `pbr/solver.py` blob `99aa00b5592dbeb5c05a4fc87dcc2c4ff9a576e8`; `pbr/closures.py` blob `aa12b22a072fe0e6c93be72101f411b2c514c4ec`; `pbr/chemistry.py` blob `ebe23da668d64b5e44a837fc36f6fdc7fb0cf6ec`
- `pbr/species.py` blob `775e308e5e39cbc9be04240c7972d3f5b5877fbd`; `pbr/discretisation.py` blob `ea89f7c8d12302f9cef5a7df3999e22736eb4a96`
- `tests/test_solver.py` blob `c3ed5427b0a122539c70f04e09996c249484489d`; `tests/test_discretisation.py` is present in the live tree.

The primary 2019 paper was inspected via its publisher PDF. The 2022 article abstract was checked; full SI parameter/equation verification was not available. Berger’s bibliographic identity was checked; full equation-level review was not available.

## Pending owner/research decisions

- Original 18 October visible user message access, or an exact export, is needed to finish the literal completeness audit.
- K remains partly discussed; L and M remain unevaluated. No deck choice is approved here.
- Confirm the intended source-case ID and flow basis for the benchmark.
- Select BEP outputs, forcing range, and acceptable numerical/prediction error before DOE.
- Obtain the 2022 mechanism/SI data or explicitly defer dynamic-coverage implementation.
- Resolve the bulk/pore storage and interface-flux equation before calling the radial path conservative.
- No notebook design, model implementation, presentation, public Action, or merge approval is established by this receipt.
