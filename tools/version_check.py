#!/usr/bin/env python3
"""Detect changed result manifests and optionally demote affected APPROVED claims."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

def digest(p:Path)->str: return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(text):
 for no,line in enumerate(text.splitlines(),1):
  if line.startswith('|') and not line.startswith('|---') and '论文主张' not in line:
   c=[x.strip() for x in line.strip('|').split('|')]
   if len(c)>=9: yield no,c

def main():
 ap=argparse.ArgumentParser(description='检测结果/模型版本变化；--apply时将受影响主张退回REVIEW')
 ap.add_argument('project',type=Path); ap.add_argument('--table',default='主张—证据表.md'); ap.add_argument('--apply',action='store_true'); ap.add_argument('--out',default='结果/version_check.json'); a=ap.parse_args(); root=a.project.resolve(); table=root/a.table; snap=root/'结果/evidence_snapshot.json'
 report={'status':'PASS','apply':a.apply,'changed_manifests':[],'affected_claims':[],'findings':[]}
 if not table.exists(): report['status']='BLOCKED'; report['findings'].append({'level':'P0','type':'table_missing'}); return finish(root,a.out,report,2)
 current={str(p.relative_to(root)):digest(p) for p in (root/'结果').rglob('*_manifest.json') if p.is_file()}
 old=json.loads(snap.read_text(encoding='utf-8')) if snap.exists() else {}
 report['changed_manifests']=sorted(k for k,v in current.items() if old.get(k)!=v)
 text=table.read_text(encoding='utf-8'); lines=text.splitlines(); changed_ids=[]
 for no,c in rows(text):
  cid=c[0] or f'line-{no}'; status=c[7].upper(); tokens=re.findall(r'`([^`]+)`',c[4]); hit=any(any(t in k or Path(k).name==Path(t).name for k in report['changed_manifests']) for t in tokens)
  if hit and status=='APPROVED': report['affected_claims'].append(cid); changed_ids.append((no,cid))
 if report['changed_manifests'] or report['affected_claims']: report['status']='REVIEW'
 if a.apply and changed_ids:
  for no,cid in changed_ids:
   idx=no-1; c=[x.strip() for x in lines[idx].strip('|').split('|')]
   c[7]='REVIEW'; c[8]=(c[8]+'；版本变化自动回退 '+cid).strip('；')
   lines[idx]='| '+' | '.join(c)+' |'
  table.write_text('\n'.join(lines)+'\n',encoding='utf-8'); report['table_updated']=True
 else: report['table_updated']=False
 snap.parent.mkdir(parents=True,exist_ok=True); snap.write_text(json.dumps(current,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); report['snapshot_updated']=True
 return finish(root,a.out,report,1 if report['status']!='PASS' else 0)
def finish(root,out,report,code):
 p=root/out; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(json.dumps(report,ensure_ascii=False,indent=2)); return code
if __name__=='__main__': raise SystemExit(main())
