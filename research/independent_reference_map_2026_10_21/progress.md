# Progress — independent BEP scientific reference map v2

- **Status:** v2 scientific enrichment and validation are complete. PR #175 is open and unmerged against the frozen v1 branch. All content remains AI-authored and provisional at `idea` / `ai_worked_out` maturity.
- **Scope anchor:** `Academics/BEP/Catalysis/0_Project_Management/main.tex`.
- **Frozen base:** `work/bep-independent-reference-v1-20261021` at `e330492418150103a219f49bb7e850ece4aac5b9`.
- **Work branch:** `work/bep-independent-reference-v2-20261021`.
- **PR:** [#175 — BEP: enrich the independent scientific reference map (v2)](https://github.com/AsapLoso/project-management-agents/pull/175).

## Completed second-pass work

- Preserved the frozen v1 branch and created the isolated v2 branch from its exact commit.
- Preserved all 63 existing node positions, inserting 16 new nodes beside their parents; revised selected parent links to distinguish reaction chemistry and catalyst chemistry.
- Expanded the graph from 63 nodes / 20 sources to 79 nodes / 28 sources.
- Added PdAg site-ensemble and working-surface alternatives; distinct catalyst memory, bed RTD, pellet diffusion, thermal balance and measurement dynamics.
- Added mathematical no-gain limits (stable LTI/DC, Jensen for a static concave map, nested feasible sets), nonlinear mean rectification with model-dependent sign, cycle-integrated metrics and a fair steady comparator.
- Added Systems & Control distinctions among actuator command, realized bed-plane waveform, kinetic identification, performance testing and matched steady optimization.
- Added full-text Espinoza et al. (2022) as a bounded cross-system null-result/instrumentation case; reviewed Kaps et al. (2026) as cross-system FPO evidence and corrected author metadata. Urmès et al. (2022) publisher abstract narrows the novelty claim; full methods/SI remain inaccessible.
- Reworked the claim audit, open questions and methodological synthesis to make evidence access and transfer limits explicit.
- Automated graph/provenance validation passed with zero errors; exact results are in `validation.md`.

## Evidence/access boundary

Full text read for Urmès et al. (2019), Berger et al. (2008), Espinoza et al. (2022; TU Hamburg repository published-version PDF), and Kaps et al. (2026; publisher HTML). The Urmès et al. (2022) publisher page confirms periodic acetylene-flow experiments, kinetic estimation and fixed-bed outlet prediction, but the available full-text route returned abstract-level content and its listed SI was inaccessible. Exact spatial-model scope and any performance comparison remain unresolved. Mei, Li, Pachulski, Feimer, Horn–Bailey, and Ziegelhoeffer remain abstract/metadata-level as logged in `sources.yaml`.

## Git and PR record

- Graph/source/method commit: `244c322d60ee2424c54796477c7351b744ea61d9`.
- Claim-audit/uncertainty/progress/validation commit: `ac1ce1a80fa4a370a6dfa75d48d95506c06e3d86`.
- PR #175 targets `work/bep-independent-reference-v1-20261021`; GitHub confirmed base SHA `e330492418150103a219f49bb7e850ece4aac5b9`, v2 head branch, exactly seven deliverables, and open/unmerged state. The progress/validation record is then updated on that same branch; the PR remains unmerged.
- No auto-merge was enabled. PR #173 and the frozen v1 branch remain unchanged.
- The repository commit hook regenerated root `SESSION_MAP.md` and `workspace_inventory.md`; they are unrelated and remain unstaged. All commits for this task are scoped to the seven scientific-map deliverables.

## Scientific cursor after v2

Obtain the complete Urmès et al. (2022) article/SI and the actual target PdAg catalyst data. Then identify target surface, transport, thermal, actuator/analyzer and aging modes, and define the metric and feasible steady benchmark. Only with those facts can a model-supported gain or no-gain answer be investigated. No target parameters, predicted gain, optimum, or experimental outcome is supplied here.

The progress/validation update itself is recorded as a later commit on the same v2 branch; consult Git history and the PR head for its final commit ID.
