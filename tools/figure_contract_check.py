#!/usr/bin/env python3
"""Check required fields and referenced files in 图表契约.md."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('project',type=Path); a=ap.parse_args(); r=a.project.resolve(); p=r/'图表契约.md'; findings=[]
 if not p.exists(): print('BLOCKED missing 图表契约.md'); return 2
 for no,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
  if not line.startswith('|') or line.startswith('|---') or '主张' in line: continue
  c=[x.strip() for x in line.strip('|').split('|')]
  if len(c)<10: continue
  if not c[1]: findings.append({'level':'P1','line':no,'type':'claim_empty'})
  if not c[2]: findings.append({'level':'P1','line':no,'type':'source_empty'})
  if c[8].upper()=='APPROVED' and not c[9]: findings.append({'level':'P1','line':no,'type':'approved_without_reviewer'})
  for cell in c[2:5]:
   for token in re.findall(r'`([^`]+)`',cell):
    if not (r/token).exists(): findings.append({'level':'P1','line':no,'type':'missing_path','path':token})
 status='PASS' if not findings else 'REVIEW'; print(json.dumps({'status':status,'findings':findings},ensure_ascii=False,indent=2)); return 0 if status=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
