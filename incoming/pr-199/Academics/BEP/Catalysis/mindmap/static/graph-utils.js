/* Pure graph/data helpers shared by the existing viewer and Node regression tests. */
(function (root) {
  "use strict";

  const STAGE_LABELS = {
    idea: "Idea",
    ai_worked_out: "AI worked out",
    human_worked_out: "Human worked out",
    informal_writing: "Informal writing",
    formal_writing: "Formal writing",
  };
  const LEGACY_TIER_LABELS = {
    0: "Idea",
    1: "AI worked out",
    2: "Human worked out",
    3: "Informal writing",
    4: "Formal writing",
  };

  function findHierarchyPath(rootNode, targetId) {
    if (!rootNode || !targetId) return null;
    const path = [];
    const visited = new Set();
    function visit(node) {
      if (!node || visited.has(node.id)) return false;
      visited.add(node.id);
      path.push(node);
      if (node.id === targetId) return true;
      for (const child of node.children || []) {
        if (visit(child)) return true;
      }
      path.pop();
      return false;
    }
    return visit(rootNode) ? path.slice() : null;
  }

  function parentPath(nodes, targetId) {
    const byId = new Map((nodes || []).map((node) => [node.id, node]));
    const path = [];
    const seen = new Set();
    let current = byId.get(targetId);
    while (current) {
      if (seen.has(current.id)) return [];
      seen.add(current.id);
      path.push(current);
      if (!current.parent) break;
      current = byId.get(current.parent);
      if (!current) return [];
    }
    return path.reverse();
  }

  function focusNodeIds(nodes, targetId) {
    const path = parentPath(nodes, targetId);
    if (!path.length) return [];
    const ids = new Set(path.map((node) => node.id));
    (nodes || []).forEach((node) => {
      if (node.parent === targetId) ids.add(node.id);
    });
    return [...ids];
  }

  function siblingNavigation(nodes, targetId) {
    const selected = (nodes || []).find((node) => node.id === targetId);
    if (!selected || !selected.parent) {
      return { parentId: null, previousId: null, nextId: null, index: -1, count: 0 };
    }
    const siblings = nodes.filter((node) => node.parent === selected.parent);
    const index = siblings.findIndex((node) => node.id === targetId);
    return {
      parentId: selected.parent,
      previousId: index > 0 ? siblings[index - 1].id : null,
      nextId: index >= 0 && index < siblings.length - 1 ? siblings[index + 1].id : null,
      index,
      count: siblings.length,
    };
  }

  function layoutRadialTree(rootNode, collapsedNodeIds = new Set(), options = {}) {
    if (!rootNode) return;

    const collapsed = collapsedNodeIds instanceof Set
      ? collapsedNodeIds
      : new Set(collapsedNodeIds || []);
    const gap = Number.isFinite(options.gap) ? Math.max(0, options.gap) : 24;
    const nodeWidth = Number.isFinite(options.nodeWidth) && options.nodeWidth > 0 ? options.nodeWidth : 180;
    const nodeHeight = Number.isFinite(options.nodeHeight) && options.nodeHeight > 0 ? options.nodeHeight : 138;
    const rootWidth = Number.isFinite(options.rootWidth) && options.rootWidth > 0 ? options.rootWidth : 220;
    const rootHeight = Number.isFinite(options.rootHeight) && options.rootHeight > 0 ? options.rootHeight : 160;
    const width = (node) => Number.isFinite(node.w) && node.w > 0 ? node.w : (node === rootNode ? rootWidth : nodeWidth);
    const height = (node) => Number.isFinite(node.h) && node.h > 0 ? node.h : (node === rootNode ? rootHeight : nodeHeight);
    const visibleChildren = (node) => collapsed.has(node.id) ? [] : (node.children || []);
    let nextLeafSlot = 0;

    // Each visible leaf gets one angular slot. A parent spans its descendant
    // slots, so branch angles follow whatever hierarchy the current map has.
    function assignLeafSlots(node, depth = 0) {
      node.depth = depth;
      const children = visibleChildren(node);
      if (children.length === 0) {
        node.weight = 1;
        node.layoutStart = nextLeafSlot;
        nextLeafSlot += 1;
        return node.weight;
      }
      node.layoutStart = nextLeafSlot;
      node.weight = children.reduce((sum, child) => sum + assignLeafSlots(child, depth + 1), 0);
      return node.weight;
    }

    assignLeafSlots(rootNode);
    const leafCount = Math.max(rootNode.weight, 1);
    function assignAngles(node) {
      if (node.depth > 0) {
        node.angle = -Math.PI / 2 + (2 * Math.PI * (node.layoutStart + node.weight / 2)) / leafCount;
      } else {
        node.angle = 0;
      }
      visibleChildren(node).forEach(assignAngles);
    }
    assignAngles(rootNode);

    rootNode.x = -width(rootNode) / 2;
    rootNode.y = -height(rootNode) / 2;
    const levels = [];
    function collectVisible(node) {
      if (!levels[node.depth]) levels[node.depth] = [];
      levels[node.depth].push(node);
      visibleChildren(node).forEach(collectVisible);
    }
    collectVisible(rootNode);

    function largestCard(nodes) {
      return nodes.reduce((largest, node) => ({
        width: Math.max(largest.width, width(node)),
        height: Math.max(largest.height, height(node)),
      }), { width: 0, height: 0 });
    }
    function centerClearance(first, second) {
      return Math.hypot((first.width + second.width) / 2 + gap, (first.height + second.height) / 2 + gap);
    }
    function requiredRingRadius(nodes, minimumCenterDistance) {
      if (nodes.length < 2) return 0;
      const turns = nodes
        .map((node) => ((node.angle % (2 * Math.PI)) + 2 * Math.PI) % (2 * Math.PI))
        .sort((a, b) => a - b);
      let minimumAngle = 2 * Math.PI;
      for (let index = 0; index < turns.length; index += 1) {
        const current = turns[index];
        const next = index + 1 < turns.length ? turns[index + 1] : turns[0] + 2 * Math.PI;
        minimumAngle = Math.min(minimumAngle, next - current);
      }
      return minimumCenterDistance / (2 * Math.sin(Math.max(minimumAngle, 0.001) / 2));
    }

    let priorRadius = 0;
    let priorSize = { width: width(rootNode), height: height(rootNode) };
    for (let depth = 1; depth < levels.length; depth += 1) {
      const nodes = levels[depth] || [];
      if (nodes.length === 0) continue;
      const size = largestCard(nodes);
      const sameLevelClearance = centerClearance(size, size);
      const radialFloor = priorRadius + centerClearance(priorSize, size);
      const ringRadius = requiredRingRadius(nodes, sameLevelClearance);
      const radius = Math.max(radialFloor, ringRadius);
      nodes.forEach((node) => {
        node.x = radius * Math.cos(node.angle) - width(node) / 2;
        node.y = radius * Math.sin(node.angle) - height(node) / 2;
      });
      priorRadius = radius;
      priorSize = size;
    }
  }

  function stagePresentation(node) {
    const explicit = node && (node.progress_stage || node.maturity);
    if (Object.prototype.hasOwnProperty.call(STAGE_LABELS, explicit)) {
      return { label: STAGE_LABELS[explicit], stage: explicit, legacy: false, note: "Recorded stage." };
    }
    if (node && Number.isInteger(node.tier) && Object.prototype.hasOwnProperty.call(LEGACY_TIER_LABELS, node.tier)) {
      return {
        label: `Legacy tier ${node.tier} · read-only`,
        stage: null,
        mappedLabel: LEGACY_TIER_LABELS[node.tier],
        legacy: true,
        note: "Historical tier shown for reference only. It does not establish owner understanding or citation verification.",
      };
    }
    return {
      label: "Stage not recorded",
      stage: null,
      legacy: false,
      note: "No progress stage is recorded for this node.",
    };
  }

  function sourceId(source) {
    return typeof source === "string" ? source : (source && source.id) || null;
  }

  function firstText(record, keys) {
    for (const key of keys) {
      const value = record && record[key];
      if (typeof value === "string" && value.trim()) return value;
      if (Array.isArray(value) && value.length) return value.map((item) => String(item)).join("; ");
    }
    return null;
  }

  function resolveClaimProvenance(node, referenceMap) {
    const referenceNodes = (referenceMap && referenceMap.nodes) || [];
    const referenceSources = (referenceMap && referenceMap.sources) || [];
    const referenceNodeById = new Map(referenceNodes.map((item) => [item.id, item]));
    const referenceSourceById = new Map(referenceSources.map((item) => [sourceId(item), item]));
    const ownerSources = node && Array.isArray(node.sources) ? node.sources : [];
    const ownerSourceById = new Map(ownerSources.map((item) => [sourceId(item), item]));
    const claims = node && Array.isArray(node.claims) ? node.claims : [];

    return claims.map((claim) => {
      const links = Array.isArray(claim.ai_reference_links) ? claim.ai_reference_links : [];
      const linkSourceIds = links.map((link) => link.source_id).filter(Boolean);
      const sourceIds = [...new Set([...(claim.source_ids || []), ...linkSourceIds])];
      if (!sourceIds.length && !links.some((link) => link.reference_node_id || link.reference_claim_id)) {
        return {
          claim,
          entries: [],
          absentCitation: true,
          claimVerification: claim.human_verified === true ? "human_verified" : (claim.human_verified === false ? "not_human_verified" : "not_recorded"),
        };
      }

      const effectiveLinks = links.length ? links : sourceIds.map((id) => ({ source_id: id }));
      const entries = effectiveLinks.map((link) => {
        const id = link.source_id || sourceIds[0] || null;
        const ownerSource = (id && ownerSourceById.get(id)) || null;
        const referenceSource = (id && referenceSourceById.get(id)) || null;
        const refNode = link.reference_node_id ? referenceNodeById.get(link.reference_node_id) || null : null;
        const referenceClaims = refNode
          ? [...(refNode.claims || []), ...(refNode.claim_refs || [])]
          : [];
        const refClaim = referenceClaims.find((item) =>
          (link.reference_claim_id && (item.id === link.reference_claim_id || item.claim_id === link.reference_claim_id))
          || (id && item.source_id === id)
        ) || null;
        const source = referenceSource || ownerSource;
        let linkVerification = "not_recorded";
        if (link.human_verified === true) linkVerification = "human_verified";
        else if (link.human_verified === false) linkVerification = "not_human_verified";
        return {
          sourceId: id,
          ownerSource,
          referenceSource,
          source,
          referenceNodeId: link.reference_node_id || null,
          referenceNode: refNode,
          referenceClaimId: link.reference_claim_id || null,
          referenceClaim: refClaim,
          relation: link.relation_to_claim || null,
          interpretationNote: link.ai_interpretation_note || null,
          ownerReview: link.owner_review || null,
          sourceRecordStatus: link.source_record_status || null,
          locator: firstText(source, ["locator", "section", "page", "passage_locator"])
            || firstText(ownerSource, ["locator", "section", "page", "passage_locator"]),
          ownerLocator: firstText(ownerSource, ["locator", "section", "page", "passage_locator"]),
          referenceLocator: firstText(refClaim, ["locator", "section", "page", "passage_locator"])
            || firstText(referenceSource, ["locator", "section", "page", "passage_locator"]),
          referenceSupport: firstText(refClaim, ["supports", "support", "statement"]),
          excerpt: firstText(source, ["quote", "quotation", "excerpt", "passage", "quotation_excerpt"]),
          sourceAccess: firstText(source, ["source_access", "access", "access_status"]),
          referenceVerification: firstText(referenceSource, ["verification", "review"]),
          linkVerification,
          resolvedSource: Boolean(source),
          resolvedReferenceNode: !link.reference_node_id || Boolean(refNode),
        };
      });
      return {
        claim,
        entries,
        absentCitation: false,
        claimVerification: claim.human_verified === true ? "human_verified" : (claim.human_verified === false ? "not_human_verified" : "not_recorded"),
      };
    });
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function safeMarkdownHref(value) {
    const href = String(value || "").trim();
    if (href.startsWith("#")) return href;
    try {
      const parsed = new URL(href);
      return ["http:", "https:", "mailto:"].includes(parsed.protocol) ? href : null;
    } catch (_error) {
      return null;
    }
  }

  function renderInlineMarkdown(value, options = {}) {
    const source = String(value ?? "");
    const tokenPattern = /!\[([^\]]*)\]\(([^)\s]+)(?:\s+["']([^"']*)["'])?\)|\[([^\]]+)\]\(([^)\s]+)\)|`([^`]+)`|\*\*([\s\S]+?)\*\*|\*([^*\n]+)\*/g;
    let output = "";
    let cursor = 0;
    let match;
    while ((match = tokenPattern.exec(source)) !== null) {
      output += escapeHtml(source.slice(cursor, match.index)).replace(/\n/g, "<br>");
      if (match[1] !== undefined) {
        const alt = match[1];
        const imagePath = match[2];
        if (options.allowFigures === false || /^(?:[a-z][a-z0-9+.-]*:|\/\/|\/)/i.test(imagePath)) {
          output += escapeHtml(match[0]);
        } else {
          output += `<button type="button" class="reader-figure-button" data-reader-image-path="${escapeHtml(imagePath)}" data-reader-image-alt="${escapeHtml(alt)}">Show figure: ${escapeHtml(alt || "Open figure")}</button>`;
        }
      } else if (match[4] !== undefined) {
        const href = safeMarkdownHref(match[5]);
        output += href
          ? `<a href="${escapeHtml(href)}" target="_blank" rel="noopener">${escapeHtml(match[4])}</a>`
          : escapeHtml(match[4]);
      } else if (match[6] !== undefined) {
        output += `<code>${escapeHtml(match[6])}</code>`;
      } else if (match[7] !== undefined) {
        output += `<strong>${escapeHtml(match[7])}</strong>`;
      } else {
        output += `<em>${escapeHtml(match[8])}</em>`;
      }
      cursor = tokenPattern.lastIndex;
    }
    output += escapeHtml(source.slice(cursor)).replace(/\n/g, "<br>");
    return output;
  }

  function renderMarkdownSafe(markdown, options = {}) {
    const lines = String(markdown ?? "").replace(/\r\n?/g, "\n").split("\n");
    const blocks = [];
    let paragraph = [];
    let listType = null;
    let listItems = [];
    let quoteLines = [];
    let codeLines = null;

    const flushParagraph = () => {
      if (paragraph.length) {
        blocks.push(`<p>${renderInlineMarkdown(paragraph.join("\n"), options)}</p>`);
        paragraph = [];
      }
    };
    const flushList = () => {
      if (listType && listItems.length) {
        blocks.push(`<${listType}>${listItems.map((item) => `<li>${renderInlineMarkdown(item, options)}</li>`).join("")}</${listType}>`);
      }
      listType = null;
      listItems = [];
    };
    const flushQuote = () => {
      if (quoteLines.length) {
        blocks.push(`<blockquote>${quoteLines.map((line) => `<p>${renderInlineMarkdown(line, options)}</p>`).join("")}</blockquote>`);
      }
      quoteLines = [];
    };

    for (const line of lines) {
      const trimmed = line.trim();
      if (codeLines !== null) {
        if (/^```/.test(trimmed)) {
          blocks.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
          codeLines = null;
        } else {
          codeLines.push(line);
        }
        continue;
      }
      if (/^```/.test(trimmed)) {
        flushParagraph();
        flushList();
        flushQuote();
        codeLines = [];
        continue;
      }
      if (!trimmed) {
        flushParagraph();
        flushList();
        flushQuote();
        continue;
      }
      const heading = trimmed.match(/^(#{1,6})\s+(.+)$/);
      if (heading) {
        flushParagraph();
        flushList();
        flushQuote();
        const level = Math.min(5, heading[1].length + 1);
        blocks.push(`<h${level}>${renderInlineMarkdown(heading[2], options)}</h${level}>`);
        continue;
      }
      if (/^(?:---+|\*\*\*+|___+)$/.test(trimmed)) {
        flushParagraph();
        flushList();
        flushQuote();
        blocks.push("<hr>");
        continue;
      }
      const quote = trimmed.match(/^>\s?(.*)$/);
      if (quote) {
        flushParagraph();
        flushList();
        quoteLines.push(quote[1]);
        continue;
      }
      const listItem = trimmed.match(/^([-+*]|\d+[.)])\s+(.+)$/);
      if (listItem) {
        flushParagraph();
        flushQuote();
        const nextType = /^\d/.test(listItem[1]) ? "ol" : "ul";
        if (listType && listType !== nextType) flushList();
        listType = nextType;
        listItems.push(listItem[2]);
        continue;
      }
      flushList();
      flushQuote();
      paragraph.push(line);
    }
    flushParagraph();
    flushList();
    flushQuote();
    if (codeLines !== null) blocks.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
    return blocks.join("");
  }

  const api = {
    STAGE_LABELS,
    LEGACY_TIER_LABELS,
    layoutRadialTree,
    findHierarchyPath,
    parentPath,
    focusNodeIds,
    siblingNavigation,
    stagePresentation,
    resolveClaimProvenance,
    renderMarkdownSafe,
  };
  root.BepMindMapGraph = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
})(typeof window !== "undefined" ? window : globalThis);
