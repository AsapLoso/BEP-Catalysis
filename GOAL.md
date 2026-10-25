# Agent 1 — Schbib (1996) source and benchmark re-audit

**Branch:** `feat/schbib-co-benchmark`  
**Current task:** independently investigate and correct the Schbib source-model interpretation and benchmark.  
**Tracking issue:** [#10 — Schbib baseline audit](https://github.com/AsapLoso/BEP-Catalysis/issues/10)  
**Dependency:** Agent 5 may not start the combined PdAg–CO model until this and Agent 4's separate audit have been reviewed by the owner.

## 0. First deliverable: YOUR OWN RESEARCH PLAN, then execution

**Begin in plan mode.** Read this GOAL, `TODO.md`, issue #10, the primary sources, the existing benchmark notebook/plots and the relevant repository guidance. **Independently expand the user's proposed corrections into a defensible investigation plan**; do not just parrot a checklist or say "plan looks good."

Your plan must identify:
- exact source conflicts and how you will independently check them (pages, equations, tables, publisher/author corrections);
- the smallest experiments and dimensional checks that discriminate possible causes of the failed Table 6 comparison;
- which existing work is historical, which may be re-used, and what must be rerun;
- explicit PASS/BLOCKED criteria, anticipated deliverables and source-access blockers;
- what you will *not* claim even if your code runs.

**Present the plan for owner review before making substantive scientific/code corrections.** The owner is reviewing scope, priorities, experimental design and whether claims are independently checkable; **the owner is not responsible for personally certifying scientific formulas or original-paper data**. You must verify those yourself against primary material, document competing hypotheses, and state honestly when evidence remains inadequate. After the owner approves the plan, work autonomously on your assigned branch, testing and committing verified changes without seeking approval for each commit. You may do ordinary focused commits/pushes on this branch; never force-push, merge or create a PR without a separate request. Do not touch any owner personal map, owner-written notebook, Agent 4/5 branch or `main`.

## 1. Existing on-branch sources and outputs (inspect; no needless re-fetch)

**New readable source record:** `research/evidence/transcriptions/schbib_1996_author_table8_correction.md` provides the numeric table from a public author-shared corrective note, with a clear UNVERIFIED-AS-JOURNAL-ERRATUM status. Read and **visually verify** it against the linked document before choosing parameters. The older local extracted paper text lacks this appended correction. The companion `research/evidence/` directories separate originals, transcriptions, agent analysis and computed results. Do not silently replace the historical Table 8 or treat the text note as an independently validated source correction.

- `research/literature/schbib_1996_full_article.html` — large article HTML archive; inspect content carefully, including any appended/embedded corrections, and preserve its original bytes.
- `research/literature/schbib_1996_front_end_acetylene_hydrogenation.pdf` — archived paper PDF.
- `research/literature/schbib_1996_extracted_text.txt` — convenience text, **not** a substitute for checking ambiguous superscripts/units against the original page.
- `notebooks/benchmarks/schbib_1996_steady_state.ipynb` — historical agent reproduction, with saved executed output.
- `notebooks/benchmarks/schbib_fig1_conversion_temperature.png`, `schbib_fig2_rates_temperature.png`, `schbib_fig3_axial_profiles.png`, `schbib_fig4_axial_profiles.png` — recorded plots. Inspect them but do **not** call them independently validated or rerun until you actually reproduce them.
- `research/literature/gobbo_2004_*.pdf/.txt` and `research/literature/README.md` — secondary comparison only; Gobbo's later industrial parameter sets must not silently replace Schbib's published laboratory constants.

Use repository-relative paths, not historical `file:///c:/Users/...` links, which may not exist in an agent environment.

## 2. Scientific investigation: do not decide the answer in advance

The existing Schbib benchmark notebook explicitly acknowledges that its simplified model fails to reproduce Table 6 conversions, with a discrepancy near **98 percentage points** in representative cases. This is an **observed problem in the notebook**, not an explanation of the cause.

**Recheck the primary source and any author-supplied/publisher correction to Table 8.** Historical instructions list `log10 A(K_H)=20.2` and `log10 A(K_CO)=13.6`. Leads from prior reading suggest corrected values `17.2` and `10.16` (sometimes rounded `10.2`); **none is to be hard-coded as the corrected truth without verifying its precise primary locator and correction status**. Separate the numerical value of `log10 A` from the actual Arrhenius pre-exponential `A=10^(log10 A)`. Distinguish changes to the adsorption terms from changes to kinetic-rate constants and catalyst-mass basis.

Audit the actual full and simplified rate laws, concentration basis (`kmol/m³` vs `mol/m³`), temperature/Arrhenius sign and units, `K_H sqrt(C_H2)`, `K_CO C_CO`, reaction enthalpies, and source-defined catalyst loading. Verify the original rate denominator exponent and dimensions rather than trusting a prior prose equation. Compare laboratory glycol-bath conditions and models with the historical **adiabatic pseudohomogeneous** notebook; do not treat a deliberately simplified energy closure as a full reproduction. Check the temperature/pressure/space-velocity conditions, Table 6 conversion definitions and missing geometrical parameters.

Test independent, controlled hypotheses: pre-exponential correction; unit conversion; reactor mass/volume/void normalization; boundary/heat-transfer choices; incorrect equation transcription; and any remaining unidentifiable factor. Change one cause at a time with plotted numerical effects. **Never hide failure through silent parameter retuning.**

Derive what a **shared common adsorption denominator** implies for the *local uncapped* ratio of r₂/r₁, and separately discuss reactor-integrated selectivity and possible thermal effects; preferential selective inhibition is **not** automatically established.

## 3. Required results AFTER the plan is approved

1. `research/reports/schbib_parameter_and_benchmark_audit.md`: sourced comparison of original versus any corrected Table 8 entries, units, equation variants, operating conditions, failure diagnoses, actual residuals and an open-uncertainty ledger. Cite exact pages/tables/figure locators and source-access status.
2. Correct/source-faithful `notebooks/benchmarks/schbib_1996_steady_state.ipynb` **on this branch** with clear reproducible comparisons to Table 6 and Figures 1–4. Preserve the historical notebook interpretation in Git history and explain all formula/input changes in the report. Recorded historical plots are not fresh runs.
3. Explicit diagnostics: stoichiometry/element conservation, positive rate denominators, dimensional consistency, Arrhenius/log checks, solver convergence, boundary/geometry conventions; clearly separate internal checks from experimental comparison. Record actual runtime and Python/package environment. The previous under-60-second target is an optimization, not permission to skip the audit.
4. Update `TODO.md` using observed PASS/BLOCKED receipts; report exact committed SHA and the change summary. The report must explain if the original published benchmark remains irreproducible under defensible assumptions.
5. Send a brief **future Agent 5 handoff**: which model pieces and `K_CO` interpretation can be relied upon; what is specific to Pd/Al₂O₃; what is still uncertain about transfer to PdAg.

## 4. Owner-learning boundary

All present work is **AI reference research**. The owner has not necessarily studied any of these derivations. Answer the questions for eventual teaching, but do not add personal-map nodes, mark concepts understood, change source verification to human-verified, or write owner prose. The separate owner-led review queue (Q99–Q106) records future discussion prompts.

**Historical contract notice:** Earlier `GOAL.md` variants prescribed Table 8 numeric values and successful figure replication without qualifying the later source/benchmark discrepancy. Those formulations are preserved in Git history, not automatically validated by this revised goal.
