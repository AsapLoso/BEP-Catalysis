# Dual BEP Catalysis: Mathematical Modeling & Kinetics of Acetylene Semi-Hydrogenation

> [!IMPORTANT]
> **Wednesday presentation work: start at the [repo-wide coordination page](../../../WEDNESDAY_START_HERE.md).** All contributing chats should check the [presentation Wayfinder](research/wayfinder/bep_presentation_2026_10_14.md) and link new work there.

**Student:** Lucas van Dekken (Double BSc Applied Mathematics & Applied Physics, TU Delft)  
**Research Group:** Catalysis Engineering Group (ChemE / TNW) & Numerical Analysis (TW / EEMCS)  
**Supervisors:** ⚠️ **ONBEVESTIGD — zie [`state.md`](./state.md) § Status "Supervisieconflict" (canoniek).** Deze regel noemde Damian Vico van Berkel, Zoë Gromotka **en Prof. dr. Atsushi Urakawa**, en is de bron geweest van een foutieve bio die naar een openbare TU-pagina zou gaan. Vier bestanden in deze map geven vier verschillende supervisoren; gebruikersstand 2026-09-29: *"Bera no longer main supervisor"*. **Niet als vastgesteld gebruiken tot de gebruiker de actuele supervisie bevestigt.**

---


## BEP Intellectual Reclamation — current map handoff (2026-10-22)

**Fresh-chat entry point.** If the user asks *“look at the BEP intellectual reclamation project in GitHub and continue”*, first open the **[manual scientific-map session README](https://github.com/AsapLoso/project-management-agents/blob/docs/bep-theme-first-progress-units-20261022/Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/README.md)**, followed by the **[latest owner-map state](https://github.com/AsapLoso/project-management-agents/blob/docs/bep-theme-first-progress-units-20261022/Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/state.md)** and **[theme-first authoring insight](https://github.com/AsapLoso/project-management-agents/blob/docs/bep-theme-first-progress-units-20261022/Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/THEME_FIRST_PROGRESS_UNITS_2026_10_22.md)**.

These files are on **[draft PR #186](https://github.com/AsapLoso/project-management-agents/pull/186)**, built on **[manual-map PR #182](https://github.com/AsapLoso/project-management-agents/pull/182)**. The separate AI scientific reference dataset is in PR #180. Check latest branch/PR statuses and read actual files; do not assume an unmerged PR is present on `devcontainer`.

**Crucial design correction:** build the personal map to track independently assessable scientific questions. Under `Reaction Chemistry & Pathways → Our Reactions`, list R1/R2/R3 inside the parent node, split by investigative **themes**, and allow R1/R2/R3-specific progress under each of **exactly two currently selected themes** (**six independently assessable work units**): microscopic pathways and viability/conditions. **No third theme is requested.** The old 8-node YAML is **not yet migrated**. No automatic human-understood or human-verified promotions; source citations and owner knowledge have independent status. Continue discussing the graph with the owner rather than beginning a new reference-research campaign. **Parallel frontend Work:** [execution goal](https://github.com/AsapLoso/project-management-agents/blob/docs/bep-theme-first-progress-units-20261022/Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/FRONTEND_WORK_GOAL_2026_10_22.md) (implementation starts from `devcontainer`; scientific owner-map files stay isolated).

---

## 🎯 Project Scope

This project focuses on the dynamic 1D spatial + 1D temporal continuum modeling and simulation of a Packed Bed Reactor (PBR) for selective acetylene semi-hydrogenation ($C_2H_2 + H_2 \rightarrow C_2H_4$). It combines rigorous transport phenomena (Péclet and Damköhler scaling, axial dispersion, intra-pellet diffusion) with non-linear reaction kinetics (extended Langmuir-Hinshelwood rate equations) and candidate dynamic excitation/optimization techniques.

---

## 📂 Directory Layout

- **[`state.md`](state.md):** Current active project state, action items, open communication lines, and committee status.
- **[`conventions.md`](conventions.md):** Directory conventions, Zotero citation workflows, and branch guidelines.
- **[`history.log`](history.log):** Historical record of completed tasks and project milestones.
- **[`resources.md`](resources.md):** Primary reference library, literature reviews, textbook links, and meeting notes.
- **[`committee_candidates.md`](committee_candidates.md):** Candidate profiles and draft outreach for the defense committee.
- **[`thread_examencommissie_paula.md`](thread_examencommissie_paula.md):** Correspondence log with the TN Board of Examiners.
- **[`0_Project_Management/`](0_Project_Management/):** Proposal LaTeX sources (`main.tex`), compiled PDFs, Zotero sync scripts, and archived writing transcripts.
- **[`1_Transport_Phenomena/`](1_Transport_Phenomena/):** Derivations and notes on PBR transport equations and scaling laws.
- **[`3_Model/`](3_Model/):** Executable transient PBR model track (Method of Lines, `solve_ivp(method='BDF')`), with its own four-file convention and defect register. Theory stays in `1_Transport_Phenomena/`.
- **[`Articles/`](Articles/):** Literature repository with 28+ acquired papers, chronological meeting dossiers, synthesis indices (`Articles/analyses/`), and extraction tools (`Articles/scripts/`).
- **[`Code/`](Code/):** Python and simulation scripts for kinetics and reactor reproduction.
- **[`Meetings/`](Meetings/):** Agendas, preparation notes, and minutes for supervisory meetings.


## Wednesday presentation knowledge hub

- [**Presentation structure — A–M, all deep dives, narratives and future script**](presentation/PRESENTATION_STRUCTURE.md) · [deep-dives folder](presentation/deep-dives/) — canonical starting point for the end-presentation research structure; **not yet** the final spoken script.

- [Wednesday presentation Wayfinder map](research/wayfinder/bep_presentation_2026_10_14.md) — active presentation frontier, open decisions, and links across the Catalysis project.
- [First presentation checkpoint — imported draft](presentation/README.md) — ten-slide HTML deck and editable Word outline, available on `devcontainer`, still subject to scientific/owner review.
- [Presentation checkpoint audit](research/dossiers/presentation_checkpoint_audit_2026_10_14.md) — narrative rationale, QA, evidence boundaries and remaining editorial questions.
- [Source dump capture](research/wayfinder/user_dump_capture_2026_10_13.md) — the work named in the 13 October planning dump, with unknowns kept explicit.
- [**Supervisor briefing (13 October 2026)**](research/briefing/BEP_SUPERVISOR_BRIEFING_2026-10-13.md) — canonical, evidence-tagged; with [spoken update](research/briefing/spoken_update.md), [technical Q&A](research/briefing/technical_qa.md), [Wednesday handoff](research/briefing/wednesday_handoff.md) and [evidence bundle](research/briefing/evidence/README.md).
- [Scientific reconnaissance dossier](research/dossiers/scientific_wayfinder_2026_10_13/README.md) — research synthesis, simulator review, provenance, and audit receipts gathered from the parallel work.
- [Master document map](DOCUMENT_MAP.md) · [Thesis-wide Wayfinder](research/wayfinder/bep_catalysis_master.md) · [Scientific method-selection Wayfinder](research/wayfinder/scientific_method_selection.md) · [Project state](state.md)
