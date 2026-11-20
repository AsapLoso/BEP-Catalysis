> **NIET VOLLEDIG GEËVALUEERD — LETTER K (GEDEELTELIJK BESPROKEN)**
>
> **ALLEEN DE GELDIGHEID VAN VOORLOPIGE SIMULATOROUTPUTS IS BESPROKEN.** De overige vragen uit de eerste K-verkenning wachten nog op gebruikersbeoordeling. **L EN M ZIJN HELEMAAL NIET INHOUDELIJK BESPROKEN OF GEËVALUEERD.** Geen automatische goedkeuring voor de presentatie.

# K — What results are scientifically defensible?

**14 October 2026 · User decision: NO sufficiently validated reactor result for the presentation yet.** This is a short status record, not a full results dive or a proposal for a compulsory results slide.

## NOG TE BESPREKEN — OORSPRONKELIJKE K-VERKENNING (GEBRUIKER HEEFT DIT NOG NIET VOLLEDIG GEËVALUEERD)

Dit is de inhoud uit het **eerste K-bericht** die door de korte statusafsluiting niet volledig samen met de gebruiker is uitgewerkt. De voorlopig toegekende presentatieprioriteiten **HOOG / INTERESSANT** waren slechts voorstellen van de assistant, **niet** door de gebruiker geaccordeerd.

- [ ] **Eerste werkende simulatie met niet-nul reactiesnelheden:** wat toont de implementatie wél aan, en wat is enkel brontranscriptie/codewerking? Heeft dit zelfstandig presentatiewaarde?
- [ ] **Conversie, selectiviteit, verblijftijd in één synthetische referentieconditie:** ontvangst van de opgeslagen getallen (9,30% C₂H₂-conversie, 76,93% netto C₂H₄-selectiviteit, 11,88 ms nominale gasverblijftijd; 51 °C en 1,26 bar in samengestelde, aangenomen geometrie). **AL WEL BESPROKEN:** deze cijfers zijn niet voldoende gevalideerd om als fysieke reactorresultaten te presenteren. **NOG OPEN:** of we de berekende outputs alleen als diagnostiek toelichten of volledig weglaten.
- [ ] **Welke parameters beïnvloeden de voorspelling?** De gevoeligheidsstudie en de beperkingen van verschillen in modelconfiguratie en parameterbereik zijn nog niet inhoudelijk door de gebruiker beoordeeld; er is geen vastgestelde fysieke rangschikking.
- [ ] **Periodieke invoer: wat is werkelijk aangetoond?** De test bevat een sinusvormige C₂H₂-invoer van ±20%, maar vergelijkt hoofdzakelijk eindconcentraties van periodiek/constant aangedreven runs. Nog geen vastgestelde uitgangsamplitude/fase, ingeregelde periodieke baan of cyclusgemiddelde netto C₂H₄-opbrengst; bespreek of dit in de presentatie een apart open onderzoeksprobleem is.
- [ ] **Waar horen numerieke tests, bugs en correcties?** Voorlopig vooral ondersteunend en bij **J**, niet automatisch een K-slide.

**WEL BESPROKEN / BEHOUDEN BEPERKING:** *Er bestaat numerieke output, maar nog geen voldoende wetenschappelijk gevalideerd reactorresultaat.* Dit is **geen** claim dat de code gegarandeerd fout is of dat letterlijk nul fouten nodig zijn.

**LET OP:** Ga bij een volgend gesprek terug naar deze checklist en de eerste K-verkenning; de korte statusnotitie hieronder vervangt de nog niet afgeronde inhoudelijke evaluatie niet. L en M mogen op zichzelf als besproken gelden; hun eventuele keuzes over slide-inhoud staan los van dit K-vinkje.

## Editorial conclusion

There **are** numerical calculations and saved simulator outputs, but those are **not equivalent to physically or scientifically validated reactor results**. In the user's judgment, the outstanding model/numerical inconsistencies mean we should **not present a specific simulated conversion/selectivity number as an established scientific finding**. Distinguish this from requiring literally *bug-free* software; validity requires sufficient evidence/verification for the claim made.

- **[FACT: recorded numerical output, NOT validated reactor prediction]** A Hermes saved synthetic-case sensitivity receipt reports 9.30% acetylene conversion and 76.93% net ethylene selectivity for an assumed, composite reactor at nominal conditions. Keep these numbers as **diagnostic outputs only**, not a deck headline, an experimentally reproduced value, or an accepted periodic-operation result. [Receipt](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/evidence/vertical_slice/sensitivity_receipt.json) · [E source/geometry audit](E_operating_regime_transport_2026-10-14.md).
- **[FACT: actual progress]** Published Urmès-2019 chemistry was transcribed/audited; the new model has *nonzero* reacting code and a periodic-inlet function; the original code has a documented state-space structure and code-audit findings. These are **implementation/source-verification achievements**, not validation of the full physical predictions. [Source receipt](../../3_Model/probes/urmes2019_source_receipt.json) · [old audit](../../research/briefing/evidence/audit_2026_10_13.txt).
- **[UNRESOLVED]** Reactor source/catalyst/geometry transfer, code/physics inconsistencies, source normalization, radial conservation and derivative consistency, spatial and temporal error, and genuine sustained periodic response still need resolution. In the inspected Hermes branch, the periodic gate compares only **terminal outlet concentrations** under constant vs sinusoidal inlet; it does **not** calculate **harmonic phase/amplitude, converged cycle-average ethylene yield, or superiority over a matched steady reference**. [Code](https://github.com/AsapLoso/project-management-agents/blob/hermes/reacting-vertical-slice-2026-10-13/Academics/BEP/Catalysis/3_Model/vertical_slice_reacting_reactor.py) · [G numerical fidelity](G_numerical_methods_jacobian_feasibility_2026-10-14.md).
- **[SCOPING]** Do not erase measured/test receipts or call every computed output false; just restrict inference. The older Wednesday handoff saying *no reacting code and no periodic inlet* is also stale relative to Hermes, so don't repeat it as current status.

## Optional short statement for the presentation (if needed)

“We have assembled the mathematical and kinetic ingredients and generated preliminary reacting simulations. Before drawing conclusions about conversion, selectivity or periodic gains, we still need to verify that the model, numerical method and comparison metric accurately represent the intended physics.”

**Scientific takeaway (already discussed):** **No currently defensible claim of increased ethylene yield under periodic inlet forcing.** **K IS NOT FULLY EVALUATED:** only the validity/status boundary was discussed; the initial thematic K exploration above remains for review, and no positive reactor result or presentation slide has been approved. Next substantive presentation work may move to **L (what precisely remains to test)** or **A/M (return to the scientific question and assemble the story)**. Technical checks remain in **J**.

**Links:** [A–M master](../RESEARCH_JUSTIFICATION_INDEX_2026-10-14.md) · [presentation hub](../PRESENTATION_STRUCTURE.md) · [optional I bridge](../sub-stories/05_reacting_model_inlet_candidate.md).
