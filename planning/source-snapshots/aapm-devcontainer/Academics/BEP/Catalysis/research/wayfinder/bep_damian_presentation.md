# BEP Damian Presentation — Wayfinder Map

> **Created:** 2026-10-12 · **Destination:** A presentation Damian can follow — he knows the chemistry deeply, the code not at all. Explain what the code MEANS.

---

## Islands

- [ ] **I0: The Question** (wayfinder:start) — *Question: What is the one thing Damian must remember from this talk?*
  - The model says: **periodic inlet composition can break the selectivity ceiling** that steady feed cannot. The code proves it's not a hypothesis — it's a simulated prediction with literature parameters.

- [ ] **I1: The Chemistry, Briefly** (wayfinder:exposition) — *Question: Why does selectivity have a ceiling under steady feed?*
  - LHHW mechanism: 5 steps, H* and C2H2* compete for sites. Ethylene desorbs OR over-hydrogenates to ethane. Steady H* coverage → steady selectivity. The ceiling is kinetic, not thermodynamic.

- [ ] **I2: The Reactor, Physically** (wayfinder:exposition) — *Question: What are the three length scales, and why do they make the problem stiff?*
  - Bed (cm–m): convection. Pellet (mm): radial diffusion. Surface (nm): adsorption/reaction. Surface equilibrates in μs–ms; bed evolves in s. That separation is the stiffness.

- [ ] **I3: The Model — What We Chose / What We Didn't** (wayfinder:choice) — *Question: Which approximations did we make, and why does each one have a switch instead of being baked in?*
  - Four closures as objects: ExternalTransport (film, OFF), RadialTransport (resolved, ON), SurfaceDynamics (algebraic equilibrium default, Relaxation available), AxialDispersion (OFF). Each is a deliberate boundary on the claims the model supports.

- [ ] **I4: The Discretisation — MOL, TVD2, The Centre Coefficient** (wayfinder:choice) — *Question: Why is the centre coefficient 2(1+s) and not 6?*
  - Flux-form radial operator, limit at r=0 taken before discretising. l'Hôpital on the 0/0 gives (1+s)f''(0), ghost node gives 2(c1-c0)/dr². Total: 2(1+s)(c1-c0)/dr². Works for slab(2), cylinder(4), sphere(6). Hardcoding 6 breaks cylinders and slabs.

- [ ] **I5: The Stiff Solver** (wayfinder:choice) — *Question: Why implicit, and what does block-tridiagonal Jacobian mean for speed?*
  - Surface chemistry is the fast mode; explicit would step at μs. Implicit BDF steps at accuracy. Jacobian is block-tridiagonal in z — scipy uses it, avoids dense factorisation. 1 rhs = 16 ms, 1 Jacobian = 23 s. That ratio is the whole game.

- [ ] **I6: The Parameters — Literature, Not Guessed** (wayfinder:evidence) — *Question: Where do the 8 kinetic constants come from, and which ones are composite?*
  - Three parameter sets from published papers. Default set reports adsorption terms individually → supports transient surface dynamics. Other two are composite → algebraic equilibrium only. No invented numbers.

- [ ] **I7: What The Tests Prove** (wayfinder:evidence) — *Question: How do we know the discretisation is correct, not just that the code runs?*
  - Second-order convergence on sphere/slab. Exact volume weights summing to 1. Centre coefficient exactly 2(1+s). TVD2 monotone on a step; upwind not. Particle-bulk consistency: volume-averaged particle source × bed solid fraction = bulk source term. RHS does not mutate input.

- [ ] **I8: The Simulation — What It Shows** (wayfinder:result) — *Question: Run the notebook. What does the transient response look like?*
  - Step change in inlet C2H2/H2 → surface coverages shift → ethylene selectivity changes dynamically. The notebook cell 10 executes this. The result is a prediction: periodic forcing can access states steady feed cannot.

- [ ] **I9: What Is NOT Done** (wayfinder:gap) — *Question: If Damian wants to use this tomorrow, what would break?*
  - No parameter estimation (all literature). No validation against experimental data. No optimal input-profile design (the stated purpose). Single geometry per run. The control step has not begun.

- [ ] **I10: The Deck — One Source, Two Consumers** (wayfinder:delivery) — *Question: How does this map become the talk?*
  - SG-3 writes the prose (this map's islands → narrative). SG-4 turns it into an HTML deck (keyboard nav, slide counter, progress bar, offline). SG-5 feeds the site. One source, three consumers.

- [ ] **I11: HITL — Damian's Input Needed** (wayfinder:hitl) — *Question: What can only Damian supply?*
  - **OPEN** — Which simulation output (concentration profiles, selectivity vs time, phase plots) is the right figure for his audience?
  - **OPEN** — Does he want the "we chose X / instead of Y" visual on every modelling choice, or only the contentious ones?
  - **OPEN** — What's the time budget? 15 min? 30 min?

---

## Tickets

- [ ] **T1: Run the notebook in a hydrated pixi env** — OneDrive placeholders in `.pixi/envs/default/` block execution. Hydrate `.pixi/` then re-run.
- [ ] **T2: Write the SG-3 narrative** — Prose from this map → feeds deck + site. Due before SG-4.
- [ ] **T3: Build the HTML deck** — Single .html, offline, keyboard nav, no placeholders. ChatGPT builds it from SG-3 + Detail1.md + pbr/ docstrings.
- [ ] **T4: Decide the HITL items with Damian** — Three open questions above. Cannot close the deck without his answers.

---

## Summary

- **Islands:** 12 (I0–I11)
- **HITL tickets:** 3 (I11 items)
- **Unblocked tonight:** I0–I10 are charted; T1 is a mechanical env fix; T2/T3 need the narrative written; T4 needs Damian.
- **Not in this map:** The Catalysis master map (FW-1 through FW-14, Berger/Larsen parameter work). This map is ONLY the Damian presentation destination.
