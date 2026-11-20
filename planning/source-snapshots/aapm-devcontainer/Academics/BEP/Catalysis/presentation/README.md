# BEP Catalysis — presentation archive and resource map

The canonical current status, owner decisions and scientific review boundaries live in the [BEP state](../state.md). This README maps the presentation materials.

## Ten-slide checkpoint package

- [Offline HTML deck](BEP_Dynamic_Acetylene_Progress.html) · [slide PDF](BEP_Dynamic_Acetylene_Progress.pdf)
- [Editable Word outline](BEP_Presentation_Outline.docx) · [Markdown outline](GLOBAL_PRESENTATION_OUTLINE.md) · [HTML outline](BEP_Presentation_Outline.html) · [PDF outline](BEP_Presentation_Outline.pdf)
- [Speaker cues](SPEAKER_NOTES.md) · [claim/source checklist](CLAIM_SOURCE_CHECKLIST.md)
- [QA report](QA_REPORT.md) · [integration log](INTEGRATION_LOG.md) · [checkpoint audit and story rationale](../research/dossiers/presentation_checkpoint_audit_2026_10_14.md)
- [A–M presentation structure](PRESENTATION_STRUCTURE.md) · [deep-dives](deep-dives/) · [deck-wide open questions](DECK_OPEN_QUESTIONS.md)
- [Shared editable content](presentation_content.json) · [build scripts](scripts/) · [rendered slide images](shots/)
- [Presentation handoff](HANDOFF.md) · [original PR #4 branch](https://github.com/AsapLoso/project-management-agents/tree/codex/bep-presentation-2026-10-14)

The HTML deck is self-contained, works offline, and supports keyboard navigation; N opens speaker cues, F toggles fullscreen, and P prints or saves a PDF. Editable content is centralized in [presentation_content.json](presentation_content.json). To rebuild from this folder:

```bash
node scripts/build_presentation.cjs
python scripts/build_outline_docx.py
node scripts/capture_slides.cjs
```

The first command regenerates the HTML deck, Markdown/HTML outline and speaker cues. The second creates the Word outline. The last uses Playwright and Chromium for slide capture and PDF export. Set `CHROME_PATH` or `PLAYWRIGHT_MODULE` for local installations; use `pixi run python` when that environment is available. The QA report records the captured checks and the managed-browser limitation.

The HTML itself requires no build step, server or network connection.

## Existing notebook-first prototype

These are **presentation artifacts**, not the validated numerical reactor model. They reproduce a notebook-first, 16:9 HTML stage with vertically moving Jupyter cells and a sideways Method-of-Lines explanatory detour.

- `BEP_Catalysis_Presentation_v1.ipynb`: editable demonstration notebook, including saved outputs. The transient example is **transport-only**, with no active catalytic kinetics.
- `BEP_Notebook_Presentation_v3.html`: standalone HTML presentation. Open this file in a modern browser (no web server required). Use arrow keys / Space to navigate, `F` for fullscreen and `G` for section navigation.
- `build_bep_notebook_stage.py`: regenerates the HTML from the notebook in the same folder; presentation detour slides are currently defined in this generator.

To rebuild, use Python with `nbformat`, `nbconvert`, `beautifulsoup4`, `markdown-it-py`, and `matplotlib` installed:

```bash
python build_bep_notebook_stage.py
```

The notebook is a curated teaching/presentation artifact based on the BEP model structure, **not** the original full model. The actual reactor implementation and defect register remain in [`../3_Model/`](../3_Model/). Do not interpret the illustrative plots as validated acetylene semi-hydrogenation predictions.
