# BEP Presentation — open scientific decisions and questions for Zoë

**14 October 2026 · Status: OPEN, no message sent, no meeting/approval assumed.**  
This is a **deck-level research/discussion agenda**, not a preselected slide script or a claim that Zoë has approved the model. The user explicitly wants **full content first to think through aloud**, with the assistant's *tentative presentation picks at the top*, and a short global bullet outline only after scientific selection. Scientific A–M work continues in parallel with a separate deck-producing Work session.

**Evidence to read before discussing:** [master structure](PRESENTATION_STRUCTURE.md) · [F physical balances and state-space](deep-dives/F_conservation_state_space_2026-10-14.md) · [G numerical methods and Jacobians](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md) · [state-space story](sub-stories/01_three_concentrations_to_state_space.md) · [older defect register](../3_Model/state.md) · [Hermes reacting code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py).

## 0. Provisional choice for deck

- **Likely useful:** physical stored state and how bulk/pore/adsorbed fields lead to MOL/state-space; stiffness and the explicit-vs-implicit numerical **integration** question; computational Jacobian structure/sparsity; why we need verifiable accuracy per cyclic outlet observable.
- **Not automatically a slide:** entire F balance derivations, detail of erroneous source terms, every numerical method candidate, or computational performance anecdotes without verifiable context.
- **Do not close editorial choices yet:** user will think aloud about F/G's **full content**; keep the source-backed G note intact, not only a retrospective.

**[USER PROPOSAL — NOT IMPLEMENTED]** Start with **Forward Euler (explicit in time)** and **first-order upwind (space)** to expose stability/stiffness and numerical spatial attenuation. In the *pure-advection* case at **CFL=1**, the update reduces to a one-cell shift with no damping. At CFL<1, or with nonlinear reactions/diffusion, that special cancellation is not guaranteed. Both existing Python scripts still run implicit BDF; do **not** label Forward Euler an implemented solution. **Zoë question:** When does physical stiffness prohibit this simple explicit method, and which numerical errors matter for cyclic outlet amplitude/phase?

## Numerically concrete presentation lead — cyclic-wave fidelity (2026-10-14)

**[DERIVED, not a reacting simulation]** For **pure advection**, first-order spatial upwind with \(N\) cells and a sine forcing at one cycle per gas residence time attenuates the harmonic outlet amplitude to \(\bigl[1+(2\pi/N)^2\bigr]^{-N/2}\) even with exact integration in time. At the new script's **60-cell** default this is only **72.09% amplitude retained**, i.e. **27.91% purely numerical attenuation**. This calculation assumes *linear no-reaction transport, uniform positive flow and steady harmonic response*, not real reactor output. See [full G derivation](deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md#G0a-new-scientificnumerical-lead--quantify-spatial-attenuation-before-blaming-bdf-or-rk-user-discussion-14-oct).

- [ ] **[OPEN / Zoë / deck]** How to demonstrate spatial upwind diffusion vs temporal solver damping, isolate grid error from physics, and measure periodic amplitude and phase?
- [ ] **[OPEN / model choice]** Is explicit RK4/RK45 accurate and affordable on our relevant model/timescales, compared to implicit BDF/Radau, or does chemistry/diffusion stiffness favour implicit methods?
- [ ] **[NOT RUN]** Prefer a controlled *advection-only* test first and matched \`upwind1\` vs \`tvd2\` grid convergence before showing reacting waveform figures.

**Possible spoken question:** “If our numerical scheme removes almost 28% of a periodic *pure-transport* signal at the standard mesh, how do we make sure any reactor amplitude/phase change we attribute to chemistry isn't a discretisation artefact?”

## 1. Communication/action ticket — Zoë (NOT YET SENT)

- [ ] **[USER ACTION / OPEN] Write Zoë Gromotka a short scientific update/questions about F first, also incorporating G's implicit-numerics/solver questions; invite review or a conversation and decide whether/what belongs in the deck.** Draft only when ready; do not imply this has been sent.
- [ ] **[USER DECISION / OPEN]** Does the formulation of physical bulk/pore/site states and the proposed reactor state-space representation correctly address our research question, or have we retained or omitted the wrong physics?
- [ ] **[USER DECISION / OPEN]** Which physical balance/closure ought to be our mathematical reference for bulk-pore exchange, particularly with dynamic pore inventories and a zero-film boundary? Do we need a discrete conservation demonstration at the next supervisor discussion?
- [ ] **[USER DECISION / OPEN]** Clarify what the user meant by “my explicit model” if they meant an **explicit numerical integration scheme**; the two currently inspected production scripts use **implicit SciPy BDF**, while their model equations and state-space form are explicit mathematical expressions.
- [ ] **[USER DECISION / OPEN]** Would **BDF**, **Radau** or a suitable **IMEX** scheme be the principled numerical comparison at the actual stiffness/frequency regime? Which error measure matters: steady conversion, forced outlet amplitude/phase, cycle-averaged yield, or parameter recovery?
- [ ] **[USER DECISION / OPEN]** Should the next solver effort focus on a **correct sparse/block Jacobian** and boundary handling before comparing integrators? The current new code returns dense matrices; its optional radially resolved Jacobian lacks full cross-coupling checks.
- [ ] **[USER DECISION / OPEN]** How to make a scientifically fair/concise mathematical contribution in the presentation without presenting uncalibrated kinetics, F's flux coupling suspicion, or solver code audits as validated reactor results?

## 2. Short potential talking points (pending)

**F:** “We move from measured bulk concentration to a state that can include pore and surface storage, allowing us to formulate a dynamic state-space problem. Which variables are essential and which are just expensive detail?”  
**G:** “Once written as an ODE system, what drives stiffness and solver cost? Our numerical work suggests Jacobian construction is central; we now need to check boundary correctness, sparsity and convergence rather than simply adding compute.”

**Scientific status:** F is a derivation/code inspection, not an executed conserved-reaction test. G is code/audit comparison, not a new benchmark. Existing Hermes receipts cover some uniform-pellet checks but not comprehensive radially resolved dynamics.

## 3. Parallel deck session coordination

The deck-producing session should inspect this file **before locking narrative/slides**, use the full F and G deep dives as material, carry Zoë's questions as **OPEN** and avoid assuming that a meeting or agreement took place. The F/G questions are not blockers for creating a preliminary deck, but can materially affect its final maths and validation wording.

**Linked tracking:** [project state](../state.md) · [Zoë/Damian correspondence thread](../thread_zoe_damien.md) · [global task tracker](../../../../task.md). Keep all statuses honest until a real message is sent and Zoë's response is received.
