# Wayfinder: BEP R1–R3 reaction-pathway source evidence

> **Noun locks:** R1/R2/R3 name net gas-phase stoichiometric transformations, **not automatically three independent microscopic mechanisms or kinetic rate laws**. The three suggested individual-reaction children are **Ideas, not approved or read owner-map nodes**. "Verified by AI" never means human-verified.  
> **Owning dossier:** `Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/state.md`; personal-map reference is `current_map.yaml`, pending additions in `bridges.yaml`.  
> **Charting trigger:** owner asked 2026-10-22 to record exactly R1, R2 and R3 as research ideas; consult existing repository science first. An article among the original three sent by Damian might be relevant; exact identity/upload status is **not established**.  
> **Hard stops:** This charting pass performs **no new literature search**, no personal-map node insertion, no owner reading/approval/blue promotion, no changes to integrated source graph or reactor code. Later research tickets may investigate original sources, but they cannot assert a verified BEP mechanism without catalyst-specific evidence.  
> **Grammar:** `wayfinder-maps` ticket grammar; the map plans source/interpretation decisions and does not carry out research.

## 1. Destination

Establish, using actual cited passages and stated catalyst/experimental context, the net chemistry and defensible microscopic pathway alternatives for each of **R1**, **R2** and **R3**, so the owner may later review three proposed direct children of the approved `own_ph_net_hydrogenation` branch **one at a time**.

**Three active open research tickets** (R1, R2, R3); all **idea/unverified at personal-understanding level**, with AI research allowed to reach `ai_worked_out`. Each ticket closes only with a source-and-claim ledger: existing map node IDs, primary bibliographic IDs, exact section/page/table/equation and short accurate quote where accessible, a bounded mechanism interpretation, unverified items, and recommendation for the next *proposed* owner-map node. No owner content/reading/citation verification implied.

**Read-first references (not proofs by themselves):**
- Primary BEP proposal/bibliography: `Academics/BEP/Catalysis/0_Project_Management/main.tex`, `0_Project_Management/references.bib`.
- Existing integrated graph: `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/nodes.yaml`, `sources.yaml` (AI reference PR #180, known scientific head `1cd680f95902a0a79b17afb084fa29ab49c6b25f`).
- Current individual-reaction sketch: `Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/current_map.yaml`; node `own_ph_net_hydrogenation` already stores all three balanced equations within ONE node.
- Previously identified primary evidence candidates: **Urmès et al. 2019**, `urmes2019` (full text previously inspected, printed pp. 2–6 and 9–11); **Mei, Neurock & Smith 2009**, `mei2009` (abstract/preview access); **Bos & Westerterp 1993**, `bos_westerterp_1993` (bibliographic/abstract-level attachment, full-text specific pathway claim not yet verified); **Borodziński & Cybulski 2000**, `borodzinski2000` (AI source-access records differ across passes; reopen original rather than trusting inherited access flag). Where appropriate check `pachulski2012` (PdAg/Al₂O₃ abstract), `lan2025` (review abstract).
- Potential original three Damian-shared papers: **identify actual email/reference identifiers and repository holdings if needed**; do not assert which paper or that it was uploaded.

## 2. Decisions So Far

- [x] **2026-10-22 — Three stoichiometric expressions are known:** R1 = C₂H₂ + H₂ → C₂H₄; R2 = C₂H₄ + H₂ → C₂H₆; R3 = C₂H₂ + 2H₂ → C₂H₆. These equations were user-discussed and are recorded inside `own_ph_net_hydrogenation` without asserting three kinetic mechanisms.
- [x] **2026-10-22 — R3 is algebraically dependent on R1/R2:** the R3 net stoichiometric vector equals R1 + R2; this neither proves nor excludes a separate microscopic route to ethane.
- [x] **2026-10-22 — Ideas only:** Owner asked for individual-reaction deep-dive research tickets, not immediate personal-map insertion or source/human-understanding verification.
- [x] **2026-10-22 — Existing evidence first:** use original proposal, reference map and cited studies before looking for further literature; missing Damian attachments remain an open locator question, not an established absence.

## 3. Active Frontier

### Island: R1 Semi-hydrogenation

- [ ] **R1 Determine supported routes to ethylene** (`wayfinder:research`) — *Question: Which source-inspected net and surface mechanisms account for C₂H₂ + H₂ → C₂H₄, under exactly which catalyst/feed conditions and with what claim-specific evidence?*
  - Status: **Open — Idea**, no owner-read or scientific approval.
  - Mode: **AFK research in a future wave**; no new search in this map-authoring session.
  - Dependencies: existing source catalogue `urmes2019`, `mei2009`, `ph_sequential_path`, `c1_acetylene_semihydrogenation`, and any source that is actually identifiable in Damian's references.
  - Evidence target: distinguish gas net equation, adsorbed intermediates/Horiuti–Polanyi model choices, observed products and the separate question of actual target PdAg pathway.
  - Deliverable: claim-by-claim short quotation/locator + interpreted support + unresolved mechanism alternatives; proposed child `R1` only in bridge ledger until owner placement approval.

### Island: R2 Ethylene over-hydrogenation

- [ ] **R2 Determine supported routes to ethane from ethylene** (`wayfinder:research`) — *Question: Which measured or modelled pathways justify C₂H₄ + H₂ → C₂H₆ and distinguish gas-phase ethylene readsorption from continued hydrogenation of surface-bound intermediates under the stated conditions?*
  - Status: **Open — Idea**, no owner-read or scientific approval.
  - Mode: **AFK research in a future wave**.
  - Dependencies: `urmes2019` (two-rate fitted network, supported Pd), `mei2009` (idealized Pd/PdAg model), `c1_ethylene_overhydrogenation`, `ph_sequential_path`.
  - Evidence target: net product evidence versus elementary site route; ethylene in the feed versus produced ethylene; conditions and detection/measurement limits.
  - Deliverable: source-passage list and bounded interpretation; proposed child `R2` remains a bridge until explicitly placed.

### Island: R3 Acetylene-to-ethane overall conversion

- [ ] **R3 Test evidence for an independent path** (`wayfinder:research`) — *Question: Does accessible primary evidence support any kinetically distinguishable route from acetylene to ethane without free-gas ethylene as an obligatory intermediate, and in which catalyst/regime, rather than merely the sum of R1 and R2?*
  - Status: **Open — Idea; independent route not established for target BEP catalyst**.
  - Mode: **AFK research in a future wave**.
  - Dependencies: `c1_parallel_ethane_paths`, `c1_vinyl_ethylidene_alternative`, `bos_westerterp_1993` (historical/unverified claim attachment) and `mei2009` (abstract-level idealized-surface model); check actual source full text if accessible, not only AI interpretations.
  - Evidence target: separate (a) overall 2H₂ net equation, (b) hydrogen addition via adsorbed ethylene-like intermediate without gas desorption, (c) bypass through another adsorbate family, and (d) independent identifiable fitted rate. Avoid equating these.
  - Deliverable: source-verified *by AI* quotation/locator and explicit evidence gap or model-specific support; proposed child `R3` remains a bridge until owner approval.

## 4. Not Yet Specified (The Fog of War)

### Island: R1 Semi-hydrogenation

- After candidate mechanisms are anchored, determine whether distinct R1 child nodes are necessary for site families, H adsorption, ethylene desorption or catalyst-specific constraints.

### Island: R2 Ethylene over-hydrogenation

- Future regime-specific branching (ethylene-rich tail-end feed, adsorbate coverages, support and metal composition) must depend on what the primary papers actually support.

### Island: R3 Acetylene-to-ethane overall conversion

- Determine which of Damian's initial three papers, if any, contributes specific evidence; filenames/mail attachments and full text are not yet established.
- Decide whether an independent third kinetic-rate expression is warranted, observationally identifiable or only a mechanistic possibility after reading primary evidence.

## 5. Out of Scope

- New searching, fetching new articles or resolving the three tickets in the **current note-taking session**.
- Automatic insertion/approval/blue status of R1–R3 in the owner's map.
- Universal Pd/PdAg chemistry claims, copied quantitative kinetics, or a third fitted rate based only on the balanced R3 equation.
- Catalyst parameter fitting, transient simulator development, waveform optimization or experimental performance claims.
- Automatic promotion of AI-attached citations to human-verified.

## 6. Execution Contract

- verification_cmd: `pixi run python Academics/BEP/Catalysis/research/wayfinder/validate_bep_reaction_pathway_evidence_map.py`
- scoped_commit_files: `Academics/BEP/Catalysis/research/wayfinder/bep_reaction_pathway_evidence_2026_10_22.md, Academics/BEP/Catalysis/research/wayfinder/validate_bep_reaction_pathway_evidence_map.py, Academics/BEP/Catalysis/research/wayfinder/bep_reaction_pathway_evidence_prompts.md, Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/bridges.yaml, Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/state.md`
- commit_message: "docs(bep): park R1-R3 source-research ideas in a focused Wayfinder"
