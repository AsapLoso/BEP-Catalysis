# Veto Crosswalk — Seven Vetoes × Briefing Claims

**Companion to** [`afk_findings.md`](afk_findings.md). **Session:** CEO, autonomous overnight workstream, 2026-10-08.
**Map:** [`damian_briefing_2026_10_09.md`](../wayfinder/damian_briefing_2026_10_09.md), destination criterion 4 at
`:19` — *"No vetoed claim is spoken. Every one of the seven vetoes in `state.md:33-39` is checked against the script
before the meeting."*

**Line-number correction, applies to the whole table.** The map cites the vetoes at `state.md:33-39`. Read directly,
the seven bullets are at **`state.md:34-40`**; `:32` is the `## 🚫 Vetoes & Constraints` heading and `:33` is blank.
Verified by reading `state.md` lines 1-120. This table uses the corrected numbers.

**Legend.** **CLEAR** = the claim can be spoken aloud as written. **BLOCKED** = it must not be spoken. **BOUNDED** =
speakable only in the narrower form given.

---

## The seven vetoes as written

| # | Line | Veto, as recorded |
|---|---|---|
| V1 | `state.md:34` | Never name the six Larsen parameter values from `larsen…run2.md` / `_consensus.md` as a source — unverifiable from our text layer **and** missing `r_{1,max}` and `n_{inh}`. → `conventions.md` §12.2 |
| V2 | `state.md:35` | Do not call those parameters "gefabriceerd" either — verify Appendix F first. Without this a later session could reverse the retraction into a fabrication claim. → §12.2 |
| V3 | `state.md:36` | `Articles/analyses/bep_example_index.md` is a navigation aid, **not** a fact or parameter source — the catalyst series is reversed. → §12.6 |
| V4 | `state.md:37` | Never cite a "0 grep-hits" proof for an absence in an extraction file that does not contain the relevant pages — `pdf_full_extracted.txt` stops at p. 54. → §12.1 |
| V5 | `state.md:38` | Never cite `Ch4:59-60` ("changes over time") as dynamic motivation without the correction — it is author imprecision and means position along the bed. → §12.1 |
| V6 | `state.md:39` | "Julia/SciML" is an unsupported claim about **our own** solver, not about Larsen; also in `larsen*_run1.md:112`. → §12.6 |
| V7 | `state.md:40` | "Key Quotes" from the 2-pass analysis pipeline are not automatically valid — Larsen's text demonstrably appears in Wang / Zhang / Ball / Borodzinski files. **Extent not measured.** → §12.5 |

---

## V1 — the six Larsen parameter values

| Briefing claim | Verdict | Note |
|---|---|---|
| "Larsen's final model is Extended LHHW with an `r_{1,max}` cap and a fitted `n_{inh}` exponent on `r₂`." | **CLEAR** | Grounded. `literature_index.md:22` writes the equations at `:255`, `:257`, `:259`; two grounded KG edges carry quotes (`larsen2024:sec:6-2-3:para:1` → `r1-rate-cap` and → `inhibition-term`). Structure, not values. |
| "Those two terms are exactly what the six-value set is missing." | **CLEAR** | The claim is about a *gap*, not about a number. `conventions.md:202`; `larsenSemihydrogenationAcetyleneEthylene2024_taxonomy.md:14`. |
| *Any* of the six numeric values, by name or by value | **BLOCKED** | `state.md:34`. Do not speak, do not display. |
| "The six values were deliberately omitted from the thesis body text." | **CLEAR** | `literature_index.md:261` — Larsen's own stated reason. This is the safest way to make the point *without* the numbers. |

**Verification that no file leaks them.** One `Select-String` pass over all 8 files in `Articles/analyses/` for
`7.1852e-5|1.0492e-5|936.21|972.00|3.3319`: **zero hits in every file.** Limitation: that proves absence of those
strings, not of a paraphrase.

---

## V2 — no "gefabriceerd"

| Briefing claim | Verdict | Note |
|---|---|---|
| "The six values are not fabricated." | **BLOCKED — as a positive claim.** | `state.md:35`. `conventions.md:206` records the reason: a Jupyter execution counter is something you read off a screenshot, not something you invent, and the most likely explanation is that run2 read raster pages our extractor did not. That remains speculation. |
| "The six values are unverifiable from our text layer, and incomplete besides." | **CLEAR** | This is the `conventions.md:199-202` wording — "niet bewezen onjuist", plus two independent grounds. Says what is known without asserting fabrication. |
| "**Appendix E**, not Appendix F, is where they would be." | **CLEAR** | `Ch6_Results_and_Discussion.txt:436` verbatim: *"The parameters used in each variant can be found in Appendix tables E.1 to E.3."* |
| Any statement that the values *are* fabricated, or *aren't* | **BLOCKED both ways** | V2 bars the word; V1 bars the values. The only permitted move is the bounded form above. |

**V2 is mis-routed, and the briefing should say so.** V2 says "verify Appendix F first". Appendix F is pages 77–88
and holds `A`, `rho_support`, solver / grid / tolerance and DE-bounds (`conventions.md:214`, `state.md:56`) — it
cannot hold the six values, which `Ch6:436` and `literature_index.md:261` both place in Appendix E, pages 71–76.
**The minimum read that lifts V1 and V2 is pages 71–76.** See RS-3.

---

## V3 — `bep_example_index.md` is not a source

| Briefing claim | Verdict | Note |
|---|---|---|
| "The catalyst series is Pd₀Ag 0.025 / Pd₂Ag 0.05 / Pd₃Ag 0.1 wt% Pd, 5.0 wt% Ag each, Ag:Pd 200:1 / 100:1 / 50:1." | **CLEAR — from the right file** | `literature_index.md:239`, independently `conventions.md:192` (Table 4.1, `Ch4:17-21`). This is *precisely* the claim `bep_example_index.md` gets backwards (`conventions.md:231-232`), so the veto is what makes the correct version safe to say. |
| "Our reactor has a 1/4″ OD, 4 mm ID, 50 mg catalyst + 450 mg SiC." | **BLOCKED** | `conventions.md:234-235` — invented geometry and a SiC error, both in the vetoed file. The thesis gives no reactor diameter. |
| "We dried at 110 °C, calcined at 450 °C, reduced at 400 °C." | **BLOCKED** | `conventions.md:233` — fabricated process steps. The real ones: 12 h at 80 °C, pretreatment 250 °C (`Ch4:14-15, :28-32`). |
| "ΔH is −137 kJ/mol." | **BLOCKED** | `conventions.md:236`. The correct value is **−136** (`:193`, `Ch4:68-69`). |
| Referencing `bep_example_index.md` as anything but navigation | **BLOCKED** | `state.md:36`. The only hit for the filename inside `Articles/analyses/` is its own header at `bep_example_index.md:8`. |

---

## V4 — no "0 grep-hits" absence proofs

| Briefing claim | Verdict | Note |
|---|---|---|
| "Our extraction stops at page 54, so pages 71–88 have no text layer." | **CLEAR, and positively proved** | Verified, not asserted: `pdf_full_extracted.txt` runs `--- PAGE 1 ---` at line 1 to `--- PAGE 54 ---` at line 1760, which is its last page marker, and the file ends on the bibliography. 1 814 lines, 135 421 bytes. This is an affirmative statement about where the text layer stops — not a grep-hit count. |
| "I searched and found nothing, therefore Appendix E is empty / the parameters do not exist." | **BLOCKED** | Exactly the barred inference. `state.md:37`; `conventions.md:201`. |
| "Larsen's model has no time derivative in the species balances." | **BLOCKED as proved by absence** | `conventions.md:188` bars a zero-hit proof for this specific claim. It must be argued **positively**, from Eqs. 4.6–4.9 (`Ch4_Materials_and_Methods.txt:64-80`) plus the 7-minute stabilisation protocol (`Ch4:34-36`). |
| The RM-SE triple 5.10 / 5.43 / 7.14 % | **CLEAR** | `literature_index.md:263-265`; `conventions.md:191` confirms these exist and are correct at `Ch6:678`, `Ch7:35`, `Ch1:21`. |

**A second V4 trap found during RS-3, same shape.** `Articles/2 meeting Damian + Zoë/` contains **two** copies of
the thesis: `BEP Example.pdf` (9 167 352 bytes) and `BEP Example (no appendix).pdf` (5 519 129 bytes). Opening the
second and finding no Appendix E yields the identical wrong conclusion — "the appendices are not there". The
appendices exist; only our text layer stops at p. 54. Both files verified on disk.

---

## V5 — `Ch4:59-60` is not dynamic motivation

| Briefing claim | Verdict | Note |
|---|---|---|
| Quoting `Ch4:59-60` ("composition of the flow changes over time") as motivation for transient modelling | **BLOCKED unless the correction travels with it** | `state.md:38`; `conventions.md:189`. It is author imprecision and means position along the bed. |
| "Larsen's system is steady-state in `z` only, with no time derivative." | **CLEAR — positive proof** | `conventions.md:186-188`: Eqs. 4.6–4.9 verbatim at `Ch4_Materials_and_Methods.txt:64-80`, plus every GC measurement being a steady state after 7 min stabilisation (`Ch4:34-36`). Note `conventions.md:188` also records that `Ch3:58` discusses time-dependent deactivation that is never modelled — so the honest sentence carries that limit. |
| `Ch4:59-60` cited at all | **BOUNDED** | Speakable **only** as *"author imprecision; it means position along the bed"* in the same breath. The map's own SP-1/§2 do not need it. |

---

## V6 — "Julia/SciML"

| Briefing claim | Verdict | Note |
|---|---|---|
| Any statement that we use Julia, SciML, or any non-Python stack | **BLOCKED** | `state.md:39`. Unsupported about our own solver. Our stack is Python / SciPy `solve_ivp` (`conventions.md:237`; the script uses `solve_ivp` throughout). |
| "Our solver is Python with `scipy.integrate.solve_ivp`, 1480 ODEs, implicit BDF." | **CLEAR** | `3_Model/state.md:49-51`; script `:238-239`. The *opposite* of the vetoed claim, so speaking it discharges V6. |
| Any statement that Larsen used Julia/SciML | **BLOCKED** | `state.md:39` names `larsen*_run1.md:112` as a second occurrence of the same unsupported claim. |

**Verification.** One `Select-String` for `Julia|SciML` over all 8 files in `Articles/analyses/`: exactly two hits,
`bep_example_index.md:19` and `:138` — precisely the pair `conventions.md:237` names. The veto is corroborated to
the line, and both occurrences are inside the already-vetoed V3 file.

---

## V7 — 2-pass "Key Quotes" are not automatically valid

| Briefing claim | Verdict | Note |
|---|---|---|
| Quoting anything labelled "Key Quote" from the 2-pass pipeline | **BLOCKED** | `state.md:40`; `conventions.md:216-225`. |
| "The knowledge-graph quotes come from a separate route with a validator that substring-checks each quote." | **CLEAR** | `conventions.md:152-154`. The KG is `kg_chunk.py` → in-session SOP → `kg_validate.py`, **not** the 2-pass pipeline. I verified all 23 grounded quotes are ordinal substrings of their chunk text: 23 of 23 match. |
| "Our quotes are clean." | **BLOCKED** | `conventions.md:225`: the contamination extent over the ~141 pipeline runs is `⚠️ Omvang niet gemeten`. Never measured means never clean. |
| The RMSE triple 5.10 / 5.43 / 7.14 | **BOUNDED** | Speakable **only** attributed to Larsen's Section 6.2.4 p. 43 (`literature_index.md:262-265`) and **never** sourced from the pipeline files where the fragments were cross-contaminated (`conventions.md:220-221`). |
| The bridge edges linking Larsen's `r_{1,max}` to Berger's transport criteria | **BLOCKED as a claim** | `conventions.md:161`; both are `llm_inferred` `SEMANTIC_LINKS` in `bridge_*.json`, confidences 0.85 and 0.80, never a `\cite{}` basis. What *may* be said: that the two papers were compared on those criteria — as our comparison, not as a citation. |

**Verification.** One `Select-String` for `Key Quotes` over all 8 files in `Articles/analyses/`: **zero hits.** Again:
that proves the phrase is absent, not that no pipeline quote was reused.

---

## Summary

| Veto | Clear claims | Blocked | Bounded |
|---|---|---|---|
| V1 | 3 | 1 | — |
| V2 | 3 | 2 | — |
| V3 | 1 | 4 | — |
| V4 | 3 | 2 | — |
| V5 | 1 | 1 | 1 |
| V6 | 1 | 2 | — |
| V7 | 1 | 2 | 1 |

**Nothing in the KG's 23 grounded edges trips any of the seven vetoes.** The KG is the safest speakable material in
the project, and it is the only major research artefact that is — its risk is not contamination but fidelity
(3 of 23 quotes carry pypdf mojibake, in names rather than numbers; see RS-2).

**The one claim that carries the most risk and is worth pre-rehearsing is the Carberry threshold.** Berger's is
`< 0.05`; `Articles/analyses/literature_analysis.md:40` gives `Ca ≤ 0.15` for a *different, methanol* paper;
`3_Model/state.md:66` fixes Berger's Wheeler–Weisz at `< 0.1`, not `< 0.05`. Three numbers in three files, one
project, one topic. `transient_model_framework_audit.md:44` says it outright: *"Thresholds are paper-specific. Do not
average them, do not cite them for Berger."* Answer with Berger's `0.05`, attribute it to Berger, and never mention
the other two.