# BEP Catalysis Project Conventions

This file documents the directory architecture, operational workflows, and guidelines unique to the BEP Catalysis (Urakawa Group) project.

---

## 📁 Directory Architecture & File Layout

The Catalysis project directory is strictly structured into modular components:

```
Academics/BEP/Catalysis/
├── 0_Project_Management/              # Proposal LaTeX sources, compiled PDFs, and drafting tools
│   ├── BEP_Project_Proposal__PP_(1)/  # Reference proposal drafts
│   ├── BEP_Proposal_Overleaf/         # Overleaf sync source tree
│   ├── archive/                       # Historical drafting transcripts and brainstorming logs
│   │   └── transcripts/               # Session transcripts and writing logs
│   ├── scripts/                       # Zotero citation sync, tracker, and renaming utilities
│   ├── main.tex                       # Core master LaTeX proposal document
│   ├── references.bib                 # Master Better BibLaTeX bibliography export
│   └── section*.tex                   # Modular proposal chapters (intro, lit, method, plan)
├── 1_Transport_Phenomena/             # Mass/heat transport physics notes & Thiele/Péclet scaling
├── 2_Courses/                         # Archived Brightspace course tracks (four-file convention per course)
│   └── PDC/                           # Process Dynamics & Control (OrgUnitId 860369); MAX_PATH-sensitive, see its conventions.md
├── 3_Model/                           # Transient PBR model: Gemini-framework transcripts, audits, solver code
│   ├── c2h2_hydrogenation_transient_model.py  # MOL/BDF solver skeleton (C2H2->C2H4->C2H6); kinetics all 0.0
│   ├── gemini_transcript_2026-09-29.md        # Sibling chat 7378843f85f483d1: numerics + ModelParams
│   ├── gemini_transcript_2026-09-29_83878835991845b5.md  # Chat: Berger Sec.5 criteria + model framework
│   ├── transient_model_framework_audit.md     # Audit vs Berger (2008): 9 framework defects (§3) + UNVERIFIED list (§4). READ FIRST
│   └── state.md / conventions.md / resources.md / history.log  # Four-file convention; state.md = code-execution defect register
├── Articles/                          # Literature repository and research analyses
│   ├── 0 initlal lead by Damian/      # Foundational papers provided by supervisor
│   ├── 1 Meeting Zoe/                 # Literature & reference materials from initial TW meeting
│   ├── 2 meeting Damian + Zoë/        # BEP baseline examples and meeting materials
│   │   └── extracted/                 # Extracted chapter text from Larsen BEP benchmark thesis
│   ├── 3 Meeting Dylan/               # Audio recording and discussion notes
│   ├── 4 PDE to ODE/                  # Method of Lines and ODE numerical references
│   ├── acquired_pdfs/                 # Full repository of acquired academic paper PDFs
│   ├── analyses/                      # Comprehensive indices, trackers, and synthesis documents
│   ├── graph/                         # Knowledge-graph artifacts (ontology, chunks, paper KGs, merged graph)
│   │   ├── chunks/                    # Deterministic chunk manifests per document (larsen2024, berger2008, ...)
│   │   ├── paper_kgs/                 # Per-document LLM extraction runs + bridge files
│   │   ├── kg_extraction_workflow.md  # In-session extraction SOP (bounded-ontology prompt + glean + consistency)
│   │   ├── knowledge_graph.json       # Merged concatenated graph (output of kg_merge.py)
│   │   ├── ontology.yml               # Node/edge types + provenance schema (v1)
│   │   └── aliases.yml                # Entity alias map for deterministic SAME_AS resolution
│   ├── metadata/                      # Citation manifests, library exports, and raw text dumps
│   ├── paper_analyses/                # Consensus summaries and analysis reports per paper
│   └── scripts/                       # Automated PDF acquisition and citation extractors
├── Code/                              # Mathematical modeling, kinetics, and simulation scripts
├── Meetings/                          # Chronological meeting dossiers, agendas, and minutes
├── README.md                          # High-level overview of the Catalysis dual BEP track
├── committee_candidates.md            # Candidate staff profiles and outreach templates
├── conventions.md                     # Branch-specific operational rules (this file)
├── history.log                        # Pruned completed actions and chronological event history
├── resources.md                       # Core reference library, literature links, and textbook guides
├── state.md                           # Active project status, next actions, and open loops
└── thread_examencommissie_paula.md    # Formal Board of Examiners correspondence log
```

---

## 🔬 Project Guidelines & Operational Rules

### 1. Dual Degree Integration
- Ensure all modeling options satisfy both Applied Physics (TN) and Applied Mathematics (TW) BEP requirements.
- Maintain a balanced emphasis on physical-chemical transport phenomena and rigorous numerical/mathematical analysis.

### 2. State & History Hygiene (Rule 2 & Rule 17)
- **Active State Only:** `state.md` strictly contains active action items and open communication lines.
- **Immediate Pruning:** Completed tasks and past states must be logged to `history.log` and removed from `state.md`.
- **Knowledge Base Separation (Rule 9):** Reference materials, links, and detailed notes reside in `resources.md` and `Articles/analyses/`, never cluttering `state.md`.

### 3. Helper & Script Isolation (Rule 1 & Rule 19)
- No loose Python scripts (`.py`), data dumps (`.json`), or auxiliary build files may reside in root project directories.
- All management utilities belong in `0_Project_Management/scripts/`, citation tools in `Articles/scripts/`, and simulation code in `Code/`.

### 4. Citation & Literature Passage Extraction Convention
- **No Blind Citations:** Before finalizing any citation (`\cite{...}`), extract the exact passage/quote from the PDF source based on keywords/glossary and TOC section.
- **Passage Review:** Present the raw extracted text passage to the user to confirm the exact physical mechanism before locking it into LaTeX.
- **Master Source:** Zotero with Better BibTeX auto-export is the single source of truth for `references.bib`.

### 5. Candidate Methods Framing (No Premature Promises)
- When proposing mathematical or physical techniques (e.g., Method of Lines, Upwind schemes, BDF/Radau solvers, Langmuir-Hinshelwood rate laws, Genetic Algorithms), ALWAYS frame them as **candidate methods / potential frameworks to evaluate**, NOT as locked-in commitments.

### 6. Writing Collaboration & Humanized Prose (Rule 15)
- Provide structure, keywords, and concept blueprints using clean LaTeX markup (`itemize`, `enumerate`, headers, bold terms)—never dense prose.
- Strictly adhere to anti-AI slop standards: eliminate buzzwords (*delve, tapestry, pivotal, crucial, robust, landscape*), avoid significance inflation, use plain verbs, and maintain concise sentences.

### 7. Supervisor Communication Formatting (Damian / WhatsApp)
- **Channel:** WhatsApp (no email).
- **Language & Tone:** English, natural and low-key.
- **Formatting:** Use bullet points only when making summations or listing specific cases to improve readability.

### 8. Exact Academic Titles & Formulier TWN3002-24 Mapping
NEVER hallucinate or inflate academic titles. Strictly use these verified credentials:
- **Dr. Bijoy Bera:** Assistant Professor (Vast staflid TNW / ChemE - Transport Phenomena) -> *Begeleider TN / Vast staflid TN (positie b)*.
- **Dr.ir. Z.J.G. (Zoë) Gromotka:** Universitair Docent / Assistant Professor (Vast staflid DIAM / Mathematische Fysica) -> *Begeleider TW / Vast staflid TW (positie a)*.
- **Dr. N.V. (Neil) Budko:** The supplied 2026 roster marks him Senior=x and places him in Numerical Mathematics, a different section from TW1 Zoë; this makes him a roster/section-compatible candidate only. The current directory lists Scientific Staff but does not establish fixed/permanent status. No selection or formal appointment is confirmed.
- **Damian Vico van Berkel:** PhD Candidate (TNW / ChemE - Catalysis Engineering) -> *Dagelijkse begeleiding Lab & Kinetiek*.
- **Prof.dr. A. (Atsushi) Urakawa:** Full Professor / PI (TNW / ChemE) -> *Labhoofd / optioneel 5e adviserend lid*.
- **Dr. C.S. (Carlas) Smith:** Assistant Professor (3mE / DCSC - Systems & Control / TN PI) -> *Kandidaat Tweede staflid TN (positie d)*.
- **Dr. Dylan Kalisvaart:** Postdoc / Researcher (3mE / DCSC) -> *Informele Sparringpartner SysCon*.

**Formulier TWN3002-24 Regels:**
- **Voetnoot 3:** Leden *a* (Zoë) en *c* (een eventuele TW3-kandidaat) moeten lid zijn van de vaste wetenschappelijke staf DIAM bij verschillende secties, en ten minste één moet BEP-senior zijn. De aangeleverde roster bevestigt de sectie/Senior=x-screen voor kandidaten; contractstatus en formele goedkeuring zijn nog te verifiëren.
- **Voetnoot 4:** Leden *b* (Bijoy) en *d* moeten lid zijn van de vaste staf van TNW en tenminste één moet onderwijs verzorgen in de BSc TN.
- **Sectie- & Stafbeperkingen TW3:** Alle 15 senioren van Mathematische Fysica (inclusief Dr. Yves van Gennip) zijn uitgesloten voor TW3 omdat TW1 Zoë Gromotka in dezelfde sectie zit en de supplied TWN3002 rule verschillende secties vereist. De facultaire directorycategorieën Teachers/Emeritus bewijzen op zichzelf geen arbeidscontract of vaste-wetenschappelijke-stafstatus; verifieer dit per kandidaat vóór selectie. Hanne Kekkonen niet opnieuw benaderen zonder een nieuw expliciet gebruikersbesluit. Geen outreach of toezeggingen zonder expliciet gebruikersbesluit.

---

## 🎓 Geverifieerde Titels & Academische Conventies (Anti-Hallucinatie)

Om hallucinaties in correspondentie en documenten te voorkomen, gelden strikt de volgende geverifieerde titels:
- **Dr. Bijoy Bera** (Assistant Professor, ChemE / Transport Phenomena, TNW)
- **Dr.ir. Z.J.G. (Zoë) Gromotka** (Assistant Professor, Mathematische Fysica, DIAM / EWI)
- **Dr. N.V. (Neil) Budko** (Associate Professor, Numerical Analysis, DIAM / EWI — BEP Senior)
- **Dr. Carlas Smith** (Associate Professor, DCSC / 3mE-TNW)
- **Damian Vico van Berkel** (PhD Candidate, Catalysis Engineering, TNW — géén dr./prof.)
- **Prof. dr. Atsushi Urakawa** (Full Professor, Catalysis Engineering, TNW)
- **Roel Smit** (Opleidingsdirecteur BSc Technische Natuurkunde)
- **Els Arkesteijn** (Secretariaat Catalysis, Separation and Electrochemical Engineering / CaSE, Afdeling ChemE, Faculteit TNW — `Secr-CaSE-TNW@tudelft.nl`, Gebouw 58)

### 📋 Formele Richtlijnen Afsprakenformulier TWN3002-24 (24 EC)
- Inleveren uiterlijk 3 maanden voor afstudeerdatum via `BoE-AM@tudelft.nl`.
- Vaste commissie van 4 vaste stafleden: TW1 (DIAM), TN2 (TNW), TW3 (DIAM senior, andere sectie), TN4 (TNW, geeft onderwijs in BSc TN).

---

## 🖥️ 9. Thesis Writing & MyST/Typst Publishing Stack

Om de integratie tussen data-analyse, Python simulaties en het uiteindelijke scriptieverslag naadloos te laten verlopen, wordt de TU Delft Open Publishing Starterkit gebruikt in [`methanol-catalysis/`](file:///REDACTED_LOCAL_HOME/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/Methanol-Catalysis):

1. **Markdown First met LaTeX Math & Typst Output:**
   - Hoofdstukken worden geschreven in MyST Markdown (`content/*.md`) met LaTeX KaTeX syntaxis (`$...$` en `$$...$$`).
   - Typst (`export typst.yml`) genereert de primaire PDF (`exports/thesis.pdf`), wat zorgt voor snelle compilatie en strakke TU Delft thesis formatting zonder LaTeX-compile overhead.
2. **Reproduceerbaarheid via Pixi:**
   - Lokale compilatie en interactieve sessies verlopen strikt via Pixi: `pixi run preview` (webserver) en `pixi run pdf` (PDF build).
3. **Gescheiden Output via Selective Tagging:**
   - Interactieve widgets (bijv. ipywidgets sliders voor kinetische fits) of mermaiddiagrammen krijgen de tag `+++{"no-pdf":true}` zodat ze interactief renderen op het web, maar de PDF schoon houden.
   - Statische figuren met hoge resolutie worden geplaatst in `content/figures/`.
4. **Bibliografie Single Source of Truth:**
   - Zotero exporteert naar `references.bib` in de repo. Citaten worden ingevoegd via `{cite:p}` of `{cite:t}` conform MyST standaarden.

---

## 🕸️ 10. Knowledge-Graph Method (Inside-File Level 2)

Universele parse-methode voor "all things" (papers én workspace `state.md`-type files), O(n) lineair per chunk — géén O(n²) pairwise vergelijking.

| Stap | Script/File | Functie |
|---|---|---|
| Chunking | `Articles/scripts/kg_chunk.py` | Deterministic chunking: `.txt` (headings/blank-lines), PDF (pypdf), markdown (`#`); stabiele IDs `doc:sec:para:N` → `graph/chunks/<doc>.chunks.json` |
| Extractie | `graph/kg_extraction_workflow.md` | **In-session SOP**: 1× bounded-ontology prompt per chunk + 1× glean pass + doc-level consistency pass → `graph/paper_kgs/<doc>_run<N>.json` |
| Valideren | `Articles/scripts/kg_validate.py` | Schema-check + grounded-quote substring-check + citekey; sprint naar 0 failures |
| Merge | `Articles/scripts/kg_merge.py` | Concatenatie per-doc → `graph/knowledge_graph.json`; alias SAME_AS uit `aliases.yml`; support_counts |
| Query | `Articles/scripts/kg_query.py` | `--node/--search --hops`, `--grounded-only`, `--conflicts`, `--params`, `--concepts`, `--communities` |

**Provenance & Evidence (Rule 16):**
- `grounded` = quote is letterlijke substring van brondocument (auto-geverifieerd door validator). Citableerbaar.
- `llm_inferred` = waarde met `confidence` + `rationale`; **nooit** als `\cite{}`-basis (Rule 16). `--grounded-only` verbergt ze.
- Cross-doc bruggen (bv. Berger §5 transport-criteria ↔ Larsen §6.2.3 `r1,max` cap) worden als `llm_inferred` SEMANTIC_LINKS in `bridge_*.json` gemarkeerd.

**Node-types:** DOCUMENT, SECTION, PARAGRAPH, SPECIAL, CONCEPT, PARAMETER, METHOD. Edge-types: PART_OF, SPECIAL_IN, MENTIONS, USES, DEPENDS_ON, DERIVES_FROM, SUPPORTS, CONTRADICTS, SAME_AS, SEMANTIC_LINKS, CONTEXT_REF. Zie `graph/ontology.yml`.

---

## 🏗️ 11. Model-architectuur besluiten (30-09, vastgelegd)

Vastgelegd in het transcript van 29-09 en bevestigd in de audit [`3_Model/transient_model_framework_audit.md`](3_Model/transient_model_framework_audit.md). **Dit zijn besluiten, geen kandidaten** — §5 hierboven blijft gelden voor alles wat nog níét gekozen is.

1. **Drie gekoppelde niveaus:** bulkgas `C_b(z)` → film `C_s(z)` → intraparticle `c_p(z,r)` → oppervlaktebedekking `θ(z,r)`. State vector `[C_b, c_p, θ]`.
2. **`C_b` en `C_s` blijven apart in de code, worden gelijkgesteld om Berger's Eq. 1 te recupereren.** Motief: Berger Eq. 1 heeft géén filmterm — pseudo-homogeniteit *is* Bergers model. Zo krijgen we de uitbreiding gratis.
3. **Intraparticle diffusie is expliciet, nooit instant.** Eigen uitbreiding, geen Berger (diens state count is `(N_gas + N_surf) × N_z`). Moet in de scriptie als bewuste upgrade worden beargumenteerd.
4. **Snelheid = `[Arrhenius]` × `[Langmuir]`.** Complementaire assen, geen alternatieven: Arrhenius = `k(T)`, Langmuir = bedekkingsafhankelijkheid.
5. **Centered Arrhenius** voor `k_p(T)` (Berger Eq. 17) — mét de reden (binaire parametercorrelatie `< 0.71`), niet alleen de formule.
6. **Voorwaarts simuleren op literatuurwaarden; fitting is een latere, optionele stap.** Het framework hoeft geen fit om te draaien.
7. **Numeriek:** MOL; bulk-advectie = backward/upwind difference; particle-diffusie = centrale difference; tijd = impliciete BDF (`solve_ivp(method='BDF')`).
8. **Nieuw chemisch systeem = nieuwe elementaire stappen + stoichiometrie + snelheidswetvorm.** Engine blijft hetzelfde, zolang de snelheidswetten in de Langmuir/Arrhenius-familie blijven.

## §12 — Larsen (2024) als modelleringsbaseline: geverifieerd, en wat níét bruikbaar is

Vastgelegd 2026-10-03. Vervangt `Articles/analyses/bep_example_index.md` als bron voor kinetische parameters (§12.6).

### §12.1 Geverifieerd tegen de primaire tekst

- **Eq. 4.6–4.9** (`dF_i/dz`, vier molbalansen) verbatim bevestigd — `Ch4_Materials_and_Methods.txt:64-80`.
- **Eq. 6.9–6.11** (final Extended LHHW) verbatim bevestigd — `Ch6_Results_and_Discussion.txt:665-677`. Let op de asymmetrie: in `r1` is de volledige drieterm-noemer **gekwadrateerd**; in `r2` ontbreekt `K_H2 p_H2` in de noemer terwijl het in de teller blijft, en is `(1 + K_inh p_C2H2)^{n_inh}` een **fitted** niet-gehele exponent. Niet "corrigeren".
- **Steady-state in `z` alleen, géén tijdafgeleide.** Positief bewijs: Eqs. 4.6–4.9 + het stabilisatieprotocol (`Ch4:34-36`: elke GC-meting is een steady state na 7 minuten stabilisatie). **Schrijf nooit een "0 grep-hits"-bewijs voor deze bewering** — de zoekpatroon matcht structureel niet op "changes over time", en `Ch3:58` bespreekt wél tijdafhankelijke deactivering die nooit gemodelleerd is.
- **`Ch4:59-60` ("composition of the flow changes over time") is auteur-imprecisie** en betekent positie langs het bed, géén tijdsmodel. Niet citeren als dynamische-motivatie zonder deze correctie.
- **Fitting:** Differential Evolution, minimaliseert RMSE = Eqs. 4.14/4.15 — `Ch4:117-127`. RMSE in procentpunten; 4.15 is een **rekenkundig gemiddelde** per experiment.
- **Gerapporteerde overall RMSE 5.10 / 5.43 / 7.14** — `Ch6:678`, `Ch7:35`, `Ch1:21`. Deze bestán en zijn correct; zie §12.5 voor waarom ze ooit "niet reproduceerbaar" leken.
- **Table 4.1** (`Ch4:17-21`): Pd **0.025 / 0.05 / 0.1 wt%**, Ag **5 wt% bij alle drie**, ratio 200/100/50.
- ΔH: −172 en **−136** kJ/mol (`Ch4:68-69`).

### §12.2 níét bruikbaar — de parameters uit run2/consensus

Onze eigen `Articles/paper_analyses/larsenSemihydrogenationAcetyleneEthylene2024_run2.md` (waarden staan nu op `:107-112`, voorafgegaan door de intrekking op `:99-106`) en de `_consensus.md` noemen zes waarden (`k1=7.1852e-5`, `k2=1.0492e-5`, `K_C2H2=936.21`, `K_C2H4=10.21`, `K_inh=972.00`, `K_H2=3.3319`).

**Waarom niet bruikbaar — twee onafhankelijke gronden:**

1. **Onverifieerbaar vanuit onze tekstlaag, niet "bewezen onjuist".** De appendix zit níet in `pdf_full_extracted.txt` (die stopt op pagina 54); een nul-hit-grep op dat bestand bewijst dus niets over het document. De thesis zegt zelf dat de parameters ernaartoe verwijzen: *"The parameters used in each variant can be found in Appendix tables E.1 to E.3"* (`Ch6:436-437`). Zie §12.4.
2. **De set is sowieso onvolledig.** Er ontbreken `r_1,max` en `n_inh` — juist de twee termen die het *final model* definiëren (`Ch6:662-677`). Zonder `r_1,max` is Eq. 6.10 niet evalueerbaar. Onafhankelijk van verificatie onbruikbaar voor het final model.

Een derde observatie die níét als grond wordt gebruikt: `K_inh = 972.00` zit tegen de bovengrens die `run2` zelf opgeeft. Die bovengrens staat in **hetzelfde bestand** waarvan we de parameters intrekken, en de waarde hoort bij de *lineaire*-inhibitievariant terwijl `Ch6:749-752` het *final model* beschrijft met een fitted niet-gehele `n_inh`. Dat is geen tegenspraak die iets bewijst — het is reden om de set sowieso niet te gebruiken, niet om haar te weerleggen.

**Niet "gefabricieerd" noemen.** Een Jupyter-executieteller ("In [31]") is iets dat je van een screenshot leest, niet iets dat je verzint — de meest waarschijnlijke verklaring is dat run2 de rasterpagina's van Appendix F wél heeft gelezen en onze extractor niets. Dat blijft speculatie; zie quarantine.

### §12.3 Tweede open source-ambiguïteit die het coderen blokkeert

`A` (doorsnede) en `rho_support` (ondersteuningsdichtheid) in Eqs. 4.6–4.9 worden **nergens gedefinieerd** — geen doorsnede, geen bedlengte, geen voidage, geen pelletgrootte in de hele thesis. **Zonder deze twee is het model niet genormaliseerd** en is er geen conversievoorspelling. Deze zijn alleen te achterhalen uit de raster-pagina's van Appendix F, of moeten expliciet als eigen modelleringsaanname worden gekozen en gedocumenteerd. Net als §10 is dit een open beslispunt, géén vrijbrief om waarden te verzinnen.

### §12.4 Volgende verificatiestap (mechanisch, goedkoop — nog niet gedaan)

Renders paginas 71–76 (Appendix E) en 77–88 (Appendix F) van `Articles/2 meeting Damian + Zoë/BEP Example.pdf` (97 pp) **als afbeelding** en lees ze. Zeven appendix-paginas hebben geen tekstlaag; `p.81` en `p.87` — precies de pagina's die run2 citeert — zitten daartussen. Dit is de goedkoopste manier om §12.2 te sluiten en tegelijk `A`/`rho_support` en de numeriek (solver, grid, tolerantie, DE-bounds) te bemachtigen. Route: `av-inspector` (Rule 31).

### §12.5 Aangetoonde extractie-contaminatie (instanties bevestigd; omvang níét gemeten)

Deze instanties zijn **verifieerd** — Larsens tekst staat als "eigen" quote in andere papers' extractiebestanden:

- `wangProbeEffectsSurface2020_run1.md:130,134,135` — *"…overall RMSE values of 5.10, 5.43, and 7.14 percentage points for Pd 0Ag,"* toegekend aan "Page 7" van Wang 2020 (werkelijke bron `Ch1:21`); idem `:134` → "Page 43".
- `zhangSelectiveHydrogenationAcetylene2014_run2.md:112,122,124`, `ballAgPdCuPdCatalysts2020_{run1,run2,consensus}.md`, `borodzinskiKineticModelHydrogenation2000_consensus.md:142`.

Gevolg: **deze** RMSE-fragmenten zijn over documenten en modelvarianten heen samengevoegd. Dat verklaart waarom "5.10/5.43/7.14" ooit afwezig leek in Appendix E — gezocht naar een tabel die per variant en per katalysator is opgesplitst.

⚠️ **Omvang niet gemeten.** Het voorkomen van contaminatie is vastgesteld; **de totale omvang over de ~141 pipeline-uitvoeren is níet onderzocht** en kan veel groter of kleiner zijn. De gevolgtrekking "de Key Quotes van het 2-pass-pipeline zijn niet automatisch geldig" is daarom een **voorlopige** regel, geen gemeten uitkomst. Eén grep beslist het: zie `.agents/resources/runbooks/verifying-extraction-claims-against-pdf-text-layer.md` § Cross-contamination. Open vraag staat in `.agents/quarantine/2026-10-03-1522-larsen-parameter-provenance.md` §6.

### §12.6 Gedegradeerde bronnen — `bep_example_index.md`

`Articles/analyses/bep_example_index.md` is **een navigatiehulpmiddel, geen parameter- of feitenbron**. Geverifieerde fouten:

- **De katalysatorserie staat achterstevoren.** `:29-30` bouwt een verhaal op "monometallic Pd over-hydrogenates"; Pd0Ag is in werkelijkheid de *meest* Ag-verdunde katalysator (5 wt% Ag, `Ch4:19`).
- **Pd-lastings verkeerd** (`:30,:102-104` noemt 0.04 wt% Pd en 0.00/0.08/0.12 wt% Ag) → Table 4.1 is 0.025/0.05/0.1 wt% Pd, 5 wt% Ag.
- **Gefabriceerde processtappen** (`:101` "dried 110 °C, calcined 450 °C, reduced 400 °C") — komen niet in de thesis voor; werkelijk: 12 h drogen op 80 °C en pretreatment 250 °C (`Ch4:14-15,:28-32`).
- **Verzonnen geometrie** (`:105` "1/4'' OD, 4 mm ID") — de thesis geeft geen reactordiameter.
- **SiC-fout** (`:105,:118` "50 mg + 450 mg SiC in de reactor") — SiC komt alleen voor in H₂-TPR, en daar 150 mg + 300 mg (`Ch4:227-229`).
- **ΔH −137** (`:63`) → −136. **Selectiviteitsformule** (`:108`) heeft `2C_{4+}` in de teller en ongebalanceerde haakjes.
- **"Julia/SciML"** (`:19,:138`) is een bewering over ónze eigen solver, niet over Larsen, en is ongedekt. Onze stack is Python/SciPy (`solve_ivp`); de fosterf staat óók in `larsenSemihydrogenationAcetyleneEthylene2024_run1.md:112`.

---

**Open source-ambiguïteit die het coderen blokkeert:** of `$u_s$` in Berger Eq. 1 superﬁcieel of interstitieel is. [`dynamic_kinetics_berger2008.md:30`](Articles/analyses/dynamic_kinetics_berger2008.md) noemt `$u_s/\varepsilon$` de "interstitiële snelheid", maar de balans heeft géén `$\varepsilon_b$` op de accumulatieterm. De twee lezingen verschillen `$\varepsilon_b^2$` (~6.25× bij `$\varepsilon_b$=0.4) op de dominante convectieterm. **Tegen de PDF checken vóór er code voor wordt geschreven** — het bepaalt `$f_{max}` en de hele numerieke schaal.

---

## §13 — BEP Scientific Reference and Personal Map Conventions (2026-10-21)

1. **Two different ownership roles.** The AI reference map may be expanded by AI without individual owner approvals, with provisional scientific ideas and evidence-grounded explanations. It **must not progress beyond the AI-developed/yellow stage**. A separate owner-directed personal understanding map or layer is changed only after the owner's explicit approval of the change. Do not infer human understanding from AI synthesis, source links, inclusion in a graph, or a scientific test.
2. **Scientific maturity ceiling.** The intended maturity model is Idea (grey), AI worked out (yellow), Human worked out (blue). Reference-map content may only be grey or yellow. Blue is available only for the personal map after explicit owner authorization; retain a specific approval record and provenance. Structural approval and source-claim verification are independent from maturity.
3. **Approval must be explicit and scoped.** Do not use automatic draft-to-canonical promotion to represent human understanding. Until the API can enforce approval cleanly, disable/avoid the legacy promotion path that defaults to `new_tier=2`. Never automatically mark sources human-verified.
4. **Backend is the source of truth, not the frontend.** The graph viewer may omit or misunderstand metadata without redefining the stored scientific information. However, current Pydantic `extra="ignore"` can also discard unknown fields during backend parsing/serialization; the eventual backend schema migration must explicitly preserve and validate all metadata before adding unsupported keys to live YAML.
5. **Proposal-anchored, expansive research execution.** No arbitrary upper limit on nodes, depth or scientific investigation in this execution, but the original BEP proposal is the center of gravity. Prioritize 1D packed-bed reactor modelling, acetylene semi-hydrogenation, surface kinetics, flow and pore transport, PDE/ODE numerical analysis, transient forcing, yield/selectivity, identification, filtering and control. Investigate additional science when it meaningfully supports, challenges, validates or extends those aims; explain the relevance and distinguish foundational support from future research, instead of encyclopedic expansion for its own sake.
6. **Scientific hierarchy.** One BEP root, three scientific disciplines (Physics, Mathematics, Systems & Control); lower levels are proposed topics revised iteratively. The A–M letters are research dossiers to mine and cross-link, not the mandatory scientific topology. The two important C1 children are Reaction Chemistry & Pathways and Catalyst Chemistry & Active Sites. No artificial depth limit.
7. **Backend file implementation remains provisional.** The current `data/bep_map.yaml` and `data/bep_draft_overlay.yaml` are the existing four-record base and expanding AI overlay, not proof that a complete two-map workflow has been implemented. Preserve all stable IDs, existing material, and the approval boundary while planning the personal-map representation. Do not silently reinterpret legacy `tier:0..4` or overwrite the curated overlay with the older synthesis graph.
8. **Map-specific authoring versus general reversible persistence.** [`bep-map-edit-review`](../../../.agents/skills/bep-map-edit-review/SKILL.md) is the **map-specific authorization and response-to-feedback skill**: AI grey/yellow references may be authored autonomously, whereas the owner's personal/blue graph changes need explicit owner approval for the precise edit. If the owner complains, inspect and correct narrowly; never panic-delete or reset the whole map. [`reversible-change-review`](../../../.agents/skills/reversible-change-review/SKILL.md) separately handles read/edit/diff/commit/push/pull-and-compare/revert for ANY reversible saved change; the Git diff verifies the mutation, not scientific truth. The two skills and [map README](mindmap/README.md) must be reviewed/maintained alongside parser/frontend/schema changes, in the same PR. Preserve independent science-edit commits rather than squash-merging multi-edit data PRs when one-commit revert granularity matters.
9. **Current task and independent reconstruction.** The requested new cloud Work task is **independent scientific DATA reconstruction from the original proposal**, in a new isolated dataset. Preserve the earlier 69-node AI reference map as a versioned comparison control and embargo it as an input until the new v1 baseline is frozen; do not delete it merely for temporary blindness. Do not rewrite the frontend or backend application absent a concrete blocker. The original BEP proposal remains the center of gravity; no arbitrary node-count/depth cap.

