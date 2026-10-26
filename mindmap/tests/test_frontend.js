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
assert.ok(!app.includes('item.motion === "return"'), "guided tour does not insert backtracking steps between siblings");
assert.ok(app.includes("BepMindMapGraph.focusHierarchy(root, targetId)"), "focus uses the tested ancestry-and-siblings projection");
assert.doesNotMatch(html, /id="tour-step-level"|id="tour-breadcrumb"/, "tour avoids repeating graph position already available in the drawer");
assert.ok(html.includes("sibling context"), "the focus control explains the retained siblings");
assert.ok(app.includes("function layoutHorizontalTree(root)"), "focus view lays the tree out horizontally");
assert.ok(html.includes('src="/vendor/elk-api.js"'), "the renderer loads the locally served ELK API");
assert.ok(html.includes('id="layout-error"') && app.includes('layoutError.classList.remove("hidden")'), "renderer failures are visible and do not silently draw misleading edges");
assert.ok(app.includes("async function layoutOverviewWithElk(visibleNodes, visibleLinks)"), "the overview uses ELK");
assert.ok(app.includes('"elk.algorithm": "radial"'), "the grand overview uses radial placement");
assert.ok(app.includes('"elk.radial.centerOnRoot": "true"'), "the radial layout keeps the root at the center");
assert.ok(app.includes('"elk.radial.wedgeCriteria": "LEAF_NUMBER"') && app.includes("BepMindMapGraph.radialSectorPadding(visibleNodes, visibleLinks)"), "the radial layout balances current root branches to equal sectors");
assert.ok(app.includes('"elk.spacing.nodeNode": "48"') && app.includes('"elk.spacing.edgeNode": "28"'), "ELK retains node-size-aware clearance");
assert.ok(app.includes("BepMindMapGraph.elkEdgePath(edge, offsetX, offsetY)") && app.includes("did not return a clipped route for every visible edge"), "overview edges use ELK radial routes clipped to cards");
assert.ok(!app.includes('"elk.direction": "RIGHT"'), "the grand overview does not use a left-to-right layout");
assert.doesNotMatch(app, /overviewFallbackPath|layoutTree\(/, "the overview has no custom overlapping-line fallback");
assert.doesNotMatch(app, /SCIENTIFIC_ARM_IDS|physics.*mathematics.*systems_control/, "root branches are discovered from the loaded map");
assert.ok(app.includes("new URLSearchParams(window.location.search)") && app.includes("layerSelect.value = requestedMode"), "launcher URLs can select an available map mode");
assert.ok(app.includes("function positionTourPanel()") && app.includes("BepMindMapGraph.chooseOverlayPosition") && app.includes('tourDragHandle.addEventListener("pointerdown"'), "guided review avoids map panels/nodes and remains movable");
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
function makeBranchFixture(leafCounts) {
  const nodes = [{ id: "map-root", parent: null, title: "Map root" }];
  const links = [];
  leafCounts.forEach((leafCount, branchIndex) => {
    const branchId = "branch-" + (branchIndex + 1);
    nodes.push({ id: branchId, parent: "map-root", title: "Branch " + (branchIndex + 1) });
    links.push({ source: "map-root", target: branchId });
    for (let leafIndex = 0; leafIndex < leafCount; leafIndex += 1) {
      let parentId = branchId;
      if ((branchIndex + leafIndex) % 2 === 0) {
        const groupId = "group-" + (branchIndex + 1) + "-" + (leafIndex + 1);
        nodes.push({ id: groupId, parent: parentId, title: "Nested group" });
        links.push({ source: parentId, target: groupId });
        parentId = groupId;
      }
      if (branchIndex === 0 && leafIndex === 0) {
        for (let depth = 1; depth <= 6; depth += 1) {
          const deepId = "deep-" + depth;
          nodes.push({ id: deepId, parent: parentId, title: "Depth " + depth });
          links.push({ source: parentId, target: deepId });
          parentId = deepId;
        }
      }
      const itemId = "item-" + (branchIndex + 1) + "-" + (leafIndex + 1);
      nodes.push({ id: itemId, parent: parentId, title: "Question item" });
      links.push({ source: parentId, target: itemId });
    }
  });
  return { nodes, links };
}

const fixtureCases = [[1], [2, 5], [1, 4, 7, 3]];
fixtureCases.forEach((counts) => {
  const fixture = makeBranchFixture(counts);
  const padding = graph.radialSectorPadding(fixture.nodes, fixture.links);
  assert.equal(padding.sectors.length, counts.length, "the layout discovers each current root child");
  assert.equal(new Set(padding.sectors.map((sector) => sector.targetLeafCount)).size, counts.length ? 1 : 0, "all current root branches receive equal leaf weight");
  assert.deepEqual(padding.sectors.map((sector) => sector.leafCount), counts, "unequal branch sizes are measured from visible edges");
  const expectedPaddingCount = padding.sectors.reduce((sum, sector) => {
    const missing = padding.targetLeafCount - sector.leafCount;
    return sum + (missing > 0 ? missing + 1 : 0);
  }, 0);
  assert.equal(padding.nodes.length, expectedPaddingCount, "only enough transient leaves are added to balance sectors");
  assert.equal(padding.edges.length, padding.nodes.length, "each transient layout leaf has one private layout edge");
  assert.ok(padding.nodes.every((node) => node.layoutOnly), "balancing leaves are labelled as layout-only data");
  assert.equal(new Set([...fixture.nodes, ...padding.nodes].map((node) => node.id)).size, fixture.nodes.length + padding.nodes.length, "transient node IDs cannot collide with source IDs");
  const balanced = graph.radialSectorPadding([...fixture.nodes, ...padding.nodes], [...fixture.links, ...padding.edges]);
  assert.ok(balanced.sectors.every((sector) => sector.leafCount === padding.targetLeafCount), "the augmented ELK input now has equal root-sector leaf counts");
  assert.equal(balanced.nodes.length, 0, "balanced input needs no second round of synthetic nodes");
});

const expandedFixture = makeBranchFixture([3, 5, 2]);
const collapsedBranchId = "branch-1";
const descendants = new Set([collapsedBranchId]);
let changed = true;
while (changed) {
  changed = false;
  expandedFixture.links.forEach((link) => {
    if (descendants.has(link.source) && !descendants.has(link.target)) {
      descendants.add(link.target);
      changed = true;
    }
  });
}
const collapsedNodes = expandedFixture.nodes.filter((node) => !descendants.has(node.id) || node.id === collapsedBranchId);
const collapsedLinks = expandedFixture.links.filter((link) => collapsedNodes.some((node) => node.id === link.source) && collapsedNodes.some((node) => node.id === link.target));
const collapsedPadding = graph.radialSectorPadding(collapsedNodes, collapsedLinks);
assert.equal(collapsedPadding.sectors[0].leafCount, 1, "a collapsed root child is one visible sector leaf");
assert.equal(collapsedPadding.sectors.length, 3, "collapse keeps all root siblings visible");
assert.equal(graph.radialSectorPadding(expandedFixture.nodes, expandedFixture.links).sectors.length, 3, "expanding restores the same data-driven sectors");
const deepPath = graph.parentPath(expandedFixture.nodes, "item-1-1");
assert.ok(deepPath.length >= 8, "the fixture exercises a branch at arbitrary depth");
assert.deepEqual(graph.focusNodeIds(expandedFixture.nodes, "item-1-1"), deepPath.map((node) => node.id), "focus keeps the full arbitrary-depth ancestry");
assert.deepEqual(graph.siblingNavigation(expandedFixture.nodes, "branch-2"), {
  parentId: "map-root", previousId: "branch-1", nextId: "branch-3", index: 1, count: 3,
});
assert.equal(graph.parentPath(expandedFixture.nodes, "missing").length, 0);
assert.equal(graph.radialSectorPadding([], []).nodes.length, 0);

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
  "tour-root", "a", "b", "a1", "a2", "b1", "a1_child", "a2_child",
], "guided tour shows every sibling level before descending");
assert.deepEqual(tour.map((item) => item.level), [0, 1, 1, 2, 2, 2, 3, 3], "tour order never descends before the current level is complete");
assert.deepEqual(tour[3].path, ["Root", "A", "A1"]);
assert.deepEqual([tour[4].levelPosition, tour[4].levelCount], [2, 2], "siblings retain their actual position in the parent");
assert.ok(tour.every((item) => !Object.hasOwn(item, "motion")), "level-order review has no misleading backtracking events");
assert.deepEqual(graph.tourSequence(null), []);

const focused = graph.focusHierarchy(tourHierarchy, "a1");
assert.deepEqual(focused.children.map((node) => node.id), ["a", "b"], "ancestor sibling is visible");
assert.deepEqual(focused.children[1].children, [], "ancestor sibling's descendants are hidden");
assert.deepEqual(focused.children[0].children.map((node) => node.id), ["a1", "a2"], "direct siblings remain visible");
assert.deepEqual(focused.children[0].children[1].children, [], "direct sibling's descendants are hidden");
assert.deepEqual(focused.children[0].children[0].children.map((node) => node.id), ["a1_child"], "every selected direct child remains visible");
assert.deepEqual(graph.focusHierarchy(tourHierarchy, "unknown"), tourHierarchy);

const overlay = graph.chooseOverlayPosition(
  { width: 640, height: 420 },
  { width: 240, height: 140 },
  [
    { left: 0, top: 0, right: 320, bottom: 210 },
    { left: 450, top: 0, right: 640, bottom: 420, weight: 100 },
  ],
);
assert.equal(overlay.overlapArea, 0, "the tour card can find a clear region between map nodes and a side panel");
assert.ok(overlay.left >= 12 && overlay.top >= 12 && overlay.left + overlay.width <= 628 && overlay.top + overlay.height <= 408, "tour placement remains inside the available surface");

const elkRoute = graph.elkEdgePath({
  sections: [{
    startPoint: { x: 110, y: 220 },
    bendPoints: [{ x: 130, y: 240 }],
    endPoint: { x: 150, y: 260 },
  }],
}, 100, 200);
assert.equal(elkRoute, "M 10.0 20.0 L 30.0 40.0 L 50.0 60.0", "ELK bend points and offsets are kept in the rendered SVG route");
assert.equal(graph.elkEdgePath({ sections: [] }), "", "an absent ELK route is never synthesized");

const stages = ["idea", "ai_worked_out", "human_worked_out", "informal_writing", "formal_writing"];
stages.forEach((stage) => {
  assert.equal(graph.stagePresentation({ maturity: stage }).stage, stage);
});
assert.equal(graph.stagePresentation({ tier: 2 }).legacy, true);
assert.match(graph.stagePresentation({ tier: 2 }).note, /does not establish owner understanding/i);
assert.equal(graph.stagePresentation({ maturity: "ai_worked_out", owner_content_approval: "unapproved" }).label, "AI worked out");

const provenance = graph.resolveClaimProvenance(
  {
    id: "synthetic_concept",
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
