#!/usr/bin/env python3
"""Convert a CSV or simple JSON result table to a LaTeX tabular fragment."""
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

def esc(x):
 s=str(x); return s.replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('$','\\$').replace('#','\\#').replace('_','\\_').replace('{','\\{').replace('}','\\}')
def main():
 ap=argparse.ArgumentParser(description='把MATLAB导出的CSV/JSON结果转为LaTeX表格片段'); ap.add_argument('input',type=Path); ap.add_argument('--out',type=Path,required=True); ap.add_argument('--caption',default='结果表'); ap.add_argument('--label',default='tab:result'); a=ap.parse_args()
 p=a.input; rows=[]
 if p.suffix.lower()=='.csv':
  with p.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.reader(f))
 elif p.suffix.lower()=='.json':
  d=json.loads(p.read_text(encoding='utf-8'))
  if isinstance(d,list):
   if d and isinstance(d[0],dict):
    keys=list(d[0]); rows=[keys]+[[x.get(k,'') for k in keys] for x in d]
   else: rows=d
  elif isinstance(d,dict):
   rows=[['字段','值']]+[[k,v] for k,v in d.items() if not isinstance(v,(dict,list))]
  else: rows=[]
 else: raise SystemExit('只支持 CSV 或 JSON')
 if not rows: raise SystemExit('输入为空')
 n=len(rows[0]); body=['\\begin{table}[htbp]','\\centering',f'\\caption{{{esc(a.caption)}}}',f'\\label{{{esc(a.label)}}}',f'\\begin{{tabular}}{{'+'c'*n+'}','\\hline']
 body += [' & '.join(esc(x) for x in r)+' \\\\ \\hline' for r in rows]
 body += ['\\end{tabular}','\\end{table}','']
 a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text('\n'.join(body),encoding='utf-8'); print('written=',a.out); return 0
if __name__=='__main__': raise SystemExit(main())
