# Damian check-in — Monday 19 October 2026

**Status:** working checklist (owner-facing; not sent to Damian).  
**Purpose:** make tomorrow's short in-person conversation useful, clear the laboratory onboarding blocker, and decide the immediate experimental/modelling next step.  
**Last updated:** 18 October 2026.  
**Evidence convention:** `[REPORTED]` = user statement; `[RECORD]` = correspondence/project dossier; `[ASK]` = still to verify with Damian or Els.

## P0 — Complete the BSc BEP application form **now**, before the lab visit

- [ ] Open [Brightspace](https://brightspace.tudelft.nl) → **Eindprojecten Administratie TNW** and retrieve the current **BSc BEP application form** (official route cited by [TU Delft TNW FAQ](https://www.tudelft.nl/studenten/faculteiten/tnw-studentenportal/organisatie/studieadviseurs/faq-studieadviseurs)).
- [ ] Check the **actual file and version** and confirm it is the form requested by **Els Arkesteijn (CaSE)** in her 14 September email. This is distinct from the Mathematics double-BEP committee agreement **TWN3002-24** and any ChemE confidentiality/IP agreement.
- [ ] Fill in only verified personal and project details. **Confirm any supervisor/committee fields and signatures rather than guessing.** Earlier working dates *14 Sep 2026–28 Feb 2027* remain **unconfirmed** for the actual form.
- [ ] Arrange required signature(s); send the completed signed form to Els at `Secr-CaSE-TNW@tudelft.nl` in the correct reply thread. **Do not claim sent until done.**
- [ ] Record the real form filename/version, submission and any reply in the BEP dossier. Do not commit sensitive filled student forms by default.

**Why this blocks access** — [RECORD, Els email 14 Sep]: Els needs the form details to enrol the student in **Lab Servant** → student completes safety quizzes (TU Delft VPN when off-campus) → after **Servicepunt** email student updates the campus card → building 58 / student desk access is activated. **Laboratory access has a separate requirement**: attend a **guided lab tour first**, then Els arranges access to the relevant labs. **No present lab authorisation has been verified.** `[REPORTED]` User has already emailed Els, but filing/submission and access are not confirmed.

## Monday — topics to bring to Damian

### 1. Catalyst / experimental materials

- [ ] **[ASK]** “Has the catalyst arrived / is it available now? How is that progressing?” **Receipt is not independently verified; do not state it has arrived as fact.**
- [ ] **[ASK]** Which actual catalyst/batch, support, amount, condition, and characterisation will be used? Is it the same material and kinetic regime as in the reference literature?
- [ ] **[ASK]** What experiment could we realistically run first once access is arranged, and what data can I already inspect in the meantime?

### 2. Lab entry and induction

- [ ] Tell Damian that the CaSE email has already been sent, but the **signed BSc form still needs completing/submitting**.
- [ ] **[ASK]** Can we schedule the required **guided lab tour**, and who should be contacted for the final lab-area authorisation?
- [ ] **[ASK]** Which parts of the set-up/data can be inspected with supervision while independent lab access is pending? Never assume independent access.

### 3. Actual BEP scientific progress — brief and defensible

- [ ] State, in own words, the research question: transient/periodic feed manipulation in packed-bed acetylene semi-hydrogenation, and whether it changes conversion and ethylene selectivity relative to an appropriate steady-state baseline.
- [ ] Explain **what was derived, what was implemented and what was tested**. Show the source equations, numerical method and real notebook/code if asked; no “AI slide” substitute for a scientific argument.
- [ ] Separate *an initial reacting simulation* from a **validated model**. No verified experimental selectivity gain or robust periodic optimisation result is established.
- [ ] **[ASK]** Which actual measurements, kinetic parameters and reactor/catalyst details can be made available to calibrate/validate the simulation?
- [ ] **[ASK]** Which concrete deliverable would Damian like next: baseline comparison, model audit, operating-condition sweep, or proposed first experiment? Agree one small checkable next step.
- [ ] **[REPORTED SENT, 15 Oct]** Urmès (2019, 2022) references were emailed to Damian already; **do not resend automatically**. Ask whether he has had a chance to look, if relevant.

### 4. Before leaving

- [ ] Record **catalyst status**, **lab-tour date/owner**, **required form signatures**, **first experiment or data source**, **one next scientific deliverable**, and **date for the next check-in**.
- [ ] Log any confirmed decisions in the BEP `state.md` and `history.log` (not in the checklist as facts before confirmation).

## Revised availability (week 19–23 October, Europe/Amsterdam)

| Day | BEP / campus availability |
| --- | --- |
| Monday 19 Oct | Morning until 12:45; return from about **14:00** |
| Tuesday 20 Oct | Morning until **15:00** |
| Wednesday 21 Oct | **From about 14:00** (new availability) |
| Thursday 22 Oct | **15:00–17:00** for BEP; **14:15–15:00** separate NB1420/NB2410 in-person TA meeting with Nina in building 58 |
| Friday 23 Oct | **From about 14:00** (new availability) |

**[REPORTED]** Wednesday and Friday afternoons supersede the earlier “not available” statements. Calendar placeholder end times at 18:00 on days with no stated end **do not define a promised departure time**. Check and send the updated availability to Damian; a draft is not a sent message.

## Short English check-in prompts

- “I wanted to give you a proper update on what I have actually built and validated, rather than relying on the slides I sent.”
- “Has the catalyst arrived yet? What’s the status of the experimental setup?”
- “I still need to complete the signed BSc form for Els, so I don't want to assume I have lab access yet. Can we arrange the guided lab tour?”
- “What would be the most useful concrete result for me to bring you next?”

## Source trail

- [Els administrative thread](../../thread_els_arkesteijn.md) — exact 14 Sep email, form request, Lab Servant, safety quizzes, badge and lab-tour requirements
- [BEP forms register](../../Dossier/bep_application_forms_register.md) — actual current form/version and signatures still unverified
- [BEP handoff, 16 Oct](../../HANDOFF_2026-10-16.md) — sent-mail assertions, scientific caveats and unresolved items
- [Damian / Zoë thread](../../thread_zoe_damien.md) — supervision communications and research context
- [Modelling state](../../3_Model/state.md) — model audit and defect history; **not** proof of validated periodic gain
