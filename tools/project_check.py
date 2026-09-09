#!/usr/bin/env python3
"""Read-only structural checker for a 数模C competition project."""
from __future__ import annotations
import argparse, json
from pathlib import Path

REQUIRED = ['state','题目','数据','求解','结果','图表','论文','支撑材料']

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('project', type=Path)
    args = ap.parse_args()
    root = args.project.resolve()
    missing = [x for x in REQUIRED if not (root/x).is_dir()]
    print(f'project={root}')
    print('missing=' + ','.join(missing))
    state = root/'state'/'decision_log.json'
    if state.exists():
        try:
            data=json.loads(state.read_text(encoding='utf-8'))
            print('decision_log=JSON_OK')
            print('current_stage=', data.get('current_stage'))
        except Exception as exc:
            print('decision_log=INVALID', exc)
            return 1
    else:
        print('decision_log=MISSING')
    return 1 if missing else 0

if __name__ == '__main__':
    raise SystemExit(main())
