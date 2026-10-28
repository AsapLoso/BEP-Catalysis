---
name: session-handoff
description: >-
  Capture a session and route every residue to its permanent home, so a chat tab can be
  closed without losing context. Use when the user says "handoff", "hand it off", "wrap
  up", "I can close this tab", "save this session", or asks what is still open before
  switching chats. Routes decisions and in-flight work to state.md, vetoes and
  corrections to conventions.md with a mandatory linked state.md veto bullet, drafts to
  thread_<person>.md, unsent commitments to state.md as active items, and speculation to
  an untracked .agents/quarantine/. Prints an explicit NOT-CAPTURED list and machine-checks
  its own writes. Manual and user-invoked; there is no automatic trigger, and the chat
  footnote is never the record.
---

# Handoff — capture a session and route its residue

**Role:** Make a chat tab safely closable. Everything said this session that matters later
must end up in a file, in the right file, before the user closes the tab.

**This is not a summary.** A summary is what the next session reads. The point is that the
next session does not have to trust a summary — it reads the same permanent files it would
read had the tab never been closed.

## Overview

Rule 28 §5.6 defines this mechanism. Read `.agents/AGENTS.md` §5.6 points 4-8 before
executing; this skill implements it and does not restate the rules.

Cite rules by **number** (`Rule 26`, `Rule 38`), never by line number — §5.6 is edited
frequently and line anchors into it silently rot.

| Tier | Destination | Contents |
|---|---|---|
| 1 — Permanent | `state.md` · `conventions.md` · `history.log` · `task.md` · `thread_<person>.md` | decided, actionable, or standing |
| 2 — Quarantine | `.agents/quarantine/<YYYY-MM-DD-HHMM>-<slug>.md` — **untracked** | speculation, unverified, unplaceable |
| 3 — Pointer | one `##` heading line in `LATEST_UPDATES.md` | session id, counts, path |

## Workflow

### 1. Identify the session — conservatively

The session id is **not** in your context. Recover it from `opencode.log`:

```powershell
$log = Join-Path $env:USERPROFILE ".local\share\opencode\log\opencode.log"
Select-String -Path $log -Pattern 'message=stream .*mode=primary' | Select-Object -Last 5
```

> **[!IMPORTANT] The key is `session.id=` (dotted), not `sessionID=`.** The filter above is
> correct, but the skill never said how to *extract* the id, and the natural guess is wrong.
> On 2026-10-03 an agent reached for `sessionID=` and got zero hits across the whole log.
> Verified real line:
>
> ```
> timestamp=2026-10-03T15:04:44.550Z level=INFO run=8b759d6c message=stream providerID=opencode
> modelID=space-bunny-free session.id=ses_efdba550bffe3C8DAQdoGjmbno small=false agent=worker mode=subagent
> ```
>
> Extract with: `[regex]::Match($_.Line, 'session\.id=(ses_[0-9a-zA-Z]+)').Groups[1].Value`
>
> **The documented filter is also much less reliable than stated.** A 4-minute sample of the
> live log contained **six distinct subagent `session.id` values** interleaved line-by-line.
> With a fan-out of four, "most recent" is close to coin-flip, and the `session-id: AMBIGUOUS`
> path below is the *expected* outcome rather than the exceptional one. Treat AMBIGUOUS as
> normal, not as an error to route around.

Constraints that matter, each learned from a real failure:

- **Require `message=stream`.** Lines reading `message=evaluated permission=bash …` echo
  *your own command text* and match any grep you write. Grepping for your own pattern will
  return your own query — check that the line is a stream record before trusting it.
- **Do NOT filter on `agent=build`.** The primary agent's role varies by session: this
  workspace runs `orchestrator`, `plan`, and `build` as primaries. A `build`-only filter
  returns whichever *other* tab last used that agent, which is a different session. On
  2026-09-30 that filter would have filed this session's residue under a neighbour's id.
- **Exclude `agent=title` and `agent=compaction`.** Both emit `mode=primary` while carrying
  *another* session's id.
- **Never use `run=`.** Shared by every session in the app instance.
- **Never use `parentID=`.** It appears only on `message=created` lines, never on the
  `message=stream` lines you are parsing.
- **The log interleaves live tabs line-by-line.** With 5+ tabs open, "most recent" is
  usually right and occasionally wrong.

The most reliable confirmation: your own turn's `messageID` (e.g. `msg_…`) and your session
id appear together on `message=process` / `message=stream` lines. If you already know any
message id from this turn, grep that instead — it is unambiguous.

### 1a. Preferred method: recover the id from a child task id

**If you delegated any subagent this session, you already hold an unambiguous session id — the
`task_id` the tool returned** (e.g. `ses_f178b0fb0ffekJqHhyzcYgcQH1`). Do not go near the
interleaved stream log. Each child is created with its parent written explicitly:

```powershell
$log = Join-Path $env:USERPROFILE ".local\share\opencode\log\opencode.log"
Select-String -Path $log -Pattern 'id=ses_<CHILD_ID> ' | Select-Object -First 1
# -> ... parentID=ses_<THIS SESSION> ...
```

Confirm by checking **every** child agrees, then re-run to check the id has not moved:

```powershell
foreach ($c in @('<child1>','<child2>')) {
  $m = Select-String -Path $log -Pattern "id=$c " | Select-Object -First 1
  if ($m.Line -match 'parentID=(ses_[A-Za-z0-9]+)') { "$c -> $($Matches[1])" } else { "$c -> NONE" }
}
```

This is strictly better than stream-log scraping and should be the **first** thing tried. The
stream heuristic in Step 1 exists only for sessions that delegated nothing.

The `parentID=` prohibition in Step 1 is about **filtering** for your own stream lines, where the
field does not appear. It is not a prohibition on reading `parentID` off a `message=created`
line for a session id you already know — that is the reliable use.

**Verified 2026-10-03:** a session that had delegated three subagents resolved to
`ses_f2a649c6cffeyfvR8xBXstDToe` from their `parentID`s alone, while the `message=stream` scan
returned two interleaved candidates (`agent=plan` and `agent=build`, both `mode=primary`). The
`parentID` route needed no disambiguation heuristic and no `agent=` filter at all.

> **[!CAUTION] Never glob or recurse `%USERPROFILE%\.local\share\opencode\`.** It contains
> `auth.json` with a live Azure `key1` and a Google API key. Any broad scan writes
> credentials into tracked markdown — a Rule 27 violation. Read `opencode.log` by exact
> path. Never read `auth.json`.

**Transcript, not just the id.** The id resolved here also keys the full verbatim prompt log
in `%USERPROFILE%\.local\share\opencode\opencode.db` — every user prompt, including turns from
before a compaction (§5.6.8). Recipe, schema, pitfalls and verification one-liners: Rule 35
runbook `.agents/resources/runbooks/opencode-transcript-recovery.md`. Never report a session's
older prompts as lost to recall when the store still has them; recall is not evidence either
way (Rule 40).

**Verify before you commit to it.** Re-run the query after writing. If the id changed, you
captured under the wrong session: report `session-id: AMBIGUOUS`, name both candidates, and
do not file the residue under a guess.

**Never overwrite.** If the target quarantine filename already exists, append a numeric
suffix. Two tabs closing in the same minute must not overwrite each other — that is silent
data loss.

If no id resolves, use `session-id: UNKNOWN` and say so. Never guess.

### 2. Record the working-tree state first

Before routing anything, capture what the tree looks like:

```powershell
git status --porcelain
git log --oneline -5
```

This is not housekeeping. Contamination of the commit record by parallel sessions is this
workspace's most frequent documented defect — twice, in commits `0924b6c` and `0bba35c`,
both times a change landing in an unrelated commit where `git log` cannot find it. State in
your report which dirty paths are attributable to this session and which are not. If you
cannot tell, say so rather than assuming all of them are yours.

### 3. Sweep for residue

Work through every row. Report `NONE FOUND` so the user can see the sweep ran. **If a row has
no home, that is a routing failure, not a licence to drop it.** Do not force it into a
near-miss row, and do not park it in `NOT CAPTURED` — step 6 defines where homeless residue
goes, and it goes there.

| # | Residue | Destination | Required form |
|---|---|---|---|
| 1 | Decision made, not yet acted on | `state.md` 🔥 | `- [ ] **[DUE: YYYY-MM-DD]**` + decision + resume command |
| 2 | In-flight work, partially done | `state.md` 🔥 | one bullet per Rule 21 — the test is **one source and one verification action = one bullet**; state what exists on disk |
| 3 | **Veto / rejected path** | `conventions.md` + veto bullet in `state.md` | see Linked-Veto Rule |
| 4 | Correction the user made to prior work | `conventions.md` + veto bullet | as above |
| 5 | Standing fact, parameter, convention | `conventions.md` | Rule 26: exactly one canonical file |
| 6 | Tone / register / language for a recipient | `conventions.md` | per named person or role |
| 7 | Standing constraint ("never do X") | `conventions.md` + veto bullet | "do not X, because Y" |
| 8 | **Session-scoped** constraint ("one command at a time today") | `state.md`, not `conventions.md` | **plain bullet, not `- [ ]`** — a checkbox pins the project in the active scan and an expiry date does not make the box completable. Must carry an expiry date: a session tempo rule is not a standing convention |
| 9 | Method-level rejection ("do it via the harness, not by hand") | `conventions.md` + veto bullet | this is feedback, not a technical finding |
| 10 | Email or message draft | `thread_<person>.md` | Rule 25: log the concept draft; on send log the **exact sent version alongside it**; append to `history.log`; prune the active bullet; **and mirror a 🔥 bullet in `state.md`** (Rule 22) |
| 11 | Unsent commitment ("I'll mail X Friday") | `state.md` 🔥 with `[DUE:]` | **not** `task.md` — see Task Segregation below |
| 12 | Retraction of an earlier claim | fix **in place** + mark it | Rule 41: state what was retracted and why |
| 13 | What was *not* done | `state.md` | **two distinct cases.** Still an open loop with a blocker → keep the `- [ ]` and ADD a `- **Status:** <blocker>` line (this is what `Catalysis/state.md:24-25` does). Never to be done → prose `- **Status:**` line only, **no checkbox** — an unactionable box is clutter under Rule 2 |
| 14 | Working-tree / commit-attribution finding | `history.log` | what landed where, and what is unattributable. If it is a *finding* needing Rule 26 canonical status, it also belongs in `state.md` — `history.log` alone is a summary channel, not a finding store |
| 15 | Open question | quarantine | `UNVERIFIED` + what would resolve it |
| 16 | Speculation floated in chat | quarantine | `UNVERIFIED` + what would confirm/refute it |
| 17 | Unverifiable chat claim | quarantine or drop | "you said yesterday it was 42" has no source |
| 18 | Cross-project pointer | `LATEST_UPDATES.md` | one `##` heading line — see Step 5 |
| 19 | Discovered resource location or procedure | runbook per Rule 35 | `.agents/resources/runbooks/` |

**Task Segregation (Rule 17).** `⏳` is for **sent** messages awaiting an external reply.
An unsent draft or a stated intention to send is ball-in-**user's**-court, so it is a 🔥
item in `state.md` and only becomes a `task.md` ⏳ row once it is actually sent. The ⏳ table
has no anchor column — it wants a *sent-on* date, not a due date.

**Lifetimes.** Row 8 is the trap: a session-scoped instruction written to `conventions.md`
becomes a permanent rule that outlives its reason and misleads the next session. If it will
not be true next week, it does not belong in `conventions.md`.

### 4. Three hard rules

**Linked-Veto Rule.** A veto, correction, or standing constraint written to `conventions.md`
MUST also emit a **veto bullet** in the owning `state.md`:

```markdown
## 🚫 Vetoes & Constraints

- **Veto (2026-09-30):** no Padé approximants in the BEP — invalid for this regime. [`conventions.md`](conventions.md) §3
```

**It is deliberately NOT a `- [ ]` checkbox.** A checkbox makes `/follow-up` treat the veto
as an open task the user can never complete, and permanently pins the project in the
active scan — which Rule 2 forbids. A plain bullet under a `##` heading is visible to a
human reading `state.md` and invisible to the task scanner. That is the correct trade: the
constraint must be *findable*, not *actionable*.

This is not a Rule 26 duplication. The `conventions.md` entry holds the full content; the
state.md bullet is a pointer that never restates it. It is mandatory because
`follow-up/SKILL.md` hardcodes `if file != 'state.md': continue`,
`generate_session_map.py` sets `TRACKED_FILES = ['state.md']`, and `graph_memory.py` stores
`conventions.md` as a bare path with no content. Without the bullet the constraint lives in
a file no scanner reads.

**Keep every bullet on ONE line.** The task scanner matches
`^[ \t]*- \[[ xX/ ]\] (.*)` — single-line, and it stops at the newline. A bullet wrapped
across two lines loses its link and its text past the wrap.

**De-veto.** When a constraint is lifted, strike the bullet and record the reversal in
`history.log`. A pointer to a constraint that no longer exists is worse than none.

**No-SHA Rule.** Never write a commit SHA into `history.log`. Rule 34 orders append → stage
→ commit, so a SHA written during the capture turn is an unprovable mutation claim under
Rule 40. The provenance channel already exists and is authoritative: `git log -- <path>`
maps every `history.log` line to its commit. Rule 26 asks for a summary, not an identifier.

**No-Anchor-in-Quarantine Rule.** Quarantined items carry **no** temporal anchor. Rule 23
binds "direct action items in `task.md` and `state.md`"; a quarantined item is neither.
Anchoring it would grant an unverified claim the status of a finding — the exact behaviour
Rule 41's corollary forbids.

### 5. Pointer line

`generate_session_map.py` indexes **only lines beginning with `#`**. So the pointer must
*be* a heading, with the payload inline:

```markdown
## 2026-09-30 handoff — ses_f0e6b7515 — 4 routed, 1 quarantined → .agents/quarantine/2026-09-30-1930-a1.md
```

A prose line under an existing `##` heading is **dropped**, regardless of depth. Body lines
beneath the heading are for humans and are never indexed. Do not dump the session here — the
file is 405 lines of mixed format and becomes unfilterable.

### 6. Report, then let the user decide

**`NOT CAPTURED` is a destination, not a confession.**

On 2026-10-03 this report correctly flagged that a plan-review verdict existed only in chat.
That was the mechanism working — the line named the gap. But the tab still closed with the
item unwritten, which defeats the skill's stated purpose. The gap is only closed when the
thing is **written to a file**, not when it is named in a report the user must remember to act on.

So: if a residue row has no home, **it still gets a file.** Do not defer it to the user.

| Why it had no home | Where it goes instead |
|---|---|
| Decided, but the owning project is unknown | quarantine, `UNVERIFIED`, stating what would place it |
| A verdict on something outside the repo (a file on the Desktop, a plan under review) | a `research/<subject>_review.md` stub in the nearest owning project, plus one line in its `state.md` |
| Analysis whose value you cannot judge yet | the same stub, marked as raw findings with no recommendation |
| Nothing else applies | the quarantine file, untracked, with `UNVERIFIED` |

The stub does not need to be finished. **A rough stub beats a clean `NOT CAPTURED`.** The next
session can refine a file; it cannot refine a chat that is gone.

Then report it as captured:

```
HANDOFF COMPLETE — <session-id or UNKNOWN/AMBIGUOUS>
  Swept:      <n>/19 rows had residue — <row numbers, or "all NONE FOUND">
  Written:    <file> — <one line each>
  Reconciled: <stale entries corrected>
  Quarantined: <n> items → .agents/quarantine/<file>
  Working tree: <n> paths dirty — <yours> / <not yours / cannot tell>
  Dropped:     <what you deliberately did not capture, and why>
  Stubbed:     <anything with no home, written to a stub file anyway per step 6>
  NOT CAPTURED: <only what you could not even determine, or "nothing">
```

`NOT CAPTURED` is the least reliable line, because it is self-reported by the same agent
whose recall `tail_turns: 2` has already damaged. A compacted session is exactly where
recall is worst and confidence is highest. So the mechanical claims get machine-checked in
the Verification section below; the judgement claims rest on your honesty.

**But it should be short.** A long `NOT CAPTURED` is not humility, it is an unfinished
routing pass. If it lists three things, the sweep is incomplete — every one of them had a
file available to it. Anything reportable under `NOT CAPTURED` should have been a `Stubbed`
line first. Reserve `NOT CAPTURED` for: things you cannot identify as residue at all, and
facts you never established (write those to quarantine as `UNVERIFIED` if they came up at all).

## BEP scientific conversation handoff, including plain ChatGPT

Apply [`bep-guided-science-loop`](../bep-guided-science-loop/SKILL.md)
and [`bep-map-edit-review`](../bep-map-edit-review/SKILL.md).
A session may produce several approved map edits and no Python. Scientific
meaning belongs in the approved owner map and decision receipts; tentative
AI research goes to bridges/reference material, and owner-selected
implementations go to the working notebook. `state.md` should link to
these, naming one next scientific question, not duplicate the science.

For plain ChatGPT or cloud environments without the local OpenCode log,
**do not** guess a `ses_...` identifier or run the Windows log recipe.
Record `session-id: UNKNOWN`, exact known refs, what is merely proposed
versus approved, and inaccessible local-only commits/unsaved buffers.
Verify actual writes; if persistence is unavailable, provide a portable
**NOT SAVED** handoff rather than claiming completion.

## Rate Limiting

None. Two read-only log queries, two git queries, then local file writes.

## Common Mistakes

| Mistake | Consequence |
|---|---|
| Writing a veto only to `conventions.md` | Invisible — no scanner reads it |
| Making a veto a `- [ ]` checkbox | Permanent unactionable task; project pinned in active scan |
| Wrapping a bullet across two lines | Scanner drops everything past the wrap, including the link |
| Sending an unsent commitment to `task.md` ⏳ | Rule 17 — ⏳ is for *sent* items |
| Writing a session-scoped rule to `conventions.md` | Outlives its reason; misleads the next session |
| Writing a commit SHA into `history.log` | Rule 40 unprovable-mutation claim |
| Anchoring a quarantined item | Quarantine becomes a finding (Rule 41) |
| Reporting a residue item as `NOT CAPTURED` instead of writing it to a file | The tab closes and the item is gone — this is the failure the skill exists to prevent |
| Copying full content into both files | Rule 26 breach — the bullet is a pointer |
| Globbing `%USERPROFILE%\.local\share\opencode\` | Rule 27 credential leak via `auth.json` |
| Using `run=` or `parentID=` as the session id | Wrong or unparseable |
| Filtering on `agent=build` | Returns another tab's session; primaries may be `orchestrator`/`plan` |
| Scraping the stream log when you delegated a subagent | Pointless — the child's `parentID` is exact (see §1a) |
| Grepping for a pattern your own command contains | The `message=evaluated permission=` line echoes your query back |
| Accepting `agent=title` / `agent=compaction` | Captures a neighbour's session |
| Overwriting an existing quarantine file | Silent data loss between parallel tabs |
| A prose pointer line instead of a `##` heading | Dropped from `SESSION_MAP.md` |
| Dumping the session into `LATEST_UPDATES.md` | 405 lines becomes unfilterable |
| Reporting "all captured" when something was skipped | Destroys the only trust mechanism |

## Verification

The mechanical claims in your report are machine-checkable. Check them:

```powershell
git status --porcelain            # every TIER-1 file you claim to have written MUST appear here
git diff --name-only --cached     # scoped staging only; catches contamination
git diff --stat
pixi run python .agents/scripts/byte_guard.py --file <each tier-1 file you wrote>
```

**Carve-out: quarantine files never appear in `git status`.** The tier-2 bucket is
gitignored by design, so its absence from `git status` is the correct outcome, not a
failure. Verify tier-2 writes differently — `Test-Path` on the file, and confirm
`git check-ignore -v` still matches it.

Two corrections learned the hard way:

- **`byte_guard.py --staged` is a no-op if you have not staged yet** — it prints "no staged
  blob to scan". Use `--file <path>` for a pre-commit check. The pre-commit hook already runs
  `--staged` on the real staged set.
- **`byte_guard.py` is warn-only by design and does not block.** Read its output; it is the
  only check that catches control-character corruption in quoted user text.

If a **tier-1** file you claimed to write does not appear in `git status --porcelain`, your
report is provably false. Fix the report.
