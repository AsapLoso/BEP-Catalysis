# Presentation checkpoint — quality report

**14 October 2026 · Research snapshot `996781c` · 10 slides, target 9 min 30 s.**

## Deliverables checked

- `BEP_Dynamic_Acetylene_Progress.html`: one standalone 16:9 HTML with inline vector figures and runtime; no external fonts, scripts or image assets.
- `BEP_Dynamic_Acetylene_Progress.pdf`: ten 16:9 pages, including the analytic amplitude-and-phase figure.
- `BEP_Presentation_Outline.docx`: native editable Word text, 30 native bullet paragraphs, zero embedded media. Built using `python-docx`, then opened and exported with LibreOffice for layout inspection.
- `GLOBAL_PRESENTATION_OUTLINE.md` and the HTML/PDF reading versions: substantial speaking bullets, short scientific context, visual proposals, transitions and source links. No written speech or page screenshots form the document.
- Concise cues, claim checklist, integration log, editable shared content and reproducible generation scripts.

## Rendering and controls

- Every slide rendered and visually inspected at 1920×1080. A second complete pass at 1366×768 checks the scaled stage and footer clearance.
- The automated harness checks slide count, arrow-key navigation, cue toggle and Escape, browser errors, external references, body overflow, footer overlap and screenshot size.
- Every slide is rendered again from an isolated copy of the single HTML with browser networking disabled. Corresponding images are byte-identical and no HTTP requests occur.
- **Environment limitation:** managed Chromium blocks direct `file://` navigation. The harness therefore reads the isolated HTML bytes and loads them with `setContent` while networking is disabled. Direct double-click opening was not exercised in that managed browser; all required content is inline.
- PDF page counts and sizes were checked with `pdfinfo`; the slide PDF and the outline were also visually inspected after export.

## Review and corrections

- An independent read-only reviewer inspected all ten rendered slides and the scientific scope. Initial scores were 8–9/10, with no clipping or overlap blocker.
- Corrected ambiguous optimizer-failure wording: a failed recovery optimizer alone does not establish non-identifiability.
- Clarified that PSSA describes the surface closure, and labelled the Jacobian pattern as schematic.
- Added the requested phase-shift inset. Independent focused review confirmed amplitude ratio 0.720942409, lag 358.692644°, phase lead error 1.307356°, and normalized zero crossing 0.996368456. The same-frequency and exact-time conditions remain explicit.
- Corrected the bulk subscript to Latin **b**, made the inlet sketch a constant-amplitude conceptual sinusoid, and resolved compact-layout overflow during production.

## Scientific boundaries

- No new chemistry, model fitting, optimizer, reactor benchmark or experimental validation was executed for this presentation task.
- G's response is an analytic pure-advection example. The source-simulator's preliminary conversion/selectivity numbers are excluded under K.
- F's resolved conservation issue remains an open verification question; no quantified residual or physical consequence is claimed.
- L's same-mean versus best-admissible-steady distinction is incorporated as a future comparison requirement. No objective or supervisor approval is assumed.
- The 9½-minute duration is an editorial allocation, not a measured rehearsal time. F/G correspondence and scientific questions remain open.

## Reproduction

```bash
node scripts/build_presentation.cjs
python scripts/build_outline_docx.py
node scripts/capture_slides.cjs
```

Use `pixi run python` when that environment is available. The presentation HTML itself needs no build command or network connection.
