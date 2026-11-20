> **NIET VOLLEDIG GEËVALUEERD — LETTER K — VOORLOPIGE VOLLEDIGE UITWERKING**
>
> **HERIJKING 18 OKTOBER — ONDERZOEK, NIET PRESENTATIE.** De gebruiker heeft een fundamentele model-fidelity-kritiek geformuleerd en wil terug naar de originele fysische onderzoeksvraag. [Bronnotitie uit de volledige gebruikersfeedback](../../research/notes/user_thought_dump_2026_10_18_reactor_recovery.md) · [47-puntenregister en subletters Kα–Kθ](../../research/dossiers/reactor_recovery_2026_10_18/decision_and_implementation_register.md) · [Issue #58](https://github.com/AsapLoso/project-management-agents/issues/58). De eerdere redactionele ‘presentatieprioriteiten’ in dit document zijn **NIET meer de primaire taak**; geen van de nieuwe modelkeuzes is uitgevoerd of geratificeerd.
>
> **DEZE UITWERKING IS DOOR DE ASSISTANT VOORBEREID, MAAR NOG NIET VOLLEDIG MET DE GEBRUIKER BESPROKEN OF GOEDGEKEURD.** De gebruiker heeft wél vastgesteld dat de voorlopige simulatoroutputs geen voldoende gevalideerde reactorresultaten zijn. **L EN M ZIJN NOG HELEMAAL NIET INHOUDELIJK GEËVALUEERD.** De presentatiekeuzes hieronder zijn expliciet *voorlopig*.

# K — Wat hebben we werkelijk bereikt, wat betekenen de getallen en waar houdt de evidentie op?

**18 oktober 2026 — volledige inhoudelijke reconstructie, aanvullend op het eerdere korte [K-statusdocument](K_results_validation_status_2026-10-14.md).** De A–M letters zijn researchvragen, geen verplichte afzonderlijke slides. Het doel van deze uitwerking is de getallen fysisch en wiskundig begrijpelijk maken voordat de gebruiker de presentatiekeuzes maakt. **Geen nieuwe reactorintegratie in deze sessie uitgevoerd:** onderstaande getallen zijn nageslagen uit opgeslagen receipts; extra stoichiometrische controles en de figuurcorrectie zijn analytisch afgeleid uit die data/broncode.

## 0. Voorlopige presentatieprioriteiten — nog niet door gebruiker beoordeeld

| Mogelijk verhaal | Prioriteit | Afbakening |
|---|---|---|
| Een model met echte, niet-nul reactiesnelheden bestaat | **OVERWEEG** | Softwarematige mijlpaal, geen reactorvalidatie; overlapt I narrative 05 |
| Conversie 9,30% en netto selectiviteit 76,93% | **NIET ALS GEVALIDEERD RESULTAAT** | Uitsluitend synthetische referentieberekening; eerder door gebruiker vastgesteld |
| Stationaire convergentie tegenover vervorming van periodieke golf | **STERK WISKUNDIG INZICHT** | K↔G, met analytische pure-advection-caveat |
| Temperatuur/debiet/druk sweep en de betekenis van negative selectivity | **INTERESSANT OM TE BEGRIJPEN** | Geen experimenteel gevalideerde sensitiviteitsrangorde |
| Straal/tortuositeit lijken niets te doen | **GOEDE MODELLERINGSCAVEAT** | Hun nul-effect is per constructie in de uniforme baseline |
| Welke periodieke werking is daadwerkelijk aangetoond? | **CENTRALE OPEN VRAAG** | Eén terminal outlet snapshot, nog geen amplitude/fase/periodisch gemiddelde |
| Alle individuele fouten | **NAAR J / BACKUP** | Alleen opnemen als ze verklaren waarom een wetenschappelijke conclusie begrensd is |

## 1. Welke bewijsstukken zijn er?

**Legacy** op devcontainer: 1.480 gealloceerde toestanden in bulk+pore+oppervlakte, standaard nul-prefactoren voor de chemische kinetiek, oude defecten reproduceerbaar. Geen gevalideerde reacting reactorprestatie.

**Nieuwere Hermes reacting vertical slice**: default uniform-pelletmodel met 60 axiale cellen × 4 gassoorten = **240 dynamische gascoördinaten**, brongebaseerde Urmès-2019 LHHW/PSSA-kinetiek, SciPy BDF en variabele inlet. De optionele radiale variant met 2.400 coördinaten en experimentele niet-PSSA-θ-route zijn **andere**, niet op vergelijkbare wijze gevalideerde configuraties.

**Source/rate-law-verificatie**: 24/24 geselecteerde primaire-brontranscriptiechecks en een aparte coverage-bereiktest **10/12** (twee H₂-waarden net buiten het opgegeven bereik). De oude 11/12-tekst was een telvergissing; 37 pbr-tests slagen maar de source-dependence/closure-vragen blijven.

**Saved receipts:**
- [vertical_slice_receipt.json](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/evidence/vertical_slice/vertical_slice_receipt.json), timestamp **2026-10-15T12:23:32Z**: **17/17 gates PASS**, baseline in/out, C1 sinus eindtoestand, stationaire rooster-/tolerantiechecks, geselecteerde Jacobiaandifferenties.
- [sensitivity_receipt.json](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/evidence/vertical_slice/sensitivity_receipt.json), timestamp **2026-10-14T02:01:56Z**: parameter-sweeps op default uniform-pelletmodel.
- Figuurbestanden van de baseline en sensitiviteit staan in dezelfde Hermes evidence-map. **Geen frequency_response_receipt.json** in die gecontroleerde map. Het losse frequentieresponsscript is geen uitgevoerd/geverifieerd meetresultaat.

**Belangrijk:** 17/17 betekent dat de *gedefinieerde codegates* slagen, niet dat 17 onafhankelijke fysische metingen overeenstemmen.

## 2. Modelconfiguratie versus Urmès 2019: hetzelfde rate law, niet dezelfde bedconfiguratie

[Het primaire Urmès-paper (2019)](https://doi.org/10.3390/catal9020180) gebruikt **0,05 wt.% Pd/α-Al₂O₃**, **0,1 g katalysator**, 100–200 µm gezeefde deeltjes, een **4-mm binnenbuis**, een verdunning met alumina en proeven bij **51 en 62 °C**, **1,26 bar**, nominaal **200 mL/min**. Bij operating condition 1 is de in tabel 1 gerapporteerde acetyleenconversie bij 51 °C **0,13**.

[De gebruikte reacting code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) mengt broncondities met andere aannames: **5-mm buis, 75 mg katalysator, ε_b=0,45, ε_p=0,50, 1.550 kg/m³ deeltjesdichtheid**; het catalyst-object noemt **γ-Al₂O₃** terwijl het bronartikel **α-Al₂O₃** gebruikte. Die verschillen moeten ook bij overdracht van correct getranscribeerde kinetische parameters worden verantwoord.

Uit deze aannames volgt de codegeometrie:
- bedlengte **4,480608 mm**;
- nominale interstitiële verblijftijd **0,01187683 s** (11,877 ms);
- superficiële gassnelheid **circa 0,16977 m/s** en interstitiële snelheid **circa 0,3773 m/s**.

De 200 mL/min is in het model als volumetrisch debiet ingevoerd; voor vergelijking met MFC-metingen moet duidelijk zijn of die **standaard** of **actuele reactorcondities** beschrijven.

**Feed-source discrepantie:** de code gebruikt acetyleen \(y_{C2H2}=0,010\) bij P=126.000 Pa, dus \(p_{C2H2}=1.260\) Pa, terwijl de code-source-check elders 950 Pa aanhaalt (**32,6% verschil**). H₂ \(0,043P=5.418\) Pa versus circa 5.500 Pa (**1,5%**). Eerst controleren of beide partiële drukwaarden werkelijk exact dezelfde conditie/meetpunt beschrijven; niet zonder die check een fout bij het paper of de code claimen. De nieuwe feed gebruikt terecht de volledige \(y_iP\)-conventie, niet de foutieve renormalisatie die Ar uitsloot.

**Gevolg:** het synthetische resultaat **9,30%** is geen directe reproduktie of weerlegging van de gepubliceerde **13%** bij 51 °C. Catalyst support/massa, geometrie en exacte invoer zijn verschillend.

## 3. De drie kerngetallen — interpretatie in plaats van losse percentages

Met A=C₂H₂ (acetyleen), B=C₂H₄ (ethyleen), C=C₂H₆ (ethaan), volgens de code met vaste Q-/snelheidsconventie:

\[
X_A=\frac{C_{A,\mathrm{in}}-C_{A,\mathrm{out}}}{C_{A,\mathrm{in}}},\qquad
S_{B,\mathrm{net}}=\frac{C_{B,\mathrm{out}}-C_{B,\mathrm{in}}}
{C_{A,\mathrm{in}}-C_{A,\mathrm{out}}}.
\]

**Concrete saved baseline, componenten in mol/m³:**

| Component | Ingang | Uitgang | Netto verandering |
|---|---:|---:|---:|
| H₂ | 2,010290 | 1,956752 | −0,053539 |
| C₂H₂ | 0,467509 | 0,424008 | −0,043502 |
| C₂H₄ | 32,725657 | 32,759122 | +0,033465 |
| C₂H₆ | 0 | 0,010037 | +0,010037 |

Daaruit volgt:
- **X = 0,09305 = 9,305%** aangevoerd acetyleen verbruikt.
- **S_net = 0,76928 = 76,928%** netto gevormd ethyleen per verbruikt acetyleen (niet de totale ethyleenuitstroom; er zit al 70% ethyleen in de toevoer).
- **X·S ≈ 0,07158 = 7,158%** netto B-toename per hoeveelheid aangevoerd A **onder de codeconventie**, geen onafhankelijk fysisch gevalideerde yield.
- \(\Delta A =0,04350162 = \Delta B_{\mathrm{net}}+\Delta C=0,03346474+0,01003689\), tot circa 10⁻¹⁵ in de opgegeven waarden.
- \(\Delta H_2=0,05353851=\Delta A+\Delta C\), tot circa 10⁻¹⁶.

Dit is een **nuttige en exact narekenbare interne stoichiometrische check** voor de gebruikte twee-reactiestappen. Het bewijst **niet** de volledige reactorinventaris-/pore-bulkconservering of experimentele overeenstemming. Voor een fysisch variabel totaal gasdebiet dient men molair \(F_{in/out}\) te gebruiken; de concentratieformules veronderstellen de relevante constante-speed/volumestroom-benadering.

**Verblijftijd 11,877 ms** is slechts \(V_\text{void}/Q\), dus een gastransportschaal, niet de levensduur van een oppervlaktesoort. **Pellet-diffusietijd 1,166 ms** is een **diagnostische afleiding** \(\tau_p=\varepsilon_pR_p^2/D_{\mathrm{eff}}\) die **niet als radiaal dynamisch veld** in de uniform-pelletbaseline voorkomt. De daarvan afgeleide \(\phi=0,08531,\ \eta\approx0,999515\) zijn **vereenvoudigde Thiele/effectiveness-schattingen**, niet een in de berekende reactiesnelheid ingevoerde effectiviteitscorrectie. Dat τ_p ≈ 0,098 τ_res suggereert een mogelijk snelle interne diffusie, maar bewijst geen afwezigheid van alle periodieke transport- of oppervlaktememory-effecten.

## 4. De vijf gevoeligheidssweeps — wat betekenen de trends?

Elke sweep verandert *één* ingevoerde parameter rond de modelbaseline. De source-claim “physically admissible ranges” wordt niet ondersteund door bronvalidatie over alle waarden; Urmès' **metingen/fit zijn slechts bij 51 en 62 °C, 1,26 bar**. De ranking op maximale absolute \(|\Delta X|\) bij **ongelijke sweepintervallen** is geen algemene significantie- of gevoeligheidsrangorde.

### 4.1 Temperatuur — conversie kan stijgen terwijl netto ethyleen verdwijnt

| T °C | Berekende X_C₂H₂ | Berekende netto S_C₂H₄ |
|---:|---:|---:|
| 20 | 1,23% | 82,75% |
| 36,85 | 3,85% | 79,87% |
| **51** | **9,30%** | **76,93%** |
| 66,85 | 23,58% | 71,98% |
| 86,85 | 80,02% | 42,84% |
| **100** | **99,99%** | **−225,73%** |

**Waarom mag netto S negatief zijn?** Voor achtereenvolgens \(A+H_2\to B\) en \(B+H_2\to C\) geldt voor de geïntegreerde hoeveelheden \(S_{\rm net}=1-r_2/r_1\). Een uitkomst **−2,257** betekent \(r_2\approx3,257r_1\): er wordt netto meer van de al overvloedig aanwezige **70%-ethyleenfeed** gehydrogeneerd dan ethyleen uit acetyleen wordt gevormd.

Voor de 100 °C snapshot, genormaliseerd per mol oorspronkelijke gasmix, is dit ongeveer 0,009999 mol A verbruikt, 0,032569 mol ethaan gevormd, 0,022570 mol B netto verdwenen en 0,042568 mol H₂ vereist tegenover 0,043 mol in de feed. Dit is **stoichiometrisch mogelijk** maar nadert waterstofuitputting. **Niet automatisch een numerieke fout**; wél ongevalideerde extrapolatie van de rate law ver buiten 51–62 °C en een reden om H₂-budget/flow/thermische aannames te controleren.

### 4.2 Debiet — tijd in de reactor

| Q | Berekende X |
|---:|---:|
| 50 mL/min | 41,32% |
| 100 mL/min | 19,18% |
| **200 mL/min** | **9,30%** |
| 400 mL/min | 4,59% |
| 800 mL/min | 2,28% |

Meer verblijftijd bij lager Q maakt meer omzetting mogelijk. Dit is een **fysisch begrijpelijke modeltrend**, geen volledige kinetische validatie.

### 4.3 Druk — geen algemene drukwet afleiden

| P | Berekende X |
|---:|---:|
| 0,50 bar | 24,52% |
| 1,00 bar | 11,81% |
| **1,26 bar** | **9,30%** |
| 2,50 bar | 4,63% |
| 5,00 bar | 2,30% |
| 10,00 bar | 1,15% |

Mogelijke bijdragen: competitieve adsorptie/inhibitie in de LHHW-rate law, andere partiële drukken, en bij **vast gekozen volumestroom** een andere aangevoerde *molaire* hoeveelheid. De bronkinetiek is niet aangetoond geldig op 0,5–10 bar. Controleer partiële snelheden en normalisatie vóór een fysische conclusie.

### 4.4 Radius en tortuositeit — nullen door **de modelarchitectuur**

Bij 25–200 µm deeltjesstraal en tortuositeit 1–10 blijven de opgeslagen X en S **precies ongewijzigd**. Dit is geen verrassende gemeten fysica: het default model heeft **resolve_radial=False**; zijn reaction source hangt **niet af van R_p of D_eff**. De sensitivity-run berekent τ_p, φ en η **na** de forward solve als aparte getallen. Daarom is de outletconversie per constructie ongevoelig voor radius/tortuositeit in deze gekozen baseline. Een echte radiale of periodieke respons moet apart berekend en onderzocht worden.

## 5. 17/17 PASS: welke eigenschappen zijn werkelijk geverifieerd?

[De opgeslagen reactor-gate receipt](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/evidence/vertical_slice/vertical_slice_receipt.json) noemt 17/17 PASS:

- **A1/A3:** het gebruikte gas-rate-vector en beide stoichiometrische deelreacties conserveren de C- en H-atomen; **A2:** één gekozen coverage-point valt in gepubliceerde ranges; **A4:** de gekozen yᵢ·P-invoerconventie wordt gehanteerd, hoewel er expliciet brongetallenverschillen zijn.
- **B1–B5:** baselineconcentraties zijn eindig en niet-negatief, acetyleen neemt langs het bed af, X en S worden berekend. De **selectiviteitsgate controleert alleen dat S gerapporteerd wordt**, niet of S natuurkundig of experimenteel klopt.
- **C1/C2:** één periodiek opgelegde inlet geeft een andere eind-outletconcentratie dan een constante inlet; waarden blijven eindig/positief. Geen waveform-, yield- of fasevalidatie.
- **D1:** reacties nul + constante inlet geeft constant plug-flow-evenwicht — geen tijdsafhankelijke advection benchmark.
- **D2:** **steady-state X_C₂H₂** verandert bij n_z=30 naar n_z=120 van 0,09309235 naar 0,09302845: **0,06869% relatieve verandering**. Eén twee-roostervergelijking; geen algemene bewezen convergentieorde.
- **D3:** rtol 10⁻⁵ versus 10⁻⁸ verschilt voor steady X relatief slechts **3,5×10⁻¹⁰** in deze receipt.
- **D4a/D4b:** in geteste punten/kolommen komt de analytische chemische en samengestelde Jacobiaan overeen met finite-difference-stencils. Geen volledig gedekt radial-resolved systeem.
- **E1:** receipt/figuur bestaan.

De afzonderlijke **10/12 coverage-bereikvergelijking** is geen tegenspraak met A2 PASS: dat zijn **verschillende tests en operating points**. Evenmin zijn 37 geslaagde package-unit-tests een reactorbenchmark.

### Kerninzicht K↔G: **steady X convergent ≠ outletgolf betrouwbaar**

Een stationaire conversie kan met 0,069% roosterafhankelijkheid weergegeven worden terwijl dezelfde ruimtediscretisatie een *periodiek signaal* afvlakt. In G is het zuivere-advectionvraagstuk analytisch uitgewerkt: bij eerste-orde-upwind met **N=60**, een forcingperiode gelijk aan één verblijftijd en **exacte integratie van de semi-discrete ODEs** blijft circa **72,09% amplitude** over, dus **27,91% puur numeriek afgevlakt**, plus ongeveer **1,31° faseverschil** ten opzichte van de ideale transportvertraging. Dit is een **wiskundig referentieprobleem zonder chemie**, niet een gemeten fout in de reacting reactor. Forward Euler bij **CFL=1** kan in die speciale *pure-advection*-situatie exact één cel doorschuiven; bij stijve reactie/diffusie hoeft dit niet te gelden.

Daarom moet men **amplitude, fase en geïntegreerde periodieke observabelen zelf** op discretisatie, tolerantie en integratiestap controleren; stationaire X is een andere grootheid.

## 6. De periodieke run: wat bewijst de test?

De code legt alleen aan de acetyleeningang een sinus \(C_{A,\rm in}(t)=\bar C_A[1+0,20\sin(2\pi f t)]\) op met \(f=1/\tau_{\rm res}\approx84,1975\) Hz en T≈11,8768 ms. De inletamplitude is **±0,093502 mol/m³** bij een baseline van 0,467509 mol/m³.

Op \(t_{\rm end}=8\tau_{\rm res}+0,05s\approx0,145015s\) toont de reactorreceipt:

| Species | Constant outlet | Periodiek outlet op **één** eindtijdstip |
|---|---:|---:|
| H₂ | 1,956752 | 1,963531 |
| C₂H₂ | 0,424008 | 0,494252 |
| C₂H₄ | 32,759122 | 32,756703 |
| C₂H₆ | 0,010037 | 0,007856 |

De maximale absolute verschillen op dat tijdstip zijn **0,070244 mol/m³** (acetyleen); C1 PASS betekent **‘periodieke input verandert de terminal snapshot’**. Niet: 75% amplitudegain, een bewezen faseverschuiving of verbeterde opbrengst. Er is **geen** gecontroleerde \(x(t+T)-x(t)\)-norm, geen Fourier/harmonische amplitude+phase, geen cyclusintegraal netto ethyleen en geen fair steady reference.

Dat is het precieze verschil tussen **een synthetische time-dependent test** en **de wetenschappelijke test van periodiek bedrijf**.

## 7. Twee extra statische bevindingen over *diagnostische code* — naar J

1. **Sensitivity-plot paneel 6 schaalt τ_p zesmaal verkeerd.** Het berekent \(k=\tau_{p0}/(\epsilon_pR_{p0}^2)\) en vervolgens \(\tau_{p,\mathrm{plot}}=\mathrm{tortuosity}\,R_p^2k\), terwijl dezelfde code \(\tau_p=\epsilon_pR^2/D_{\rm eff}\) en \(D_{\rm eff}=\epsilon_pD_m/\mathrm{tortuosity}\) gebruikt. Het plotrecept vermenigvuldigt dus nogmaals met \(\mathrm{tortuosity}_0/\epsilon_p=3/0,5=\mathbf6\). Op het basispunt tekent de formule **6,997 ms** waar de **JSON-data zelf 1,166 ms** rapporteren. Daardoor mag het paneel “above the line = transport limited” niet gebruikt worden als fysisch bewijs. Deze analyse is algebra uit de broncode, **geen nieuwe scriptuitvoering**. De JSON-data hoeven niet even fout te zijn.
2. **frequency_response.py heeft een tijdreeks/reshape-inconsistentie**. De code geeft **sol.y** met vorm \((n_\mathrm{states},n_\mathrm{times})\) aan een helper **bulk_outlet** die een *enkelvoudige* toestandsvector naar \((n_z,4)\) hervormt. Als de oplossing meerdere tijdpunten bevat, is dat niet compatibel. Zelfs na een fix zou een max-min over de laatste **25% adaptief gekozen solverpunten** niet automatisch een betrouwbare harmonische amplitudeschatter zijn of fase geven; bovendien staat \([\tau_{\rm res},\tau_p]\) in het commentaar omgekeerd voor de opgeslagen baseline, waarin \(\tau_p<\tau_{\rm res}\). **Geen frequency-response receipt aangetroffen.**

Deze twee kwesties zijn een afbakening van wat de *diagnostiek* bewijst, geen algemene veroordeling van de 17/17 default reactorgates. Laat J ze indien nodig reproduceren.

## 8. Interpretatieniveaus voor de eindpresentatie

| Soort claim | Wat daadwerkelijk beschikbaar is | Wat absoluut niet bewezen is |
|---|---|---|
| **Bron en mechanisme** | 2019 LHHW-parameters en brontranscriptie met bekende uitzonderingen | Volledige parametertransfer naar onze catalyst/bed |
| **Software-implementatie** | Dynamische bulk-reactor met niet-nul PSSA rates en inletfunctie | Volledig gekalibreerde transient-θ chemie |
| **Interne numerieke consistentie** | 17/17 beperkte gates; stationary X rooster/tolerantie; chemische stoichiometrie | Geverifieerde amplitude/fase of volledige radiale fluxconservering |
| **Synthetische modelvoorspelling** | X=9,30%, S=76,93%; T/Q/P sweeps voor aannames | Experiment reproduceert deze conversie/selectiviteit |
| **Wetenschappelijke onderzoeksvraag** | Modulerende feed als uitvoerbare input | Cyclusgemiddelde ethyleenwinst tegenover gelijke of beste steady input |

[Urmès et al. 2022](https://doi.org/10.1002/cctc.202101826) is reeds een direct relevant **periodiek-debiet / kinetische-identificatie** precedent. Het bewijst niet onze eigen concentratiemodulatie of de beoogde optimale ethyleenwinst.

## 9. Minimale route van output naar wetenschappelijk resultaat (voor later)

1. Bepaal één intern consistente fysische bed/catalyst/feedconfiguratie, inclusief α/γ, massa, Q-referentie, inert gas, partiële drukken, density en brongeldige rate-lawcondities.
2. Controleer de werkelijk gekozen fysische observable: X, *netto* ethyleenproductie, selectiviteit, uitgangsamplitude, fase en periodieke gemiddelden zijn niet equivalent.
3. Verifieer bron/stoichiometrie/fluxconservering en stationaire én dynamische rooster/timestep-convergentie op **die observabelen**.
4. Bouw een matched-input reactorbenchmark in het brongeldige regime. Een uitkomst met dezelfde T en P maar een andere bed/katalysator is geen strenge benchmark.
5. Bij sinusvormige forcing: eerst periodiek ingeregeld \(x(t+T)\approx x(t)\), dan amplitude/fase/cycle-integrated **net** ethyleenproductie en eerlijke gemiddelde toevoerbasis; pas daarna variatie/optimalisatie.
6. Indien de vraag werkelijk dynamische adsorbaten betreft, vergelijk een source-grounded dynamisch-\(\theta\)-model met PSSA onder identieke gasreactorcondities. Bepaal welke parameters experimenteel identificeerbaar zijn.

**Niet nu** de hele simulator herschrijven om de presentatie te rechtvaardigen. Dit zijn falsifieerbare onderzoeksvragen, geen reeds uitgevoerde verbeteringen.

## 10. De mogelijk sterkste presentatiesynthese

> **We hebben een reagerende simulator die zijn gekozen basistests haalt en numeriek consistente stationaire conversiecijfers produceert. Maar een betrouwbare *periodieke* ethyleenopbrengst vraagt een extra laag bewijs: fysisch correcte configuratie, verifieerbare amplitude en fase van de uitgevoerde golf, en een eerlijke cyclusgemiddelde vergelijking.**

Een plausibele vertelvolgorde is één zin over **wat gebouwd is** → één toetsbaar feit over **wat getest is** → **wat die test niet meet** → **de volgende beslissende proef**. Laat K geen pagina met bugmeldingen worden. De gebruiker moet hierover nog expliciet kiezen; geen K-slide goedgekeurd.

## 11. Open gesprekspunten — K **NIET AFVINKEN**

- [ ] Is de eerste reagerende run een zin waard in de deck, ook zonder fysische validatie?
- [ ] Willen we 17/17 gates, de stoichiometrische in/out-balans of de 9,30% helemaal laten zien, of alleen als technische achtergrond bewaren?
- [ ] Welke gevoeligheden zijn werkelijk interessant: T/Q/P, of juist de per constructie nul R_p-gevoeligheid?
- [ ] Is **−225,73% S** bij 100 °C een leerzaam definitievoorbeeld, of vooral een nutteloze extrapolatie buiten de bronfit?
- [ ] Is **stationaire X-convergentie ≠ periodieke waveform-fidelity** de beste verbinding tussen G en K?
- [ ] Welke externe claims (bronreactor, catalyst, flow) moeten eerst worden gecorrigeerd?
- [ ] Moeten de twee code-diagnostiekbevindingen afzonderlijk naar J zonder het K-verhaal te domineren?
- [ ] Pas ná bespreking: welke K-bevindingen komen in de presentatie, en welke blijven backup?

**STATUS: NIET VOLLEDIG GEËVALUEERD. L EN M NOG NIET INHOUDELIJK BESPROKEN.**
