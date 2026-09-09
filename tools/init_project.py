#!/usr/bin/env python3
"""Initialize a standalone 数模C CUMCM project without touching A/B."""
from __future__ import annotations
import argparse, json, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / 'templates'
DIRS = ['state','题目','数据','求解','结果','图表','论文','支撑材料']

def copy_if_absent(src: Path, dst: Path) -> None:
    if not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

def init_paper(dst: Path) -> None:
    """Copy the CUMCM template and remove the template TOC by default."""
    src_dir = ROOT / 'templates' / 'cumcm' / '论文'
    if dst.exists() and any(dst.iterdir()): return
    shutil.copytree(src_dir, dst, dirs_exist_ok=True)
    main = dst / '论文.tex'
    if main.exists():
        text = main.read_text(encoding='utf-8')
        text = text.replace('\\tableofcontents\n\\thispagestyle{empty}\n\\newpage\n', '')
        main.write_text(text, encoding='utf-8')

def main() -> int:
    ap=argparse.ArgumentParser(description='初始化数模C CUMCM项目')
    ap.add_argument('project',type=Path); ap.add_argument('--questions',type=int,default=4)
    args=ap.parse_args(); root=args.project.resolve(); root.mkdir(parents=True,exist_ok=True)
    for d in DIRS: (root/d).mkdir(exist_ok=True)
    for q in range(1,args.questions+1):
        qd=root/'求解'/f'问题{q}'; qd.mkdir(exist_ok=True)
        src=ROOT/'matlab/templates/main_qX.m'; dst=qd/f'main_q{q}.m'
        if not dst.exists():
            text=src.read_text(encoding='utf-8').replace('main_qX',f'main_q{q}').replace('qX',f'q{q}').replace("cfg.problem = 'X';",f"cfg.problem = 'q{q}';")
            dst.write_text(text,encoding='utf-8')
        copy_if_absent(TEMPLATE/'模型合同.md',qd/'模型合同.md')
    copy_if_absent(TEMPLATE/'模型合同.md',root/'模型合同-模板.md')
    copy_if_absent(TEMPLATE/'主张—证据表.md',root/'主张—证据表.md')
    copy_if_absent(TEMPLATE/'团队分工.md',root/'团队分工.md')
    copy_if_absent(TEMPLATE/'Agent交接单.md',root/'Agent交接单-模板.md')
    copy_if_absent(ROOT/'模板/图表契约.md',root/'图表契约.md')
    copy_if_absent(TEMPLATE/'复现清单.json',root/'复现清单.json')
    copy_if_absent(TEMPLATE/'AI使用台账.json',root/'AI使用台账.json')
    copy_if_absent(ROOT/'references/compliance/CUMCM终审清单.md',root/'CUMCM终审清单.md')
    init_paper(root/'论文')
    state=root/'state/decision_log.json'
    if not state.exists():
        base=json.loads((TEMPLATE/'decision_log.json').read_text(encoding='utf-8'))
        base['competition']='cumcm'; base['problem_meta']['team_size']=3
        state.write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    readme=root/'README.md'
    if not readme.exists(): readme.write_text('# 数模C CUMCM项目\n\n请先放入题目与附件，填写模型合同和团队分工，再编译论文/论文.tex。\n',encoding='utf-8')
    print(f'initialized={root}'); print(f'questions={args.questions}'); print(f'paper_template={root/"论文/论文.tex"}')
    return 0
if __name__=='__main__': raise SystemExit(main())
