# 19 oktober 2026 — externe film, diffusieslider en tweede agent: feedback- en gap-audit

> **INHOUDELIJKE GEBRUIKERSCORRECTIE / NOG NIET VOLLEDIG UITGEVOERD.** K gedeeltelijk geëvalueerd; L/M niet inhoudelijk besproken. Dit document vormt een vervolg op [18 okt Thought Dump](user_thought_dump_2026_10_18_reactor_recovery.md), [19 okt notebookcorrectie](user_followup_2026_10_19_notebook_and_urmes_checklist.md), [47-puntenregister](../dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md), [Wayfinder notebook](../wayfinder/bep_reactor_notebook_delivery_2026_10_19.md), [avond-handoff](session_handoff_radial_notebook_and_parallel_work_2026_10_19.md).

## 1. Concrete primaire vindplaats voor Damian — rechtstreeks gecontroleerd

**Urmès et al. (2019), §3.1, Table 7, gedrukte p. 10 (cover-PDF p. 11),** [officiële primaire PDF](https://mdpi-res.com/d_attachment/catalysts/catalysts-09-00180/article_deploy/catalysts-09-00180-with-cover.pdf?version=1686479401) / [DOI](https://doi.org/10.3390/catal9020180). Tabel 7 titel: criteria for the absence of mass and heat transfer limitations; originele tabel visueel gecontroleerd in huidige beurt.

- **External MASS transfer (Carberry): 3.3 × 10^-4 < 0.05**.
- **Internal MASS transfer (Weisz–Prater): 1.7 × 10^-2 < 0.33**.
- **External HEAT transfer (film): 0.14 K < 1.1 K**. Dit laatste betreft warmtetransport en is niet identiek aan externe MASSAoverdracht; de eerste tabelrij hierboven is relevant voor de externe concentratiefilm.
- Uitleg §3.1: de authors gebruiken maximaal geobserveerde acetyleenverbruiksrate van 9 mmol/kgcat/s en Eurokin-criteria voor hun steady kinetische proeven. Dit bewijst niet automatisch dat de film in onze BEP-reactor onder elke forcing nooit relevant is.

**Kort gesprekspunt voor Damian (niet verstuurd):** “In Urmès 2019, §3.1 tabel 7 staan externe massatransfer (Carberry) en interne diffusie (Weisz–Prater) apart. Bedoelde je met mass transport limitations allebei? Wij willen de externe film verwaarlozen en de interne radiale diffusie juist dynamisch behouden. Is dat een verdedigbare afbakening voor onze case?”

**Berger et al. 2008, Table 2, gedrukte p. 11 / PDF p. 9** benoemt volgens [eerdere directe primaire PDF-inspectie](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md) ook de externe/interne en transient massaoverdrachtcriteria. De originele Berger-PDF is **niet opnieuw rechtstreeks gelezen** in deze beurt. [DOI](https://doi.org/10.1016/j.apcata.2008.03.020). Berger §6 wordt apart bestudeerd, geen automatische blokkade op notebookbouw.

## 2. Correcte interpretatie van 5–30 ms (geen exit-time zonder definitie)

**Modelkeuze van de gebruiker:** de buitenrand heeft direct de lokale bulk-gasconcentratie, c_p(R_p,t)=C_b(t); interne concentratie c_p(r,t) blijft ruimtelijk en dynamisch. In bolgeometrie geldt symmetrie ∂c_p/∂r|r=0=0. De interne diffusie is geassocieerd met Fickse Brownse microscopische beweging maar valt niet samen met een gemiddelde molecule-outlet-tijd.

**Aanbevolen startbediening voor notebook:** pelletstraal R_p en gewenste karakteristieke diffusietijd tau_D, bijvoorbeeld slider 5–30 ms met nominale 10 ms. Toon de afgeleide effectieve diffusiviteit D_eff = epsilon_p R_p² / tau_D, plus duidelijk “illustratief/niet uit bron gekalibreerd”. Voor fysisch geijkte modus later: independent R_p and D_eff, with tau_D derived. Indien R en tau onafhankelijk worden bediend, **verandert impliciet het gekozen materiaal-D**. Een echte gekoppelde reacting-pellet heeft ook Thiele/Da, oppervlak/volume en interfaciale fluxschaling; niet iedere output hangt uitsluitend van R²/D af.

**Pure diffusion step benchmark:** in een bol met direct opgelegde randsprong heeft de dominante tijdmodus een verval exp(-π²t/tau_D). Een ruimtelijk gemiddelde stapafwijking daalt in dat zuivere voorbeeld tot circa 5% na ~0.25 tau_D, maar dat is niet een gemiddelde molecular first-passage/exit-time en niet automatisch geldig met reacties.

Voor epsilon_p=0.5, R=75 μm en tau_D=10 ms: D_eff=2.8125e-7 m²/s; interpretatie uitsluitend exploratief.

## 3. Nog NIET goed behandeld in de vorige beurt

| Punt uit de gebruikersfeedback | Correcte status |
|---|---|
| Fysische keuze “niet uniforme pellet, directe rand, interne diffusie” | **Besproken en in map**, niet in code geïmplementeerd |
| Filmlimitatie: letterlijk vindplaats in bestaande papers | **Nu geverifieerd Urmès 2019 Tabel 7**; Berger via oudere directe-PDF audit |
| Voorstel voor Brownian/pellet responstijd 5–30ms | **Nu fysisch geduid en defaultbediening aanbevolen**, geen gemeten parameter |
| Vraag welke belangrijke vorige punten gemist waren | **Dit register vormt een expliciete correctieve gap-audit**, geen onafhankelijke 47-puntenaudit |
| Tweede agent “wetenschappelijke stappen daadwerkelijk maken” | **Handoff vereist herschrijving:** niet slechts plannen/map invullen, maar actief de volgende wetenschappelijke slice onderzoeken/uitvoeren |
| Tweede sessie met eigen kopie van beide kaarten en latest head SHA | **Als startup-check voor uitvoerende Work-agent vastleggen**, geen kopie van repo nu fysiek gemaakt |
| Andere ChatGPT informeren als klaar | **Niet automatisch tussen chats mogelijk**; wetenschappelijke agent schrijft GitHub Issue #58/PR permalink + SHA en meldt klaar in de eigen Work-chat, notebook-agent leest de actuele handoff opnieuw |
| Eventuele aparte derde Berger §6 reader | **Optioneel hoog geprioriteerd, geen automatische gestart**, eigen bibliografische bewijslijn |
| Work notebook met werkende wetenschappelijke plots | **Nog niet gestart**, geen overnight delivery geclaimd |
| 47-punten tweede pass en PR-review | **Open; onafhankelijke auditor nog niet aan het werk** |

## 4. Tweede agent = daadwerkelijke wetenschappelijke processtappen, niet plan-as-output

**Minimum work contract:**
1. Lees via repository-HEAD met SHAs de bestaande Scientific Method Selection Wayfinder, Notebook Delivery Wayfinder, Numerical Wayfinder, dit document en U01–U47; inspecteer live Methanol-Catalysis/main/pbr en tests.
2. Reconstructie: welke inhoudelijke stappen, modelleringen, verificaties en keuzes zijn aantoonbaar gedaan; welke claims blijven hypotheses; wat verandert door de nu gekozen directe pelletgrens?
3. Kies de volgende *uitvoerbare* niet-blocked wetenschappelijke slice uit de map. **Deze avond: check de reële gekoppelde bulk/pore RHS**, interfaciale diffusieflux, inlet/randcondities, en waar reacties dubbel geboekt kunnen zijn. Gebruik eerder F-rapport als hypothese, geen automatisch verdict.
4. **Doe daadwerkelijk wetenschappelijk werk**: onafhankelijke derivatie met units; code inspectie op exacte file/lines; indien uitvoerbaar beperkte test/run op de echte package op eigen werkbranch met receipt; beslis volgende keuze met bewijs. Maak dus niet alleen weer een nieuwe Wayfinderkaart.
5. Koppel bevindingen en concreet bewijs aan de bestaande kaart (geen kaartgroei om de groei), geef minimale actie/acceptatietest voor de notebook-agent.
6. Laat bij afronding op [issue #58](https://github.com/AsapLoso/project-management-agents/issues/58) of in een eigen PR een bericht achter: “FOR NOTEBOOK AGENT”, plus datum, branch, commit-SHA, wat gedaan en wat onveilig/onbewezen is. Meld de permalink aan de gebruiker in de eigen Work-chat. **Andere Work-agent moet actief opnieuw inlezen**. Er is géén automatische directe chat-chat-notificatie geïmplementeerd.

**Geen agent gestart, geen codepatch uitgevoerd, geen notificatie verzonden. Alle claims uit gebruikersfeedback moeten nog tegen 47-puntenregister onafhankelijk worden geaudit.**
