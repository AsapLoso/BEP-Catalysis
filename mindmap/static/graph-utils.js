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

  // Breadth-first order visits every node at a level before any deeper node.
  function tourSequence(rootNode) {
    const sequence = [];
    const queue = [{ node: rootNode, ancestors: [] }];
    const visited = new Set();
    let cursor = 0;
    while (cursor < queue.length) {
      const { node, ancestors } = queue[cursor++];
      if (!node || visited.has(node.id)) continue;
      visited.add(node.id);
      const path = [...ancestors, node.title || node.id];
      if (node.parent) {
        sequence.push({
          id: node.id,
          category: ancestors[ancestors.length - 1] || "Root",
          path,
          level: ancestors.length,
        });
      }
      (node.children || []).forEach((child) => queue.push({ node: child, ancestors: path }));
    }
    const levelCounts = new Map();
    sequence.forEach((item) => levelCounts.set(item.level, (levelCounts.get(item.level) || 0) + 1));
    const levelPositions = new Map();
    sequence.forEach((item) => {
      const position = (levelPositions.get(item.level) || 0) + 1;
      levelPositions.set(item.level, position);
      item.levelPosition = position;
      item.levelCount = levelCounts.get(item.level);
    });
    return sequence;
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

  const api = {
    STAGE_LABELS,
    LEGACY_TIER_LABELS,
    findHierarchyPath,
    parentPath,
    focusNodeIds,
    tourSequence,
    siblingNavigation,
    stagePresentation,
    resolveClaimProvenance,
  };
  root.BepMindMapGraph = api;
  if (typeof module !== "undefined" && module.exports) module.exports = api;
})(typeof window !== "undefined" ? window : globalThis);
