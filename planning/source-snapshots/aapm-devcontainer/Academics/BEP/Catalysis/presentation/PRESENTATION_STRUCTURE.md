> **GESPREKSSTATUS: K = GEDEELTELIJK GEËVALUEERD; L EN M = NIET BESPROKEN / NIET GEËVALUEERD.** De Markdownonderzoeken van L en M zijn door de assistant opgesteld, maar de gebruiker heeft die inhoud nog niet samen met ons besproken. Behandel geen van deze drie letters als volledig geëvalueerd of als goedgekeurde presentatie-inhoud.

# BEP — Final presentation structure and research file map

**Updated:** 14 October 2026. **Status:** Working master structure; **not yet the final slide order or a spoken script**. This file is a single entry point to the evidence behind the eventual end presentation.

**Open the full [deep-dives folder](deep-dives/) · [A–M central research index](RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [deep-dive re-entry guide](deep-dives/README.md).**

All links below are **relative to this structure file**, so they work in GitHub and in a local clone. Each letter is currently a research question, **not automatically a slide**. Only the completed letters have their own document; avoid dead links.

## A–M: research modules and where to find them

| Letter | Topic | File or source | Current state |
|---|---|---|---|
| **A** | Scientific question and project objective | [A–M index, section A](RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) | Open; dedicated deep dive not yet created |
| **B** | Literature and source provenance | [Deep dive B](deep-dives/B_literature_priority_2026-10-14.md) | Documented, with outstanding source-verification questions |
| **C** | Mechanism, intermediate sites, selectivity and omitted reactions | [Deep dive C](deep-dives/C_reaction_mechanism_2026-10-14.md) | Documented, including the direct acetylene-to-ethane follow-up |
| **D** | Rate laws, parameters, uncertainties and identifiability | [Deep dive D](deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md) | **Documented** — 2019 ledger, identifiability, limitations; parameter transfer unresolved |
| **E** | Actual reactor regime, catalyst, feed and transport timescales | [Deep dive E](deep-dives/E_operating_regime_transport_2026-10-14.md) | **Documented** — 3 configurations distinguished; paper Table 7, baseline timescales and code-note inconsistencies |
| **F** | Gas, pellet and surface balances; physical state space | [Deep dive F](deep-dives/F_conservation_state_space_2026-10-14.md) | **Documented** — 1,480 vs 240 states, pore/bulk flux conservation question; core state-space slide candidates |
| **G** | Numerical schemes, stiffness and computational feasibility | [Deep dive G](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md) | **Documented** — full methods comparison, stiffness, Jacobian/sparsity and open Zoë questions |
| **H** | Original 1,480-state model spotlight | [A–M index, section H](RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) | Open |
| **I** | Source-backed reacting vertical slice spotlight | [A–M index, section I](RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [**🚩 OVERWEEG — optional narrative 05**](sub-stories/05_reacting_model_inlet_candidate.md) | **Scoped / full I dive deferred by user**; optional presentation transition only, **NOT selected** |
| **J** | Numerical/scientific verification and corrections | [A–M index, section J](RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) | Open |
| **K** | Results and their validity | [K — no validated reactor-result claim yet](deep-dives/K_results_validation_status_2026-10-14.md) | **NIET VOLLEDIG GEËVALUEERD** — only preliminary-output validity discussed; original K topics (reacting simulation, sensitivity, periodic test) await user review |
| **L** | Outlook: periodic optimisation, physics needed and future extensions | [Deep dive L](deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md) · [Narrative 03](sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md) | **NIET BESPROKEN / NIET GEËVALUEERD** — door assistant opgestelde research beschikbaar; nog geen gebruikersbeoordeling of slidekeuze; geen optimisatieresultaat |
| **M** | Edit the global story and review the real first deck | [M — editorial synthesis and PR #4 review](deep-dives/M_editorial_synthesis_pr4_2026-10-14.md) · [actual ten-slide Work PR #4](https://github.com/AsapLoso/project-management-agents/pull/4) | **NIET BESPROKEN / NIET GEËVALUEERD** — assistant heeft een conceptredactie geschreven, maar gebruiker heeft deze nog niet beoordeeld; PR #4 op 15-10-2026 om 22:40:12Z gemerged in devcontainer (merge commit faa678b865e044188ecb827513e5079cc88ebcd2); 27 standalone conceptbestanden zijn op 16-10 als gekopieerd geregistreerd; niet goedgekeurd |

**Current reality:** B–G and L–M have dedicated deep-dive files; K has a results-validity status note; I was scoped to an **optional** narrative (full dive deferred). A, H and J remain open in the A–M index. These letters are research modules, **not slide numbers**. The ten-slide deck and editable outline are now available **on devcontainer** as a preserved draft: [deck](BEP_Dynamic_Acetylene_Progress.html), [editable outline](BEP_Presentation_Outline.docx), [source ledger](CLAIM_SOURCE_CHECKLIST.md) and [QA](QA_REPORT.md). [PR #4](https://github.com/AsapLoso/project-management-agents/pull/4) merged into `devcontainer` on 15 October 2026 at 22:40:12Z (merge commit `faa678b865e044188ecb827513e5079cc88ebcd2`). A 16 October history entry separately records 27 standalone artifacts as imported verbatim, without overwriting BEP state/history; overlap with the PR #4 diff has not been independently audited. Its original branch remains preserved. **No user approval or scientific model validation is implied.**

**Deck-wide OPEN supervisor agenda (Zoë, F + G):** [DECK_OPEN_QUESTIONS.md](DECK_OPEN_QUESTIONS.md). **User preference:** review **full letter content** and tentative editorial picks at top before selecting compact presentation bullets; F/G are questions to discuss, not yet sent or approved. The parallel deck session should consult this file before locking slides.

**First global editable presentation checkpoint (ARCHIVED PR #4; BRANCH PRESERVED, NOT APPROVED):** [PR #4](https://github.com/AsapLoso/project-management-agents/pull/4) · [actual global bullet outline](https://github.com/AsapLoso/project-management-agents/blob/codex/bep-presentation-2026-10-14/Academics/BEP/Catalysis/presentation/GLOBAL_PRESENTATION_OUTLINE.md) · [offline HTML deck](https://github.com/AsapLoso/project-management-agents/blob/codex/bep-presentation-2026-10-14/Academics/BEP/Catalysis/presentation/BEP_Dynamic_Acetylene_Progress.html) · [Word outline](https://github.com/AsapLoso/project-management-agents/blob/codex/bep-presentation-2026-10-14/Academics/BEP/Catalysis/presentation/BEP_Presentation_Outline.docx). **Editorial review/questions** live in [M](deep-dives/M_editorial_synthesis_pr4_2026-10-14.md). PR #4 merged into `devcontainer` on 15 October 2026 at 22:40:12Z (merge commit `faa678b865e044188ecb827513e5079cc88ebcd2`); integrate only owner-approved content into any future fresh branch rather than treating the checkpoint as final.

## Narratives, planning, and presentation files

**Presentation-story source material (distinct from the A–M taxonomy):**

- [Sub-stories directory](sub-stories/)
- [01 — Three concentrations to state space](sub-stories/01_three_concentrations_to_state_space.md)
- [02 — Proposal to predictive optimisation](sub-stories/02_proposal_to_predictive_optimization.md)
- [03 — Urmès 2019 to 2022, future transient kinetics and continuous pellet-radius distribution](sub-stories/03_urmes_2019_2022_and_pellet_size_distribution.md)
- [04 — Can we identify parameters from noiseless cyclic simulations?](sub-stories/04_model_fidelity_and_identifiability.md) — **short presentation argument**; E's extensive transport audit stays background research, not an intended presentation section
- [05 — 🚩 OVERWEEG / NIET BESLOTEN: source-backed reacting simulator with time-dependent inlet](sub-stories/05_reacting_model_inlet_candidate.md) — **optional bridge only**, do not automatically make a slide; user declined full I technical exploration for now.
- [Optional presentation gags / lighter moments](sub-stories/visual_gags.md)

**Prior planning and prototypes (do not assume final/validated):**

- [Wednesday deck plan — earlier 8-slide candidate](WEDNESDAY_DECK_PLAN_2026-10-14.md)
- [Presentation folder README](README.md)
- [Notebook prototype](BEP_Catalysis_Presentation_v1.ipynb) · [HTML stage prototype](BEP_Notebook_Presentation_v3.html) · [stage generator](build_bep_notebook_stage.py)
- [Presentation Wayfinder, planning and dependencies](../research/wayfinder/bep_presentation_2026_10_14.md)

**Research evidence to consult:**

- [Project state / tasks](../state.md) · [source links for Zotero-import review](../Articles/links.md) · [project literature resources](../resources.md)
- [Primary-literature reuse audit](../research/dossiers/scientific_wayfinder_2026_10_13/literature_reuse.md)
- [Urmès 2019 parameter/rate-law source receipt](../3_Model/probes/urmes2019_source_receipt.json)
- [Legacy model](../3_Model/c2h2_hydrogenation_transient_model.py) · [legacy numerical audit](../3_Model/state.md) · [framework audit](../3_Model/transient_model_framework_audit.md)
- [New reacting model on Hermes branch](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py)
- [Experimental non-PSSA surface bridge — PR #3 merged 16 Oct 2026 into Hermes research branch; opt-in and scientifically unvalidated](https://github.com/AsapLoso/project-management-agents/pull/3)

## Later: turn research material into a concrete script

The A–M files are **research preparation**. They should eventually feed a **selective narrative and concrete spoken presentation script**, not thirteen compulsory sections of slides. A tentative path to discuss is: project question → physical chemistry → why we chose or changed models → old and new model spotlights → what has actually been verified → unresolved questions and prospects.

**When a new deep dive is finished:** create or update its Markdown document in the [deep-dives directory](deep-dives/), replace this table's index-only pointer with its real **relative link**, and cross-reference it from the [A–M research index](RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md). Start each new chat/dive by rereading that index and the [deep-dive re-entry guide](deep-dives/README.md), not by relying on a long chat history.

**Path choice:** We deliberately use portable relative Markdown links instead of hard-coded personal Windows absolute paths. Separate-branch GitHub URLs are absolute because their files do not exist on this branch.
