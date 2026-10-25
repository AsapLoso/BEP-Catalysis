# Larsen 2024 — Appendix E/F transcription worklist (NOT a verified transcript)

**Status: PAGE TRANSCRIPTION REQUIRED.** The existing 18 PNGs are original-page **image renditions**; there is no comprehensive readable, page-checked transcription of those pages in this branch. Do not claim otherwise. A derived CSV or notebook parameter table **cannot** substitute for a literal, source-faithful page transcription.

## Existing original images

The exact source view is `notebooks/benchmarks/source_renders/appendix_pages/`, PDF page **71–88**, one-based filename `page-<N>.png`. That directory's README explains that the source thesis PDF itself was **not** copied into this branch. The user's separate Zotero archive may contain it locally, but availability in an agent's runtime is unverified.

## Current preparation (not yet a completed transcript)

A [page-by-page Markdown scaffold](larsen_2024_appendix_E_F.md) now exists with links to **each** of the original 18 source PNGs and explicit `not_started` review statuses. This is intentionally **not** a transcription of the source words; none of the 18 source images were visually readable from the assistant's current environment. Fill the scaffold using actual visual evidence and check technical notation page by page.

## Work product Agent 4 must produce

- `research/evidence/transcriptions/larsen_2024_appendix_E_F.md`: one headed section per PDF page, **71 to 88**, with printed page number (if visible), complete readable prose, tables, equations, parameters and any relevant source code fragments. For genuinely visual-only plots describe axes, legends and data visibility rather than inventing exact plotted numbers. Pages with no machine-readable text still require human-readable manual transcription from the image.
- For large tables, optionally add `*.csv` with exact transcribed columns and rows; distinguish this from `notebooks/benchmarks/data/larsen_2024_selected_curves.csv` (which already contains a mix of exact table values and graph-digitized estimates).
- For each page: original image link; provenance/method; status `raw_unchecked` then `checked_against_image` only after visual comparison; ambiguity marker `[unclear]` where needed. Use OCR only as a preliminary aid and verify against the original image. Put all interpretation and proposed mathematical corrections into `../analysis/`, **never** within the literal source transcription.
- Create a distinct transcription for Larsen's *main-body* Eq. 6.9–6.11 and Figure 6.6 **only if the full thesis is actually accessible**. These pages are absent from the 18 PNGs; do not hallucinate their source text. Highlight this source blocker in the report.

## Existing leads (not full source transcript)

- `notebooks/benchmarks/data/larsen_2024_parameters.csv`: agent-extracted vectors from reported Figure 6.6 (main text absent in current image set); units partly marked inferred.
- `notebooks/benchmarks/data/larsen_2024_selected_curves.csv`: exact Pd0Ag Appendix F table data and digitized other-alloy plots *as classified by a prior agent*; their correctness is still awaiting page-wise checking.
- `notebooks/benchmarks/larsen_2024_benchmark.ipynb`: program code and stored outputs, **derived model work**, not original thesis content.

**Next audit gate:** Give the owner a link to a readable transcription, not merely a PNG gallery, along with a separate source-vs-model discrepancy report. The owner does not have to personally certify all thesis equations to let the agent investigate.
