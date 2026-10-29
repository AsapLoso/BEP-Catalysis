# 19 Oct 2026 — Kan de radiale pelletdimensie zichtbaar zijn aan de reactoruitgang?

> **PROVENANCE ERRATUM:** De eerdere persoonlijke lognormal-fit ging over **SEM-karakterisering van een YBCO-supergeleider**, niet de BEP katalysatorpellets. [Correctie](2026_10_19_erratum_log_normal_ybco_sem_vs_bep_pellets.md). De lognormale BEP-pelletverdeling is een **later te testen hypothese**, geen uit YBCO afgeleide experimentele radiusdata.


> **NIEUWE GEBRUIKERSCORRECTIE — ONDERZOEKSVRAAG, GEEN VASTGESTELD RESULTAAT.**
>
> **Intentie:** De gebruiker wil NIET dat het radiaal-resolved model permanent en zonder vergelijking verplicht blijft. Het volledige radiale model dient als **referentie om daadwerkelijk te testen of de extra dimensie aan de buitenkant observeerbaar is**. Als een goedkopere vereenvoudiging dezelfde relevante outlet-respons oplevert, is dat een wenselijke en interessante modelreductie. De eerder genoemde **5–30 ms (10 ms voorbeeld)** zijn slechts grove schattingen voor exploratie, **geen opgelegde relaxation time of gekalibreerde pellet-eigenschap**. Laat reële fysische invoeren en de simulator de respons bepalen en leid effectieve responstijden achteraf af. **NIET** zonder bronwaarden beweren dat simulator zelf de werkelijke materiaal-diffusiviteit kan vaststellen.
>
> Deze update corrigeert de nadruk in [Notebook Delivery Wayfinder](../wayfinder/bep_reactor_notebook_delivery_2026_10_19.md) en [Science/Notebook Handoff](session_handoff_radial_notebook_and_parallel_work_2026_10_19.md); zij vervangt NIET de gebruikersintentie om radiale diffusie expliciet te onderzoeken. **K nog niet volledig geëvalueerd, L en M nog helemaal niet geëvalueerd.**

> **BELANGRIJKE GEBRUIKERSCORRECTIE — 19 OKT, LATER DIE NACHT.** De **eerste** gevraagde onderzoeksvraag is concreet: **blijft de gesimuleerde respons gelijk voor verschillende combinaties van pelletstraal \(R_p\) en effectieve diffusiviteit \(D_\mathrm{eff}\) met dezelfde verhouding \(R_p^2/D_\mathrm{eff}\)?** Dit is een **schaalvergelijking/invariantietest**, niet primair een algemene discussie over meetbaarheid of over het mogen schrappen van de radiale dimensie. De eerdere vraag “is de radiale dimensie aan de outlet zichtbaar?” blijft hooguit een **optionele vervolgvraag**. Verder is een **verdeling van pelletgroottes** een **latere hypothese**, niet nu een engineeringticket of vereiste notebookoptie. De 5–30 ms zijn slechts een eerdere schatting.

## Correctie: eerst schaalinvariantie, dan eventueel modelreductie

Voor pure bolsymmetrische diffusie met \(x=r/R_p\) is de radiale diffusieterm evenredig met \(D_\mathrm{eff}/R_p^2\) (of, in de porositeitsconventie van het model, \(D_\mathrm{eff}/(\varepsilon_p R_p^2)\)). Daardoor volgt bij gelijke \(R_p^2/D_\mathrm{eff}\), dezelfde porositeit en identieke dimensieloze begin-/randwaarden theoretisch dezelfde **genormaliseerde radiale pure-diffusierespons**. Een volledige reactieve bulk–pellet-simulatie kan die schaalinvariantie in specifieke omstandigheden óók behouden; dat moet uit de volledige flux- en brontermen blijken, niet worden geraden.

**Eerste toets:** voer meerdere \((R_p,D_\mathrm{eff})\)-paren met constante \(R_p^2/D_\mathrm{eff}\) uit, vergelijk \(c_p(r/R_p,t)\), de conserverend gekoppelde bulk- en outlet-respons, en onderscheid exacte wetenschappelijke invariantie van numerieke fout of veranderde materiaalkinetiek. Houd pore porosity, catalyst/solid volume fraction, chemistry en inlet vast. Let op: bij monodisperse bolletjes met hetzelfde totale vaste-volumevolume geldt de interfaciale oppervlakte per reactorvolume \(a\propto1/R_p\), en flux \(j\propto D_\mathrm{eff}/R_p\); dus de *volumetrische* flux \(aj\propto D_\mathrm{eff}/R_p^2\) kan ook invariant zijn. Reactieaanname of ander oppervlakte-/massa-criterium kan dat breken.

**Aparte latere hypothese:** vervang één straal door een **fysisch positieve grootteverdeling**, expliciet een **lognormale** verdeling (gebruikerskeuze als toekomstige hypothese), en vergelijk onder gelijke totale katalysatormassa/volume de gewogen radiale/residence-respons. Verschillende distributies met dezelfde gemiddelde \(R^2/D\) hoeven niet dezelfde input–output-overdrachtsfunctie te geven (gemiddelden over vele diffusiemodi). Maar als *iedere* straal met factor \(a\) en *iedere* diffusiviteit met \(a^2\) wordt geschaald bij gelijke gewichten en resterende fysische aannames, kan zelfs een verdeling dezelfde dynamische schaalinvariantie behouden. Dit is een te toetsen analyse, geen bewezen effect van een lognormale pelletverdeling.

**Pas daarna:** de eerdere bredere vraag of een lager-ordemodel of zelfs een uniforme pellet voldoende is voor specifieke outlet-observabelen. Dat is een *ander experiment* dan constante \(R^2/D\)-paren. Geen van deze experimenten is in deze chat uitgevoerd.

## 1. Wat betekent “zichtbaar aan de buitenkant”?

- **Binnen:** c_p(z,r,t) kan sterk van r afhangen en verschillende concentratiegeschiedenissen bevatten.
- **Op pelletinterface:** onder de gekozen zero-film aannamen c_p(z,R_p,t)=C_b(z,t), maar de **gradient ∂_r c_p|R_p** bepaalt een diffusieflux. Een vaste waarde aan de buitenrand impliceert niet nul flux.
- **Langs de bulkreactor:** die interfaceflux moet conserverend en met de juiste oppervlakte/volumeschaal in de bulkbalans verschijnen. Anders kan een pelletverandering fysisch onmogelijk aan de outlet verschijnen — door een codefout/ontkoppeling, niet doordat het effect afwezig is.
- **Aan het meetpunt:** alleen C_out(t), selectiviteit en netto productflux/cyclische gemiddelden zijn direct als reactor-outlet-observabelen zichtbaar. Een radiaal profiel in de simulator is *intern* inzicht, niet automatisch een experimenteel meetbaar signaal.

Het gaat om **gevoeligheid/identificeerbaarheid van een interne dynamische dimensie in een gegeven input-output-experiment**, niet om een abstract ja/nee bewijs dat elk pore-effect fysisch nul is. Vergelijk verschil met (a) numerieke mesh/time-fout en (b) bekende detector-ruis, sample-rate en flow/residence-time spread indien beschikbaar. Als die nog niet bekend zijn, rapporteer simulatie-only onderscheidbaarheid, geen meetclaim.

## 2. Klein experiment om het toetsbaar te maken

**Kies één heldere reference configuration, zelfde chemie, feeds en geometrie waar mogelijk; behoud expliciete modelverschillen.** Bij radiale diffusie in een bol:

\[
\varepsilon_p \partial_t c_p
= D_\mathrm{eff} \,r^{-2}\partial_r(r^2\partial_r c_p)+s(c_p,\theta),
\quad c_p(R,t)=C_b(t),
\quad \partial_r c_p(0,t)=0.
\]

**Vergelijk drie families**, met conservatie en identieke doelobservabelen:
1. **Radiaal-resolved** pore PDE (ground-truth *binnen het gekozen model*, niet fysische waarheid).
2. **Lumped pellet state / reduced-order diffusie-approximation:** minstens een gemiddelde pore inventory en een bron- of effectieve-fluxbenadering die massaconservatie bewaart; coefficients waar mogelijk uit radiale PDE afgeleid, niet willekeurig fitten om resultaat te forceren.
3. **Instant uniformly mixed pellet:** c_p(r,t)=C_b(t) zonder afzonderlijke interne pore-responstijd. Dit is een **specifieke limiet** en niet automatisch aanvaardbaar.

**Per inlet test:**
- Een stap- of (fysisch veilig) pulssignaal plus kleine sinus-/frequentiesweep; meet C_out,i(t), uitstroom F_i(t), en eventueel cyclusgemiddelde netto ethyleenproductie.
- Lees radiale c_p(r,t) van model (1), interfaceflux, en bulk-outlet van alle drie.
- Controleer op verschillende N_r/N_z/solver-toleranties dat zichtbaar verschil geen discretisatieverschil is.
- Evalueer na ingeregelde cycli *volle perioden*; onderscheid verschil in DC mean, amplitude en fase, hogere harmonischen wanneer nodig.
- Markeer per frequentie welke reductie voldoende nauwkeurig is voor de geselecteerde observable, en waar het volledige model niet reduceerbaar blijkt.

**Bij nul diffusieverschil aan de outlet**: laat controleren of bulk↔pore flux echt actief is, en of gekozen reactieregime en inletfrequentie een verschil hadden kunnen blootleggen. Een nul op één conditie is géén algemene reductiestelling.

## 3. Diffusion timescale — niet vooraf vastpinnen

Zuivere karakteristieke schaal bij deze PDE-conventie:

\[
\tau_D=\frac{\varepsilon_p R_p^2}{D_\mathrm{eff}}.
\]

Een “10 ms” input als onafhankelijke slider zou feitelijk een D_eff impliceren; de gebruiker vraagt nu primair **fysische parameterkeuze en daadwerkelijke modelberekening**, niet een verplichte relaxation delay. Aanbevolen:
- Primair **R_p**, **D_eff** (of verifieerbare D_m + tortuosity + porosity), reactor Q, feed forcing frequency/amplitude.
- Toon **berekende** tau_D naast deze inputs (uit de gekozen pore-volume conventie).
- Na het simuleren: bepaal **effectieve** relaxatie/phase-lag uit de berekende pore-/outlet-curves; die is niet vanzelf gelijk aan tau_D.
- Het 5–30 ms-idee mag hooguit als oriëntatie / visuele referentie blijven, **geen bounded validity range** tenzij uit echte data afgeleid.

## 4. Bestaande relevantie, broncontrole en literatuur

- [Berger et al. (2008) dynamic methods for catalytic kinetics](https://doi.org/10.1016/j.apcata.2008.03.020), en [primaire leesroute sectie 6](PRIORITY_reading_2008_s6_transport_vs_surface_memory_2026_10_19.md). Sectie 6 bevat onder meer diffusie/adsorptie en transient reactor analyse; Berger bronpaper moet voor detailfiguren direct gelezen worden.
- **Sterk gericht gevonden:** D. H. Kim (2008), [*Approximations for unsteady-state diffusion and reaction in porous catalyst and their application to packed-bed reactor*](https://doi.org/10.1002/aic.11554), AIChE Journal 54, 2423–2431. Het abstract beschrijft 1e/2e/3e orde benaderingen van de exacte pellet-PDE Laplace-oplossing, en identificeert zowel bedruimte-tijd als pelletdiffusietijd als parameters voor reductiefouten. Relevantie **research lead, geen geïmplementeerde methode**.
- [Diffusion limitation in fast transient experiments](https://doi.org/10.1016/j.ces.2004.07.111), Chem Eng Sci 59 (2004), 5615–5622: gemeten/pulsvorm-gebaseerde transportverstoringen door intra-particle diffusie; andere experimentele systemen, nuttig als precedent voor buitenwaarneming.

## 5. Assignment boundary / next agent

**Science Work agent:** voer de **modelvergelijking als volgend wetenschappelijk doel** uit of bereid een minimale uitvoerbare toets voor, *na* analyse of bulk/pore coupling in de gepushte Methanol-Catalysis/pbr correct werkt. Leg de interfaceflux en behoud vast. Test één source-honest baseline en een eenvoudige stap/forcing op echte code. Maak apart onderscheid **simulatie-detecteerbaar** versus **experimenteel identificeerbaar**, en sluit geen user choice op basis van één ongeverifieerde run. Schrijf een receipt + handoff voor Notebook Work via GitHub Issue #58 / PR.

**Notebook Work agent:** toon de radiaal-resolved case én, indien onafhankelijk gevalideerd, een vereenvoudigd model in dezelfde visualisaties. Niet vooraf alle varianten als fysisch juist aannemen; duidelijk label welke vergelijkingen achter de beelden zitten.

**STATUS: OPEN HYPOTHESIS — NO NEW PBR SIMULATIONS OR REDUCTION TESTS HAVE BEEN RUN IN THIS CHAT.**
