# BEP reconsolidation capture — 16 October 2026

**Purpose:** Preserve this conversation's user-authored observations before scientific verification. This file is a provenance record, not an approved scientific interpretation or presentation script.

## Authority labels

- **[RAW USER THOUGHT]** Verbatim or lightly punctuated speech from the referenced conversation. These statements describe the user's view or questions; they are not automatically established scientific facts.
- **[USER-REPORTED CORRECTION]** A user-directed retraction/correction recorded as such. The replacement value still needs source and unit verification before use as an independently established scientific result.
- **[AI INFERENCE — NOT USER-APPROVED]** The comparison and recommended sequence below are my synthesis of the repository evidence.
- **[DECISION LOG]** Only explicit approvals or decisions are treated as decisions. A merge, an assistant-authored file, or a generally positive reaction does not imply approval.

Source: ChatGPT conversation [Project orientation review](chatgpt-conversation://6ad158ef-8288-83ed-a868-b575e9e28651), user's messages in the project orientation discussion, read on 16 October 2026. The cached preview marks the final utterance as truncated after “Can you just make more t”; no missing wording is reconstructed here.

## 1. User-authored raw thoughts

**[RAW USER THOUGHT — purpose and evidence]**

> “Shouldn't the vertical slice? I'm just reading above. Shouldn't it be identical in some ways to actual measurement data? Because it reports.”

> “There are some very good points about that we implemented this too rashly. I mean basically you just made some code that is basically incorrect, okay? We can say what we want, but the code should have a clear purpose. What is the purpose for what we made it? Just getting a number? No, that's not the purpose.”

These are recorded as questions and critique, not as an approved requirements specification. The intended relationship between the vertical slice and measurements remains to be made precise.

**[RAW USER THOUGHT — catalyst comparison, left unresolved]**

> “If I see, for example... Ah, okay. Yeah, no, I meant, for example, just combining palladium aluminum compared to palladium argon silicon? Okay, never mind. Yeah, okay. The kinetics, of course, differ per catalyst, but palladium is the working ingredient, so that should be fine.”

The catalyst/material phrases are preserved as spoken and are not normalized here into a specific support, alloy, or catalyst formulation. The suggestion that palladium as the active ingredient may be enough to compare kinetics is a user hypothesis; transferability across supports, alloys, dispersion and operating conditions has not been established.

**[RAW USER THOUGHT — withdrawn timescale and parked follow-up]**

> “As for that timescale part, please, if that's anywhere outside of the log, just, you know, shoo it away. It was a bug. That happens.”

> “Good thing these runs go really quick, so yeah, you can just turn on the pellet radius, you know, for simulations. Might as well also immediately make for a Gaussian distribution of the sizes.”

> “I should definitely give this, of course, to a worker, but I mean this is all just not a priority right now, I'm telling you. But definitely something to note down in state or maybe even a wayfinder map.”

The radius-resolved diffusion and Gaussian-size-distribution ideas are **parked research questions**. This capture does not authorize an implementation, dispatch, or priority increase.

## 2. [USER-REPORTED CORRECTION] Withdrawn diffusion timescale claim

The earlier extreme pellet-diffusion statement, approximately **116.6 s**, is withdrawn as a claim and must not be repeated as a current result. The user specifies the corrected order of magnitude as approximately **0.001166 s**. Preserve the old value only where needed to explain the audit trail; do not erase its historical log entry.

The replacement value is recorded as user-directed and is consistent with the correction already discussed in the E transport analysis, but its inputs, units, geometry and diffusivity convention must be independently checked before treating it as a scientific fact. The implication that pellet diffusion is the dominant timescale is also withdrawn pending that check.

## 3. [AI INFERENCE — NOT USER-APPROVED] Critical model comparison

| Approach | What its current evidence supports | Main scientific limit |
|---|---|---|
| **Legacy transient framework** | An ambitious Method-of-Lines state layout with bulk gas, pore gas and evolving surface states (1,480 entries on the documented grid). The repository labels it a scaffold; its kinetic constants are zero and the old code register records multiple blocking defects. | Its physical ambition is not predictive validity. It is not an appropriate source of conversion, selectivity, or dynamic-performance claims until equations, conservation and numerical defects are reconciled. |
| **Urmès 2019 reacting vertical slice** | A smaller gas-transient reactor using the paper's composite LHHW/PSSA kinetics. A static source receipt checks 24 source items, including Table 5 constants, rate expressions, feed and catalyst details. This is useful as a source-matched reacting baseline. | A source-transcription check establishes consistency with the paper text, not reproduction of measured reactor outputs. The companion PBR implementation receipt records an unsuccessful coverage-reproduction gate and a pressure-path discrepancy; E also records geometry/material mismatches. There is no validated periodic-yield result. |
| **Urmès 2022 transient non-PSSA route** | It represents time-dependent surface coverages, the mechanism needed to investigate catalytic memory under periodic operation. PR #3 added an opt-in experimental mechanism with isolated algebraic checks. | It is not yet a sourced, calibrated reactor prediction: the complete 2022 mechanism/parameters and supporting information were not verified in the cited bridge, default parameters are absent, and the full coupled reactor/data benchmark is not established. PR #3 was merged into a Hermes branch, not `devcontainer`. |

**Code consistency and experimental comparison are separate gates.** A source-to-code audit can establish that equations, constants, units and the selected code path match a source. A code-consistency or isolated invariant test cannot establish that the reactor reproduces real measurements. That requires a like-for-like benchmark against a published or project measurement dataset with catalyst identity/support, feed, pressure, temperature, bed and pellet geometry, and measured outputs matched. The Urmès 2019 paper's own fitted data do not automatically validate a separate implementation.

**Recommendation [AI inference, not a user decision]:** Start with a bounded Urmès 2019 source-matched baseline and an explicit experimental-data reproduction benchmark, while resolving its known implementation and numerical issues. In parallel, keep the 2022 surface-memory route as a later comparison whose full source mechanism and parameterization must first be verified. Do not start by merging the legacy framework and the vertical slice: integration alone does not improve accuracy or answer the experimental question. Revisit the legacy architecture only where a clearly stated physical requirement justifies it. This recommendation is not a new priority assignment and does not dispatch work.

## 4. Capture first, verify separately

1. **Raw capture:** The user dictates freely. Save the words with date, source conversation/turn, and minimal punctuation cleanup under **[RAW USER THOUGHT]**. Preserve uncertainty, corrections, abandoned examples and “never mind” moments. Do not turn these into requirements or facts.
2. **Verification pass:** In a separate section or file, check each scientific claim against the primary paper/data, code path, units and reproducible calculations. Label claims **[FACT: source/code]**, **[USER-REPORTED]**, **[INFERENCE]**, or **[UNVERIFIED]**; cite exact evidence and say what the check does not establish.
3. **Decision log:** Record a **[DECISION]** only when the user explicitly chooses it, with date and evidence. Keep approvals granular by artifact/section. Preserve the raw capture and append corrections to history rather than silently rewriting the original.
4. **Project-state update:** Mirror only the confirmed decision and its remaining open questions into state/Wayfinder. Leave recommendations and parked questions labelled as such until the user decides otherwise.

The open request to assemble a coherent scientific document for Damian remains open; this provenance capture is preparatory material, not that document.

## 5. [DECISION LOG] Approval boundaries

- **PR #4 / presentation draft:** The GitHub API reports PR #4 merged into `devcontainer` on 15 October 2026. The user explicitly said, “It did not receive my approval.” These statements coexist: merge status is repository history, not user approval. The presentation draft remains unapproved by the user.
- **E/F/G analyses:** Treat review or approval of E, F and G content as separate, section-specific judgments. A positive remark about “some very good points” is not blanket approval of all three analyses, the deck, or PR #4.
- **PR #3:** GitHub reports it merged into `hermes/reacting-vertical-slice-2026-10-13`; that branch/PR status does not by itself establish scientific validation or approval of its claims.
- **Not discussed/decided here:** The user's reaction does not ratify L/M, other presentation content, the catalyst transferability hypothesis, or any implementation plan.

## 6. User preferences and participation (recorded 16 October 2026)

**[USER-PROVIDED PREFERENCES — not scientific evidence]**

- Code should answer a clear scientific question. The 2019 components may eventually be integrated into the existing framework the user called “model 1” / “model 3,” after checking that framework's baseline. The naming difference is preserved here rather than resolved by inference.
- The 2022 transient mechanism should likewise extend the current framework. A third standalone vertical slice needs a strong technical reason before being chosen.
- Keep pellet-radius distributions, dynamic attenuation and conservation work parked at the research level until their question and priority are revisited. This capture authorizes no implementation.
- Preserve original user utterances separately from AI interpretation. Keep E/F/G judgments section-specific and preserve the explicit boundary that PR #4's merge did not receive user approval.
- The user's proposed involvement pattern has two broad phases: the user frames the research question, and joins again for a short scientific synthesis before a final artifact. The user gives final sign-off on a concise thesis-worthy synthesis; the agent may do the broad middle exploration with traceable evidence and make upstream revisions when the synthesis fails review. Low-value slide decks are not an approval artifact.
- Guided discussion while reading the papers is the preferred route for rebuilding scientific ownership; more agent autonomy is not the goal. No Jira or new ticket system is requested.

**[USER-PROPOSED WORKING MODEL]** The two-phase involvement description records a proposed collaboration pattern, not a claim that the user has approved any scientific conclusion or a particular presentation.

The reference milestone statuses and evidence are tracked separately in [BEP model verification milestones](model_verification_milestones.md).

## Evidence map

- [BEP model state](../../3_Model/state.md)
- [Framework audit](../../3_Model/transient_model_framework_audit.md)
- [Urmès 2019 source receipt](../../3_Model/probes/urmes2019_source_receipt.json)
- [PBR implementation receipt](../../3_Model/probes/pbr_implementation_receipt.json)
- [Transport analysis E](../../presentation/deep-dives/E_operating_regime_transport_2026-10-14.md)
- [Conservation analysis F](../../presentation/deep-dives/F_conservation_state_space_2026-10-14.md)
- [Numerical methods analysis G](../../presentation/deep-dives/G_numerical_methods_jacobian_feasibility_2026-10-14.md)
- [2022 non-PSSA bridge](../notes/NON_PSSA_SURFACE_BRIDGE_2026-10-14.md)
