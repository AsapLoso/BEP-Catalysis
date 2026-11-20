# Saturday follow-up scanner / state audit — preflight 2026-10-15

## Mandate and boundary

**[USER-DECISION, 2026-10-15]** Reconsolidate the ROOT, the BEP state, relevant BEP child-state files, and master/sub-Wayfinder decision maps this weekend. **Target [DUE: 2026-10-17] (Saturday)**, internal target rather than an external institutional cutoff. The objective is a `/follow-up` result that actually exposes every applicable active BEP action and external wait without resurrecting completed tasks or treating decisions on Wayfinder maps as executable to-dos.

**This is a static source inspection, NOT a full executed scanner regression.** Run a clean-worktree `python .agents/triage/scan.py Academics/BEP/Catalysis` and a ROOT/global scan on Saturday, inspect the generated `.agents/triage/follow_up_scan.txt`, and attach before/after evidence. Do **not** run optional calendar/YT sync hooks without their own permissions.

## Inspected code and sources

- `.agents/skills/follow-up/SKILL.md`: scan is intentionally **restricted to files named `state.md`**, with subtree recursion. `research/wayfinder/*.md` files are **not scanned directly**. Decisions/tickets that require action need an explicit, dated `- [ ]` mirror in the owning `state.md`, possibly rolled up to ROOT `task.md`. The actual scanner to verify is `.agents/triage/scan.py`, not merely the older example embedded in the skill.
- `state.md` (ROOT): 38 unchecked and **2 checked** checkboxes at inspection, plus many other task styles. The root 'Open Communication Lines' heading originally omitted the `⏳` token expected by the actual parser and said 'None', despite outstanding BEP waits and a separate `task.md` table. A subsequent repair must test that external lines are actually emitted by `scan.py`.
- `Academics/BEP/Catalysis/state.md`: ~68 unchecked checkbox actions at inspection, including inherited child-task mirrors; status and external lines present. Previously contained stale Els 'NIET VERZENDEN' to-do entries despite confirmed sent mail. **The two stale Els outbound checkboxes and blocker status were pruned on 15 October**, preserving the unknown form-delivery status.
- `Academics/BEP/Catalysis/3_Model/state.md`: 9 unchecked actions; **older 'scaffold with zero constants' text may not describe the newer live model branch**. This is a freshness/reconciliation issue, not a claim that 9 code defects still exist.
- `Academics/BEP/Catalysis/2_Courses/PDC/state.md`: 10 unchecked actions; the dated 22 October course submission remains a real cutoff in these records, independent from this admin task.
- `Academics/BEP/Catalysis/research/wayfinder/bep_catalysis_master.md`: 27 unchecked frontier tickets and 33 checked decision/fact entries. They are decision-map records, **not automatically actionable scanner tasks**.
- `Academics/BEP/Catalysis/research/wayfinder/scientific_method_selection.md`: 9 unchecked tickets; not directly scanned.
- `Academics/BEP/Catalysis/research/wayfinder/bep_presentation_2026_10_14.md`: 8 unchecked tickets (the date is now past); do not automatically carry 'Wednesday delivery' as an imminent hard deadline. Investigate whether the map should be closed, archived, or retain genuinely live work.

## Reproducible parser defects to check first

1. **Completed-checkbox false positives.** In the actual `scan.py`, `open_tasks = re.findall(r'^[ \\t]*- \\[[ xX/ ]\\] (.*)', content, flags=re.MULTILINE)` **discards the checkbox token**, then filters `not t.lower().startswith('[x]')`. As ordinary completed lines start with a task description rather than `[x]`, they will incorrectly appear as `- [ ]` in the report. The skill's embedded sample has the same structural bug. Unit-test with one `- [x] Done` and one `- [ ] Open` first.
2. **Scope mismatch:** Wayfinder map files are neither named `state.md` nor parsed by `scan.py`. Decide **which map frontier tickets should become real active work**, avoid indiscriminately mirroring every grilling or conditional item, and ensure each approved active actionable item has a temporal anchor in BEP `state.md`.
3. **External-wait visibility:** actual table regex looks for heading `## ⏳ Open Communication Lines` followed by a Markdown table. The ROOT heading used no hourglass and its body was 'None' (while elsewhere active correspondence existed), so root-only scans could silently miss waits. Project BEP table has a compliant heading/table; still validate **actual extracted rows**, including Damian's promised BEP form.
4. **Stale state:** older project and child status blocks, especially completed/retracted research, risk falsely presenting a non-reacting scaffold or completed October-14 presentation deadline as active. Compare with latest source receipts, history and other branches; do not blindly flip technical claims.
5. **Meta directives / snooze:** check `<!-- SNOOZE: until YYYY-MM-DD -->` and `<!-- META: ... -->` semantics against `SKILL.md`. A map's own 'status' prose does not count as a `state.md` field.
6. **Scoping:** verify that `.agents`, archive, scratch, 0_Project_Management are intentionally excluded; don't assume a child `state.md` in an excluded directory will appear. Use the correct project-scope scan rather than pulling in unrelated repositories.

## Completion tests — Saturday

- Run and inspect the exact script for ROOT/global and BEP-specific inputs, without triggering unrelated state-sync hooks.
- Reproduce, fix and test completed-checkbox false positives; add a regression test in the proper test location if available.
- Compare actual counted active checkboxes, parsed external waits, blockers, snoozes and vetoes against expected/approved records. Do not claim a complete audit from a source-only spot-check.
- Crosswalk BEP master and relevant submap frontiers with BEP `state.md`, then ROOT `task.md`. Mark each open item `active / conditional / research / requires user decision / archived`; carry only actionable ones into scanner-readable state. Keep one-goal-per-map and don't destroy history.
- Reconcile the currently uncertain committee TW3 selection (Neil not confirmed; Yves same Mathematical Physics section as Zoë and no exception desired), the Els/Damian admin follow-up, and any stale pre-presentation statuses.
- Record before/after receipts in project `history.log`, and use scoped commits. Preserve user decisions, do not send emails or alter grading data.

## Navigation

- [ROOT state](../../../../../state.md) · [ROOT task tracker](../../../../../task.md)
- [BEP state](../../state.md) · [BEP history](../../history.log)
- [BEP master map](../wayfinder/bep_catalysis_master.md) · [Scientific selection map](../wayfinder/scientific_method_selection.md) · [Presentation map](../wayfinder/bep_presentation_2026_10_14.md)
- [Follow-up skill](../../../../../.agents/skills/follow-up/SKILL.md) · [Actual scanner](../../../../../.agents/triage/scan.py)

## 2026-10-15 correction: checkbox defect implemented, broader audit still open

- Scanner regex repaired in default-branch `.agents/triage/scan.py`; checked items are separately enumerated as evidence candidates, never silently converted into active `- [ ]`.
- `.agents/skills/follow-up/SKILL.md` Step 2b now requires checking primary sources and logging to the owning history **before** pruning checked task mirrors. The scanner's illustrative older regex was also corrected in the skill.
- A source-driven re-parse of ROOT/BEP and two known BEP child state files shows zero completed boxes presented as active; results and provenance in `../../../.agents/triage/checked_reconciliation_2026_10_15.md` from repo root (canonical relative link: [ROOT evidence receipt](../../../../../.agents/triage/checked_reconciliation_2026_10_15.md)).
- Regression tests committed; authenticated remote Python execution unavailable, so live suite and full project-wide scanner proof **not** claimed. Complete project status reconciliation remains an open Saturday task.
