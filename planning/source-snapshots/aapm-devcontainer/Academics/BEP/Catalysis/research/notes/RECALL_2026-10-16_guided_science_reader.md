# BEP — actieve terughaalronde gesprek 16 oktober 2026

**Status:** reconstructie uit de zichtbare gebruikersberichten van deze ChatGPT-conversatie en vergelijking met de bestaande repositorydocumentatie. **Geen woordelijke transcript-export, geen wetenschappelijke verificatie en geen impliciete gebruikersgoedkeuring.** De oorspronkelijke Gemini-conversatie over de paper-browser van 22 september is wel afzonderlijk woordelijk gearchiveerd: [historische chat](../../0_Project_Management/archive/transcripts/dynamic_kinetics_dashboard_transcript_2026-09-22.md).

**Hoofdwaarschuwing aan een volgende agent:** de wens is NIET slechts "lees papers met mij". De gebruiker wil (a) opnieuw zelf eigenaar zijn van de wetenschap, (b) een referentiemodel en gepubliceerde resultaten doelbewust reproduceren en (c) een interactieve paper-reader met een tijdens het gesprek veranderende, brongebonden AI-sidecar. Geen van die drie mag de andere wegdrukken.

## A. Wat er in de BEP-wetenschap is besproken

1. **Reproductie is zelf een mijlpaal.** De gebruiker corrigeerde de formulering waarin dit slechts als een voorbereidende check klonk. De vier afzonderlijke bewijsstadia voor het BEP zijn:
   - numerieke verificatie van de bedoelde vergelijkingen;
   - reproductie van een gepubliceerde modelberekening bij gelijke input;
   - overeenstemming met daadwerkelijk experimentele meetdata onder vergelijkbare condities;
   - onafhankelijke validatie of voorspelling buiten de voor parameterfitting gebruikte condities.
   **Open checklist**, liefst voortgang in komende weken en uiteindelijk voor de thesis; geen harde volgende-week-deadline. De gebruiker dacht hardop dat de eerste twee al behaald waren: **niet stilzwijgend als feit overnemen**. Interne tests en source-transcriptiereceipts zijn geen volledige reactorresultaatreproductie.

2. **Code moet een concrete wetenschappelijke functie hebben**, niet alleen een getal genereren. De huidige 2019 reagerende vertical slice is nuttig als beperkte test en basis voor gepubliceerde reproductie. De opgeslagen circa 9,3% acetyleenconversie en circa 77% netto ethyleenselectiviteit zijn niet bewezen dezelfde meting als een experiment bij exact gelijke condities. Eerst een betrouwbare referentie, pas daarna periodieke resultaten fysisch interpreteren.

3. **Beoogde integratie in het bestaande framework, niet oneindig nieuwe slices.** De gebruiker was verrast dat een afzonderlijk reagerend model gemaakt was; hij heeft zijn bestaande framework ("model 1", elders "model 3") zelf nog amper gelezen. De 2019-componenten zouden uiteindelijk in dat framework moeten worden geïntegreerd, na controle en correctie van dat framework. De 2022-transiënte oppervlaktekinetiek eveneens, tenzij een aantoonbaar technisch verschil een andere architectuur vereist. Een geïsoleerde testmodule is prima, maar **geen derde parallel reactorframework als default**. Dit is een gebruikersintentie, geen bewezen technische ontwerpbeslissing.

4. **Urmès 2022 is inhoudelijk relevant** wegens dynamisch oppervlak/geheugen, maar vereist controle van het werkelijk gepubliceerde mechanisme, parameters en aard van de inputmodulatie. Niet doen alsof een illustratieve 7-stapsmodule de gepubliceerde modelresultaten al reproduceert. De 2019-reproductie en het begrijpen van 2022 zijn afzonderlijke doelen die mogelijk de komende week/weken worden opgepakt, zonder onrealistische deadlines.

5. **Interessante maar voorlopig geparkeerde vragen:** numerieke amplitude-attenuatie en faseverschuiving bij periodieke toevoer, pelletradius en expliciete pelletdiffusie, een verdeling van de korrelgroottes, massaconservatie bulk/pellet, overeenstemming van feed/geometrie/support/kinetiek met de paper. De oude extreem trage diffusietijdschaal was een eenhedenbug: ingetrokken, niet als fysisch resultaat blijven circuleren. De eerdere circa 27,9% amplitudedemping komt uit een analytische zuivere upwind-advectionschets en is geen geverifieerde reactoruitkomst. Geen extra prioriteitsverhoging.

6. **E/F/G-discussies versus presentatiebestanden.** De gebruiker heeft in chat E, F en G besproken/becommentarieerd/onderschreven, maar weet niet of de uiteindelijke AI-versies exact zo verwoord zijn. Dat is geen aanleiding de gespreksgoedkeuring te wissen. PR #4 is gemerged maar de slide-presentatie is **niet** door de gebruiker goedgekeurd. K slechts gedeeltelijk besproken; L/M nog niet door de gebruiker geëvalueerd. Technisch mergen =/= wetenschappelijk instemmen.

## B. De werkverdeling en het risico van AI-verdichting

De gebruiker omschreef een **expansieproces** (vraag → tientallen bronnen → ideeën → analyses) en vervolgens **convergentie** (kiezen → thesiswaardig argument → concept/document/presentatie). Veel werk in het brede midden is geschikt voor AI. Menselijke input is belangrijk aan het begin, **bij een vroeg, compact wetenschappelijk selectiemoment vóór het eindproduct**, en bij een controleerbaar eindresultaat. Niet pas voor het eerst bij slides, maar ook niet noodzakelijk elke AI-tussenstap volledig zelf lezen.

Het grootste risico is dat een AI-herschrijving **de fundatie ongemerkt verwisselt**, waardoor omliggende uitleg of argumenten verdwijnt als één detail wordt gecorrigeerd. De gebruiker beschreef dit met een Indiana-Jones-vergelijking. Daarom steeds duidelijk scheiden:
- oorspronkelijke gebruikersuitspraak (liefst woordelijk, speech-to-text kan fout zijn);
- expliciete gebruikerscorrectie of door de gebruiker onderschreven interpretatie;
- passage/claim van de paper;
- interpretatie, analogie of hypothese van de AI;
- wetenschappelijk bewijs, vraag en downstream-afhankelijkheid.
Een verbeterde formulering is niet vanzelf door de gebruiker onderschreven. Versies en afhankelijkheden moeten herstelbaar zijn, niet stilletjes herschreven.

Concreet transcriptievoorbeeld: de gebruiker vroeg **of** oudere PR's teruggedraaid moesten worden. Een eerdere speech-to-text-/AI-interpretatie maakte ervan dat ze **al** waren teruggedraaid. Dit is gecorrigeerd: er was geen door de gebruiker gemelde revert. Jira was een grap en geen keuze voor een extra ticketsysteem.

De gebruiker wil **geleid hardop denken** ("guided yapping") en zelf papers, vergelijkingen en argumentaties gaan begrijpen; niet eerst verplicht een uitgebreide LaTeX-/Markdown-tekst maken. De huidige grote hoeveelheid AI-notities is referentiemateriaal, niet automatisch eigen begrip of thesiswaardig bewijs. Een vraag/figuur/equation samen lezen kan waardevoller zijn dan een nieuwe autonome analysesprint.

## C. De reader is méér dan een PDF plus chat

De chat verwijst naar Zotero (PDF en soms HTML), een bestaande PDF-annotatiewatcher, de BEP-paper knowledge graph, een Harness-chatgraaf, een oudere Gemini-dashboardschets en de aantrekkelijke Methanol-Catalysis/Pixi-preview als mogelijke UX-inspiratie. Dat zijn bouwstenen, **niet** het bewijs van één werkende geïntegreerde applicatie.

De gevraagde leesomgeving:
- toont de **echte brontekst**, met hoofdstuk/subsectie/alinea/zinsnavigatie, highlights en links naar formules, figuren en citaties;
- zet *relevante* AI-uitleg en eigen annotaties **precies bij de gelezen passage**, met herkomst en herzienbare status, en laat die informatie tijdens een gesprek mee veranderen;
- bewaart de optionele navigeerbare zoom-/floating-balls-kaart en de niet-hiërarchische "rabbit holes" naar aangehaalde papers, zonder honderden gelijkwaardige bubbles te tonen;
- beschouwt citations niet louter als bibliografische nummers: interessant is **welke rol de geciteerde bron in dát argument van de auteur speelt**. Een door AI voorgestelde "citation intent" blijft een interpretatie totdat een bronpassage het ondersteunt;
- houdt later bij wat door de gebruiker zelf is gelezen, alleen door AI geanalyseerd, onbegrepen, belangrijk of door de gebruiker onderschreven.

De bestaande gegenereerde literatuurtracker toont soms **Verified** bij meerdere AI-analyseruns plus consensus. Dat mag niet worden verward met "gebruiker heeft paper gelezen", "alle claims tegen de primaire bron gecheckt" of "experimenteel gevalideerd".

**Werkelijke productstand:** [VISION](../../Articles/reader/VISION.md), [reader prototype](../../Articles/reader/README.md), [reader-state](../../Articles/reader/state.md). De HTML-demo is nog geen echte Zotero-importer; het periodiek inlezen van een JSON-sidecar is nog geen live koppeling met de ChatGPT-chat/dictatie. Geen van die externe koppelingen als afgevinkt melden.

### Relatie met de eerdere reconsolidatie (apart en op PR #8)

De andere Work-agent schreef al [reconsolidation_capture_2026-10-16.md](https://github.com/AsapLoso/project-management-agents/blob/bep/reconsolidation-2026-10-16/Academics/BEP/Catalysis/research/notes/reconsolidation_capture_2026-10-16.md) en een [Wayfinder voor numerieke nauwkeurigheid](https://github.com/AsapLoso/project-management-agents/blob/bep/reconsolidation-2026-10-16/Academics/BEP/Catalysis/research/wayfinder/bep_dynamic_numerical_accuracy.md) op branch **bep/reconsolidation-2026-10-16**, PR #8 (bij het controleren op 16 oktober nog **open**, dus niet in devcontainer). Die notitie bevat veel letterlijke fragmenten over de vertical slice, diffusietijdfout en massabalans. **Niet dupliceren alsof dit allemaal pas hier voor het eerst is vastgelegd.** Deze nieuwe recall richt zich op de *latere* uitgebreide discussie over onderzoekseigenaarschap, 2019/2022-integratie, goedkeuringen en de daadwerkelijk gewenste paper-reader. Bij toekomstig samenvoegen moeten de twee bronrecords naast elkaar blijven en inhoudelijk worden vergeleken.

## D. Waar de oude notitie te kort schoot

De huidige VISION registreert veel technische readerwensen, maar bevat de **wetenschappelijke vierstappenchecklist**, de **één-framework-intentie**, **verschillende approval-niveaus**, de **expansie/convergentie-checkpoints**, het specifieke **waarom van citaten**, en de speech-to-text **revert-correctie** niet allemaal als samenhangend en herleidbaar gespreksrecord. Deze notitie vult dat aan; hij overschrijft VISION en oudere audits niet.

Ook deze active recall is **niet uitwisselbaar met een volledige export van alle ChatGPT-gebruikersberichten**. Behandel hem als startpunt om later concrete gebruikersuitspraken en bronstukken afzonderlijk te herleiden.

## E. Minimale eerstvolgende proef

Neem **één bestaand werkelijk artikel**: verifieer citekey en PDF/HTML-versie, kies één paragraaf met vergelijking of bronverwijzing, en toon in een bruikbare reader:
(1) die echte paragraaf,
(2) één bronverankerde **eigen gebruikersnotitie**,
(3) één expliciet daarvan gescheiden **AI-uitleg**,
(4) een klikbare **bronverwijzing** met het doel dat de auteurs daar aan die referentie geven.
Het is geslaagd wanneer je terug kunt navigeren, de oorspronkelijke woorden onveranderd blijven en ontbrekende bronrelaties als *onzeker* zichtbaar zijn. Geen verplicht nieuw framework of nieuwe hele site.

Technische specificatie voor het minimale parse-output: [PARSING_SPINE](../../Articles/reader/PARSING_SPINE.md).
