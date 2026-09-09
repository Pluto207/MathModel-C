#!/usr/bin/env python3
"""Read-only mining index for local CUMCM excellent-paper PDFs.

Uses PyMuPDF when available, then pdftotext. Generated artifacts stay under output.
This is a corpus map and signal extractor, not a quality judge.
"""
from __future__ import annotations
import argparse, json, re, subprocess, signal
from collections import Counter
from datetime import datetime
from pathlib import Path

YEAR_RE=re.compile(r"20(?:1[6-9]|2[0-5])")
SECTIONS={
    "摘要":["摘要","abstract"], "问题分析":["问题分析","问题的分析","题目分析"],
    "假设":["模型假设","基本假设","假设条件","假设"], "符号":["符号说明","符号表","符号"],
    "模型建立":["模型的建立","模型建立","模型构建","模型的构建"],
    "模型求解":["模型求解","模型的求解","求解过程"],
    "结果":["结果分析","结果与分析","结果讨论","模型结果","结果"],
    "灵敏度":["灵敏度分析","敏感性分析","敏感性检验","敏感度"],
    "检验":["模型检验","模型验证","误差分析","稳健性","检验"],
    "评价推广":["模型评价","模型优缺点","优点与缺点","模型推广","推广"],
    "结论":["结论","结语"]}
PHRASES=["本文研究","针对","建立","构建","首先","其次","然后","最后","综上所述","结果表明","由此可见","验证","灵敏度","敏感性","鲁棒性","稳定性","误差","局限","推广","进一步"]

def pdf_text(p:Path)->tuple[str,str]:
    class Timeout(Exception): pass
    def alarm_handler(signum, frame): raise Timeout()
    old = signal.signal(signal.SIGALRM, alarm_handler)
    try:
        signal.alarm(12)
        try:
            import fitz
            doc=fitz.open(str(p)); text="\n".join(page.get_text("text") for page in doc)
            if text.strip(): return text,"pymupdf"
        except Exception: pass
        finally: signal.alarm(0)
        try:
            r=subprocess.run(["pdftotext","-enc","UTF-8",str(p),"-"],capture_output=True,text=True,errors="ignore",timeout=12)
            if r.returncode==0 and r.stdout.strip(): return r.stdout,"pdftotext"
        except Exception: pass
        return "","unreadable"
    except Timeout:
        return "","timeout"
    finally:
        signal.alarm(0); signal.signal(signal.SIGALRM, old)

def norm(s): return re.sub(r"\s+"," ",s).strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("source",type=Path); ap.add_argument("output",type=Path); ap.add_argument("--year-from",type=int,default=2016); ap.add_argument("--year-to",type=int,default=2025); args=ap.parse_args()
    src=args.source.resolve(); out=args.output.resolve(); out.mkdir(parents=True,exist_ok=True)
    rows=[]; section_counts=Counter(); phrase_counts=Counter(); year_counts=Counter(); method_counts=Counter(); unread=[]
    for p in sorted(src.rglob("*.pdf")):
        years=[int(x) for x in YEAR_RE.findall(str(p)) if args.year_from<=int(x)<=args.year_to]
        if not years or "优秀论文" not in str(p): continue
        year=years[0]; rel=str(p.relative_to(src)); text,method=pdf_text(p)
        if not text: unread.append(rel)
        low=text.lower(); sections=[]
        for sec,terms in SECTIONS.items():
            if any(t.lower() in low for t in terms): sections.append(sec); section_counts[sec]+=1
        for ph in PHRASES: phrase_counts[ph]+=text.count(ph)
        for term in ["微分方程","差分方程","蒙特卡洛","遗传算法","粒子群","模拟退火","线性规划","整数规划","层次分析","熵权","TOPSIS","灰色预测","回归","神经网络","灵敏度分析","敏感性分析","数值模拟","有限元"]:
            if term in text: method_counts[term]+=1
        year_counts[str(year)]+=1
        rows.append({"year":year,"path":rel,"filename":p.name,"chars":len(text),"pages_signal":text.count("\f")+1 if text else None,"extractor":method,"sections":sections,"pre_ai":year<=2019,"title_hint":next((norm(x) for x in text.splitlines() if len(norm(x))>=8),"")})
    rows.sort(key=lambda x:(x["year"],x["path"]))
    summary={"generated_at":datetime.now().isoformat(timespec="seconds"),"source":str(src),"years":dict(year_counts),"papers":len(rows),"unread":unread,"readable":len(rows)-len(unread),"section_presence":dict(section_counts),"phrase_counts":dict(phrase_counts),"method_presence":dict(method_counts),"pre_ai_years":"2016-2019"}
    (out/"corpus_index.json").write_text(json.dumps({"summary":summary,"papers":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    lines=["# CUMCM 优秀论文语料索引（2016–2025）","",f"生成时间：{summary['generated_at']}",f"论文总数：{len(rows)}",f"可抽取正文：{summary['readable']}",f"不可抽取：{len(unread)}","","## 年份分布","","| 年份 | 论文数 |","|---:|---:|"]
    for y,n in sorted(year_counts.items()): lines.append(f"| {y} | {n} |")
    lines += ["", "## 章节信号覆盖（仅表示文本中出现相关词，不等于质量评价）","", "| 模块 | 出现篇数 |","|---|---:|"]
    for k,v in section_counts.most_common(): lines.append(f"| {k} | {v} |")
    lines += ["", "## 方法信号覆盖（仅表示出现过术语，不代表方法使用正确）","", "| 术语 | 出现篇数 |","|---|---:|"]
    for k,v in method_counts.most_common(): lines.append(f"| {k} | {v} |")
    lines += ["", "## 语料范围说明","", "- 统计对象为 `竞赛资料/2016`–`2025` 下路径含 `优秀论文` 的 PDF。", "- `pre_ai=true` 标记 2016–2019 论文，作为重点人工归纳样本；这不是对论文是否使用 AI 的事实判断。", "- 章节、短语和方法统计只是检索信号，不能替代逐篇阅读、题目约束核对或质量评价。", "- PDF 可抽取并不等于内容已完成高分判读；后续报告会以案例卡片和人工复核为准。"]
    (out/"语料索引.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
