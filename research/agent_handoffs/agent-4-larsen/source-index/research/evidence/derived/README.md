# Derived datasets and computational results

For processed/digitized/transformed values, simulation outputs and reproducibility receipts. Existing `notebooks/benchmarks/data/` and notebooks/figures keep their paths; index them here with source and generating code SHA rather than moving them in a bulk migration.

Record: original input locator, transformation/recalculation formula, units, uncertainty, stored-vs-newly-executed status, run environment, baseline comparison and what a result **does not validate**. Never label digitized or fitted values as raw experimental data.

## Larsen 2024 source audit outputs

| Artifact | Content and provenance |
|---|---|
| [experiment-count reconciliation](larsen_2024_experiment_count_reconciliation.csv) | Appendix F processed-row counts versus Figure 6.6 N; identifies the unresolved 36-row Pd₃Ag final-fit mask. |
| [selected experiment-ID crosswalk](larsen_2024_selected_experiment_id_crosswalk.csv) | Maps selected plot conditions to visible Appendix F IDs while retaining the existing dataset's exact-versus-digitized labels. A condition match alone does not prove a plotted marker is the same record. |
| [selected Appendix F processed responses](larsen_2024_appendix_F_selected_processed_responses.csv) | Visually transcribed displayed Pd₂Ag selected rows and Pd₃Ag Figure 6.1 head rows. These are author-processed conversion/selectivity outputs; the source workbook and raw GC data are absent. |
| [plot-versus-table response cross-check](larsen_2024_plot_vs_appendix_response_crosscheck.csv) | Differences between digitized markers and visible table responses; retains disagreements outside the stated ±2 pp graph-reading uncertainty. |
| [fixed-parameter model predictions](larsen_2024_source_law_selected_predictions.csv) | Executed independent notebook predictions for the printed first-power Eq. 6.11 and historical/Appendix F squared alternative. No refit. |
| [mapped processed-subset metrics](larsen_2024_mapped_processed_subset_metrics.csv) | Paired RMSEs on 15 Pd₀Ag, 15 condition-matched Pd₂Ag, and 4 displayed Pd₃Ag rows. Not the Figure 6.6 fitting populations. |
| [flow-reference sensitivity](larsen_2024_flow_reference_sensitivity.csv) | Five candidate flow-reference conventions for both rate-law branches; explicitly scenario analysis, not evidence of the actual MFC standard state. |
| [solver and balance checks](larsen_2024_solver_and_balance_checks.csv) | BDF/Radau and tolerance deltas, integrated flow minima and atom-balance residuals for selected inputs. |

The reproducible implementation is [the separate source-audit notebook](../../../notebooks/benchmarks/larsen_2024_source_audit.ipynb), executable with [its runner](../../../notebooks/benchmarks/run_larsen_source_audit.py). The historical [benchmark notebook](../../../notebooks/benchmarks/larsen_2024_benchmark.ipynb), its parameter CSV, and its selected-curve CSV remain unchanged. See [the audit report](../../reports/larsen_2024_equation_and_baseline_audit.md) for source locators, numerical results, verification gates and limitations.
