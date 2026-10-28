# Larsen 2024 — Appendix E/F transcription worklist and status

**Execution status (2026-10-26): RECOVERABLE TRANSCRIPTION COMPLETE, visually checked with source gaps.** The [transcription](larsen_2024_appendix_E_F.md) contains Appendix E Tables E.1–E.3; all readable Appendix F code on PDF pp. 78–88; every displayed processed-input table row and legible cell; and the full 41-row Pd₀Ag standard-model comparison output. The linked CSV gives page references and marks unreadable/cropped cells. Larsen's Pd₃Ag table omits its middle rows; intermediate pandas previews also omit rows or columns, as documented page by page. No absent data are reconstructed.

## Existing original images

The exact source view is `notebooks/benchmarks/source_renders/appendix_pages/`, PDF page **71–88**, one-based filename `page-<N>.png`. The entire original 97-page thesis PDF is **now committed** at `research/evidence/original/Larsen - 2024 - Semihydrogenation of acetylene to ethylene with a PdAg catalyst.pdf` (byte-verified against the uploaded copy); image-only pages nevertheless require page-by-page transcription.

## Completed source transcription work

- The Markdown transcript links every PDF page 71–88 render and includes a printed page index and review-status note.
- Appendix E tables were transcribed in full and compared with the page images.
- Appendix F code, all displayed processed-input table rows/cells that can be read, and the Pd₀Ag fitted comparison output were checked against the images; these are kept distinct from raw chromatographic data and graph-digitized responses.
- Scientific interpretation and unresolved source/model conflicts are recorded separately in `research/reports/larsen_2024_equation_and_baseline_audit.md`.

## Original completion specification and remaining gap

- The transcription target is met for readable source text, equations, parameters, code and displayed processed/comparison table entries on PDF pages **71–88**. Computed head/tail previews are documented without reconstructing omitted rows; pandas-elided columns, the source-omitted Pd₃Ag middle, and unreadable/cropped raster cells remain explicit gaps. Visual-only plot points are not invented.
- For large tables, optionally add `*.csv` with exact transcribed columns and rows; distinguish this from `notebooks/benchmarks/data/larsen_2024_selected_curves.csv` (which already contains a mix of exact table values and graph-digitized estimates).
- For each page: original image link; provenance/method; status `raw_unchecked` then `checked_against_image` only after visual comparison; ambiguity marker `[unclear]` where needed. Use OCR only as a preliminary aid and verify against the original image. Put all interpretation and proposed mathematical corrections into `../analysis/`, **never** within the literal source transcription.
- Create a source-checked readable transcription for main-body Eq. 6.9–6.11 (PDF p. 43) and source-derived Figure 6.6 parameters (PDF p. 44), using the now available complete PDF. Do not claim parameters are printed in Appendix E/F when they actually come from the main text.

## Existing leads (not full source transcript)

- `notebooks/benchmarks/data/larsen_2024_parameters.csv`: agent-extracted vectors from reported Figure 6.6 (main text absent in current image set); units partly marked inferred.
- `notebooks/benchmarks/data/larsen_2024_selected_curves.csv`: exact Pd0Ag Appendix F table data and digitized other-alloy plots *as classified by a prior agent*; their correctness is still awaiting page-wise checking.
- `notebooks/benchmarks/larsen_2024_benchmark.ipynb`: program code and stored outputs, **derived model work**, not original thesis content.

**Current verification gate:** Appendix E and all recoverable Appendix F text/table content are source-linked and visually checked. The transcription gate passes with the source gaps listed above and in the audit report. Do not treat those gaps as evidence that the original source tables/code are absent; distinguish genuinely omitted rows and unreadable cells from readable material already transcribed.
