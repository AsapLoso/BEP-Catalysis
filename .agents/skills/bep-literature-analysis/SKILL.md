---
name: bep-literature-analysis
description: Standard operating procedure for extracting verified physical mechanisms and exact passages from Zotero PDFs using the 3-pass subagent process, guaranteeing zero-hallucination citations.
---

# Agentic Literature Analysis

## Context
As defined in `AGENTS.md` (Rule 16) and `conventions.md` (Convention 3), we cannot use blind citations. We must extract the exact passages from PDFs before finalizing any `\cite{...}` in the LaTeX proposal. To avoid AI hallucinations or missing critical physics, we use a 3-pass agentic verification system.

## Trigger
Run this skill whenever new papers are added via `/zotero-sync`, or when the `literature_analysis_tracker.md` shows papers in a `🔴 Unanalyzed` state.

## Procedure

### 1. Check Current Status
Run the automated tracker script to generate the latest status matrix of all papers.
```powershell
python "c:\Users\Deuts\OneDrive - Delft University of Technology\Misc\Gemini\Aa Project management\Academics\BEP\Catalysis\0_Project_Management\update_literature_tracker.py"
```
Review `Academics/BEP/Catalysis/literature_analysis_tracker.md` to identify which citekeys need analysis.

### 2. Launch Extraction Subagents (Run 1 & Run 2)
For each target paper, launch two independent `bep-paper-analyzer` subagents to perform the initial extraction.
*   **Prompt to subagent:** "Perform Run [1/2] analysis on [Citekey]. The PDF is in `acquired_pdfs/`. Extract exact quotes relating to plug flow, PSSA breakdown, dynamic operation, and LHHW kinetics. Save output to `paper_analyses/ref_[ID]_[Author][Year]_run[1/2].md`. Operational agency (Rule 43) applies: extract text via Python PDF tooling proactively; never claim unreadable without trying."


### 3. Launch Consensus Subagent
Once Run 1 and Run 2 are completed for a paper, launch a `bep-paper-comparator` subagent.
*   **Prompt to subagent:** "Compare Run 1 and Run 2 reports for [Citekey]. Classify discrepancies as [CONFLICT] or [BOTH TRUE]. Save output to `paper_analyses/ref_[ID]_[Author][Year]_consensus.md`."

### 4. Update Tracker & Review
Re-run the tracker script from Step 1 to verify the paper has moved to `🟢 Verified` status. The user can now safely review the `_consensus.md` files and approve citations for the LaTeX proposal.
