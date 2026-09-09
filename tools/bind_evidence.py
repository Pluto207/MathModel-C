#!/usr/bin/env python3
"""Bind result manifests to claim-evidence rows without changing claims."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path

def main()->int:
 ap=argparse.ArgumentParser(description='检查结果版本与主张—证据表绑定'); ap.add_argument('project',type=Path); ap.add_argument('--table',default='主张—证据表.md'); ap.add_argument('--out',default='结果/evidence_binding.json'); a=ap.parse_args(); root=a.project.resolve(); table=root/a.table
 report={'project':str(root),'status':'PASS','findings':[],'claims':0}
 if not table.exists(): report['status']='BLOCKED'; report['findings'].append({'level':'P0','type':'table_missing'}); return finish(root,a.out,report,2)
 manifests={}
 for p in (root/'结果').rglob('*_manifest.json'):
  try: manifests[str(p.relative_to(root))]=json.loads(p.read_text(encoding='utf-8'))
  except Exception as e: report['findings'].append({'level':'P1','type':'bad_manifest','path':str(p),'error':str(e)})
 for p in (root/'结果').rglob('*_manifest.txt'):
  d={}
  for line in p.read_text(encoding='utf-8',errors='ignore').splitlines():
   if '=' in line:
    k,v=line.split('=',1); d[k.strip()]=v.strip()
  if d: manifests[str(p.relative_to(root))]=d
 for no,line in enumerate(table.read_text(encoding='utf-8').splitlines(),1):
  if not line.startswith('|') or line.startswith('|---') or '论文主张' in line: continue
  c=[x.strip() for x in line.strip('|').split('|')]
  if len(c)<9: continue
  report['claims']+=1; cid=c[0] or f'line-{no}'; paths=re.findall(r'`([^`]+)`',c[4])
  if not paths: continue
  found=[]
  for token in paths:
   candidates=[k for k in manifests if token in k or Path(k).name==Path(token).name]
   if candidates: found += candidates
   elif not (root/token).exists(): report['findings'].append({'level':'P1','type':'result_missing','claim':cid,'path':token,'line':no})
  if c[7].upper()=='APPROVED' and not found: report['findings'].append({'level':'P1','type':'approved_without_result_manifest','claim':cid,'line':no})
 if report['findings']: report['status']='REVIEW'
 return finish(root,a.out,report,1 if report['status']!='PASS' else 0)

def finish(root,out,report,code):
 p=root/out; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(json.dumps(report,ensure_ascii=False,indent=2)); return code
if __name__=='__main__': raise SystemExit(main())
