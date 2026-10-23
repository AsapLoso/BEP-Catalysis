# Goal 5 — BEP claim-level citation provenance and repeatable evidence audit

**Status:** work specification and handoff; NOT executed.  
**Authoritative starting AI reference:** `AsapLoso/project-management-agents`, branch `work/bep-integrated-reference-map-v1-20261022`, PR [#180](https://github.com/AsapLoso/project-management-agents/pull/180). Verify the latest branch head before starting; prior inspected head was `1cd680f95902a0a79b17afb084fa29ab49c6b25f`.  
**Existing dataset:** `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/`.  
**Parallel owner map (READ-ONLY context):** branch `research/bep-manual-map-session-20261022`, draft PR [#182](https://github.com/AsapLoso/project-management-agents/pull/182), `Academics/BEP/Catalysis/research/manual_map_sessions_2026_10_22/owner_working_map/`.

## Scientific goal

Make every substantive AI-reference claim **traceable to its actual evidentiary passage**, so a later human or fresh AI session can independently inspect the source and decide whether the interpretation is justified. Audit the *existing* integrated scientific map instead of generating another taxonomy or more node count.

Baseline checked on 2026-10-22: **143 scientific nodes, 65 source/context records, 340 claim references, 59 typed relationships (35 cross-disciplinary), 21 reconciliations, 23 uncertainties**. Verify current numbers from real files. Preserve all 171 historical concept dispositions, 144 prior crosswalk rows and 96 historical source attachments. The original scientific map remains AI provisional; no target reactor gain is established.

## Correct ownership, reading and verification semantics

There are **separate dimensions**. Never collapse them:

1. **Five scientific writing/maturity stages**, historically `tier 0..4`: `Idea`, `AI worked out`, `Human worked out`, `Informal Writing`, `Formal Writing`. Existing reference dataset uses `idea` and `ai_worked_out` only. Never promote a reference claim to a personal/human state automatically; later writing stages are NOT evidence verification.
2. **Source/citation review authority:** `AI` versus `human`. A source-to-claim connection is AI-level even after multiple automatic audits. `human_verified` requires the owner's explicit, claim-specific affirmation after inspecting evidence. Internally distinguish *AI attached but not checked*, *AI passage checked*, *AI challenged/corrected*, and *source inaccessible*; none is human-verified.
3. **Owner reading:** `unread` or explicitly read, independent of source access by AI.
4. **Node structural approval:** accepted/proposed/rejected for exact node and parent. Acceptance of a taxonomy placement does not establish scientific understanding or citation correctness.
5. **Human understanding:** only the owner can explicitly confirm it at the precise node/claim scope. Never infer blue from a conversation, a structural change, or successful scientific validation.

Do not change `current_map.yaml` or other owner science records during this citation mission. The existing owner map has structure-level approvals but the AI-written scientific contents are unread/unapproved; inspect `owner_working_map/state.md` for the latest authoritative state.

## Claim → evidence contract

For each substantive claim reference, create/update a stable, machine-readable citation record linking:

`owner node (if one exists) → AI reference node ID → precise claim ID → source ID → located evidence passage`.

Required fields, wherever available:

- **IDs:** stable `claim_id`, `reference_node_id`, `source_id`, one or more evidence locator IDs; explicit relationship, not an uninspectable general bibliography citation.
- **Bibliography:** exact title/authors/year, DOI/stable URL or immutable local repository path and source edition/version; reuse existing `sources.yaml` IDs.
- **Locator:** chapter/section/subsection, printed page **and PDF-page index if different**, equation/figure/table/paragraph as appropriate; say `unknown` instead of guessing.
- **Evidence quotation:** a **short exact verbatim excerpt**, with precise attribution and locator. Keep extracts minimal, observe source copyright restrictions and do not aggregate long text from a single publication; link to the full source for broader inspection. No invented words or reconstructed quotes.
- **Support judgement:** the precise claim being supported, what the excerpt *actually* states or demonstrates, why it supports/contradicts/only partially supports the AI inference, and alternative interpretations.
- **Applicability limits:** catalyst (including Pd versus PdAg), support, experimental/theoretical method, feed/pressure/temperature window, rate normalization and other conditions when material.
- **Evidence class:** direct source measurement, source model result, review synthesis, project-proposal hypothesis, assumption-bound mathematical derivation, historical unverified attachment, etc.
- **Access and status:** `full_text_read`, `abstract_only`, `preview`, `metadata_only`, `local_project_source`, `inaccessible`; separate AI audit state and **human_verified=false** unless user gives explicit approval.
- **Provenance:** DOI/path, retrieval date, relevant document revision or file SHA when possible, prior claim text, auditor session/wave, outstanding questions.

Where mathematical claims follow by a derivation rather than a paper quotation, record the theorem/source and assumptions, equations and reproducible derivation/proof. Do not invent an empirical quotation for an algebraic identity. If a paper is behind an inaccessible paywall, attach only what was truly read and mark the broader claim unverified.

Example: `C₂H₂ + 2 H₂ → C₂H₆` is an overall stoichiometric net result (`R3=R1+R2`), **not** itself proof of an independent microscopic path or a third fitted rate. Record separate source-specific evidence for direct/non-desorbing/ethylidene pathways, and the applicability limits.

## Scientific scope and priorities

The work is **a real citation research/audit execution**, not a schema-only or checklist-only assignment.

Cover the **current full claim inventory** progressively, first prioritizing (a) catalyst-specific pathways, adsorption and mechanistic statements, (b) equations/units/transport and kinetics, (c) identification/periodic forcing and any positive-performance wording, and (d) inherited historic citations with weak or wrong locators. Use available primary PDFs in `Academics/BEP/Catalysis/Articles/`, the original proposal and bibliography, existing source ledger and PDFs before searching outside. New high-value public papers may be added with separate source identity and correct access status.

Known issues worth preserving and checking, not automatically resolving: Berger DOI mismatch (previously corrected), Urmès 2019 `K1` internal discrepancy, Borodziński ranges/units, Pd–Mn mechanism qualification, Dehghani rate/decay-basis conflicts, and inherited claim attachments without an inspected source span. Beware direct-periodic Urmès 2022 abstract not demonstrating optimization gain for target PdAg. No measured target-model fitting, waveform optimum, periodic improvement, or human source approval is established.

## Independent re-audit and context-compaction resilience

Run persistent batches/waves according to [EXECUTION_PLAN.md](EXECUTION_PLAN.md); update the GitHub audit ledger and checkpoint **as you work**, not only at the end. After a substantial context reset/compaction, every new session must reload the actual YAML and audit ledger; source reopening, not trusting AI summaries, is required.

The final second pass must **reopen evidence passages and re-evaluate substantive claims independently from previous AI conclusions**. Use explicit outcomes: `supported_under_scope`, `partially_supported`, `contradicted`, `misattributed`, `unverifiable_with_access`, `derivation_checked`, `needs_human_review`. Track changes with before/after text and reason. A same-agent re-audit is not a human review.

## Delivery constraints

Start from the **latest** `work/bep-integrated-reference-map-v1-20261022` and create a *fresh* research branch targeting that exact branch with an **unmerged PR**. Keep source graphs, migration histories and original app intact. **Do not merge PR #180, PR #182, or the new PR**. Do not build the frontend, refactor parser, or write a new general taxonomy; this is scientific DATA and evidence work.

Place work under `Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/citation_audit/` on the new branch. Create a stable machine-readable passage/quote ledger, source-access index, claim correction/disposition log, audit/checkpoint file, methodology and validation report. Existing graph claim records may be narrowly updated with corrections/references, but retain provenance and stable IDs.

Acceptance: every current claim reference is either **source-anchored**, **derivation-backed**, or **explicitly unresolved with the exact reason**; source-level and citation-level access limits are truthful; full inventory counts and coverage by evidence class are reported; independent second-pass sample/review plus recovery procedure are documented; no scientific or human verification is fabricated. If this cannot be completed in one Work execution, **deliver the completed validated waves** and a precise, executable remaining queue instead of calling it finished.

Record source/quotation coverage, claim corrections, conflicts, inaccessible documents, validation errors, Git diffs/commit links and open PR URL. Test schema/reference integrity but explicitly distinguish structural validity from scientific truth.
