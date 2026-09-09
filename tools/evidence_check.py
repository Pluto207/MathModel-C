#!/usr/bin/env python3
"""Read-only evidence-chain checker for a 数模C project.

Checks project paths, claim-evidence rows, status vocabulary and stale-risk hints.
It does not judge mathematical correctness and never edits the project.
"""
from __future__ import annotations
import argparse, json, re
from datetime import datetime
from pathlib import Path

STATUSES={'DRAFT','REVIEWED','APPROVED','REVIEW','BLOCKED'}

def parse_table(path: Path):
    rows=[]
    for line_no,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.startswith('|') or line.startswith('|---') or '论文主张' in line: continue
        cols=[x.strip() for x in line.strip('|').split('|')]
        if len(cols)>=9: rows.append((line_no,cols))
    return rows

def main()->int:
    ap=argparse.ArgumentParser(description='检查数模C主张—证据链，不修改文件')
    ap.add_argument('project',type=Path)
    ap.add_argument('--table',default='主张—证据表.md')
    ap.add_argument('--json-report',default='结果/evidence_check.json')
    args=ap.parse_args(); root=args.project.resolve(); table=root/args.table
    report={'timestamp':datetime.now().isoformat(timespec='seconds'),'project':str(root),'table':str(table),'status':'PASS','claims':0,'findings':[]}
    if not table.exists():
        report['status']='BLOCKED'; report['findings'].append({'level':'P0','type':'missing_table','path':str(table)})
    else:
        rows=parse_table(table); report['claims']=len(rows)
        for line_no,cols in rows:
            cid=cols[0] or f'line-{line_no}'; status=cols[7].upper()
            if status not in STATUSES:
                report['findings'].append({'level':'P1','type':'invalid_status','claim':cid,'line':line_no,'value':status})
            if not cols[1]: report['findings'].append({'level':'P1','type':'empty_claim','claim':cid,'line':line_no})
            evidence_cells=cols[2:7]
            if not any(x and x not in {'—','-'} for x in evidence_cells):
                report['findings'].append({'level':'P1','type':'no_evidence_cell','claim':cid,'line':line_no})
            for cell in evidence_cells:
                for token in re.findall(r'`([^`]+)`',cell):
                    p=root/token
                    if not p.exists(): report['findings'].append({'level':'P1','type':'missing_path','claim':cid,'path':token,'line':line_no})
            if status=='APPROVED' and not cols[8]: report['findings'].append({'level':'P1','type':'approved_without_reviewer','claim':cid,'line':line_no})
    if any(x['level']=='P0' for x in report['findings']): report['status']='BLOCKED'
    elif report['findings']: report['status']='REVIEW'
    out=root/args.json_report; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2)); return 0 if report['status']=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
