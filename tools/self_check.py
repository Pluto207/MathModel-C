#!/usr/bin/env python3
"""Read-only self-check for the 数模C Skill package."""
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
REQUIRED=['SKILL.md','README.md','使用指南.md','融合设计说明.md','tools/c.py','tools/init_project.py','tools/state_check.py','tools/evidence_check.py','tools/version_check.py','tools/figure_contract_check.py','tools/paper_number_check.py','模板/模型合同.md','模板/主张—证据表.md','模板/图表契约.md','模板/复现清单.json','模板/AI使用台账.json','references/compliance/CUMCM终审清单.md']
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--json',action='store_true'); a=ap.parse_args(); findings=[]
 for x in REQUIRED:
  if not (ROOT/x).is_file(): findings.append({'level':'P0','type':'missing_file','path':x})
 for p in ROOT.rglob('*.json'):
  try: json.loads(p.read_text(encoding='utf-8'))
  except Exception as e: findings.append({'level':'P0','type':'invalid_json','path':str(p.relative_to(ROOT)),'error':str(e)})
 py=list(ROOT.rglob('*.py'))
 r=subprocess.run([sys.executable,'-m','py_compile',*map(str,py)],capture_output=True,text=True)
 if r.returncode: findings.append({'level':'P0','type':'python_compile','error':r.stderr[-2000:]})
 result={'status':'PASS' if not findings else 'FAIL','files':sum(p.is_file() for p in ROOT.rglob('*')),'findings':findings}
 print(json.dumps(result,ensure_ascii=False,indent=2) if a.json else f"status={result['status']} files={result['files']} findings={len(findings)}")
 return 0 if not findings else 1
if __name__=='__main__': raise SystemExit(main())
