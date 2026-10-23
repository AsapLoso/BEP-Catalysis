# Twee Work-agents voor vanavond — startbrief, 19 oktober 2026

> **STARTKLAAR ALS PROMPTS; SESSIES NIET DOOR DEZE CHAT GESTART.**
>
> **Twee zelfstandige, complementaire opdrachten:** Agent A **wetenschappelijke methode / inhoudelijk onderzoek** in project-management-agents, Agent B **uitvoerbare notebook** in Methanol-Catalysis. Gebruik **aparte Work-chats en aparte branches/PR's**; bouw niet op vanzelf gedeelde chatcontext. De gebruiker wil wakker worden met een **mooi, uitvoerbaar notebook met zinvolle grafieken**, niet een 47-tickets-afvinkrapport. Beschrijf eerlijk wat wel/niet werkelijk is doorgerekend of gevalideerd; beloof niet gegarandeerd een volledige fysische implementatie.
>
> **Laatste gebruikerscorrectie:** de **eerste toets** mag verschillende **(R,D)**-paren met **constant R²/D** vergelijken. De vraag of de hele radiale dimensie aan reactor-outlet observeerbaar is / via modelreductie weg kan, blijft interessant maar is **een separate vervolgonderzoeksvraag**, niet hetzelfde experiment. **De pelletpopulatie is later een expliciete LOGNORMALE-verdelingshypothese**, geen nu verplichte implementatie.
>
> **K partly reviewed; L and M not user-reviewed.** Presentation PR #4 onaangeroerd.

## Source of truth / links

- [Scientific Method Selection Wayfinder](../wayfinder/scientific_method_selection.md)
- [Notebook Delivery Wayfinder](../wayfinder/bep_reactor_notebook_delivery_2026_10_19.md)
- [Numerical Accuracy Wayfinder](../wayfinder/bep_dynamic_numerical_accuracy.md)
- [19 Oct research method handoff / revised steps](session_handoff_radial_notebook_and_parallel_work_2026_10_19.md)
- [R²/D scaling and radial observability](2026_10_19_radial_observability_and_reduction.md)
- [47-item critique ledger](../dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md) and [user primary thought dump](user_thought_dump_2026_10_18_reactor_recovery.md)
- [Film/units and execution-scope correction](followup_2026_10_19_film_diffusion_agent_gap_audit.md)
- [BEP issue #58](https://github.com/AsapLoso/project-management-agents/issues/58); [draft research PR #50](https://github.com/AsapLoso/project-management-agents/pull/50)
- [Actual canonical pushed code: Methanol-Catalysis/main/pbr](https://github.com/AsapLoso/Methanol-Catalysis/tree/main/pbr) with module tests. Snapshot visible on 19 Oct: Methanol-Catalysis/main SHA **5400881b3d06164db10488abae27b110ac618258**. **REFETCH SHA on agent start**, don't assume static SHA or package compliance.

### Shared rules

1. Read repository instructions and freshest branch states; record *both* repos + SHAs at start. Do not blindly duplicate old Hermes uniform-pellet PSSA baseline.
2. **Chosen experimental modelling simplification:** no **external** film resistance: c_p(z,R,t)=C_b(z,t); **finite radially resolved pore diffusion** inside. Treat Dirichlet boundary and bulk↔pellet flux as one conservative coupled model. This is not evidence that **internal** transport is instantaneous. Real site chemistry dynamic-θ vs PSSA remains unverified, don't invent parameters.
3. Use actual physical R,D_eff,epsilon_p inputs and **derive** tau_D=epsilon_p R²/D_eff under explicit convention. **5–30 ms was a casual ballpark**, neither validated physical bound nor mandated relaxation delay.
4. The 47 points are a traceability list. Triage relevant subset; do not fabricate 47 tickets or close untested points. An independent second pass is still outstanding.
5. No blind changes to default branches, no merging, no unreviewed public publication of private data, no fake run receipts or silent assumptions; use separate PRs and dependency notes.
6. Scientific handoff via **GitHub** with exact branch SHA, source paths, what was checked/run, assumptions and blockers. In the Work chat, notify user with permalink; peer agent must **REFETCH** handoff before changing shared physical assumptions. **No automatic cross-chat notifications assumed**.
7. Work sessions can run in parallel: B proceeds with notebook UI/plots and minimal toy/synthetic visual scaffolding clearly labeled pending source; B **does not pass off unverified bulk/pellet physics** until A's evidence is read. A **does not rewrite notebook UX**.

## AGENT A — SCIENTIFIC METHODS: copy-paste Work prompt

> Werk als zelfstandige **wetenschappelijke onderzoeksagent** voor mijn BEP over dynamische acetyleenhydrogenering.
>
> Begin in \`AsapLoso/project-management-agents\`, branch \`research/bep-K-results-review-2026-10-18\`. Lees de Scientific Method Selection-, Numerical Accuracy- en Notebook Delivery-Wayfinders en de researchhandoff/critique-index van 19 oktober; de 47 punten zijn een auditregister, geen 47 tickets. Lees de **actuele** \`AsapLoso/Methanol-Catalysis/main/pbr\` en tests, niet alleen oudere assistant summaries.
>
> **Doe daadwerkelijk wetenschap, geen nieuw planningsrapport.** Reconstrueer de eerdere stappen en kies één concrete verifieerbare eerste slice. Prioriteit: inspecteer en leid de conservatieve **bulk↔radiaal pellet** koppeling af onder **nul externe filmweerstand** en **eindige radiale diffusie**. Verifieer de echte RHS, grens- en centrumvoorwaarden, brontermen, units, massa-/atoombalansen en de plaats van PSSA of dynamische θ. Voer waar verantwoord een **kleine echte reproducible test** uit. Doe daarna een heldere modelvergelijking met verschillende \`(R,D_eff)\`-paren die dezelfde \`R²/D_eff\` delen; interpreteer of dimensieloze pellet- en outletcurves samenvallen en welke aannames dit garanderen of verbreken. Als het model eerst gerepareerd moet worden, lever een reproduceerbare defecttest en een minimaal uitvoerbaar herstelvoorstel, niet een verzonnen succes.
>
> De eerdere 5–30 ms is slechts een ruwe schatting. De lognormale pelletgrootteverdeling hoort als **later te testen hypothese**, niet als blocker. Zie \`research/notes/2026_10_19_radial_observability_and_reduction.md\` voor scheiding van scaling vs reduceren.
>
> **Op te leveren:** één kort owner-readable wetenschappelijk notitieboek/rapport met vergelijkingen en exacte codebronregels; echte testoutputs/plots indien uitgevoerd; controleerbare receipt; minimaal één inhoudelijke vervolgbeslissing; relevante 47-punten met OPEN/VERIFIED/DEFERRED. Werk uitsluitend op **eigen branch/PR**. Sluit geen Wayfinderbeslissingen op basis van aannames. Plaats op issue #58 of eigen PR een expliciete **FOR NOTEBOOK AGENT**-handoff met datum, repo SHAs, bewijs, benodigde correcties, nog onzekere fysica en minimaal verantwoord uitvoerbaar modelpad. Meld voltooiing met link in deze Work-chat. **Geen merge en geen wijzigingen aan presentatie-PR #4.**

## AGENT B — NOTEBOOK BUILDER: copy-paste Work prompt

> Werk als zelfstandige **wetenschappelijke notebook-ontwikkelaar** voor mijn BEP, vanuit de werkelijk gepushte \`AsapLoso/Methanol-Catalysis/main/pbr\` plus de Notebook Delivery Wayfinder en het handoffdocument op \`AsapLoso/project-management-agents\` branch \`research/bep-K-results-review-2026-10-18\`. Lees de relevante user thought dump en science context via links, niet door zelf 47 tickets uit te vinden.
>
> **Bouw een echt uitvoerbare, verzorgde, modulaire plug-and-play Jupyter-notebook** (kleine helpermodules, duidelijk configuratieblok en leesbare fysica). Hoofdoutput: prachtige, begrijpelijke **input→output tijdcurves** voor de vier reagerende gassen, axiale profielen, **radiale pelletprofielen/heatmap**, een plot van de laatste **volledig ingeregelde** perioden en berekende periodegemiddelden. Maak parameters zoals inlet amplitude/frequentie, R, fysisch onderbouwde D_eff/epsilon_p, T/P/Q en solverresolution eenvoudig te veranderen; toon afgeleide R²/D en tau, niet een arbitraire vaste delay. Een first-cut kleine \`(R,D)\` scaling comparison met identieke R²/D is zeer welkom.
>
> **Fysisch contract:** nul externe filmweerstand, maar **finite radiale pellet diffusie**. Pas niet ongemerkt een uniform pelletmodel toe als enige hoofdresultaat. Controleer conservatie en oorspronkelijke source assumptions. Dynamic surface θ moet alleen als **werkelijk gekoppeld bron-onderbouwd** verschijnen; geen gefabriceerde kinetics. Als dit fysisch nog niet werkt, lever een **eerlijk benoemde prototype-notebook** die draait, met plots waarop duidelijk staat wat alleen synthetisch/toy is en welke fysica nog blokkeert; doe niet alsof het af is.
>
> Werk op **eigen feature branch/PR in Methanol-Catalysis**. Begin parallel met notebook-UX, config, figuren en reproduceerbare tests; voordat je wetenschappelijk inhoudelijke modelkeuzes vastlegt, lees de **nieuwste FOR NOTEBOOK AGENT-handoff** van Agent A op GitHub issue #58 of diens PR. Geen stille overname van ongeteste fixes. Probeer de notebook end-to-end echt uit te voeren, zorg dat alle opgeslagen figuren uit echte runs komen of expliciet als illustratie gemarkeerd zijn, leg versies, inputs, runtimes, geslaagde/mislukte checks en bronstatus vast. Lever de notebook, duidelijke runinstructies, eigen PR en handoff naar Agent A/gebruiker. Meld voltooiing met permalink in je eigen Work-chat. **Niet mergen; presentatie-PR #4 niet wijzigen.**

## Later/parked: LOGNORMAL pellet population hypothesis — owner correction

> **LATEST USER CORRECTION:** Use a **lognormal pellet-radius distribution**, **NOT** a Gaussian/ordinary normal distribution and **NOT** a truncated Gaussian. The earlier ordinary-normal formula, negative-radius handling, and claims that an ordinary Gaussian was the user’s definitive choice were mistaken and are superseded. No population simulation is required for tonight’s first notebook.

For a number-weighted population of **positive** radii define

\[
\ln R \sim \mathcal N(m,s^2),\quad R>0,\quad
\mathbb E[R^k]=\exp(km+\tfrac12 k^2s^2).
\]

Here \(m,s^2\) are the **log-radius** mean and variance, and should not be conflated with the arithmetic radius mean/variance:

\[
\mathbb E[R]=e^{m+s^2/2},\quad
\operatorname{Var}(R)=(e^{s^2}-1)e^{2m+s^2},\quad
\mathbb E[R^2]=e^{2m+2s^2}.
\]

**User’s postponed experiment:** compare differently parameterized lognormal pellet populations and diffusivities while holding an appropriate **mean squared-radius/diffusivity ratio** fixed, asking whether their output response differs; test as a hypothesis, do **not** assert they must differ.

**Mathematical caution:** At fixed log-spread \(s\), a location scaling \(m\mapsto m+\ln a\) and diffusivity \(D\mapsto a^2D\) gives the **same entire distribution** of \(R^2/D\), hence no change for a response dependent on that argument alone. To test differences while fixing \(\mathbb E[R^2]/D\), allow the distribution **shape** (e.g. \(s\)) to differ, or specify constant arithmetic \(\operatorname{Var}(R)\) (which is NOT the same as constant \(s^2\)) and adjust \(D\). These are distinct comparisons. The user has not yet chosen which notion of “same variance” should be fixed.

**Population weighting:** If the distribution is **number-weighted**, equal-density catalyst volume contributions scale as \(R^3\). A reactor-inventory average of a radius-dependent quantity \(f\) is \(\mathbb E[R^3 f(R)]/\mathbb E[R^3]\), NOT generally \(\mathbb E[f(R)]\). The relevant volume-weighted mean diffusion ratio is \(\mathbb E[R^5]/(D\mathbb E[R^3])\), not automatically \(\mathbb E[R^2]/D\). If instead the input distribution is **mass-weighted**, say so and change the integration measure. Keep catalyst amount and geometry physically consistent.

**IMPORTANT PROVENANCE ERRATUM:** User explicitly clarified that their **own previous lognormal fitting/writing concerned SEM characterization of a YBCO superconductor**, NOT catalyst-pellet data or the BEP reactor/synthesis. The 'I can cite my own writing' remark was partly a joke. Do **not** use it as evidence for lognormal catalyst-pellet radii, do not conflate with an unrelated remembered Verwachte.txt case, and do not fabricate its bibliographic identity. The lognormal pellet distribution is **a later user-selected hypothetical BEP model family** only, pending pellet-specific evidence. [Source-provenance correction](2026_10_19_erratum_log_normal_ybco_sem_vs_bep_pellets.md).

**DEFERRED:** lognormal PSD population DOE, direct comparison with monodisperse pellets, full Berger §6 reading, global model reduction/identifiability, and final independent 47-item audit. Keep tracked without blocking two-agent notebook/science first slice.

## Latest statuses

- **Agent A:** not started in this conversation.
- **Agent B:** not started in this conversation.
- **Scientific assumption choice:** no-film/finite-radial, but actual source-specific kinetic/transport proof unverified.
- **Notebook:** not yet built or run by this handoff.
- **Work-mode onboarding:** user starts two separate Work chats and pastes prompts A and B; they link via GitHub handoffs, not autonomous inter-chat messaging.
