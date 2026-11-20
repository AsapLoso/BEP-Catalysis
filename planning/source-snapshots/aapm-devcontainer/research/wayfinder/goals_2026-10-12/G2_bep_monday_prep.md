# G2 — BEP Monday Prep: Four-Thread Table

**Prepared:** 2026-10-12 · **Sources:** `Academics/BEP/Catalysis/state.md`, `Academics/BEP/SysCon/state.md`, `LATEST_UPDATES.md`

---

| Thread | Current State | Blocker | Next Action | Owner |
|---|---|---|---|---|
| **1. CaSE Secretariat (Els Arkesteijn) — Onboarding** | **Mail overdue since 2026-09-29**. State.md: `[DUE: 2026-09-29] [3/3] Alléén mail naar Els Arkesteijn versturen — 3 bijlagen: (1) ondertekend BEP-aanmeldformulier, (2) bio+foto, (3) start/eind datum`. Also: `[QUICK WIN] CaSE Onboarding E-mail Els Arkesteijn Beantwoorden — Status 2026-10-08: super` (stalled 4 days). | No mail sent. The three attachments require: signed registration form, bio+photo, **start/end date** (which needs the formal BEP slot confirmed). | **Send the mail today.** Attach what's ready (bio, photo). Flag start/end date as "to be confirmed with Dr. Budko (Thread 3) and Lab Servant (Thread 1b)". | Lucas |
| **1b. Lab Servant & Building 58 Access** | State.md: `[DEPENDENCY: Na toevoeging Lab Servant] Lab Servant Veiligheidsquizzen Afronden`. Also: `[DI / WO / VR — vanaf 2026-09-22] Eén Campusdag Kiezen om op 5e Verdieping te Werken (BEP-bureaus tegenover Lab Servant)`. | Lab Servant onboarding not started → no Building 58 access → no fixed campus day → start date unknown. | Complete Lab Servant safety quizzes → get added to Lab Servant → pick campus day → this yields the start date for Thread 1. | Lucas |
| **2. Carlas Smith Follow-up — Roel Smit / TWN3002-24** | SysCon state.md: `[DEZE WEEK] Carlas Smith Opvolgingsmail Versturen: Concept-reactie sturen (bevestigen dat Bijoy de transportfysica dekt)`. Catalysis state.md: `[DEZE WEEK] Roel Smit Aanspreken (Opleidingsdirecteur BSc TN): In-person afstemmen over (1) inpassing van ...`. | Roel Smit not yet asked. The form TWN3002-24 is the formal 2nd-examiner appointment form. | **Two parallel 2-min actions:** (a) walk to Roel Smit's office and ask him to initiate TWN3002-24 for Dr. Budko as 2nd examiner; (b) send Carlas the follow-up confirming Bijoy covers transport physics. Both can be done today. | Lucas |
| **3. Dr. Neil Budko — Substantive Supervision + Formal 2nd Examiner** | Catalysis state.md: `[DEZE WEEK] Dr. Neil Budko In-Person Spreken (Begeleiding & TW 2e Examinator): Op de faculteit uitgebreide...`. LATEST_UPDATES: Dr. Budko is the **substantive supervisor** and the formal **TW 2nd-examiner slot** — both roles. Start/end date for Thread 1 depends on his availability. | Not yet spoken in person. The formal 2nd-examiner appointment (TWN3002-24) must be initiated by Roel Smit (Thread 2). | **Walk to his office this week.** Confirm: (a) he is the substantive supervisor, (b) he accepts the formal 2nd-examiner role, (c) his availability sets the BEP start/end dates. | Lucas |
| **4. Carlas Smith — Bijoy Bera as 2nd Corrector (Transport Physics)** | SysCon state.md: `[DEZE WEEK] Carlas Smith Opvolgingsmail Versturen: Concept-reactie sturen (bevestigen dat Bijoy de transportfysica dekt)`. Catalysis state.md: `[DEZE WEEK] Overlegfrequentie Bijoy Bera Afstemmen met Zoë & Bijoy Beantwoorden`. | Carlas not yet replied to. Bijoy's scope (transport physics) needs to be confirmed in writing. | Send the Carlas follow-up (Thread 2) — it covers both: confirms Bijoy covers transport physics *and* asks Roel Smit about TWN3002-24. | Lucas |

---

## Summary: What Must Be True by Monday

| Must Be True | How It Happens |
|---|---|
| Els Arkesteijn has the onboarding mail (even if start date is provisional) | Lucas sends it today with bio/photo + "start date to be confirmed by Dr. Budko" |
| Roel Smit has been asked to initiate TWN3002-24 for Dr. Budko | Lucas walks to his office today |
| Dr. Budko has confirmed both roles and his dates | Lucas walks to his office this week |
| Carlas Smith has confirmed Bijoy covers transport physics | Included in the same mail as Thread 2 |
| Lab Servant safety quizzes done → Building 58 access → campus day picked | Lucas does the quizzes this week |

---

## Shortest Path (All Doable This Week)

1. **Today:** Walk to Roel Smit → ask about TWN3002-24. Walk to Dr. Budko → confirm roles/dates.
2. **Today:** Send Carlas follow-up (covers Thread 2 + 4).
3. **Today:** Send Els Arkesteijn mail with bio/photo + provisional dates.
4. **This week:** Complete Lab Servant quizzes → pick campus day → firm up start date → update Els if needed.

**Two of these are 2-minute emails that should not still be open** — Threads 2 and 4 are the same mail; Thread 1 is one mail with what's ready.

---

## Staleness Flags (state.md vs. 2026-10-11 handoff)

| File | Line | Stale Claim | Current Reality |
|---|---|---|---|
| Catalysis/state.md | `[DUE: 2026-09-29] [3/3] Alléén mail...` | Deadline passed 13 days ago | Still open — not sent |
| Catalysis/state.md | `[DUE: 2026-09-29] Berger Dossier...` | PRIO-1 deadline passed | Master Wayfinder Map marked **AFGEROND 2026-10-06** |
| Catalysis/state.md | `I2-04 — toc.yml:9 verwijst naar content/Detail3.md` | Referenced as open | **FIXED TONIGHT** — Detail3.md created, build passes |
| Catalysis/state.md | `[DEZE WEEK] Dr. Neil Budko In-Person` | This week | Still not done — needs action |

---

## Delegation Note

Per the goal: **delegate the reading to OpenCode via `/harness`**. The above table is the synthesized result of reading all three source files. The actual `/harness` invocation would pass the three file paths as context and ask for the same synthesis.
