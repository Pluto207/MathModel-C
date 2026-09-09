#!/usr/bin/env python3
"""Generate AI usage Markdown and, when a renderer exists, PDF."""
from __future__ import annotations
import argparse,json,shutil,subprocess,tempfile
from pathlib import Path

def make_md(data):
 lines=['# AI工具使用详情','',f"竞赛届次：{data.get('contest_year','未填写')}",'','> 由数模C根据队伍台账生成；最终内容和格式以当届官方规则为准。','']
 for i,e in enumerate(data.get('entries',[]),1):
  lines += [f"## {i}. {e.get('tool','未填写')} / {e.get('stage','未填写')}",f"- 日期：{e.get('date','未填写')}",f"- 模型/版本：{e.get('model_version','未填写')}",f"- 任务：{e.get('task_summary','未填写')}",f"- 是否采纳：{'是' if e.get('output_used') else '否'}",f"- 人工修改：{e.get('human_modification','未填写')}",f"- 验证：{e.get('verification','未填写')}",f"- 审核人：{'、'.join(e.get('reviewers',[])) or '未填写'}",f"- 状态：{e.get('status','DRAFT')}",'']
 return '\n'.join(lines)+'\n'

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('project',type=Path); ap.add_argument('--out',default='支撑材料/AI工具使用详情.md'); ap.add_argument('--pdf',action='store_true'); a=ap.parse_args(); root=a.project.resolve(); src=root/'AI使用台账.json'
 if not src.exists(): print('BLOCKED ledger_missing=',src); return 2
 md=make_md(json.loads(src.read_text(encoding='utf-8'))); out=root/a.out; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(md,encoding='utf-8'); print('written=',out)
 if not a.pdf: return 0
 pdf=out.with_suffix('.pdf');
 if shutil.which('pandoc'):
  r=subprocess.run(['pandoc',str(out),'-o',str(pdf)],cwd=root,check=False)
 elif shutil.which('wkhtmltopdf'):
  html=out.with_suffix('.html'); html.write_text('<meta charset="utf-8"><pre>'+md.replace('&','&amp;').replace('<','&lt;')+'</pre>',encoding='utf-8'); r=subprocess.run(['wkhtmltopdf',str(html),str(pdf)],cwd=root,check=False)
 else:
  print('PDF_BLOCKED no pandoc/wkhtmltopdf; Markdown retained at',out); return 3
 if r.returncode!=0 or not pdf.exists(): print('PDF_FAILED',pdf); return 1
 print('written=',pdf); return 0
if __name__=='__main__': raise SystemExit(main())
