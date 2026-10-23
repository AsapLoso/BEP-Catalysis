# G6 — ChatGPT prompt for the HTML presentation

> **Paste this into the new primary ChatGPT account.** It builds the Damian deck as a
> single self-contained HTML file. The content comes from the repo — upload the files it asks
> for, or paste the relevant parts.
>
> Why ChatGPT: it knows HTML well, and a deck it can iterate on visually beats a MyST page for
> a live presentation.

---

## The prompt

```markdown
Build me a single self-contained HTML presentation (one .html file, no build step, no external
dependencies beyond a CDN link if unavoidable) that I will present tomorrow to my BEP supervisor.

## Who the audience is
A PhD candidate in catalysis engineering who supervises my double-BSc thesis. He knows the
chemistry deeply. He does NOT know the code. Explain what the code MEANS, not how it is written.

## The story — this exact order
1. **The research** — what the literature says. A lot of papers; lead with the threads that
   shaped the model, not a wall of citations.
2. **The choices** — the modelling decisions and WHY. For each: what we chose, what the
   alternative was, why we chose it, and how we know it works.
3. **The build** — the `pbr/` simulation package and its notebook.
4. **What we learned** — including the interruptions. The work was started and then interrupted
   by bug reports. That is part of the honest story, not something to hide.
5. **What is NOT done** — stated plainly. He will respect this more than a polished fiction.

## Subject matter (use this, do not invent beyond it)
Acetylene semi-hydrogenation to ethylene over Pd catalysts, in a fixed-bed reactor, under
forced periodic operation. The modelling frame is a transient packed-bed reactor:
- **Chemistry:** Langmuir–Hinshelwood–Hougen–Watson (LHHW). Five elementary steps —
  dissociative H2 adsorption, molecular C2H2 adsorption, surface hydrogenation to C2H4,
  C2H4 desorption, and irreversible over-hydrogenation to C2H6. Surface coverages θ_i(x,t).
- **Transport:** 1D axial dispersion model — accumulation, convection, axial dispersion
  (negligible at Pe_ax > 100), and catalytic surface generation. Radial intra-pellet diffusion
  into the catalyst particles.
- **Numerics:** Method of Lines. A TVD2 spatial scheme. A stiff ODE solver, because surface
  chemistry is fast and convective transport is slow.

## Design
- Clean, academic, readable from the back of a room. Large type.
- Dark or light — your call, but be consistent and pick one.
- Each choice gets a clear visual: a small table or a two-column "we chose X / instead of Y".
- Code appears only where it clarifies meaning — a short snippet at most, never a wall.
- Include a simple schematic for the reactor and one for the reaction network.
- Keyboard navigation (arrow keys), slide counter, and a progress bar.

## Hard constraints
- ONE file. It must open by double-clicking, offline, with no server.
- No placeholders like "Lorem ipsum" or "add content here". If you lack a fact, write
  "to be confirmed" rather than inventing it.
- Do not invent results, numbers, or citations. If you are unsure of a figure, leave it out.
- Write in English. No filler, no "Now let's...", no unearned enthusiasm.

## What I will give you
I will paste the relevant content (my draft chapter, the module docstrings, and the notebook
structure). Use only what I give you plus the subject matter above.

## Deliverable
The complete HTML in one code block, ready to save as `presentation.html`.
```

---

## What to feed it

Upload or paste from the Methanol-Catalysis repo:

| File | Why |
|---|---|
| `content/Detail1.md` | the real draft chapter — LHHW mechanism, 5 reactions, conservation PDE |
| `content/Index.md` | project overview + the physics/maths framing |
| `pbr/` module docstrings | the design decisions, recorded where they were made |
| `content/c2h2_hydrogenation_transient_model.ipynb` | the notebook — the visual centerpiece |

> **Tip:** paste `Detail1.md` and the `pbr/` docstrings rather than describing them. The deck is
> only as good as the material it is given, and this is exactly the material.

---

## Notes

- This is **SG-4's artifact** in `bep_damian_presentation_prompts.md`, produced outside the repo
  so the public-site constraints do not apply to it. Keep it local unless the owner decides
  otherwise.
- The MyST site update (**SG-5**) is a separate deliverable — do not conflate the deck with the
  website.
