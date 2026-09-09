#!/usr/bin/env python3
"""Download Source Han Serif CN (OFL) fonts used by the 数模C CUMCM template.

SIL OFL-1.1 allows free redistribution; we keep the binary fonts out of the
git repo to keep clones light, and fetch official release assets on demand.
"""
from __future__ import annotations
import argparse, shutil, sys, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
DEST = ROOT/'templates'/'cumcm'/'论文'/'fonts'
URLS = {
 'SourceHanSerifCN-Regular.otf':'https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTF/SimplifiedChinese/SourceHanSerifSC-Regular.otf',
 'SourceHanSerifCN-Bold.otf':'https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTF/SimplifiedChinese/SourceHanSerifSC-Bold.otf',
}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',type=Path,default=None,help='本地已有思源宋体目录（可选，避免下载）'); a=ap.parse_args(); DEST.mkdir(parents=True,exist_ok=True); missing=[]
 for name,url in URLS.items():
  dst=DEST/name
  if dst.exists(): print('exists',name); continue
  if a.source_dir is not None and (a.source_dir/name).exists(): shutil.copy2(a.source_dir/name,dst); print('copied',name); continue
  try:
   print('fetching',name,'...'); urllib.request.urlretrieve(url,dst); print('fetched',name)
  except Exception as e: missing.append(name); print('FAILED',name,e)
 print('fonts_dest=',DEST); print('missing=',missing)
 return 1 if missing else 0
if __name__=='__main__': raise SystemExit(main())
