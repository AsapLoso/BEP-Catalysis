import math
import platform
import sys


R_KCAL_PER_MOL_K = 1.98720425864083e-3
R_PA_M3_PER_KMOL_K = 8314.46261815324


def arrhenius(log10_a: float, e_kcal_per_mol: float, temperature_k: float) -> float:
    return 10.0**log10_a * math.exp(
        -e_kcal_per_mol / (R_KCAL_PER_MOL_K * temperature_k)
    )


def schbib_terms(temperature_k: float, pressure_pa: float, co_ppm: float) -> dict:
    mole_fractions = {
        "CH4": 0.0653,
        "C2H2": 0.0052,
        "C2H4": 0.4399,
        "C2H6": 0.2672,
        "H2": 0.2210,
        "CO": co_ppm * 1.0e-6,
    }
    concentrations = {
        species: y * pressure_pa / (R_PA_M3_PER_KMOL_K * temperature_k)
        for species, y in mole_fractions.items()
    }
    adsorption = {
        "KH": arrhenius(20.2, 21.22, temperature_k),
        "KCO": arrhenius(13.6, 9.95, temperature_k),
        "KE": arrhenius(0.26, 0.005, temperature_k),
        "KEt": arrhenius(-0.012, 0.001, temperature_k),
        "KA": arrhenius(-16.0, 0.001, temperature_k),
    }
    terms = {
        "hydrogen": math.sqrt(adsorption["KH"] * concentrations["H2"]),
        "CO": adsorption["KCO"] * concentrations["CO"],
        "acetylene": adsorption["KA"] * concentrations["C2H2"],
        "ethylene": adsorption["KE"] * concentrations["C2H4"],
        "ethane": adsorption["KEt"] * concentrations["C2H6"],
    }
    denominator_base = 1.0 + sum(terms.values())
    return {
        "T_K": temperature_k,
        "P_Pa": pressure_pa,
        "CO_ppm": co_ppm,
        "KCO_m3_kmol": adsorption["KCO"],
        "CCO_kmol_m3": concentrations["CO"],
        "KCO_CCO": terms["CO"],
        "KH_m3_kmol": adsorption["KH"],
        "CH2_kmol_m3": concentrations["H2"],
        "sqrt_KH_CH2": terms["hydrogen"],
        "other_terms": terms,
        "denominator_base": denominator_base,
        "denominator_cubed": denominator_base**3,
    }


def schbib_isothermal_pfr(
    temperature_k: float, pressure_pa: float, co_ppm: float, n_steps: int
) -> tuple[float, float]:
    """Integrate Table 8 kinetics over 1 g at Table 6 SV100.

    Uses the Table 3 gas composition, with its unreported 0.125 mol% balance
    treated as inert, and 0 C / 1 atm for the STP flow conversion.
    """
    feed_total_kmol_s_per_g = (
        1.0e-4
        * 101325.0
        / (8314.46261815324 * 273.15)
        / 60.0
    )
    y0 = {
        "CH4": 0.0653,
        "C2H2": 0.0052,
        "C2H4": 0.4399,
        "C2H6": 0.2672,
        "H2": 0.2210,
        "CO": co_ppm * 1.0e-6,
    }
    y0["unreported_balance"] = max(0.0, 1.0 - sum(y0.values()))
    f0 = tuple(feed_total_kmol_s_per_g * y0[k] for k in y0)
    species = tuple(y0)
    ia = species.index("C2H2")
    ie = species.index("C2H4")
    ih = species.index("H2")
    iex = species.index("C2H6")
    ico = species.index("CO")
    k_a = arrhenius(31.1, 45.51, temperature_k)
    k_e = arrhenius(26.6, 42.94, temperature_k)
    k_h = arrhenius(20.2, 21.22, temperature_k)
    k_co = arrhenius(13.6, 9.95, temperature_k)
    k_e_ads = arrhenius(0.26, 0.005, temperature_k)
    k_et_ads = arrhenius(-0.012, 0.001, temperature_k)
    k_a_ads = arrhenius(-16.0, 0.001, temperature_k)
    c_total = pressure_pa / (R_PA_M3_PER_KMOL_K * temperature_k)

    def rhs(flow: tuple[float, ...]) -> tuple[float, ...]:
        total = sum(flow)
        if total <= 0.0:
            raise ArithmeticError("non-positive total molar flow")
        c = {name: value / total * c_total for name, value in zip(species, flow)}
        d = (
            1.0
            + math.sqrt(k_h * c["H2"])
            + k_co * c["CO"]
            + k_a_ads * c["C2H2"]
            + k_e_ads * c["C2H4"]
            + k_et_ads * c["C2H6"]
        )
        rate_a = k_a * c["C2H2"] * c["H2"] / d**3
        rate_e = k_e * c["C2H4"] * c["H2"] / d**3
        out = [0.0] * len(species)
        out[ia] = -rate_a
        out[ih] = -rate_a - rate_e
        out[ie] = rate_a - rate_e
        out[iex] = rate_e
        return tuple(out)

    def add(a: tuple[float, ...], b: tuple[float, ...], scale: float) -> tuple[float, ...]:
        return tuple(x + scale * y for x, y in zip(a, b))

    state = f0
    h = 1.0 / n_steps
    for _ in range(n_steps):
        k1 = rhs(state)
        k2 = rhs(add(state, k1, h / 2.0))
        k3 = rhs(add(state, k2, h / 2.0))
        k4 = rhs(add(state, k3, h))
        state = tuple(
            x + h * (a + 2.0 * b + 2.0 * c + d) / 6.0
            for x, a, b, c, d in zip(state, k1, k2, k3, k4)
        )
    return 1.0 - state[ia] / f0[ia], 1.0 - state[ie] / f0[ie]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"platform={platform.platform()}")
    print(f"python={sys.executable}")
    print(f"python_version={sys.version.split()[0]}")
    cases = [
        ("user_condition_328K_16.3bar", 328.15, 16.3e5, 150.0),
        ("Schbib_Table6_341K_16atm", 341.0, 16.0 * 101325.0, 150.0),
        ("341K_16.3atm_explains_1460", 341.0, 16.3 * 101325.0, 150.0),
        ("Schbib_Fig2_reference_325K_16.3atm_1400ppm", 325.0, 16.3 * 101325.0, 1400.0),
    ]
    for label, temperature_k, pressure_pa, co_ppm in cases:
        result = schbib_terms(temperature_k, pressure_pa, co_ppm)
        print(f"\n[{label}]")
        for key, value in result.items():
            print(f"{key}={value}")

    print("\n[Schbib_Table8_isothermal_PFR_1g_at_SV100]")
    for label, temperature_k, pressure_pa in (
        ("user_condition_328.15K_16.3bar", 328.15, 16.3e5),
        ("Table6_condition_341K_16atm", 341.0, 16.0 * 101325.0),
    ):
        for n_steps in (1000, 10000):
            xa, xe = schbib_isothermal_pfr(temperature_k, pressure_pa, 150.0, n_steps)
            print(f"{label}, n_steps={n_steps}, X_C2H2_pct={100*xa}, X_C2H4_pct={100*xe}")

    print("\n[upwind_numerical_dispersion]")
    for n_cells in (50, 100):
        for peclet in (17.0, 400.0):
            ratio = peclet / (2.0 * n_cells)
            print(f"N={n_cells}, Pe={peclet:g}, Dnum_over_Dax={ratio:g}")
    print("N_for_Dnum_le_Dax_at_Pe400=200")
    print("N_for_Dnum_le_0.1Dax_at_Pe400=2000")

    print("\n[Gobbo_minus_Schbib_log10_preexponent]")
    deltas = {"acetylene": (27.4, 31.1), "ethylene": (23.3, 26.6),
              "hydrogen": (17.2, 20.2), "CO": (10.2, 13.6)}
    for species, (gobbo, schbib) in deltas.items():
        print(f"{species}={gobbo - schbib:+.1f}")


if __name__ == "__main__":
    main()
