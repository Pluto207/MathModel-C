#!/usr/bin/env python3
"""Append a redacted, human-readable AI usage entry to a project ledger."""
from __future__ import annotations
import argparse, json
from datetime import date
from pathlib import Path

def main()->int:
    ap=argparse.ArgumentParser(description='记录一次AI使用，不记录秘密或完整私聊')
    ap.add_argument('project',type=Path); ap.add_argument('--tool',required=True); ap.add_argument('--model',default='未填写'); ap.add_argument('--stage',required=True); ap.add_argument('--summary',required=True); ap.add_argument('--used',choices=['yes','no'],default='yes'); ap.add_argument('--verification',default='待填写'); ap.add_argument('--reviewer',action='append',default=[]); ap.add_argument('--status',choices=['DRAFT','REVIEWED','APPROVED'],default='DRAFT')
    a=ap.parse_args(); root=a.project.resolve(); p=root/'AI使用台账.json'
    data=json.loads(p.read_text(encoding='utf-8')) if p.exists() else {'schema_version':'1.0','contest_year':None,'entries':[]}
    data.setdefault('entries',[]).append({'date':date.today().isoformat(),'tool':a.tool,'model_version':a.model,'stage':a.stage,'task_summary':a.summary,'input_scope':'由队伍指定的项目文件','output_used':a.used=='yes','human_modification':'待填写','verification':a.verification,'reviewers':a.reviewer,'status':a.status})
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print('recorded=',p); return 0
if __name__=='__main__': raise SystemExit(main())
