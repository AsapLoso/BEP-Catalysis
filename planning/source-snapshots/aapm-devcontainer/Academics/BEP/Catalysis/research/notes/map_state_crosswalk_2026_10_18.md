# Map→state-crosswalk — 18 oktober 2026

**Opdracht:** [follow_up_audit_2026_10_15.md](follow_up_audit_2026_10_15.md) §Completion tests, punt 4 — "Crosswalk BEP master and relevant submap frontiers with BEP `state.md`, then ROOT `task.md`. Mark each open item active / conditional / research / requires user decision / archived; carry only actionable ones into scanner-readable state. Keep one-goal-per-map and don't destroy history."

**Bereik.** Masterkaart (27 frontier-tickets), `scientific_method_selection.md` (9), `bep_presentation_2026_10_14.md` (8). Buiten bereik: de Damian-briefingkaart (eigen frontier, al begrensd in `state.md` §2026-10-08) en de geparkeerde numerical-accuracy-kaart (`state.md` §PARKED).

**Methode.** Elk open item 1-op-1 geclassificeerd (Rule 33) in de vijf klassen van de auditnotitie. Spiegelregel: alleen `active` en **nu actionable** `requires user decision` worden scanner-leesbaar (`- [ ]`) in `state.md`; `research`, `conditional` en gedeferde beslissingen blijven op de kaart. Dat is geen verberging: `state.md` §"Directe acties — uit de frontier" linkt naar de volledige kaart, en deze crosswalk legt per ticket vast waarom het wel of niet spiegelt. De scanner leest geen kaarten; de kaart leest de scanner niet — de wederzijdse pointer is het kanaal.

**Uitkomst.** Master: 27 → 25 open (`I1-10` opgelost, `I3-04` vervallen); 14 gespiegeld, 11 kaart-only. Scientific: 9/9 kaart-only (research/conditional/HITL-gedeferd). Presentatie: 8 tickets gearchiveerd als historisch record; 2 live restpunten nieuw als checkbox in `state.md`.

> Regelnummers gelden voor de bestanden **vóór** de edits van deze pass; de mirrors zijn per ticker-ID traceerbaar.

## 1. Masterkaart — [(bep_catalysis_master.md)](../wayfinder/bep_catalysis_master.md)

| Ticket | Onderwerp | Klasse | Spiegel / bewijs | Actie |
|---|---|---|---|---|
| I1-01 | Appendix E.1–E.3 leesbaar & admissible | research | `state.md` "Appendix E … als afbeelding lezen" | kaart-only; mirror bestaat |
| I1-02 | Appendix F geometrie/solver/tolerantie | research | `state.md` Appendix F-bullet | kaart-only; mirror bestaat |
| I1-03 | `u_s`/ε-ambiguïteit | research | FW-1-bullet | mirror bestaat |
| I1-04 | bulk-vergelijking: welk artefact overleeft | requires user decision | FW-2-bullet | mirror bestaat |
| I1-05 | readsorption/TPD-scope | requires user decision | FW-7-bullet | mirror bestaat |
| I1-06 | filmclosure | requires user decision | FW-8/FW-9-bullets | mirror bestaat |
| I1-07 | report-gate vóór cijfers in de thesis | conditional (schrijffase) | — | kaart-only; wordt actief bij schrijven |
| I1-08 | kinetiekbron-policy als E onleesbaar blijft | conditional (I1-01) | — | kaart-only |
| I1-09 | plug-flow vs. Danckwerts | requires user decision | "plug-flow vs. Danckwerts"-bullet | mirror bestaat |
| I1-10 | 13-vs-14-telling | archived | `state.md:112` gecorrigeerd 13→14 | ticket gesloten; bullet gepruned |
| I1-11 | acht UNVERIFIED-claims | research | FW-14-bullet | mirror bestaat |
| I2-01 | canonieke thesisbron | requires user decision — gedeferd (schrijffase) | — | kaart-only |
| I2-02 | unpublished divergence | conditional (I2-01) | — | kaart-only |
| I2-03 | supervisieclaim in publieke metadata | conditional (I3-01) | — | kaart-only |
| I2-04 | ontbrekende `content/Detail3.md` | active (mechanisch) | I2-04-bullet | mirror bestaat |
| I3-01 | TNW draft fields user-provided; TW3 seat open | formal appointment/approval unverified; TW3 selection still requires user decision | state I3-01/TW3 bullet | current mirror exists |
| I3-02 | locate exact user-reported ruling text | active archive-source task; no new external request under Paula hold | new state archive-gap bullet | current mirror added |
| I3-03 | reconcile submitted constructions against the located ruling | dependent on I3-02 source text | no new choice until ruling scope is read | map-only |
| I3-04 | Els-mail: wat blokkeert | archived | user-reported verzending 13/15-10 (`state.md` §STATUS RECONCILED) | gesloten; restpunten in nieuwe ADMIN-checkboxes |
| I3-05 | verlopen 2026-09-29-doelen | requires user decision | §Doeldatum verstreken + **nieuwe checkbox** | nieuw mirror |
| I3-06 | ontbrekend bewijsbestand | active (mechanisch) | I3-06-bullet | mirror bestaat |
| I4-01 | formal slots on current TNW/TWN forms | user-selected draft fields recorded; current form, eligibility and Board approval remain open | state Roel/form-review bullets | mirrored |
| I4-02 | historical DCSC/Carlas second-corrector route | superseded by user-selected TNW draft fields; informational closure remains open | SysCon state / task follow-up | mirrored |
| I4-03 | ruling scope for physics-side supervision | depends on I3-02 source text; user reports ruling exists | map-only research item | pending |
| I4-04 | DCSC-scope | requires user decision — gedeferd (HITL; kaart: "agent must not answer this") | — | kaart-only; DCSC-backlogbuls dekken alleen de verkenning |
| I4-05 | overlegcadans | requires user decision (geblokkeerd I3-01) | "Overlegfrequentie"-bullet | mirror bestaat (legacy anker) |
| I4-06 | PDC-koppeling | active | PDC-cursustrack-bullets | mirror bestaat |

**Telling:** 27 = 2 archived + 17 gespiegeld + 8 kaart-only (I3-02, I4-01 en I4-02 zijn nu gespiegeld). De kaart-only-items zijn geen vergeten taken: hun beslissing/threshold is nog niet actionable (upstream gate, schrijffase of expliciete HITL-deferral), en de kaart zelf blijft via `state.md` §frontier gelinkt.

## 2. Scientific map — [(scientific_method_selection.md)](../wayfinder/scientific_method_selection.md)

| Ticket | Onderwerp | Klasse | Spiegel / bewijs | Actie |
|---|---|---|---|---|
| SM-1 | acetylene-mechanismetransfer | research | — | kaart-only |
| SM-2 | welke voorspellingen het bewijs draagt | research | — | kaart-only |
| SM-3 | herbruikbare implementatie (executed evidence) | research | — | kaart-only |
| SM-4 | coherente conservatie (executed evidence) | research; closure-keuze loopt via master I1-04/I1-06 | — | kaart-only |
| SM-5 | predictie-acceptatietarget | requires user decision (owner+supervisors) — gedeferd | — | kaart-only |
| SM-6 | verification-corpus | research | — | kaart-only |
| SM-7 | is de impliciete route toereikend | research (conditional op SM-1/4/5/6) | — | kaart-only |
| SM-8 | methodology-package selectie | requires user decision (HITL) — gedeferd | — | kaart-only |
| SM-9 | eerlijke optimalisatievergelijking | conditional (I4-04) | — | kaart-only |

De kaart legt zelf vast dat de state-link gedeferd is (de kaartmissie mocht geen state-engine-bestanden aanraken, §6). Geen enkel SM-ticket is nu scanner-actionable; geen mirror toegevoegd om de state niet te vervuilen. De SM-beslissingen blijven bereikbaar via de masterkaart-link.

## 3. Presentatiemap — [(bep_presentation_2026_10_14.md)](../wayfinder/bep_presentation_2026_10_14.md)

| Ticket | Onderwerp | Klasse | Bewijs / reden |
|---|---|---|---|
| W1 | audience en purpose | archived | eventdatum verstreken; levering niet op schijf (UNVERIFIED) |
| W2 | duur en format | archived | 9½-min-toewijzing vastgelegd; vereiste moot |
| W3 | evidence-backed content | archived | claim/source-ledger + M-review zijn de blijvende artefacten |
| W4 | contentprioriteit | archived | voorlopig tien-slide-verhaal staat |
| W5 | narratief | archived | concept-arc staat |
| W6 | visuele aanpak | archived | checkpoint-deck levert de gevraagde "verzendbare" deck |
| W7 | ready-to-present-standaard | archived | geen repetitieverslag; achterhaald |
| — | "Format is not ratified" (beslissingenlijst) | archived | HTML-deck bestaat; formatvraag moot |

Live restpunten **na** de checkpoint-integratie (geen W-tickets): owner-review (narrative 05, compressie, closing, slide 10) en de Zoë F/G-discussievoorbereiding. Beide zijn nu scanner-leesbare `- [ ]` in `state.md` §"BEP presentation — reconciled status".

## 4. ROOT `task.md`-reconciliatie

- **L9** P0-presentatie: herschreven — kaartdatum verstreken, leveringsstatus UNVERIFIED, restpunten naar `state.md`; kaart gearchiveerd (Rule 38: geen verstreken deadline als actief presenteren).
- **L19** zaterdag-audit: status-append; blijft open wegens restpunten (legacy-ankers, dedupe, 3_Model-versheid).
- **L25** BEP-aanmeldformulier: consistent met het nieuwe state-checkbox (ADMIN-formulier).
- **L26** Damian-document: mirror bestaat al in `state.md` (FROM 2026-10-15 ASAP).
- **L28–L30** F/G-follow-up: blijft staan; `state.md` krijgt nu de scanner-leesbare checkbox.
- **L170** Els-onboarding "2 MIN" en **L285** PRIO-0 confidentiality "NIET VERZENDEN": **gepruned** — user-reported verzonden (13/15-10). De bio/foto-constraint blijft geborgd in `thread_els_arkesteijn.md`, `state.md` §STATUS RECONCILED en de nieuwe ADMIN-verificatiecheckbox.
- **L297** "14 openstaande punten": ✓ consistent met de gecorrigeerde `state.md:112`.
- **L352** Els-mail sent-regel: ✓ consistent.
- Niet aangeraakt: BEP-blok L288–L296 / L314 (3_Model-versheid — zie §6). Duplicatie state↔task is bewust (Rule 22/5.4), geen defect.

## 5. Toepassingen deze pass

**`state.md`:** `:112` 13→14; I1-10-bullet gepruned; **+5 checkboxes** (owner-review, F/G-discussie, I3-05-herijking, ADMIN-Els-verificatie, ADMIN-BEP-formulier); Neil-rij TW3 → optie/niet bevestigd; frontier-kop 27→25 + crosswalk-link; zaterdag-auditbullet status-append.

**`task.md`:** L9 herschreven; L19 status-append; L170 + L285 gepruned.

**Kaarten:** master `I1-10` + `I3-04` gesloten met datumnotitie; master telnoot 25 open; scientific crosswalk-noot; presentatie archiefblok.

## 6. Restpunten (buiten deze pass)

1. **3_Model-versheid** — `state.md` §2026-10-13 SESSION (gates C–E open) vs §INTERIM (D4a/b gefixt; uniform-pellet weerlegd; `resolve_radial` default, run niet afgemaakt); `task.md:294-296/314` weerspiegelt de oudere scaffoldstand. Vereist een eigen reconcile tegen `3_Model/state.md`.
2. **Legacy-ankers** — `[DEZE WEEK]`/`[DONSDAG]`-vormen in `state.md`/`task.md` (o.a. de I4-05-mirror) zijn niet Rule 23-conform; normaliseren.
3. **scan.py:88 OCL-regex** — onbegrensde skip vangt `## Defect register` als communicatielijnen (8 valse rijen in de BEP-scan); fix + regressietest vereist.
4. **Statusvormen** — PDC (geen Status-regel) en `Articles/reader/state.md:3` (`Status:` zonder dash/bold) tellen als "No explicit status"; rapport-only.
5. **I3-04-restdetail** — welke bijlagen/ondertekeningen ooit zijn aangekomen is niet vastgesteld; de nieuwe ADMIN-checkbox dekt de navraag.
6. **Presentatielevering** — of het woensdaggesprek heeft plaatsgevonden staat nergens op schijf (UNVERIFIED); de kaart is daarom als *event record* gearchiveerd, niet als "afgerond".
7. **Duplicate-hygiëne `task.md`** — BEP-blok L285–L314 dupliceert `state.md` bewust; alleen echte stale items (L170/L285) zijn gepruned.

## 7. Verificatie

- `pixi run python .agents/triage/scan.py Academics/BEP/Catalysis` → verwacht **111 actieve blokken** (107 + 5 nieuwe − 1 gepruned), 0 checked, 10 open lines, 0 snoozed.
- `pixi run python .agents/triage/scan.py` → verwacht **750 actieve blokken** (746 + 5 − 1), 27 checked, 75 open lines, 71 snoozed.
- Receipts: `scratch/followup_audit/scan_bep_final.txt`, `scan_global_final2.txt`; `git status` mag alleen de bedoelde BEP-/task.md-paden tonen.
