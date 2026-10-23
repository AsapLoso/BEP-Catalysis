"use strict";

const assert = require("node:assert/strict");
const graph = require("../static/graph-utils.js");

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

const layoutById = new Map(nodes.map((node) => {
  const isRoot = node.id === "root";
  const isDeepNote = node.id.startsWith("micro_r1_detail_");
  const isLongTheme = node.id === "theme_viability";
  return [node.id, {
    ...node,
    children: [],
    w: isRoot ? 220 : (isDeepNote ? 238 : (isLongTheme ? 210 : 180)),
    h: isRoot ? 160 : (isDeepNote ? 164 : (isLongTheme ? 210 : 138)),
  }];
}));
nodes.forEach((node) => {
  if (node.parent) layoutById.get(node.parent).children.push(layoutById.get(node.id));
});
const layoutRoot = layoutById.get("root");
const cardGap = 24;
function visibleLayoutNodes(node, collapsed = new Set()) {
  const visible = [node];
  if (!collapsed.has(node.id)) {
    (node.children || []).forEach((child) => visible.push(...visibleLayoutNodes(child, collapsed)));
  }
  return visible;
}
function assertNoCardOverlaps(visible, context) {
  for (let left = 0; left < visible.length; left += 1) {
    for (let right = left + 1; right < visible.length; right += 1) {
      const first = visible[left];
      const second = visible[right];
      const overlaps = Math.abs(first.x + first.w / 2 - second.x - second.w / 2) < (first.w + second.w) / 2 + cardGap
        && Math.abs(first.y + first.h / 2 - second.y - second.h / 2) < (first.h + second.h) / 2 + cardGap;
      assert.equal(overlaps, false, `${context}: ${first.id} and ${second.id} overlap`);
    }
  }
}

graph.layoutRadialTree(layoutRoot, new Set(), {
  gap: cardGap,
  nodeWidth: 180,
  nodeHeight: 138,
  rootWidth: 220,
  rootHeight: 160,
});
assert.equal(layoutRoot.weight, 6, "branch weights follow the six currently visible question leaves");
const themeAngleDelta = Math.abs(Math.atan2(
  Math.sin(layoutById.get("theme_micro").angle - layoutById.get("theme_viability").angle),
  Math.cos(layoutById.get("theme_micro").angle - layoutById.get("theme_viability").angle),
));
assert.ok(Math.abs(themeAngleDelta - Math.PI) < 1e-10, "the two equal-sized theme branches receive balanced radial space");
assertNoCardOverlaps(visibleLayoutNodes(layoutRoot), "expanded hierarchy with variable card sizes");

const collapsedLayoutNodes = new Set(["theme_micro"]);
graph.layoutRadialTree(layoutRoot, collapsedLayoutNodes, { gap: cardGap });
assert.equal(layoutRoot.weight, 4, "collapsing a branch gives its hidden descendants no display weight");
assertNoCardOverlaps(visibleLayoutNodes(layoutRoot, collapsedLayoutNodes), "hierarchy with a collapsed branch");

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

const stages = ["idea", "ai_worked_out", "human_worked_out", "informal_writing", "formal_writing"];
stages.forEach((stage) => {
  assert.equal(graph.stagePresentation({ maturity: stage }).stage, stage);
});
assert.equal(graph.stagePresentation({ tier: 2 }).legacy, true);
assert.match(graph.stagePresentation({ tier: 2 }).note, /does not establish owner understanding/i);
assert.equal(graph.stagePresentation({ maturity: "ai_worked_out", owner_content_approval: "unapproved" }).label, "AI worked out");

const readerHtml = graph.renderMarkdownSafe([
  "## Reader page",
  "A **bounded** scientific note with `k = 1` and [a source](https://example.org/paper).",
  "",
  "- First point",
  "- Second point",
  "",
  "![Surface diagram](figures/surface.webp)",
  "[unsafe](javascript:alert(1)) <script>alert(1)</script>",
].join("\n"));
assert.match(readerHtml, /<h3>Reader page<\/h3>/);
assert.match(readerHtml, /<strong>bounded<\/strong>/);
assert.match(readerHtml, /href="https:\/\/example\.org\/paper"/);
assert.match(readerHtml, /<ul><li>First point<\/li><li>Second point<\/li><\/ul>/);
assert.match(readerHtml, /data-reader-image-path="figures\/surface\.webp"/);
assert.doesNotMatch(readerHtml, /<img\b/i, "reader figures do not load until the user asks to show them");
assert.doesNotMatch(readerHtml, /href="javascript:/i);
assert.match(readerHtml, /&lt;script&gt;/, "raw HTML in Markdown is rendered as text");
assert.doesNotMatch(
  graph.renderMarkdownSafe("![Figure](figures/no-reader-file.png)", { allowFigures: false }),
  /reader-figure-button/,
);

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
