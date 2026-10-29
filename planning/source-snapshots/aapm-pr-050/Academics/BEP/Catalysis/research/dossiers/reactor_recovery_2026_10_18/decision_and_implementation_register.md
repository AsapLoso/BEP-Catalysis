# BEP reactor recovery — besluitvorming, subletters en uitvoeringsregister

> **UPDATE 19 OKTOBER 2026: pbr/ IS INMIDDELS GEÜPLOAD NAAR METHANOL-CATALYSIS/main.** Claims hieronder dat remote nog geen `pbr/` bevat, zijn **historisch, van vóór de laptopsynchronisatie**. [Gecontroleerde status, gebruikerscorrecties en checklist voor volgende beurt](../../notes/user_followup_2026_10_19_notebook_and_urmes_checklist.md). **Onderzoeksinstrument bijgesteld:** plug-and-play Jupyter-notebook met input/outputplots en ingeregelde cycli; fysische/numerieke verificatie is een randvoorwaarde en niet het einddoel. **U01–U47 blijven open voor de tweede auditpass.**


> **18 OKTOBER 2026 — WERKDOCUMENT, GEEN GOEDGEKEURDE SPECIFICATIE**
>
> [Gebruikersbron: transcriptnabije Thought Dump](../../notes/user_thought_dump_2026_10_18_reactor_recovery.md) · [K uitgebreide technische reconstructie](../../../presentation/deep-dives/K_full_results_interpretation_2026-10-18.md) · [bestaande scientific method Wayfinder](../../wayfinder/scientific_method_selection.md) · [numerieke Wayfinder](../../wayfinder/bep_dynamic_numerical_accuracy.md) · [bestaand F-bulk/pellet-conserveringsonderzoek](../../../presentation/deep-dives/F_conservation_state_space_2026-10-14.md)
>
> **Auteur:** assistant vertaalt de recente user thought dump naar **controles, besluitvragen en uitvoerbare slices**. Dit is niet de implementatie zelf. **K: gedeeltelijk geëvalueerd; L/M: niet inhoudelijk geëvalueerd.**
>
> **Eén bestemming:** een **brongetrouw, reproduceerbaar, fysisch consistent, gekoppeld reactormodel** dat de voor het BEP relevante *stationaire en periodieke* observabelen met gecontroleerde fout kan voorspellen. We willen exact weten **welk fysisch probleem een bepaalde softwareconfiguratie oplost**, niet alleen of de code runt.

## 0. Snel oordeel over scope & oorzaken van de ontstane verwarring

**[USER REVIEW]** De standaard 240-variabelen-run is voor de beoogde dynamische onderzoeksvraag **veel te gereduceerd**: geen radiaal veld; 2019 LHHW/PSSA sluit oppervlaktememory instantaan; periodieke gate registreert één eindsnapshot. Zelfstandige waarde als sanity/bronkinetische **baseline** blijft open — niet hetzelfde als hoofdwetenschappelijke reactor.

**[FACT: code/docs]** Radiale velden bestaan als opt-in codepad (2.400 allocated scalar entries), and a broader local `pbr/` framework was previously documented in a Wayfinder. **[HISTORICAL remote check, 18 Oct]** Public `Methanol-Catalysis/main` lacked `pbr/` at that check. **[VERIFIED 21 Oct]** Current public `main` is `5400881b3d06164db10488abae27b110ac618258` and contains the `pbr/` modules and two test files; its workflows are deployment-only. This proves publication of code, not scientific validation, a passing test run, or a PBR GitHub Action.

**[USER REPORTED]** De methodologische kritiek was vóór letter K onvoldoende als *centrale beslisvoorwaarde* zichtbaar, hoewel F/G/E/J al belangrijke voorwaarden documenteerden. **[AI DIAGNOSIS]** Vermoedelijk: (i) modelreductie naar default \`resolve_radial=False\` niet als verschuiving van onderzoeksobject behandeld; (ii) geen expliciet minimumphysics-contract met relevante observabelen; (iii) positieve interne tests en sensitiviteitsplots kregen te veel gewicht; (iv) prioritering van de presentatie boven wetenschappelijk begrip; (v) source-mix/geometrie stond in voetnoten in plaats van blocking acceptance gate. Dit is een *hypothese over workflowfout*, geen bewijs wie wat wanneer besloten heeft.

## 1. Inhoud opdelen in subletters — juist om te vermijden dat K alles opslokt

| Subletter | Te begrijpen/beslissen | Resultaat dat er zou moeten liggen | Niet verwarren met |
|---|---|---|---|
| **Kα — Wetenschappelijke observabelen** | Welke X, S, T/P, totale stofbalans, \(\bar F_{ethylene}\), \(A_\text{out},\phi\), θ en vergelijking moeten we voorspellen, met welke nauwkeurigheid? | Observabelencontract, eenheden, in/out samenhang, periode/mean definities | code-test PASS |
| **Kβ — Fysisch modelcontract** | Welke bulk-, pore- en oppervlaktevelden, interfaciale flux, boundary conditions, adsorptiemechanismen horen daarbij? | PDE/ODE + conservatie + baseline↔full structure | aantal regels code |
| **Kγ — Brondomein en benchmark** | Hoe maken we **exacte Urmès-2019-case** reproduceerbaar naast onze eigen bedconfiguratie? | bronconfiguratie, α-drager, 0,1 g, 4 mm, 0,5 g diluent, feed-conventies, 51/62 °C, 1,26 bar, check tegen gepubliceerd X/flows | een mixed 5-mm/75-mg run |
| **Kδ — Parameter- en initialisatie-ruimte** | Wat varieert per run (Q/P/T/inlet/radius) vs wat is een dynamische toestand? Wat is een fysisch toegestane scan? | admissible-domain tabel, LHS/Cartesian kleine smoke-grid, normalization, tau_res plots | 11-/13-dimensionale **physical state** |
| **Kε — Numeriek verifieerbare koppeling** | Kunnen de bulk/pore/surface balances discretiseren zonder dubbel geboekte chemie en met geschikte stijfheidsbehandeling? | verified FV/MOL, coupled film/shell flux, positivity/conservation, Jacobian and mesh benchmarks | default uniform PSSA suite |
| **Kζ — Periodieke experimentdefinitie** | Wanneer is periodic steady state bereikt, wat meten we over de laatste n complete cycli? | trajectory/phase/harmonics/cycle-mean/noise-tolerance receipt | single terminal sample |
| **Kη — Reproduceerbare software** | Welk \`pbr\` is canoniek? publiceer/migreer naar Methanol-Catalysis, CI met volledige provenance | pinned code, datasets, tests, artifacts/actions | een geslaagde lokale OneDrive-run |
| **Kθ — Onafhankelijke audit en wetenschappelijke beslissing** | Zijn alle user-claims inhoudelijk behandeld, welke bewijslast is geleverd? | onafhankelijke check, issue closure met evidence/owner review | zelfattestatie 17/17 |

**NB:** Dit zijn **nieuwe subletters van K als onderzoeks-/werktriage**, geen uitbreiding van het presentatie-A–M alfabet of alvast definitieve solverarchitectuur.

## 2. Traceerbare user-feedback naar technische vragen en werk

| ID | Gebruikerspunt / te behouden intentie | Verificatie, actie of besluit |
|---|---|---|
| **U01** | Onderzoek weer zelf “ownen”; presentatie niet leidend | Herstel fysische afleidingen + experiment-specificaties; vraag eigenaar welke observabelen leidend zijn |
| **U02** | Waarom kwamen K-kritiekpunten niet in F/G/E naar boven? | Onafhankelijk spoor terug door F/G/E/J; markeer de oorzaken van lost assumptions en default-reductie |
| **U03** | 3 getallen: exacte rekendefinities | Mathematische X/S/τ definitions, eenheids-/balancebewijs, codepad naar receipts |
| **U04** | Periodieke sinus: outlet over laatste relevante cycli, per gascomponent | Alle H₂, C₂H₂, C₂H₄, C₂H₆ timeseries en transport/state histories; periodiek mean, FFT/harmonics en phase |
| **U05** | Mogelijk out = sinus, of niet? | Lineair sinus-in/sinus-out vs niet-lineair harmonics/DC rectificatie expliciet |
| **U06** | Geen terminal sample en geen vroege starttransient middelen | Convergentie \(x(t+T)\approx x(t)\), analyse n complete cycli, quadrature |
| **U07** | Sinus-fit optioneel, middelen kan genoeg zijn | Mean voor doel, fit/harmonics voor gain/phase, aantoonbaar als twee afzonderlijke outputvragen |
| **U08** | Residence time is primaire fysische x-as | \(\tau_{res}=\epsilon_b V_{bed}/Q_{actual}\), flow-basis, charts T/P/Q→τ; dimensionless time and forcing frequency |
| **U09** | “11 of 13?” physical state | 11 types = 4 bulk gas + 4 pore gas + 3 coverages. 13 is hypothetical 4+4+5. The actual Hermes explicit-coverage branch has 4 bulk gas + 5 coverages and no radial pore-gas fields (9 types); its separate radial branch has 4 bulk + 4 pore. Distinguish field types from allocated/independent coordinates; time, inputs and parameters are not states. |
| **U10** | Bedrijfscondities T, P, Q etc vormen *andere* parameter/configruimte | Benoem \(\lambda=(T,P,Q,R_p,\tau,\mathrm{feed},\ldots)\); \(\lambda\) ≠ \(x(t)\); input \(u(t)\) tijdvariabel |
| **U11** | Inlet-compositie ook variëren mogelijk | DOE-extensie met simplex constraints, H₂:C₂H₂ ratio, Ar compensation, constant molar budget |
| **U12** | Default zonder radiaal pore transport is voor projectdoel niet goed genoeg | Heropen verplichting; verifieer waarom/wanneer radial coupling fysisch nodig; leg *full vs reduced* modelkeuze expliciet vast |
| **U13** | “Zet radiaal gewoon aan” maar track effecten | Gebruik bestaand \`resolve_radial\` pad slechts na conservative flux & Jacobian audit; geen instant claim het werkt |
| **U14** | Dynamic surface physics is missing | Retrieve and verify the published 2022 network, equations and parameter availability; do not imply they are ready to implement. The current package’s optional assumed-τ relaxation is not the 2022 microkinetic model and its gas-rate path does not consume θ. |
| **U15** | 2008 en ‘2021’ wetenschappelijke modellen niet toegepast | Bronregister 2008 Berger/Urakawa vs 2022 Urmès (2021 submission), identificeer exacte equations/transferability en niet-verwerkte termen |
| **U16** | Temperatuurfiguur assen en “ideale 66–86 °C” | Plots met zichtbare schalen/axes; **geen fysisch optimum** buiten bronwindow zonder validatie; 51/62 window apart |
| **U17** | Negatieve netto S is logisch, geen sensationeel bugverhaal | Noteer definitie \(S=1-r_2/r_1\); alleen check domein/flow/stoichiometry |
| **U18** | Waarom twee coverage tests “falen” buiten geldigheidsinterval? | Identificeer exacte 12 source rows, gemeten condities, opgegeven ranges en error definition; split **in-domain pass**, extrapolation, out-of-source-range; **geen test eraf knippen** om 10/10 te claimen |
| **U19** | LHS of grid op alle geldige parameterranges | DOE-spec, dimensional sampling, sparse grid/LHS, feasibility filter, run cost estimate; geen naieve hoge-dim cartesian explosion |
| **U20** | Flow-residence afhankelijkheid en T/P surfaces | Chart tau vs Q, T, P **alleen** na vastleggen Q_actual of F_molar/mass basis; pressure at fixed Q changes molar flow |
| **U21** | Druktrend “welke formule beïnvloedt dit echt?” | Per source expliciet p_i=y_iP in LHHW adsorption denominator, kinetic partial rates, stoichiometric throughput normalisation controleren |
| **U22** | Expo-vorm flow kan simplifier toelaten maar *niet nu* | Bewaar als uitgesteld mathematisch modelreductie-idee, **geen curvefit als nieuw fysisch bewijs** |
| **U23** | Experiment-brongeometrie overnemen voor valideren | Urmès 2019: **α-Al₂O₃**, 0.1 g active catalyst +0.5 g diluent, 4 mm, 200mL/min, 1.26 bar, 51/62°C, source feed conditions; separate project reactor |
| **U24** | Automatische tests gaan over beperkte properties | 17/17 gate-scope matrix: chemical atom balance vs actual bed inventory, positivity vs stability, one X-grid test vs waveform |
| **U25** | Concentraties niet-negatief, finite, monotonic | Failure classes expliciteren: solver divergence ≠ negative concentration ≠ physically impossible reaction |
| **U26** | 30→120 axial cells, BDF tolerances lijken mesh/compute ruimte te geven | Zoë: gerichte discussion; formele error-vs-dofs/timestep/cost pas bij relevante observabelen; geen universal optimal grid claim |
| **U27** | Jacobian analytisch vs independent numerical check | Finite differences met tolerantie/step/refinement, check niet alleen selected columns; benchmark runtime; niet claimen één vergelijking bewijst alle Jacobian correctness |
| **U28** | Periodiek eerst settle, daarna laatste volledige cycli middelen | \(\|x(t+T)-x(t)\|_{\rm scaled}\) en cycle output convergence; 8+4 perioden of 50ms slechts start-hypothesen; runtime afleiden |
| **U29** | Laatste 9 van 10s is illustratief | Doe geen arbitraire horizon/mean met startup samples; period-based exact windows |
| **U30** | “27.9% moet verdwijnen bij Δt→0” | Exact-time *semi-discrete* upwind spatial diffusion (G), \(N_z\to\infty\) vs \(dt\to0\), FE CFL=1 pure-advection exception; owner pedagogical review |
| **U31** | Niet meer op tijdstip x, amplitude/phase/time series | Periodic output design & tests; process input and output full curves; compute harmonic transfer and net yield |
| **U32** | “Wat beantwoordt het huidige baseline-model?” | Explicit limitation statement: steady/constant-feed LHHW advection baseline and basic forced-gas response, *not* resolved pellet/surface-memory/validated periodic yield |
| **U33** | Model te simpel, wetenschappelijk zwakke opbrengst | Leg model reduction vs original hypothesis vast; geef reductie zijn plaats als *unit test / baseline*, niet hoofdwetenschappelijke conclusie |
| **U34** | Diagnostic code bugs niet stil laten staan | Patch sensitivity figure scaling, frequency_response shape/readout; reproduceer voor/na; origin in J ticket |
| **U35** | Move to Methanol-Catalysis repo | **Historical 18 Oct:** remote main lacked `pbr/`. **Verified 21 Oct:** public main at `5400881b3d06164db10488abae27b110ac618258` contains it. Review the live code/feed basis and provenance; no scientific PBR workflow is present. |
| **U36** | GitHub Actions laat experimenten reproduceerbaar runnen | Spec minimal CI + physics tests + short smoke sweep + artifact retention + scheduled/manual bigger sweeps; avoid hours burn; no secrets in repo |
| **U37** | “Alles opschrijven, misschien woord voor woord” | Raw capture linked; preserve user quotes + uncertainty; do not silently overwrite |
| **U38** | Independent auditor / completeness pass | Compare original user message word by word against thought dump, IDs, tickets and evidence; **outside authoring agent**; write signed audit receipt |
| **U39** | “Het was te groot; opsplitsen in subletters” | Kα–Kθ with one observable/scientific decision gate per slice; don't mix presentation with numerical research |
| **U40** | Kan ik dit aan Damian/Zoë fysisch verantwoorden? | Owner-reproducible equations, provenance and 1-page state-of-research; Zoë numerical error/Jacobian/radial gate; Damian kinetics/experiment transfer. **No messages sent.** |
| **U41** | Geen defensieve reacties, inhoudelijke technische discussie | Mark user value judgments as user judgments, explain substantive scientific caveats without nitpicking tone |
| **U42** | Hoe leggen we “simpel model” accuraat uit? | Beschrijf *semi-discrete 1D convective-reactive MOL with algebraic PSSA source, no independent radial/surface inventory in default*; simple relative to goal, not necessarily numerically free |
| **U43** | “Welke grootheden moet dit model betrouwbaar beschrijven?” | **Voorwaarde voor alle andere tickets:** formalise target outputs, relevant forcing frequency and tolerated error from BEP scope |
| **U44** | Variabele deeltjesporositeit, tortuositeit, particle radius | Ensure physical variation enters dynamic model, not only post-processed diagnostic η/φ; verify units and effect on species-specific D |
| **U45** | Zorg dat nieuwe tests bronvaliditeitsregime respecteren | Separate paper reproduction, broad extrapolation stress tests, positivity/mass checks, code sanity, and physically supported DOE |
| **U46** | State-space staat nergens meer centraal | Draw exact vector layouts and dimensionalities in legacy, PSSA, radial and dynamic θ; inspect number of independent states versus frozen shells |
| **U47** | Overloop eerdere secties waar deze randvoorwaarden gemist zijn | Make backward trace audit E/F/G/I/J/K: what was already flagged, what was not elevated, when default changed, which files/PRs tracked |

**Status van alle items:** **OPEN FOR AUDIT**, tenzij er apart een **[VERIFIED]**-artefact met exact source ref of runreceipt wordt toegevoegd. Een user-idee wordt niet automatisch een implementatiebesluit.

## 3. Afhankelijkheidsstructuur: niet gewoon alles tegelijk op CI gooien

### Island A — Required physics and observables (decision first)

- [ ] **A1 Scientific output contract**: op welke tijdschaal/periode en met welke tolerantie moeten X, S, cycle-average net \(F_\mathrm{C2H4}\), full species & flux balance en transfer gains worden voorspeld? **User/supervisor gate**. Start met bestaande [research method selection](../../wayfinder/scientific_method_selection.md).
- [ ] **A2 Fidelity contract:** is radiale diffusie **verplicht voor het doel** ondanks quasi-uniformiteit in een gemeten regime? Is echte dynamic-θ kinetic memory verplicht? Dit zijn verschillende keuzes: radiaal veld kan fysisch verwaarloosbaar zijn in specifieke regimes en **toch** waardevol als onderdeel van de uitgebreide onderzoeksagenda. Leg het expliciet vast.
- [ ] **A3 Model derivation**: conservation PDEs \(C_b(z,t)\), \(c_p(z,r,t)\), \(\theta(z,r,t)\) met één gas/pellet interfaciale uitwisselingsflux, juiste source-normalization; initial and boundary conditions. **Niet eerst numeriek tunen**.

### Island B — Source/benchmark and canonical code

- [ ] **B1 Source matching**: full 2019 condition matrix; exact temperature, pressure, catalyst, dilution, total molar flow convention, gas feed, sample IDs and measured outlet, effective parameters; never compare composite 5-mm/75-mg outputs directly with source 4-mm/100-mg results.
- [ ] **B2 Source physics**: Urmès 2022 published elementary mechanism, parameter availability and supporting information; source evidence for every proposed transient rate. 2008 Berger framework as retrospective reference only. No invented constants.
- [ ] **B3 Code inventory**: current public `AsapLoso/Methanol-Catalysis/main` contains `pbr/` at `5400881b3d06164db10488abae27b110ac618258`; inspect exact version/provenance, partial-pressure conversion and source conditions before reuse. The workflow tree is deployment-only; no scientific PBR Action or completed run is verified. Avoid private paths/keys.
- [ ] **B4 Build acceptance:** lock dependencies, parameter provenance config files and regression/golden-case receipts; minimal public CI only after source and licensing scope are approved.

### Island C — Numerical coupling, not mere solver PASS

- [ ] **C1 Radial coupled model**: conservative boundary flux where bulk loss == pore gain and gas reaction appears **once** in each correctly scaled physical inventory; test summed gas+adsorbate atom inventory. The F-audit raises a **possible double-booking** in radial code paths; independently reproduce before changing.
- [ ] **C2 Limits**: \(D\to\infty\) (radial approximates uniform state), zero reaction, no-flow / fixed-inlet, source stoichiometry, linear constant-velocity advection and analytic spherical diffusion.
- [ ] **C3 Dynamic θ**: is mechanism thermodynamically/kinetically source-backed? Does \(r_g\) use **θ(t)** rather than algebraic equilibrium closure? Compare PSSA limit.
- [ ] **C4 Jacobian & cost**: finite-difference/complex-step where valid, column-by-column Jv checks, sparse CSR where validated, BDF/Radau versus explicit/IMEX when physically relevant.
- [ ] **C5 Space+time convergence on goal outputs**: stationary conversion is insufficient; increase N_z, N_r, order and vary tolerance/max_step while preserving input frequency; source of numerical damping separated from physical damping.

### Island D — Experimental/sensitivity design

- [ ] **D1 Periodic steady-state**: explicitly detect recurring full state (or justified observable equivalence), hold several *full cycles*, periodic mean and Fourier coefficients; do not use only terminal sample or solver-point max/min.
- [ ] **D2 Time-scale screen**: τ_res from void volume/actual Q, τ_p vs \(R^2/D\), surface kinetic times only with source-backed rates; derive periods and t_end from these scales. 50 ms and 8+4 cycles **proposals**, no unconditional guarantee.
- [ ] **D3 DOE within source ranges**: before thousands of runs, one source-matched baseline and a small scientifically valid test matrix; LHS or factorial if dimensionality small, enforce sum of mole fractions=1, positivity and H₂ availability; distinguish empirical calibration domain vs extrapolation/guardrails.
- [ ] **D4 Stoichiometric objective**: net ethylene must subtract inlet ethylene and be integrated as a molar-flow difference in periodic steady state; avoid conflating highest conversion with highest net yield.
- [ ] **D5 Plot conventions**: clearly separate X and S axes, avoid one misleading autoscale with negative S outlier; plot X/S and τ_res vs Q,T,P with stated mass/volume flow basis. Do not fit an exponential and call it new physics.

### Island E — Reproducibility, dissemination and independent audit

- [ ] **E1 Prepare Methanol-Catalysis publication PR** once source and license are known. Keep existing content/book workflows intact.
- [ ] **E2 GitHub Actions tiers**: (a) lint+unit+smoke in allowed domain on PR; (b) manual workflow_dispatch short reference re-simulation; (c) slower parameter/mesh/frequency sweeps with artifacts/receipt checksums and configured compute budget. Never rely on long idle Codespaces sessions.
- [ ] **E3 Issue ledger and independent audit**: every U01–U47 addressed by code, test, referenced future question, or reason for deliberate deferral. No “done” without runreceipt and user scientifc review.

## 4. Non-negotiable evidence labels

- **[USER INTENT]** What the owner wants or conjectures, including “radial is required”.
- **[CODE VERIFIED]** What exactly is on which branch and which RHS/solver path.
- **[SOURCE VERIFIED]** Exact published operating point, table/equation with page.
- **[DERIVED]** Calculation performed on a disclosed mathematical model.
- **[RECEIPT VERIFIED]** Recorded successful run, commit, env, inputs, outputs and hashes.
- **[HYPOTHESIS/OPEN]** Physically plausible but not experimentally or numerically established.
- **[CLOSED BY USER]** Scope tradeoff expressly decided by the owner, never inferred from a passing gate.

## 5. Questions for the two supervisors — *not sent*

- **Zoë:** Is the physically needed state the full 11-field bulk/pore/coverage layout? Which conservation/gradient conditions justify removing radial resolution or θ? How should we quantify observables' mesh/time errors? Why can exact-time upwind still attenuate at fixed grid? Is BDF/Radau/IMEX appropriate and how to verify sparse Jacobians?
- **Damian:** Which catalyst/bed/feed data are our ground truth? Are we reproducing Urmès 2019 data as a benchmark or modelling a different reactor? Which published mechanism/parameters justify **non-PSSA** dynamic behavior? What is the target periodic output and acceptance criterion for “validated enough”?
- **Owner:** The source-matched PSSA run should be the *calibration/verification baseline*, **not** quietly substituted for the intended richer model. Decide the specific target observable and fidelity, then execute limited vertical slices with independent audit.

## 6. Exact code pointers and no-fix-yet flags

- [Legacy scaffold](../../../3_Model/c2h2_hydrogenation_transient_model.py)
- [Old/new physical conservation analysis](../../../presentation/deep-dives/F_conservation_state_space_2026-10-14.md)
- [Reacting Hermes code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py)
- [Sensitivity figure factor-six and frequency-script reshape](../../../presentation/deep-dives/K_full_results_interpretation_2026-10-18.md) — **CODE FINDINGS NOT PATCHED**, defer to exact error reproducer.
- [Methanol-Catalysis remote](https://github.com/AsapLoso/Methanol-Catalysis)
- **PR #50** houses preparatory research only; do not claim full model/radial corrections or CI execution happened.

**END STATUS:** **RESEARCH REBOOT IN PROGRESS — NO SIMULATION PATCHES EXECUTED — INDEPENDENT AUDIT PENDING — USER REVIEW PENDING**.


## Audit status — 21 October 2026

A bounded non-author review is recorded in [independent_audit_receipt.md](independent_audit_receipt.md). Verdict: **INCOMPLETE** because the original visible 18 October message was unavailable, detailed 2022 SI parameters were not verified, and current source/physics blockers remain. U01–U47 stay open; K is partly discussed and L/M remain unevaluated. No code, tests, simulations or Actions were run.