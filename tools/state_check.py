#!/usr/bin/env python3
"""Essential project/state gate; read-only by default."""
from __future__ import annotations
import argparse,json
from pathlib import Path
REQ=['state','题目','数据','求解','结果','图表','论文','支撑材料']
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('project',type=Path); a=ap.parse_args(); r=a.project.resolve(); findings=[]
 for d in REQ:
  if not (r/d).is_dir(): findings.append({'level':'P0','type':'missing_dir','path':d})
 state=r/'state/decision_log.json'
 if not state.exists(): findings.append({'level':'P0','type':'missing_state'})
 else:
  try:
   d=json.loads(state.read_text(encoding='utf-8')); stage=d.get('current_stage'); print('current_stage=',stage)
   if not isinstance(stage,int) or not 0<=stage<=9: findings.append({'level':'P1','type':'invalid_stage','value':stage})
   comp=d.get('competition');
   if comp not in {'cumcm',None}: findings.append({'level':'P1','type':'competition_mismatch','value':comp})
   if d.get('compliance',{}).get('ruleset',{}).get('verified_at') in {None,'', 'unknown'}: findings.append({'level':'P1','type':'rules_not_verified'})
   if d.get('problem_meta',{}).get('team_size') not in {3,None}: findings.append({'level':'P1','type':'team_size_unexpected'})
  except Exception as e: findings.append({'level':'P0','type':'invalid_state','error':str(e)})
 status='BLOCKED' if any(x['level']=='P0' for x in findings) else ('REVIEW' if findings else 'PASS')
 print(json.dumps({'status':status,'project':str(r),'findings':findings},ensure_ascii=False,indent=2)); return 1 if status=='BLOCKED' else 0
if __name__=='__main__': raise SystemExit(main())
