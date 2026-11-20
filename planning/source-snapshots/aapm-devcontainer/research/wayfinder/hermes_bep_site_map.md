# Hermes Map — BEP site + presentation (self-directed, tonight)

> **Charted:** 2026-10-12 · **Mode:** executing directly (not delegating this one)
> **Working dir:** `%USERPROFILE%\OneDrive - Delft University of Technology\Misc\Gemini\Methanol-Catalysis`
> **Constraint:** repo is PUBLIC, Pages live off `main`. User has cleared names + paths. Only real secrets are off-limits — and there are none (verified).

## Destination (verifiable end states)

| # | End state | Checkable |
|---|---|---|
| D1 | The site builds and serves locally without error | `pixi run preview` starts; localhost responds 200 |
| D2 | No starterkit template text survives in `content/` | grep for template strings returns 0 |
| D3 | `toc.yml` references resolve — no missing files | every `file:` entry exists on disk |
| D4 | `Theory.md` + `Methods.md` state the real physics and numerics | they cite `Detail1.md` content + `pbr/` modules |
| D5 | The presentation artifact for Damian exists and builds | a MyST page/deck that compiles |
| D6 | Nothing is left dehydrated for the next session | hydration walk returns `failed: 0` |

## Frontier

### Island: Unblock (done)

- [x] **U1 Diagnose the read failures** (`task`) — root cause: OneDrive Files On-Demand, not ACLs.
- [x] **U2 Hydrate the repo** (`task`) — `attrib +P` + read walk; 52/52 in content/pbr/scripts/tests.
- [x] **U3 Fix `export typst.yml`** (`task`) — placeholder resisted pinning; replaced from the git object store.
- [ ] **U4 Confirm the site serves** (`task`) — *in progress: `pixi run preview` launched, verifying.*

### Island: Truth pass

- [ ] **T1 Replace the starterkit template text** (`task`) — `Theory.md`, `Methods.md`, `Conclusion.md` are all raw starterkit (`E=mc²`, the Schrödinger equation, "Jupyter Book is feasible"). Rewrite from `Detail1.md` + `pbr/`.
- [ ] **T2 Fix the broken toc entries** (`task`) — `Detail3.md` is referenced but missing (fails the build); `Detail2.md` is 0 bytes; `Leken.md` is 20 bytes.
- [ ] **T3 Sweep for template residue** (`task`) — grep for starterkit strings; D2 is the gate.

### Island: Substance

- [ ] **S1 Write `Theory.md`** (`task`) — the real physics: LHHW mechanism (5 reactions, from `Detail1.md`), conservation PDE, Danckwerts BCs, dimensionless groups.
- [ ] **S2 Write `Methods.md`** (`task`) — the real numerics: MOL, TVD2 scheme, radial diffusion, stiff solver choice. Source: `pbr/` docstrings + `test_discretisation.py`.
- [ ] **S3 Rewrite `Conclusion.md`** (`task`) — honest: what we learned, what is not done.
- [ ] **S4 Fill `Detail2.md` / `Detail3.md` / `Leken.md`** (`task`) — or drop them from `toc.yml` if they have no content. Do not ship empty pages.

### Island: Presentation

- [ ] **P1 Build the Damian artifact** (`task`) — research → choices → build → what we learned. MyST page or deck; state the choice.
- [ ] **P2 Verify it builds** (`task`) — `pixi run preview` / `pdf`; report real output.

### Island: Hygiene

- [ ] **H1 Stop OneDrive when done** (`task`) — standing rule; confirm files stay readable after.
- [ ] **H2 Commit scoped** (`task`) — `git commit --only <paths>`; never `git add -A`.
- [ ] **H3 Leave the HITL items** (`grilling`) — emphasis, candour depth, inline-vs-import `pbr/`, page-vs-deck, what gets published. **Owner's, tomorrow.**

## Fog

- [Fog] Whether the site should stay a thesis book or become a presentation site — the two audiences differ and the toc is currently thesis-shaped.
- [Fog] Whether `Detail*.md` / `Leken.md` are meant to exist at all, or are abandoned scaffolding.
- [Fog] How much of `pbr/` the site should expose vs summarise.

## Execution contract

- verify_cmd: `pixi run myst --version && curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/`
- scoped_commit: `content/`, `toc.yml` only unless a decision says otherwise.
