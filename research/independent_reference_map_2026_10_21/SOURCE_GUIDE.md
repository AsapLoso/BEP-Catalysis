# Independent scientific map — starting sources

All paths are relative to repository root in `AsapLoso/project-management-agents`. They were checked to exist on `experiment/bep-independent-science-map-20261021` on 2026-10-21.

## First-pass source set (read in this order)

| File | Role | What to extract |
|---|---|---|
| `Academics/BEP/Catalysis/0_Project_Management/main.tex` | **Primary project framing** | Problem statement, hypotheses, research questions, assumptions, balances, methodological scope, planned validation, deliverables |
| `Academics/BEP/Catalysis/0_Project_Management/references.bib` | Bibliographic locator index | Original paper titles, authors, DOIs, original publication claims to check directly |
| `Academics/BEP/Catalysis/0_Project_Management/section1_intro.tex` | Standalone introduction draft | Alternative phrasing and research-question detail; check revision differences against main.tex |
| `Academics/BEP/Catalysis/0_Project_Management/section2_lit.tex` | Standalone literature draft | Paper leads, proposed literature gap, PSSA and experimental-method claims; verify against originals |
| `Academics/BEP/Catalysis/0_Project_Management/section3_method.tex` | Standalone methodology draft | Reactor governing equations, boundary assumptions, surface-state dynamics, discretization, input parameterization and validation strategy; check differences against main.tex |
| `Academics/BEP/Catalysis/0_Project_Management/bep_proposal_roadmap.md` | Planning/context aid | Scope and discipline coverage; **not independent scientific evidence** |

**Critical revision caveat:** `main.tex` includes its own proposal sections and does not simply include these separate files at LaTeX build time. Treat standalone `section*.tex` as potentially different revisions; identify discrepancies and select the proposal baseline explicitly in `method.md`.

## Primary-source escalation

Follow citations in `references.bib` to original literature when possible. Aim to ground key mechanisms, physics assumptions, kinetic constants, mathematical statements and experimental applicability in original articles or rigorous technical references, not merely the proposal. Record:

- Full author/title/year, DOI or stable URL, and source type (paper, proposal, experiment, code, theoretical derivation).
- Exact page/section/equation/figure/table locator when available.
- What particular claim the cited locator supports, and what it does **not** support.
- Whether the original source was actually accessed, accessible only by abstract, or only cited secondhand.
- Source-system differences such as catalyst, support, feed, pressure, temperature and timescale.

Do not claim an unpublished experimental result or validated performance gain because a project proposal anticipates it.

## Source interpretation standard

Use these distinctions consistently:

**Observed/published under stated conditions** ≠ **proposed project hypothesis** ≠ **mathematical deduction under assumptions** ≠ **physically plausible interpretation** ≠ **unverified possibility**.

Place these tags in node claim/evidence details rather than relying solely on an overall maturity color.

## Later research inputs

Additional primary sources or direct experiment descriptions may be located as scientifically needed. Later supporting research dossiers are useful to identify leads but are not inherently independent proof; when added after first baseline, identify that as a distinct literature-enrichment pass. Broad project tracking, presentation artifacts and existing app implementation are not needed to derive the initial scientific subject taxonomy.
