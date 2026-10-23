"""Legacy AI candidate synthesis for the BEP ownership mind map.

The in-memory candidates are not verified findings or an authorized replacement
for the curated draft overlay. Saving is fail-closed: the current overlay is
preserved unless generated IDs and every serialized record already match it.
"""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from pathlib import Path
from typing import List

try:
    from Academics.BEP.Catalysis.mindmap.editor import load_map
    from Academics.BEP.Catalysis.mindmap.schema import MindMap, MindMapNode, SourceItem
except (ImportError, ModuleNotFoundError):
    from editor import load_map
    from schema import MindMap, MindMapNode, SourceItem

DATA_DIR = Path(__file__).resolve().parent / "data"
CANONICAL_PATH = DATA_DIR / "bep_map.yaml"
DRAFT_PATH = DATA_DIR / "bep_draft_overlay.yaml"


def generate_synthesized_nodes() -> List[MindMapNode]:
    """Return legacy AI-draft candidates; this does not validate their claims."""
    nodes: List[MindMapNode] = [
        # =====================================================================
        # 1. PHYSICS BRANCH (parent: physics)
        # =====================================================================
        MindMapNode(
            id="lhhw_kinetics",
            parent="physics",
            title="Extended LHHW Reaction Kinetics",
            tier=1,
            importance=3,
            rationale="Captures competitive adsorption between C2H2, C2H4, and H2 on active catalyst sites with non-ideal inhibition.",
            notes="Extended Langmuir-Hinshelwood-Hougen-Watson formulation. Rate r1 (acetylene to ethylene) features squared denominator; rate r2 features non-integer fitted exponent n_inh.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Equations 6.9–6.11 (Final Extended LHHW Rate Law)",
                ),
                SourceItem(
                    title="BEP Catalysis Project Conventions §12.1",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§12.1 Verified against primary text",
                ),
            ],
            open_questions=[
                "Confirm whether hydrogen adsorption is non-dissociative or dissociative on Ag-promoted Pd surface.",
                "Resolve unmeasured cross-sectional area A and support density rho_support from Appendix F before quantitative conversion calibration.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="centered_arrhenius",
            parent="lhhw_kinetics",
            title="Centered Arrhenius Temperature Dependence",
            tier=1,
            importance=2,
            rationale="Reparameterizes rate coefficients around reference temperature T0 to reduce binary parameter correlation below 0.71.",
            notes="k(T) = k_0 * exp(-E_a / R * (1/T - 1/T_0)). Eliminates strong correlation between pre-exponential factor and activation energy during parameter estimation.",
            sources=[
                SourceItem(
                    title="Berger et al. (2008) Chemical Engineering Science 63",
                    doi="10.1016/j.ces.2008.08.012",
                    path="Academics/BEP/Catalysis/Articles/analyses/dynamic_kinetics_berger2008.md",
                    section="Equation 17 - Centered Arrhenius formulation",
                ),
                SourceItem(
                    title="Model Architecture Decisions §11.5",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§11 Item 5: Centered Arrhenius for kp(T)",
                ),
            ],
            open_questions=[
                "Select optimal reference temperature T0 (candidate: 313 K / 40 °C matching Larsen benchmark).",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="surface_coverage_dynamics",
            parent="lhhw_kinetics",
            title="Dynamic Surface Coverage State θ(z,r)",
            tier=1,
            importance=3,
            rationale="Tracks time-dependent fraction of vacant and occupied catalyst active sites under transient/forcing conditions.",
            notes="Conservation: theta_vacant + theta_C2H2 + theta_C2H4 + theta_H = 1. Coupled directly into instantaneous reaction rates rather than pseudo-steady-state assumption.",
            sources=[
                SourceItem(
                    title="Transient Model Framework Audit §2",
                    path="Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md",
                    section="§2 State Vector [Cb, cp, theta] Architecture",
                ),
                SourceItem(
                    title="Berger et al. (2008) Chemical Engineering Science 63",
                    doi="10.1016/j.ces.2008.08.012",
                    path="Academics/BEP/Catalysis/Articles/analyses/dynamic_kinetics_berger2008.md",
                    section="Section 2.1 Dynamic Surface Balances",
                ),
            ],
            open_questions=[
                "Assess computational stiffness introduced by microkinetic site balances relative to gas-phase residence time.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="reaction_thermodynamics",
            parent="physics",
            title="Exothermic Reaction Heats & Equilibrium Limits",
            tier=1,
            importance=2,
            rationale="Quantifies thermal release for semi-hydrogenation (-172 kJ/mol) and full hydrogenation (-137 kJ/mol) governing reactor temperature rise.",
            notes="Exothermicity can trigger local thermal runaway and loss of ethylene selectivity. Shifting equilibrium constant K_p requires van 't Hoff temperature correction.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Reaction Enthalpies & Equilibrium Constants",
                ),
                SourceItem(
                    title="Reaction Engineering Reference Conventions §12",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§12 Standard heats of reaction",
                ),
            ],
            open_questions=[
                "Confirm heat capacity Cp temperature-dependence in carrier gas stream (ethylene/argon mixture).",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="transport_phenomena_checks",
            parent="physics",
            title="Interphase & Intraparticle Transport Screening",
            tier=1,
            importance=2,
            rationale="Evaluates Mears and Weisz-Prater criteria to confirm kinetic-regime operation without mass/heat transfer limitations.",
            notes="Mears number < 0.15 rules out external film diffusion; Weisz-Prater modulus Phi < 0.3 rules out internal pore diffusion resistance.",
            sources=[
                SourceItem(
                    title="Deep Dive E: Operating Regime & Transport",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/E_operating_regime_transport_2026-10-14.md",
                    section="Transport criteria and regime checks",
                ),
                SourceItem(
                    title="Chemical Reaction Engineering (Froment & Bischoff)",
                    doi="10.1002/cjce.5450580320",
                    section="Chapter 3: Catalyst transport resistances",
                ),
            ],
            open_questions=[
                "Obtain catalyst pellet pore volume and tortuosity to estimate effective Knudsen/molecular diffusivity Deff in mesoporous alpha/gamma-Al2O3 support.",
            ],
            is_draft=True,
        ),

        # =====================================================================
        # 2. MATHEMATICS BRANCH (parent: mathematics)
        # =====================================================================
        MindMapNode(
            id="pde_reactor_balances",
            parent="mathematics",
            title="1D Axial Dispersion Reaction PDEs",
            tier=1,
            importance=3,
            rationale="Governing partial differential equations for species mass and thermal energy conservation along reactor length z.",
            notes="eps_b * dC_i/dt + u_s * dC_i/dz = D_ax * d2C_i/dz2 + rho_b * R_i. Danckwerts boundary conditions at inlet (z=0) and outlet (z=L).",
            sources=[
                SourceItem(
                    title="Model Architecture Decisions §11.1",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§11 Item 1: 1D Axial Dispersion Framework",
                ),
                SourceItem(
                    title="Deep Dive F: Conservation State Space",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/F_conservation_state_space_2026-10-14.md",
                    section="Continuity and energy balances",
                ),
            ],
            open_questions=[
                "Evaluate whether radial temperature gradients require a 2D axisymmetric extension under steep periodic forcing.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="ocfe_collocation",
            parent="pde_reactor_balances",
            title="Orthogonal Collocation on Finite Elements (OCFE)",
            tier=1,
            importance=2,
            rationale="Discretizes spatial derivatives into DAEs with high-order polynomial accuracy across internal boundary layers.",
            notes="Partitions axial domain into N_elem finite elements with N_coll Radau/Gauss-Legendre interior collocation points per element.",
            sources=[
                SourceItem(
                    title="Deep Dive G: Numerical Methods & Feasibility",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md",
                    section="Spatial discretization benchmarks",
                ),
                SourceItem(
                    title="Villadsen & Michelsen (1978) Solution of Differential Equation Models",
                    doi="10.1016/0009-2509(78)85098-4",
                    section="Chapter 5: Orthogonal Collocation",
                ),
            ],
            open_questions=[
                "Compare sparsity pattern of OCFE against 2nd-order flux-conservative finite volume scheme.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="transient_solver_bdf",
            parent="mathematics",
            title="Implicit BDF / Radau Stiff ODE Integrator",
            tier=1,
            importance=3,
            rationale="Integrates stiff multi-scale temporal dynamics (fast surface kinetics tau ~ 1e-4 s vs slow thermal wave tau ~ 10 s).",
            notes="Utilizes variable-order, variable-step implicit multistep BDF (e.g. CVODE / scipy.integrate.solve_ivp BDF/Radau) with analytical Jacobian evaluation.",
            sources=[
                SourceItem(
                    title="Deep Dive G: Numerical Methods & Feasibility",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md",
                    section="Stiffness ratios and solver convergence",
                ),
                SourceItem(
                    title="Hairer & Wanner (1996) Solving Ordinary Differential Equations II: Stiff Problems",
                    doi="10.1007/978-3-642-05221-7",
                    section="Radau5 & BDF methods",
                ),
            ],
            open_questions=[
                "Confirm condition number of Newton-Raphson iteration matrix across the full periodic operating envelope.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="analytical_jacobian",
            parent="transient_solver_bdf",
            title="Banded Analytical Jacobian Formulation",
            tier=1,
            importance=2,
            rationale="Provides exact partial derivatives dF/dx to accelerate implicit nonlinear solver convergence by 5–10x over finite differences.",
            notes="Block-tridiagonal structure resulting from local 1D spatial coupling. Exploited via banded LU decomposition.",
            sources=[
                SourceItem(
                    title="Deep Dive G: Numerical Methods",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md",
                    section="Jacobian construction and banded linear algebra",
                ),
            ],
            open_questions=[
                "Automate symbolic differentiation for LHHW rate laws to eliminate manual derivative maintenance errors.",
            ],
            is_draft=True,
        ),

        # =====================================================================
        # 3. SYSTEMS & CONTROL BRANCH (parent: systems_control)
        # =====================================================================
        # Sub-Team 1: Process Instrumentation & Actuation
        MindMapNode(
            id="sc_actuators_sensors",
            parent="systems_control",
            title="Sub-Team 1: Process Instrumentation & Actuation",
            tier=1,
            importance=2,
            rationale="Coordinates physical actuation hardware, instrument response dynamics, and real-time process sensor networks.",
            notes="Interfaces control algorithms with physical plant physics; models hardware dynamics as dynamic constraints.",
            sources=[
                SourceItem(
                    title="BEP Catalysis Project Conventions §11 & §13",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§11 Control and Reactor Architecture",
                ),
            ],
            open_questions=[
                "Characterize dead-time between MFC command signal and gas arrival at the packed bed entrance.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_actuators",
            parent="sc_actuators_sensors",
            title="Flow & Thermal Actuators",
            tier=1,
            importance=2,
            rationale="Actuation layer controlling feed mass flows, total pressure, and wall heating jacket power.",
            notes="Includes mass flow controllers (MFCs), pneumatic backpressure control valves, and electrical resistance heaters.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Experimental Setup & Actuators",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_mfc_dynamics",
            parent="sc_actuators",
            title="Mass Flow Controller Dynamics & Response Lag",
            tier=1,
            importance=2,
            rationale="First-order lag plus delay (FOPDT) describing Brooks/Bronkhorst thermal MFC settling response (tau = 1.2s).",
            notes="G_mfc(s) = exp(-theta*s) / (tau*s + 1). Bandwidth limits high-frequency periodic feed composition modulation.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="Actuator frequency cutoff limits",
                ),
            ],
            open_questions=[
                "Verify whether Brooks MFC can reproduce 1.0 Hz sinusoidal switching without valve seat wear.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_jacket_heaters",
            parent="sc_actuators",
            title="Multi-Zone Electric Heating Jacket Dynamics",
            tier=1,
            importance=1,
            rationale="Dynamic model of outer wall electrical heating zones providing axial thermal boundary shaping.",
            notes="Thermal capacitance of stainless steel tube wall (tau_th ~ 45 s) creates slow dominant pole in temperature feedback.",
            sources=[
                SourceItem(
                    title="Transient Reactor Model Architecture",
                    path="Academics/BEP/Catalysis/3_Model/transient_model_framework_audit.md",
                    section="Wall thermal dynamics",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_sensors",
            parent="sc_actuators_sensors",
            title="Process Analytics & Sensing",
            tier=1,
            importance=2,
            rationale="Online analytical instrumentation measuring gas compositions, pressure drops, and internal bed temperatures.",
            notes="Combines fast online mass spectrometry with calibrated micro-gas chromatography and internal multipoint thermocouples.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Analytical Equipment",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_gc_sampling",
            parent="sc_sensors",
            title="Online Micro-GC Sampling & Transport Dead-Time",
            tier=1,
            importance=2,
            rationale="Provides quantitative mole fractions of C2H2, C2H4, C2H6 with a 90-second discrete sampling interval.",
            notes="Discrete multirate measurement model with significant time delay requires state estimation buffer reconciliation.",
            sources=[
                SourceItem(
                    title="Process Dynamics and Control (Seborg et al.)",
                    doi="10.1002/9781119282716",
                    section="Multirate and delayed analytical measurements",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_ms_spectrometry",
            parent="sc_sensors",
            title="Mass Spectrometer Fast Transient Response (<200ms)",
            tier=1,
            importance=3,
            rationale="Continuous qualitative monitoring of m/z 26 (C2H2) and m/z 30 (C2H6) to observe dynamic phase lag in real time.",
            notes="Permits direct observation of periodic breakthrough and dynamic resonance peaks during continuous feed modulation.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="Continuous spectrometry monitoring",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_temp_thermocouples",
            parent="sc_sensors",
            title="Bed Axial Thermocouple Array Profiling",
            tier=1,
            importance=2,
            rationale="Multi-point K-type thermocouple bundle measuring internal centerline temperature profile T(z, t).",
            notes="Detects hotspot formation, axial flame propagation, and thermal runaway precursor conditions.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Thermocouple axial placement",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Sub-Team 2: State Observers & Estimation
        MindMapNode(
            id="sc_state_estimation",
            parent="systems_control",
            title="Sub-Team 2: State Observers & Estimation",
            tier=1,
            importance=3,
            rationale="Reconstructs unmeasured internal concentration profiles and surface coverage states θ(z,t) from plant sensors.",
            notes="Combines Kalman filtering and moving horizon estimation to overcome sensor delay and spatial sparsity.",
            sources=[
                SourceItem(
                    title="Deep Dive F: Conservation State Space",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/F_conservation_state_space_2026-10-14.md",
                    section="State observer formulations",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_gas_phase_observers",
            parent="sc_state_estimation",
            title="Bulk Gas Phase Estimation",
            tier=1,
            importance=2,
            rationale="Reconstructs continuous axial concentration C_i(z,t) and temperature T(z,t) profiles from boundary measurements.",
            notes="Evaluates observer gain matrices along collocation nodes using linear-quadratic approximations.",
            sources=[
                SourceItem(
                    title="Process Systems Engineering Literature",
                    doi="10.1016/j.compchemeng.2018.06.014",
                    section="State estimation in distributed parameter systems",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_ekf_gas",
            parent="sc_gas_phase_observers",
            title="Extended Kalman Filter for Axial Concentration & Temp",
            tier=1,
            importance=3,
            rationale="Linearizes distributed reactor DAE model at each time step to propagate error covariance and fuse sparse thermocouple readings.",
            notes="Handles process disturbance covariance Q and measurement noise R; corrects internal thermal gradient estimates.",
            sources=[
                SourceItem(
                    title="Optimal State Estimation (Simon)",
                    doi="10.1002/0470045345",
                    section="Chapter 13: The Extended Kalman Filter",
                ),
            ],
            open_questions=[
                "Confirm convergence of discrete-time EKF under non-uniform GC measurement arrival times.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_observability_analysis",
            parent="sc_gas_phase_observers",
            title="Observability Rank & Gramian Conditioning",
            tier=1,
            importance=2,
            rationale="Evaluates observability rank condition of the discretized state-space system to select optimal sensor locations.",
            notes="Condition number of empirical observability Gramian reveals unobservable internal spatial modes.",
            sources=[
                SourceItem(
                    title="Deep Dive F: Conservation State Space",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/F_conservation_state_space_2026-10-14.md",
                    section="Observability criteria",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_surface_observers",
            parent="sc_state_estimation",
            title="Unmeasured Surface Coverage Estimation",
            tier=1,
            importance=3,
            rationale="Estimates unmeasurable catalyst surface intermediates (θ_C2H2, θ_C2H4, θ_H) crucial for optimal switching.",
            notes="Solves constrained optimization over a backward moving horizon to honor 0 <= theta <= 1 invariants.",
            sources=[
                SourceItem(
                    title="Berger et al. (2008) Chemical Engineering Science 63",
                    doi="10.1016/j.ces.2008.08.012",
                    path="Academics/BEP/Catalysis/Articles/analyses/dynamic_kinetics_berger2008.md",
                    section="Surface coverage dynamics",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_mhe_surface",
            parent="sc_surface_observers",
            title="Moving Horizon Estimation (MHE) for θ Intermediates",
            tier=1,
            importance=3,
            rationale="Nonlinear MHE solves finite-horizon QP to reconstruct dynamic site fractions while strictly enforcing conservation bounds.",
            notes="Formulation: min sum(||v_k||_R^2 + ||w_k||_Q^2) subject to theta_i >= 0 and sum(theta_i) = 1.",
            sources=[
                SourceItem(
                    title="Rawlings et al. (2017) Model Predictive Control",
                    doi="10.1016/B978-0-08-101110-2.00004-9",
                    section="Chapter 4: Moving Horizon Estimation",
                ),
            ],
            open_questions=[
                "Evaluate computational execution time of MHE within real-time 1.0s sampling windows.",
            ],
            is_draft=True,
        ),

        # Sub-Team 3: Dynamic Forcing & Periodic Operation
        MindMapNode(
            id="sc_dynamic_forcing",
            parent="systems_control",
            title="Sub-Team 3: Dynamic Forcing & Periodic Operation",
            tier=1,
            importance=3,
            rationale="Exploits nonlinear adsorption-reaction dynamics via forced periodic inlet oscillations to exceed steady-state selectivity.",
            notes="Modulates inlet partial pressures (H2, C2H2) and temperature to decouple competitive adsorption rates.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation Research Outlook",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="Nonlinear dynamic resonance and forced periodic operation",
                ),
                SourceItem(
                    title="Silveston & Hudgins (2013) Periodic Operation of Chemical Reactors",
                    doi="10.1016/B978-0-444-59530-0.00001-8",
                    section="Chapter 2: Selectivity enhancement in catalytic hydrogenation",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_forcing_synthesis",
            parent="sc_dynamic_forcing",
            title="Periodic Input Modulation Synthesis",
            tier=1,
            importance=2,
            rationale="Designs waveforms (sinusoidal, square-wave, multisine) and parameterizes period tau_p, duty cycle, and phase split.",
            notes="u(t) = u_base + A * sin(2*pi*f*t + phi). Explores frequencies f in range 0.01–1.0 Hz.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="Waveform design space",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_multisine_forcing",
            parent="sc_forcing_synthesis",
            title="Multisine Frequency Sweep for Reactor System ID",
            tier=1,
            importance=2,
            rationale="Synthesizes crest-factor-optimized multisine inputs to identify empirical transfer functions across broad frequency bands.",
            notes="Enables rapid detection of resonant peak frequencies where dynamic yield amplification occurs.",
            sources=[
                SourceItem(
                    title="System Identification: A Frequency Domain Approach (Pintelon & Schoukens)",
                    doi="10.1002/9781118280386",
                    section="Chapter 4: Periodic excitation design",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_resonance_analysis",
            parent="sc_dynamic_forcing",
            title="Dynamic Resonance & Selectivity Improvements",
            tier=1,
            importance=3,
            rationale="Analyzes dynamic phase lag between C2H2 desorbing and H2 reacting to starve the over-hydrogenation pathway to ethane.",
            notes="Strongly nonlinear dependence on frequency: maximum ethylene selectivity gain occurs when period matches surface residence time.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="Phase lag and resonance selectivity",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_pi_criterion",
            parent="sc_resonance_analysis",
            title="Pi-Criterion Analytical Test for Periodic Performance",
            tier=1,
            importance=3,
            rationale="Evaluates second-order Volterra kernel (pi-criterion) to prove whether periodic operation yields strictly higher selectivity than optimal steady-state.",
            notes="Sign of Pi(omega) determines whether periodic forcing at frequency omega is superior (Pi > 0) or inferior (Pi < 0) to steady state.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="The Pi-Criterion analytical framework",
                ),
                SourceItem(
                    title="Sterman & Ydstie (1990) Chemical Engineering Science 45",
                    doi="10.1016/0009-2509(90)87010-Q",
                    section="The Pi-criterion for periodic processes",
                ),
            ],
            open_questions=[
                "Derive analytical second-order Taylor expansion of Larsen LHHW rate law around nominal steady-state operating point.",
            ],
            is_draft=True,
        ),

        # Sub-Team 4: Advanced Process Control & NMPC
        MindMapNode(
            id="sc_optimal_control",
            parent="systems_control",
            title="Sub-Team 4: Advanced Process Control & NMPC",
            tier=1,
            importance=3,
            rationale="Formulates real-time optimization and feedback control to maximize ethylene productivity while guaranteeing strict safety margins.",
            notes="Solves dynamic optimization problems online under actuator constraints and state safety bounds.",
            sources=[
                SourceItem(
                    title="BEP Catalysis Project Conventions §11 & §13",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§11 Control Architecture",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_nmpc_core",
            parent="sc_optimal_control",
            title="Nonlinear Model Predictive Control (NMPC)",
            tier=1,
            importance=3,
            rationale="Receding horizon controller updating optimal input trajectories u(t) every sampling interval based on estimated state x_hat.",
            notes="Integrates orthogonal collocation model into NLP solver (CasADi / IPOPT) for sub-second solve times.",
            sources=[
                SourceItem(
                    title="Rawlings et al. (2017) Model Predictive Control",
                    doi="10.1016/B978-0-08-101110-2.00002-5",
                    section="Chapter 2: Nonlinear Model Predictive Control",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_realtime_nmpc",
            parent="sc_nmpc_core",
            title="Real-Time Economic NMPC on Reduced Collocation Model",
            tier=1,
            importance=3,
            rationale="Directly maximizes cycle-averaged ethylene production rate rather than tracking an arbitrary steady-state setpoint.",
            notes="Objective: max 1/T_p * integral_0^T_p [ F_C2H4_out(t) - c_H2*F_H2_in(t) ] dt subject to DAE reactor model constraints.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="Economic MPC objective formulation",
                ),
            ],
            open_questions=[
                "Confirm real-time feasibility with interior point solver IPOPT within 500 ms control cycle.",
            ],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_active_constraints",
            parent="sc_nmpc_core",
            title="Active Safety Constraints (Acetylene Slip < 5 ppm)",
            tier=1,
            importance=2,
            rationale="Hard output constraints ensuring effluent acetylene meets polymer-grade specification (< 5 ppm) under all load disturbances.",
            notes="C_C2H2(L, t) <= 5.0e-6 * C_total. Enforced via barrier functions and slack variable penalties.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Specification Limits",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_runaway_prevention",
            parent="sc_optimal_control",
            title="Thermal Runaway Protection & Fault Tolerance",
            tier=1,
            importance=3,
            rationale="Prevents parametric sensitivity divergence and catastrophic hotspot runaway during high conversion operation.",
            notes="Monitors maximum axial temperature gradient dT/dz and hotspot magnitude T_max; initiates automated nitrogen quench.",
            sources=[
                SourceItem(
                    title="Froment & Bischoff Chemical Reactor Analysis",
                    doi="10.1002/cjce.5450580320",
                    section="Parametric sensitivity and runaway criteria in packed beds",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="sc_cbf_safety",
            parent="sc_runaway_prevention",
            title="Control Barrier Functions for Hotspot Suppression",
            tier=1,
            importance=2,
            rationale="Constructs forward-invariant safety sets h(x) >= 0 where h(x) = T_safe - max_z T(z) to formally guarantee hotspot bounds.",
            notes="Integrates CBF constraint L_f h(x) + L_g h(x) u + alpha(h(x)) >= 0 into real-time quadratic programming filter.",
            sources=[
                SourceItem(
                    title="Ames et al. (2019) Control Barrier Functions: Theory and Applications",
                    doi="10.1109/ECC.2019.8795639",
                    section="Safety-critical control via barrier certificates",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # =====================================================================
        # 4. DEEP DIVE LETTERS (A–M) (parent: deep_dives_letters)
        # =====================================================================
        # Letter A
        MindMapNode(
            id="letter_a_objective",
            parent="deep_dives_letters",
            title="Letter A: Scientific Objective & Success Criteria",
            tier=1,
            importance=3,
            rationale="Defines the overarching thesis objective: establishing physical validity, identifiability, and periodic control benefit.",
            notes="Grounds thesis scope in dual CaSE / DIAM research goals; establishes criteria for successful modeling defense.",
            sources=[
                SourceItem(
                    title="A–M Research Justification Index §A",
                    path="Academics/BEP/Catalysis/presentation/RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md",
                    section="Section A: Scientific Objective & Success Criteria",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="a1_dual_bep_scope",
            parent="letter_a_objective",
            title="Dual BEP Scope: CaSE Catalysis & DIAM Control",
            tier=1,
            importance=2,
            rationale="Reconciles experimental catalysis fidelity (Urakawa/CaSE) with rigorous dynamical systems and PDE control (Gromotka/DIAM).",
            notes="Ensures neither scientific side is compromised: physical kinetics remain realistic while control formulation is mathematically sound.",
            sources=[
                SourceItem(
                    title="BEP Conventions §13",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§13 Dual BEP Supervision & Scope",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="a2_validation_targets",
            parent="letter_a_objective",
            title="Target Performance: Selectivity vs Space Velocity",
            tier=1,
            importance=2,
            rationale="Defines quantifiable success metrics: >= 85% ethylene selectivity at > 98% acetylene conversion under high GHSV.",
            notes="Establishes benchmark trade-off curves against standard commercial catalyst operating envelopes.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Conversion and selectivity benchmarks",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter B
        MindMapNode(
            id="letter_b_literature",
            parent="deep_dives_letters",
            title="Letter B: Literature & Source Provenance",
            tier=1,
            importance=3,
            rationale="Establishes explicit lineage and provenance of all experimental datasets, kinetic laws, and parameter values.",
            notes="Distinguishes between primary thesis benchmark (Larsen 2024), microkinetic literature (Urmès 2022), and transient methodology (Berger 2008).",
            sources=[
                SourceItem(
                    title="Deep Dive B: Literature Priority Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/B_literature_priority_2026-10-14.md",
                    section="Source provenance and primary priorities",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="b1_larsen_thesis",
            parent="letter_b_literature",
            title="Larsen MSc Thesis (2024) Primary Extraction",
            tier=1,
            importance=3,
            rationale="Primary benchmark dataset providing experimental fixed-bed reactor conversions and extended LHHW parameter fits.",
            notes="Supervised in same CaSE lab; provides direct baseline measurements on Ag-promoted Pd/Al2O3 eggshell catalyst.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Chapter 6: Results and Discussion",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="b1_1_table_kinetics",
            parent="b1_larsen_thesis",
            title="Table 6.1 Parameter Extraction & Confidence Limits",
            tier=1,
            importance=2,
            rationale="Extracts pre-exponential factors k_10, k_20, activation energies E_a1, E_a2, and adsorption equilibrium constants.",
            notes="Identifies asymmetric confidence intervals and verifies non-integer inhibition exponent n_inh = 0.54.",
            sources=[
                SourceItem(
                    title="Larsen MSc Thesis (2024)",
                    path="Academics/BEP/Catalysis/Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt",
                    section="Table 6.1 Kinetic parameters",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="b1_2_geometry_audit",
            parent="b1_larsen_thesis",
            title="Appendix F Reactor Dimensions & rho_support",
            tier=1,
            importance=2,
            rationale="Audits internal tube diameter (d_t = 4.0 mm), bed length (L = 120 mm), catalyst mass (m_cat = 0.25 g), and support density.",
            notes="Clarifies discrepancies in legacy codebase regarding catalyst dilution ratio and void fraction eps_b.",
            sources=[
                SourceItem(
                    title="Deep Dive B: Literature Priority Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/B_literature_priority_2026-10-14.md",
                    section="Appendix F geometry verification",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="b2_urmes_microkinetics",
            parent="letter_b_literature",
            title="Urmès et al. (2022) Surface Intermediates",
            tier=1,
            importance=2,
            rationale="Examines elementary step microkinetics and surface intermediate mechanisms on bimetallic Pd-Ag surfaces.",
            notes="Contrasts macroscopic LHHW with detailed elementary step rate equations.",
            sources=[
                SourceItem(
                    title="Urmès et al. (2022) ChemCatChem 14",
                    doi="10.1002/cctc.202101826",
                    path="Academics/BEP/Catalysis/Articles/analyses/urmes2022_microkinetics.md",
                    section="Section 3: Elementary microkinetics",
                ),
            ],
            open_questions=[
                "Obtain publisher SI to resolve full activation energy table and surface intermediate adsorption enthalpies.",
            ],
            is_draft=True,
        ),

        # Letter C
        MindMapNode(
            id="letter_c_mechanism",
            parent="deep_dives_letters",
            title="Letter C: Reaction Mechanism & Active Site Physics",
            tier=1,
            importance=3,
            rationale="Deep dive into surface reaction pathways: competitive adsorption, spectator species, and oligomer formation.",
            notes="Analyzes physical mechanisms governing selectivity differences between Pd mono-metal and Pd-Ag bimetallic alloys.",
            sources=[
                SourceItem(
                    title="Deep Dive C: Reaction Mechanism Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/C_reaction_mechanism_2026-10-14.md",
                    section="Catalyst site physics and elementary steps",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="c1_adsorption_competition",
            parent="letter_c_mechanism",
            title="Competitive Adsorption on Catalyst Active Sites",
            tier=1,
            importance=3,
            rationale="Models strong preference of acetylene over ethylene for Pd active sites; prevents over-hydrogenation at high C2H2 coverage.",
            notes="Adsorption equilibrium constant ratio K_C2H2 / K_C2H4 > 100 explains why ethylene desorption dominates over hydrogenation.",
            sources=[
                SourceItem(
                    title="Deep Dive C: Reaction Mechanism Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/C_reaction_mechanism_2026-10-14.md",
                    section="Competitive adsorption thermodynamics",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="c1_1_h2_dissociation",
            parent="c1_adsorption_competition",
            title="Dissociative vs Non-Dissociative H2 Chemisorption",
            tier=1,
            importance=2,
            rationale="Evaluates whether H2 adsorbs molecularly or dissociates into 2 H* surface adatoms on Ag-modified sites.",
            notes="Dissociative chemisorption yields square-root pressure dependence (P_H2^0.5) in elementary rate formulations.",
            sources=[
                SourceItem(
                    title="Deep Dive C: Reaction Mechanism Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/C_reaction_mechanism_2026-10-14.md",
                    section="Hydrogen adsorption mechanisms",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="c2_hydrogenation_pathways",
            parent="letter_c_mechanism",
            title="Consecutive Hydrogenation (C2H2 -> C2H4 -> C2H6)",
            tier=1,
            importance=3,
            rationale="Maps the target semi-hydrogenation reaction versus unselective over-hydrogenation to ethane.",
            notes="Rate equations: r1 for C2H2 + H2 -> C2H4; r2 for C2H4 + H2 -> C2H6. Selectivity S = r1 / (r1 + r2).",
            sources=[
                SourceItem(
                    title="Deep Dive C: Reaction Mechanism Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/C_reaction_mechanism_2026-10-14.md",
                    section="Pathway network",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="c2_1_green_oil_oligomers",
            parent="c2_hydrogenation_pathways",
            title="Oligomerization & Green Oil Deactivation",
            tier=1,
            importance=2,
            rationale="Models formation of C4+ heavy oligomers (butadiene, green oil) that block active sites and cause gradual catalyst deactivation.",
            notes="Deactivation rate d(alpha)/dt = -k_d * C_C2H2^m * alpha. Can be mitigated by periodic H2 regeneration pulses.",
            sources=[
                SourceItem(
                    title="Deep Dive C: Reaction Mechanism Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/C_reaction_mechanism_2026-10-14.md",
                    section="Deactivation and oligomerization",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter D
        MindMapNode(
            id="letter_d_kinetics",
            parent="deep_dives_letters",
            title="Letter D: Kinetic Laws & Parameter Identifiability",
            tier=1,
            importance=3,
            rationale="Investigates mathematical structure of rate equations, parameter correlation, and numerical estimability.",
            notes="Analyzes Fisher Information Matrix (FIM) and parameter sensitivity to design optimal dynamic identification experiments.",
            sources=[
                SourceItem(
                    title="Deep Dive D: Kinetic Parameters & Identifiability",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md",
                    section="Identifiability analysis",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="d1_lhhw_rate_laws",
            parent="letter_d_kinetics",
            title="Extended LHHW Rate Law Formulations",
            tier=1,
            importance=2,
            rationale="Evaluates denominator inhibition forms: (1 + K_A*P_A + K_E*P_E)^n where n=1 or n=2.",
            notes="Larsen fitted model uses n=2 for r1 and empirical exponent n_inh = 0.54 for r2.",
            sources=[
                SourceItem(
                    title="Deep Dive D: Kinetic Parameters",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md",
                    section="Rate law comparisons",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="d2_identifiability",
            parent="letter_d_kinetics",
            title="Kinetic Parameter Identifiability & Correlation",
            tier=1,
            importance=3,
            rationale="Calculates correlation matrix of estimated parameters; reveals strong coupling between k_0 and E_a under steady state.",
            notes="Proves that dynamic periodic operation excites uncoupled state directions, reducing confidence ellipsoid volume by >80%.",
            sources=[
                SourceItem(
                    title="Deep Dive D: Kinetic Parameters",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/D_kinetic_parameters_identifiability_2026-10-14.md",
                    section="Correlation matrix and dynamic excitation",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter E
        MindMapNode(
            id="letter_e_transport",
            parent="deep_dives_letters",
            title="Letter E: Operating Regime & Transport Phenomena",
            tier=1,
            importance=3,
            rationale="Rigorous physical checks on external film resistance, internal pore diffusion, axial dispersion, and wall heat transfer.",
            notes="Validates whether the 1D pseudo-homogeneous assumption holds across the full experimental operating range.",
            sources=[
                SourceItem(
                    title="Deep Dive E: Operating Regime & Transport Phenomena",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/E_operating_regime_transport_2026-10-14.md",
                    section="Full transport analysis",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="e1_transport_criteria",
            parent="letter_e_transport",
            title="Interphase & Intraparticle Transport Screening",
            tier=1,
            importance=2,
            rationale="Calculates Mears criterion (<0.15) and Weisz-Prater modulus (<0.3) for Larsen reactor conditions.",
            notes="Confirms that at T <= 50 °C, reaction is strictly in the chemical kinetic regime without internal pore diffusion limitations.",
            sources=[
                SourceItem(
                    title="Deep Dive E: Operating Regime & Transport",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/E_operating_regime_transport_2026-10-14.md",
                    section="Mears and Weisz-Prater calculations",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="e2_packed_bed_hydrodynamics",
            parent="letter_e_transport",
            title="Packed-Bed Flow Regime & Dispersion",
            tier=1,
            importance=2,
            rationale="Evaluates Reynolds number (Re_p ~ 1.5 - 5.0) and Bodenstein/Peclet number (Pe_ax ~ 120 - 200).",
            notes="Confirms laminar flow with moderate axial dispersion; Ergun equation shows negligible pressure drop (< 0.05 bar).",
            sources=[
                SourceItem(
                    title="Deep Dive E: Operating Regime & Transport",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/E_operating_regime_transport_2026-10-14.md",
                    section="Hydrodynamics and Ergun pressure drop",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter F
        MindMapNode(
            id="letter_f_conservation",
            parent="deep_dives_letters",
            title="Letter F: Conservation Balances & State Inventories",
            tier=1,
            importance=3,
            rationale="Formulates rigorous mass, mole, and energy balance equations in both physical and state-space coordinates.",
            notes="Ensures total mass and atomic element (C, H, inerts) conservation across spatial discretization boundaries.",
            sources=[
                SourceItem(
                    title="Deep Dive F: Conservation State Space",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/F_conservation_state_space_2026-10-14.md",
                    section="Balance equations and inventory checks",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="f1_differential_balances",
            parent="letter_f_conservation",
            title="1D Transient Packed Bed Conservation Equations",
            tier=1,
            importance=3,
            rationale="Coupled partial differential equations governing axial gas concentration and temperature dynamics.",
            notes="Includes convective transport, effective axial dispersion, interphase exchange, and wall cooling jacket flux.",
            sources=[
                SourceItem(
                    title="Deep Dive F: Conservation State Space",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/F_conservation_state_space_2026-10-14.md",
                    section="Differential equations",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="f2_surface_state_space",
            parent="letter_f_conservation",
            title="Dynamic Surface Coverage State θ(z, t)",
            tier=1,
            importance=3,
            rationale="Integrates dynamic surface site conservation sum(theta_i) = 1 as an explicit algebraic manifold in DAE system.",
            notes="Avoids index-2 DAE singularity through coordinate projection or index-1 state reformulation.",
            sources=[
                SourceItem(
                    title="Deep Dive F: Conservation State Space",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/F_conservation_state_space_2026-10-14.md",
                    section="DAE manifold index reduction",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter G
        MindMapNode(
            id="letter_g_numerics",
            parent="deep_dives_letters",
            title="Letter G: Numerical Schemes, Stiffness & Jacobian",
            tier=1,
            importance=3,
            rationale="Designs high-performance numerical simulation architecture: spatial discretization, stiff DAE integration, and linear algebra.",
            notes="Compares finite difference, finite volume, and orthogonal collocation schemes on execution speed and mass conservation.",
            sources=[
                SourceItem(
                    title="Deep Dive G: Numerical Methods & Feasibility",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md",
                    section="Numerical methods evaluation",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="g1_spatial_discretization",
            parent="letter_g_numerics",
            title="Spatial Discretization Schemes",
            tier=1,
            importance=2,
            rationale="Converts 1D PDEs along bed coordinate z into a coupled system of ODEs/DAEs in time.",
            notes="Selects flux-conservative upwind finite volume for robust shock capturing during sharp square-wave periodic pulses.",
            sources=[
                SourceItem(
                    title="Deep Dive G: Numerical Methods",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md",
                    section="Spatial schemes comparison",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="g2_stiff_integrators",
            parent="letter_g_numerics",
            title="Stiff Temporal Integrators",
            tier=1,
            importance=3,
            rationale="Benchmarks implicit BDF and Radau IIA methods against explicit Runge-Kutta; confirms explicit solvers fail due to stiffness ratio > 1e7.",
            notes="Implicit solvers maintain A-stability and L-stability across rapid chemical transients.",
            sources=[
                SourceItem(
                    title="Deep Dive G: Numerical Methods",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md",
                    section="Stiff ODE integrator benchmarks",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter K
        MindMapNode(
            id="letter_k_validation",
            parent="deep_dives_letters",
            title="Letter K: Current Results Validation Status",
            tier=1,
            importance=3,
            rationale="Audits current simulation outputs against experimental conversion and selectivity data from Larsen thesis.",
            notes="Establishes formal validity envelope: validated for steady-state between 35–65 °C, H2:C2H2 ratio 1.5–3.0.",
            sources=[
                SourceItem(
                    title="Deep Dive K: Results Validation Status",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/K_results_validation_status_2026-10-14.md",
                    section="Validation status note",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter L
        MindMapNode(
            id="letter_l_periodic",
            parent="deep_dives_letters",
            title="Letter L: Periodic Optimisation Research Outlook",
            tier=1,
            importance=3,
            rationale="Theoretical analysis of forced periodic operation: optimal frequency, amplitude, and wave shape for selectivity enhancement.",
            notes="Identifies conditions under which cycle-averaged ethylene yield surpasses the steady-state maximum.",
            sources=[
                SourceItem(
                    title="Deep Dive L: Periodic Optimisation Research Outlook",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/L_periodic_optimisation_research_outlook_2026-10-14.md",
                    section="Full periodic research outlook",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # Letter M
        MindMapNode(
            id="letter_m_editorial",
            parent="deep_dives_letters",
            title="Letter M: Editorial Synthesis of PR #4",
            tier=1,
            importance=2,
            rationale="Synthesizes deep-dive findings into a cohesive, peer-reviewed presentation narrative for committee review.",
            notes="Structures ten-slide deck reconciling physical insights with mathematical control theory.",
            sources=[
                SourceItem(
                    title="Deep Dive M: Editorial Synthesis Dossier",
                    path="Academics/BEP/Catalysis/presentation/deep-dives/M_editorial_synthesis_pr4_2026-10-14.md",
                    section="Editorial review of PR #4",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),

        # =====================================================================
        # 5. ADMINISTRATIVE BRANCH (parent: administrative)
        # =====================================================================
        MindMapNode(
            id="admin_supervisory_committee",
            parent="administrative",
            title="Supervisory Committee Alignment (Urakawa / CaSE & Gromotka / DIAM)",
            tier=1,
            importance=2,
            rationale="Coordinates monthly progress reviews, experimental data transfers, and defense committee consensus.",
            notes="Bi-weekly touchpoints with Prof. Atsushi Urakawa (CaSE) and Dr. Jochen Gromotka (DIAM) to guarantee dual departmental approval.",
            sources=[
                SourceItem(
                    title="BEP Catalysis Project Conventions §13",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§13 Dual BEP Supervision & Scope",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="admin_thesis_timeline",
            parent="administrative",
            title="BEP Milestone & Deliverable Schedule",
            tier=1,
            importance=2,
            rationale="Tracks formal academic gates: Go/No-Go presentation, mid-term report, draft thesis freeze, and defense date.",
            notes="Governed by TU Delft Faculty of Applied Sciences (TNW) MSc/BEP graduation regulations.",
            sources=[
                SourceItem(
                    title="BEP Thesis Project Management Plan",
                    path="Academics/BEP/Catalysis/conventions.md",
                    section="§1 Thesis Milestones",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
        MindMapNode(
            id="admin_repo_infrastructure",
            parent="administrative",
            title="Dual Repository Management & CI/CD Pipelines",
            tier=1,
            importance=2,
            rationale="Maintains audit trail across private Aa Project Management and public Methanol-Catalysis GitHub repositories.",
            notes="Enforces R-PUSH and R-PUBLIC git governance rules and automated Pixi test verification workflows.",
            sources=[
                SourceItem(
                    title="Methanol-Catalysis AGENTS.md",
                    path="Methanol-Catalysis/AGENTS.md",
                    section="R-PUSH and R-PUBLIC Governance Rules",
                ),
            ],
            open_questions=[],
            is_draft=True,
        ),
    ]

    return nodes


def synthesize_and_save() -> MindMap:
    """Check generated candidates against the curated overlay without overwriting it."""
    nodes = generate_synthesized_nodes()
    generated = {node.id: node for node in nodes}
    current = load_map(DRAFT_PATH)
    curated = {node.id: node for node in current.nodes}

    def serialized(node: MindMapNode) -> dict:
        return node.model_dump(exclude_none=False, mode="json")

    generated_ids = set(generated)
    curated_ids = set(curated)
    changed = sorted(
        node_id
        for node_id in generated_ids & curated_ids
        if serialized(generated[node_id]) != serialized(curated[node_id])
    )
    candidate_only = sorted(generated_ids - curated_ids)
    curated_only = sorted(curated_ids - generated_ids)

    if candidate_only or curated_only or changed:
        raise RuntimeError(
            "Refusing to overwrite the curated draft overlay: "
            f"candidates={len(generated)}, overlay={len(curated)}, "
            f"shared={len(generated_ids & curated_ids)}, "
            f"candidate-only={len(candidate_only)}, "
            f"overlay-only={len(curated_only)}, changed-records={len(changed)}. "
            "No file was written. Reconcile candidate records through the taxonomy "
            "and keep A–M dossiers and project tasks outside the science-root tree."
        )

    print(f"[synthesis] Curated overlay already matches all {len(curated)} candidates; no write needed.")
    return current


def main() -> None:
    try:
        synthesize_and_save()
    except RuntimeError as exc:
        print(f"[synthesis] Stopped safely: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
