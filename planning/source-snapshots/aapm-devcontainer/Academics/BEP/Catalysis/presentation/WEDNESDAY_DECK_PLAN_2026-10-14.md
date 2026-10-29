# Wednesday BEP presentation — production plan
**Date:** Wednesday 14 October 2026 · **Prepared:** Tuesday 13 October
**Status:** Committed content/production plan; **not** a completed or approved deck.
**Source of truth:** [Wednesday entry](../../../../WEDNESDAY_START_HERE.md), [presentation Wayfinder](../research/wayfinder/bep_presentation_2026_10_14.md), [evidence briefing](../research/briefing/BEP_SUPERVISOR_BRIEFING_2026-10-13.md).
**Provisional audience/duration:** research-progress update with supervisor; target 8–10 minutes of core slides. If time differs, trim or expand, not start over.

## One-sentence thesis
**Can time-varying reactor input improve ethylene yield in acetylene semi-hydrogenation, and what model must we build to test that hypothesis honestly?**

Present a **research-progress narrative**, not a claim of completed reactor validation: **question → proposal → what literature changed → mathematical implementation → verified evidence → missing physics → next experiment**.

## Main deck: eight slides

| # | On-screen headline | Main visual / content | Point to say aloud | Evidence / guardrail |
|---|---|---|---|---|
| 1 | **Can a changing feed outperform steady operation?** | Reaction chain C₂H₂ → C₂H₄ → C₂H₆, with ethylene highlighted; steady vs oscillating inlet schematic. | Conversion competes with selectivity; dynamic feeding is the *hypothesis* to test. | Proposal; do **not** say yield improvement is demonstrated. |
| 2 | **Our proposal: predict, then optimise** | Clean pipeline: periodic inlet u(t) → 1D reactor model → ethylene outlet → compare cycle-averaged yield. | The primary deliverable is an open-loop predictive model, followed by input optimisation. MPC/observers are later possibilities. | Original project proposal. |
| 3 | **Literature changed the modelling choices** | Three source cards connected to one revised architecture: Berger 2008 (transport + surface dynamics, MoL/BDF); Urmès 2019 (steady kinetic parameter set); Urmès 2022 (periodic-operation comparator, not yet inspected). | Separate an available steady-state *parameter* paper from a relevant but **unread** periodic-operation paper. | Briefing §§2 and 5; no inference about unread 2022 paper details. |
| 4 | **From physical fields to a state vector** | Packed-bed + pellet cutaway, labeled C_bulk(z), C_pore(z,r), θ(z,r), arrows to x(t), u(t), output y(t). | After spatial discretisation, physical transport and chemistry become ẋ=f(x,u(t)); a representative older mesh allocates 1,480 entries. | Briefing §3. 1,480 = older implementation's allocated states, **not** independent validated degrees of freedom. |
| 5 | **Why this becomes a stiff numerical problem** | Lightweight animation/stepwise reveal: advection → radial diffusion → surface chemistry; MoL → implicit BDF. | Upwind is chosen for axial advection, central differences for radial diffusion, BDF for stiff timescales; numerical choices have to be verified. | Briefing §3; avoid claiming a full successful reacting integration. |
| 6 | **What we can actually demonstrate** | Three large evidence tiles: 24/24 source parameter and rate-law checks; 37 local package tests passed; 10/12 numerical coverage-range checks. Small notice: coverage discrepancy at high-acetylene condition. | Stronger provenance and test coverage, **not** reactor validation. | Receipts in 3_Model/probes and briefing. **Use 10/12, NOT the briefing's erroneous 11/12.** |
| 7 | **The missing link is physical, not rhetorical** | Two-column status diagram: older transport scaffold (kinetic tuples zero, 6 reproduced defects); modular pbr (steady/PSSA rates, auxiliary relaxation, 3 reproduced defects). Footer: newer reacting branch unverified. | We cannot yet infer an improvement in periodic ethylene yield. Model structure and dynamic surface feedback still need resolution. | Briefing §4, Wayfinder GitHub checkpoint. No unverified run figures. |
| 8 | **The next decisive experiment** | Research sequence: select/reconcile model → verify kinetic coupling → run steady baseline → run forced inlet → compare cycle-averaged ethylene output; question callout for supervisor. | Ask which model fidelity to commit to (pseudo-homogeneous vs additional resolved pellet physics), then produce falsifiable yield comparison. | Proposed work, clearly labeled as **next**, not completed. |

## Supporting material: only if needed
- **Backup A:** Arrhenius reference conventions and why Berger vs Urmès must not be mixed.
- **Backup B:** Audit ledger: 6 old defects, 3 additional modular-package issues, Jacobian cost.
- **Backup C:** Coverage probe explains why exactly **2** H₂ cells miss the published lower bound (10/12).
- **Notebook demonstration:** transport-only notebook can be used as an explicitly labeled transport illustration; do not show it as a reacting yield experiment.

## Build sequence (strict priority)
1. **Lock evidence wording** from the tracked receipts, with the Wayfinder's 10/12 correction overriding stale supervisor-briefing text.
2. **Make one polished, full-viewport 16:9 HTML deck**, eight slides, slide-to-slide navigation; no scrollable notebook pasted into a slide, no illegible tables, no placeholder UI.
3. **Create original explanatory diagrams** for slides 1, 2, 4, 5 and 8. Use only traceable plots and distinguish any conceptual shapes from simulation data.
4. **Write concise speaker notes** (45–75 s per slide) and a short answer to “what has actually been validated?”
5. **Self-test the deck** at projector size and small laptop size, with keyboard next/back, no external-network dependency; export **PDF fallback** if feasible.
6. **Cross-check all numerical claims** and open the delivered files; the deck is not “ready” simply because the files exist.

## Definition of done for Wednesday
- A **single clearly named final HTML presentation** in `Academics/BEP/Catalysis/presentation/`, plus PDF fallback if available.
- One readable accompanying **speaker-notes Markdown file**.
- Strong narrative; each slide answers one question in ~1 minute.
- Any figure is either sourced, executed with a receipt, or labeled schematic.
- No statement that periodic selectivity gain, reacting simulation, or transient surface model has been validated.
- GitHub commit + direct link; openable offline.

## Don't spend Wednesday's preparation on
A full thesis Wayfinder, a new reactor engine, control/MPC detour, importing Guy's presentation skill, or attempting to rescue an unread paper into a factual slide at the last minute. Reuse existing work; polish and present what is defensible.

## Open but nonblocking owner choices
Exact speaking slot and audience have not been supplied; eight slides and 8–10 minutes are **defaults**, not verified requirements. Format direction is HTML (previously requested), with PDF as insurance.
