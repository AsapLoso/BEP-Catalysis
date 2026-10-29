# Wayfinder: DCSC Thesis-Relevance Index

## 1. Destination
A per-person relevance index of DCSC (3ME) against Lucas's methanol-catalysis BEP thesis — **specific enough to decide which 2–3 people are actually worth approaching, and with a stated reason per name.** Complete when every candidate carries either a `RELEVANT (because X)` or a `NOT RELEVANT (because Y)` verdict, and the shortlist is chosen.

This map **plans, it does not write the verdicts.** The verdicts are the tickets.

## 2. Decisions So Far

- **[x] Dylan Kalisvaart is in the DCSC roster.** `### D. Kalisvaart (Dylan)`, under `Researchers and postdocs`, [The Scientists](file:///REDACTED_LOCAL_HOME/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/Aa%20Project%20management/research/wayfinder/dcsc_thesis_relevance.md) — 2026-10-04. Cross-checked against `Academics/BEP/SysCon/state.md:27` (`D.Kalisvaart@tudelft.nl`).
- **[x] Dylan is NOT in the cluster-membership index.** The 8 cluster pages name 26 people; he is not among them. Cluster membership covers academic staff only. *Consequence: for Dylan, a cluster index yields nothing — his relevance must come from his own record.*
- **[x] Carlas Smith is in DCSC at a higher rank than Bregman.** `dr. C.S. Smith (Carlas)`, **Associate professor** (9 of 27 on the Professors page), vs Bregman who appears on **no** DCSC page at all.
- **[x] Person→cluster membership IS published, on 8/8 cluster pages.** Each carries an explicit *"People at DCSC that are active in this research area/application area are:"* line. ⇒ The index is buildable **without** scraping 113 individual profiles. This was the pivotal unknown.
- **[x] The roster is stowed.** All names + the 26-person membership matrix + the keyword-density table are persisted in [`Academics/BEP/SysCon/resources.md`](file:///REDACTED_LOCAL_HOME/OneDrive%20-%20Delft%20University%20of%20Technology/Misc/Gemini/Aa%20Project%20management/Academics/BEP/SysCon/resources.md) (Rule 9: reference data does not live in `state.md`).
- **[x] The "1:1 with my thesis" claim is a METHOD match, not a domain match.** Thesis = 1D transient PBR, Extended LHHW + `$r_{1,max}$` cap + non-linear `$n_{inh}$` inhibition, Pd0Ag/α-Al₂O₃ series, **open-loop dynamic trajectory optimisation** (§3.3), closed-loop deliberately out of scope (§3.5); transport phenomena is Bera's (TNW) half. Dylan himself: *"Onze domeinen liggen ontzettend ver uit elkaar, maar op wiskundig niveau zijn er juist weer veel parallellen."* ⇒ The index answers **"who owns the methods I must borrow"**, not "who does my thesis".
- **[x] Two hard negatives from the cluster pages** (2026-10-04, full table in `resources.md`): `MPC`/`model predictive` **0/8**; `state estimation`/`Kalman`/`observer` **0/8**; `FEM`/`CFD`/`flow`/`fluid`/`turbulence`/`FSI` **0/8**. DCSC publishes none of the three things that would make this thesis obvious. *This is the map's central finding and it is a negative one.*
- **[x] Van Wingerden is not in the Energy cluster.** His clusters are **Modeling & system identification** and **Control & Learning**. Energy names only 4 people (Batselier, Ferrari, Grammatico, Keviczky) and says "wind **farms**" once inside a domain list. ⇒ The wake-dynamics work is a **personal** track record, invisible to any cluster-based index.

## 3. Active Frontier

### Island A: The gating scope question (blocks every other island)
- [ ] **Does §3.5 survive? — is closed-loop / SI / state estimation IN the thesis, or is open-loop optimisation the deliverable?** (`wayfinder:grilling`) — *Question: given the open-loop baseline is already built and working, what decides whether the thesis commits to delivering system identification + data-driven control, or explicitly parks it as a follow-on paper?*
  - Status: Open. **HITL — the agent must not answer this.**
  - Dependencies: None. Unblocked, and **highest leverage on this map**: the answer sets the relevance criterion itself. If open-loop stands, the entire Control & Learning and Optimization clusters drop to near-zero relevance and the map collapses to 2 names.

### Island B: Grounding the one "super relevant" claim
- [ ] **What does Van Wingerden's own record actually claim?** (`wayfinder:research`) — *Question: on `tudelft.nl/staff/j.w.vanwingerden/` and his group's publication list, which of nonlinear system identification, state estimation, Koopman/linear lifting, data-driven MPC, and wake/turbine control are demonstrably present?*
  - Status: Open. Dependencies: None.
  - Why it matters: this is the *only* candidate with a user-asserted 1:1 claim, and the cluster pages say nothing about fluids. The claim currently rests on one introweek presentation — a single unverified data point.

### Island C: Turning membership into expertise
- [ ] **Which of the 26 have published *nonlinear SI / state estimation / Koopman / predictive control* work — as opposed to merely being listed?** (`wayfinder:research`) — *Question: for the 26 names on the membership matrix, which have publications or staff-page project text in the four method families that §3.5 would need?*
  - Status: Open. Dependencies: Island A (the criterion depends on the §3.5 answer), but the *data collection* can start now and be filtered later.
  - Note: membership is attribution, not evidence. `Control & Learning` names 19 people and zero physical systems — breadth here is not depth.

### Island D: The Dylan-shaped gap
- [ ] **Is the right index boundary "26 cluster members" or "113 roster names"?** (`wayfinder:grilling`) — *Question: the 26 have published methods; the 86 Scientists hold the day-to-day SI/state-estimation execution. Which population is the index for?*
  - Status: Open. Dependencies: None.
  - Fact driving it: Dylan — the one contact who already replied, already agreed to coffee, and already offered to prep Van Wingerden papers — is in the 86, not the 26. The population that produced every useful contact so far is the one the cluster index excludes.

### Island E: Persist the roster (mechanics)
- [ ] ~~Stow roster + membership + keyword table in `SysCon/resources.md`~~ — **DONE 2026-10-04**, `d2c3fdd`-era working tree.
- [ ] **Link the map from `SysCon/state.md`** (`wayfinder:task`) — *Question: n/a — mechanical; the map must be reachable from a canonical `state.md` per the skill contract.*

## 4. Not Yet Specified (The Fog of War)

### Island A Fog
- *How the §3.5 decision propagates into the 4 Work Packages and the PDC course coupling (MIMO module, process-optimization module) — unknown until A resolves.*
- *Whether a fallback-only open-loop thesis still justifies any DCSC contact at all.*

### Island B Fog
- *Whether the fluid-dynamics half of the thesis (Bera, transport phenomena) has a TU Delft control-theory counterpart at all — DCSC publishes zero fluid/FSI content, so the search may have to leave DCSC entirely.*

### Island C Fog
- *Whether SI/state-estimation for a **1D stiff PBR with LHHW inhibition** is even an open problem in the literature, or solved enough that it is not thesis material. Unclear until the method candidates are read.*
- *Koopman lifting for periodic limit cycles — Dylan raised exactly this on 29 jul (`$x_{k+1}=f(x_k,u_k)$) and it connects to van Wingerden's own Koopman mention. Neither has been read.*

### Island D Fog
- *DIAM (EWI) is a separate institute and a separate question. Deferred to its own map — explicitly not this destination.*
- *Whether the 71 PhD candidates are prospects (future MSc supervision), peers, or noise. Different index, different criterion.*

## 5. Out of Scope
- **DIAM / EWI** — a different faculty and a much larger population. Own map if it is ever wanted.
- **The TA / course route** — Bregman, Broeren, Janssen. Solved separately in `Jobs/TA_Positions/Replies/Bregman_KT1005/`. Club membership is not thesis relevance.
- **Actually contacting anyone.** This map produces a shortlist; outreach is a separate decision.
- **Scraping the other 5 application clusters for depth** — Health scores 0/28 on the method keyword set, Transportation 1/28. Recorded as settled, not deferred.
- **Publications, projects, news per person** — DCSC publishes none at cluster level; anything deeper comes from personal staff pages (Island B/C).
