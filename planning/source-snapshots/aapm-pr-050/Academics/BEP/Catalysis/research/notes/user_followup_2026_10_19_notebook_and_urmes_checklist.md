# Gebruikerscorrecties en checklist voor volgend BEP-bericht — 19 oktober 2026

> **LATER DEZELFDE AVOND — MODELGRENS GEKOZEN:** radiale pellet niet uniform, instantane buitenrand c_p(R)=C_b door géén externe filmweerstand, binnenste finite radial diffusion met voorstel tau_diff 5–30ms (voorbeeld 10ms). Radius en tau niet onafhankelijk bij gefixeerde D_eff. [Handoff/gesprekslog](session_handoff_radial_notebook_and_parallel_work_2026_10_19.md) en [Notebook Delivery Wayfinder](../wayfinder/bep_reactor_notebook_delivery_2026_10_19.md); de gebruiker wil eventueel twee aparte Work-sessies en Berger §6 mogelijk als derde, **niet automatisch starten**.


> **LATERE 19-OKTOBER-AANVULLING — HOGE LEESPRIORITEIT:** Gebruiker wil het fysische onderscheid **snelle gas/pore diffusie ≠ snelle oppervlakteadsorptie/-reactie** zelfstandig doorgronden, met nadruk op **Berger 2008 §6**. [Brongebaseerde gerichte leeskaart](PRIORITY_reading_2008_s6_transport_vs_surface_memory_2026_10_19.md). Dit is een nieuwe prioriteit, geen afgeronde inhoudelijke evaluatie van K/L/M.


> **NIET VOLLEDIG GEËVALUEERD — K; L EN M NOG NIET BESPROKEN.**
>
> **Bron:** gebruikersbericht van rond 00:40 (Europe/Amsterdam), 19 oktober 2026. Handmatig samengevat; het oorspronkelijke chatbericht blijft de letterlijke bron. **Geen inhoudelijke beantwoording van de 2019-vraag in deze notitie.**
>
> **Belangrijk:** deze aanvullingen corrigeren de interpretatie van [de Thought Dump van 18 oktober](user_thought_dump_2026_10_18_reactor_recovery.md) en het [47-puntenregister](../dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md). Ze zijn **niet** de bevestiging dat alle eerdere punten opgelost zijn.

## Primaire herformulering van het doel — door gebruiker

- **[USER CORRECTION]** De eerdere lijst “wat verlangen we van het model” is grotendeels een lijst **pre-implementatie-randvoorwaarden** (fysica, methodologische verificatie, validiteit) en dus **niet** het eigenlijke gewenste gebruiksresultaat.
- **[USER INTENT]** Het model moet de **onderzoeksvraag helpen beantwoorden met inzichtelijke plots** van de systeemrespons op gekozen inputs. Bedrijfscondities en signaalvormen moeten eenvoudig aanpasbaar zijn.
- **[USER INTENT]** Voorkeursvorm is **een Jupyter-notebook** met samenhangende afbeeldingen/plots, kleine herbruikbare subcodes en **plug-and-play**-configuraties, zoals het eerste model maar beter gestructureerd. Geen gecompliceerd eindproduct bouwen voordat de basale onderzoekservaring werkt.
- **[USER INTENT]** Analyse van een voldoende ingeregelde respons over de **laatste complete perioden**, bijvoorbeeld drie, met een gemiddelde. Sinusfit kan helpen maar hoeft niet altijd; inspectie van de figuren is belangrijk. Een niet-lineair systeem kan een niet-zuivere sinus opleveren. Aantal perioden, sample-rate en statistische precisie moeten adequaat zijn maar worden niet als reeds vastgesteld voorgeschreven.
- **[USER CORRECTION]** Ruimte- en tijdresolutie plus voldoende punten per golfperiode zijn voor de gebruiker **standaard numerieke checklistcriteria**, niet het speciale doel van deze onderzoeksfase of een verrassende ontdekking.

## Nog niet begrepen / te verduidelijken zonder nu de vraag te beantwoorden

- **[USER QUESTION]** Waarom geven eerdere checks **10 van 12** coverage-range matches? De gebruiker wil strikt scheiden tussen gevallen die volgens expliciete criteria **binnen** het geldigheidsgebied liggen en extrapolaties of gevallen buiten het domein. Hij suggereert daarom bijvoorbeeld een **10/10 within-domain** score mits een onafhankelijke broncontrole de afbakening rechtvaardigt. **Niet zonder nader onderzoek 10/12 omboeken naar 10/10**; dit is een *te toetsen voorstel*.
- **[USER QUESTION]** Waar kan de grens van het bruikbare **parameterdomein** werkelijk liggen en in welke mate leert die ene testcase daar iets over? Niet beweren dat twee afwijkende coverages automatisch buiten de T/P-domain lagen.
- **[USER QUESTION]** Wat betekent concreet dat oppervlaktebedekkingen uit het bestaande **pbr**-framework “niet aan de gasreactiesnelheid teruggekoppeld” zijn? Volgende keer eenvoudig uitleggen met de benodigde functies, toestanden en afhankelijkheden; geen jargon herhalen zonder formule.
- **[USER SCIENTIFIC JUDGEMENT]** De 2019 PSSA/steady-rate-baseline wordt voor de **oorspronkelijke dynamische oppervlaktedoelstelling** als onvoldoende ervaren: gebruik hooguit als stationaire of gereduceerde vergelijkingscase tegenover 2022. Niet verwarren met de onjuiste claim dat een PSSA-gasreactor **geen enkele** tijdsafhankelijke gasrespons kan simuleren.
- **[USER QUESTION — EXPLICIET UITGESTELD]** **“Wat maakt het Urmès-2019-papermodel eigenlijk zo bijzonder?”** Niet in dit antwoord beantwoorden. Zet dit op de checklist voor het **volgende** inhoudelijke bericht en vergelijk dan 2019 met 2022 en het onderzoeksdoel; begin bij wat het *wel* en *niet* modelleert.
- **[USER QUESTION]** Er zijn **vier reagerende gasvariabelen** H₂, C₂H₂, C₂H₄ en C₂H₆. De gebruiker probeert de **drie versus vijf oppervlaktebedekkingen** en de plaats van een inert gas zoals Ar te reconstrueren. Dit zijn **verschillende grootheden**; analyseer opnieuw de daadwerkelijke state-layout en het mechanisme, zonder nu een “vijfde” chemische soort te raden of Ar tot dynamische surface coverage te verheffen.
- **[USER INTENT]** De grote eerdere kritiekpunten zijn nog niet verwerkt in de nieuwe code. Een **tweede reviewpass** blijft noodzakelijk; eerdere F/G/E-audits en het oorspronkelijke model moeten daarin actief worden vergeleken met de nu gepushte pbr-code.

## Nieuwe, gecontroleerde GitHub-feiten

- **[CODE VERIFIED, 19 oktober 2026]** [AsapLoso/Methanol-Catalysis/main/pbr](https://github.com/AsapLoso/Methanol-Catalysis/tree/main/pbr) **bestaat nu wel**. GitHub Contents geeft `model.py`, `solver.py`, `chemistry.py`, `closures.py`, `discretisation.py`, `parameter_sets.py`, `parameters.py`, `provenance.py`, `species.py`, `sweep.py` en `__init__.py`.
- **[CODE VERIFIED]** Onder `tests/` staan `test_discretisation.py` en `test_solver.py`. Onder `.github/workflows/` staan op dit moment `deploy.yml` en `deploylatex.yml`, **nog geen geverifieerde wetenschappelijke PBR-simulatie-GitHub Action**. Bestaan van bestanden is **geen bewijs dat tests of een notebook al draaien**.
- **[CODE VERIFIED]** De gelezen `main` HEAD is `5400881b3d06164db10488abae27b110ac618258`. [Repository](https://github.com/AsapLoso/Methanol-Catalysis). De vorige notitie dat `pbr/` op remote `main` ontbrak is **historisch achterhaald**.
- **[PENDING]** Controleer of lokale/source snapshot van het oude framework exact gelijk is aan huidige remote code; eerst diff/smoke/requirements en source/units, dan pas een modellerings- of CI-PR.

## EÉN CHECKLIST VOOR HET VOLGENDE INHOUDELIJKE BERICHT

- [ ] **Beantwoord de uitgestelde hoofdvraag:** *Wat maakt Urmès 2019 bijzonder, en wat is het onderscheid met Urmès 2022 voor ons doel?* Begin daarmee, in begrijpelijke termen.
- [ ] Leg kort en concreet uit welke **vier gascomponenten** en welke **drie/vijf site-coverages** het model bevat; waar past het inerte Ar, en wat is een fysische toestand versus een parameter?
- [ ] Laat in één eenvoudig formuletje/codeverwijzing zien wat **gasrates niet van θ afhankelijk** betekent, en waarom dat het beoogde surface-memory-experiment beperkt.
- [ ] Controleer de werkelijke broncondities achter **10/12 coverage-range matches**; definieer alleen na bronverificatie het verschil tussen *within-domain* en *out-of-domain*, en welke conclusie over de grens verantwoord is.
- [ ] Gebruik de inmiddels **gepushte pbr-code** als bron van waarheid voor volgende modelinspectie; controleer welke configuraties en tests er echt in zitten en wat ontbreekt.
- [ ] Ontwerp een **plug-and-play notebook** vanuit de onderzoeksplots en inputs (full transient trajectories, laatste ingeregelde cycli, gemiddelden/harmonischen indien nuttig), zonder alle standaardverificatie-eisen tot de doelstelling te verheffen.
- [ ] **Tweede pass** door het eerdere uitgebreide gebruikerscommentaar en de 47 punten: wat is al aanwezig, wat nog niet; behoud alle open statuspunten en claim geen implementatie zonder bewijs.

**Status:** **ALLE VRAGEN NOG OPEN VOOR VOLGEND BERICHT — 2019-VRAAG HIER EXPRES NIET BEANTWOORD.**
