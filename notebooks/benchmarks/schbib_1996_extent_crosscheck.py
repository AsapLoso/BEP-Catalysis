"""Independent two-extent cross-check for Schbib (1996) Table 6.

Numerical consistency only, NOT validation of published experimental data,
the author-shared correction, Model III heat transfer, or PdAg transfer.

Run from repository root:
    python notebooks/benchmarks/schbib_1996_extent_crosscheck.py

Uses only the two source versions in the audit and compares predictions with
the existing six-flow audit JSON. Does not rewrite the historical notebook.
"""
import math
from pathlib import Path
import json
import sys

import numpy as np
from scipy.integrate import solve_ivp
from sympy import Matrix, symbols

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

GAS_CONSTANT = 8.314462618  # J/(mol K)
NU = np.array([[0, 0], [-1, 0], [1, -1], [0, 1], [-1, -1], [0, 0]], float)
FEED = np.array([.0653, .0052, .4399, .2672, .2210, 0.0])
CASES = [(150, 341), (1400, 359), (5000, 393)]
SETS = {
    "Original printed Table 8": {
        "rate_mass_basis": "gcat",
        "logs": [31.1, 26.6, 20.2, 13.6, .26, -.012, -16.0],
    },
    "Author-shared correction (text transcription)": {
        "rate_mass_basis": "kgcat",
        "logs": [31.1, 26.6, 17.2, 10.16, -2.74, -3.012, -19.0],
    },
}
ENERGIES_J_MOL = np.array([45.51, 42.94, 21.22, 9.95, .005, .001, .001]) * 4184.0
METHODS = ("Radau", "BDF", "LSODA", "DOP853")


def inlet_flow(co_ppm):
    fractions = FEED.copy()
    fractions[-1] = co_ppm * 1e-6
    fractions[:-1] *= (1 - fractions[-1]) / FEED[:-1].sum()
    # Table 3, 100 cm3(STP)/min. STP=273.15 K, 1 atm is an explicit assumption.
    ftot_kmol_s = (100e-6 / 60) * 101325 / (1000 * GAS_CONSTANT * 273.15)
    return ftot_kmol_s * fractions


def extent_rates(extents, feed, temperature_k, parameters):
    flows = feed + NU @ extents
    if flows.sum() <= 0:
        raise ValueError("No positive total flow")
    # Species-flow state is reconstructed from both extents simultaneously.
    concentrations = np.maximum(flows / flows.sum(), 0) * (
        16 * 101325 / (1000 * GAS_CONSTANT * temperature_k)
    )
    logs = np.array(parameters["logs"], dtype=float)
    if parameters["rate_mass_basis"] == "gcat":
        logs[:2] += 3.0  # per gram to per kg, when W is kg catalyst
    coeff = 10**logs * np.exp(-ENERGIES_J_MOL / (GAS_CONSTANT * temperature_k))
    k_a, k_e, kh, kco, ke, ket, ka = coeff
    _, ca, ce, cet, ch, cco = concentrations
    denominator = 1 + math.sqrt(kh * ch) + kco * cco + ka * ca + ke * ce + ket * cet
    assert denominator > 0 and math.isfinite(denominator)
    return np.array([k_a * ca * ch / denominator**3,
                     k_e * ce * ch / denominator**3])


def run_extent(co_ppm, temperature_k, parameters, method):
    feed = inlet_flow(co_ppm)
    # The state comprises only accumulated reaction extents xi1 and xi2 [kmol/s].
    solution = solve_ivp(
        lambda mass, xi: extent_rates(xi, feed, temperature_k, parameters),
        (0, 0.001), [0.0, 0.0], method=method,
        rtol=1e-10, atol=1e-19, max_step=0.001/80,
    )
    assert solution.success, (method, solution.message)
    xi1, xi2 = solution.y[:, -1]
    flows = feed + NU @ np.array([xi1, xi2])
    assert np.isfinite(flows).all() and flows.min() >= -1e-16
    return {
        "C2H2 model (%)": 100 * xi1 / feed[1],
        "C2H4 model net (%)": 100 * (xi2 - xi1) / feed[2],
        "C2H4 reaction-2 extent (%)": 100 * xi2 / feed[2],
    }


def test_symbolic_stoichiometry():
    stoich = Matrix(NU.astype(int).tolist())
    elements = Matrix([[1, 2, 2, 2, 0, 1],
                       [4, 2, 4, 6, 2, 0],
                       [0, 0, 0, 0, 0, 1]])
    assert elements * stoich == Matrix.zeros(3, 2)
    xi1, xi2 = symbols("xi1 xi2")
    assert stoich * Matrix([xi1, xi2]) == Matrix(
        [0, -xi1, xi1-xi2, xi2, -xi1-xi2, 0]
    )


def main():
    test_symbolic_stoichiometry()
    repo = Path(__file__).resolve().parents[2]
    reference = repo / "research/evidence/derived/schbib_1996_audit_results.json"
    if not reference.is_file():
        raise FileNotFoundError(f"Audited six-flow results required: {reference}")
    expected_rows = json.loads(reference.read_text(encoding="utf-8"))[
        "table6_full_law_results"
    ]
    largest_method_difference = 0.0
    largest_reference_difference = 0.0
    for name, cfg in SETS.items():
        for co, temperature in CASES:
            methods = {m: run_extent(co, temperature, cfg, m) for m in METHODS}
            comparable = [row for row in expected_rows
                          if row["set"] == name and row["equation"] == "full"
                          and row["thermal"] == "isothermal"
                          and row["CO (ppm)"] == co]
            assert len(comparable) == 1, (name, co, len(comparable))
            for key in ("C2H2 model (%)", "C2H4 model net (%)",
                        "C2H4 reaction-2 extent (%)"):
                values = [methods[m][key] for m in METHODS]
                spread = max(values) - min(values)
                difference = abs(methods["Radau"][key] - comparable[0][key])
                largest_method_difference = max(largest_method_difference, spread)
                largest_reference_difference = max(largest_reference_difference, difference)
                assert spread < 1e-6, (name, co, key, spread)
                # Audit JSON stores rounded decimal results; compare within 1e-4 pp.
                assert difference < 1e-4, (name, co, key, difference)
            print(f"{name}: {co} ppm, {temperature} K -> "
                  f"C2H2 {methods['Radau']['C2H2 model (%)']:.6f}%, "
                  f"net C2H4 {methods['Radau']['C2H4 model net (%)']:.6f}%")
    print(f"PASS: E*N = 0; max solver spread = {largest_method_difference:.3e} pp; "
          f"max deviation from recorded six-flow audit = {largest_reference_difference:.3e} pp")
    print("Numerical equivalence only: all-species Table 6 experimental gate remains BLOCKED.")


if __name__ == "__main__":
    main()
