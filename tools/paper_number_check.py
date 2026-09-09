#!/usr/bin/env python3
"""Practical pre-submission paper sanity check; not a mathematical proof."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
BAD=['TODO','PLACEHOLDER','待补充','待填写','MISSING_EVIDENCE']
def main():
 ap=argparse.ArgumentParser(description='检查论文入口、占位符、图表引用和证据表'); ap.add_argument('project',type=Path); a=ap.parse_args(); r=a.project.resolve(); findings=[]
 paper=r/'论文/论文.tex'
 if not paper.exists(): print('BLOCKED missing 论文/论文.tex'); return 2
 t=paper.read_text(encoding='utf-8',errors='ignore')
 for x in BAD:
  if x in t: findings.append({'level':'P1','type':'placeholder','value':x})
 fig_contract=r/'图表契约.md'
 if not fig_contract.exists(): findings.append({'level':'P1','type':'figure_contract_missing'})
 evidence=r/'主张—证据表.md'
 if not evidence.exists(): findings.append({'level':'P1','type':'evidence_table_missing'})
 figures={int(x) for x in re.findall(r'图\s*([0-9]+)',t)}
 tables={int(x) for x in re.findall(r'表\s*([0-9]+)',t)}
 for n in sorted(figures):
  if not any(p.exists() and str(n) in p.stem for p in (r/'图表').rglob('*') if p.is_file()): findings.append({'level':'P2','type':'figure_reference_unresolved','number':n})
 report={'status':'PASS' if not findings else 'REVIEW','paper':str(paper),'figure_refs':sorted(figures),'table_refs':sorted(tables),'findings':findings}
 print(json.dumps(report,ensure_ascii=False,indent=2)); return 0 if not findings else 1
if __name__=='__main__': raise SystemExit(main())
