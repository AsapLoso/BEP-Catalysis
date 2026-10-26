#!/usr/bin/env python3
"""Reproduce scoped row/cell summaries from Dehghani et al. (2019) S1 workbooks."""
from __future__ import annotations
from decimal import Decimal
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile
import yaml
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[4]
ARCHIVE = REPO / "Academics/BEP/Catalysis/research/integrated_reference_map_2026_10_22/source_evidence/source_snapshots/dehghani2019_supplementary_data.zip"
OUT = ROOT / "source_evidence/dehghani_supplement_summary.yaml"


def workbook(z: ZipFile, name: str):
    return load_workbook(BytesIO(z.read(name)), data_only=True, read_only=False)


def main() -> None:
    digest = sha256(ARCHIVE.read_bytes()).hexdigest()
    result = {
      "resource_id": "AUX-dehghani2019-s1",
      "parent_source_id": "dehghani2019_pdag_alphaal2o3",
      "archive_path": str(ARCHIVE.relative_to(REPO)),
      "archive_bytes": ARCHIVE.stat().st_size,
      "archive_sha256": digest,
      "extraction_tool": "openpyxl 3.1.5",
      "scope": "Selected workbook row/column and arithmetic checks; not a reconstruction of the authors' run plan or plant-data correspondence.",
      "workbooks": []
    }
    with ZipFile(ARCHIVE) as z:
        n1="Supplementary Data Set 1/Supplementary Data Set 1.xlsx"
        wb=workbook(z,n1); ws=wb.worksheets[0]
        rows=list(ws.iter_rows(values_only=True)); header=list(rows[0])
        run_rows=[(i+1,row) for i,row in enumerate(rows) if row and isinstance(row[0],(int,float))]
        labels=[int(row[0]) for _,row in run_rows]
        ranges={}
        for j,h in enumerate(header):
            values=[row[j] for _,row in run_rows if j<len(row) and isinstance(row[j],(int,float))]
            if h is not None and values:
                ranges[str(h)]={"min":min(values),"max":max(values),"numeric_count":len(values)}
        result["workbooks"].append({
          "workbook_name":n1,"worksheet":ws.title,"sheet_max_row_including_formatting":ws.max_row,
          "header_row":1,"numeric_run_rows":{"first_excel_row":run_rows[0][0],"last_excel_row":run_rows[-1][0],"count":len(run_rows),"unique_count":len(set(labels),),"min_label":min(labels),"max_label":max(labels),"missing_integer_labels":[i for i in range(1,max(labels)+1) if i not in set(labels)]},
          "column_ranges":ranges,"cell_locator":"Sheet1!A1:V159 (numeric RUN data occupy rows 2–159)"
        })
        wb.close()
        n2="Supplementary Data Set 2/Supplementary Data Set 2.xlsx"
        wb=workbook(z,n2); ws=wb.worksheets[0]
        phase_rows=[]; date_rows=[]
        for r in range(1,ws.max_row+1):
            phase=ws.cell(r,1).value; day=ws.cell(r,2).value
            if phase in {"SOR","MOR","EOR"} and isinstance(day,(int,float)):
                phase_rows.append((r,phase,day))
            if isinstance(phase,str) and r>=70 and day is None:
                nonempty=[c for c in range(1,ws.max_column+1) if ws.cell(r,c).value is not None]
                if nonempty:
                    date_rows.append({"excel_row":r,"date_text_verbatim":phase,"day_cell":"B"+str(r),"nonempty_columns":[ws.cell(3,c).column_letter for c in nonempty],"last_nonempty_column":ws.cell(r,max(nonempty)).column_letter})
        phase_counts={p:sum(1 for _,q,_ in phase_rows if q==p) for p in ("SOR","MOR","EOR")}
        result["workbooks"].append({
          "workbook_name":n2,"worksheets":[{"title":s.title,"max_row":s.max_row,"max_column":s.max_column} for s in wb.worksheets],
          "phase_coded_numeric_day_rows":{"count":len(phase_rows),"counts_by_phase":phase_counts,"day_min":min(d for _,_,d in phase_rows),"day_max":max(d for _,_,d in phase_rows),"excel_row_min":min(r for r,_,_ in phase_rows),"excel_row_max":max(r for r,_,_ in phase_rows)},
          "date_text_rows_without_numeric_day":date_rows,"cell_locator":"Sheet1!A1:BR82; phase-coded time data in A4:B49; three date-text rows at A78:A80 have blank day cells B78:B80 and nonempty cells only through column R (no component-composition columns T:AT)."
        })
        wb.close()
        n3="Supplementary Data Set 3/Supplementary Data Set 3.xlsx"
        wb=workbook(z,n3); ws=wb.worksheets[0]
        categories=[{"row":r,"label":ws.cell(r,1).value.strip(),"percent":ws.cell(r,2).value,"cell":"B"+str(r)} for r in range(85,91)]
        total=sum((Decimal(str(x["percent"])) for x in categories),Decimal("0"))
        total_cell=ws.cell(91,2).value
        result["workbooks"].append({
          "workbook_name":n3,"worksheet":ws.title,"max_row":ws.max_row,"max_column":ws.max_column,
          "summary_categories":categories,"category_sum_decimal":str(total),"displayed_total_sum_cell":"B91","displayed_total_sum_value":total_cell,
          "difference_from_displayed_total":str(total-Decimal(str(total_cell))),"cell_locator":"Sheet1!A85:B91",
          "interpretation_limit":"The six displayed category values do not sum to the displayed Total Sum. No analytical method, overlap, cause or pathway assignment is inferred."
        })
        wb.close()
    OUT.write_text(yaml.safe_dump(result,sort_keys=False,allow_unicode=True,width=110),encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)}; SHA-256 {digest}; 3 workbooks summarized")

if __name__ == "__main__":
    main()
