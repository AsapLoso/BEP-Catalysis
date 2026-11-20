# 19 oktober 2026 — Science-first notebook, modelkeuze, twee Work-sessies (concept-handoff)

> **BELANGRIJKE GEBRUIKERSCORRECTIE — 19 OKT, LATER DIE NACHT.** De **eerste** gevraagde onderzoeksvraag is concreet: **blijft de gesimuleerde respons gelijk voor verschillende combinaties van pelletstraal \(R_p\) en effectieve diffusiviteit \(D_\mathrm{eff}\) met dezelfde verhouding \(R_p^2/D_\mathrm{eff}\)?** Dit is een **schaalvergelijking/invariantietest**, niet primair een algemene discussie over meetbaarheid of over het mogen schrappen van de radiale dimensie. De eerdere vraag “is de radiale dimensie aan de outlet zichtbaar?” blijft hooguit een **optionele vervolgvraag**. Verder is een **verdeling van pelletgroottes** een **latere hypothese**, niet nu een engineeringticket of vereiste notebookoptie. De 5–30 ms zijn slechts een eerdere schatting.

> **Update voor science Work-agent:** begin waar mogelijk met een *dimensionele verificatie/invariantietest* met meerdere R²/D-constante pelletparen, na controle van de conservatieve bulk–pellet-koppeling. De eerder genoemde brede “is de tweede dimensie waarneembaar aan de outlet?” vraag is nu een **volgende** vraag, geen door de gebruiker gekozen eerste stap. [Uitwerking en verdelingshypothese](2026_10_19_radial_observability_and_reduction.md).


> **NIEUWSTE SCIENCE-HANDOFF (19 OKT):** Onderzoek **of radiale pellettijdschalen en ruimtelijke concentratieprofielen zichtbaar zijn in de berekende reactor-outlet**, en vergelijk full radial tegen een conserverende lumped diffusiebenadering en een instant uniforme limiet. **Een vereenvoudiging die outletrespons voor relevante inputs behoudt, is een gewenst resultaat.** De 5–30ms/tau-slider uit oudere zinnen hieronder is slechts een ruwe verkenningsschatting, **niet** een opgelegde eigenschap of notebookrange; primaire (R_p,D_{eff},epsilon_p) kiezen op fysische bronbasis, tau berekenen en respons uit simulatie afleiden. [Nieuwe experimentele testvraag en Kim 2008-literatuur](2026_10_19_radial_observability_and_reduction.md). **Science-agent moet experiment/modelvergelijking uitvoeren**; Notebook-agent visualiseert en implementeert enkel de onderbouwde modelopties.


> **CORRECTIE — GEBRUIKER 19 OKTOBER 01:50:** Het 'stappenplan' is **de concrete taak van een tweede, werkende wetenschappelijke Work-agent**, niet een extra passieve roadmap. Agent A moet de stappen uit deze avondhandoff **doorlopen en uitvoeren op een beperkte wetenschappelijke slice**, met bron- en codebewijs, en daarna de volgende keuze vastleggen. De oudere kopieerprompt hieronder met 'implementeer niets' is **te passief**: liever minimaal fysische bulk↔pore-koppeling auditen, zelfstandig derivatie + reproduceerbare beperkte test als veilig, eigen PR/receipt. Agent B werkt aan de notebook zodra deze keuze helder is. [Concrete primaire filmweerstandbron, diffusie-advies en gap-audit](followup_2026_10_19_film_diffusion_agent_gap_audit.md). Berichten tussen chats verlopen niet direct: plaats GitHub-handoff op issue #58/PR en meld permalink in eigen Work-chat; B moet herladen. **NOG GEEN EXTERNE SESSIES GESTART.**


> **SNAPSHOT VOOR VERVOLGSESSIES, NIET EEN GESTARTE AUTONOME JOB.**
>
> Dit is de kopie van de **tot nu toe besproken** stand van wetenschap, intentie, open keuzes en avondstappen. Latere sessies moeten de live repo opnieuw lezen. Dit document is **geen vervanging** van de 18-oktober-userwoorden en het 47-puntenregister. **K gedeeltelijk besproken, L/M nog niet besproken.**

## Door gebruiker inmiddels helder gekozen

- **Primair doel:** mooi, bruikbaar, modulair **Jupyter-notebook** voor eigen BEP-onderzoek: inputvariaties → uitvoerbare reactormodellen → duidelijke plots (inlet/outlet tijd, langs de reactor, radiale pellet en laatste ingeregelde volledige cycli). Herbruikbare submodules, parameters in één configuratieblok, geschikt om met Damian te bespreken. **Niet** een nieuw presentatie-deck; ook niet het afvinken van 47 researchcriteria als eindproduct.
- **Fysische uitgangskeuze:** **radiaal niet uniform**. Pellet buitenlaag neemt de *lokale* bulkconcentratie direct aan (geen externe filmweerstand), **binnenste pelletdiffusie is eindig**; midden nul-gradiënt. Bij gekozen bolgeometrie: c_p(z,R_p,t)=C_b(z,t), ∂_r c_p(z,0,t)=0, epsilon_p·∂_t c_p = D_eff·r⁻²∂_r(r²∂_r c_p)+reactiebron. **De bulkbalans moet de bijbehorende interfaciale flux ontvangen; anders ontbreekt gasinventaris.**
- **Voorgesteld voor exploration, NIET experimenteel bepaald:** karakteristieke radiale diffusietijd circa **10 ms**, range **5–30 ms**, mogelijk als slider. \(\tau_{\rm diff}\sim\epsilon_p R_p^2/D_{\rm eff}\); bij \(R_p\) en gewenste tau als aparte bediening moet \(D_{\rm eff}\) worden afgeleid. Als \(D_{\rm eff}\) fysiek constant blijft, is tau géén onafhankelijke slider. Bij gevarieerde porositeit/tortuositeit opnieuw units en diffusiviteit consistent houden.
- **Geen filmbegrenzing** is hier een modelling choice over *extern transport*. Dat is **niet** hetzelfde als instantane radiale diffusie, en zegt nog **niets definitiefs** over onafhankelijke dynamiek van oppervlaktebedekkingen. De gebruiker wil het niet onnodig tot een filosofische hoofdonderzoeksvraag uitvergroten; leg de keuze eenvoudig uit.
- **Relevante code staat online:** [Methanol-Catalysis/main/pbr](https://github.com/AsapLoso/Methanol-Catalysis/tree/main/pbr) is sinds de laptopsync gepusht. Lees opnieuw de files, methode, tests en workflows. Het vorige bericht “remote heeft geen pbr/” is **stale**.
- **Separate reading priority:** Berger (2008), **sectie 6** volledig; dit is hoge wetenschappelijke leesprioriteit maar niet automatisch op het kritieke pad van de notebook. [Leeskaart](PRIORITY_reading_2008_s6_transport_vs_surface_memory_2026_10_19.md). 2019 vs 2022 source-specific verschil eveneens open.

## Welke wetenschappelijke stappen zijn al gemaakt?

1. Proposal en oorspronkelijke 11 fysieke veldtypen gedocumenteerd (4 bulk + 4 pore + 3 surface), met experiment 5 surface soorten (=13 velden), grotendeels zonder gevalideerde actieve chemie.
2. Berger/2019/2022 en transport/kinetiek in bestaande research dossiers geïnventariseerd; E/F/G analyses bevatten echte open fysische/numerieke punten.
3. Reacting Hermes-prototype gebouwd als gereduceerde uniform-pellet 2019-PSSA-baseline; 17/17 *eigen beperkte gates* PASS, maar fysisch resultaat en periodieke observabelen **niet gevalideerd**.
4. Gebruiker heeft de methodologische reductie bekritiseerd; [thought dump](user_thought_dump_2026_10_18_reactor_recovery.md) en [47-puntenregister](../dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md) bestaan, externe auditor nodig.
5. Bestaande uitgebreidere pbr-module door gebruiker vanaf laptop gepubliceerd, op remote bevestigd.
6. Gebruiker corrigeert gewenste output naar **plug-and-play notebook met mooie onderzoeksgrafieken**, niet verificatierapporten als doel.
7. Huidige keuze: **geen externe film, wel finite radial diffusion**. Radiale binnen-tijdschaal 5–30ms is een **hypothese voor experiment**, niet geijkt.

## Wat besluiten/doen we de rest van deze avond?

- **Deze beurt:** structuur van twee gekoppelde kleine Wayfinderdoelen + 47-item auditregister, expliciet user-inhoud vastleggen, twee compacte Work-handoffs voorbereiden. **Geen simulatie starten of public code wijzigen.**
- **Volgende inhoudelijke keuze:** wat is het minimale figuursetje in eerste notebook? Default kan vier species inlet/outlet, radial heatmap/profielen, axiaal profiel en drie laatste volledige cycli (alleen als werkelijk ingeregeld) zijn; wijzigingen plug-and-play.
- **Wetenschappelijk minimum:** laat een research agent bestaand pbr-pellet RHS & bulkflux tegen F-conservation en source/BC checken; beslis daarna of de eerste versie radiaal + PSSA als duidelijk gelabelde tussenmijlpaal mag zijn of expliciete werkende θ-terugkoppeling vereist. **De gebruiker heeft dat laatste nog niet definitief beslist.**
- **Work na go-ahead:** notebook bouwen met source-preserving modules, echte runs/figuren, contrast input/outlet, radial \(c_p(z,r,t)\), convergentie over volledige cycli en expliciete fysische disclaimers; tests, artifacts en PR.
- **Parallel vrijstaand:** originele Berger 2008 §6 leesagent, die een citeerbaar verslag met exacte figs/equations maakt. Het mag de notebook niet uitstellen zonder aangetoonde dependency.
- **Na beide rapporten:** onafhankelijke tweede pass op alle 47 punten, ga na of iets verkeerd uit eerdere F/G of de gereduceerde Hermes-route is overgenomen; de wetenschappelijke rapporten bepalen toekomstige tickets, geen automatische closure.

## Overdrachten: twee onafhankelijke chats kunnen niet automatisch met elkaar spreken

**Beide sessies kunnen gedeelde repo-documenten als source-of-truth gebruiken**, maar hebben geen automatische toegang tot elkaars chat, en een sessie kan niet vanzelf een andere informeren. Vertel de uitvoerder daarom: **schrijf aan het einde een gedateerde handoff (in een eigen branch/PR of als issuecomment op #58) met status, SHA, links, beslissing/niet-beslissing, testreceipts, blockers. Maak expliciet zichtbaar wat de andere sessie moet inlezen.** De gebruiker kan het PR-/issueadres aan de andere sessie doorgeven. Een andere sessie moet de actuele state opnieuw fetch'en vóór zij verdergaat. Geen automatische berichten of achtergrondwerk gesuggereerd.

### Kopieerbare korte opdracht A — wetenschappelijke tweede pass (zonder code)

> Bekijk in Work de BEP-science Wayfinder en de nieuwe Notebook Delivery Wayfinder op branch research/bep-K-results-review-2026-10-18 in AsapLoso/project-management-agents. Lees het 47-puntenregister en de 19-oktober handoff. Inspecteer de nu gepushte Methanol-Catalysis/main/pbr-code. Focus op de gekozen **niet-uniforme pellet met instantane buitenrand en eindige interne diffusie**, de koppeling van gas/pore flux en het onderscheid PSSA/actuele θ-terugkoppeling. Stel de concrete besluitvragen en onafhankelijke fysieke/codebevindingen vast; **implementeer niets en herhaal niet alle 47 punten**. Gebruik de bestaande Wayfinder-tickets, schrijf een korte citeerbare handoff/PR met exacte bronlocaties, doe geen definitieve gebruikerskeuzes zelf. Meld het resultaat in deze Work-chat en geef een permalink voor overdracht aan de notebook-sessie.

### Kopieerbare korte opdracht B — notebook-ontwerp (bouwen pas na gebruikersakkoord)

> Lees de Notebook Delivery Wayfinder en 19-oktober handoff in AsapLoso/project-management-agents, plus de live Methanol-Catalysis/main/pbr. Ontwerp de **kleinst mogelijke modulaire plug-and-play Jupyter-onderzoekssessie** met fraaie, fysisch eerlijk gelabelde input/output- en radiale pelletresponsplots, en analyse van ingeregelde volledige perioden. **Neem geen uniforme pellet als vervanging aan**: buitenrand instantaan gekoppeld aan bulk, binnenin eindige radiale diffusie. Gebruik verkennings-tau 5–30 ms alleen als expliciet hypothetisch; straal en diffusiviteit zijn gekoppeld. Vraag om gebruikersakkoord op de minimale modelvariant vóór je de volledige implementatie bouwt. Raadpleeg de nieuwste science handoff voordat je fysische codekeuzes neemt. Maak eigen branch/PR, log echte runs/tests/blokkades; rapporteer in deze Work-chat en op GitHub zodat de andere agent de laatste stand kan herladen.

### Optionele, afzonderlijke opdracht C — literatuur, geen code

> Bestudeer de volledige originele Berger et al. (2008), Dynamic methods for catalytic kinetics, sectie 6, vooral §6.2, §6.4, §6.6 plus §4/Table 2. Gebruik repo-literatuurwerk slechts als routekaart, verifieer primaire originele vergelijkingen, figuren en pagina's. Leg uit hoe externe gasaanvoer, interne diffusie en dynamische oppervlaktesite-inventaris afzonderlijk kunnen bijdragen; vergelijk waar relevant Urmès 2019 vs Urmès 2022. Maak een wetenschappelijk citeerbaar leesrapport op een eigen branch/PR met exact bronbewijs en open vragen. **Verander geen simulator.** Rapporteer expliciet aan de gebruiker en verwijs naar je permalink.

**STATUS:** alleen planning + handoff, geen Work agent gestart of voltooid. Geen onterechte closure van K, L of M.
