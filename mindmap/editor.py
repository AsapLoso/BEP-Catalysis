"""Deterministic Python Editor Engine for BEP Ownership Mind Map.

Provides atomic, schema-validated mutations for canonical and draft overlay YAML files.
"""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import argparse
import os
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union

import yaml

try:
    from Academics.BEP.Catalysis.mindmap.schema import MindMap, MindMapNode, SourceItem, SourceType
except (ImportError, ModuleNotFoundError):
    from schema import MindMap, MindMapNode, SourceItem, SourceType


PROMOTION_DISABLED_MESSAGE = (
    "Promotion is disabled. Moving a node between maps requires a separately recorded, "
    "scoped owner decision; placement must not imply human understanding or citation verification."
)
LEGACY_TIER_WRITE_MESSAGE = (
    "Legacy tiers 2-4 are read-only because they can imply owner understanding or writing status. "
    "Use the explicit five-stage owner-map field in a reviewed snapshot instead."
)
OWNER_REVIEW_WRITE_MESSAGE = (
    "Owner progress, placement approval, reading status, and citation verification are read-only in the legacy editor. "
    "Load an explicit owner snapshot for review; no UI or AI-map operation may assert those decisions."
)
OWNER_REVIEW_FIELDS = {
    "progress_stage",
    "maturity",
    "approval",
    "structural_approval",
    "structure_status",
    "owner_structure_approval_scope",
    "owner_read_status",
    "owner_content_approval",
    "owner_approval_status",
    "understanding_status",
    "human_understanding_review",
    "source_claim_review",
    "owner_citation_approval",
}


def _reject_owner_review_mutation(value: Any) -> None:
    """Keep explicit owner-review fields outside legacy editor write paths."""
    if isinstance(value, dict):
        for key, item in value.items():
            if key in OWNER_REVIEW_FIELDS:
                raise ValueError(OWNER_REVIEW_WRITE_MESSAGE)
            if key == "human_verified" and item is True:
                raise ValueError(OWNER_REVIEW_WRITE_MESSAGE)
            if key == "review" and str(item).lower() in {"human_verified", "verified", "approved"}:
                raise ValueError(OWNER_REVIEW_WRITE_MESSAGE)
            _reject_owner_review_mutation(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _reject_owner_review_mutation(item)


def load_map(path: Union[str, Path]) -> MindMap:
    """Load and validate a MindMap from a YAML file."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Mind map file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    if not isinstance(data, dict) or "nodes" not in data:
        raise ValueError(f"Invalid mind map file structure in {path}: expected dict with 'nodes' key.")

    return MindMap.model_validate(data)


def save_map(map_data: MindMap, path: Union[str, Path], is_canonical: bool = False, allowed_external_parents: Optional[Set[str]] = None) -> None:
    """Save a MindMap to a YAML file atomically with fail-closed validation."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Validate before write
    if is_canonical:
        map_data.validate_canonical_integrity()
        map_data.validate_parents_exist()
    elif allowed_external_parents is not None:
        map_data.validate_parents_exist(allowed_external_parents=allowed_external_parents)

    # Dump to YAML format
    data_dict = map_data.model_dump(exclude_none=False, mode="json")
    yaml_str = yaml.dump(data_dict, sort_keys=False, allow_unicode=True, indent=2)

    # Atomic write via temp file in same directory
    temp_dir = path.parent
    with tempfile.NamedTemporaryFile("w", dir=temp_dir, delete=False, encoding="utf-8") as tf:
        tf.write(yaml_str)
        tf.flush()
        os.fsync(tf.fileno())
        temp_name = tf.name

    # Resilient atomic replace with exponential backoff on Windows file locks
    max_retries = 8
    for attempt in range(max_retries):
        try:
            os.replace(temp_name, path)
            break
        except (PermissionError, OSError):
            if attempt == max_retries - 1:
                if os.path.exists(temp_name):
                    try:
                        os.remove(temp_name)
                    except Exception:
                        pass
                raise
            time.sleep(0.05 * (1.5 ** attempt))


def add_node(
    path: Union[str, Path],
    node: Union[MindMapNode, Dict[str, Any]],
    is_canonical: bool = False,
    allowed_external_parents: Optional[Set[str]] = None,
) -> MindMapNode:
    """Add a new node to the mind map file."""
    m = load_map(path)
    if isinstance(node, dict):
        new_node = MindMapNode.model_validate(node)
    else:
        new_node = node

    _reject_owner_review_mutation(new_node.model_dump(exclude_unset=True))

    if new_node.tier >= 2:
        raise ValueError(LEGACY_TIER_WRITE_MESSAGE)

    if any(n.id == new_node.id for n in m.nodes):
        raise ValueError(f"Node id '{new_node.id}' already exists in {path}")

    # Check parent
    if new_node.parent is not None:
        known_parents = {n.id for n in m.nodes}
        if allowed_external_parents:
            known_parents.update(allowed_external_parents)
        if new_node.parent not in known_parents:
            raise ValueError(f"Parent '{new_node.parent}' does not exist.")

    m.nodes.append(new_node)
    save_map(m, path, is_canonical=is_canonical, allowed_external_parents=allowed_external_parents)
    return new_node


def edit_node(
    path: Union[str, Path],
    node_id: str,
    is_canonical: bool = False,
    allowed_external_parents: Optional[Set[str]] = None,
    **updates: Any,
) -> MindMapNode:
    """Edit fields of an existing node in the mind map."""
    requested_tier = updates.get("tier")
    if requested_tier is not None and requested_tier >= 2:
        raise ValueError(LEGACY_TIER_WRITE_MESSAGE)
    _reject_owner_review_mutation(updates)

    m = load_map(path)
    target = None
    target_idx = -1
    for idx, node in enumerate(m.nodes):
        if node.id == node_id:
            target = node
            target_idx = idx
            break

    if target is None:
        raise ValueError(f"Node '{node_id}' not found in {path}")

    node_dict = target.model_dump()
    for k, v in updates.items():
        if v is not None and k in node_dict:
            node_dict[k] = v

    updated_node = MindMapNode.model_validate(node_dict)
    m.nodes[target_idx] = updated_node

    save_map(m, path, is_canonical=is_canonical, allowed_external_parents=allowed_external_parents)
    return updated_node


def reparent_node(
    path: Union[str, Path],
    node_id: str,
    new_parent_id: Optional[str],
    is_canonical: bool = False,
    allowed_external_parents: Optional[Set[str]] = None,
) -> MindMapNode:
    """Change the parent of an existing node, checking for cycles."""
    if node_id == new_parent_id:
        raise ValueError("A node cannot be its own parent.")

    m = load_map(path)
    target = next((n for n in m.nodes if n.id == node_id), None)
    if target is None:
        raise ValueError(f"Node '{node_id}' not found in {path}")

    if target.id == "bep" and new_parent_id is not None:
        raise ValueError("Root node 'bep' cannot have a parent.")

    if new_parent_id is not None:
        known = {n.id for n in m.nodes}
        if allowed_external_parents:
            known.update(allowed_external_parents)
        if new_parent_id not in known:
            raise ValueError(f"New parent '{new_parent_id}' does not exist.")

    target.parent = new_parent_id
    save_map(m, path, is_canonical=is_canonical, allowed_external_parents=allowed_external_parents)
    return target


def delete_node(
    path: Union[str, Path],
    node_id: str,
    cascade: bool = False,
    is_canonical: bool = False,
) -> List[str]:
    """Delete a node from the map. If cascade is True, delete all descendant nodes."""
    m = load_map(path)
    if is_canonical and node_id in ("bep", "physics", "mathematics", "systems_control"):
        raise ValueError(f"Cannot delete protected canonical node '{node_id}'")

    target = next((n for n in m.nodes if n.id == node_id), None)
    if target is None:
        raise ValueError(f"Node '{node_id}' not found in {path}")

    # Build children map
    children_map: Dict[str, List[str]] = {}
    for n in m.nodes:
        if n.parent:
            children_map.setdefault(n.parent, []).append(n.id)

    to_delete: Set[str] = {node_id}
    if cascade:
        queue = [node_id]
        while queue:
            curr = queue.pop(0)
            for child in children_map.get(curr, []):
                to_delete.add(child)
                queue.append(child)
    else:
        # Check if it has children
        children = children_map.get(node_id, [])
        if children:
            raise ValueError(f"Cannot delete node '{node_id}' because it has {len(children)} children. Reparent or use cascade=True.")

    deleted_ids = list(to_delete)
    m.nodes = [n for n in m.nodes if n.id not in to_delete]
    allowed = None
    if not is_canonical:
        try:
            canonical_path = Path(path).parent / "bep_map.yaml"
            if canonical_path.exists():
                can = load_map(canonical_path)
                allowed = {n.id for n in can.nodes}
        except Exception:
            pass
    save_map(m, path, is_canonical=is_canonical, allowed_external_parents=allowed)
    return deleted_ids


def set_tier(
    path: Union[str, Path],
    node_id: str,
    tier: int,
    is_canonical: bool = False,
) -> MindMapNode:
    """Set a legacy AI-reference tier; owner-progress tiers are read-only."""
    if not (0 <= tier <= 4):
        raise ValueError(f"Tier must be between 0 and 4, got {tier}")
    if tier >= 2:
        raise ValueError(LEGACY_TIER_WRITE_MESSAGE)
    return edit_node(path, node_id, tier=tier, is_canonical=is_canonical)


def set_importance(
    path: Union[str, Path],
    node_id: str,
    importance: Optional[int],
    is_canonical: bool = False,
) -> MindMapNode:
    """Set the importance stars (0 to 3, or None) of a node."""
    if importance is not None and not (0 <= importance <= 3):
        raise ValueError(f"Importance must be 0, 1, 2, 3 or null, got {importance}")
    return edit_node(path, node_id, importance=importance, is_canonical=is_canonical)


def attach_source(
    path: Union[str, Path],
    node_id: str,
    source: SourceType,
    is_canonical: bool = False,
) -> MindMapNode:
    """Attach a source record without implying human verification."""
    if isinstance(source, dict):
        _reject_owner_review_mutation(source)
    elif isinstance(source, SourceItem):
        _reject_owner_review_mutation(source.model_dump(exclude_unset=True))
    m = load_map(path)
    target = next((n for n in m.nodes if n.id == node_id), None)
    if target is None:
        raise ValueError(f"Node '{node_id}' not found in {path}")

    # Validate source
    if isinstance(source, dict):
        source_obj = SourceItem.model_validate(source)
        target.sources.append(source_obj)
    else:
        target.sources.append(source)

    save_map(m, path, is_canonical=is_canonical)
    return target


def promote_draft_node(
    draft_path: Union[str, Path],
    canonical_path: Union[str, Path],
    node_id: str,
    new_tier: int = 2,
    cascade: bool = False,
) -> MindMapNode:
    """Retain the legacy call shape while refusing unsafe implicit promotion."""
    raise ValueError(PROMOTION_DISABLED_MESSAGE)


def main() -> None:
    parser = argparse.ArgumentParser(description="BEP Mind Map Editor CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # validate
    val_p = subparsers.add_parser("validate", help="Validate a mind map YAML file")
    val_p.add_argument("path", help="Path to YAML file")
    val_p.add_argument("--canonical", action="store_true", help="Validate canonical integrity")

    # set-tier
    tier_p = subparsers.add_parser("set-tier", help="Set node tier")
    tier_p.add_argument("path", help="Path to YAML file")
    tier_p.add_argument("id", help="Node ID")
    tier_p.add_argument("tier", type=int, choices=[0, 1], help="AI-reference legacy tier (0=Idea, 1=AI proposal)")

    # set-importance
    imp_p = subparsers.add_parser("set-importance", help="Set node importance stars")
    imp_p.add_argument("path", help="Path to YAML file")
    imp_p.add_argument("id", help="Node ID")
    imp_p.add_argument("stars", type=int, choices=[0, 1, 2, 3], help="Importance stars")

    args = parser.parse_args()

    if args.command == "validate":
        m = load_map(args.path)
        if args.canonical:
            m.validate_canonical_integrity()
            m.validate_parents_exist()
        print(f"Validation successful: {len(m.nodes)} nodes in {args.path}")
    elif args.command == "set-tier":
        updated = set_tier(args.path, args.id, args.tier)
        print(f"Node '{updated.id}' tier set to {updated.tier}")
    elif args.command == "set-importance":
        updated = set_importance(args.path, args.id, args.stars)
        print(f"Node '{updated.id}' importance set to {updated.importance}")


if __name__ == "__main__":
    main()
