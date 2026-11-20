# Source evidence separation — BEP agent island convention

**Applies to all five independent BEP agent branches** (A1 Schbib, A2 dynamic reactor, A3 theory and defense, A4 Larsen, A5 PdAg–CO). This is a **source-provenance convention**, not a claim that all evidence has been checked or that the owner personally understands it.

## Fixed directory structure

```
research/evidence/
  README.md
  original/        Original unedited paper/PDF/image/data, plus link manifests
  transcriptions/  Readable source-faithful text and tables extracted from originals
  analysis/        Agents' explanations, derivations, hypotheses, criticism, research reports
  derived/         Processed data, fitted vectors, digitizations, calculations and run evidence
```

**Strict distinction:** An original source ≠ a transcription ≠ a proposed interpretation ≠ a computed result ≠ owner-approved knowledge. Each kind must be labelled and traceable to its source. Never paste AI deductions as supposed literal source transcription; do not label digitization/fit as measured raw data. An equation in a paper is still not proof that it describes a different catalyst or experimental setting.

**No mass migration or duplication:** Existing original PDFs/HTML under `research/literature/`, archived appendix images under `notebooks/benchmarks/source_renders/`, notebooks in `notebooks/` and historical reports keep their present paths (to avoid breaking Git history, data-relative paths and branch integration). This structure defines **where new evidence belongs** and where indices to old files live. Do not copy copyrighted source files or move repository assets merely to make the directory look complete; link pinned originals, include their exact paths, and preserve provenance.

**Transcription protocol:** For each scanned page, provide a readable Markdown transcription under `transcriptions/` or a small plaintext/CSV companion for long tables. Include source title, exact PDF page index **and** printed page if known, path/link to original image/PDF, transcription method (native text, manual, OCR), status (`raw_unchecked`, `checked_against_image`, `ambiguous`), omissions, uncertain characters (`[unclear]`), equations/units and original-versus-transcriber editorial distinctions. Verify technical notation, superscripts, subscripts, decimals and minus signs against a rendered page. OCR is a draft method, not verification; never call it a verified transcription without visual review. Preserve full original table structure and code listings rather than retaining only convenient fitted values.

**Analysis protocol:** Put explanatory prose, mathematical derivations, source comparisons and model variants under `analysis/`, or put index links there to existing `research/reports/`. Use precise citations to `original/` and `transcriptions/`; distinguish confirmed, disputed, inferred and hypothetical claims. Do not assert "validated" from stored notebook output.

**Derived protocol:** Keep cleaned/selected data, digitized plots, numerical overlays, notebook results and verification checks under `derived/` or link existing `notebooks/benchmarks/data/`. Record generator/input source, transformations, units, uncertainties, executed code commit and rerun status.

**Owner boundary:** None of these files is the owner's personal map or owner-written scientific explanation. Actual owner understanding requires a separate owner-led discussion and explicit, specific approval before any map changes. Pending science-teaching questions are in the distinct owner queue Q99–Q106.

**Parallel/branch rule:** Every agent uses the same logical structure **on its own branch only**, and may revise its evidence independently. Do not merge entire branch histories or overwrite sibling GOAL/TODO files. Future Agent 5 reference imports should use reviewed source snapshots with provenance and an explicit, separate integration PR.
