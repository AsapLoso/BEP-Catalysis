#!/usr/bin/env python3
"""Validate graph and provenance references in this AI scientific map."""
from collections import Counter
from pathlib import Path
import json
import sys
from datetime import datetime, timezone
import yaml

ROOT = Path(__file__).resolve().parent
FILES = [
    'nodes.yaml', 'sources.yaml', 'concept_mapping.yaml', 'source_provenance.yaml',
    'interdisciplinary_links.yaml', 'claim_reconciliations.yaml', 'uncertainties.yaml', 'coverage.yaml',
    'evidence_audit.yaml'
]
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def load(name):
    return yaml.safe_load((ROOT / name).read_text(encoding='utf-8'))

for name in FILES:
    require((ROOT / name).is_file(), f'missing required file: {name}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)

graph = load('nodes.yaml')
nodes = graph['nodes']
node_by_id = {n['id']: n for n in nodes}
source_rows = load('sources.yaml')['sources']
sources = {s['id']: s for s in source_rows}
concept_doc = load('concept_mapping.yaml')
concepts = concept_doc['concepts']
crosswalk = concept_doc['prior_reconciliation_crosswalk']
provenance = load('source_provenance.yaml')
attachments = provenance['original_overlay_attachment_records']
research_additions = provenance.get('research_additions', [])
link_doc = load('interdisciplinary_links.yaml')
links = link_doc['links']
claim_rec_doc = load('claim_reconciliations.yaml')
claim_recs = claim_rec_doc['claims']
uncertainty_doc = load('uncertainties.yaml')
uncertainties = uncertainty_doc['uncertainties']
coverage = load('coverage.yaml')['coverage']
audit_doc = load('evidence_audit.yaml')
audit_entries = audit_doc['entries']

require(len(node_by_id) == len(nodes), 'duplicate node IDs')
require(len(sources) == len(source_rows), 'duplicate source IDs')
require(sum(n.get('parent') is None for n in nodes) == 1, 'graph must have one root')
require(node_by_id.get('bep', {}).get('parent') is None, 'BEP root missing or has a parent')
require(set(node_by_id['bep'].get('related_ids', [])) == {'physics', 'mathematics', 'systems_control'}, 'root discipline links incomplete')
require(set(graph['dataset'].get('maturity_values', [])) == {'idea', 'ai_worked_out'}, 'unexpected maturity vocabulary')
require(graph['dataset'].get('maturity_ceiling') == 'ai_worked_out', 'maturity ceiling is not AI-worked-out')
require(graph['dataset'].get('human_understanding') == 'not_asserted', 'human understanding was asserted')
require(graph['dataset'].get('human_source_verification') == 'not_asserted', 'human source verification was asserted')
require(all(n.get('maturity') in {'idea', 'ai_worked_out'} for n in nodes), 'a node exceeds allowed AI maturity')
require(not any(s.get('human_verified') is True for s in source_rows), 'source marked human verified')
allowed_claim_classes = set(graph['dataset'].get('scientific_claim_classes', []))
require(bool(allowed_claim_classes), 'scientific claim-class vocabulary is empty')
require(all(s.get('access_status') for s in source_rows), 'a source record has no access status')

# Validate a rooted, connected, acyclic hierarchy and node evidence references.
for node in nodes:
    parent = node.get('parent')
    if parent is not None:
        require(parent in node_by_id, f"missing parent {node['id']} -> {parent}")
    require(bool(node.get('summary')) and bool(node.get('explanation')), f"missing explanation on {node['id']}")
    require(node.get('open_questions') is not None, f"missing open_questions field on {node['id']}")
    for related in node.get('related_ids', []):
        require(related in node_by_id, f"missing related node {node['id']} -> {related}")
    for ref in node.get('claim_refs', []):
        require(ref.get('source_id') in sources, f"missing claim source on {node['id']}: {ref.get('source_id')}")
        require(all(ref.get(k) for k in ('locator', 'supports', 'evidence_type')), f"incomplete claim reference on {node['id']}")
        require(ref.get('evidence_type') in allowed_claim_classes, f"unknown evidence class on {node['id']}: {ref.get('evidence_type')}")
    for ref in node.get('source_map_refs', []):
        require(bool(ref.get('dataset')) and bool(ref.get('source_node_id')), f"incomplete lineage reference on {node['id']}")
    seen = set()
    current = node
    while current.get('parent') is not None:
        require(current['id'] not in seen, f"parent cycle at {node['id']}")
        seen.add(current['id'])
        current = node_by_id.get(current['parent'], {})
        if not current:
            break
    require(current.get('id') == 'bep', f"node not connected to root: {node['id']}")

# Every source snapshot concept and crosswalk target must have an integrated disposition.
require(len(concepts) == 171, 'concept disposition count differs from expected snapshots')
concept_keys = {(row['source_dataset'], row['source_node_id']) for row in concepts}
require(len(concept_keys) == len(concepts), 'duplicate concept disposition keys')
expected_counts = {'independent_v2': 79, 'original_devcontainer_canonical': 4, 'original_devcontainer_overlay': 69, 'proposed_unified_map': 19}
require(dict(Counter(row['source_dataset'] for row in concepts)) == expected_counts, 'concept snapshot coverage counts differ')
for row in concepts:
    require(bool(row.get('integrated_node_ids')), f"concept has no target: {row['source_dataset']}:{row['source_node_id']}")
    for target in row.get('integrated_node_ids', []):
        require(target in node_by_id, f"missing concept target {row['source_node_id']} -> {target}")
require(len(crosswalk) == 144, 'prior reconciliation crosswalk row count differs')
require(len({(r['dataset'], r['source_node_id']) for r in crosswalk}) == len(crosswalk), 'duplicate prior crosswalk keys')
for row in crosswalk:
    require(all(target in node_by_id for target in row.get('integrated_node_ids', [])), f"missing crosswalk target for {row['source_node_id']}")

# Verify historical source attachments and independent source-record lineage.
require(len(attachments) == 96, 'historical attachment count differs')
require(len({row['attachment_id'] for row in attachments}) == len(attachments), 'duplicate attachment IDs')
for row in attachments:
    require(row.get('resolved_source_id') in sources, f"unresolved historical source {row.get('resolved_source_id')}")
require(provenance.get('independent_source_record_count') == 28, 'independent source count differs')
independent_lineage = provenance.get('independent_source_record_lineage', [])
require(len(independent_lineage) == 28, 'independent source lineage incomplete')
for row in independent_lineage:
    require(all(sid in sources for sid in row.get('integrated_source_ids', [])), f"missing source lineage target for {row['source_id']}")
require(any(row.get('bibliographic_metadata_source_id') == 'berger_wrong_doi_metadata' and row.get('corrected_catalysis_source_id') == 'berger2008' for row in attachments), 'Berger DOI correction lineage missing')
require(len({row.get('resolved_source_id') for row in research_additions}) == len(research_additions), 'duplicate research-addition provenance IDs')
for row in research_additions:
    require(row.get('resolved_source_id') in sources, f"unresolved research-addition source {row.get('resolved_source_id')}")

# Cross-disciplinary edges identify their real discipline scope and carry valid endpoint source context.
def branch(node_id):
    current = node_by_id[node_id]
    while current.get('parent') and current['parent'] != 'bep':
        current = node_by_id[current['parent']]
    return current['id']
require(len(links) == link_doc['dataset'].get('edge_count') and len({edge['id'] for edge in links}) == len(links), 'scientific relation edge count/IDs invalid')
require(sum(edge.get('relationship_scope') == 'cross_disciplinary' for edge in links) == link_doc['dataset'].get('cross_disciplinary_edge_count'), 'cross-disciplinary edge count differs')
for edge in links:
    require(edge.get('from') in node_by_id and edge.get('to') in node_by_id, f"missing edge endpoint {edge['id']}")
    if edge.get('from') in node_by_id and edge.get('to') in node_by_id:
        expected = 'cross_disciplinary' if branch(edge['from']) != branch(edge['to']) else 'within_discipline_scientific_relation'
        require(edge.get('relationship_scope') == expected, f"incorrect edge scope {edge['id']}")
    for context in edge.get('endpoint_source_context', []):
        require(context.get('node_id') in node_by_id, f"bad evidence context endpoint {edge['id']}")
        require(all(sid in sources for sid in context.get('source_ids', [])), f"bad evidence context source {edge['id']}")

require(len(claim_recs) == claim_rec_doc['dataset'].get('count') and len({r['id'] for r in claim_recs}) == len(claim_recs), 'claim reconciliation records invalid')
for record in claim_recs:
    require(all(sid in sources for sid in record.get('source_ids', [])), f"missing reconciliation source {record['id']}")
require(len(uncertainties) == uncertainty_doc['dataset'].get('count') and len({r['id'] for r in uncertainties}) == len(uncertainties), 'uncertainty records invalid')
for record in uncertainties:
    require(all(nid in node_by_id for nid in record.get('linked_nodes', [])), f"missing uncertainty node link {record['id']}")
for record in coverage:
    require(all(nid in node_by_id for nid in record.get('node_ids', [])), f"missing coverage node in {record['id']}")

# Second-pass audit records must point to real sources/nodes/edges and use declared evidence classes.
require(audit_doc['dataset'].get('entry_count') == len(audit_entries), 'evidence-audit entry count differs')
require(len({r['id'] for r in audit_entries}) == len(audit_entries), 'duplicate evidence-audit IDs')
require(audit_doc['dataset'].get('reviewer_class') == 'same_agent_second_pass; no independent human review claimed', 'evidence-audit reviewer scope is overstated')
for record in audit_entries:
    require(all(sid in sources for sid in record.get('source_ids', [])), f"missing evidence-audit source {record['id']}")
    require(all(nid in node_by_id for nid in record.get('node_ids', [])), f"missing evidence-audit node {record['id']}")
    for edge_id in record.get('edge_ids', []):
        require(edge_id in {edge['id'] for edge in links}, f"missing evidence-audit edge {record['id']} -> {edge_id}")
    for claim in record.get('checked_claims', []):
        require(all(claim.get(k) for k in ('locator', 'claim', 'outcome', 'evidence_class')), f"incomplete evidence-audit claim in {record['id']}")
        require(claim.get('evidence_class') in allowed_claim_classes, f"unknown evidence class in audit {record['id']}")

report = {
    'status': 'passed' if not errors else 'failed',
    'validated_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'validation_scope': 'YAML structure, graph integrity, evidence references, provenance lineage, crosswalk, relation edges, uncertainty links and second-pass audit references; not scientific truth or model validation.',
    'counts': {
        'nodes': len(nodes), 'unique_node_ids': len(node_by_id),
        'sources': len(source_rows), 'unique_source_ids': len(sources),
        'claim_references': sum(len(n.get('claim_refs', [])) for n in nodes),
        'historical_attachments': len(attachments), 'concept_records': len(concepts),
        'research_addition_source_records': len(research_additions),
        'prior_crosswalk_rows': len(crosswalk), 'scientific_relation_edges': len(links),
        'cross_disciplinary_edges': sum(e.get('relationship_scope') == 'cross_disciplinary' for e in links),
        'claim_reconciliations': len(claim_recs), 'uncertainties': len(uncertainties),
        'coverage_areas': len(coverage), 'second_pass_evidence_audit_entries': len(audit_entries),
    },
    'maturity_counts': dict(Counter(n['maturity'] for n in nodes)),
    'source_access_status_counts': dict(Counter(s.get('access_status') for s in source_rows)),
    'concept_dispositions': dict(Counter(row['disposition'] for row in concepts)),
    'errors': errors,
}
RESULT_PATH = ROOT / 'validation_results.json'
RESULT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(report, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
