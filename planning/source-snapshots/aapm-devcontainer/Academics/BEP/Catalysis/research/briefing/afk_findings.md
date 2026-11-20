# AFK Findings — Damian Briefing Map

**Session:** CEO, autonomous overnight workstream, 2026-10-08.
**Map:** [`damian_briefing_2026_10_09.md`](../wayfinder/damian_briefing_2026_10_09.md).
**Scope executed:** six AFK tickets (RS-1, RS-2, RS-3, SP-3, DR-3, AR-3), in that order.
**Isolation:** no write to any `state.md`, `history.log`, `conventions.md` or `task.md`; no mutating git command
(`.agents/skills/wayfinder/SKILL.md:151`). Every claim below carries `file:line`. Absence claims name what was read
to prove the absence.

**Reading conventions used throughout:** PowerShell `(Get-Culture).Name` returns `nl-NL`, so `LastWriteTime` renders
`d-M-yyyy`. `7-10-2026` is 7 October 2026; `10-8-2026` is 10 August 2026. This matters for RS-1.

**Citation correction, applies to all six tickets.** The map cites the vetoes at `state.md:33-39` and the KG at
`state.md:103`. Both are off by one. Read directly, the seven veto bullets are `state.md:34-40` (`:32` is the
`## 🚫 Vetoes & Constraints` heading, `:33` is blank), and the "40 nodes / 30 edges" claim is on the
Knowledge-Graph Piloot bullet at `state.md:104` (`:103` is the dashboard bullet). Verified by reading `state.md`
lines 1-120 in full. This session uses the corrected line numbers throughout and flags every place the map's number
would mislead a later reader.

---

## RS-1 — Was the finding-taxonomy extraction run ever completed?

**Ticket type:** `wayfinder:research`.

### Question, verbatim from the map

> `finding_taxonomy.md` describes the extraction procedure in future tense and lists "known starting members", while
> four `*_taxonomy.md` files were written 2026-10-08 05:54–08:14. Which taxonomy files exist, which documents are
> classified, and what is the next unclassified member?

(`damian_briefing_2026_10_09.md:93`)

### Answer

**Started, not completed. Four of 36 documents classified (11%). The four classified are exactly the four seed
members in §6, so the run stopped at the end of its seed set and never left it.**

| Fact | Value | Evidence |
|---|---|---|
| Taxonomy files in existence | **5 total**: 1 procedure + 4 per-paper reports | procedure: `Articles/analyses/finding_taxonomy.md`; reports: `Articles/paper_analyses/{bergerDynamicMethodsCatalytic2008, larsenSemihydrogenationAcetyleneEthylene2024, ref_28_Battezzati2016, silvestonPeriodicOperationCatalyticReactors1995}_taxonomy.md` |
| Documents in scope | **36** | `Articles/analyses/finding_taxonomy.md:4`; counted: 36 files matching `*_consensus.md` under `Articles/paper_analyses/` |
| Documents classified | **4 of 36** | the four `*_taxonomy.md` files above |
| Documents unclassified | **32** | 36 minus 4; enumerated below |
| Header status line | **stale** — still reads "extraction **not started** (2026-10-06)" | `Articles/analyses/finding_taxonomy.md:3` |
| Next unclassified member | **Borodzinski & Bond (2006)** — under the only recorded ordering (below) | `Articles/analyses/literature_categorization_and_action_plan.md:129-135` |

**Four corrections to the map's premises.** The map states these as facts; each is wrong, and each matters because
the briefing would inherit the error.

1. **The four reports are not siblings of `finding_taxonomy.md`.** The map says "four sibling `*_taxonomy.md`
   files" (`damian_briefing_2026_10_09.md:95`). `Articles/analyses/` holds 8 files and exactly **one**
   `*_taxonomy.md`, which is the procedure itself. The four reports live in a different directory,
   `Articles/paper_analyses/`. Verified by reading the `Articles/analyses` directory listing in full and by a
   recursive `Get-ChildItem -Filter "*taxonomy*"` over `Articles/`.
2. **The date range is wrong.** The map says 2026-10-08 05:54–08:14. All five taxonomy files have
   `LastWriteTime` on **7 October 2026**, 08:00 (`finding_taxonomy.md`) through 08:14 (the four reports). The
   `05:54` in the map belongs to a different batch: `zengPhaseDiagramsGuide2022_run1.md` and
   `caoSyntheticStrategiesSupported2023_run1.md` at 10 August 2026 05:54–05:56. The map conflated two runs.
3. **Git cannot corroborate any of it.** `git log` for all five taxonomy files returns empty, because
   `.gitignore:85` (`**/Articles/`) ignores them; `git check-ignore -v` confirms the rule and the path. So the
   filesystem timestamp is the only dating evidence available, and it is not reproducible from the audit trail.
   28 files under `Articles/` are tracked (grandfathered, including 7 under `Articles/graph/`).
4. **`finding_taxonomy.md:202` points at a file that does not exist.** §6 lists Battezzati as
   `paper_analyses/battezzatiPolymerizationC2H4PdCatalysts2016_consensus.md`. The file on disk is
   `ref_28_Battezzati2016_consensus.md` (confirmed by reading the full `Articles/paper_analyses` listing). The
   per-paper report cites the correct path (`ref_28_Battezzati2016_taxonomy.md:39`), so the run repaired the
   pointer in practice while `finding_taxonomy.md` still carries the broken one.

### The next unclassified member

`finding_taxonomy.md` §5 (`:174-188`) specifies "for each of the 36 `_consensus.md` files, in isolation" and
**names no ordering**. So there is no canonical binning order in the procedure. The only recorded processing order
anywhere in the project is the triage list, which `finding_taxonomy.md:11-19` explicitly keeps and designates as the
thing that "decides what gets read". Its conclusion at
`Articles/analyses/literature_categorization_and_action_plan.md:129-135` names five articles requiring targeted
analysis. Against that list:

| Priority-list article | Classified? | Taxonomy report |
|---|---|---|
| Berger (2008) | yes | `bergerDynamicMethodsCatalytic2008_taxonomy.md` |
| Larsen (2024) | yes | `larsenSemihydrogenationAcetyleneEthylene2024_taxonomy.md` |
| **Borodzinski & Bond (2006)** | **no** | — |
| Danckwerts (1953) | no | — |
| Silveston (1995) | yes | `silvestonPeriodicOperationCatalyticReactors1995_taxonomy.md` |
| Urakawa (2008) | no | — |

**Next member = `borodzinskiSelectiveHydrogenationEthyne2006_consensus.md`.** Not
`borodzinskiKineticModelHydrogenation2000_consensus.md`: that 2000 paper is already in Categorie 1 as verified
(`literature_categorization_and_action_plan.md:38`) and is a different document.

### Completeness of the four that were done

None of the four is complete against `finding_taxonomy.md`'s own schema. Two distinct defects:

- **Three of four use the wrong axis vocabulary.** The procedure defines **seven axes** (§3, `:36-152`) and
  requires each finding to be binned into them (`:183`). `bergerDynamic…:11-28`,
  `larsenSemihydrogenation…:5` and `silveston…:17-23,45-48` instead bin against **master-map ticket IDs**
  (`I1-01` … `I1-07`). The mapping is indirect but recoverable — Axis 4→I1-03 (`:91`), Axis 5→I1-04 (`:108`),
  Axis 6→I1-05/I1-06 (`:123`), Axis 1→I1-01 (`:39`), Axis 2→I1-02 (`:58`), Axis 7→I1-07 (`:140`), Axis 3→TU Delft
  benchmark track (`:74`) — so it is a naming inconsistency, not a lost classification.
- **Per-bin `file:line` traceability is missing in three of four.** Rule 4 (`:167-168`) requires every bin to
  cite `file:line` into the `_consensus.md` it came from. Counted by reading each report in full:
  `ref_28_Battezzati2016_taxonomy.md` complies, with six (`ref_28_Battezzati2016_taxonomy.md:15,21,31,32,33`).
  `bergerDynamicMethodsCatalytic2008_taxonomy.md` carries **one**, and it points into the analysis file, not the
  consensus file (`bergerDynamicMethodsCatalytic2008_taxonomy.md:14` →
  `Articles/analyses/dynamic_kinetics_berger2008.md:30`).
  `larsenSemihydrogenationAcetyleneEthylene2024_taxonomy.md` uses chapter-relative anchors (`Ch4:17-21`, `Ch6:665-677`),
  which are not `file:line` into any workspace file.
  `silvestonPeriodicOperationCatalyticReactors1995_taxonomy.md` carries **zero** line-level citations; line 4 names
  the consensus file path and no further anchoring follows.

### A substantive finding, not a bookkeeping one

**One of the four seed members was mis-binned at seed time.** `finding_taxonomy.md:202` lists Battezzati et al.
(2016) under "Likely axes: **1**" (parameter provenance and admissibility). The per-paper report establishes the
opposite: `ref_28` is a book review of a solid-state-crystallography monograph with "**no chemical reaction
kinetics, no catalytic data, no rate constants, no adsorption coefficients, and no activation energies**"
(`ref_28_Battezzati2016_taxonomy.md:15`) and is therefore inadmissible as a kinetic basis
(`ref_28_Battezzati2016_taxonomy.md:20`). The triage list had already said this reference needs no extraction at all —
`Rogl - 2018` is Categorie 2, "⚪ **Geen extractie**; naslagwerk"
(`literature_categorization_and_action_plan.md:65`).

So the seed set §6 calls complete is not merely unfinished, it is **wrong on one of four members**, and the wrong
member is the one that turned out not to be a chemistry paper. A `BACKGROUND` verdict on ref_28 is correct; the
Axis 1 prediction in `finding_taxonomy.md:202` is not, and it is still on disk.

### UNVERIFIED

| Item | Status | What would resolve it |
|---|---|---|
| Whether the run was *interrupted* or simply *stopped after the seed set* | `UNVERIFIED`. The four reports carry no run-log, no manifest, and no progress marker; `finding_taxonomy.md` has no "extraction in progress" flag to contradict. | A run log, or the session transcript. Rule 35: recoverable from `%USERPROFILE%\.local\share\opencode\opencode.db` (read-only) for OpenCode sessions, or `%USERPROFILE%/.gemini/antigravity/` for Antigravity sessions. |
| Whether the four reports are accepted or provisional | `UNVERIFIED`. No file records a review verdict on them. | The supervisor's reading, or a re-run of §5 procedure over all 36. |
| Whether "next" means Borodzinski 2006 under some other ordering | `UNVERIFIED` and undecidable from disk: §5 names no order, and no other file assigns one. Only the triage list does. | A stated binning order, or the supervisor naming the order. |
| Whether §6's "Larsen (2024) — index entry with the eight fitted values" (`:200`) is a real extracted source | `UNVERIFIED`. The pointer names no file. `larsenSemihydrogenationAcetyleneEthylene2024_taxonomy.md:14` reports six of the eight are present and `r_{1,\max}` and `n_{\text{inh}}` are absent. | Reading the index entry it refers to. Bears directly on RS-3. |

> **Resolved during RS-3.** The index entry is `Articles/analyses/literature_index.md:229-266`, and it contains
> **no fitted values at all** — it says so at `:261`. See the RS-3 section; RS-1's UNVERIFIED row is closed there.

### Correction to RS-1, found while working RS-3

Recorded as an addendum rather than an edit to the finding above, per the correction protocol.

**`ref_28_Battezzati2016_taxonomy.md:6` states the wrong year for the book review.** It reads "**Year:** 2016
(Monograph) / **2018** (Book Review, online 2017)". Larsen's own bibliography, at the final entry of
`Articles/2 meeting Damian + Zoë/extracted/pdf_full_extracted.txt` (reference [28], the last lines of the file,
which runs to line 1814), reads: *"Livio Battezzati. Intermetallics. Structures, Properties, and Statistics. By
Walter Steurer and Julia Dshemuchadse. Oxford University Press, 2016, Hardcover, Pp. 592 … In: Acta
Crystallographica Section B Structural Science, Crystal Engineering and Materials **73.6 (Dec. 2017)**, pp.
1194–1195."* The review is 2017, not 2018. The monograph year 2016 is correct.

This is small, and it does not change the verdict — `ref_28` is still a book review of a crystallography monograph
with no kinetics (`ref_28_Battezzati2016_taxonomy.md:15`), still inadmissible as a kinetic basis (`:20`), and the
bibliography entry independently corroborates the authorship split the report relies on (`:5`). But it is the second
date slip in a project document written days before the briefing, and the briefing's whole claim is that provenance
was checked. Worth fixing before it is shown.

---

## RS-2 — What is presentable from the knowledge graph under the vetoes?

**Ticket type:** `wayfinder:research`.

### Question, verbatim from the map

> given the seven vetoes in `state.md:33-39` — and specifically the veto barring 2-pass pipeline "Key Quotes" as
> automatically valid — which of the KG's 40 nodes and 30 edges, and which of the 8 files in `Articles/analyses/`,
> can Lucas say out loud to Damian without tripping a veto?

(`damian_briefing_2026_10_09.md:98`; vetoes at `state.md:34-40`, see the citation correction above)

### The decisive structural fact

The merged KG separates cleanly into **two provenance classes, and the split is exact**:

| Class | Count | Rule | Consequence |
|---|---|---|---|
| `MENTIONS` edges with `provenance.kind = grounded` | **23 of 30** | `conventions.md:159` — quote is a literal substring of the source, auto-verified by the validator; **citable** | speakable |
| everything else | **7 of 30** | `conventions.md:160` — `llm_inferred` carries `confidence` + `rationale` and is **never** a `\cite{}` basis | never speakable as a claim |
| — 2 × `SEMANTIC_LINKS` | | the cross-doc bridge edges from `bridge_larsen_berger_run1.json` | `conventions.md:161`, never citable |
| — 3 × `USES` | | `lhhw-kinetics` → `r1-rate-cap`, `lhhw-kinetics` → `inhibition-term`, `packed-bed-reactor-model` → `larsen2024:sec:4-3:para:1` | `llm_inferred`, confidences 0.95 / 0.95 / 0.7 |
| — 1 × `PART_OF` | | `stimulus-response-technique` → `transient-kinetics` | `llm_inferred`, conf. 0.97 |
| — 1 × `SAME_AS` | | `pssa` → `pssa` | a **self-loop**, rationale literally `"aliases.yml determinism"`, conf. 1.0. No semantic content; it is 1 of the 30 edges by construction, not by finding. |

Verified by dumping all 30 edges with their `provenance` blocks from
`Articles/graph/knowledge_graph.json` and cross-checking against `stats` in the same file
(`grounded_edges: 23`, `llm_inferred_edges: 7`). The counts agree exactly, and the 23 grounded edges are precisely
the 23 `MENTIONS`.

**So the answer is a clean rule, not a list: speak any `MENTIONS` edge and nothing else.** All 23 grounded edges
carry a `quote` and a `source_file`. The 7 `llm_inferred` edges carry a `confidence` and a `rationale` and no
quote at all — `conventions.md:160` states the reason: they are reasoned, not read.

### Which specific claims are speakable

Ranked by how much they carry, all grounded, all quoted:

1. **Berger's Section 5 transport-criteria argument** — `berger2008:sec:5:para:1` → `transport-criterion`, quote
   *"In order to ascertain that the obtained data represents the intrinsic kinetic information, it should be free
   from deviations due to nonideal reactor behavior and interference by transport phenomena"*. This is the single
   best-grounded sentence in the graph and it is thematically the model thesis: a transient PBR is only measuring
   kinetics if transport is not confounding it.
2. **Berger's plug-flow PDE statement** — `berger2008:sec:4:para:1` → `packed-bed-reactor-model`, quote *"For the
   plug-flow reactor a set of coupled partial differential equations (PDEs) is obtained"*. Directly supports
   destination criterion 1, and it is the basis on which our code is defensibly a Berger framework at all.
3. **The PSSA reduction** — `berger2008:sec:4:para:1` → `pssa`, quote *"the ODEs for the surface intermediates can
   be replaced by a set of algebraic equations"*. Compare `state.md:53` PRIO-1, which still lists the PSSA
   sensitivity comparison as an open action.
4. **The three stimulus families** — `step-response-experiment`, `pulse-response-experiment`,
   `multisine-stimulus`, three grounded quotes from `berger2008:sec:2-1:para:1`. The multisine one is the bridge to
   the SysCon collaboration and is grounded in Berger's own wording, not borrowed from Dylan Kalisvaart's framing.
5. **SSITKA** — `berger2008:sec:2-3:para:1` → `ssitka`, quote naming the technique in full.
6. **The two Larsen structural facts that the vetoes leave untouched** — `larsen2024:sec:6-2-3:para:1` →
   `r1-rate-cap` (*"limits the reaction rate through a"*) and → `inhibition-term` (*"the second hydrogenation step
   included a flexible inhibition term"*). **This is the RS-2 headline: the two terms the six-value set is missing
   are grounded and citable as structure; only their numeric values are blocked.**
7. **Larsen's own reactor statement** — `larsen2024:sec:4-3:para:1` → `packed-bed-reactor-model`, quote *"The packed
   bed reactor is the reactor used throughout the regular experiments"*.
8. **The fitting method** — `larsen2024:sec:4-3:para:2` → `differential-evolution-fit`, quote naming differential
   evolution. Consistent with `conventions.md:190` (`Ch4:117-127`).

### Three defects in the KG that the briefing must not inherit

**1. `grounded` certifies fidelity to *our text layer*, not to the PDF.** `conventions.md:159` describes grounded
as "letterlijke substring van brondocument (auto-geverifieerd door validator)", but the validator substring-checks
against `Articles/graph/chunks/<doc>.chunks.json`, which is itself a lossy `pypdf` extraction
(`conventions.md:152`). I tested all 23 grounded quotes as ordinal substrings of their chunk text: **23 of 23
match.** So the quotes really are verbatim *of the chunk*. The problem is what is in the chunk. **3 of 23 carry
mojibake** from the PDF text layer:

| Node | Corruption | Should read |
|---|---|---|
| `packed-bed-reactor-model` | `plug-ï‚,ow` (U+00EF U+00AC U+201A) | `plug-flow` |
| `wheeler-weisz-parameter` | `Wheelerâ€œWeisz` (U+00E2 U+20AC U+201C) | `Wheeler–Weisz` |
| `dewar-chatt-duncanson-model` | `Dewarâ€œChattâ€œDuncanson` | `Dewar–Chatt–Duncanson` |

Codepoints read directly off the string with `[int[]][char[]]`, not inferred from the console rendering. All three
are compound proper nouns or one hyphenated word; **no number is affected**, so destination criterion 1 is not at
risk. The claim is narrow and should be stated narrowly: the damage is in names, not in quantities.

**2. Node descriptions carry no provenance field at all.** A node in `knowledge_graph.json` has exactly four keys
— `id`, `type`, `docs`, `descriptions`. There is no `grounded` / `llm_inferred` marker on a description. So a
number that appears only in a description is **unclassifiable** from the merged graph alone. The live instance is
`carberry-number`, whose description reads `Ca = r_obs / (k_g a0 cb) < 0.05`. Under `conventions.md:160` a value
whose provenance is unrecorded cannot be asserted. Call it `UNVERIFIED` in the briefing, or pin it to
`dynamic_kinetics_berger2008.md` directly.

**3. That same `0.05` collides with a number from another paper.** `Articles/analyses/literature_analysis.md:40`
gives **Carberry `Ca ≤ 0.15`** and `:41` gives **Weisz–Prater `Da_II ≤ 0.3`**, for a *methanol-synthesis* paper.
`state.md:66` (FW-5) already warns about exactly this class of error — *"horen bij een **ander** paper (methanol) —
niet middelen, niet voor Berger citeren"* — and fixes the Berger Wheeler–Weisz threshold at `< 0.1`, not `< 0.05`.
So the project holds two different Carberry thresholds in two files. Damian asking "what's your Carberry number?"
is the most likely place this bites. The spoken answer must be Berger's `0.05`, attributed to Berger, with the
methanol `0.15` never mentioned.

### Which of the 8 files in `Articles/analyses/` are speakable

| File | Bytes | Veto status | Speakable? |
|---|---|---|---|
| `bep_example_index.md` | 24 091 | **VETOED as a source** — `state.md:36`, `conventions.md:227-237` | **No.** Navigation aid only. Its known errors are enumerated at `conventions.md:231-237`. |
| `dynamic_kinetics_berger2008.md` | 7 512 | clean on all seven | Yes — the most substantive analysis, and the source of FW-1/FW-2 |
| `finding_taxonomy.md` | 10 322 | clean on all seven | Yes, as **method**. Its own Axis 1 entry (`:200`) is wrong — see RS-3. |
| `literature_analysis.md` | 9 536 | clean, but **carries the methanol `Ca ≤ 0.15` trap** | Only with `:40-41` explicitly excluded for Berger |
| `literature_categorization_and_action_plan.md` | 12 047 | clean | Yes, as the processing-order authority (used for RS-1) |
| `literature_index.md` | 24 874 | clean | Yes, and it is the **strongest** Larsen source — see RS-3 |
| `literature_notes.md` | 5 611 | clean | Yes |
| `literature_analysis_tracker.md` | 4 767 | clean | Barely; a status table only |

**Method, so the absence claim is auditable.** I ran one `Select-String` pass per veto trigger over
`Articles/analyses/*.md` (all 8 files) with these patterns: `7.1852e-5|1.0492e-5|936.21|972.00|3.3319` (V1),
`bep_example_index` (V3), `grep.?hit|0 hits|zero hits` (V4), `changes over time` (V5), `Julia|SciML` (V6),
`Key Quotes` (V7). Result: **V1, V4, V5 and V7 return zero hits across all 8 files.** V3 hits only
`bep_example_index.md:8` (a self-reference). V6 hits exactly `bep_example_index.md:19` and `:138` — which is
precisely the pair `conventions.md:237` names, so the veto is corroborated to the line.
**Limitation, stated because Rule 36 requires it:** this proves absence of those exact strings, not absence of a
paraphrase. A claim could still trip V7 by restating a 2-pass "Key Quote" without using the phrase.

### Veto 7 does not apply to the KG — and that is the point worth making

Veto 7 (`state.md:40`) voids the *2-pass pipeline's* "Key Quotes". The KG is a **different extraction route**:
`kg_chunk.py` → in-session bounded-ontology prompt → `kg_validate.py` substring-check (`conventions.md:152-154`).
Its grounded quotes are validator-checked substrings, not pipeline quotes. So the KG survives V7 — **but only
because its provenance is re-checkable**, and `conventions.md:225` is explicit that the contamination extent was
never measured (`"Omvang niet gemeten"`). The honest briefing line is therefore about *method*, not about the
numbers: *"the knowledge graph was built by a separate route with a validator that substring-checks every quote;
the two-pass quotes are a different artefact and we do not use them."* Never: *"our quotes are clean."*

### One thing I could not read

`Articles/graph/paper_kags/bridge_larsen_berger_run1.json` **could not be opened on this machine.** The three
files in that directory are enumerated with their sizes (6 630 / 1 852 / 7 525 bytes) but their bytes are not
retrievable: `Test-Path` returns `True`, `Get-Content` returns `Cannot find path`,
`[System.IO.File]::Exists` returns `False`, `New-Object System.IO.FileInfo(...).Attributes` returns `-1`, and
`[System.IO.File]::Open(...)` throws `Could not find a part of the path`. `git show HEAD:<path>` reports
*"does not exist in 'HEAD'"* and `git cat-file -p :<path>` reports *"neither on disk nor in the index"*, while
`git ls-files` lists all three — an inconsistent index, most likely a OneDrive Files On-Demand placeholder in an
error state rather than a missing file.

**This does not block RS-2.** Both `SEMANTIC_LINKS` edges it produces are present in `knowledge_graph.json` with
their full `provenance` blocks inline — `provenance.kind: llm_inferred`, `within_chunk: false`, confidences 0.85
and 0.80, and rationales naming the two cross-doc bridges. `conventions.md:161` already fixes their status. I read
them from the merged graph, not from the bridge file, and I do not claim to have read the bridge file.

### UNVERIFIED

| Item | Status | What would resolve it |
|---|---|---|
| Whether `Articles/graph/paper_kags/` is readable after a OneDrive re-sync | `UNVERIFIED`, not absent | Re-sync, then re-run the three probes. Until then the bridge file's own contents are unread. |
| Whether the 3 mojibake quotes match the PDF after rendering | `UNVERIFIED`. Provenance stops at the chunk file; nothing in the KG reaches the PDF bytes. | Render `berger2008` p. 8–11 and compare. Cosmetic, not a number risk. |
| Whether `carberry-number`'s `< 0.05` is Berger's or an extraction artefact | `UNVERIFIED`. The node has no provenance field; only the *edge* above it is grounded, and that edge's quote names the criterion without a threshold. | Read `dynamic_kinetics_berger2008.md` for the threshold, then check Berger p. 11. |
| Extent of the 2-pass contamination | `UNVERIFIED` and explicitly out of reach tonight — `conventions.md:225` states the extent over the ~141 pipeline runs was never investigated. | The runbook named at `conventions.md:225`: `.agents/resources/runbooks/verifying-extraction-claims-against-pdf-text-layer.md` § Cross-contamination. |

---

## RS-3 — Which of Larsen (2024) is citable, given both Appendix E and Appendix F are unread?

**Ticket type:** `wayfinder:research`.

### Question, verbatim from the map

> Appendix F was never read (`conventions.md:212-214`), and until it is, the six Larsen parameters may neither be cited
> as a source nor called fabricated (`state.md:33-34`). What is the minimum read that would settle this, and does it
> change what the briefing can say?

(`damian_briefing_2026_10_09.md:103`; vetoes at `state.md:34-35`, see citation correction above)

### Answer

**Minimum read: pages 71–76 only — Appendix E. Appendix F is not needed, and both vetoes are mis-routed to it.**

The two vetoes point at the wrong appendix. `state.md:35` says *"verifieer eerst Appendix F"* before the six values
may be called anything. But the six values are not in Appendix F:

| Appendix | Pages | What is in it | Which blocker it settles |
|---|---|---|---|
| **E** | 71–76 | Tables E.1–E.3, the fitted parameters per variant, plus every calculated RMSE | **Veto 1** — the six values, and whether `r_{1,\max}` and `n_{\text{inh}}` exist |
| **F** | 77–88 | `A`, `rho_support`, solver / grid / tolerance / DE-bounds | **§12.3** — a *separate* blocker, that the model is not normalised |

Evidence, verbatim: `Articles/2 meeting Damian + Zoë/extracted/Ch6_Results_and_Discussion.txt:436` reads
*"The parameters used in each variant can be found in Appendix tables E.1 to E.3, together with every calculated
RMSE, RMSE … and RMSE … values."* That is Larsen's own sentence, and it routes the parameters to **E**. The same
route is given independently by `state.md:54` (`Ch6:436-437`) and by
`literature_categorization_and_action_plan.md`. Appendix F's contents are separately enumerated at
`conventions.md:214` and `state.md:56`, and neither list mentions a fitted parameter.

So lifting Veto 1 and Veto 2 requires **pages 71–76**. Reading Appendix F settles §12.3 and leaves both vetoes
exactly where they are.

### What is citable from Larsen right now, with no appendix at all

This is the larger finding, and it is what the briefing can actually say tomorrow.

`Articles/analyses/literature_index.md:229-266` is a full, independent Larsen record with **no values in it at
all** — and that is the point, not a defect. It is citable for:

| Citable now | Line | Note |
|---|---|---|
| Bibliographic identity, citekey `BEPExample`, BEP thesis, TU Delft, Catalysis Engineering, 2024 | `literature_index.md:229-237` | `:231` citekey; `:237` document type |
| **Supervisor line** — Ir. Damian Vico van Berkel daily supervisor, Prof. Atsushi Urakawa responsible supervisor, Dr. Ana Somoza-Tornos second examiner | `literature_index.md:234` | see the caution below |
| The three catalyst formulations with loadings: Pd₀Ag 0.025 wt% Pd / 5.0 wt% Ag, Pd₂Ag 0.05 / 5.0, Pd₃Ag 0.1 / 5.0; Ag:Pd 200:1 / 100:1 / 50:1 | `literature_index.md:239` | agrees with `conventions.md:192` (Table 4.1, `Ch4:17-21`) — two independent records of the same numbers |
| GHSV range 30 000–120 000 h⁻¹ | `literature_index.md:239` | |
| **All three rate equations in LaTeX** — `r_{1,\text{raw}}`, the capped `r_1`, and `r_2` with `(1 + K_{\text{inh}} p_{\text{C}_2\text{H}_2})^{n_{\text{inh}}}` | `literature_index.md:255,257,259` | The asymmetry `conventions.md:187` warns not to "correct" is visible on the page |
| Differential Evolution discriminating Power Law, Standard LHHW, Extended LHHW | `literature_index.md:239` | agrees with `conventions.md:190` |
| The RMSE triple 5.10 / 5.43 / 7.14 %, attributed to Section 6.2.4, p. 43 | `literature_index.md:262-265` | `conventions.md:191` independently confirms these "bestaan en zijn correct" at `Ch6:678`, `Ch7:35`, `Ch1:21` |

**`literature_index.md:261` is the single most important line for this ticket**, and it also closes RS-1's open
item:

> *"Individual numerical kinetic parameter values ($k_1$, $k_2$, $K_{C_2H_2}$, $K_{C_2H_4}$, $K_{H_2}$,
> $K_{\text{inh}}$, $n_{\text{inh}}$, $r_{1,\max}$) were omitted from the thesis text because all parameters were
> fitted simultaneously and individual values were deemed not meaningful on their own (Larsen, 2024, Section 6.2.4,
> p. 40)."*

Two consequences:

1. **RS-1 closed.** `finding_taxonomy.md:200` describes Larsen as *"index entry with the eight fitted values"*.
   That description is **wrong** — the index entry it points at lists the eight *symbols* and states they have no
   values in the thesis text. The run's premise for binning Larsen on Axis 1 (parameter provenance) was already
   unfounded; the paper says the values are deliberately not in the body.
2. **It strengthens Veto 1 rather than weakening it.** The values are absent from the thesis text *by Larsen's own
   design*, and live only in Appendix E. That is a second, independent reason the six-value set cannot be verified
   from our text layer — separate from the reason `conventions.md:201` gives (the appendix pages have no text layer
   because our extraction stops at page 54).

### The extraction cutoff, verified

`conventions.md:201` and veto 4 (`state.md:37`) both state that `pdf_full_extracted.txt` stops at page 54. I
verified this rather than repeating it: the file's page markers run `--- PAGE 1 ---` at line 1 through
`--- PAGE 54 ---` at **line 1760**, which is the last page marker in the file, and the file ends with the
bibliography at reference [28]. Total 1 814 lines, 135 421 bytes. So the cutoff is exactly as documented, and
veto 4's warning is real: a zero-hit grep over that file cannot prove absence from pages 71–88.

### Files verified on disk, including one trap

| Path | Status |
|---|---|
| `Articles/2 meeting Damian + Zoë/BEP Example.pdf` | **exists, 9 167 352 bytes.** This is the target named at `conventions.md:214`. |
| `Articles/2 meeting Damian + Zoë/BEP Example (no appendix).pdf` | **exists, 5 519 129 bytes.** Sits in the same folder. |
| `%USERPROFILE%\Zotero\storage\4GYT8PKI\BEP Example.pdf` (`literature_index.md:232`) | **does not exist** — `[System.IO.File]::Exists` returns `False`. The index entry's `File Path` is dead. |
| `Articles/2 meeting Damian + Zoë/extracted/` | 8 files: `Ch1`–`Ch7` plus `pdf_full_extracted.txt` |

The `(no appendix)` file is a trap worth naming in the briefing prep, because it produces the same wrong conclusion
as a zero-hit grep: opening it and finding no Appendix E gives a false "the appendices don't exist / are empty",
which is veto 4's error in a different costume. The appendices exist; only *our text layer* stops at page 54.

**I did not attempt to view any PDF.** No page was rendered. The minimum read is stated as a specification:
render pages **71–76** of `Articles/2 meeting Damian + Zoë/BEP Example.pdf` as images and read the three tables
E.1–E.3. Route is `av-inspector` per Rule 31 and `conventions.md:214`. If pages 77–88 are rendered in the same
pass, §12.3 closes too, but it is a separate deliverable.

### The one caution on the otherwise-citable supervisor line

`literature_index.md:234` names Damian as Larsen's daily supervisor and Urakawa as responsible supervisor. That is
*about Larsen's thesis*, and it is citable as such. It is **not** a statement about Lucas's own supervision line,
where four irreconcilable lines are live and unresolved (`state.md:6-11`) and where the user's own position is
governing (`state.md:5`, Rule 41). The briefing must not slide from one to the other. Map §4 already flags this at
`damian_briefing_2026_10_09.md:138`.

### UNVERIFIED

| Item | Status | What would resolve it |
|---|---|---|
| Whether Appendix E tables E.1–E.3 contain the six values **and** `r_{1,\max}`, `n_{\text{inh}}` | `UNVERIFIED`, and unresolvable tonight. `conventions.md:206` records the competing explanation — that run2 *did* read raster pages and our extractor did not — as explicit speculation. | Render pages 71–76 and read them. Nothing else in the workspace can settle it. |
| Whether `literature_index.md`'s equations at `:255-259` are verbatim from the thesis | `UNVERIFIED`. They are consistent with `conventions.md:187`, which reports Eqs. 6.9–6.11 "verbatim bevestigd" at `Ch6:665-677` — but consistency is not identity, and the index entry is a secondary record. | Diff `literature_index.md:255-259` against `Ch6:665-677`. Cheap, needs no PDF. |
| Whether the two `BEP Example.pdf` files are the same document | `UNVERIFIED`. The 9.17 MB file is 1.66× the 5.52 MB file; consistent with appendices present in one and absent in the other, but I did not open either. | Compare page counts, or render page 1 of each. |
| Whether `literature_index.md:232`'s dead Zotero path ever existed | `UNVERIFIED`. Dead now; no record of when or why. | Check the Zotero storage folder. Low priority: the workspace copy is present and is the cited one. |

---

## SP-3 — `3_Model/transient_model_framework_audit.md` claim-status sweep

**Ticket type:** `wayfinder:research`.

### Question, verbatim from the map

> of the 8 model defects the framework audit raises against Berger (2008), which are now confirmed present in the
> script, which are already covered by the register under a different ID, and which remain UNVERIFIED?

(`damian_briefing_2026_10_09.md:62`)

### The count is wrong: there are nine, not eight

The audit states its own count. `transient_model_framework_audit.md:7` reads: *"Fix the **nine** items in §3 before
any of this reaches code."* §3 has nine subsections, `:52` through `:114` — §3.1, §3.2, §3.3, §3.4, §3.5, §3.6,
§3.7, §3.8, §3.9 — confirmed by reading the full heading outline of the 155-line file.

The figure **8** originates in the register, `3_Model/state.md:22`: *"8 *model*-defecten"*. The map inherits it at
`damian_briefing_2026_10_09.md:62`. **Nine is correct and the audit is authoritative on its own count.** The
briefing should say nine, and should say where the eight came from rather than silently correcting it.

The number 8 is not arbitrary, and the coincidence is the trap: the **register** also has eight rows,
`3_Model/state.md:79-86` — D1–D6 plus two `—` rows. Two different eight-versus-nine counts, one row apart in the
project, on opposite sides of the distinction the briefing is built to make. The audit's eight are the *other* list,
`transient_model_framework_audit.md:124-134`, which is a **cite list, not model defects** — `:122` says "**Eight are
`UNVERIFIED`; the ninth row is the one confirmed item**". That is the probable origin of the confusion, and it is
the same nine-versus-eight pattern in a second place.

### The sweep — all nine, and the four not already covered

`3_Model/state.md:40-45` accounts for §3.9↔D5, §3.4↔D1, §3.3 and §3.6 unregistered. Per the ticket those four are
verified, not re-derived. The remaining five:

| Audit § | Finding | Status | Evidence |
|---|---|---|---|
| **§3.1** | Displayed bulk equation contradicts Berger Eq. (1) by `ε_b²` | **NOT present in the script** | Script uses Berger's form: `advectie_term = - (p.u_s / p.epsilon_b) * …` at `c2h2_hydrogenation_transient_model.py:206` and `:208`, and the transfer term carries `(1 - p.epsilon_b)` at `:203` — matching the audit's *pseudocode* term for term (`audit:66`), which the audit calls "the correct one". The `ε_b²` defect lived only in the Canvas's **displayed** equation. Document-level fix, tracked as FW-1/FW-2 at `state.md:62-63`. **No register ID needed, and none is missing.** |
| **§3.2** | The `r = 0` branch is wrong twice | **CONFIRMED PRESENT** — and this is the D2 line | `:179` reads `(1 + p.s) * (c_p[z, 1, :] - c_p[z, 0, :]) / (dr**2)`. Both audit complaints are true of it: it is one-sided (no ghost node `c_{-1} = c_1`, so it cannot be the central rule), and the coefficient is `(1+s) = 3` where the exact limit is `2(1+s) = 6`. The file's own comment at `:178` says *"voor sfeer is het 6 ipv 2 in de limiet"*. → **D2** |
| **§3.7** | `Bim` defined twice, inverting (`k_g R/D_e` vs `D_e k_g R`) | **NOT present in the script** | Zero hits for `Bim`, `bim`, `Biot` across all 251 lines. The audit required at `:108` that this "must not reach the code", and it did not. Document-level fix, tracked as FW-10 at `state.md:71`. **This is a clean negative result and it is worth saying out loud in the briefing.** |
| **§3.8** | Scheme inconsistency across the two chats | **CONFIRMED PRESENT, and already covered inside D2** | `:182` labels the interior scheme "CENTRAL DIFFERENCE SCHEME voor diffusie", and the `r == 0` branch at `:179` is one-sided. The register's D2 row already carries this: `3_Model/state.md:61` states the script is "`s`-dependent and one-sided (§3.2)". **No new ID is needed** — it is a component of D2, not a seventh defect. |
| **§3.5** | "State-space ordering" is coupling, not ordering | **CONFIRMED**, no separate code line | Same underlying condition as §3.4 — the film closure choice. `audit:155` lists §3.5 among the items the second audit confirmed. `state.md:70` (FW-9) carries it as a **coupling decision**, explicitly *"géén volgordevraag"*. |

### Verification of the register, by reading the code rather than re-deriving

Every register row was checked against the source lines, read directly:

| Register | Register line | Script line, read | Verdict |
|---|---|---|---|
| **D1** rhs mutates the state vector | `3_Model/state.md:79` | `:135` `c_p = y[idx1:idx2].reshape((N_z, N_r, N_gas))` is a **view**; `:158` `c_p[z, -1, :] = C_s` writes through it, inside `for z in range(N_z)` at `:152` | **confirmed** |
| **D2** `r=0` coefficient is ½ of exact | `:80` | `:179` `(1 + p.s)` → `3` at s=2, against exact `6` | **confirmed** |
| **D3** `θ` at `r = R_p` never receives a derivative | `:81` | `:164` `for r in range(N_r - 1)` with comment *"Buitenste schil is al gedefinieerd"* — the last shell is outside the loop, so `dTheta_dt[z, N_r-1, :]` is never assigned | **confirmed by loop bound**, independent of running the probe |
| **D4** quadrature is `O(dr)` and drops `r=0` | `:82` | `:195` `volume_gewicht = (r_radius**p.s) * dr` is zero at `r=0`; `:199` normalises by the analytic `(p.R_p**(p.s + 1)) / (p.s + 1)`, not the discrete sum | **confirmed** |
| **D5** `R_gas` docstring wrong, no double-`C_t` | `:83` | `:174` and `:203` — the two `C_t` factors | **confirmed**; retraction intact |
| **D6** Jacobian dominates | `:84` | not a single line; a cost property | **not re-verified** — the map's §2 records a live probe run on 2026-10-08 and `3_Model/state.md:88-91` makes the *structure* the durable claim. Not re-run: fixing and measuring are out of scope and the probe takes ~46 s under load. |
| **`E_a` parsed but unused** (row `—`) | `:85` | `E_a` occurs exactly once in the file, in the comment at `:32`; `k = lambda name: p.kinetics[name][0]` at `:87` reads only index `[0]` | **confirmed** — temperature is inert |
| **all kinetics `0.0`** (row `—`) | `:86` | `:34-43`, all eight entries `(0.0, 0.0)` | **confirmed**, exactly as the map cites |

### Answer in one line

**Of the nine: four are confirmed present and unregistered as concerns only in FW bullets (§3.1, §3.3, §3.6, §3.7
— of which §3.1 and §3.7 are *not* in the script at all), one is confirmed present as part of D2 (§3.8), one is D2
itself (§3.2), one is part of D1 (§3.4), one is a coupling decision (§3.5), and one is D5 (§3.9). Nothing in §3
remains UNVERIFIED — but two of the nine are absent from the code, which is the finding the briefing gains.**

### Two things this sweep changes for the briefing

1. **The register is complete for the code, and the framework audit's nine items are all adjudicated.** There is no
   seventh blocking defect hiding in the audit. That directly supports the destination criterion that the blocking
   defects "are presented as the strength, not the embarrassment" (`damian_briefing_2026_10_09.md:17`).
2. **§3.1 and §3.7 are two defects that were caught before they reached the code.** The audit found them; the
   implementation avoided them by following the pseudocode rather than the displayed equation, and by never
   transcribing `Bim`. That is a demonstration that the framework audit did work, and it is the cheapest available
   answer to Damian's likely question — *"what did the audit actually buy you?"*

### UNVERIFIED

| Item | Status | What would resolve it |
|---|---|---|
| Whether D6's seconds reproduce today | `UNVERIFIED` in this session. `damian_briefing_2026_10_09.md:37` records a live run on 2026-10-08 (rhs `0.0114 s`, Jacobian `16.9 s`) against the register's `0.016 s` / `23 s`. | Re-run `pixi run python Academics/BEP/Catalysis/3_Model/probes/audit_2026_09_30.py`. `3_Model/state.md:88-91` already rules the seconds non-durable and the structure durable, so this is not blocking. |
| Whether `3_Model/state.md:22`'s "8" was deliberate | `UNVERIFIED`. The audit says nine at `:7`; no document explains the eight. The eight-versus-nine coincidence across the cite list (`audit:122`) is the likely cause but is inference, not evidence. | The 2026-09-30 session transcript, or the supervisor's recollection. |
| Whether §3.5's coupling question has been *decided* | `UNVERIFIED`. Confirmed present as a question (`state.md:70`), but no file records a decision. Register `:84` says D6 is blocking "for any sweep", and the film closure is still open at `state.md:102`. | A choice, and it is a choice: BW-flux balance or drop the film term. Belongs to the human, per the map's DR-1 inheritance. |

---

## DR-3 — The four overlap points, one sentence each

**Ticket type:** `wayfinder:task`. · **Destination chosen: `afk_findings.md`**, as a numbered section. Not
`veto_crosswalk.md`, which is reserved for the veto mapping so the two documents stay independently citable.

### Question, verbatim from the map

> for each of the four documented overlaps between the framework audit and the register, what is the one sentence
> that shows the distinction was seen — and in particular, how is the corrected D2 story (same line, two different
> diagnoses) put in one sentence?

(`damian_briefing_2026_10_09.md:80`)

### The four overlaps

`3_Model/state.md:40-45` is a four-row table. Each row is one line of Dutch working prose in the project's register.
Below: a one-sentence English rendering for each, then the D2 sentence broken out because it does not survive
compression without the two-part structure.

**Overlap 1 — §3.9 ↔ D5, the `C_t` question.**
> *"The framework audit flagged that one symbol is used for both per-site and per-volume rates; D5 is that same
> finding once the script's docstring is read dimensionally — which also showed the `C_t` factors themselves are
> correct, so the double-`C_t` defect I first reported was mine and is withdrawn."*

(`3_Model/state.md:42`; `3_Model/state.md:65`; `3_Model/state.md:83`; retraction wording at `:65`)

**Overlap 2 — §3.4 ↔ partly D1, the same code line.**
> *"Both findings sit on line 158 of the script, but they are asking different questions: §3.4 asks whether the
> film term can ever be switched on, and D1 asks whether writing that boundary condition corrupts the solver's
> state — one is a modelling switch that is stuck off, the other is a memory bug."*

(`3_Model/state.md:43`; script `:158` for `c_p[z, -1, :] = C_s`, `:155` for the `C_s = C_b[z, :]` assignment, `:203`
for the film term's absence)

**Overlap 3 — §3.3, readsorption, present but unregistered.**
> *"§3.3 says the source's only stated requirement is a readsorption term and the model has none — the script
> confirms that, and it is a real gap that the register does not yet carry as a numbered item."*

(`3_Model/state.md:44`; `state.md:68` FW-7; script confirmed: zero `readsorp`/`TPD` hits, read across all 251 lines)

**Overlap 4 — §3.6, no energy balance, present but unregistered.**
> *"§3.6 notes the model drops the energy balance and both Prater numbers while our own scope says 'isothermal →
> exotherm', and the script does drop it — but that is a scope decision to be made explicitly, not a coding bug to
> be fixed."*

(`3_Model/state.md:45`; `state.md:74` FW-13; script confirmed: zero `Prater`/`exotherm`/`energy_balance`/`dT_dt`
hits; the audit's own framing at `transient_model_framework_audit.md:104` is "Scope decision, not a coding bug")

### The D2 sentence, and why it needs two clauses

The correction at `3_Model/state.md:28-37` records that an earlier version of the register wrongly claimed the two
audits overlapped on one point and that §3.6 was "the same defect" as D2. It was wrong. Both point at line 179 of
the script, and both are true, and they are not the same claim:

- **§3.2** is about the **chat pseudocode**, and it is about the *scheme*: the hard-coded `6/dr²` is a spherical-only
  limit presented as general, and a stencil that reads `c_p[r+1]` from the centre node is one-sided, which is not the
  central rule that was agreed. (`transient_model_framework_audit.md:78-79`)
- **D2** is about the **script**, and it is about the *number*: the script evaluates `(1+s) = 3` where the exact
  spherical limit is `2(1+s) = 6`, so the code is half of correct. (`3_Model/state.md:61`, `:80`; script `:179`)

Three things follow, and the one sentence has to carry all three.

1. They are on the same line, so they cannot be dismissed as describing different code.
2. They diagnose different things — *scheme* versus *coefficient* — so the audit does not explain D2 away.
3. The audit **endorses 6 as the correct symmetry factor** while faulting its `s`-restriction, which means the audit
   *confirms the direction* of D2 rather than duplicating it. (`transient_model_framework_audit.md:79`: the ghost-node
   construction "restores the factor-6 symmetry instead of approximating around it"; `3_Model/state.md:34-35`)

**The sentence:**

> *"Both findings land on line 179 of the script, but they diagnose different things — §3.2 is about the scheme,
> that reading the centre node one-sidedly breaks the central-difference rule we agreed on, while D2 is about the
> coefficient, that the script uses 3 where the exact spherical limit is 6 — so the audit confirms the direction of
> D2 without explaining it away, and the fix is the ghost node that satisfies both at once."*

**Why "the fix satisfies both at once" is load-bearing, and is also the honest framing of a still-open item.**
Implementing §3.2's prescribed ghost-node construction (`c_{-1} = c_1`, `transient_model_framework_audit.md:79`)
replaces the one-sided `(c₁ − c₀)/dr²` with the symmetric `(c₁ − c_{-1})/dr² = 2(c₁ − c₀)/dr²`, which restores the
factor of 2 — i.e. `3` → `6`. One edit clears the coefficient error and the scheme error together. That is the
cleanest single sentence available for the walkthrough, because it converts an apparent double-count into one fix.

**What it must not say.** Not "the two audits are the same" (`3_Model/state.md:29` retracts that), and not "the audit
found D2" — the script's `3` where the chat said `6` was, per `3_Model/state.md:36-37`, *"een **eigen** afwijking die
geen van beide audits eerder had opgemerkt"*, an independent divergence neither audit had noted.

### Where these sentences sit in the 12-minute route

`3_Model/state.md:59` allots segment (4) two minutes to the four overlap points. At roughly 15 seconds each, the four
sentences above plus the D2 sentence is the whole segment, with no room for the FW-bullet backlog. Two of the four
overlaps (3 and 4) are *not in the register*, so the honest sentence there is "a real gap I found and have not yet
numbered" — which is a stronger statement than a register ID would be, and costs nothing to say.

### UNVERIFIED

| Item | Status | What would resolve it |
|---|---|---|
| Whether the ghost-node fix would give exactly `6` | `UNVERIFIED` — **arithmetic, not measurement.** Read off `transient_model_framework_audit.md:79` and the `r=0` stencil at `:183-190`. I did not implement it; implementing D2 is forbidden and is the register's fix task. | Run the audit probe after the fix. Belongs to whoever takes D2. |
| Whether D2's `max` factor-of-2 claim and the §3.2 scheme claim have independent numerics | `UNVERIFIED`. The register's D2 number (`:80`) comes from the analytic `f=r²` check; the scheme claim has no separate probe block. | A probe that ablates only the stencil direction, holding the coefficient fixed. |
| Whether these sentences survive Damian interrupting | `UNVERIFIED`. They are drafted, not rehearsed. | Say them out loud. Not an agent task. |

---

## AR-3 — Language and register of the briefing artefact

**Ticket type:** `wayfinder:task`.

### Question, verbatim from the map

> is the delivered artefact in Dutch, English, or bilingual, and does `conventions.md` §7 (Damian comms = English,
> natural, low-key) govern the spoken briefing as well as written messages?

(`damian_briefing_2026_10_09.md:126`)

### The cited rules, verbatim

`conventions.md:90-93` in full:

```
### 7. Supervisor Communication Formatting (Damian / WhatsApp)
- **Channel:** WhatsApp (no email).
- **Language & Tone:** English, natural and low-key.
- **Formatting:** Use bullet points only when making summations or listing specific cases to improve readability.
```

`conventions.md:86-88` in full:

```
### 6. Writing Collaboration & Humanized Prose (Rule 15)
- Provide structure, keywords, and concept blueprints using clean LaTeX markup (`itemize`, `enumerate`, headers,
  bold terms)—never dense prose.
- Strictly adhere to anti-AI slop standards: eliminate buzzwords (*delve, tapestry, pivotal, crucial, robust,
  landscape*), avoid significance inflation, use plain verbs, and maintain concise sentences.
```

### Conclusion, and the honest limit of the rule

**The spoken briefing and the written artefact are English. Dutch is the language of the internal notes around
them, and that stays as it is. §7 governs the *tone* of the briefing but not, by its own terms, the briefing.**

The reasoning, in the order it should be given:

1. **§7 does not reach the briefing, literally.** Its heading scopes it to "Supervisor Communication Formatting
   (**Damian / WhatsApp**)" (`conventions.md:90`), and its first rule fixes the **channel**: "WhatsApp (no email)"
   (`conventions.md:91`). A channel rule cannot govern a spoken conversation in a room, and it cannot govern a
   printed sheet. **So the map's phrasing — "does §7 govern the spoken briefing as well as written messages" —
   has the wrong premise: §7 does not govern the spoken briefing, and it governs the spoken briefing no more and no
   less than it governs a written message.** A channel rule is a rule about a channel.

2. **§7 is nevertheless the strongest available evidence for the language, and it points one way.** `:92` fixes
   "English, natural and low-key" for Damian-facing content. It is the **only** language rule in the entire branch
   conventions file — I searched the whole 243-line file for `Language|Tongue|Dutch|Nederlands|Engels|English` and
   got exactly two hits, `:90` and `:92`. So there is no competing rule, and the only rule that names a language
   names English for content aimed at Damian.

3. **§6 *does* govern the written artefact, unambiguously.** `:86-88` is a writing rule with **no channel scope**,
   so it applies to anything written for this project: structure as `itemize`/`enumerate`/headers/bold terms and
   "never dense prose", plus the anti-slop list. That is the binding constraint on the DR-2 one-pager, and it is
   the same list this session's own output is written against.

4. **The project already demonstrates the split, so no decision is actually being invented.** In
   `3_Model/state.md` the *narrative* prose is Dutch — the walkthrough ticket at `:59` is entirely Dutch — while the
   *technical content* is English: every defect bullet from `:60` to `:67` is English ("Make the rhs non-mutating",
   "Correct the `r=0` symmetry factor", "Surface coverage at the pellet shell is frozen"), and so is the register
   table at `:77-86`. The walkthrough artefact would sit between them, and it is the English half that Damian reads.

5. **Rule 15 and the map's own framing agree.** `conventions.md:86` is titled "Rule 15", whose workspace text is
   "Collaborative Authoring & Anti-AI Humanization" — a rule about prose quality, not about language. The map's
   destination text at `damian_briefing_2026_10_09.md:10-12` is written in English, and so is the whole of §1-§5 of
   this map. A Dutch artefact inside an English project would read as a translation, not as the work.

### The register rule, stated as a constraint rather than a licence

`:93` is a **limitation** on formatting, not permission to bullet anything: "Use bullet points only when making
summaries or listing specific cases to improve readability." Read against §6's "never dense prose", the two together
mean the one-pager is a **table with a short margin note per number**, not a bulleted essay. That is consistent with
the destination's criterion 1 — every number re-derivable on demand (`damian_briefing_2026_10_09.md:16`) — and it
constrains DR-2, which is a `wayfinder:prototype` ticket and therefore not in tonight's scope.

Tone, from `:92`: **English, natural and low-key.** Concretely that forbids the register's own register-praise — no
"significant", no "crucial", none of the `:88` word list, and no participle clause trailing a finding. The six
sentences in DR-3 were written against that list deliberately.

### What is settled, and what is not

| Question | Answer | Basis |
|---|---|---|
| Language of the spoken briefing | **English** | `conventions.md:92` as the only language rule; `3_Model/state.md:60-67` is already English |
| Language of the written artefact | **English** | same, plus `conventions.md:86-88` governing the prose |
| Does §7 *govern* the briefing? | **No, not by its own terms** — it is channel-scoped to WhatsApp (`:90-91`). Its language/tone rule is the best evidence and it says English. | `conventions.md:90-92` |
| Does §6 govern the written artefact? | **Yes** | `conventions.md:86-88`, no channel scope |
| Internal prep notes around the artefact | **Dutch, unchanged** | `3_Model/state.md:59` and `:6` |
| Register / tone | **English, natural, low-key**; structure not dense prose; bullets only for summations and cases | `conventions.md:92-93`, `:86-88` |

### UNVERIFIED

| Item | Status | What would resolve it |
|---|---|---|
| Whether the briefing is recorded in writing at all | `UNVERIFIED`, and it depends on AR-2, which is a `wayfinder:grilling` ticket (`damian_briefing_2026_10_09.md:120-123`) — script versus conversation. Not mine to close. | The human's choice between a deliverable script and a hand-held register. |
| Whether the *thesis* language constrains the artefact | `UNVERIFIED`. No language rule for the thesis exists in `conventions.md`; the one-line search returned only `:90` and `:92`. The thesis is a separate artefact in a separate repo. | Check the thesis sources directly. Not gating for a spoken briefing. |
| Whether Damian prefers to be addressed as "Damian" or by title in an English artefact | `UNVERIFIED`. `conventions.md:100` records "Damian Vico van Berkel — PhD Candidate (TNW / ChemE - Catalysis Engineering)" and `:118` fixes "**géén** dr./prof." for him. | Ask, or read the existing thread. Cheap, but a human call. |