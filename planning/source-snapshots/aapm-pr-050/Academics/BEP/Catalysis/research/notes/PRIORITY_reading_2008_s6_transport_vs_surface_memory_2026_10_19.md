# HOGE PRIORITEIT — Berger 2008 §6, diffusie vs oppervlaktekinetiek

> **HOGE LEESPRIORITEIT — EXPLICIETE GEBRUIKERSWENS, 19 OKTOBER 2026.**
>
> **NOG NIET AFGEROND:** De volledige originele 26-pagina's Berger-PDF, inclusief alle figuren en formules van sectie 6, is in deze sessie **niet opnieuw direct gelezen**. Dit overzicht baseert zich op bibliografische primary metadata plus eerdere lokale original-PDF audits, [literature_reuse.md](../dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md) en [het uitgebreide eerdere paper-consensusdocument](../../Articles/paper_analyses/bergerDynamicMethodsCatalytic2008_consensus.md). Controleren aan het origineel voordat nieuwe fysische of codeclaims worden goedgekeurd.
>
> **ONDERZOEK VOOROP.** De vraag is of radiaal deeltjestransport en oppervlaktekinetische geheugenwerking verschillende tijdschalen hebben en welke zichtbaar moeten zijn in de beoogde input→output-notebook, niet of er morgen slides af zijn.

## Fysisch onderscheid: drie mechanismen

1. **Gas langs bed:** bulk C_b(z,t), verblijftijd en eventueel axiale dispersie.
2. **Gas in pelletporiën:** c_p(z,r,t), radiale diffusie en eventuele film; een diffusive karakteristieke tijd is epsilon_p*R_p²/D_eff. Als transport snel is, mag c_p circa C_b zijn.
3. **Chemisch oppervlak:** geadsorbeerde soorten theta_j(z,r,t) hebben eigen balans dtheta/dt = elementary adsorption − desorption ± reaction. Snel pore transport legt theta niet direct vast. **De PSSA-aanname dtheta/dt≈0 is onafhankelijk van snelle poriediffusie.**

Illustratief *generiek* adsorptievoorbeeld (NIET het bronmechanisme van Pd):

- dtheta/dt = k_ads*c*(1−theta) − k_des*theta.
- theta_ss = k_ads*c / (k_ads*c+k_des).
- tau_theta = 1/(k_ads*c+k_des).
- Bij sprong naar constante c: theta(t) = theta_ss(c) + [theta(0)−theta_ss(c)]exp(−t/tau_theta).

Zelfs wanneer c_p≈C_b reeds geldt, hoeft de oppervlaktebedekking dus niet instantaan gelijk te worden aan theta_ss. Het omgekeerde kan ook: PSSA-chemie bij een pellet met meetbare interne diffusie. Afwezigheid van **stationaire** massatransferlimitaties sluit **dynamische** demping niet automatisch uit. Wat voor deze BEP-condities aantoonbaar het geval is, blijft een open fysisch onderzoekspunt.

## Berger et al. 2008 — concrete sectie-6 leesroute

**Bron:** R.J. Berger et al., *Dynamic methods for catalytic kinetics*, Applied Catalysis A: General 342 (2008), 3–28. DOI [10.1016/j.apcata.2008.03.020](https://doi.org/10.1016/j.apcata.2008.03.020). [Uitgever](https://www.sciencedirect.com/science/article/abs/pii/S0926860X08001610). De paper is een **review met zes toepassingsvoorbeelden**, geen direct gepubliceerde acetyleenreactor.

**Voor zelfstandig gericht lezen, in volgorde van de gestelde vraag:**

- **§6.2 — adsorptie en diffusie in zeolieten.** Hoe onderscheiden transienten sorptie en intracrystalline diffusie? Dit is het meest direct voor de transportkant.
- **§6.4 — simultane SO₂/NOₓ adsorptie/reactie op Na/γ-Al₂O₃.** Hier staan tijdafhankelijke oppervlakte-/adsorptieprocessen. In **§6.4.4.1** is volgens de eerdere primaire-PDF-audit MOL, ruimtelijke eindige differenties en een NAG implicit BDF integrator daadwerkelijk toegepast. Lees bronvergelijkingen en welke voorraad exact meegerekend wordt.
- **§6.6 — SCR-DeNOx met NH₃/NO.** Adsorptie, desorptie en coverage-afhankelijke kinetiek. Relevant voor waarom onmiddellijke bezetting niet klakkeloos uit snelle gastoevoer volgt. Andere katalysator en chemie.
- **§6.5 — oxidative coupling of methane met SSITKA**, voor oppervlaktesites, opslag en kinetische parameters; de eerdere primaire audit noemt ook **§6.5.4.2** als numerical MOL-voorbeeld.
- **§6.1 cracking en §6.3 chemical looping** later als bredere context.

**Niet overslaan vóór §6:** **Berger §4, Fig. 5, Eqs. (1)–(3) en Table 2** (eerder door repo primary audit gelezen). §4 gebruikt een pseudo-homogene axiale gasbalans mét aparte dynamische site-balans dtheta_j/dt=R_j; het levert niet ons eigen volledige radiale pellet-PDE. Table 2 onderscheidt **steady-state** en **transient** transportcriteria. Het specifieke circa-1ms diffusievoorbeeld is *geen universele frequentiegrens*; vergelijk altijd tijdschalen/forcings/observabelen.

**Wat nog geverifieerd moet worden:** exacte namen, figurennummers, symbolen, stoichiometrische en fluxconventies en geldig domein van elk §6-geval aan de oorspronkelijke PDF; lees alle figuren. De eerste analyse- en consensusbestanden zijn geen vervanging van een kritische eigen paperstudie en bevatten eerder gecorrigeerde overgeneraliserende uitspraken.

## Hoe verhouden Urmès 2019, Urmès 2022 en een andere Urakawa 2008 zich hiertoe?

- **Urmès 2019:** C. Urmès et al., [Kinetic Study of the Selective Hydrogenation of Acetylene over Supported Palladium under Tail-End Conditions](https://doi.org/10.3390/catal9020180), *Catalysts* 9:180. Stationair gefitte effectieve LHHW/PSSA-kinetiek met (deels) algebraïsche bezettingen; **een gas-PDE met deze rate law kan een transient gasrespons simuleren**, maar zonder onafhankelijke theta-ODE volgt oppervlaktegeheugen niet uit de fitting. Van belang als source-matched gereduceerde referentie.
- **Urmès 2022:** C. Urmès et al., [Microkinetic Modeling of Acetylene Hydrogenation Under Periodic Reactor Operation](https://doi.org/10.1002/cctc.202101826), *ChemCatChem* 14 e202101826. **Dit is de directste acetyleenspecifieke bron.** Uit het uitgeversabstract bevestigd: Pd/α-Al₂O₃, kleine periodieke **flow**-modulatie, microkinetische single-site modelparameters afgeleid uit dynamische outlet molfracties, met gevoeligheid voor H₂-adsorptie en vinyl→adsorbed ethylene. Volledige mechanistische ODE's, rate constants, state constraints en SI moeten **nog rechtstreeks worden beoordeeld**: noem dit niet reeds geïmplementeerd.
- **Urakawa/Bürgi/Baiker 2008:** [Sensitivity enhancement and dynamic behavior analysis by modulation excitation spectroscopy](https://doi.org/10.1016/j.ces.2007.06.009), *Chemical Engineering Science* 63:4902–4909. **Ander 2008-paper dan Berger**, relevant voor fasegevoelige periodieke meting en lineaire-kleinsignaal-interpretatie (§3). Beter als aanvullende notebook-analysemethode, niet de hoofdbron voor bulk+surface PDE.
- **2022 uitgeverspagina** vermeldt SI-bestand met naam cctc202101826-sup-0001-misc_information.pdf; toegankelijkheid en inhoud nog niet onafhankelijk gecontroleerd.

## Hoge-prioriteitsvragen voor de volgende wetenschappelijke pass

- [ ] **Lees Berger 2008 sectie 6 volledig, origineel PDF, figuren/formules inbegrepen** en schrijf een begrijpelijk inhoudelijk overzicht per voorbeeld: systeem, dynamische toestand, output, onderscheid transport/chemie, welke aannames gelden?
- [ ] **Lees Berger §4 en Table 2** om te zien onder welke omstandigheden een fysische reductie is gerechtvaardigd.
- [ ] **Vind/lees Urmès 2022 full paper én SI** om dynamische surface state, rate-source, parameteridentificeerbaarheid en periodieke simulatie daadwerkelijk te reconstrueren. Expliciet onderscheid tussen 2022-flow en beoogde BEP-composition forcing.
- [ ] Vergelijk 2019 algebraïsche theta met 2022 dynamische theta; maak één worked example dat laat zien dat gelijke c(t) maar verschillende theta(t) verschillende r(t) kan geven.
- [ ] Stel voor de plug-and-play notebook relevante outputs vast: inlet/outlet time series, radiaal profiel c_p, theta(t), gemiddelde over laatste volle perioden en optioneel fase/FFT. Niet claimen dat alle outputs al brongetrouw beschikbaar zijn.
- [ ] Behoud onderwerp als **hoge prioriteit, niet afgerond** in scientific-method Wayfinder; pas niet eigenmachtig modelparameters aan en start nog geen Work-implementatie.

**LEESPRIORITEIT HOOG — NOG OPEN — GEEN CODE GEWIJZIGD.**
