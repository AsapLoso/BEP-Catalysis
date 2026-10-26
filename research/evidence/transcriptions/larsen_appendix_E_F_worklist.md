# Larsen 2024 — Appendix E/F transcription worklist and status

**Execution status (2026-10-26): PARTIAL, visually checked.** The original worklist below required a page-linked, human-readable transcript. Agent 4 inspected all 18 source renders and completed Appendix E Tables E.1–E.3. The current [transcription](larsen_2024_appendix_E_F.md) captures Appendix F's readable formulas, setup, selected processed responses, code settings, bounds and output excerpts, but does not retype every visible code line or every Pd₀Ag/Pd₂Ag table cell. The source's Pd₃Ag table itself omits its middle rows. Do not describe this status as a complete Appendix F transcript.

## Existing original images

The exact source view is `notebooks/benchmarks/source_renders/appendix_pages/`, PDF page **71–88**, one-based filename `page-<N>.png`. The entire original 97-page thesis PDF is **now committed** at `research/evidence/original/Larsen - 2024 - Semihydrogenation of acetylene to ethylene with a PdAg catalyst.pdf` (byte-verified against the uploaded copy); image-only pages nevertheless require page-by-page transcription.

## Completed source transcription work

- The Markdown transcript links every PDF page 71–88 render and includes a printed page index and review-status note.
- Appendix E tables were transcribed in full and compared with the page images.
- Appendix F excerpts and selected Pd₂Ag/Pd₃Ag responses were checked against the images; these are kept distinct from raw chromatographic data and graph-digitized responses.
- Scientific interpretation and unresolved source/model conflicts are recorded separately in `research/reports/larsen_2024_equation_and_baseline_audit.md`.

## Original completion specification and remaining gap

- The original target remains `research/evidence/transcriptions/larsen_2024_appendix_E_F.md`: one headed section per PDF page, **71 to 88**, with printed page number (if visible), complete readable prose, tables, equations, parameters and relevant source code fragments. For visual-only plots, describe axes, legends and data visibility rather than inventing exact plotted numbers. The current Appendix F coverage has not yet reached this full target.
- For large tables, optionally add `*.csv` with exact transcribed columns and rows; distinguish this from `notebooks/benchmarks/data/larsen_2024_selected_curves.csv` (which already contains a mix of exact table values and graph-digitized estimates).
- For each page: original image link; provenance/method; status `raw_unchecked` then `checked_against_image` only after visual comparison; ambiguity marker `[unclear]` where needed. Use OCR only as a preliminary aid and verify against the original image. Put all interpretation and proposed mathematical corrections into `../analysis/`, **never** within the literal source transcription.
- Create a source-checked readable transcription for main-body Eq. 6.9–6.11 (PDF p. 43) and source-derived Figure 6.6 parameters (PDF p. 44), using the now available complete PDF. Do not claim parameters are printed in Appendix E/F when they actually come from the main text.

## Existing leads (not full source transcript)

- `notebooks/benchmarks/data/larsen_2024_parameters.csv`: agent-extracted vectors from reported Figure 6.6 (main text absent in current image set); units partly marked inferred.
- `notebooks/benchmarks/data/larsen_2024_selected_curves.csv`: exact Pd0Ag Appendix F table data and digitized other-alloy plots *as classified by a prior agent*; their correctness is still awaiting page-wise checking.
- `notebooks/benchmarks/larsen_2024_benchmark.ipynb`: program code and stored outputs, **derived model work**, not original thesis content.

**Current verification gate:** Appendix E and the selected Appendix F evidence are readable, source-linked and visually checked. Full Appendix F transcription remains open; see the explicit PASS/BLOCKED table in the audit report. Do not treat this documentary gap as evidence that the original source tables/code are absent—the visible screenshot material remains available for further transcription.
