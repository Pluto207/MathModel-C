# 数模 C 工具入口

## 比赛前最常用

```bash
python 数模C/tools/c.py init 2026国赛-A题
python 数模C/tools/c.py check 2026国赛-A题
python 数模C/tools/c.py evidence 2026国赛-A题
python 数模C/tools/c.py version 2026国赛-A题
python 数模C/tools/c.py figure 2026国赛-A题
python 数模C/tools/c.py paper 2026国赛-A题
python 数模C/tools/c.py ai-report 2026国赛-A题
```

## 工具说明

- `tools/c.py`：统一入口。
- `tools/init_project.py`：初始化 CUMCM 三人项目。
- `tools/project_check.py`、`tools/state_check.py`：项目结构与状态检查。
- `tools/evidence_check.py`、`tools/bind_evidence.py`：主张—结果证据检查与绑定。
- `tools/version_check.py`：结果 manifest 变化检测和主张状态回退。
- `tools/figure_contract_check.py`：图表主张/来源/代码/结果绑定。
- `tools/paper_number_check.py`：论文占位符和证据表基础检查。
- `tools/ai-agents/`：AI台账、详情报告和 Agent 任务边界工具。
- `tools/matlab/`：MATLAB 环境、结果固化和核心检查函数。
- `tools/matlab/result_to_latex.py`：CSV/JSON结果转 LaTeX 表格片段。
- `tools/latex/`、`figure/`、`xlsx/`、`pdf/`：辅助工具，使用前读取各自 SKILL.md。

所有检查工具默认只读；任何安装、删除、覆盖和外部提交动作都必须由用户明确授权。