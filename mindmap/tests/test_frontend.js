"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const graph = require("../static/graph-utils.js");
const staticDir = path.join(__dirname, "..", "static");
const html = fs.readFileSync(path.join(staticDir, "index.html"), "utf8");
const app = fs.readFileSync(path.join(staticDir, "app.js"), "utf8");
const css = fs.readFileSync(path.join(staticDir, "style.css"), "utf8");
assert.ok(html.includes('id="btn-zoom-in"'), "the map has a visible zoom-in control");
assert.ok(html.includes('id="btn-zoom-out"'), "the map has a visible zoom-out control");
assert.doesNotMatch(html, /btn-promote-node|tour-promote-btn/, "the interface has no promotion button");
assert.ok(app.includes("BepMindMapGraph.tourSequence(visibleHierarchy)"), "guided tour follows the displayed hierarchy");
assert.ok(app.includes('item.motion === "return"'), "guided tour communicates deliberate backtracking");
assert.ok(app.includes("BepMindMapGraph.focusHierarchy(root, targetId)"), "focus uses the tested ancestry-and-siblings projection");
assert.doesNotMatch(html, /id="tour-step-level"|id="tour-breadcrumb"/, "tour avoids repeating graph position already available in the drawer");
assert.ok(html.includes("sibling context"), "the focus control explains the retained siblings");
assert.ok(app.includes("function layoutHorizontalTree(root)"), "focus view lays the tree out horizontally");
assert.ok(html.includes('src="/vendor/elk-api.js"'), "the renderer loads the locally served ELK API");
assert.ok(app.includes("async function layoutOverviewWithElk(visibleNodes, visibleLinks)"), "the overview uses ELK");
assert.ok(app.includes('"elk.algorithm": "radial"'), "the grand overview uses radial placement");
assert.ok(app.includes('"elk.radial.centerOnRoot": "true"'), "the radial layout keeps the root at the center");
assert.ok(app.includes('"elk.radial.wedgeCriteria": "NODE_SIZE"') && app.includes('"elk.spacing.nodeNode": "48"'), "radial spacing accounts for node dimensions and clearance");
assert.ok(app.includes("edge.sections") && app.includes("did not return a clipped route for every visible edge"), "overview edges use ELK radial routes clipped to cards");
assert.ok(!app.includes('"elk.direction": "RIGHT"'), "the grand overview does not use a left-to-right layout");
assert.ok(app.includes("using the built-in radial fallback") && app.includes("layoutTree(visibleHierarchy);"), "an engine failure keeps the overview radial");
assert.ok(!app.includes("readable horizontal tree fallback"), "the overview never falls back to horizontal placement");
assert.ok(graph.focusHierarchy, "focus hierarchy helper is exported for regression tests");
assert.ok(css.includes(".node-square.root-square") && css.includes("stroke-width: 5px !important"), "the overview root has a strong visible anchor");
assert.ok(css.lastIndexOf(".node-square.branch-anchor") > css.indexOf(".node-square.stage-idea"), "top-level anchors retain their stronger border over stage colors");
assert.ok(css.includes(".tree-link.selected-path") && css.includes("stroke-width: 5px"), "the selected ancestry is emphasized");
assert.ok(app.includes('tourDragHandle.addEventListener("pointerdown"'), "guided tour can be dragged");
assert.ok(app.includes('tourDragHandle.addEventListener("keydown"'), "guided tour can be moved by keyboard");
assert.ok(css.includes(".node-title {") && css.includes("font-size: 15px;"), "map labels use a readable size");
assert.ok(css.includes('.map-source-status[data-map-mode="owner"]'), "the personal map has a distinct status treatment");
assert.ok(html.includes('id="drawer-audit-details"') && html.includes("Technical details and source audit"), "technical metadata starts behind an explicit disclosure");
assert.ok(html.includes('id="drawer-reader-section"') && html.includes('id="reader-content"'), "owner reader pages have a primary content surface");
assert.ok(html.includes('id="drawer-background-details"') && html.includes("Hidden background files"), "background files require a separate disclosure");
assert.ok(html.includes('id="reference-panel"') && html.includes("Separate AI reference snapshot"), "AI reference material uses its own panel");
assert.doesNotMatch(html, /reference-node-preview/, "AI reference content is not embedded in the owner drawer");
assert.ok(app.includes("async function renderOwnerReader(node)"), "the selected owner reader page is loaded into the reader surface");
assert.ok(app.includes("loadBackgroundFile(selectedNodeId"), "background text loads only after its explicit action");
assert.ok(app.includes('data-search-reference=') && app.includes("activeMode === \"owner\""), "reference search is available only with an explicitly loaded owner snapshot");
assert.ok(app.includes("BepMindMapGraph.renderMarkdownSafe(data.content"), "reader Markdown passes through the safe renderer");
assert.ok(css.includes(".reference-panel") && css.includes(".audit-details"), "reference and audit surfaces have separate presentation");
const readerHtml = graph.renderMarkdownSafe('<script>alert("x")</script> ![vector](assets/path.svg) ![plot](assets/plot.png)', { allowFigures: true });
assert.ok(readerHtml.includes("&lt;script&gt;"), "reader Markdown escapes raw HTML");
assert.doesNotMatch(readerHtml, /<script>/, "reader Markdown cannot inject script elements");
assert.doesNotMatch(readerHtml, /data-reader-image-path="assets\/path\.svg"/, "SVG page assets are not exposed as figures");
assert.ok(readerHtml.includes('data-reader-image-path="assets/plot.png"'), "linked raster figures are available on demand");
const nodes = [
  { id: "root", parent: null, title: "BEP" },
  { id: "physics", parent: "root", title: "Physics" },
  { id: "chemistry", parent: "physics", title: "Reaction chemistry" },
  { id: "our_reactions", parent: "chemistry", title: "Our reactions" },
  { id: "theme_micro", parent: "our_reactions", title: "Microscopic pathways" },
  { id: "theme_viability", parent: "our_reactions", title: "Viability and conditions" },
  ...["r1", "r2", "r3"].flatMap((reaction) => [
    { id: `micro_${reaction}`, parent: "theme_micro", title: `${reaction.toUpperCase()} pathways` },
    { id: `viability_${reaction}`, parent: "theme_viability", title: `${reaction.toUpperCase()} viability` },
  ]),
  { id: "micro_r1_detail_1", parent: "micro_r1", title: "Arbitrary depth one" },
  { id: "micro_r1_detail_2", parent: "micro_r1_detail_1", title: "Arbitrary depth two" },
  ...Array.from({ length: 6 }, (_, index) => ({
    id: `micro_r1_detail_${index + 3}`,
    parent: `micro_r1_detail_${index + 2}`,
    title: `Arbitrary depth ${index + 3}`,
  })),
];

const questionNodes = nodes.filter((node) => /^(micro|viability)_r[123]$/.test(node.id));
assert.equal(questionNodes.length, 6, "the fixture has two themes and six independent R1/R2/R3 questions");
assert.deepEqual(
  graph.focusNodeIds(nodes, "micro_r1_detail_8"),
  ["root", "physics", "chemistry", "our_reactions", "theme_micro", "micro_r1", "micro_r1_detail_1", "micro_r1_detail_2", "micro_r1_detail_3", "micro_r1_detail_4", "micro_r1_detail_5", "micro_r1_detail_6", "micro_r1_detail_7", "micro_r1_detail_8"],
  "focus mode keeps the full ancestry through arbitrary depth and immediate children only",
);
assert.deepEqual(graph.focusNodeIds(nodes, "theme_micro"), [
  "root", "physics", "chemistry", "our_reactions", "theme_micro", "micro_r1", "micro_r2", "micro_r3",
]);
assert.deepEqual(graph.siblingNavigation(nodes, "micro_r2"), {
  parentId: "theme_micro",
  previousId: "micro_r1",
  nextId: "micro_r3",
  index: 1,
  count: 3,
});
assert.equal(graph.parentPath(nodes, "missing").length, 0);

const tourHierarchy = {
  id: "tour-root", parent: null, title: "Root", children: [
    { id: "a", parent: "tour-root", title: "A", children: [
      { id: "a1", parent: "a", title: "A1", children: [
        { id: "a1_child", parent: "a1", title: "A1 child", children: [] },
      ] },
      { id: "a2", parent: "a", title: "A2", children: [
        { id: "a2_child", parent: "a2", title: "A2 child", children: [] },
      ] },
    ] },
    { id: "b", parent: "tour-root", title: "B", children: [
      { id: "b1", parent: "b", title: "B1", children: [] },
    ] },
  ],
};
const tour = graph.tourSequence(tourHierarchy);
assert.deepEqual(tour.map((item) => item.id), [
  "tour-root", "a", "a1", "a1_child", "a1", "a", "a2", "a2_child",
  "a2", "a", "tour-root", "b", "b1", "b", "tour-root",
], "guided tour explores depth-first and revisits parents when backtracking");
assert.deepEqual(tour.map((item) => item.motion), [
  "enter", "enter", "enter", "enter", "return", "return", "enter", "enter",
  "return", "return", "return", "enter", "enter", "return", "return",
]);
assert.deepEqual(tour.map((item) => item.level), [0, 1, 2, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]);
assert.deepEqual(tour[3].path, ["Root", "A", "A1", "A1 child"]);
assert.deepEqual([tour[4].levelPosition, tour[4].levelCount], [1, 2], "return visits retain the actual sibling position");
assert.deepEqual(graph.tourSequence(null), []);

const focused = graph.focusHierarchy(tourHierarchy, "a1");
assert.deepEqual(focused.children.map((node) => node.id), ["a", "b"], "ancestor sibling is visible");
assert.deepEqual(focused.children[1].children, [], "ancestor sibling's descendants are hidden");
assert.deepEqual(focused.children[0].children.map((node) => node.id), ["a1", "a2"], "direct siblings remain visible");
assert.deepEqual(focused.children[0].children[1].children, [], "direct sibling's descendants are hidden");
assert.deepEqual(focused.children[0].children[0].children.map((node) => node.id), ["a1_child"], "every selected direct child remains visible");
assert.deepEqual(graph.focusHierarchy(tourHierarchy, "unknown"), tourHierarchy);

const stages = ["idea", "ai_worked_out", "human_worked_out", "informal_writing", "formal_writing"];
stages.forEach((stage) => {
  assert.equal(graph.stagePresentation({ maturity: stage }).stage, stage);
});
assert.equal(graph.stagePresentation({ tier: 2 }).legacy, true);
assert.match(graph.stagePresentation({ tier: 2 }).note, /does not establish owner understanding/i);
assert.equal(graph.stagePresentation({ maturity: "ai_worked_out", owner_content_approval: "unapproved" }).label, "AI worked out");

const provenance = graph.resolveClaimProvenance(
  {
    id: "micro_r1",
    sources: [{ id: "paper-1", title: "Example source", locator: "p. 4", review: "ai_attached", human_verified: false }],
    claims: [
      { id: "claim-1", statement: "A bounded claim.", status: "ai_attached", source_ids: ["paper-1"], human_verified: false,
        ai_reference_links: [{ reference_node_id: "ref-1", reference_claim_id: "ref-claim-1", source_id: "paper-1", human_verified: false }] },
      { id: "claim-2", statement: "Citation not yet attached.", source_ids: [] },
    ],
  },
  { nodes: [{ id: "ref-1", title: "Reference concept", claim_refs: [{ source_id: "paper-1", locator: "Section 2.3", supports: "A concise AI evidence summary." }] }], sources: [{ id: "paper-1", title: "Example reference source", access_status: "abstract_checked" }] },
);
assert.equal(provenance[0].entries[0].resolvedReferenceNode, true);
assert.equal(provenance[0].entries[0].referenceClaim.supports, "A concise AI evidence summary.");
assert.equal(provenance[0].entries[0].referenceLocator, "Section 2.3");
assert.equal(provenance[0].entries[0].linkVerification, "not_human_verified");
assert.equal(provenance[0].entries[0].locator, "p. 4");
assert.equal(provenance[0].entries[0].excerpt, null, "no quotation is invented when the source has no excerpt");
assert.equal(provenance[1].absentCitation, true);
assert.equal(provenance[1].claimVerification, "not_recorded");

console.log("Mind-map frontend helper checks passed.");
