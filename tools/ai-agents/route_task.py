#!/usr/bin/env python3
"""Create a bounded Agent handoff task JSON; does not launch an Agent."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('project',type=Path); ap.add_argument('--agent',required=True); ap.add_argument('--stage',required=True); ap.add_argument('--task',required=True); ap.add_argument('--read',action='append',default=[]); ap.add_argument('--write',action='append',default=[]); ap.add_argument('--forbid',action='append',default=[]); a=ap.parse_args(); root=a.project.resolve()
    payload={'agent':a.agent,'stage':a.stage,'task':a.task,'project_root':str(root),'allowed_read':a.read,'allowed_write':a.write,'forbidden':a.forbid,'return_format':['scope','evidence','commands_and_exit_status','outputs','unknowns','P0-P2_risks','human_confirmation']}
    out=root/'state'/'agent_tasks'; out.mkdir(parents=True,exist_ok=True); path=out/f"{a.stage}_{a.agent}.json"; path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print('written=',path); return 0
if __name__=='__main__': raise SystemExit(main())
