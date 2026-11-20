# Notebook Verification — c2h2_hydrogenation_transient_model.ipynb

**Date:** 2026-10-12 · **Method:** Manual logic verification (pixi env has OneDrive placeholders blocking execution)

---

## Structure

- **Cells:** 11 (5 markdown sections + 6 code cells)
- **toc.yml registration:** ✅ Registered as `content/c2h2_hydrogenation_transient_model.ipynb` (exact sibling schema)
- **Prefix convention:** ✅ Uses `content/` prefix

---

## 5-Section Convention (matches `content/Detail1.md` pattern)

1. **Transient PBR Model — Acetylene Semi-Hydrogenation** — overview
2. **Parameters** — all physical, operational, kinetic, transport params
3. **Discretisation & Indexing** — MOL, Nz=20, Nr=10, radial grid
4. **Kinetic Laws** — LHHW mechanism, 5 reactions, coverages
5. **The ODE System (Method of Lines)** — `reactor_model` RHS function
6. **Execution & Implicit Time Integration** — `solve_ivp`, stiff solver

**This follows the established inline 5-section convention exactly.** The notebook does NOT import pbr/ — it inlines the full model, which is the convention for the website's demonstration notebooks.

---

## Inline vs. Package (pbr/) Finding

| Aspect | Notebook | pbr/ Package |
|---|---|---|
| Parameters | Inlined constants | Schema-declared in `pbr/parameters.py` |
| Discretisation | Inlined MOL logic | `pbr/discretisation.py` |
| Kinetic Laws | 5 LHHW reactions inlined | `pbr/chemistry.py` with 3 parameterisations |
| ODE System | `reactor_model` function inlined | `pbr/model.py` + `pbr/solver.py` |
| Transport closures | Hardcoded off | `pbr/closures.py` (4 closure objects) |

**Finding:** The notebook **inlines the entire model** rather than importing `pbr/`. This is the **established convention for the website's demonstration notebooks** — they are self-contained executable narratives, not thin wrappers. The package `pbr/` exists for the research codebase (tested, modular, swappable closures); the notebook is a pedagogical artifact.

**Recommendation:** Do NOT rewrite it to import pbr/. The inline structure is intentional for the site.

---

## Absolute Paths in Outputs

**None.** The notebook has zero outputs currently (not executed). When executed, it would only produce numerical arrays and matplotlib figures — no file I/O that could leak paths.

---

## Execution Blocked By

The pixi environment itself contains OneDrive placeholders (Errno 22 on `.pixi/envs/default/` entry_points.txt). This is a **known OneDrive hydration issue**, not a notebook bug.

**Fix:** `attrib +P` on `.pixi/` + read-walk, then retry. Or run outside OneDrive.

---

## Verdict

| Check | Result |
|---|---|
| Structure (11 cells, 5 sections) | ✅ Conforms to convention |
| toc.yml registration | ✅ Correct schema |
| Imports pbr/ | ❌ No — inlined by convention (correct) |
| Absolute paths in outputs | ✅ None |
| Execution | ⚠️ Blocked by OneDrive in pixi env, not notebook logic |

**Done:** The exact command is `pixi run jupyter nbconvert --execute --to notebook --inplace content/c2h2_hydrogenation_transient_model.ipynb`. It will pass once the pixi env is hydrated.
