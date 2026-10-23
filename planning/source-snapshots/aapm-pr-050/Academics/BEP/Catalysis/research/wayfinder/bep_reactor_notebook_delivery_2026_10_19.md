# Wayfinder: BEP reactor notebook — verkennende onderzoeksomgeving

> **TWO WORK AGENTS READY, NOT LAUNCHED (19 OCT):** [Kort gecoördineerd startdocument met twee uitvoerbare Work-prompts](../notes/2026_10_19_two_work_agent_launch_brief.md). Science-agent doet daadwerkelijk bulk↔pellet/conservation en (R,D) scaling onderzoek, Notebook-agent bouwt uitvoerbaar notebook op eigen PR en leest het science-handoffbewijs voordat fysische resultaten worden bekrachtigd. **Startcontrol: kies R en D als fysische invoer, leid R²/D en τ_D af.** **LATER**: hypothetische **lognormale** pellet-radiusverdeling met vooraf gedefinieerde momenten en massaweging; de eerdere persoonlijke fit betrof **YBCO SEM**, géén BEP-katalysatorpelletmetingen. Zie [herkomstcorrectie](../notes/2026_10_19_erratum_log_normal_ybco_sem_vs_bep_pellets.md). Geen automatische validatie/uitvoering.


> **BELANGRIJKE GEBRUIKERSCORRECTIE — 19 OKT, LATER DIE NACHT.** De **eerste** gevraagde onderzoeksvraag is concreet: **blijft de gesimuleerde respons gelijk voor verschillende combinaties van pelletstraal \(R_p\) en effectieve diffusiviteit \(D_\mathrm{eff}\) met dezelfde verhouding \(R_p^2/D_\mathrm{eff}\)?** Dit is een **schaalvergelijking/invariantietest**, niet primair een algemene discussie over meetbaarheid of over het mogen schrappen van de radiale dimensie. De eerdere vraag “is de radiale dimensie aan de outlet zichtbaar?” blijft hooguit een **optionele vervolgvraag**. Verder is een **verdeling van pelletgroottes** een **latere hypothese**, niet nu een engineeringticket of vereiste notebookoptie. De 5–30 ms zijn slechts een eerdere schatting.

> **Scientific note:** [R²/D schaalvergelijking en latere grootteverdelingshypothese](../notes/2026_10_19_radial_observability_and_reduction.md). **Bewaar de eerdere radiale waarneembaarheidsvraag als vervolg, niet eerste onderzoekstaak.**


> **NIEUW ONDERZOEKSDOEL 19 OKTOBER — RADIALE OBSERVEERBAARHEID EN VEREENVOUDIGING:** De **volledige radiale pellet** is een *te toetsen referentiemodel*, niet per se een blijvend vereiste voor alle notebookvarianten. De kernvraag: **is de tweede dimensie zichtbaar in reactor-outlet (C_{out}(t)) / netto productstroom en zo ja bij welke inlet-frequenties?** Vergelijk het vol-radiale model met een conserverend gereduceerd pelletmodel en eventueel de instant-uniform-limiet, bij dezelfde fysische configuratie; controleer het bulk↔pellet-interfacefluxpad en numerieke fout. **5–30 ms (10 ms) blijft ruwe schatting, geen opgelegde slider-range of relaxation law**; gebruik indien beschikbaar fysische (R_p,D_{eff},epsilon_p) en bereken tijdschaal uit de invoer en effectieve respons uit werkelijke simulatie. [Volledige testvraag, literatuur Kim 2008 en agenthandoff](../notes/2026_10_19_radial_observability_and_reduction.md). Deze update **supersedeert** het eerdere voorstel dat (R_p+	au_D) standaard de verplichte sliders zijn. **NB-3/nodige modelreductie blijft een beslissing op basis van metingen, geen vooraf opgeloste zaak.**


> **CORRECTIE 19 OKT 01:50 — GEEN KAART ALS OPLEVERING:** de tweede Work-agent voert een **scientific-method-loop in echt werk** uit: oude stappen en fysische aannames herbeoordelen → eerste tractable open bulk/pellet-vraag kiezen → code/primary bronnen inspecteren → beperkte echte verificatie doen → bevindingen + nieuwe beslissingen aan Notebook-agent overdragen. De Wayfinder houdt alleen beslissingen/bewijs bij. [Detailed source/agent gap audit](../notes/followup_2026_10_19_film_diffusion_agent_gap_audit.md). Aanbevolen bedieningen voor eerste exploratienotebook: pelletstraal plus **tau_D**, afgeleid **D_eff** zichtbaar; onderzoeksmatige range 5–30 ms, niet experimenteel geijkt. Geen uitgangswaarde gelijk aan molecuul-escape-time zonder definitie.


> **CONCEPT / NOG NIET DOOR GEBRUIKER GOEDGEKEURD — 19 OKTOBER 2026.**
>
> **GEBRUIKERSKEUZE VOOR MODELVERKENNING:** Pellet **niet uniform**. **Geen externe filmweerstand**: buitenste pelletlaag volgt lokaal bulk-gas onmiddellijk. **Binnenin** eindige radiale diffusie en mogelijke vertraging. Voorgestelde exploratieve diffusiestijd circa **10 ms**, slider voorlopig **5–30 ms**, niet gemeten of gevalideerd. Niet stilzwijgend vervangen door zero-radial/PSSA-gasmodel.
>
> **BEPAALDE BESTEMMING:** een modulaire, echt uitvoerbare Jupyter-notebook, met begrijpelijke plots van ingang, uitgang, axiale en radiale concentraties en laatste ingeregelde cycli, waarvan de gebruiker zelf parameters kan aanpassen. De fysica en verificaties zijn voorwaarden voor zinvolle figuren; de deliverable is de notebook.
>
> **Geen 47 tickets:** [U01–U47 blijven in het traceability-register](../dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md), niet als Wayfinder-ticket vermenigvuldigen. Eigen doel voor deze map = **notebookoplevering**. Bronkeuze en fysica blijven bij [Scientific Method Selection](scientific_method_selection.md), numeriek bewijs bij [Dynamic Numerical Accuracy](bep_dynamic_numerical_accuracy.md), thesisplanning bij [master](bep_catalysis_master.md).
>
> **Broncontext:** [thought dump 18 Oct](../notes/user_thought_dump_2026_10_18_reactor_recovery.md), [notebook correctie 19 Oct](../notes/user_followup_2026_10_19_notebook_and_urmes_checklist.md), [avondplanning en agentshandoff](../notes/session_handoff_radial_notebook_and_parallel_work_2026_10_19.md). Canonieke codebron [Methanol-Catalysis/main/pbr](https://github.com/AsapLoso/Methanol-Catalysis/tree/main/pbr), door gebruiker inmiddels gepusht. De oude melding dat pbr remote ontbrak is verouderd.

## 1. Destination

Het notebook kan een fysische reactorconfiguratie en een inlet-signaal inlezen, het beoogde radiaal-resolved model daadwerkelijk uitvoeren, de tijd- en ruimterespons tonen, en de laatste volledige ingeregelde cycli analyseren (gemiddelde, eventueel amplitude/fase), zonder gesuggereerde fysische validatie die niet uit bronnen/tests volgt. Interactief **plug-and-play** via een configuratieblok en kleine herbruikbare modules uit de pbr-package.

**Runbooks:** de repo-lokale Wayfinder-skill, repo-instructies, en de wetenschappelijke bron-/preflight-runbooks uit de bestaande scientific-method kaart. Eventueel ontbrekend notebook-reproductierunbook apart rapporteren, niet stilzwijgend aannemen.

## 2. Decisions So Far

- [x] **[USER INTENT 19 Oct]** Notebook, geen nieuwe slide-deck; onderzoek met fraaie systeemresponsplots is het primaire product.
- [x] **[USER MODEL ASSUMPTION 19 Oct]** Sferisch pellet: aan de rand c_p(z,R,t)=C_b(z,t), in centrum ∂r c_p=0, **interne radiale diffusie eindig**. Geen externe concentratieval/film; dit is een gekozen *modelaanname*, geen experimenteel bewijs.
- [x] **[USER EXPLORATION IDEA, NOT CALIBRATED]** Tijdschuif 5–30 ms, startvoorbeeld 10 ms. Met vaste porositeit geldt ongeveer tau_diff=epsilon_p R²/D_eff; straal en diffusietijd zijn gekoppeld. Als R en target tau afzonderlijk schuiven, moet D_eff worden afgeleid en duidelijk vermeld; of gebruik R+D als onafhankelijke sliders en toon afgeleide tau.
- [x] **[CODE FACT 19 Oct]** Gepushte pbr-module en tests bestaan in Methanol-Catalysis/main; werkelijke correctheid van coupled radial bulk/pore RHS moet opnieuw worden aangetoond.
- [x] **[WORKFLOW INTENT]** Een tweede Work-sessie en eventueel geïsoleerd §6-literatuurwerk zijn ideeën, **nog niet gestart**; eerdere negatieve numerieke/source bevindingen blijven open.
- [x] **[REVIEW STATUS]** K gedeeltelijk beoordeeld; L/M helemaal niet besproken.

## 3. Active Frontier

### Island: Notebook experience (user decisions)

- [ ] **NB-1 — Eerste figuren kiezen** (wayfinder:grilling) — Welke combinatie vormt de minimale bruikbare pagina: vier inlet/outlet soorten, axiale profielen, radiale profielen/heatmaps en de laatste volle cycli? Welke paneeltjes zijn optioneel? Geen verzonnen θ-curves als fysische resultaten.
- [ ] **NB-2 — Sliders en fysische afhankelijkheid** (wayfinder:grilling) — Twee representaties zijn mogelijk: onafhankelijke R en D_eff met afgeleide tau, of R + doel-tau met afgeleide D_eff. Wat is begrijpelijker voor de gebruiker? Inlet-amplitude, frequentie, T/P/Q gescheiden en binnen hun geldigheidsgebied.
- [ ] **NB-3 — Eerlijke gedeeltelijke oplevering** (wayfinder:grilling) — Mag er al een wetenschappelijk duidelijk gelabelde **radial + PSSA** notebook zijn als de brongebaseerde dynamische θ-kinetiek nog niet implementeerbaar is, of moet zij expliciet onvoltooid blijven? **Niet zelf ratificeren.**

### Island: Reuse and scientific acceptance (crosslinked)

- [ ] **NB-4 — Bestaat een conservatief radiaal rekenpad?** (wayfinder:research) — Test of de echte pbr RHS rand, interfaciale bulk↔pelletflux, reaction source en pore-inventaris juist koppelt. Lees F/SM-4. Los geen nieuwe complexiteit op via uitsluitend een user-interface toggle.
- [ ] **NB-5 — Wanneer zijn de plots numeriek informatief?** (wayfinder:research) — Meet settling via verschillen tussen volledige cycli, maak gemiddelden over bijvoorbeeld laatste drie **volledige** cycli, verifieer de resolutie van sinusperiode en radiale/snelheidstijdschalen, meld onzekerheid per observable. Geen terminal snapshot of fictieve sinusfit.

## 4. Not Yet Specified — fog

- **LATER / HYPOTHESE: pellet-size distribution** — de door de gebruiker voorgestelde **lognormale** radiusverdeling bij vast totaal katalysatorvolume; onderzoeken of een verdeling versus één representatieve straal tot andere outletrespons leidt. Niet automatisch afleiden uit hetzelfde gemiddelde R²/D; correcte massa-/volumewichten en diffusiviteitsschaal vereisen aandacht. **Niet nu uitvoeren als notebook-blocker.**


- Inhoud, parameters en identificeerbaarheid van een werkelijk gekoppeld dynamisch oppervlakte-θ mechanisme (bestaande scientific-method kaart; 2022 full + SI).
- Kost/CI-opzet zodra een korte werkende referentierun bestaat.
- Later meerdere pelletgroottes tegelijk, complexer inputdesign, geautomatiseerde parameterverkenning en eigen notebook-paperleesomgeving.
- Optionele **derde sessie** voor volledige Berger (2008) §6. Hoge leesprioriteit, maar geen verzonnen harde afhankelijkheid voor iedere eerste notebookfiguur.

## 5. Out of Scope

47 Wayfinder-tickets, een automatisch gelauncht Work-proces, onbewezen kinetische constanten, alle bugs als voltooid markeren, het gehele thesistraject afsluiten, eigenmachtig publicatie op main, of een nieuwe presentatie-PR.

## 6. Scientific method loop — gebeurtenissen en avondstappen

| Stap | Status | Onderbouwing of direct vervolg |
|---|---|---|
| 1. Oorspronkelijke onderzoeksvraag, groot gekoppeld model | Historisch vastgelegd | Thesis/proposal + oude 11 fysieke velden |
| 2. Papers, E/F/G analyses, methodes en numeriek spoor | Gedeeltelijk onderzocht | Scientific-method & numerical Wayfinders |
| 3. Legacy scaffold en Hermes gereduceerde PSSA-reactor | Bestaande prototypes | Geen gelijkstelling reduced ↔ full physics |
| 4. K onderzoeksresultaten en 47 kritiekpunten | Assistant research vastgelegd, **user review open** | [register](../dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md) |
| 5. pbr eindelijk naar remote | **Door gebruiker gedaan, geverifieerd** | [Methanol-Catalysis/main/pbr](https://github.com/AsapLoso/Methanol-Catalysis/tree/main/pbr) |
| 6. Notebook-doel en radial/no-film aanname | **Nu vanavond besproken** | Dit concept; onafhankelijk-koppeling nog open |
| 7. Kleine Wayfinder + 2 Work-handoffs voorbereiden | **Nu voorbereid, niet gelanceerd** | [coördinatienotitie](../notes/session_handoff_radial_notebook_and_parallel_work_2026_10_19.md) |
| 8. Echte wetenschappelijke inspectie/bronselectie | **Open** | Science sessie, eigen evidence PR; beslisgate niet omzeilen |
| 9. Notebookimplementatie/runs en gereviewde figuren | **Open — nog niet begonnen** | Notebook sessie na user go-ahead, eigen PR |
| 10. Origineel Berger 2008 §6 lezen | **HOGE PRIORITEIT / OPEN** | Als aparte derde bronlees-sessie mogelijk |

## 7. Multi-session agreement

Agent **Science** en agent **Notebook** hebben elk een eigen context/snapshot en een eigen GitHub-branch/PR. Laat een sessie zijn **besluit/evidence/handoffs met permalink en SHA** schrijven. De andere moet **expliciet opnieuw lezen**, niet vertrouwen op automatisch gedeelde chats. Zij kunnen elkaar niet hier zelfstandig berichten. De gebruiker start Work-sessies zelf; **geen** start of voltooiing is uitgevoerd door dit document. Een aparte Berger-lezer is optioneel. [Kort startdocument](../notes/session_handoff_radial_notebook_and_parallel_work_2026_10_19.md).

## 8. Status

**MAP IS CONCEPT.** Geen modelrun uitgevoerd, geen GitHub Actions gestart, geen onafhankelijke auditor actief, geen fysische parameter geijkt en geen definitieve notebookconfiguratie door gebruiker goedgekeurd. Grensvoorwaarde buitenrand en radiaal profiel wél uitdrukkelijk van gebruiker afkomstig. K niet volledig geëvalueerd; L/M onbesproken.
