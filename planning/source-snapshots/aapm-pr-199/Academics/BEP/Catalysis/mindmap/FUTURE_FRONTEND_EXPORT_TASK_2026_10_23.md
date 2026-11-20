# Deferred frontend task — portable export of the *real* BEP mind-map viewer

**Owner instruction (23 October 2026):** Record this for the **frontend worker**, **do not implement it in the present science-map conversation**. It is a future viewer feature, not permission to alter owner-approved science, publish the map, or send material to Damian.

## Why this task exists

A separate science-map session produced a basic, standalone HTML **proof of concept**:

`Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/exports/BEP_owner_map_Damian_review_2026-10-23.html`

on the evolving docs branch `docs/bep-theme-first-progress-units-20261022`.

The owner noticed that this local HTML renders a navigable snapshot but is **not an export of the real, established BEP mind-map frontend**. They want the *actual frontend worker* to own a future proper export, reusing the current application rather than creating another simplistic independent renderer. Preserve the proof of concept as historical work; don't confuse it with the final frontend capability.

## Requested future deliverable

Provide a deliberate **Export / Save portable map** workflow in the **existing** `Academics/BEP/Catalysis/mindmap/` application (Python adapter + SVG/JS frontend). Deliver an export that represents the chosen snapshot with the genuine viewer's graph, navigation, current reader pages, source/approval distinctions and assets as far as practical, rather than simply listing node text.

A strong design should:

1. **Reuse actual viewer features** and styles, not duplicate all visualization code into an unrelated new mini-app. Preserve hierarchy, focus/navigation, responsive rendering and an easy route from graphical nodes to linked reader Markdown.
2. **Work offline/local** after export. Choose a safe portable format (e.g. an HTML bundle with local packaged assets, or fully self-contained HTML where practical). State unavoidable browser/file-scheme or linked-asset limitations instead of claiming it is standalone when it depends on local server endpoints, CDNs, GitHub authentication or ChatGPT Library.
3. **Snapshot deliberately**: read a user-selected owner-map or AI-reference-map revision, make the source ref/SHA and generation timestamp visible, compute tier from ancestry, never infer human scientific verification from maturity. Do not overwrite, promote or modify any map node or approval data.
4. **Include appropriate reader content and images**, resolving local/relative Markdown and SVG/raster assets safely; indicate unresolvable external/Library figure refs gracefully rather than substituting unrelated imagery or treating AI-generated illustrations as verified evidence.
5. **Support curation** (whole owner-selected map versus a selected reviewed/written subset). Important: `human_worked_out`, `informal_writing`, `formal_writing` are owner progress stages, **not** equivalent to verified scientific citations. Keep AI notes and evidence behind optional audit views, and prevent unintentional disclosure of private working material in a shareable export.
6. **Test with live-shaped data**, not just an eight-node fixture. Include deep parent chains and evolving fields, lossless adapter roundtrips, client-side browsing after server shutdown, readable documents, figures, and explicit validation of all files being packaged.
7. **Keep the app responsive** and profile excessive CPU/watch/re-render work independently; no ungrounded performance changes or new dev servers just for export.

## Ownership, integration and acceptance

- This task belongs to the **frontend worker**, on its own frontend branch/PR chain against `devcontainer`. **Not in scope for the science writer** or for immediate automatic execution.
- First review the current `mindmap/README.md`, `preview.py`, `owner_map.py`, `static/` and tests. Confirm whether PR #199 has merged, and integrate with the current frontend state rather than applying a stale branch-specific patch blindly.
- Read the latest science branch `docs/bep-theme-first-progress-units-20261022` **by explicit ref**. Its content changes concurrently. Treat `current_map.yaml` as the authoritative source for current owner topology/status and supporting docs as maintained relational/history artifacts.
- Run a genuine visual/browser test in addition to Python/JS unit tests, inspect the generated offline package, give a reviewable diff and instructions for exporting/opening the output.
- **Done when:** the owner can open the exported *real viewer* locally, navigate its graph and reader notes without needing the development server, inspect current progress/provenance, and choose what to share. No scientific status changes, website deployment, or message to Damian are part of this task.

**Urgency clarification:** A separate request to prepare/review material for Damian on 23 October was tracked on the science branch. This **future frontend feature** is a different task, and its existence neither means that the earlier prototype was final nor that a deadline was met or canceled.
