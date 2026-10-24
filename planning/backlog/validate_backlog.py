#!/usr/bin/env python3
"""Validate occurrence, source-coverage, and cluster traceability."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
BACKLOG = ROOT / 'planning' / 'backlog'
WORKSTREAMS = {
    'supervision', 'notebooks_and_model_ownership', 'model_numerics',
    'chemistry_and_literature', 'scientific_verification',
    'personal_understanding_map', 'ai_reference_and_provenance',
    'mindmap_frontend', 'presentation_and_thesis',
    'administration_and_committee', 'project_coordination',
    'other_needs_review',
}

def fail(msg: str) -> None:
    print(f'FAIL: {msg}', file=sys.stderr)
    raise SystemExit(1)

source_doc=json.loads((BACKLOG/'SOURCE_COVERAGE.json').read_text(encoding='utf-8'))
sources=source_doc['sources']
source_index={
    (s['source_repository'],s['source_path'],s['source_ref'],s['source_sha'],s['source_content_sha256']):s
    for s in sources
}
if len(source_index)!=len(sources): fail('duplicate source identity rows in SOURCE_COVERAGE.json')
if source_doc.get('source_count')!=len(sources): fail('source_count does not match sources list')

occurrences=[]
with (BACKLOG/'raw_occurrences.jsonl').open(encoding='utf-8') as f:
    for line_no,line in enumerate(f,1):
        try: occurrences.append(json.loads(line))
        except Exception as e: fail(f'raw_occurrences.jsonl line {line_no} is invalid JSON: {e}')
occ_by_id={x.get('occurrence_id'):x for x in occurrences}
if None in occ_by_id or len(occ_by_id)!=len(occurrences): fail('missing or colliding occurrence IDs')

source_occ_counts=Counter()
for x in occurrences:
    for field in ('occurrence_id','original_text','source_repository','source_path','source_ref','source_content_sha256','heading_section','line_start','line_end','item_kind','original_status','extraction_method','extraction_confidence','cluster_id'):
        if field not in x or x[field] in (None,''):
            # Sources without Git refs are represented by an external identity string in source_ref.
            fail(f'{x.get("occurrence_id")} missing required field {field}')
    if not isinstance(x['line_start'],int) or not isinstance(x['line_end'],int) or x['line_start']<1 or x['line_end']<x['line_start']:
        fail(f'{x["occurrence_id"]} has invalid line range')
    if not isinstance(x['original_text'],str) or not x['original_text'].strip(): fail(f'{x["occurrence_id"]} has empty original text')
    if not x.get('source_sha') and not x.get('source_content_sha256'):
        fail(f'{x["occurrence_id"]} lacks a Git SHA and source content digest')
    key=(x['source_repository'],x['source_path'],x['source_ref'],x.get('source_sha'),x['source_content_sha256'])
    if key not in source_index: fail(f'{x["occurrence_id"]} source is absent from coverage')
    source_occ_counts[key]+=1
    if not x.get('workstreams') or not set(x['workstreams']).issubset(WORKSTREAMS): fail(f'{x["occurrence_id"]} has unknown workstream tags')

for x in occurrences:
    parent=x.get('parent_occurrence_id')
    if parent:
        if parent not in occ_by_id: fail(f'{x["occurrence_id"]} has missing parent {parent}')
        p=occ_by_id[parent]
        if (p['source_repository'],p['source_path'],p['source_ref'])!=(x['source_repository'],x['source_path'],x['source_ref']):
            fail(f'{x["occurrence_id"]} parent is from another source version')

cluster_doc=json.loads((BACKLOG/'task_clusters.json').read_text(encoding='utf-8'))
clusters=cluster_doc.get('clusters',[])
cluster_by_id={c.get('cluster_id'):c for c in clusters}
if len(cluster_by_id)!=len(clusters): fail('duplicate cluster IDs')
if cluster_doc.get('cluster_count')!=len(clusters): fail('cluster_count does not match clusters list')
assignment=Counter()
for c in clusters:
    if not c.get('occurrence_ids'): fail(f'{c.get("cluster_id")} has no occurrence IDs')
    for oid in c['occurrence_ids']:
        assignment[oid]+=1
        if oid not in occ_by_id: fail(f'{c["cluster_id"]} references missing occurrence {oid}')
        if occ_by_id[oid].get('cluster_id')!=c['cluster_id']: fail(f'{oid} cluster ID disagrees with cluster index')
    for e in c.get('status_evidence',[]):
        if e.get('occurrence_id') not in c['occurrence_ids']: fail(f'{c["cluster_id"]} has unlinked status evidence')
orphans=[oid for oid in occ_by_id if assignment[oid]!=1]
if orphans: fail(f'{len(orphans)} occurrences are unclustered or multiply assigned; first: {orphans[:5]}')

for s in sources:
    if not s.get('examined_entire_source'): fail(f'source not marked fully examined: {s.get("source_path")}')
    key=(s['source_repository'],s['source_path'],s['source_ref'],s.get('source_sha'),s['source_content_sha256'])
    n=source_occ_counts[key]
    if n!=s.get('extracted_occurrence_count'): fail(f'extracted count mismatch for {s["source_path"]}: {s.get("extracted_occurrence_count")} vs {n}')

manifest=json.loads((ROOT/'planning'/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
covered_imports={s.get('imported_path') for s in sources if s.get('source_kind')=='archive_snapshot'}
expected_imports={f['new_path'] for f in manifest['files']}
if covered_imports!=expected_imports: fail(f'archive coverage differs from manifest: missing={sorted(expected_imports-covered_imports)[:5]} extra={sorted(covered_imports-expected_imports)[:5]}')
if len(expected_imports)!=119: fail(f'expected 119 archive imports, found {len(expected_imports)}')

print(json.dumps({
    'result':'PASS',
    'sources':len(sources),
    'archive_snapshots':len(expected_imports),
    'occurrences':len(occurrences),
    'clusters':len(clusters),
    'one_to_one_occurrence_cluster_mapping':True,
    'source_traceability':True,
    'zero_action_sources':sum(s.get('extracted_occurrence_count')==0 for s in sources),
},indent=2))
