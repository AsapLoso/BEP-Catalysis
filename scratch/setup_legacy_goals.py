import subprocess
import os

branches_data = {
    "feat/schbib-co-benchmark": {
        "todo": """# Subgoals & Gate Receipts — Schbib (1996) Steady-State Benchmark

## 01 — Literature & Parameter Extraction
- [ ] Inspect `research/literature/schbib_1996_full_article.html` and extract Table 3 (feed specs), Table 4 (catalyst morphology), and Table 8 (kinetic & adsorption Arrhenius constants).
- [ ] Record extracted constants in notebook preamble with explicit units.

## 02 — Differential PFR Model Formulation
- [ ] Implement molar balance ODEs: $dF_i/dz = A \\rho_s (1 - \\varepsilon_b) \\sum_j \\nu_{i,j} r_j$.
- [ ] Implement non-isothermal energy balance: $dT/dz = \\frac{A \\rho_s (1 - \\varepsilon_b) \\sum_j (-\\Delta H_{r,j}) r_j}{\\sum_i F_i C_{p,i}}$.
- [ ] Implement Schbib Langmuir-Hinshelwood rate laws with cubed denominator: $[1 + K_H C_H^{1/2} + K_{CO} C_{CO}]^3$.

## 03 — Figure Reproduction
- [ ] Replicate Figure 1: Conversion of C2H2 and C2H4 vs. Temperature (290–360 K).
- [ ] Replicate Figure 2: Reaction rates r1 and r2 vs. Temperature.
- [ ] Replicate Figures 3 & 4: Axial temperature and conversion profiles along the bed (thermal runaway suppression).

## 04 — Table 6 Benchmark Validation
- [ ] Simulate reactor at 150 ppm, 1400 ppm, and 5000 ppm CO at 341 K, 359 K, 393 K.
- [ ] Output validation table comparing simulated conversions against measured values from Table 6.

## 05 — Gate Receipt
- [ ] Notebook `notebooks/benchmarks/schbib_1996_steady_state.ipynb` executes top-to-bottom with 0 errors in < 60 seconds.
- [ ] Commit notebook and figures to branch.
""",
        "goal_note": "\n\n**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts."
    },
    "feat/v4-dynamic-reactor": {
        "todo": """# Subgoals & Gate Receipts — V4 Dynamic 1D Coupled Reactor Engine

## 01 — Chemistry & CO Competitive Adsorption Engine
- [ ] Update `notebooks/v3/vendor/pbr/chemistry.py` to add Carbon Monoxide ($CO$) as an active species.
- [ ] Implement Schbib (1996) Langmuir-Hinshelwood kinetics with cubed denominator term $[1 + K_H C_H^{1/2} + K_{CO} C_{CO}]^3$.

## 02 — True Transient ODE Method of Lines (NO PSSA)
- [ ] Verify that the gas accumulation term $\\varepsilon_b \\frac{\\partial C_{b,i}}{\\partial t}$ is strictly active in `pbr/solver.py` (no pseudo-steady-state shortcuts).
- [ ] Discretize space via Method of Lines into a stiff ODE system $\\frac{d\\mathbf{y}}{dt} = \\mathbf{F}(t, \\mathbf{y})$.
- [ ] Verify solver convergence to baseline steady-state using `scipy.integrate.solve_ivp(method='BDF')`.

## 03 — Periodic Inlet Modulation Hook
- [ ] Implement Danckwerts boundary conditions at $z = 0$ with time-dependent inlet forcing:
  $C_{CO,\\text{in}}(t) = C_{CO,\\text{mean}} + \\Delta C_{CO} \\operatorname{sgn}(\\sin(2\\pi t / \\tau_p))$.
- [ ] Test both square-wave and sinusoidal modulation across periods $\\tau_p \\in [0.1, 10]\\ \\text{s}$.

## 04 — Dynamic Wave Propagation & Limit Cycles
- [ ] In `notebooks/v4/unified_v4_dynamic_reactor.ipynb`, plot 2D spatiotemporal heatmaps $C_i(z, t)$ showing concentration waves traveling through the packed bed.
- [ ] Plot limit cycle trajectories in the phase plane: Conversion $X(t)$ vs. Ethylene Selectivity $S(t)$.

## 05 — Gate Receipt (Pareto Enhancement)
- [ ] Calculate cycle-averaged $(\\overline{X}, \\overline{S})$ and generate a Pareto comparison plot demonstrating that dynamic periodic CO operation shifts performance beyond the static steady-state limit.
- [ ] Notebook executes cleanly in < 3 minutes on CPU.
""",
        "goal_note": "\n\n**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts."
    },
    "feat/personal-map-alignment": {
        "todo": """# Subgoals & Gate Receipts — Theory Alignment & Defense Preparation

## 01 — Dimensionless Transport Criteria Scaling
- [ ] Calculate Péclet numbers ($Pe_{m,ax}, Pe_p$), Damköhler numbers ($Da_I, Da_{II}$), Biot numbers ($Bi_m, Bi_h$), and Thiele modulus ($\\Phi$) across the experimental operating window ($L = 0.05\\text{--}0.2\\ \\text{m}$, $d_p = 1\\text{--}3\\ \\text{mm}$, $u = 0.01\\text{--}0.1\\ \\text{m/s}$).
- [ ] Provide mathematical justification for 1D continuum axial dispersion vs. plug flow.

## 02 — Boundary Condition Proofs
- [ ] Derive Danckwerts inlet boundary condition at $z = 0$ from interface flux conservation.
- [ ] Prove why Dirichlet boundary conditions ($C(0, t) = C_{\\text{in}}(t)$) fail mass conservation during steep inlet concentration pulsing.
- [ ] Justify the outflow Neumann condition ($\\partial C / \\partial z = 0$ at $z = L$).

## 03 — Oral Defense Question Bank (25 Questions)
- [ ] Author 25 rigorous oral defense questions with detailed model answers, structured across 5 themes:
  1. Reactor Transport & Non-Idealities (5 Qs)
  2. Surface Kinetics & Competitive CO Adsorption (5 Qs)
  3. Numerical Analysis & Stiff ODE Solvers (5 Qs)
  4. Periodic Forcing Dynamics & Resonance (5 Qs)
  5. Experimental Feasibility & Sampling Lag (5 Qs)
- [ ] Include explicit "Supervisor Trap" and mathematically grounded "Model Answer" for each.

## 04 — Personal Mind Map Alignment Proposals
- [ ] Following `bep-map-edit-review` skill rules, draft proposed alignment updates for the personal mind map in `research/notes/theory_alignment/personal_map_updates.md` without modifying master maps.

## 05 — Gate Receipt
- [ ] Compile comprehensive dossier `research/notes/theory_alignment/mathematical_formulation_and_defense_prep.md` and verify all citations and equations.
""",
        "goal_note": "\n\n**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts."
    },
    "feat/larsen-pdag-benchmark": {
        "todo": """# Subgoals & Gate Receipts — Larsen (2024) PdAg Replication

## 01 — High-Resolution Raster Appendix Extraction
- [ ] Render pages 71–88 of `BEP Example.pdf` to 300 DPI PNG images in `scratch/larsen_appendices/`.
- [ ] Extract full parameter sets from Tables E.1–E.3, specifically recovering $r_{1,\\max}$ and $n_{\\text{inh}}$.
- [ ] Extract tube diameter, bed length, and catalyst mass from Appendix F Python code screenshots.

## 02 — Experimental Curve Digitization
- [ ] Digitize data points from Appendix B (vs. $p_{\\text{C}_2\\text{H}_2}$), Appendix C (vs. $p_{\\text{C}_2\\text{H}_4}$), and Appendix D (vs. $p_{\\text{H}_2}$) across $\\text{Pd}_0\\text{Ag}$, $\\text{Pd}_2\\text{Ag}$, and $\\text{Pd}_3\\text{Ag}$.
- [ ] Save raw coordinates to CSV in `notebooks/benchmarks/data/`.

## 03 — 1D Differential Reactor ODE Simulation
- [ ] Implement Larsen's molar balance ODEs (Eqs. 4.6–4.9) with Extended LHHW rate laws (Eqs. 6.9–6.11).
- [ ] Solve ODEs across experimental partial pressures.

## 04 — RMSE Validation & Figure Overlay
- [ ] In `notebooks/benchmarks/larsen_2024_benchmark.ipynb`, plot simulated vs. measured conversion and selectivity curves.
- [ ] Calculate RMSE in percentage points and confirm agreement with Larsen's published values (Pd0Ag: ~5.10%, Pd2Ag: ~5.43%, Pd3Ag: ~7.14%).

## 05 — Gate Receipt
- [ ] Notebook executes cleanly with 0 errors in < 60 seconds. Commit notebook and digitized data.
""",
        "goal_note": "\n\n**Governance:** `GOAL.md` defines the scientific completion contract; `TODO.md` governs the subgoals and gate receipts."
    }
}

for branch, data in branches_data.items():
    print(f"Updating branch {branch}...")
    subprocess.run(["git", "checkout", branch], check=True)
    with open("TODO.md", "w", encoding="utf-8") as f:
        f.write(data["todo"])
    
    if os.path.exists("GOAL.md"):
        with open("GOAL.md", "r", encoding="utf-8") as f:
            goal_content = f.read()
        if "TODO.md" not in goal_content:
            with open("GOAL.md", "a", encoding="utf-8") as f:
                f.write(data["goal_note"])
    
    subprocess.run(["git", "add", "TODO.md", "GOAL.md"], check=True)
    subprocess.run(["git", "commit", "-m", f"docs(governance): add legacy structured TODO.md subgoals and gate receipts to {branch}"], check=True)
    subprocess.run(["git", "push", "origin", branch], check=True)

subprocess.run(["git", "checkout", "unified-reactor-model"], check=True)
print("All branches successfully updated and pushed!")

