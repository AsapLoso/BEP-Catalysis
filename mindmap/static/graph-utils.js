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

  // Traverse by level so every sibling at a depth is shown before the tour
  // moves to deeper questions. Previous/Next remain direct, read-only navigation.
  function tourSequence(rootNode) {
    if (!rootNode) return [];
    const sequence = [];
    const visited = new Set();
    const queue = [{ node: rootNode, ancestors: [], siblingPosition: 1, siblingCount: 1 }];

    for (let cursor = 0; cursor < queue.length; cursor += 1) {
      const item = queue[cursor];
      const node = item.node;
      if (!node || visited.has(node.id)) continue;
      visited.add(node.id);
      const path = [...item.ancestors, node.title || node.id];
      sequence.push({
        id: node.id,
        category: item.ancestors[item.ancestors.length - 1] || "Root",
        path,
        level: item.ancestors.length,
        levelPosition: item.siblingPosition,
        levelCount: item.siblingCount,
      });
      const children = node.children || [];
      children.forEach((child, index) => queue.push({
        node: child,
        ancestors: path,
        siblingPosition: index + 1,
        siblingCount: children.length,
      }));
    }
    return sequence;
  }

  // Focus keeps every immediate child of the selected node, plus the selected
  // ancestry and direct siblings at each ancestor level (without their children).
  function focusHierarchy(rootNode, targetId) {
    if (!rootNode || !targetId) return rootNode;
    const path = findHierarchyPath(rootNode, targetId);
    if (!path) return rootNode;

    function copyPath(node, index) {
      const selectedChild = path[index + 1];
      return {
        ...node,
        children: (node.children || []).map((child) => (
          selectedChild && child.id === selectedChild.id
            ? copyPath(child, index + 1)
            : { ...child, children: [] }
        )),
      };
    }

    return copyPath(path[0], 0);
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

  // Add layout-only leaves to lighter top-level subtrees. ELK Radial's
  // LEAF_NUMBER criterion then gives each root child the same angular budget,
  // while the real tree and its node count remain untouched.
  function radialSectorPadding(nodes, links) {
    const nodeList = Array.isArray(nodes) ? nodes : [];
    const edgeList = Array.isArray(links) ? links : [];
    const childrenById = new Map();
    const usedIds = new Set(nodeList.map((node) => String(node.id)));
    const nodeById = new Map(nodeList.map((node) => [String(node.id), node]));
    const idOf = (value) => String(value && typeof value === "object" ? value.id : value);

    edgeList.forEach((edge) => {
      const sourceId = idOf(edge.source);
      const targetId = idOf(edge.target);
      if (!nodeById.has(sourceId) || !nodeById.has(targetId)) return;
      childrenById.set(sourceId, [...(childrenById.get(sourceId) || []), targetId]);
    });

    const root = nodeList.find((node) => node.parent === null || node.parent === undefined);
    if (!root) return { nodes: [], edges: [], sectors: [], targetLeafCount: 0 };
    const rootId = String(root.id);
    const rootChildren = childrenById.get(rootId) || [];

    function leavesInSubtree(id, ancestors = new Set()) {
      if (ancestors.has(id)) return [];
      const nextAncestors = new Set(ancestors);
      nextAncestors.add(id);
      const children = childrenById.get(id) || [];
      if (!children.length) return [id];
      const leaves = children.flatMap((childId) => leavesInSubtree(childId, nextAncestors));
      return leaves.length ? leaves : [id];
    }

    const sectors = rootChildren.map((id) => {
      const leaves = leavesInSubtree(id);
      return { id: nodeById.get(id)?.id ?? id, leafCount: leaves.length, targetLeafCount: 0, leaves };
    });
    const targetLeafCount = sectors.reduce((largest, sector) => Math.max(largest, sector.leafCount), 0);
    sectors.forEach((sector) => { sector.targetLeafCount = targetLeafCount; });

    let serial = 0;
    const paddingNodes = [];
    const paddingEdges = [];
    function uniqueId(prefix) {
      let candidate;
      do {
        candidate = prefix + serial++;
      } while (usedIds.has(candidate));
      usedIds.add(candidate);
      return candidate;
    }

    sectors.forEach((sector) => {
      const missing = targetLeafCount - sector.leafCount;
      if (missing <= 0) return;
      const attachmentId = String(sector.leaves[0] ?? sector.id);
      // Replacing one visible leaf with missing+1 layout leaves increases its
      // sector's leaf count by exactly the number needed.
      for (let index = 0; index < missing + 1; index += 1) {
        const paddingId = uniqueId("__bep_layout_padding_node_");
        const edgeId = uniqueId("__bep_layout_padding_edge_");
        paddingNodes.push({ id: paddingId, width: 1, height: 1, layoutOnly: true });
        paddingEdges.push({ id: edgeId, source: attachmentId, target: paddingId });
      }
    });

    return { nodes: paddingNodes, edges: paddingEdges, sectors, targetLeafCount };
  }

  // Choose the least obstructed tour-card position inside a surface.
  function chooseOverlayPosition(surface, panel, obstacles, margin = 12) {
    const surfaceWidth = Math.max(0, Number(surface && surface.width) || 0);
    const surfaceHeight = Math.max(0, Number(surface && surface.height) || 0);
    const safeMargin = Math.max(0, Number(margin) || 0);
    const width = Math.min(Math.max(0, Number(panel && panel.width) || 0), Math.max(0, surfaceWidth - safeMargin * 2));
    const height = Math.min(Math.max(0, Number(panel && panel.height) || 0), Math.max(0, surfaceHeight - safeMargin * 2));
    const maxLeft = Math.max(safeMargin, surfaceWidth - width - safeMargin);
    const maxTop = Math.max(safeMargin, surfaceHeight - height - safeMargin);
    const clamp = (value, max) => Math.max(safeMargin, Math.min(Number(value) || safeMargin, max));
    const candidates = new Map();
    const addCandidate = (left, top) => {
      const point = { left: clamp(left, maxLeft), top: clamp(top, maxTop) };
      candidates.set(point.left.toFixed(2) + ":" + point.top.toFixed(2), point);
    };

    [safeMargin, maxLeft, (surfaceWidth - width) / 2].forEach((left) => {
      [safeMargin, maxTop, (surfaceHeight - height) / 2].forEach((top) => addCandidate(left, top));
    });
    (Array.isArray(obstacles) ? obstacles : []).forEach((obstacle) => {
      const left = Number(obstacle.left) || 0;
      const top = Number(obstacle.top) || 0;
      const right = Number(obstacle.right) || 0;
      const bottom = Number(obstacle.bottom) || 0;
      const middleY = (top + bottom - height) / 2;
      const middleX = (left + right - width) / 2;
      addCandidate(left - width - safeMargin, middleY);
      addCandidate(right + safeMargin, middleY);
      addCandidate(middleX, top - height - safeMargin);
      addCandidate(middleX, bottom + safeMargin);
    });

    const items = Array.isArray(obstacles) ? obstacles : [];
    let best = { left: safeMargin, top: safeMargin, width, height, overlapArea: Infinity };
    candidates.forEach((candidate) => {
      let score = 0;
      items.forEach((obstacle) => {
        const overlapWidth = Math.max(0, Math.min(candidate.left + width, obstacle.right) - Math.max(candidate.left, obstacle.left));
        const overlapHeight = Math.max(0, Math.min(candidate.top + height, obstacle.bottom) - Math.max(candidate.top, obstacle.top));
        score += overlapWidth * overlapHeight * Math.max(1, Number(obstacle.weight) || 1);
      });
      if (score < best.overlapArea) best = { ...candidate, width, height, overlapArea: score };
    });
    return best;
  }

  function elkEdgePath(edge, offsetX = 0, offsetY = 0) {
    const sections = Array.isArray(edge && edge.sections) ? edge.sections : [];
    return sections.map((section) => {
      const points = [section.startPoint, ...(section.bendPoints || []), section.endPoint]
        .filter((point) => point && Number.isFinite(point.x) && Number.isFinite(point.y));
      if (points.length < 2) return "";
      return "M " + (points[0].x - offsetX).toFixed(1) + " " + (points[0].y - offsetY).toFixed(1)
        + points.slice(1).map((point) => (
          " L " + (point.x - offsetX).toFixed(1) + " " + (point.y - offsetY).toFixed(1)
        )).join("");
    }).filter(Boolean).join(" ");
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
      .replace(/\"/g, "&quot;")
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
        const rasterImage = /\.(?:png|jpe?g|gif|webp)(?:[?#].*)?$/i.test(imagePath);
        if (options.allowFigures !== true || !rasterImage || /^(?:[a-z][a-z0-9+.-]*:|\/\/|\/)/i.test(imagePath)) {
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
    findHierarchyPath,
    parentPath,
    focusNodeIds,
    focusHierarchy,
    tourSequence,
    siblingNavigation,
    radialSectorPadding,
    chooseOverlayPosition,
    elkEdgePath,
    stagePresentation,
    resolveClaimProvenance,
    renderMarkdownSafe,
  };
  root.BepMindMapGraph = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
})(typeof window !== "undefined" ? window : globalThis);
