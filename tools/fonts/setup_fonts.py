#!/usr/bin/env python3
"""Copy Windows system fonts used by the 数模C CUMCM template into the project.

These fonts are NOT redistributable, so clones generate them from the local
Windows fonts directory. On Linux/macOS, provide a --source directory holding
the renamed files, or install equivalent fonts and adjust format.cls.
"""
from __future__ import annotations
import argparse, shutil, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
DEST = ROOT/'templates'/'cumcm'/'论文'/'fonts'/'system'
MAP = {
 'times.ttf':'TimesNewRoman-Regular.ttf','timesbd.ttf':'TimesNewRoman-Bold.ttf',
 'timesi.ttf':'TimesNewRoman-Italic.ttf','timesbi.ttf':'TimesNewRoman-BoldItalic.ttf',
 'arial.ttf':'Arial-Regular.ttf','arialbd.ttf':'Arial-Bold.ttf','ariali.ttf':'Arial-Italic.ttf',
 'arialbi.ttf':'Arial-BoldItalic.ttf','simkai.ttf':'SimKai.ttf',
 'consola.ttf':'Consolas-Regular.ttf','consolab.ttf':'Consolas-Bold.ttf',
 'consolai.ttf':'Consolas-Italic.ttf','consolaz.ttf':'Consolas-BoldItalic.ttf',
}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source',type=Path,default=None,help='Windows字体目录；默认自动探测'); a=ap.parse_args()
 src=a.source
 if src is None:
  for cand in ['/mnt/c/Windows/Fonts','C:/Windows/Fonts',str(Path('C:/Windows/Fonts'))]:
   if Path(cand).exists(): src=Path(cand); break
 if src is None or not src.exists(): print('BLOCKED no Windows fonts dir; use --source'); return 2
 DEST.mkdir(parents=True,exist_ok=True); missing=[]
 for win_name,dst_name in MAP.items():
  s=src/win_name
  if s.exists(): shutil.copy2(s,DEST/dst_name)
  else: missing.append(win_name)
 print('fonts_dest=',DEST); print('missing=',missing)
 return 1 if missing else 0
if __name__=='__main__': raise SystemExit(main())
