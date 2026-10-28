"""Rate laws, one per literature parameterisation, behind one interface.

Rate laws return gas production rates and optional surface-coverage targets.
Schbib's published macro-kinetics do not provide elementary adsorption rates,
so the Schbib V4 case uses a transparent finite-relaxation extension of the
reported H/CO adsorption equilibrium. Its relaxation time is a declared
scenario assumption, not a fitted or literature rate constant. The reactor
gas, pore and surface inventories remain ODE states when their closures are
enabled; the V4 notebook uses `Relaxation`, never `AlgebraicEquilibrium`.

Interface. `rates` takes partial pressures in Pa and returns

    gas[i]     mol/(kg_cat s)  net production of gas species i
    surface[j] 1/s             net production of coverage j (per site)

Both are *already* normalised to per kilogram of catalyst. Sources publish per
gram, per mole of metal, or per kilogram; the conversion lives in
`KineticSet.mass_scale` / `site_basis`, so no expression below carries a unit
conversion. `r_1max` is the one exception: it is a rate rather than a
pressure-dependent coefficient, so it is not divided by `pressure_scale`.

All three laws are monotone in hydrogen and *decrease* in acetylene over part
of their range -- the rate maximum the sources both report. Preserving that
non-monotonicity is the point: a model in which the rate rises monotonically
in its own reactant cannot exhibit the competitive-adsorption regime that
makes periodic operation worth studying.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, runtime_checkable

import numpy as np
from numpy.typing import NDArray

from pbr.parameters import (
    Borodzinski2000,
    KineticSet,
    Larsen2024,
    R_GAS,
    Schbib1996,
    Urmes2019,
)
from pbr.species import GASES, IGAS


@dataclass(frozen=True, slots=True)
class RateResult:
    """Volumetric rates out of the rate law.

    `gas` and `surface` are stacked rather than returned separately so a caller
    cannot get one without the other -- they are never independently meaningful.
    """

    gas: NDArray[np.float64]
    """Shape (..., 5) in the order of `pbr.species.GASES`. mol/(kg_cat s)."""

    surface: NDArray[np.float64]
    """Shape (..., 4) for H*, C2H2*, C2H4*, CO*. 1/s."""

    @property
    def has_surface(self) -> bool:
        return bool(np.any(self.surface))


@runtime_checkable
class RateLaw(Protocol):
    """A rate law. The only thing `rhs` needs to know about chemistry."""

    @property
    def name(self) -> str: ...

    def rates(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
        surface: NDArray[np.float64] | None = None,
    ) -> RateResult:
        """Evaluate at partial pressures in Pa.

        `pressures` broadcasts over leading axes, so a (N_z, N_r) stack of
        local pressures gives a (N_z, N_r, 5) result without a Python loop.
        Dynamic laws may use the current coverage state supplied in `surface`.
        """

    def coverages(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
    ) -> NDArray[np.float64] | None:
        """Quasi-steady adsorbed fractions in the order H*, C2H2*, C2H4*.

        `None` when the parameter set does not permit recovery. The two-site
        model is the case that cannot: its constants are products of
        elementary constants, so the individual site populations are not
        identifiable from the published numbers. Returning `None` rather than
        an approximate answer is deliberate.
        """


def _pressures(p: NDArray[np.float64]) -> dict[str, NDArray[np.float64]]:
    """Pull the four reactive partial pressures out of an array."""
    return {name: p[..., IGAS[name]] for name in GASES if name != "H2"} | {
        "H2": p[..., IGAS["H2"]]
    }


def _gas_stack(
    h2: NDArray[np.float64],
    c2h2: NDArray[np.float64],
    c2h4: NDArray[np.float64],
    c2h6: NDArray[np.float64],
    co: NDArray[np.float64] | None = None,
) -> NDArray[np.float64]:
    if co is None:
        co = np.zeros_like(h2)
    return np.stack([h2, c2h2, c2h4, c2h6, co], axis=-1)


# --- Larsen 2024 ------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Larsen2024Rate:
    """Extended LHHW with a saturating primary rate.

    The two empirical pieces are kept verbatim because they are the reason this
    model exists. Plain LHHW cannot fit these experiments: `k1` and `K_C2H2`
    trade off against each other so completely that the fitted pair predicts
    total conversion at every operating point, which is a curve that carries
    no information. The saturation cap `r_1max` and the free inhibition
    exponent `n_inh` are what make the fit mean something.

    The cap is written as a Michaelis-Menten saturation rather than a hard
    `min()`, because a hard clip is discontinuous in `p_C2H2` and would make
    the integrator take vanishing steps every time the rate crosses it.
    """

    params: Larsen2024

    @property
    def name(self) -> str:
        return "Larsen2024 (extended LHHW, rate saturation + acetylene inhibition)"

    @property
    def _k1(self) -> float:
        return self.params.rate_constant("k1")

    @property
    def _k2(self) -> float:
        return self.params.rate_constant("k2")

    @property
    def _r_cap(self) -> float:
        """The cap, on the model's own per-kilogram basis.

        Not divided by `pressure_scale`: it is a rate, not a coefficient with
        pressure factors in it.
        """
        return self.params.r_1max * self.params.mass_scale * self.params.site_basis

    def rates(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
        surface: NDArray[np.float64] | None = None,
    ) -> RateResult:
        p = pressures
        ph2 = p[..., IGAS["H2"]]
        pa = p[..., IGAS["C2H2"]]
        pb = p[..., IGAS["C2H4"]]

        k_acetylene = self.params.adsorption_constant("C2H2")
        k_ethylene = self.params.adsorption_constant("C2H4")
        k_hydrogen = self.params.adsorption_constant("H2")
        k_inh = self.params.adsorption_constant("inh")

        theta_star = 1.0 + k_acetylene * pa + k_ethylene * pb + k_hydrogen * ph2

        r1_raw = self._k1 * k_acetylene * pa * k_hydrogen * ph2 / theta_star**2
        # Saturating cap. Strictly monotone in r1_raw, smooth at the cap.
        r1 = r1_raw / (1.0 + r1_raw / self._r_cap)

        # Ethylene hydrogenation, with acetylene poisoning the site. The
        # denominator is split as the source writes it: the competitive
        # Langmuir term excludes hydrogen, the inhibition term is separate.
        inhibition = (1.0 + k_inh * pa) ** self.params.n_inh
        r2 = (
            self._k2
            * k_ethylene
            * pb
            * k_hydrogen
            * ph2
            / ((1.0 + k_acetylene * pa + k_ethylene * pb) * inhibition)
        )

        zeros = np.zeros_like(ph2)
        return RateResult(
            gas=_gas_stack(
                -r1 - r2,  # H2
                -r1,  # C2H2
                +r1 - r2,  # C2H4
                +r2,  # C2H6
            ),
            surface=np.stack([zeros, zeros, zeros, zeros], axis=-1),
        )

    def coverages(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
    ) -> NDArray[np.float64] | None:
        """Competitive Langmuir isotherm on a single site type.

        Recoverable because the source reports `K` per species instead of only
        as products. The sum is 1, so the vacant-site fraction needs no separate
        balance.
        """
        p = pressures
        ph2 = p[..., IGAS["H2"]]
        pa = p[..., IGAS["C2H2"]]
        pb = p[..., IGAS["C2H4"]]

        w_h2 = self.params.adsorption_constant("H2") * ph2
        w_c2h2 = self.params.adsorption_constant("C2H2") * pa
        w_c2h4 = self.params.adsorption_constant("C2H4") * pb
        denom = 1.0 + w_h2 + w_c2h2 + w_c2h4
        zero = np.zeros_like(w_h2)
        return np.stack([w_h2 / denom, w_c2h2 / denom, w_c2h4 / denom, zero], axis=-1)


# --- Borodzinski & Cybulski 2000 --------------------------------------------


@dataclass(frozen=True, slots=True)
class Borodzinski2000Rate:
    """Two-site model: narrow A sites and wide E sites.

    The mechanism this encodes is geometric, not electronic. Carbonaceous
    deposits on the palladium leave crevices wide enough for acetylene to adsorb
    perpendicularly and for hydrogen atoms to move in, but too narrow for
    ethylene to lie flat. Acetylene is therefore hydrogenated to ethylene on
    sites ethylene cannot occupy, and only the small fraction that does reach an
    E site is over-hydrogenated to ethane.

    That is also why the model has no `A`-site constant for ethylene, and why
    the acetylene-to-ethylene adsorption ratio on E sites is about 2000: trace
    acetylene displaces ethylene and shuts down the undesired reaction. The
    dimensionless ratio `K_C2H2_E / K_C2H4_E` is the single most important
    number in the mechanism, and it is a *ratio*, so unlike the individual
    constants it survives a pressure-unit error.
    """

    params: Borodzinski2000
    site_basis: float = 1.0
    """Metal site density [mol_Pd/kg_cat], injected by the model."""

    @property
    def name(self) -> str:
        return "Borodzinski2000 (two-site LHHW, A/E site populations)"

    def _k(self, index: int) -> float:
        return self.params.rate_constant(f"k{index}")

    def rates(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
        surface: NDArray[np.float64] | None = None,
    ) -> RateResult:
        p = pressures
        ph2 = p[..., IGAS["H2"]]
        pa = p[..., IGAS["C2H2"]]
        pb = p[..., IGAS["C2H4"]]

        ka = self.params.adsorption_constant("C2H2_A")
        ke_a = self.params.adsorption_constant("C2H2_E")
        ke_b = self.params.adsorption_constant("C2H4_E")

        # A-site isotherm: acetylene only.
        a_denom = 1.0 + ka * pa
        a1 = a_denom**1
        a2 = a_denom**2
        a3 = a_denom**3
        # E-site isotherm: everything competes.
        e_denom = 1.0 + ke_a * pa + ke_b * pb
        e2 = e_denom**2

        # r1: acetylene -> ethane on A sites, three-point adsorption.
        r1 = self._k(1) * pa * ph2**2 / a3
        # r2: ethylene -> ethane on E sites.
        r2 = self._k(2) * pb * ph2 / e2
        # r3: acetylene -> ethylene by non-competitive hydrogen transfer.
        r3 = self._k(3) * pa * ph2 / a1
        # r4: acetylene -> ethylene, competitive, two-point adsorption.
        r4 = self._k(4) * pa * ph2 / a2
        # r5: acetylene dimerisation / oligomerisation to C4.
        r5 = self._k(5) * pa**2 * ph2 / a3

        # Carbon balance. Each C2 carries two carbons, so ethane formation from
        # either C2H2 or C2H4 gives one ethane molecule.
        c2h4_net = r3 + r4 + 2.0 * r5 - r2
        c2h2_net = -(r1 + r3 + r4 + 2.0 * r5)
        c2h6_net = r1 + r2
        h2_net = -(2.0 * r1 + r2 + r3 + r4 + r5)

        zeros = np.zeros_like(ph2)
        return RateResult(
            gas=_gas_stack(h2_net, c2h2_net, c2h4_net, c2h6_net),
            surface=np.stack([zeros, zeros, zeros, zeros], axis=-1),
        )

    def coverages(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
    ) -> NDArray[np.float64] | None:
        """Not recoverable, and the reason is worth stating.

        The published constants are products: `k1 = k8 K_C2H2^A K5 K7 (K_H2^A)^2`
        and so on. The elementary constants are not reported, so there is more
        than one set of coverages consistent with the same `k`. Inverting the
        published denominators would silently assume one particular choice of
        elementary constants, which is a claim the source does not make.
        """
        return None


# --- Schbib et al. 1996 ----------------------------------------------------


@dataclass(frozen=True, slots=True)
class Schbib1996Rate:
    """CO-competitive Schbib kinetics with a dynamic H/CO site inventory.

    At equilibrium the free-site fraction is exactly
    ``1 / (1 + sqrt(KH C_H2) + KCO C_CO)``; cubing it recovers the source's
    reduced equations (24-25). With `surface` supplied, rates use the current
    free-site fraction and the coverage states lag their adsorption targets.
    The relaxation closure supplies the declared timescale.
    """

    params: Schbib1996

    @property
    def name(self) -> str:
        return "Schbib1996 (CO-competitive LH with dynamic H/CO adsorption)"

    def rates(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
        surface: NDArray[np.float64] | None = None,
    ) -> RateResult:
        p = np.maximum(pressures, 0.0)
        c_total = p / (1.0e3 * R_GAS * temperature)  # kmol/m^3
        c_h2 = c_total[..., IGAS["H2"]]
        c_c2h2 = c_total[..., IGAS["C2H2"]]
        c_c2h4 = c_total[..., IGAS["C2H4"]]
        c_co = c_total[..., IGAS["CO"]]

        if surface is None:
            kh = self.params.adsorption_constant_at("KH", temperature)
            kco = self.params.adsorption_constant_at("KCO", temperature)
            free_site = 1.0 / (1.0 + np.sqrt(kh * c_h2) + kco * c_co)
        else:
            # Surface order: H*, C2H2*, C2H4*, CO*. Schbib's reduced
            # denominator drops the two hydrocarbon adsorption terms.
            occupied = np.clip(surface[..., 0] + surface[..., 3], 0.0, 1.0)
            free_site = 1.0 - occupied

        rate_scale = self.params.mass_scale * 1.0e3  # g->kg and kmol->mol
        k_a = self.params.arrhenius_rate_constant("kA", temperature)
        k_e = self.params.arrhenius_rate_constant("kE", temperature)
        r_a = rate_scale * k_a * c_c2h2 * c_h2 * free_site**3
        r_e = rate_scale * k_e * c_c2h4 * c_h2 * free_site**3

        zeros = np.zeros_like(c_h2)
        return RateResult(
            gas=_gas_stack(-r_a - r_e, -r_a, r_a - r_e, r_e, zeros),
            surface=np.zeros(c_h2.shape + (4,), dtype=float),
        )

    def coverages(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
    ) -> NDArray[np.float64]:
        p = np.maximum(pressures, 0.0)
        concentration = p / (1.0e3 * R_GAS * temperature)  # kmol/m^3
        kh = self.params.adsorption_constant_at("KH", temperature)
        kco = self.params.adsorption_constant_at("KCO", temperature)
        h_weight = np.sqrt(kh * concentration[..., IGAS["H2"]])
        co_weight = kco * concentration[..., IGAS["CO"]]
        free = 1.0 / (1.0 + h_weight + co_weight)
        zero = np.zeros_like(free)
        return np.stack([h_weight * free, zero, zero, co_weight * free], axis=-1)


# --- Urmes et al. 2019 ------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Urmes2019Rate:
    """Single-site Horiuti-Polanyi sequential hydrogen addition.

    Both transformations run through adsorbed intermediates: acetylene adsorbs,
    takes one hydrogen, takes a second; ethylene adsorbs and does the same.
    Ethylene is the *intermediate* of the wanted reaction and the *reactant* of
    the unwanted one, which is what makes this chemistry hard: the same
    species has to be made fast and consumed slow.

    Dissociative adsorption is visible in the square root on hydrogen in the
    denominator but not in the numerator. That asymmetry is the source's, not a
    typo introduced here -- hydrogen is first adsorbs atomically onto a site
    pair, so coverage goes as `sqrt(p)`, while the reacting step sees a
    hydrogen-covered surface whose dependence enters through the total coverage
    term.

    This is the only set with activation energies, so it is the only one whose
    rates respond to temperature. `arrhenius` is evaluated at the temperature
    passed in, centred on the temperature the set was fitted at.
    """

    params: Urmes2019

    @property
    def name(self) -> str:
        return "Urmes2019 (single-site Horiuti-Polanyi LHHW, Arrhenius)"

    def rates(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
        surface: NDArray[np.float64] | None = None,
    ) -> RateResult:
        # `arrhenius` returns mol/(mol_Pd_s s); multiplying by the reported
        # site density gives mol/(kg_cat s), the model's working unit.
        k4 = self.params.arrhenius("k04", temperature) * self.params.site_density
        k7 = self.params.arrhenius("k07", temperature) * self.params.site_density

        p = np.maximum(pressures, 0.0)
        ph2 = p[..., IGAS["H2"]]
        pa = p[..., IGAS["C2H2"]]
        pb = p[..., IGAS["C2H4"]]

        sqrt_h2 = np.sqrt(max(self.params.K_H2, 0.0) * ph2)
        k_c2h2 = self.params.K_C2H2
        desorption = pb / self.params.K_C2H4_des

        denom = 1.0 + sqrt_h2 + k_c2h2 * pa + desorption
        denom2 = denom**2

        # Acetylene hydrogenation to ethylene. `k4` arrives already multiplied
        # by N_S, so this is `N_S k04 exp(-E4/RT) K_1 K_2 P P / theta_star^2`.
        r1 = k4 * self.params.K_H2 * k_c2h2 * pa * ph2 / denom2
        # Ethylene hydrogenation to ethane. The source carries an explicit
        # `(K_1 / K_5)` factor, which is *not* folded into `k07`: `k07` is a
        # bare pre-exponential and the source's own expression keeps the ratio
        # separate. Dropping it -- as an earlier version of this file did,
        # having assumed the constant was composite like Borodzinski's -- costs
        # a factor of `K_1 / K_5 = 1.8 Pa^-1` on every ethane rate, which is
        # precisely the reaction whose selectivity is the point of the study.
        r2 = k7 * (self.params.K_H2 / self.params.K_C2H4_des) * pb * ph2 / denom2

        zeros = np.zeros_like(ph2)
        return RateResult(
            gas=_gas_stack(
                -(r1 + r2),
                -r1,
                +(r1 - r2),
                +r2,
            ),
            surface=np.stack([zeros, zeros, zeros, zeros], axis=-1),
        )

    def coverages(
        self,
        pressures: NDArray[np.float64],
        temperature: float,
    ) -> NDArray[np.float64] | None:
        """Langmuir coverages, directly from the reported adsorption constants.

        The source publishes the operating-range coverages alongside the rate
        data, so this is directly checkable against them -- one of the few
        places in the model where a computed quantity has an independent
        published value to be wrong against.
        """
        p = pressures
        ph2 = p[..., IGAS["H2"]]
        pa = p[..., IGAS["C2H2"]]
        pb = p[..., IGAS["C2H4"]]

        w_h = np.sqrt(self.params.K_H2 * ph2)
        w_c2h2 = self.params.K_C2H2 * pa
        w_c2h4 = pb / self.params.K_C2H4_des
        denom = 1.0 + w_h + w_c2h2 + w_c2h4
        zero = np.zeros_like(w_h)
        return np.stack([w_h / denom, w_c2h2 / denom, w_c2h4 / denom, zero], axis=-1)


def rate_law(
    params: KineticSet,
    site_basis: float = 1.0,
    temperature: float | None = None,
) -> RateLaw:
    """Build the rate law matching a parameter set.

    `site_basis` is the metal site density for sets published per mole of metal
    and is ignored by sets published per kilogram of catalyst.
    """
    match params:
        case Larsen2024():
            return Larsen2024Rate(params)
        case Borodzinski2000():
            if site_basis <= 0.0:
                raise ValueError(
                    "Borodzinski2000 rates are per mole of palladium; the "
                    "catalyst declares no metal loading, so they cannot be "
                    "converted to a volumetric rate."
                )
            return Borodzinski2000Rate(params, site_basis=site_basis)
        case Urmes2019():
            return Urmes2019Rate(params)
        case Schbib1996():
            return Schbib1996Rate(params)
    raise TypeError(f"no rate law implemented for {type(params).__name__}")


__all__ = [
    "Borodzinski2000Rate",
    "Larsen2024Rate",
    "RateLaw",
    "RateResult",
    "Schbib1996Rate",
    "Urmes2019Rate",
    "rate_law",
]
