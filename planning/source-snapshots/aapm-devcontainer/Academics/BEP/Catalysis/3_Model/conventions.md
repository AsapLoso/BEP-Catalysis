# 3_Model — Transient PBR Modelling Submap

Parent project: [BEP Catalysis (Urakawa Group)](../state.md) · Parent conventions: [`../conventions.md`](../conventions.md)

## Purpose

This submap holds the **executable** side of the Catalysis BEP: the 1D-axial + 1D-intra-particle
transient packed-bed-reactor (PBR) model for acetylene semi-hydrogenation
($C_2H_2 \rightarrow C_2H_4 \rightarrow C_2H_6$), discretised by Method of Lines and integrated
with an implicit stiff solver.

Theory and derivations stay in [`../1_Transport_Phenomena/pbr_transport_phenomena.md`](../1_Transport_Phenomena/pbr_transport_phenomena.md).
This directory only holds code, its audit record, and the transcripts that produced it.

## Files

| File | Role |
|---|---|
| `c2h2_hydrogenation_transient_model.py` | The MOL reactor model. Currently a **scaffold with verified defects** — see [`state.md`](state.md). |
| `transient_model_framework_audit.md` | **Read first.** The 30-message sister chat audited against Berger (2008): 8 *framework* defects + an UNVERIFIED-cite list. |
| `gemini_transcript_2026-09-29.md` | Gemini chat `7378843f85f483d1` (7 msgs) that generated the scaffold. Voice-dictated NL, Dutch. |
| `gemini_transcript_2026-09-29_83878835991845b5.md` | Sister chat `83878835991845b5` (30 msgs): Berger §5 transport criteria + the full Canvas "Transient Reactor Model Structure". |
| `probes/audit_2026_09_30.py` | Re-derives **every** measured number in the register. `pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py` |
| `conventions.md` | This file. |
| `state.md` | Active open loops + the code-execution defect register. |
| `resources.md` | Reference links for kinetics constants and numerical methods. |
| `history.log` | Append-only log of every change to the model, including retractions. |

## Working rules

1. **Never commit an unverified number as a physical parameter.** `ModelParams.kinetics` ships as
   all-zero tuples *on purpose*. Filling them is the whole point of the exercise, and each value
   must be traceable to a `resources.md` row with a `file:line` or a page citation (Rule 16).
2. **A defect fix needs a probe, not a read.** The register in `state.md` was produced by executing
   the rhs against analytic solutions (`f = r^2`, `f = r^4`) and by A/B-running the model against a
   non-mutating wrapper. New claims follow the same route. **The probe script is part of the
   deliverable** — keep it under `probes/`, never in gitignored `scratch/`. Writing the probe out
   is what caught the D4 and D6 measurement errors on 30-09; a number that only exists in a chat
   transcript cannot be re-checked when the claim is corrected.
3. **Never divide wall-clock by `nfev`.** `BDF`'s finite-difference Jacobian costs `DIM` rhs calls
   per Jacobian and is *not* counted in `nfev`, so `wall/nfev` silently attributes the dominant cost
   to the wrong thing. Report `nfev`, `njev`, and the raw rhs cost separately (D6). Wall-clock on
   this machine is load-dependent — parallel sessions move it by 5×, so the durable claim is the
   *structure* of the cost, not the seconds.
4. **Record the wall-clock cost of every run.** The model is slow enough ([`state.md`](state.md) D6)
   that a naive grid sweep will not finish.
5. **Keep transcripts out of `state.md`** (Rule 9). The Gemini chat lives here, linked.
6. **The model is a candidate method, not a commitment** (parent `conventions.md` § 5) — *with one
   documented exception.* Parent § 11 (added 30-09 by the parallel session) states *"Dit zijn
   besluiten, geen kandidaten"* and its item 7 covers exactly these numerics. That **contradicts**
   this file. The resolution taken here: the **scheme choice** (upwind bulk / central particle /
   BDF time) is now a *decision* per parent § 11, while the **model reductions** it rests on —
   plug flow without dispersion, pseudo-homogeneous `C_s = C_b`, no energy balance, no readsorption
   — remain **candidates and open scope decisions** (framework audit §3.4, §3.6, §3.3; register
   bullet "Reconcile with the `1_Transport_Phenomena` reference"). Do not read the § 11 decision as
   having settled the reductions. **This conflict is unresolved and belongs to the user.**
