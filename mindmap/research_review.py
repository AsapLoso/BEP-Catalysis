"""Research Review Pipeline & Question Dossier Generator.

Compiles proposed draft overlay nodes into a guided review path and exports
structured question portfolios and executive review dossiers for owner evaluation.
"""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from Academics.BEP.Catalysis.mindmap.editor import load_map, promote_draft_node
    from Academics.BEP.Catalysis.mindmap.schema import MindMap, merge_maps
except (ImportError, ModuleNotFoundError):
    from editor import load_map, promote_draft_node
    from schema import MindMap, merge_maps

DATA_DIR = Path(__file__).resolve().parent / "data"
CANONICAL_PATH = DATA_DIR / "bep_map.yaml"
DRAFT_PATH = DATA_DIR / "bep_draft_overlay.yaml"

DOSSIER_PATH = (
    Path(__file__).resolve().parents[1] / "research" / "dossiers" / "bep_mindmap_review_dossier.md"
)
QUESTIONS_PATH = (
    Path(__file__).resolve().parents[1] / "research" / "questions" / "phase_4_questions.json"
)


def get_consolidated_review_data() -> Dict[str, Any]:
    """Extract review items and statistics across canonical map and draft overlay."""
    can_map = load_map(CANONICAL_PATH)
    drf_map = load_map(DRAFT_PATH) if DRAFT_PATH.exists() else MindMap(nodes=[])
    merged = merge_maps(can_map, drf_map)

    # Categories
    categories = {
        "Physics": ["reaction_thermodynamics", "lhhw_kinetics", "centered_arrhenius", "surface_coverage_dynamics", "transport_phenomena", "internal_diffusion_thiele", "external_film_transfer"],
        "Mathematics": ["pbr_governing_pdes", "method_of_lines_mol", "stiff_ode_solvers", "parameter_sensitivity_jacobian"],
        "Systems & Control": ["reactor_operating_window", "periodic_feed_forcing", "cooling_jacket_control", "state_observer_mpc"],
    }

    return {
        "canonical_count": len(can_map.nodes),
        "draft_count": len(drf_map.nodes),
        "total_count": len(merged.nodes),
        "categories": categories,
        "draft_nodes": [n.model_dump(mode="json") for n in drf_map.nodes],
        "canonical_nodes": [n.model_dump(mode="json") for n in can_map.nodes],
    }


def compile_questions_portfolio() -> Dict[str, Any]:
    """Compile all owner-facing questions with recommended options and physical rationale."""
    questions = [
        {
            "id": "Q-BEP-REVIEW-01",
            "island": "Physics: Kinetics",
            "question": "How should reaction rates be normalized in the 1D PBR given that cross-sectional area A and catalyst support density rho_support are omitted from Larsen (2024)?",
            "suggested_options": [
                "(Recommended) Render raster pages 77–88 (Appendix F) as high-res images to extract experimental tube diameter and bed packing specifications.",
                "Adopt standard micro-reactor tubular geometry (e.g. 4 mm inner diameter, catalyst bed density 800 kg/m^3) and document as an explicit modeling assumption."
            ],
            "recommended": "(Recommended) Render raster pages 77–88 (Appendix F) as high-res images to extract experimental tube diameter and bed packing specifications.",
            "rationale": "Conventions §12.3 and §12.4 confirm Appendix F contains experimental setup details on non-OCR raster pages. Extracting primary facts preserves zero-hallucination ground truth.",
            "blocking_level": "hard",
            "answer": None,
        },
        {
            "id": "Q-BEP-REVIEW-02",
            "island": "Physics: Temperature Dependence",
            "question": "Which reference temperature T0 should be selected for the Centered Arrhenius parameter re-scaling?",
            "suggested_options": [
                "(Recommended) T0 = 313.15 K (40 °C), matching the central isotherm of the Larsen catalyst kinetic screening tests.",
                "T0 = 323.15 K (50 °C), matching the midpoint of the industrial acetylene converter operating window."
            ],
            "recommended": "(Recommended) T0 = 313.15 K (40 °C), matching the central isotherm of the Larsen catalyst kinetic screening tests.",
            "rationale": "Minimizes covariance between pre-exponential factor k0 and activation energy Ea around the experimental data cluster (Berger Eq. 17).",
            "blocking_level": "soft",
            "answer": None,
        },
        {
            "id": "Q-BEP-REVIEW-03",
            "island": "Physics: Adsorption Mechanism",
            "question": "Should hydrogen adsorption on the Ag-promoted Pd catalyst be modeled as associative or dissociative?",
            "suggested_options": [
                "(Recommended) Non-dissociative (associative) molecular adsorption as formulated in Larsen Eq. 6.9 (final fitted model).",
                "Dissociative adsorption with square-root hydrogen partial pressure dependence sqrt(p_H2)."
            ],
            "recommended": "(Recommended) Non-dissociative (associative) molecular adsorption as formulated in Larsen Eq. 6.9 (final fitted model).",
            "rationale": "Conventions §12.1 verified Larsen Eq. 6.9 verbatim against the thesis text; altering the rate denominator to sqrt(p_H2) would invalidate benchmark parameters.",
            "blocking_level": "soft",
            "answer": None,
        },
        {
            "id": "Q-BEP-REVIEW-04",
            "island": "Physics: Velocity Definition",
            "question": "Should fluid velocity in the 1D axial transport equations be superficial velocity u_s or interstitial velocity u_s / epsilon_b?",
            "suggested_options": [
                "(Recommended) Superficial velocity u_s with explicit bed voidage epsilon_b in the accumulation term (Berger 2008 Eq. 1).",
                "Interstitial velocity u = u_s / epsilon_b throughout all convective terms."
            ],
            "recommended": "(Recommended) Superficial velocity u_s with explicit bed voidage epsilon_b in the accumulation term (Berger 2008 Eq. 1).",
            "rationale": "Conventions §12 open ambiguity confirms a factor of epsilon_b (~0.4) on the convective scale directly shifts characteristic residence time tau_res and Peclet number Pe.",
            "blocking_level": "hard",
            "answer": None,
        },
        {
            "id": "Q-BEP-REVIEW-05",
            "island": "Mathematics: Numerical Discretization",
            "question": "Which spatial discretization scheme should be prioritized for the hyperbolic convective advection terms in the 1D PBR?",
            "suggested_options": [
                "(Recommended) First-order backward/upwind difference for unconditional monotonic stability without spurious oscillations.",
                "Second-order upwind with flux-limiter (e.g. Superbee or Minmod) to reduce numerical dissipation during steep front propagation."
            ],
            "recommended": "(Recommended) First-order backward/upwind difference for unconditional monotonic stability without spurious oscillations.",
            "rationale": "Conventions §11 Item 7 locks backward/upwind difference as the baseline MOL scheme. Flux limiters can be introduced as a second-order refinement.",
            "blocking_level": "soft",
            "answer": None,
        },
        {
            "id": "Q-BEP-REVIEW-06",
            "island": "Systems & Control: Dynamic Operation",
            "question": "What is the primary objective function for periodic feed concentration forcing in the dual BEP?",
            "suggested_options": [
                "(Recommended) Maximize ethylene selectivity S_C2H4 while constraining maximum bed temperature below runaway limit T_max = 380 K.",
                "Maximize total acetylene conversion X_C2H2 regardless of intermediate selectivity."
            ],
            "recommended": "(Recommended) Maximize ethylene selectivity S_C2H4 while constraining maximum bed temperature below runaway limit T_max = 380 K.",
            "rationale": "Industrial semi-hydrogenation is fundamentally selectivity-limited; over-hydrogenation to ethane consumes valuable product and triggers severe exothermic hotspots.",
            "blocking_level": "soft",
            "answer": None,
        },
    ]

    return {
        "phase_num": 4,
        "phase_title": "Collaborative Review Path & Question Dossier",
        "created_at": 1792453800.0,
        "questions": questions,
    }


def generate_review_dossier_markdown() -> str:
    """Generate comprehensive executive review briefing markdown document."""
    data = get_consolidated_review_data()
    questions_data = compile_questions_portfolio()

    md = f"""# BEP Mind Map: Executive Review Dossier & Question Portfolio
Date: 2026-10-20  
Status: Ready for Human Owner Review  
Target Application: `Academics/BEP/Catalysis/mindmap/`  
Live Preview: `pixi run preview` (http://127.0.0.1:8765)

---

## 1. Executive Summary

This dossier presents the consolidated ownership mind-map architecture and research synthesis for the Dual BEP (Applied Physics & Applied Mathematics), formulated in accordance with **PR #84** and **Catalysis Project Conventions §13**.

The mind map separates ground truth into two distinct layers:
1. **Approved Canonical Map (`data/bep_map.yaml`):** Contains {data['canonical_count']} verified, owner-approved nodes (root `bep` and primary arms `physics`, `mathematics`, `systems_control`).
2. **AI Proposed Draft Overlay (`data/bep_draft_overlay.yaml`):** Contains {data['draft_count']} synthesized research nodes, each assigned strictly to **Tier 1 (Amber, AI Proposal)** with zero-hallucination citation backing.

---

## 2. Structural Topology & Branch Inventory

```
bep (Dual BEP: Acetylene Semi-Hydrogenation Reactor Modeling) [Tier 2, ★★★]
├── physics [Tier 0]
│   ├── reaction_thermodynamics [Tier 1, ★★★]
│   ├── lhhw_kinetics [Tier 1, ★★★]
│   │   ├── centered_arrhenius [Tier 1, ★★☆]
│   │   └── surface_coverage_dynamics [Tier 1, ★★★]
│   └── transport_phenomena [Tier 1, ★★★]
│       ├── internal_diffusion_thiele [Tier 1, ★★☆]
│       └── external_film_transfer [Tier 1, ★★☆]
├── mathematics [Tier 0]
│   ├── pbr_governing_pdes [Tier 1, ★★★]
│   ├── method_of_lines_mol [Tier 1, ★★★]
│   ├── stiff_ode_solvers [Tier 1, ★★★]
│   └── parameter_sensitivity_jacobian [Tier 1, ★★☆]
└── systems_control [Tier 0]
    ├── reactor_operating_window [Tier 1, ★★★]
    ├── periodic_feed_forcing [Tier 1, ★★★]
    ├── cooling_jacket_control [Tier 1, ★★☆]
    └── state_observer_mpc [Tier 1, ★★☆]
```

---

## 3. Recommended Sequential Review Path (Guided Tour)

The interactive preview visualizer features an automated **Guided Tour Mode** (`#btn-tour`) that walks the owner through foundational dependencies in order:

| Step | Node ID | Topic Title | Branch | Key Evidence / Citation |
|:---:|---|---|---|---|
| **1** | `reaction_thermodynamics` | Reaction Exothermicity | Physics | Larsen Ch.4 (dH = -172, -136 kJ/mol) |
| **2** | `lhhw_kinetics` | Extended LHHW Kinetics | Physics | Larsen Eqs. 6.9–6.11; Conventions §12.1 |
| **3** | `centered_arrhenius` | Centered Arrhenius Scaling | Physics | Berger (2008) Eq. 17; Conventions §11.5 |
| **4** | `surface_coverage_dynamics` | Dynamic Coverage State $\\theta(z,r)$ | Physics | Berger Sec. 2.1; 3_Model/transient_model_audit |
| **5** | `transport_phenomena` | Coupled 3-Level Transport | Physics | Conventions §11 Item 1-3 ($C_b \\to C_s \\to c_p$) |
| **6** | `internal_diffusion_thiele` | Intraparticle Pore Diffusion | Physics | Berger Sec. 5; Weisz-Prater / Thiele scaling |
| **7** | `external_film_transfer` | Fluid-Solid Film Resistance | Physics | Mears criterion; Sherwood-Reynolds correlation |
| **8** | `pbr_governing_pdes` | 1D Dynamic PBR PDEs | Mathematics | Larsen Eqs. 4.6–4.9; Berger Eq. 1 recovery |
| **9** | `method_of_lines_mol` | Method of Lines Discretization | Mathematics | Upwind convection + Central diffusion (MOL) |
| **10** | `stiff_ode_solvers` | Stiff DAE/ODE Solvers | Mathematics | BDF / Radau IIA via `solve_ivp` |
| **11** | `parameter_sensitivity_jacobian` | Sensitivity & Identifiability | Mathematics | Forward sensitivity equations $s_{{ij}}$ |
| **12** | `reactor_operating_window` | Operating Window & Runaway | Control | van Heerden thermal runaway boundary |
| **13** | `periodic_feed_forcing` | Periodic Flow Modulation | Control | Urakawa / Silveston modulated excitation |
| **14** | `cooling_jacket_control` | Multi-Zone Cooling Dynamics | Control | PDC tubular reactor jacket feedback |
| **15** | `state_observer_mpc` | State Observers & Nonlinear MPC | Control | Conventions §5 candidate methods framing |

---

## 4. Question Portfolio & Reversible Defaults

"""
    for q in questions_data["questions"]:
        md += f"### {q['id']}: {q['question']}\n"
        md += f"- **Island / Domain:** {q['island']}\n"
        md += f"- **Rationale:** {q['rationale']}\n"
        md += f"- **Recommended Default:** {q['recommended']}\n"
        md += "- **Options:**\n"
        for opt in q["suggested_options"]:
            md += f"  - {opt}\n"
        md += "\n"

    md += """---

## 5. Owner Action Guide (Deterministic Promotion)

To promote any draft topic to **Tier 2 (Owner Critically Understood)**:
1. **In Browser:** Run `pixi run preview`, open the Guided Tour, review the supporting citations and notes, and click **"Promote to Approved"**.
2. **Via MCP / Python CLI:**
   ```powershell
   pixi run python Academics/BEP/Catalysis/mindmap/editor.py promote-node --id lhhw_kinetics --tier 2
   ```
   *The editor atomically transfers the node from `bep_draft_overlay.yaml` into `bep_map.yaml` without manual copy-pasting.*
"""
    return md


def main() -> None:
    parser = argparse.ArgumentParser(description="BEP Mind Map Research Review CLI")
    parser.add_argument("--dossier", action="store_true", help="Generate review dossier markdown")
    parser.add_argument("--questions", action="store_true", help="Generate questions JSON portfolio")
    parser.add_argument("--promote", help="Promote node ID to canonical map")
    parser.add_argument("--tier", type=int, default=2, help="Target tier upon promotion (default: 2)")
    args = parser.parse_args()

    if args.dossier:
        DOSSIER_PATH.parent.mkdir(parents=True, exist_ok=True)
        content = generate_review_dossier_markdown()
        DOSSIER_PATH.write_text(content, encoding="utf-8")
        print(f"[review] Generated executive review dossier at {DOSSIER_PATH}")

    if args.questions:
        QUESTIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
        q_data = compile_questions_portfolio()
        QUESTIONS_PATH.write_text(json.dumps(q_data, indent=2), encoding="utf-8")
        print(f"[review] Compiled question portfolio at {QUESTIONS_PATH}")

    if args.promote:
        promoted = promote_draft_node(DRAFT_PATH, CANONICAL_PATH, args.promote, new_tier=args.tier)
        print(f"[review] Promoted node '{promoted.id}' to Tier {promoted.tier} in canonical map.")


if __name__ == "__main__":
    main()
