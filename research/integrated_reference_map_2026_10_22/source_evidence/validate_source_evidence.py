#!/usr/bin/env python3
"""Validate citation provenance against the integrated graph and accessible source PDFs."""
from __future__ import annotations
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re
import subprocess
import unicodedata
import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "source_evidence"


def load(rel: str):
    return yaml.safe_load((ROOT / rel).read_text(encoding="utf-8"))


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).replace("\u00ad", "")
    s = re.sub(r"[-\u2010\u2011]\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def main() -> int:
    errors: list[str] = []
    nodes = load("nodes.yaml")["nodes"]
    sources = load("sources.yaml")["sources"]
    source_ids = {s["id"] for s in sources}
    node_by_id = {n["id"]: n for n in nodes}
    register = load("source_evidence/claim_passage_register.yaml")
    passage_doc = load("source_evidence/passage_records.yaml")
    history_doc = load("source_evidence/historical_attachment_queue.yaml")
    provenance = load("source_provenance.yaml")
    coverage = load("source_evidence/coverage_ledger.yaml")
    review = load("source_evidence/source_review_ledger.yaml")
    batches = load("source_evidence/research_batches.yaml")
    corrections = load("source_evidence/correction_ledger.yaml")
    second = load("source_evidence/second_pass_audit.yaml")

    claims = register["claim_source_links"]
    passages = passage_doc["passages"]
    historical = history_doc["attachments"]
    claim_ids = [x["claim_id"] for x in claims]
    passage_ids = [x["passage_id"] for x in passages]
    historical_ids = [x["attachment_id"] for x in historical]
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("duplicate claim_id in claim_passage_register")
    if len(passage_ids) != len(set(passage_ids)):
        errors.append("duplicate passage_id in passage_records")
    if len(historical_ids) != len(set(historical_ids)):
        errors.append("duplicate attachment_id in historical queue")

    expected = {}
    for node in nodes:
        for ordinal, ref in enumerate(node.get("claim_refs") or [], 1):
            cid = f"CLM-{node['id']}-{ordinal:03d}"
            expected[cid] = (node["id"], ref)
    actual = {x["claim_id"]: x for x in claims}
    if set(expected) != set(actual):
        errors.append(f"claim inventory mismatch: graph={len(expected)} register={len(actual)} missing={len(set(expected)-set(actual))} extra={len(set(actual)-set(expected))}")
    for cid, (nid, ref) in expected.items():
        record = actual.get(cid)
        if not record:
            continue
        if record.get("node_id") != nid or record.get("source_id") != ref.get("source_id"):
            errors.append(f"{cid}: node/source id differs from graph claim_ref")
        if record.get("claim_statement") != ref.get("supports", ""):
            errors.append(f"{cid}: claim statement differs from graph claim_ref")
        if record.get("source_id") not in source_ids:
            errors.append(f"{cid}: unknown source_id {record.get('source_id')}")
        for pid in record.get("passage_ids", []):
            if pid not in set(passage_ids):
                errors.append(f"{cid}: missing passage_id {pid}")
        for did in record.get("derivation_ids", []):
            derivation_ids = {d["derivation_id"] for d in load("source_evidence/derivation_records.yaml").get("derivations", [])} if (ROOT / "source_evidence/derivation_records.yaml").exists() else set()
            if did not in derivation_ids:
                errors.append(f"{cid}: missing derivation_id {did}")
        if record.get("human_verification_status") != "not_verified":
            errors.append(f"{cid}: human status is not not_verified")
        stage = record.get("ai_evidence_check_stage")
        if record.get("passage_ids") and stage not in {"passage_checked", "disputed", "partially_supported", "unsupported", "unverifiable"}:
            errors.append(f"{cid}: passage attached but AI evidence stage is {stage}")
        if not record.get("passage_ids") and stage == "passage_checked":
            errors.append(f"{cid}: passage_checked without passage")

    expected_hist = {x["attachment_id"] for x in provenance.get("original_overlay_attachment_records", [])}
    if expected_hist != set(historical_ids):
        errors.append(f"historical attachment inventory mismatch: source={len(expected_hist)} queue={len(historical_ids)}")
    for x in historical:
        if x.get("human_verification_status") != "not_verified":
            errors.append(f"{x['attachment_id']}: historical attachment has human status other than not_verified")
        if x.get("resolved_source_id") and x["resolved_source_id"] not in source_ids:
            errors.append(f"{x['attachment_id']}: unknown resolved source")
        for pid in x.get("passage_ids", []):
            if pid not in set(passage_ids):
                errors.append(f"{x['attachment_id']}: missing passage {pid}")

    passages_by_id = {x["passage_id"]: x for x in passages}
    linked_claims = Counter()
    quote_checks = 0
    for p in passages:
        if p.get("source_id") not in source_ids:
            errors.append(f"{p['passage_id']}: unknown graph source_id {p.get('source_id')}")
        if not p.get("locator"):
            errors.append(f"{p['passage_id']}: missing precise locator")
        if p.get("human_verification_status") != "not_verified":
            errors.append(f"{p['passage_id']}: human verification status changed")
        for cid in p.get("claim_ids_checked", []):
            linked_claims[cid] += 1
            record = actual.get(cid)
            if not record or p["passage_id"] not in record.get("passage_ids", []):
                errors.append(f"{p['passage_id']}: claim link is not reciprocal for {cid}")
        if p.get("archive_path"):
            archive_path = Path(p["archive_path"])
            if not archive_path.exists():
                errors.append(f"{p['passage_id']}: source archive missing: {p['archive_path']}")
            elif sha256(archive_path.read_bytes()).hexdigest() != p.get("archive_sha256"):
                errors.append(f"{p['passage_id']}: archive SHA-256 mismatch")
        if p.get("evidence_kind") == "verbatim_quote":
            quote = p.get("quotation", "")
            if not quote or len(quote.split()) > 30:
                errors.append(f"{p['passage_id']}: missing or non-brief quotation")
            pdf = p.get("pdf_path")
            page = p.get("pdf_page")
            if pdf and page:
                pdf_path = Path(pdf)
                if not pdf_path.exists():
                    errors.append(f"{p['passage_id']}: source PDF missing: {pdf}")
                else:
                    digest = sha256(pdf_path.read_bytes()).hexdigest()
                    if digest != p.get("source_sha256"):
                        errors.append(f"{p['passage_id']}: PDF SHA-256 mismatch")
                    result = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-raw", str(pdf_path), "-"], capture_output=True, text=True)
                    if result.returncode:
                        errors.append(f"{p['passage_id']}: pdftotext failed: {result.stderr.strip()}")
                    elif norm(quote) not in norm(result.stdout):
                        errors.append(f"{p['passage_id']}: quotation is not present on PDF page {page} after whitespace/hyphen normalization")
                    else:
                        quote_checks += 1
            else:
                excerpt = p.get("captured_source_text", "")
                if not excerpt or norm(quote) not in norm(excerpt):
                    errors.append(f"{p['passage_id']}: quotation is not contained in captured source text")
                else:
                    quote_checks += 1
        elif p.get("evidence_kind") not in {"equation_or_table_transcription", "structured_data_extraction", "derivation"}:
            errors.append(f"{p['passage_id']}: invalid evidence_kind")

    for c in claims:
        for pid in c.get("passage_ids", []):
            p = passages_by_id.get(pid)
            if p and c["claim_id"] not in p.get("claim_ids_checked", []):
                errors.append(f"{c['claim_id']}: passage {pid} is not reciprocally linked")

    passage_result_ids = []
    corrected_passage_results = 0
    correction_ids = {x.get("correction_id") for x in corrections.get("corrections", [])}
    valid_audit_outcomes = {"confirmed", "corrected", "unresolved"}
    for audit in second.get("entries", []):
        if audit.get("human_verification_status") != "not_verified":
            errors.append(f"{audit.get('audit_id')}: second-pass human status is not not_verified")
        seen_in_audit = set()
        for result in audit.get("passage_results", []):
            pid = result.get("passage_id")
            if pid not in passages_by_id:
                errors.append(f"{audit.get('audit_id')}: second pass references missing passage {pid}")
            if pid in seen_in_audit:
                errors.append(f"{audit.get('audit_id')}: duplicate passage result {pid}")
            seen_in_audit.add(pid)
            passage_result_ids.append(pid)
            outcome = result.get("outcome")
            if outcome not in valid_audit_outcomes:
                errors.append(f"{audit.get('audit_id')}: invalid second-pass outcome {outcome} for {pid}")
            if outcome == "corrected":
                corrected_passage_results += 1
                if result.get("correction_id") not in correction_ids:
                    errors.append(f"{audit.get('audit_id')}: corrected passage {pid} lacks a correction-ledger record")
        for claim_result in audit.get("claim_links_reaudited", []):
            if claim_result.get("claim_id") not in actual:
                errors.append(f"{audit.get('audit_id')}: second pass references missing claim {claim_result.get('claim_id')}")
        declared_count = audit.get("counts", {}).get("passage_records_rechecked")
        if declared_count is not None and declared_count != len(seen_in_audit):
            errors.append(f"{audit.get('audit_id')}: declared passage recheck count {declared_count} differs from {len(seen_in_audit)} results")

    linked_source_ids = {x.get("source_id") for x in claims}
    if len(review.get("sources", [])) != len(sources):
        errors.append("source review ledger does not have one row per source record")
    if {x.get("source_id") for x in review.get("sources", [])} != source_ids:
        errors.append("source review ledger source ids differ from sources.yaml")
    if len(coverage.get("by_source", [])) != len(sources) or {x.get("source_id") for x in coverage.get("by_source", [])} != source_ids:
        errors.append("coverage ledger source rows differ from sources.yaml")
    for src in review.get("sources", []):
        if src.get("human_review_status") != "not_verified":
            errors.append(f"{src.get('source_id')}: source ledger human review status changed")

    counts = {
      "nodes": len(nodes), "source_records": len(sources), "current_claim_source_links": len(claims),
      "historical_attachments": len(historical), "passage_records": len(passages),
      "verbatim_quote_records": sum(p.get("evidence_kind") == "verbatim_quote" for p in passages),
      "verbatim_quotes_checked_against_pdf_or_capture": quote_checks,
      "claim_links_with_passage": sum(bool(c.get("passage_ids")) for c in claims),
      "claim_links_with_derivation": sum(bool(c.get("derivation_ids")) for c in claims),
      "claim_links_ai_rechecked": sum(c.get("ai_evidence_check_stage") in {"passage_checked", "disputed", "partially_supported", "unsupported", "unverifiable"} for c in claims),
      "claim_links_no_passage_yet": sum(not c.get("passage_ids") and not c.get("derivation_ids") for c in claims),
      "historical_attachments_with_passages": sum(bool(x.get("passage_ids")) for x in historical),
      "sources_reopened_this_mission": sum(x.get("access_level_reopened_this_mission") not in {None, "not_reopened"} for x in review.get("sources", [])),
      "ai_revised_or_disputed_claim_links": sum(c.get("ai_evidence_check_stage") in {"disputed", "unsupported"} for c in claims),
      "ai_partially_supported_claim_links": sum(c.get("ai_evidence_check_stage") == "partially_supported" for c in claims),
      "human_verified_claim_links": sum(c.get("human_verification_status") != "not_verified" for c in claims),
      "research_batches": len(batches.get("batches", [])), "correction_records": len(corrections.get("corrections", [])),
      "second_pass_entries": len(second.get("entries", [])),
      "passage_results_in_second_pass": len(passage_result_ids),
      "corrected_passage_results_in_second_pass": corrected_passage_results,
    }
    result = {"status": "passed" if not errors else "failed", "validation_scope": "Graph-to-claim inventory, source lineage, passage/claim reciprocity, exact quote/page checks where accessible, human-status separation, historical queue and coverage rows. A pass does not establish scientific truth or owner understanding.", "counts": counts, "errors": errors}
    out = EVIDENCE / "validation_results.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not errors else 1

if __name__ == "__main__":
    raise SystemExit(main())
