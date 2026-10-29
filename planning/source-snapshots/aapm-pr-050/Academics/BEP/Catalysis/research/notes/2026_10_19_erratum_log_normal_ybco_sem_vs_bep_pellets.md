# Erratum — 19 oktober: lognormale verdeling, YBCO-SEM versus BEP-pellets

> **EXPLICIETE GEBRUIKERSCORRECTIE, NIET AFGELEID UIT EEN PAPER.** De eerdere persoonlijke **lognormale fit** had betrekking op **SEM (scanning electron microscopy)-karakterisering van YBCO (yttrium-barium-koperoxide), een supergeleider**. Dat is **ander materiaal en ander onderzoek dan BEP-acetyleenhydrogenering met katalysatorpellets**. Niet gebruiken als experimentele validatie of gemeten pellet size distribution voor de katalysator. De eerdere grap “ik kan mijn eigen schrijven citeren” rechtvaardigt **geen** bron- of dataoverdracht tussen de projecten.

## Correcte aparte contexten

- **[USER REPORTED — ander onderzoek]** Eigen schrijf-/analysewerk over lognormale fits van SEM-beelden van een **YBCO-supergeleider**. Exacte titel, locatie en welke SEM-meetgrootheid gefit werd zijn in dit gesprek **niet geïdentificeerd**. Niet zomaar aannemen dat die fit *katalysatordeeltjes*, *pelletstraal*, *synthesekorrels* of hetzelfde meetmechanisme betreft.
- **[USER CHOICE — BEP toekomstige hypothetische uitbreiding]** Voor een **nog niet geïmplementeerde pelletpopulatiestudie** is een **lognormale, positieve radiusverdeling** de gewenste modelkeuze (niet normaal, niet afgeknot normaal). Die keuze is een *verkennende hypothese*, niet onderbouwd met YBCO-SEM-data.
- **[DEFERRED WORK]** Vergelijk fysieke diffusie- en reactoroutput onder verschillende lognormale pelletpopulaties. Definieer zorgvuldig welke spreiding/momenten constant zijn: variantie van log-radius of van straal, number- versus mass-weighted distributie, totale katalysatormassa. Gebruik eigen BEP-data indien beschikbaar, of label nadrukkelijk synthetisch.
- **[CURRENT WORK]** Twee Work-agents blijven gericht op (A) bulk↔radiaal model en monodisperse `R²/D`-vergelijking en (B) een uitvoerbare Jupyter-notebook, geen pelletpopulatie-fit en geen YBCO-analyse.

## Bronnen en onzekerheid

Op de GitHub default-branches zijn eerdere *samenvattende* verwijzingen naar een lognormal fitting case ('Verwachte.txt') aangetroffen, maar er is **geen origineel YBCO-SEM-manuscript of datafile vastgesteld** in deze sessie. **Dus GEEN verzonnen referentie**, geen directe link of manuscriptcitaat claimen. De gebruiker heeft uitdrukkelijk de juiste herkomst gespecificeerd; voor een toekomstige echte bronverwijzing moet het oorspronkelijke document worden opgezocht.

## Wiskundige noot voor latere BEP-hypothese (niet de SEM-analyse claimen)

Als `ln R ~ N(m,s²)`, is `E[R²]=exp(2m+2s²)`. Positiviteit volgt uit lognormaliteit. Onder vaste *log-spreiding* en totale schaalwijziging `R→aR, D→a²D` blijft de hele verdeling van `R²/D` gelijk. Met variërende spreiding kun je bij gelijk gemiddeld `R²/D` andere populatieresponsen toetsen; inventory weighting vereist de juiste `R³` massaweging bij number-weighted R.

**STATUS: herkomst gecorrigeerd; originele YBCO-publicatie niet gevonden; BEP-distributie nog steeds latere hypothetische onderzoekslijn; beide Work-agents niet gestart door deze update.**
