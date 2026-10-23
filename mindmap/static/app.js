/**
 * BEP mind map viewer with evolving, connected scientific hierarchies.
 * The overview anchors the root in the center; focus mode reads left to right
 * from the root through the selected node, with sibling context at each level.
 */

(() => {
  "use strict";

  const STAGE_CONFIG = {
    idea: { bg: "#e2e8f0", color: "#1e293b" },
    ai_worked_out: { bg: "#fde047", color: "#78350f" },
    human_worked_out: { bg: "#7dd3fc", color: "#0369a1" },
    informal_writing: { bg: "#5eead4", color: "#115e59" },
    formal_writing: { bg: "#86efac", color: "#14532d" },
  };

  // Borderless Squircle Dimensions
  const NODE_WIDTH = 190;
  const NODE_HEIGHT = 148;
  const ROOT_WIDTH = 320;
  const ROOT_HEIGHT = 210;

  // Radial distances per level
  const R_LEVEL_1 = 380; // Distance to primary arms
  const R_LEVEL_2 = 360; // Level 1 -> Level 2
  const R_LEVEL_3 = 340; // Level 2 -> Level 3
  const R_LEVEL_DEEP = 320; // Reused at arbitrary depths
  const SCIENTIFIC_ARM_IDS = new Set(["physics", "mathematics", "systems_control"]);
  const NON_SCIENTIFIC_ROOT_KINDS = new Set(["admin", "administrative", "project", "task", "milestone", "dossier", "letter", "source_dossier"]);

  // State
  let rawNodes = [];
  let rootHierarchy = null;
  let visibleHierarchy = null;
  let selectedNodeId = null;
  let focusMode = false;
  const collapsedNodes = new Set();
  const initializedModes = new Set();
  const selectionByMode = new Map();
  const collapsedByMode = new Map();
  let activeMode = null;
  let graphSource = null;
  let referenceMap = {};
  let readerRequestId = 0;
  let currentOwnerReferenceIds = [];

  // Pan / Zoom
  let transform = { x: 0, y: 0, scale: 0.68 };
  let isPanning = false;
  let startPan = { x: 0, y: 0 };

  // DOM Elements
  const svg = document.getElementById("mindmap-svg");
  const viewport = document.getElementById("viewport-group");
  const linksGroup = document.getElementById("links-group");
  const nodesGroup = document.getElementById("nodes-group");
  const layerSelect = document.getElementById("graph-mode");
  const btnFit = document.getElementById("btn-fit");
  const btnFocus = document.getElementById("btn-focus-toggle");
  const btnExpandAll = document.getElementById("btn-expand-all");
  const btnCollapseAll = document.getElementById("btn-collapse-all");
  const btnTour = document.getElementById("btn-tour");
  const btnRefresh = document.getElementById("btn-refresh");
  const graphSearch = document.getElementById("graph-search");
  const searchResults = document.getElementById("search-results");
  const sourceStatus = document.getElementById("map-source-status");
  const appHeader = document.querySelector(".app-header");
  const btnZoomIn = document.getElementById("btn-zoom-in");
  const btnZoomOut = document.getElementById("btn-zoom-out");
  const drawer = document.getElementById("details-drawer");
  const drawerCloseBtn = document.getElementById("drawer-close-btn");
  const referencePanel = document.getElementById("reference-panel");

  // Word-wrap utility for squircle cards
  function wrapText(text, maxChars = 21) {
    if (!text) return [""];
    const words = text.split(" ");
    const lines = [];
    let currentLine = "";

    words.forEach((word) => {
      if ((currentLine + " " + word).trim().length <= maxChars) {
        currentLine = (currentLine + " " + word).trim();
      } else {
        if (currentLine) lines.push(currentLine);
        currentLine = word;
      }
    });
    if (currentLine) lines.push(currentLine);
    return lines;
  }

  // 1. Data Fetching
  function initializeCollapsedNodes(nodes) {
    const children = new Map();
    nodes.forEach((node) => {
      if (node.parent) children.set(node.parent, (children.get(node.parent) || 0) + 1);
    });
    const byId = new Map(nodes.map((node) => [node.id, node]));
    nodes.forEach((node) => {
      let depth = 0;
      let current = node;
      const seen = new Set();
      while (current && current.parent && !seen.has(current.id)) {
        seen.add(current.id);
        current = byId.get(current.parent);
        if (current) depth += 1;
      }
      if (depth >= 2 && children.has(node.id)) collapsedNodes.add(node.id);
    });
  }

  function updateSourceStatus(message = "") {
    const mapMode = activeMode || "unknown";
    sourceStatus.dataset.mapMode = mapMode;
    appHeader.dataset.mapMode = mapMode;
    if (message) {
      sourceStatus.textContent = message;
      return;
    }
    if (!graphSource) {
      sourceStatus.textContent = "No map snapshot loaded.";
      return;
    }
    const snapshot = graphSource.status === "snapshot" || graphSource.status === "local_checkout_snapshot";
    const count = activeMode === "draft"
      ? `${rawNodes.filter((node) => node.is_draft).length} draft nodes + ${rawNodes.filter((node) => node.context_only).length} canonical context nodes`
      : rawNodes.length + " nodes";
    const parts = activeMode === "owner"
      ? ["Your personal map", count, graphSource.label || "local snapshot", "read-only", "not live from GitHub"]
      : [graphSource.label || "AI reference map", count];
    if (activeMode !== "owner" && snapshot) parts.push("local snapshot");
    sourceStatus.textContent = parts.join(" · ");
  }

  async function configureModes() {
    try {
      const response = await fetch("/api/config");
      const config = await response.json();
      const ownerOption = Array.from(layerSelect.options).find((option) => option.value === "owner");
      const available = config.available_modes || [];
      if (ownerOption) {
        ownerOption.disabled = !available.includes("owner");
        ownerOption.hidden = !available.includes("owner");
        if (available.includes("owner")) ownerOption.textContent = "Personal map snapshot · read-only";
      }
    } catch (error) {
      console.warn("Could not load map-view configuration:", error);
    }
  }

  async function fetchGraph(mode = null) {
    const selectedMode = mode || layerSelect.value;
    const modeChanged = selectedMode !== activeMode;
    const priorSelection = selectedNodeId;
    if (modeChanged) {
      if (activeMode) {
        if (selectedNodeId) selectionByMode.set(activeMode, selectedNodeId);
        collapsedByMode.set(activeMode, new Set(collapsedNodes));
      }
      selectedNodeId = selectionByMode.get(selectedMode) || null;
      collapsedNodes.clear();
      const savedCollapse = collapsedByMode.get(selectedMode);
      if (savedCollapse) savedCollapse.forEach((id) => collapsedNodes.add(id));
    }
    try {
      const resp = await fetch(`/api/graph?mode=${encodeURIComponent(selectedMode)}`);
      const data = await resp.json();
      if (!resp.ok) throw new Error(data.error || `HTTP ${resp.status}`);
      rawNodes = data.nodes || [];
      if (selectedMode === "draft") {
        const contextResponse = await fetch("/api/graph?mode=canonical");
        const contextData = await contextResponse.json();
        if (!contextResponse.ok) throw new Error(contextData.error || `HTTP ${contextResponse.status}`);
        const draftIds = new Set(rawNodes.map((node) => node.id));
        const contextNodes = (contextData.nodes || [])
          .filter((node) => !draftIds.has(node.id))
          .map((node) => ({ ...node, context_only: true }));
        rawNodes = [...contextNodes, ...rawNodes];
      }
      shouldFitAfterLayout = true;
      graphSource = data.source || null;
      referenceMap = data.reference_map || {};
      activeMode = selectedMode;
      referencePanel.classList.add("hidden");
      renderSearchResults();
      if (!initializedModes.has(selectedMode) && !collapsedByMode.has(selectedMode)) initializeCollapsedNodes(rawNodes);
      initializedModes.add(selectedMode);
      const missingSelection = selectedNodeId && !rawNodes.some((node) => node.id === selectedNodeId) ? selectedNodeId : null;
      renderTree();
      if (selectedNodeId) {
        const sel = rawNodes.find((n) => n.id === selectedNodeId);
        if (sel) showDrawer(sel);
        else drawer.classList.add("hidden");
      }
      updateSourceStatus(missingSelection
        ? `Selected node “${priorSelection}” is absent from this snapshot. Its selection is retained for when it returns.`
        : "");
    } catch (err) {
      console.error("Failed to load mind map graph:", err);
      updateSourceStatus(`Could not load this map snapshot: ${err.message}`);
    }
  }

  // 2. Hierarchy Builder
  function buildHierarchy(nodes) {
    if (!nodes || nodes.length === 0) return null;

    const nodeMap = new Map();
    nodes.forEach((n) => {
      const isRoot = !n.parent;
      const w = isRoot ? ROOT_WIDTH : NODE_WIDTH;
      const h = isRoot ? ROOT_HEIGHT : NODE_HEIGHT;
      const lines = wrapText(n.title, isRoot ? 24 : 20);

      nodeMap.set(n.id, {
        ...n,
        w: w,
        h: h,
        lines: lines,
        children: [],
        weight: 1,
        depth: 0,
        x: 0,
        y: 0,
        angle: 0,
      });
    });

    let root = null;
    nodes.forEach((n) => {
      const item = nodeMap.get(n.id);
      if (!n.parent) {
        root = item;
      } else {
        const parent = nodeMap.get(n.parent);
        if (parent) {
          parent.children.push(item);
        } else if (!root) {
          root = item;
        }
      }
    });

    // Compute tree depth and weights
    function computeWeights(node, depth = 0) {
      node.depth = depth;
      const isCollapsed = collapsedNodes.has(node.id);
      const visibleChildren = isCollapsed ? [] : (node.children || []);
      if (visibleChildren.length === 0) {
        node.weight = 1;
      } else {
        node.weight = visibleChildren.reduce((sum, c) => sum + computeWeights(c, depth + 1), 0);
      }
      return node.weight;
    }

    if (root) computeWeights(root, 0);
    return root;
  }

  function findNodePath(node, targetId, path = []) {
    if (!node) return null;
    const nextPath = [...path, node];
    if (node.id === targetId) return nextPath;
    for (const child of node.children || []) {
      const found = findNodePath(child, targetId, nextPath);
      if (found) return found;
    }
    return null;
  }

  function buildFocusHierarchy(root, targetId) {
    if (!root || !targetId) return root;
    const path = findNodePath(root, targetId);
    if (!path) return root;
    path.forEach((node) => collapsedNodes.delete(node.id));
    return BepMindMapGraph.focusHierarchy(root, targetId);
  }

  function buildScientificHierarchy(root) {
    if (!root) return null;
    // Owner snapshots use their own evolving themes. Only the legacy AI
    // reference views use the historical three scientific arms.
    if (activeMode === "owner") {
      const children = root.children || [];
      const filtered = children.filter((child) => !NON_SCIENTIFIC_ROOT_KINDS.has(String(child.kind || "").toLowerCase()));
      const selectedPath = BepMindMapGraph.parentPath(rawNodes, selectedNodeId);
      const selectedRootChild = selectedPath.length > 1 ? selectedPath[1].id : null;
      if (selectedRootChild && children.some((child) => child.id === selectedRootChild) && !filtered.some((child) => child.id === selectedRootChild)) {
        filtered.push(children.find((child) => child.id === selectedRootChild));
      }
      return { ...root, children: filtered };
    }
    return {
      ...root,
      children: (root.children || []).filter((child) => SCIENTIFIC_ARM_IDS.has(child.id)),
    };
  }

  // Focus view lays the ancestry out from the anchored root toward the selected node.
  function layoutHorizontalTree(root) {
    if (!root) return;
    const HORIZONTAL_GAP = 118;
    const VERTICAL_GAP = 36;
    const spans = new Map();

    function childrenOf(node) {
      return collapsedNodes.has(node.id) ? [] : (node.children || []);
    }
    function measure(node) {
      const children = childrenOf(node);
      const childSpan = children.reduce((sum, child) => sum + measure(child), 0)
        + Math.max(0, children.length - 1) * VERTICAL_GAP;
      const span = Math.max(node.h, childSpan);
      spans.set(node.id, span);
      return span;
    }
    const rootSpan = measure(root);

    function position(node, left, top) {
      const span = spans.get(node.id) || node.h;
      const children = childrenOf(node);
      node.x = left;
      node.y = top + (span - node.h) / 2;
      node.angle = 0;
      if (!children.length) return;
      const childrenHeight = children.reduce((sum, child) => sum + spans.get(child.id), 0)
        + (children.length - 1) * VERTICAL_GAP;
      let childTop = top + (span - childrenHeight) / 2;
      children.forEach((child) => {
        position(child, left + node.w + HORIZONTAL_GAP, childTop);
        childTop += spans.get(child.id) + VERTICAL_GAP;
      });
    }
    position(root, 0, -rootSpan / 2);
  }

  // 3. The overview uses ELK Radial with the root anchored at the center.
  // Size-aware wedges and radial node spacing keep evolving cards separated.
  // Focus mode remains the existing left-to-right layout.
  const OVERVIEW_LAYOUT_OPTIONS = {
    "elk.algorithm": "radial",
    "elk.radial.centerOnRoot": "true",
    "elk.radial.wedgeCriteria": "NODE_SIZE",
    "elk.spacing.nodeNode": "48",
    "elk.spacing.edgeNode": "28",
  };
  let elkLayoutEngine = null;
  let renderGeneration = 0;
  let shouldFitAfterLayout = false;

  function overviewFallbackPath(source, target) {
    const sourceCenterX = source.x + source.w / 2;
    const sourceCenterY = source.y + source.h / 2;
    const targetCenterX = target.x + target.w / 2;
    const targetCenterY = target.y + target.h / 2;
    const dx = targetCenterX - sourceCenterX;
    const dy = targetCenterY - sourceCenterY;
    const distance = Math.hypot(dx, dy);
    if (!distance) return "";
    const ux = dx / distance;
    const uy = dy / distance;
    const extent = (node) => Math.min(
      Math.abs(ux) < 1e-9 ? Infinity : node.w / 2 / Math.abs(ux),
      Math.abs(uy) < 1e-9 ? Infinity : node.h / 2 / Math.abs(uy),
    );
    const sourceExtent = extent(source);
    const targetExtent = Math.max(0, extent(target) - 8);
    const startX = sourceCenterX + ux * sourceExtent;
    const startY = sourceCenterY + uy * sourceExtent;
    const endX = targetCenterX - ux * targetExtent;
    const endY = targetCenterY - uy * targetExtent;
    return "M " + startX.toFixed(1) + " " + startY.toFixed(1)
      + " L " + endX.toFixed(1) + " " + endY.toFixed(1);
  }

  async function layoutOverviewWithElk(visibleNodes, visibleLinks) {
    if (typeof ELK !== "function") {
      throw new Error("The locally bundled ELK layout engine did not load.");
    }
    if (!elkLayoutEngine) {
      elkLayoutEngine = new ELK({ workerUrl: "/vendor/elk-worker.min.js" });
    }

    const edgeTargetById = new Map();
    const graph = {
      id: "bep-map-overview",
      layoutOptions: OVERVIEW_LAYOUT_OPTIONS,
      children: visibleNodes.map((node) => ({
        id: node.id,
        width: node.w,
        height: node.h,
      })),
      edges: visibleLinks.map((link, index) => {
        const id = "bep-edge-" + index;
        edgeTargetById.set(id, link.target.id);
        return { id, sources: [link.source.id], targets: [link.target.id] };
      }),
    };

    const layout = await elkLayoutEngine.layout(graph);
    const offsetX = (layout.width || 0) / 2;
    const offsetY = (layout.height || 0) / 2;
    const positions = new Map((layout.children || []).map((node) => [node.id, node]));
    visibleNodes.forEach((node) => {
      const position = positions.get(node.id);
      if (!position || !Number.isFinite(position.x) || !Number.isFinite(position.y)) {
        throw new Error("ELK returned no position for node " + node.id);
      }
      node.x = position.x - offsetX;
      node.y = position.y - offsetY;
    });

    const routes = new Map();
    (layout.edges || []).forEach((edge) => {
      const path = (edge.sections || []).map((section) => {
        const points = [section.startPoint, ...(section.bendPoints || []), section.endPoint]
          .filter((point) => point && Number.isFinite(point.x) && Number.isFinite(point.y));
        if (points.length < 2) return "";
        return "M " + (points[0].x - offsetX).toFixed(1) + " " + (points[0].y - offsetY).toFixed(1)
          + points.slice(1).map((point) => (
            " L " + (point.x - offsetX).toFixed(1) + " " + (point.y - offsetY).toFixed(1)
          )).join("");
      }).filter(Boolean).join(" ");
      const targetId = edgeTargetById.get(edge.id);
      if (targetId && path) routes.set(targetId, path);
    });
    if (visibleLinks.length && routes.size !== visibleLinks.length) {
      throw new Error("ELK Radial did not return a clipped route for every visible edge.");
    }
    return routes;
  }
  // 5. Rendering
  async function renderTree() {
    const renderId = ++renderGeneration;
    rootHierarchy = buildHierarchy(rawNodes);
    if (!rootHierarchy) {
      linksGroup.innerHTML = "";
      nodesGroup.innerHTML = "";
      return;
    }

    const scientificHierarchy = buildScientificHierarchy(rootHierarchy);
    visibleHierarchy = focusMode
      ? buildFocusHierarchy(scientificHierarchy, selectedNodeId)
      : scientificHierarchy;
    const isFocusLayout = focusMode && Boolean(selectedNodeId);
    const visibleNodes = [];
    const visibleLinks = [];

    function collect(node) {
      visibleNodes.push(node);
      const isCollapsed = collapsedNodes.has(node.id);
      if (!isCollapsed && node.children) {
        node.children.forEach((child) => {
          visibleLinks.push({ source: node, target: child });
          collect(child);
        });
      }
    }
    collect(visibleHierarchy);

    let overviewRoutes = new Map();
    if (isFocusLayout) {
      layoutHorizontalTree(visibleHierarchy);
    } else {
      try {
        overviewRoutes = await layoutOverviewWithElk(visibleNodes, visibleLinks);
      } catch (error) {
        console.warn("ELK Radial overview layout failed; using the built-in radial fallback.", error);
        layoutTree(visibleHierarchy);
        overviewRoutes = new Map();
      }
    }
    if (renderId !== renderGeneration) return;

    const selectedPathIds = new Set(
      BepMindMapGraph.parentPath(rawNodes, selectedNodeId).map((node) => node.id),
    );

    // Use ELK-clipped radial routes for overview edges and curved routes in focus view.
    linksGroup.innerHTML = visibleLinks
      .map((link) => {
        const s = link.source;
        const t = link.target;

        const sCenterX = s.x + s.w / 2;
        const sCenterY = s.y + s.h / 2;
        const tCenterX = t.x + t.w / 2;
        const tCenterY = t.y + t.h / 2;
        const vx = tCenterX - sCenterX;
        const vy = tCenterY - sCenterY;
        const dist = Math.hypot(vx, vy);
        if (dist === 0) return "";

        const ux = vx / dist;
        const uy = vy / dist;
        const nx = -uy;
        const ny = ux;
        const sX = sCenterX + ux * (s.w / 2 - 8);
        const sY = sCenterY + uy * (s.h / 2 - 8);
        const tX = tCenterX - ux * (t.w / 2 + 10);
        const tY = tCenterY - uy * (t.h / 2 + 10);
        const mx = (sX + tX) / 2;
        const my = (sY + tY) / 2;
        const bendOffset = Math.min(32, dist * 0.12) * (t.angle % 2 === 0 ? 1 : -1);
        const cX = mx + nx * bendOffset;
        const cY = my + ny * bendOffset;

        const isDraftLink = t.is_draft;
        const selectedPath = selectedPathIds.has(s.id) && selectedPathIds.has(t.id);
        const cls = [
          "tree-link",
          isDraftLink ? "draft-link" : "",
          selectedPath ? "selected-path" : "",
        ].filter(Boolean).join(" ");
        const marker = isDraftLink
          ? 'marker-end="url(#arrow-head-draft)"'
          : 'marker-end="url(#arrow-head)"';
        const focusPath = "M " + sX.toFixed(1) + " " + sY.toFixed(1)
          + " Q " + cX.toFixed(1) + " " + cY.toFixed(1) + " " + tX.toFixed(1) + " " + tY.toFixed(1);
        const path = isFocusLayout
          ? focusPath
          : (overviewRoutes.get(t.id) || overviewFallbackPath(s, t));
        return '<path class="' + cls + '" d="' + path + '" ' + marker + ' />';
      })
      .join("");

    // Render Borderless Squircles (Concept Map Cards)
    nodesGroup.innerHTML = visibleNodes
      .map((node) => {
        const isRoot = !node.parent;
        const isSelected = node.id === selectedNodeId;
        const hasChildren = node.children && node.children.length > 0;
        const isCollapsed = collapsedNodes.has(node.id);
        const starsText = node.importance ? "★".repeat(node.importance) : "";

        const progress = BepMindMapGraph.stagePresentation(node);
        const boxClass = [
          "node-square",
          isRoot ? "root-square" : (progress.stage ? `stage-${progress.stage}` : "stage-unspecified"),
          node.depth === 1 ? "branch-anchor" : "",
          progress.legacy ? "legacy-tier" : "",
          node.is_draft ? "is-draft" : "",
          isSelected ? "selected" : "",
        ]
          .filter(Boolean)
          .join(" ");

        // Multi-line wrapped text
        const textLines = node.lines || [node.title];
        const lineCount = textLines.length;
        const startY = isRoot ? 68 : (node.h / 2 - (lineCount - 1) * 8);

        const titleElements = textLines
          .map(
            (line, idx) =>
              `<tspan x="${(node.w / 2).toFixed(1)}" dy="${idx === 0 ? 0 : 17}">${escapeHtml(line)}</tspan>`
          )
          .join("");

        // Floating Pill Toggle (+ / −)
        let toggleBtn = "";
        if (hasChildren && !isRoot) {
          const tX = node.w - 12;
          const tY = 12;
          const icon = isCollapsed ? "+" : "−";
          toggleBtn = `
            <g class="toggle-group" data-toggle="${escapeHtml(node.id)}" transform="translate(${tX}, ${tY})">
              <circle class="toggle-circle" r="11" />
              <text class="toggle-text">${icon}</text>
            </g>
          `;
        }

        // Subtitle / Badge at bottom
        const bottomY = node.h - 16;
        const stageConfig = STAGE_CONFIG[progress.stage] || { color: "#475569" };
        const badgeFill = isRoot ? "#1d4ed8" : (node.is_draft ? "#b45309" : stageConfig.color);
        const badgeLabel = isRoot
          ? (node.context_only ? "CANONICAL CONTEXT" : "MAP ROOT")
          : node.is_draft
          ? "⚡ AI Draft"
          : node.context_only
          ? "Context"
          : progress.label;

        const badgeElem = `<text x="16" y="${bottomY}" class="node-badge-text" fill="${badgeFill}">${escapeHtml(badgeLabel)}</text>`;
        const starsElem = starsText
          ? `<text x="${node.w - 16}" y="${bottomY}" class="node-stars" text-anchor="end">${starsText}</text>`
          : "";

        const filterAttr = isRoot ? 'filter="url(#root-shadow)"' : 'filter="url(#card-shadow)"';

        return `
          <g class="tree-node" data-id="${escapeHtml(node.id)}" transform="translate(${node.x.toFixed(1)}, ${node.y.toFixed(1)})">
            <rect class="${boxClass}" width="${node.w}" height="${node.h}" ${filterAttr} />
            <text class="node-title ${isRoot ? 'root-title' : ''}" x="${(node.w / 2).toFixed(1)}" y="${startY}" text-anchor="middle">${titleElements}</text>
            ${badgeElem}
            ${starsElem}
            ${toggleBtn}
          </g>
        `;
      })
      .join("");

    applyTransform();
    if (shouldFitAfterLayout) {
      shouldFitAfterLayout = false;
      fitView();
    }
  }

  function applyTransform() {
    viewport.setAttribute(
      "transform",
      `matrix(${transform.scale}, 0, 0, ${transform.scale}, ${transform.x}, ${transform.y})`
    );
  }

  // 6. Drawer & Selection
  function displayStatus(value) {
    if (value === true) return "Yes · recorded";
    if (value === false) return "No · recorded";
    if (value === null || value === undefined || value === "") return "Not recorded";
    return String(value);
  }

  function displayValue(value) {
    if (Array.isArray(value)) return value.map((item) => String(item)).join("; ");
    if (value && typeof value === "object") return JSON.stringify(value);
    return value === null || value === undefined ? "" : String(value);
  }

  function statusMarkup(label, value) {
    return `<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(displayStatus(value))}</dd>`;
  }

  function safeExternalUrl(value) {
    if (!value) return null;
    try {
      const url = new URL(value, window.location.href);
      return url.protocol === "http:" || url.protocol === "https:" ? url.href : null;
    } catch (_) {
      return null;
    }
  }

  function setList(containerId, values, renderItem, emptyText) {
    const container = document.getElementById(containerId);
    const items = Array.isArray(values) ? values : [];
    container.innerHTML = items.length
      ? items.map((item) => `<li>${renderItem(item)}</li>`).join("")
      : `<li class="empty-state">${escapeHtml(emptyText)}</li>`;
  }

  function renderBreadcrumb(node) {
    const path = BepMindMapGraph.parentPath(rawNodes, node.id);
    const breadcrumb = document.getElementById("drawer-breadcrumb");
    breadcrumb.innerHTML = path.map((part, index) =>
      `<button class="breadcrumb-item" data-node-nav="${escapeHtml(part.id)}" ${index === path.length - 1 ? 'aria-current="page"' : ""}>${escapeHtml(part.title)}</button>`
    ).join('<span aria-hidden="true">›</span>');
  }

  function renderSiblingNavigation(node) {
    const navigation = BepMindMapGraph.siblingNavigation(rawNodes, node.id);
    const parentButton = document.getElementById("drawer-parent-btn");
    const previousButton = document.getElementById("drawer-prev-sibling");
    const nextButton = document.getElementById("drawer-next-sibling");
    parentButton.disabled = !navigation.parentId;
    parentButton.dataset.nodeNav = navigation.parentId || "";
    previousButton.disabled = !navigation.previousId;
    previousButton.dataset.nodeNav = navigation.previousId || "";
    nextButton.disabled = !navigation.nextId;
    nextButton.dataset.nodeNav = navigation.nextId || "";
    document.getElementById("drawer-sibling-position").textContent = navigation.index < 0
      ? "Root node"
      : `Question ${navigation.index + 1} of ${navigation.count}`;
  }

  function renderClaims(node) {
    const container = document.getElementById("drawer-claims");
    const resolved = BepMindMapGraph.resolveClaimProvenance(node, referenceMap);
    if (!resolved.length) {
      container.innerHTML = '<p class="empty-state">No claim records are attached.</p>';
    } else {
      container.innerHTML = resolved.map((item) => {
        const claim = item.claim || {};
        const evidenceTag = claim.ai_attached === true || claim.status === "ai_attached"
          ? "AI evidence attached"
          : (claim.ai_attached === false
            ? "AI evidence not attached"
            : (claim.ai_reference_links?.length ? "AI source links attached" : "AI attachment not recorded"));
        const entries = item.entries.length ? item.entries.map((entry) => {
          const sourceTitle = entry.ownerSource?.title || entry.referenceSource?.title || (entry.sourceId || "Unresolved source");
          const ownerSourceLine = entry.ownerSource
            ? `<div class="source-trail">Owner-map source: ${escapeHtml(entry.ownerSource.title || entry.ownerSource.id || entry.sourceId)}</div>`
            : '<div class="source-trail">Owner-map source record unresolved.</div>';
          const referenceSourceLine = entry.referenceSource
            ? `<div class="source-trail">AI reference source: ${escapeHtml(entry.referenceSource.title || entry.referenceSource.id || entry.sourceId)}</div>`
            : "";
          const locator = entry.ownerLocator
            ? `<div class="source-trail"><strong>Owner locator:</strong> ${escapeHtml(entry.ownerLocator)}</div>`
            : "";
          const referenceLocator = entry.referenceLocator
            ? `<div class="source-trail"><strong>AI reference locator:</strong> ${escapeHtml(entry.referenceLocator)}</div>`
            : '<div class="source-trail">AI reference passage locator not available.</div>';
          const excerpt = entry.excerpt ? `<blockquote class="source-excerpt">${escapeHtml(entry.excerpt)}</blockquote>` : '<div class="source-trail">No quotation excerpt is recorded.</div>';
          const refNode = entry.referenceNode ? entry.referenceNode.title : entry.referenceNodeId;
          const refClaim = entry.referenceClaim ? (entry.referenceClaim.statement || entry.referenceClaim.id || entry.referenceClaim.supports) : entry.referenceClaimId;
          const refTrail = (refNode || refClaim)
            ? `<div class="source-trail">AI reference node: ${escapeHtml(refNode || "node unresolved")}${refClaim ? ` · mapped evidence: ${escapeHtml(Array.isArray(refClaim) ? refClaim.join("; ") : refClaim)}` : ""}</div>`
            : "";
          const interpretation = entry.interpretationNote ? `<div class="source-trail">AI interpretation: ${escapeHtml(entry.interpretationNote)}</div>` : "";
          const relation = entry.relation ? `<div class="source-trail">Relation: ${escapeHtml(entry.relation)}</div>` : "";
          const access = entry.sourceAccess ? `<div class="source-trail">Source access: ${escapeHtml(entry.sourceAccess)}</div>` : "";
          const aiSourceStatus = entry.referenceVerification ? `<div class="source-trail">AI reference source review: ${escapeHtml(entry.referenceVerification)}</div>` : "";
          const ownerReview = entry.ownerReview ? `<div class="source-trail">Owner review of this link: ${escapeHtml(entry.ownerReview)}</div>` : "";
          const recordStatus = entry.sourceRecordStatus ? `<div class="source-trail">Recorded source status: ${escapeHtml(entry.sourceRecordStatus)}</div>` : "";
          return `<div class="claim-source"><strong>${escapeHtml(sourceTitle)}</strong>${ownerSourceLine}${referenceSourceLine}${refTrail}${relation}${interpretation}${locator}${referenceLocator}${excerpt}${access}${aiSourceStatus}${ownerReview}${recordStatus}<div class="source-trail">Link verification: ${escapeHtml(entry.linkVerification.replaceAll("_", " "))}</div></div>`;
        }).join("") : '<div class="source-trail">No source link is recorded for this claim.</div>';
        const derivation = claim.ai_derivation_note ? `<div class="source-trail">AI derivation note: ${escapeHtml(claim.ai_derivation_note)}</div>` : "";
        const evidenceType = claim.evidence_type ? `<div class="source-trail">Evidence type: ${escapeHtml(claim.evidence_type)}</div>` : "";
        return `<article class="claim-card"><h4>${escapeHtml(claim.id || "Claim")}</h4><p>${escapeHtml(claim.statement || "Claim text not recorded.")}</p>${evidenceType}${derivation}<div class="claim-statuses"><span>${escapeHtml(evidenceTag)}</span><span>Claim verification: ${escapeHtml(item.claimVerification.replaceAll("_", " "))}</span></div>${entries}</article>`;
      }).join("");
    }
    document.getElementById("drawer-claims-section").classList.toggle("hidden", !resolved.length);
  }

  function fileReferencePath(reference) {
    if (typeof reference === "string") return reference;
    return reference && typeof reference === "object" ? (reference.path || reference.file || "") : "";
  }

  async function renderOwnerReader(node) {
    const section = document.getElementById("drawer-reader-section");
    const content = document.getElementById("reader-content");
    const status = document.getElementById("reader-file-status");
    const rawLink = document.getElementById("reader-raw-link");
    const reference = node.reader_file;
    const visibility = reference && typeof reference === "object" ? reference.visibility : null;
    const isVisibleReader = !visibility || ["node_detail", "reader", "visible"].includes(visibility);
    const path = fileReferencePath(reference);
    const requestId = ++readerRequestId;
    content.innerHTML = "";
    status.textContent = "";
    section.classList.toggle("hidden", activeMode !== "owner" || !path || !isVisibleReader);
    if (section.classList.contains("hidden")) return;

    const endpoint = `/api/reader?node_id=${encodeURIComponent(node.id)}`;
    rawLink.href = `${endpoint}&raw=1`;
    status.textContent = "Loading reader page…";
    try {
      const response = await fetch(endpoint);
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
      if (requestId !== readerRequestId || selectedNodeId !== node.id) return;
      const kind = data.kind ? `Reader type: ${String(data.kind).replaceAll("_", " ")}` : "Reader page";
      const review = data.human_review === "not_assessed"
        ? "Owner review not assessed"
        : (data.human_review ? "Review detail in technical audit" : "");
      status.textContent = [kind, review].filter(Boolean).join(" · ");
      status.title = [data.status ? `File status: ${data.status}` : "", data.human_review ? `Human review: ${data.human_review}` : ""].filter(Boolean).join("\n");
      content.innerHTML = BepMindMapGraph.renderMarkdownSafe(data.content, { allowFigures: true });
    } catch (error) {
      if (requestId !== readerRequestId || selectedNodeId !== node.id) return;
      status.textContent = `Reader page could not be loaded: ${error.message}`;
    }
  }

  function renderBackgroundFiles(node) {
    const section = document.getElementById("drawer-background-details");
    const list = document.getElementById("drawer-background-files");
    const content = document.getElementById("background-reader-content");
    const files = activeMode === "owner" && Array.isArray(node.background_files) ? node.background_files : [];
    document.getElementById("background-file-count").textContent = String(files.length);
    section.classList.toggle("hidden", !files.length);
    section.open = false;
    content.classList.add("hidden");
    content.innerHTML = "";
    list.innerHTML = files.length ? files.map((file, index) => {
      const descriptor = typeof file === "string" ? { path: file } : (file || {});
      const label = descriptor.path || descriptor.file || `Background file ${index + 1}`;
      const purpose = descriptor.purpose ? `<small>${escapeHtml(descriptor.purpose)}</small>` : "";
      const visibility = descriptor.visibility ? `<small>Visibility: ${escapeHtml(descriptor.visibility)}</small>` : "";
      return `<li><button class="background-file-button" data-background-index="${index}">${escapeHtml(label)}</button>${purpose}${visibility}</li>`;
    }).join("") : "";
  }

  function renderFileAudit(node) {
    const section = document.getElementById("drawer-file-audit-section");
    const list = document.getElementById("drawer-file-audit");
    const records = [];
    const append = (label, value) => {
      if (value === null || value === undefined || value === "") return;
      records.push(statusMarkup(label, displayValue(value)));
    };
    const reader = activeMode === "owner"
      ? (node.reader_file && typeof node.reader_file === "object" ? node.reader_file : (node.reader_file ? { path: node.reader_file } : null))
      : null;
    if (reader) {
      ["path", "kind", "visibility", "status", "purpose", "human_review"].forEach((field) => append(`Reader · ${field.replaceAll("_", " ")}`, reader[field]));
    }
    (activeMode === "owner" && Array.isArray(node.background_files) ? node.background_files : []).forEach((file, index) => {
      const descriptor = typeof file === "string" ? { path: file } : (file || {});
      ["path", "kind", "visibility", "purpose", "status", "human_review"].forEach((field) => append(`Background ${index + 1} · ${field.replaceAll("_", " ")}`, descriptor[field]));
    });
    list.innerHTML = records.join("");
    section.classList.toggle("hidden", !records.length);
  }

  async function loadBackgroundFile(nodeId, index, button) {
    const target = document.getElementById("background-reader-content");
    const requestId = ++readerRequestId;
    const selectedButton = button;
    selectedButton.disabled = true;
    target.classList.remove("hidden");
    target.textContent = "Loading background file…";
    try {
      const endpoint = `/api/reader?node_id=${encodeURIComponent(nodeId)}&background_index=${index}`;
      const response = await fetch(endpoint);
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
      if (requestId !== readerRequestId || selectedNodeId !== nodeId) return;
      target.innerHTML = `<h4>${escapeHtml(data.path || data.file_name || "Background file")}</h4>${BepMindMapGraph.renderMarkdownSafe(data.content, { allowFigures: true })}`;
    } catch (error) {
      if (requestId === readerRequestId && selectedNodeId === nodeId) {
        target.textContent = `Background file could not be loaded: ${error.message}`;
      }
    } finally {
      selectedButton.disabled = false;
    }
  }

  function showDrawer(node) {
    selectedNodeId = node.id;
    const drawerWasHidden = drawer.classList.contains("hidden");
    if (activeMode) selectionByMode.set(activeMode, node.id);
    const progress = BepMindMapGraph.stagePresentation(node);
    const tierBadge = document.getElementById("drawer-tier-badge");
    tierBadge.textContent = progress.label;
    const colors = STAGE_CONFIG[progress.stage] || { bg: "#e2e8f0", color: "#334155" };
    tierBadge.style.backgroundColor = colors.bg;
    tierBadge.style.color = colors.color;

    document.getElementById("drawer-title").textContent = node.title || "Untitled node";
    document.getElementById("drawer-id").textContent = `id: ${node.id}`;
    const starsTag = document.getElementById("drawer-stars");
    starsTag.textContent = Number.isInteger(node.importance) && node.importance > 0 ? "★".repeat(node.importance) : "";
    starsTag.classList.toggle("hidden", !starsTag.textContent);

    const draftTag = document.getElementById("drawer-draft-status");
    draftTag.classList.toggle("hidden", !node.is_draft);

    document.getElementById("promotion-disabled-note").classList.toggle("hidden", !node.is_draft);

    const question = node.question || node.research_question || "";
    const summary = node.summary || "Summary not recorded.";
    const questionElement = document.getElementById("drawer-question");
    questionElement.textContent = question;
    questionElement.classList.toggle("hidden", !question);
    document.getElementById("drawer-summary").textContent = summary;
    document.getElementById("drawer-rationale").textContent = node.rationale || "No rationale specified.";
    document.getElementById("drawer-notes").textContent = node.notes || "No technical notes recorded.";
    const progressNote = progress.legacy ? progress.note : (progress.stage ? "Stage is recorded independently from review and citation verification." : progress.note);
    document.getElementById("drawer-progress").textContent = `${progress.label}. ${progressNote}`;

    const review = document.getElementById("drawer-review-status");
    review.innerHTML = [
      statusMarkup("Structural approval", node.structural_approval ?? node.structure_status),
      statusMarkup("Owner reading", node.owner_read_status),
      statusMarkup("Owner content approval", node.owner_content_approval),
      ...(node.human_understanding_review !== undefined ? [statusMarkup("Human understanding review", node.human_understanding_review)] : []),
      ...(node.owner_approval_status !== undefined ? [statusMarkup("Owner approval status", node.owner_approval_status)] : []),
      ...(node.approval !== undefined ? [statusMarkup("Approval field", node.approval)] : []),
      ...(node.source_claim_review !== undefined ? [statusMarkup("Source-claim review", node.source_claim_review)] : []),
    ].join("");

    const equations = Array.isArray(node.equations) ? node.equations : [];
    setList("drawer-equations", equations, (equation) => {
      if (typeof equation === "string") return `<code>${escapeHtml(equation)}</code>`;
      const expression = equation && (equation.expression || equation.equation || equation.formula || equation.math);
      const description = equation && (equation.meaning || equation.description || equation.notes);
      const units = equation && equation.units;
      return `${expression ? `<code>${escapeHtml(expression)}</code>` : `<code>${escapeHtml(JSON.stringify(equation))}</code>`}${description ? `<div>${escapeHtml(description)}</div>` : ""}${units ? `<div class="source-trail">Units: ${escapeHtml(units)}</div>` : ""}`;
    }, "No equations recorded.");
    document.getElementById("drawer-equations-section").classList.toggle("hidden", !equations.length);
    renderClaims(node);

    setList("drawer-assumptions", node.assumptions, (value) => escapeHtml(typeof value === "string" ? value : JSON.stringify(value)), "No assumptions recorded.");
    document.getElementById("drawer-assumptions-section").classList.toggle("hidden", !(node.assumptions || []).length);
    setList("drawer-limitations", node.limitations, (value) => escapeHtml(typeof value === "string" ? value : JSON.stringify(value)), "No limitations recorded.");
    document.getElementById("drawer-limitations-section").classList.toggle("hidden", !(node.limitations || []).length);

    setList("drawer-sources", node.sources, (source) => {
      if (typeof source === "string") return `<span>${escapeHtml(source)}</span>`;
      const title = source.title || source.id || "Reference";
      const href = safeExternalUrl(source.url) || (source.doi ? `https://doi.org/${encodeURIComponent(source.doi)}` : null);
      const link = href ? `<a class="source-link" href="${escapeHtml(href)}" target="_blank" rel="noopener">${escapeHtml(source.doi ? `doi:${source.doi}` : (source.url || "Open source"))}</a>` : "";
      const locator = source.locator || source.section || source.page || source.path;
      const supports = source.supports ? `<div class="source-sec">Claim scope: ${escapeHtml(displayValue(source.supports))}</div>` : "";
      const scope = source.scope ? `<div class="source-sec">Source scope: ${escapeHtml(source.scope)}</div>` : "";
      const claimIds = source.claim_ids && source.claim_ids.length ? `<div class="source-sec">Linked claim IDs: ${escapeHtml(displayValue(source.claim_ids))}</div>` : "";
      const citationApproval = source.owner_citation_approval ? `<div class="source-sec">Owner citation approval: ${escapeHtml(source.owner_citation_approval)}</div>` : "";
      return `<div class="source-title">${escapeHtml(title)}</div>${link}${locator ? `<div class="source-sec">Locator: ${escapeHtml(locator)}</div>` : ""}${supports}${scope}${claimIds}${source.source_access ? `<div class="source-sec">Access: ${escapeHtml(source.source_access)}</div>` : ""}${source.review ? `<div class="source-sec">Attachment review: ${escapeHtml(source.review)}</div>` : ""}${citationApproval}<div class="source-sec">Human citation verification: ${escapeHtml(displayStatus(source.human_verified))}</div>`;
    }, "No source records attached.");
    setList("drawer-questions", node.open_questions, (questionText) => escapeHtml(typeof questionText === "string" ? questionText : JSON.stringify(questionText)), "No open questions.");

    const ownerRelated = [...new Set(node.related_ids || [])];
    setList("drawer-related", ownerRelated, (id) => {
      const target = rawNodes.find((item) => item.id === id);
      return target
        ? `<button class="related-node" data-node-nav="${escapeHtml(id)}">${escapeHtml(target.title)} · ${escapeHtml(id)}</button>`
        : `<span>${escapeHtml(id)} · target unavailable in this snapshot</span>`;
    }, "No related owner nodes recorded.");

    const linkedReferenceIds = [...new Set([
      ...(node.related_ai_reference_ids || []),
      ...(node.ai_reference_related_ids || []),
    ])];
    currentOwnerReferenceIds = activeMode === "owner" ? linkedReferenceIds : [];
    const availableReferenceIds = currentOwnerReferenceIds.filter((id) =>
      (referenceMap.nodes || []).some((item) => item.id === id)
    );
    const referenceLaunch = document.getElementById("drawer-reference-links-section");
    referenceLaunch.classList.toggle("hidden", !availableReferenceIds.length);
    document.getElementById("open-linked-references").textContent = `Explore AI references (${availableReferenceIds.length})`;

    renderOwnerReader(node);
    renderBackgroundFiles(node);
    renderFileAudit(node);
    document.getElementById("drawer-audit-details").open = false;

    renderBreadcrumb(node);
    renderSiblingNavigation(node);
    drawer.classList.remove("hidden");
    btnFocus.disabled = false;
    if (drawerWasHidden) shouldFitAfterLayout = true;
    renderTree();
    updateSourceStatus();
  }

  function navigateToNode(nodeId) {
    if (!nodeId) return;
    const node = rawNodes.find((item) => item.id === nodeId);
    if (!node) return;
    BepMindMapGraph.parentPath(rawNodes, node.id).forEach((item) => collapsedNodes.delete(item.id));
    showDrawer(node);
    renderTree();
    if (focusMode) fitView();
  }

  function showReferenceNode(nodeId) {
    const panelWasHidden = referencePanel.classList.contains("hidden");
    const item = (referenceMap.nodes || []).find((node) => node.id === nodeId);
    const title = document.getElementById("reference-panel-title");
    const summary = document.getElementById("reference-panel-summary");
    const claimsContainer = document.getElementById("reference-panel-claims");
    const sourcesContainer = document.getElementById("reference-panel-sources");
    const uncertaintiesList = document.getElementById("reference-panel-uncertainties");
    const relatedSection = document.getElementById("reference-panel-related-section");
    const relatedList = document.getElementById("reference-panel-related");
    if (!item) {
      title.textContent = "AI reference unavailable";
      summary.textContent = "This reference node is not present in the loaded snapshot.";
      claimsContainer.innerHTML = "";
      sourcesContainer.innerHTML = "";
      uncertaintiesList.innerHTML = "";
      relatedSection.classList.add("hidden");
      referencePanel.classList.remove("hidden");
      if (panelWasHidden) {
        shouldFitAfterLayout = true;
        renderTree();
      }
      return;
    }
    title.textContent = item.title || item.id;
    summary.textContent = item.summary || item.explanation || "No summary recorded.";
    const refs = [...(item.claim_refs || []), ...(item.claims || [])];
    claimsContainer.innerHTML = refs.length ? refs.map((claim) => {
      const support = claim.supports || claim.statement || "Evidence note not recorded.";
      const locator = claim.locator ? `<div class="reference-meta">Locator: ${escapeHtml(claim.locator)}</div>` : "";
      const sourceId = claim.source_id ? `<div class="reference-meta">Source record: ${escapeHtml(claim.source_id)}</div>` : "";
      const evidence = claim.evidence_type ? `<div class="reference-meta">Evidence type: ${escapeHtml(claim.evidence_type)}</div>` : "";
      return `<article class="reference-claim"><p>${escapeHtml(displayValue(support))}</p>${locator}${sourceId}${evidence}</article>`;
    }).join("") : '<p class="empty-state">No claim references are attached to this node.</p>';

    const sourceIds = new Set(refs.map((claim) => claim.source_id).filter(Boolean));
    (item.source_ids || []).forEach((id) => sourceIds.add(id));
    const sourceRecords = (referenceMap.sources || []).filter((source) => sourceIds.has(source.id));
    const sourceCards = sourceRecords.length ? sourceRecords.map((source) => {
      const href = safeExternalUrl(source.url) || (source.doi ? `https://doi.org/${encodeURIComponent(source.doi)}` : null);
      const link = href ? `<a href="${escapeHtml(href)}" target="_blank" rel="noopener">${escapeHtml(source.doi ? `doi:${source.doi}` : source.url)}</a>` : "";
      const fields = [
        source.locator ? `Locator: ${source.locator}` : "",
        source.source_access || source.access_status ? `Access: ${source.source_access || source.access_status}` : "",
        source.verification ? `AI review: ${source.verification}` : "",
        `Human verification: ${displayStatus(source.human_verified)}`,
      ].filter(Boolean).map((value) => `<div class="reference-meta">${escapeHtml(value)}</div>`).join("");
      return `<article class="reference-source"><strong>${escapeHtml(source.title || source.id)}</strong>${link ? `<div>${link}</div>` : ""}${fields}</article>`;
    }).join("") : '<p class="empty-state">No linked source records are present in this snapshot.</p>';
    const limitations = Array.isArray(item.limitations) ? item.limitations : (item.limitations ? [item.limitations] : []);
    const questions = Array.isArray(item.open_questions) ? item.open_questions : (item.open_questions ? [item.open_questions] : []);
    const limitMarkup = [...limitations.map((value) => `Limitation: ${displayValue(value)}`), ...questions.map((value) => `Open question: ${displayValue(value)}`)]
      .map((value) => `<li>${escapeHtml(value)}</li>`).join("");
    sourcesContainer.innerHTML = sourceCards + (limitMarkup ? `<ul class="reference-limits">${limitMarkup}</ul>` : "");

    const affected = (entry) => new Set([
      ...(Array.isArray(entry.linked_nodes) ? entry.linked_nodes : []),
      ...(Array.isArray(entry.affected_node_ids) ? entry.affected_node_ids : []),
      ...(Array.isArray(entry.node_ids) ? entry.node_ids : []),
    ]);
    const uncertaintyEntries = (referenceMap.uncertainties || []).filter((entry) => affected(entry).has(item.id));
    uncertaintiesList.innerHTML = uncertaintyEntries.length ? uncertaintyEntries.map((entry) => {
      const priority = entry.priority ? `<strong>${escapeHtml(entry.priority)} · </strong>` : "";
      const status = entry.status ? `<small>${escapeHtml(entry.status)}</small>` : "";
      return `<li>${priority}${escapeHtml(entry.question || entry.title || entry.id || "Uncertainty not described.")}${status}</li>`;
    }).join("") : '<li class="empty-state">No uncertainty ledger entries are directly linked to this node.</li>';

    const ownerLinkedIds = currentOwnerReferenceIds.includes(item.id) ? currentOwnerReferenceIds : [];
    const relatedIds = [...new Set([...(item.related_ids || []), ...ownerLinkedIds])];
    const relatedNodes = relatedIds.map((id) => (referenceMap.nodes || []).find((node) => node.id === id)).filter(Boolean);
    relatedSection.classList.toggle("hidden", !relatedNodes.length);
    relatedList.innerHTML = relatedNodes.map((node) =>
      `<li><button class="related-node" data-reference-node="${escapeHtml(node.id)}">${escapeHtml(node.title || node.id)} · ${escapeHtml(node.id)}</button></li>`
    ).join("");
    referencePanel.classList.remove("hidden");
    if (panelWasHidden) {
      shouldFitAfterLayout = true;
      renderTree();
    }
  }

  function closeDrawer() {
    drawer.classList.add("hidden");
    btnFocus.disabled = !selectedNodeId;
    shouldFitAfterLayout = true;
    renderTree();
  }

  // 7. Pan & Zoom & Fit-View Handlers
  svg.addEventListener("mousedown", (e) => {
    const toggleTarget = e.target.closest("[data-toggle]");
    if (toggleTarget) {
      const toggleId = toggleTarget.getAttribute("data-toggle");
      if (collapsedNodes.has(toggleId)) {
        collapsedNodes.delete(toggleId);
      } else {
        collapsedNodes.add(toggleId);
      }
      renderTree();
      return;
    }

    const nodeTarget = e.target.closest("[data-id]");
    if (nodeTarget) {
      const nodeId = nodeTarget.getAttribute("data-id");
      const node = rawNodes.find((n) => n.id === nodeId);
      if (node) showDrawer(node);
      return;
    }

    isPanning = true;
    startPan = { x: e.clientX - transform.x, y: e.clientY - transform.y };
  });

  window.addEventListener("mousemove", (e) => {
    if (!isPanning) return;
    transform.x = e.clientX - startPan.x;
    transform.y = e.clientY - startPan.y;
    applyTransform();
  });

  window.addEventListener("mouseup", () => {
    isPanning = false;
  });

  svg.addEventListener("wheel", (e) => {
    e.preventDefault();
    const zoomFactor = 1.08;
    const oldScale = transform.scale;
    let newScale = e.deltaY < 0 ? oldScale * zoomFactor : oldScale / zoomFactor;
    newScale = Math.max(0.12, Math.min(2.5, newScale));

    const rect = svg.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    transform.x = mouseX - ((mouseX - transform.x) / oldScale) * newScale;
    transform.y = mouseY - ((mouseY - transform.y) / oldScale) * newScale;
    transform.scale = newScale;
    applyTransform();
  });

  function zoomAtCenter(factor) {
    const rect = svg.getBoundingClientRect();
    const oldScale = transform.scale;
    const newScale = Math.max(0.12, Math.min(2.5, oldScale * factor));
    const anchorX = rect.width / 2;
    const anchorY = rect.height / 2;
    transform.x = anchorX - ((anchorX - transform.x) / oldScale) * newScale;
    transform.y = anchorY - ((anchorY - transform.y) / oldScale) * newScale;
    transform.scale = newScale;
    applyTransform();
  }

  function fitView() {
    if (!visibleHierarchy) return;
    const rect = svg.getBoundingClientRect();

    let minX = -ROOT_WIDTH / 2;
    let maxX = ROOT_WIDTH / 2;
    let minY = -ROOT_HEIGHT / 2;
    let maxY = ROOT_HEIGHT / 2;

    function walk(node) {
      minX = Math.min(minX, node.x);
      maxX = Math.max(maxX, node.x + node.w);
      minY = Math.min(minY, node.y);
      maxY = Math.max(maxY, node.y + node.h);
      if (!collapsedNodes.has(node.id) && node.children) {
        node.children.forEach(walk);
      }
    }
    walk(visibleHierarchy);

    const graphWidth = maxX - minX + 220;
    const graphHeight = maxY - minY + 220;

    const mobileSheet = window.matchMedia("(max-width: 720px)").matches;
    const referenceOpen = !referencePanel.classList.contains("hidden");
    const drawerOpen = !drawer.classList.contains("hidden");
    const activePanel = referenceOpen ? referencePanel : (drawerOpen ? drawer : null);
    let availableWidth = rect.width;
    let availableHeight = rect.height;
    if (activePanel) {
      const panelRect = activePanel.getBoundingClientRect();
      if (mobileSheet) {
        availableHeight = Math.max(160, Math.min(rect.height, panelRect.top - rect.top));
      } else {
        availableWidth = Math.max(260, Math.min(rect.width, panelRect.left - rect.left));
      }
    }
    const scaleX = availableWidth / graphWidth;
    const scaleY = availableHeight / graphHeight;
    const newScale = Math.max(0.16, Math.min(1.0, Math.min(scaleX, scaleY)));

    transform.scale = newScale;
    const centerX = (minX + maxX) / 2;
    const centerY = (minY + maxY) / 2;
    transform.x = availableWidth / 2 - centerX * newScale;
    transform.y = availableHeight / 2 - centerY * newScale;
    applyTransform();
  }

  // 8. Guided tour is generated from the selected snapshot, never a fixed list.
  let TOUR_SEQUENCE = [];
  let currentTourIndex = 0;
  const tourPanel = document.getElementById("tour-panel");
  const tourStepIndicator = document.getElementById("tour-step-indicator");
  const tourStepCategory = document.getElementById("tour-step-category");
  const tourNodeTitle = document.getElementById("tour-node-title");
  const tourNodeRationale = document.getElementById("tour-node-rationale");
  const tourPrevBtn = document.getElementById("tour-prev-btn");
  const tourNextBtn = document.getElementById("tour-next-btn");
  const tourCloseBtn = document.getElementById("tour-close-btn");
  const tourDragHandle = document.getElementById("tour-drag-handle");
  let tourDragState = null;

  function clampTourPanel(left, top) {
    const surface = tourPanel.offsetParent;
    if (!surface) return;
    const maxLeft = Math.max(8, surface.clientWidth - tourPanel.offsetWidth - 8);
    const maxTop = Math.max(8, surface.clientHeight - tourPanel.offsetHeight - 8);
    tourPanel.style.left = Math.max(8, Math.min(left, maxLeft)) + "px";
    tourPanel.style.top = Math.max(8, Math.min(top, maxTop)) + "px";
    tourPanel.style.right = "auto";
    tourPanel.style.bottom = "auto";
    tourPanel.style.transform = "none";
  }

  tourDragHandle.addEventListener("pointerdown", (event) => {
    if (event.target.closest("button")) return;
    const rect = tourPanel.getBoundingClientRect();
    const surface = tourPanel.offsetParent && tourPanel.offsetParent.getBoundingClientRect();
    if (!surface) return;
    tourDragState = {
      pointerId: event.pointerId,
      offsetX: event.clientX - rect.left,
      offsetY: event.clientY - rect.top,
    };
    tourDragHandle.setPointerCapture(event.pointerId);
    event.preventDefault();
  });
  tourDragHandle.addEventListener("pointermove", (event) => {
    if (!tourDragState || event.pointerId !== tourDragState.pointerId) return;
    const surface = tourPanel.offsetParent.getBoundingClientRect();
    clampTourPanel(
      event.clientX - surface.left - tourDragState.offsetX,
      event.clientY - surface.top - tourDragState.offsetY,
    );
  });
  const stopTourDrag = () => { tourDragState = null; };
  tourDragHandle.addEventListener("pointerup", stopTourDrag);
  tourDragHandle.addEventListener("pointercancel", stopTourDrag);
  tourDragHandle.addEventListener("keydown", (event) => {
    const movements = { ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1] };
    const movement = movements[event.key];
    if (!movement || event.target.closest("button")) return;
    event.preventDefault();
    const rect = tourPanel.getBoundingClientRect();
    const surface = tourPanel.offsetParent.getBoundingClientRect();
    const step = event.shiftKey ? 64 : 24;
    clampTourPanel(
      rect.left - surface.left + movement[0] * step,
      rect.top - surface.top + movement[1] * step,
    );
  });
  window.addEventListener("resize", () => {
    if (tourPanel.style.left) {
      clampTourPanel(parseFloat(tourPanel.style.left), parseFloat(tourPanel.style.top));
    }
  });

  function startTour() {
    focusMode = false;
    btnFocus.setAttribute("aria-pressed", "false");
    btnFocus.textContent = "Focus Selected";
    renderTree();
    TOUR_SEQUENCE = BepMindMapGraph.tourSequence(visibleHierarchy);
    if (!TOUR_SEQUENCE.length) return;
    currentTourIndex = 0;
    tourPanel.classList.remove("hidden");
    showTourStep(0);
  }

  function showTourStep(index) {
    if (index < 0 || index >= TOUR_SEQUENCE.length) return;
    currentTourIndex = index;
    const item = TOUR_SEQUENCE[index];
    const node = rawNodes.find((n) => n.id === item.id);
    if (!node) return;

    BepMindMapGraph.parentPath(rawNodes, node.id).forEach((part) => collapsedNodes.delete(part.id));
    selectedNodeId = node.id;
    focusMode = true;
    btnFocus.setAttribute("aria-pressed", "true");
    btnFocus.textContent = "Show Overview";
    renderTree();
    showDrawer(node);
    fitView();

    tourStepIndicator.textContent = "Step " + (index + 1) + " of " + TOUR_SEQUENCE.length;
    tourStepCategory.textContent = item.motion === "return" ? "Backtracking" : "Exploring";
    tourNodeTitle.textContent = node.title;
    tourNodeRationale.textContent = node.summary || "Summary not recorded.";

    tourPrevBtn.disabled = index === 0;
    tourNextBtn.textContent = index === TOUR_SEQUENCE.length - 1 ? "Finish" : "Next";

  }

  function endTour() {
    tourPanel.classList.add("hidden");
  }

  // Tour listeners
  btnTour.addEventListener("click", startTour);
  tourCloseBtn.addEventListener("click", endTour);
  tourPrevBtn.addEventListener("click", () => {
    if (currentTourIndex > 0) showTourStep(currentTourIndex - 1);
  });
  tourNextBtn.addEventListener("click", () => {
    if (currentTourIndex < TOUR_SEQUENCE.length - 1) {
      showTourStep(currentTourIndex + 1);
    } else {
      endTour();
    }
  });


  // 10. Live SSE Reload
  function initLiveReload() {
    try {
      const sse = new EventSource("/events");
      sse.onopen = () => {
        document.getElementById("sync-status").className = "sync-indicator connected";
        document.getElementById("sync-status").textContent = "● Local watch";
      };
      sse.onmessage = (e) => {
        if (e.data === "reload") {
          console.log("[SSE] Reload event received from server.");
          fetchGraph();
        }
      };
      sse.onerror = () => {
        document.getElementById("sync-status").className = "sync-indicator";
        document.getElementById("sync-status").textContent = "○ Local watch disconnected";
      };
    } catch (err) {
      console.warn("SSE not available:", err);
    }
  }

  // 11. Helper Utilities
  function escapeHtml(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function renderSearchResults() {
    const query = graphSearch.value.trim().toLocaleLowerCase();
    if (!query) {
      searchResults.innerHTML = "";
      searchResults.classList.add("hidden");
      return;
    }
    const mapMatches = rawNodes.filter((node) => {
      const sources = (node.sources || []).map((source) => typeof source === "string" ? source : JSON.stringify(source)).join(" ");
      const claims = (node.claims || []).map((claim) => claim.statement || "").join(" ");
      const text = [node.id, node.title, node.question, node.summary, node.rationale, node.notes, sources, claims, ...(node.open_questions || [])].join(" ");
      return text.toLocaleLowerCase().includes(query);
    }).map((node) => ({ type: "map", node }));
    const referenceMatches = activeMode === "owner" ? (referenceMap.nodes || []).filter((node) => {
      const claims = [...(node.claim_refs || []), ...(node.claims || [])]
        .map((claim) => [claim.supports, claim.statement, claim.locator, claim.source_id].join(" ")).join(" ");
      const nodeSourceIds = new Set([
        ...(Array.isArray(node.source_ids) ? node.source_ids : []),
        ...(Array.isArray(node.claim_refs) ? node.claim_refs.map((claim) => claim.source_id) : []),
      ].filter(Boolean));
      const sourceText = (referenceMap.sources || []).filter((source) => nodeSourceIds.has(source.id))
        .map((source) => [source.id, source.title, source.doi, source.url].join(" ")).join(" ");
      const uncertaintyText = (referenceMap.uncertainties || []).filter((entry) => {
        const linkedIds = [entry.linked_nodes, entry.affected_node_ids, entry.node_ids]
          .filter(Array.isArray).flat();
        return linkedIds.includes(node.id);
      }).map((entry) => {
        const evidenceNeeded = Array.isArray(entry.evidence_needed) ? entry.evidence_needed : [entry.evidence_needed || ""];
        return [entry.question, entry.why_open, ...evidenceNeeded].join(" ");
      }).join(" ");
      const openQuestions = Array.isArray(node.open_questions) ? node.open_questions : [node.open_questions || ""];
      const limitations = Array.isArray(node.limitations) ? node.limitations : [node.limitations || ""];
      const text = [node.id, node.title, node.summary, node.explanation, claims, sourceText, uncertaintyText, ...openQuestions, ...limitations].join(" ");
      return text.toLocaleLowerCase().includes(query);
    }).map((node) => ({ type: "reference", node })) : [];
    const matches = [...mapMatches, ...referenceMatches];
    if (!matches.length) {
      searchResults.innerHTML = '<div class="search-empty">No matching nodes in the loaded snapshots.</div>';
      searchResults.classList.remove("hidden");
      return;
    }
    const visibleMatches = matches.slice(0, 40);
    const results = visibleMatches.map(({ type, node }) => type === "reference"
      ? `<button class="search-result reference-search-result" role="option" data-search-reference="${escapeHtml(node.id)}"><span>${escapeHtml(node.title || node.id)}</span><small>AI reference · ${escapeHtml(node.id)}</small></button>`
      : `<button class="search-result" role="option" data-search-node="${escapeHtml(node.id)}"><span>${escapeHtml(node.title)}</span><small>${escapeHtml(node.id)}</small></button>`
    ).join("");
    const count = matches.length > visibleMatches.length ? `<div class="search-count">Showing ${visibleMatches.length} of ${matches.length} matches. Refine the search to narrow results.</div>` : `<div class="search-count">${matches.length} match${matches.length === 1 ? "" : "es"}</div>`;
    searchResults.innerHTML = count + results;
    searchResults.classList.remove("hidden");
  }

  // Event Listeners
  layerSelect.addEventListener("change", () => fetchGraph());
  btnRefresh.addEventListener("click", () => fetchGraph());
  graphSearch.addEventListener("input", renderSearchResults);
  searchResults.addEventListener("click", (event) => {
    const referenceResult = event.target.closest("[data-search-reference]");
    if (referenceResult) {
      showReferenceNode(referenceResult.getAttribute("data-search-reference"));
      searchResults.classList.add("hidden");
      return;
    }
    const result = event.target.closest("[data-search-node]");
    if (!result) return;
    navigateToNode(result.getAttribute("data-search-node"));
    searchResults.classList.add("hidden");
  });
  document.getElementById("drawer-navigation").addEventListener("click", (event) => {
    const target = event.target.closest("[data-node-nav]");
    if (target && !target.disabled) navigateToNode(target.dataset.nodeNav);
  });
  document.getElementById("drawer-breadcrumb").addEventListener("click", (event) => {
    const target = event.target.closest("[data-node-nav]");
    if (target) navigateToNode(target.dataset.nodeNav);
  });
  document.getElementById("drawer-related").addEventListener("click", (event) => {
    const target = event.target.closest("[data-node-nav]");
    if (target) navigateToNode(target.dataset.nodeNav);
  });
  document.getElementById("open-linked-references").addEventListener("click", () => {
    const firstReferenceId = currentOwnerReferenceIds.find((id) =>
      (referenceMap.nodes || []).some((item) => item.id === id)
    );
    if (firstReferenceId) showReferenceNode(firstReferenceId);
  });
  document.getElementById("reference-panel-close").addEventListener("click", () => {
    referencePanel.classList.add("hidden");
    shouldFitAfterLayout = true;
    renderTree();
  });
  document.getElementById("reference-panel-related").addEventListener("click", (event) => {
    const target = event.target.closest("[data-reference-node]");
    if (target) showReferenceNode(target.dataset.referenceNode);
  });
  document.getElementById("drawer-background-files").addEventListener("click", (event) => {
    const target = event.target.closest("[data-background-index]");
    if (target && selectedNodeId) loadBackgroundFile(selectedNodeId, Number(target.dataset.backgroundIndex), target);
  });
  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-reader-image-path]");
    if (!button || activeMode !== "owner" || !selectedNodeId) return;
    let output = button.nextElementSibling;
    if (!output || !output.classList.contains("reader-figure-output")) {
      output = document.createElement("span");
      output.className = "reader-figure-output";
      const image = document.createElement("img");
      image.alt = button.dataset.readerImageAlt || "Reader figure";
      image.loading = "lazy";
      image.src = `/api/figure?node_id=${encodeURIComponent(selectedNodeId)}&path=${encodeURIComponent(button.dataset.readerImagePath)}`;
      image.addEventListener("error", () => {
        output.textContent = "This figure is not available from the selected reader snapshot.";
      }, { once: true });
      output.appendChild(image);
      button.insertAdjacentElement("afterend", output);
      button.dataset.figureLoaded = "true";
      button.textContent = "Hide figure";
      return;
    }
    output.classList.toggle("hidden");
    button.textContent = output.classList.contains("hidden")
      ? `Show figure: ${button.dataset.readerImageAlt || "Open figure"}`
      : "Hide figure";
  });
  btnFit.addEventListener("click", fitView);
  btnZoomIn.addEventListener("click", () => zoomAtCenter(1.25));
  btnZoomOut.addEventListener("click", () => zoomAtCenter(0.8));
  btnFocus.addEventListener("click", () => {
    if (!selectedNodeId) return;
    focusMode = !focusMode;
    btnFocus.setAttribute("aria-pressed", String(focusMode));
    btnFocus.textContent = focusMode ? "Show Overview" : "Focus Selected";
    shouldFitAfterLayout = true;
    renderTree();
  });
  btnExpandAll.addEventListener("click", () => {
    if (rawNodes.length > 80 && !window.confirm(`This snapshot has ${rawNodes.length} nodes. Expanding all branches may make the canvas hard to read. Expand anyway?`)) return;
    collapsedNodes.clear();
    shouldFitAfterLayout = true;
    renderTree();
  });
  btnCollapseAll.addEventListener("click", () => {
    rawNodes.forEach((n) => {
      if (n.parent) collapsedNodes.add(n.id);
    });
    shouldFitAfterLayout = true;
    renderTree();
  });
  window.addEventListener("resize", () => fitView());
  drawerCloseBtn.addEventListener("click", closeDrawer);

  // Initial Boot
  configureModes().then(() => fetchGraph());
  initLiveReload();
})();
