# BEP reactor notebook review workspace

This folder holds editable copies of the three reactor-model notebooks and the related legacy Python scaffold. The copied source files are unchanged snapshots; this setup did not execute the notebooks or alter their code or saved outputs.

## The four artifacts

| Local copy | Role | Source snapshot |
|---|---|---|
| [legacy/c2h2_hydrogenation_transient_model.ipynb](legacy/c2h2_hydrogenation_transient_model.ipynb) | Legacy inline transient packed-bed model | [Methanol-Catalysis, `5785fa5f11289d72127457f9a3a25aa5c4e71be3`](https://github.com/AsapLoso/Methanol-Catalysis/blob/5785fa5f11289d72127457f9a3a25aa5c4e71be3/content/c2h2_hydrogenation_transient_model.ipynb) |
| [v1/bep_dynamic_reactor_response.ipynb](v1/bep_dynamic_reactor_response.ipynb) | Dynamic reactor response, V1 (PR #1) | [Methanol-Catalysis, `791e51c0eba11f4bd5095f48d0520c6af317f5f8`](https://github.com/AsapLoso/Methanol-Catalysis/blob/791e51c0eba11f4bd5095f48d0520c6af317f5f8/notebooks/bep_dynamic_reactor_response.ipynb) |
| [v2/bep_dynamic_reactor_response.ipynb](v2/bep_dynamic_reactor_response.ipynb) | Dynamic reactor response, V2 (PR #2) | [Methanol-Catalysis, `2ee0dc1a84529d6830dcc628fc771878907fb22c`](https://github.com/AsapLoso/Methanol-Catalysis/blob/2ee0dc1a84529d6830dcc628fc771878907fb22c/notebooks/bep_dynamic_reactor_response.ipynb) |
| [legacy/c2h2_hydrogenation_transient_model.py](legacy/c2h2_hydrogenation_transient_model.py) | Python form of the legacy scaffold in `3_Model` | [project-management-agents, `cd0df858219d3786fb7943d2ea380a9bc66195ba`](https://github.com/AsapLoso/project-management-agents/blob/cd0df858219d3786fb7943d2ea380a9bc66195ba/Academics/BEP/Catalysis/3_Model/c2h2_hydrogenation_transient_model.py) |

The canonical Python scaffold remains at [`3_Model/c2h2_hydrogenation_transient_model.py`](../../3_Model/c2h2_hydrogenation_transient_model.py). The copy here is for the side-by-side review workspace; the original has not been moved or replaced.

## Scope and status

Lucas confirmed the initial editable set as **three reactor notebooks and one Python file**. The BEP presentation notebook and `content/Results.ipynb` remain relevant as separate project context, but are not part of this four-artifact workspace.

V1 and V2 are literature-reproduction vertical slices. Their saved notebook outputs are preserved from their source commits. Copying them does not establish that they run in this repository; V1/V2 use the `pbr` package, and dependencies have not been installed or checked here.

During review, keep these evidence types separate: what the code does, what saved or newly reproduced numerical evidence supports, what AI analysis proposes, and what Lucas has personally understood or approved. No new scientific interpretation or validation is implied by this branch setup.
