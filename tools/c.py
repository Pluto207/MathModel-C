#!/usr/bin/env python3
"""Unified practical CLI for essential 数模C checks."""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; TOOLS=ROOT/'tools'
def run(script,args): return subprocess.call([sys.executable,str(TOOLS/script),*map(str,args)])
def main():
 ap=argparse.ArgumentParser(prog='c.py'); sub=ap.add_subparsers(dest='cmd',required=True)
 s=sub.add_parser('init'); s.add_argument('project',type=Path); s.add_argument('--questions',type=int,default=4)
 for n in ['check','evidence','figure','paper','bind']:
  s=sub.add_parser(n); s.add_argument('project',type=Path)
 s=sub.add_parser('version'); s.add_argument('project',type=Path); s.add_argument('--apply',action='store_true')
 s=sub.add_parser('ai-report'); s.add_argument('project',type=Path); s.add_argument('--pdf',action='store_true')
 for n,script in [('ai-record','ai-agents/record_ai_use.py'),('route','ai-agents/route_task.py')]:
  s=sub.add_parser(n); s.add_argument('project',type=Path); s.add_argument('extra',nargs=argparse.REMAINDER); s.set_defaults(_script=script)
 s=sub.add_parser('latex-table'); s.add_argument('input',type=Path); s.add_argument('--out',type=Path,required=True); s.add_argument('extra',nargs=argparse.REMAINDER)
 s=sub.add_parser('self-check'); s.add_argument('--json',action='store_true')
 a=ap.parse_args()
 if a.cmd=='init': return run('init_project.py',[a.project,'--questions',a.questions])
 if a.cmd=='check': return max(run('project_check.py',[a.project]),run('state_check.py',[a.project]))
 if a.cmd=='evidence': return run('evidence_check.py',[a.project])
 if a.cmd=='figure': return run('figure_contract_check.py',[a.project])
 if a.cmd=='paper': return run('paper_number_check.py',[a.project])
 if a.cmd=='bind': return run('bind_evidence.py',[a.project])
 if a.cmd=='version': return run('version_check.py',[a.project]+(['--apply'] if a.apply else []))
 if a.cmd=='ai-report': return run('ai-agents/build_ai_report.py',[a.project]+(['--pdf'] if a.pdf else []))
 if a.cmd in ('ai-record','route'): return run(a._script,[a.project,*a.extra])
 if a.cmd=='latex-table': return run('matlab/result_to_latex.py',[a.input,'--out',a.out,*a.extra])
 if a.cmd=='self-check': return run('self_check.py',(['--json'] if a.json else []))
if __name__=='__main__': raise SystemExit(main())
