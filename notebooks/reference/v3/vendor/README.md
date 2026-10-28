# Vendored V2 reactor engine

`pbr/` is copied without source edits from `AsapLoso/Methanol-Catalysis` at
commit `2ee0dc1a84529d6830dcc628fc771878907fb22c`, the exact revision used by
the V2 input notebook. The blob SHA for each of the 11 Python modules is in
[`../SOURCE_MANIFEST.md`](../SOURCE_MANIFEST.md). V1 and V2 share a path but
are distinct Git objects; this vendor copy follows V2 only.

V3 selects the V2 engine's `Uniform`, `NoExternalResistance`,
`NoDispersion`, and `AlgebraicEquilibrium` closures. It passes zero-valued
diffusivity sentinels because the Uniform closure has no radial state and the
RHS does not read diffusivities in that branch. These sentinels are not
physical diffusivity estimates. The upstream package's parameter registry
contains a comment that describes the 13 Pa⁻¹ hydrogen constant as “resolved”;
V3 uses the Table 5 value for its fitted-model attempt while retaining the
original paper's p. 5 / Table 5 discrepancy as unresolved.
