"""YAML Schema definitions and validation for BEP Ownership Mind Map.

Adheres to PR #84 specifications, 4-tier agency hierarchy, and Rule 16 zero-hallucination citations.
"""

from __future__ import annotations

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from typing import Any, Dict, List, Literal, Optional, Set, Union
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


ProgressStage = Literal[
    "idea",
    "ai_worked_out",
    "human_worked_out",
    "informal_writing",
    "formal_writing",
]

PROGRESS_STAGES = (
    "idea",
    "ai_worked_out",
    "human_worked_out",
    "informal_writing",
    "formal_writing",
)

# Historical labels remain available for display and migration tooling. A tier
# value is never treated as proof of owner understanding or citation review.
LEGACY_TIER_TO_STAGE = {
    0: "idea",
    1: "ai_worked_out",
    2: "human_worked_out",
    3: "informal_writing",
    4: "formal_writing",
}


class SourceItem(BaseModel):
    """Source reference item for zero-hallucination citation backing."""
    model_config = ConfigDict(extra="allow", validate_assignment=True)

    title: str = Field(description="Document title, paper name, or code reference")
    doi: Optional[str] = Field(default=None, description="Verified DOI or publication identifier")
    path: Optional[str] = Field(default=None, description="Local file path, analysis note, or notebook cell")
    citation: Optional[str] = Field(default=None, description="Formal citation key or BibTeX reference")
    section: Optional[str] = Field(default=None, description="Verified section, table, or equation in the source")


SourceType = Union[str, SourceItem, Dict[str, Any]]


class MindMapNode(BaseModel):
    """A single node in the BEP ownership mind map."""
    model_config = ConfigDict(extra="allow", validate_assignment=True)

    id: str = Field(description="Unique node identifier (slug formatted, e.g. 'physics', 'thiele_modulus')")
    parent: Optional[str] = Field(default=None, description="ID of parent node, or null/None for root")
    title: str = Field(description="Human readable display title of the node")
    tier: int = Field(default=1, ge=0, le=4, description="Maturity tier (0: Idea, 1: AI Proposal, 2: Owner Understood, 3: Informal Notes, 4: Formal Writing)")
    importance: Optional[int] = Field(default=None, ge=0, le=3, description="Importance stars (0 to 3, or null)")
    rationale: str = Field(default="", description="Why this node exists and its relevance to the thesis")
    notes: str = Field(default="", description="Technical details, equations, or personal reflection notes")
    sources: List[SourceType] = Field(default_factory=list, description="List of verified citations or repository references")
    open_questions: List[str] = Field(default_factory=list, description="Open research or modeling questions attached to this node")
    is_draft: bool = Field(default=False, description="Flag indicating if the node is part of the AI draft overlay")

    @field_validator("id")
    @classmethod
    def validate_id_slug(cls, v: str) -> str:
        v_clean = v.strip().lower()
        if not v_clean:
            raise ValueError("Node id cannot be empty.")
        if not all(c.isalnum() or c in ("_", "-", ".") for c in v_clean):
            raise ValueError(f"Node id '{v}' must be alphanumeric with underscores, hyphens, or dots.")
        return v_clean

    @field_validator("title")
    @classmethod
    def validate_title_non_empty(cls, v: str) -> str:
        v_clean = v.strip()
        if not v_clean:
            raise ValueError("Node title cannot be empty.")
        return v_clean


class MindMap(BaseModel):
    """The complete mind map or draft overlay graph."""
    model_config = ConfigDict(extra="allow", validate_assignment=True)

    nodes: List[MindMapNode] = Field(default_factory=list, description="List of nodes in the graph")

    @model_validator(mode="after")
    def validate_graph_structure(self) -> MindMap:
        """Validate uniqueness, single root (if canonical), parent references, and acyclicity."""
        node_ids: Set[str] = set()
        nodes_by_id: Dict[str, MindMapNode] = {}

        for node in self.nodes:
            if node.id in node_ids:
                raise ValueError(f"Duplicate node id detected: '{node.id}'")
            node_ids.add(node.id)
            nodes_by_id[node.id] = node

        # Check acyclicity: follow parent pointers to detect cycles
        for start_id in node_ids:
            curr: Optional[str] = start_id
            seen_in_path: Set[str] = set()
            while curr is not None:
                if curr in seen_in_path:
                    raise ValueError(f"Cycle detected involving node '{curr}'")
                seen_in_path.add(curr)
                parent_node = nodes_by_id.get(curr)
                if parent_node is None:
                    break
                curr = parent_node.parent

        return self

    def validate_canonical_integrity(self) -> None:
        """Validate canonical rules: root node 'bep' and three main arms 'physics', 'mathematics', 'systems_control'."""
        node_ids = {node.id for node in self.nodes}
        if "bep" not in node_ids:
            raise ValueError("Canonical map must contain a root node with id 'bep'")

        root_node = next(n for n in self.nodes if n.id == "bep")
        if root_node.parent is not None:
            raise ValueError(f"Root node 'bep' must have parent=null, found '{root_node.parent}'")

        required_arms = {"physics", "mathematics", "systems_control"}
        for arm_id in required_arms:
            if arm_id not in node_ids:
                raise ValueError(f"Canonical map must contain arm '{arm_id}' under 'bep'")
            arm_node = next(n for n in self.nodes if n.id == arm_id)
            if arm_node.parent != "bep":
                raise ValueError(f"Arm node '{arm_id}' must have parent='bep', found '{arm_node.parent}'")

    def validate_parents_exist(self, allowed_external_parents: Optional[Set[str]] = None) -> None:
        """Check that every non-root node has a parent either in this map or in allowed_external_parents."""
        known_parents = {node.id for node in self.nodes}
        if allowed_external_parents:
            known_parents.update(allowed_external_parents)

        for node in self.nodes:
            if node.parent is not None:
                if node.parent not in known_parents:
                    raise ValueError(f"Node '{node.id}' references non-existent parent '{node.parent}'")

    def get_node(self, node_id: str) -> Optional[MindMapNode]:
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None


class OwnerRecord(BaseModel):
    """Base for owner-map records; unrecognized metadata survives round trips."""

    model_config = ConfigDict(extra="allow", validate_assignment=True, strict=True)


class OwnerReferenceLink(OwnerRecord):
    """A claim-specific link into the separate AI reference map."""

    reference_node_id: Optional[str] = None
    reference_claim_id: Optional[str] = None
    source_id: Optional[str] = None
    reference_commit: Optional[str] = None
    relation_to_claim: Optional[str] = None
    ai_interpretation_note: Optional[str] = None
    owner_review: Optional[str] = None
    human_verified: Optional[bool] = None
    source_record_exists: Optional[bool] = None
    source_record_status: Optional[str] = None


class ReferenceClaimRef(OwnerRecord):
    """Source-locator evidence pointer in the separate AI reference graph."""

    id: Optional[str] = None
    claim_id: Optional[str] = None
    source_id: Optional[str] = None
    locator: Optional[str] = None
    evidence_type: Optional[str] = None
    supports: Optional[Union[str, List[str]]] = None


class OwnerClaim(OwnerRecord):
    """A bounded claim with independently reviewable source links."""

    id: Optional[str] = None
    statement: Optional[str] = None
    evidence_type: Optional[str] = None
    source_ids: List[str] = Field(default_factory=list)
    status: Optional[str] = None
    ai_attached: Optional[bool] = None
    human_verified: Optional[bool] = None
    ai_reference_links: List[OwnerReferenceLink] = Field(default_factory=list)


class OwnerSource(OwnerRecord):
    """A source record; absent review fields stay absent rather than becoming approved."""

    id: Optional[str] = None
    title: Optional[str] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    path: Optional[str] = None
    locator: Optional[str] = None
    source_access: Optional[str] = None
    access_status: Optional[str] = None
    verification: Optional[str] = None
    supports: Union[str, List[str]] = Field(default_factory=list)
    review: Optional[str] = None
    human_verified: Optional[bool] = None
    owner_read_status: Optional[str] = None
    owner_citation_approval: Optional[str] = None


class OwnerMapNode(OwnerRecord):
    """Validated view of a rich personal-map node without rewriting its metadata."""

    id: str
    parent: Optional[str] = None
    title: str
    kind: Optional[str] = None
    approval: Optional[str] = None
    structural_approval: Optional[str] = None
    structure_status: Optional[str] = None
    owner_structure_approval_scope: Optional[str] = None
    owner_read_status: Optional[str] = None
    owner_content_approval: Optional[str] = None
    owner_approval_status: Optional[str] = None
    understanding_status: Optional[str] = None
    human_understanding_review: Optional[str] = None
    source_claim_review: Optional[str] = None
    maturity: Optional[str] = None
    progress_stage: Optional[ProgressStage] = None
    tier: Optional[int] = Field(default=None, ge=0, le=4)
    importance: Optional[int] = Field(default=None, ge=0, le=3)
    rationale: Optional[str] = None
    summary: Optional[str] = None
    notes: Optional[str] = None
    equations: List[Any] = Field(default_factory=list)
    claims: List[OwnerClaim] = Field(default_factory=list)
    claim_refs: List[ReferenceClaimRef] = Field(default_factory=list)
    sources: List[Union[str, OwnerSource]] = Field(default_factory=list)
    assumptions: List[Any] = Field(default_factory=list)
    limitations: List[Any] = Field(default_factory=list)
    related_ids: List[str] = Field(default_factory=list)
    ai_reference_related_ids: List[str] = Field(default_factory=list)
    research_letters: List[str] = Field(default_factory=list)
    open_questions: List[str] = Field(default_factory=list)
    origin: Optional[str] = None

    @field_validator("id")
    @classmethod
    def validate_stable_id(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Owner-map node id cannot be empty.")
        return value

    @field_validator("title")
    @classmethod
    def validate_owner_title(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Owner-map node title cannot be empty.")
        return value


class OwnerMapDocument(OwnerRecord):
    """Lossless adapter for the independently authored owner-working map."""

    nodes: List[OwnerMapNode]

    @model_validator(mode="after")
    def validate_graph(self) -> "OwnerMapDocument":
        if not self.nodes:
            raise ValueError("Owner map must contain at least one node.")

        nodes_by_id: Dict[str, OwnerMapNode] = {}
        for node in self.nodes:
            if node.id in nodes_by_id:
                raise ValueError(f"Duplicate owner-map node id: '{node.id}'")
            nodes_by_id[node.id] = node

        roots = [node.id for node in self.nodes if node.parent is None]
        if len(roots) != 1:
            raise ValueError(f"Owner map must have exactly one root; found {len(roots)}.")

        for node in self.nodes:
            if node.parent is not None and node.parent not in nodes_by_id:
                raise ValueError(
                    f"Owner-map node '{node.id}' references missing parent '{node.parent}'."
                )

        for start_id in nodes_by_id:
            seen: Set[str] = set()
            current: Optional[str] = start_id
            while current is not None:
                if current in seen:
                    raise ValueError(f"Cycle detected involving owner-map node '{current}'.")
                seen.add(current)
                current = nodes_by_id[current].parent

        return self


class ReferenceMapDocument(OwnerRecord):
    """Optional AI reference records used to resolve owner-map citations."""

    nodes: List[OwnerMapNode] = Field(default_factory=list)
    sources: List[OwnerSource] = Field(default_factory=list)


def merge_maps(canonical: MindMap, overlay: MindMap) -> MindMap:
    """Merge canonical map with draft overlay into a combined graph for visualization."""
    merged_nodes: Dict[str, MindMapNode] = {}
    for node in canonical.nodes:
        node_copy = node.model_copy()
        node_copy.is_draft = False
        merged_nodes[node.id] = node_copy

    for node in overlay.nodes:
        node_copy = node.model_copy()
        node_copy.is_draft = True
        merged_nodes[node.id] = node_copy

    combined = MindMap(nodes=list(merged_nodes.values()))
    combined.validate_parents_exist()
    return combined
