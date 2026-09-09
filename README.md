# 数模 C

数模 A 与数模 B 的独立融合版，面向 CUMCM 国赛、以 MATLAB 为主要计算平台、支持 AI/Agent 高强度协作的数学建模团队 Skill。适合三人队伍，尤其适合物理/工程背景。

## 核心能力

- 10 阶段 × 三人角色 × 证据链协作（B 内核）
- CUMCM 中文论文 XeLaTeX 模板（A 适配）
- MATLAB-first 求解、结果 JSON manifest、复现与证据绑定
- AI/Agent 协作协议：模型合同、主张—证据表、图表契约、AI 台账
- 2016–2019 传统优秀论文范式 + 题型案例（可迁移经验）
- 训练模式 / 比赛模式双轨
- 统一 CLI：`python tools/c.py <init|check|evidence|bind|version|figure|paper|ai-report|self-check>`

## 快速开始

```bash
# 1) 克隆后先获取字体（思源宋体 OFL + Windows 系统字体由本机生成）
python tools/fonts/fetch_sourcehan.py      # 下载思源宋体（OFL，约 40MB）
python tools/fonts/setup_fonts.py          # Windows 会自动探测 C:\Windows\Fonts

# 2) 自检
python tools/c.py self-check

# 3) 初始化一道比赛题
python tools/c.py init 2026国赛-A题 --questions 4
```

初始化后把题目放入 `题目/`、附件放入 `数据/`，填写 `团队分工.md` 和各问 `求解/问题X/模型合同.md`，再按 SKILL.md 工作流推进。

## 环境依赖

- 必需：Python 3.10+（无第三方包必需）
- 必需：XeLaTeX（TeX Live 2023+），用于 CUMCM 中文论文编译
- 必需：MATLAB（R2020+），用于主求解；函数为纯 MATLAB，不依赖第三方工具箱时可用基础版
- 可选：`pandoc` 或 `wkhtmltopdf`，用于 `c.py ai-report --pdf` 生成 AI 使用详情 PDF；缺少时保留 Markdown 并返回 BLOCKED
- 可选：字体自动生成仅支持 Windows；Linux/macOS 需 `--source` 提供字体目录或自行替换 format.cls 字体配置
- 可选：思源宋体由 `fetch_sourcehan.py` 从 Adobe 官方仓库（OFL）下载；离线环境可用 `--source-dir` 指向本地字体

## 重要边界

- MATLAB 实机运行与完整比赛端到端演练需在有 MATLAB 的机器上执行，本仓库不替代实机验证。
- 竞赛规则以当届官方文件为准；AI 使用披露按当届要求生成。
- 优秀论文案例分析是可迁移观察，不是官方评分标准；不得复制示例论文的结论或整段文本。
- 提交前须人工核对题意、公式、数字、图表、匿名和原创性；AI 输出不得直接作为最终裁决。

## 许可与来源

- 本仓库新增与融合内容：MIT（见 LICENSE）
- 上游来源与再分发要求：见 THIRD_PARTY_NOTICES.md（Mrite / mathmodel-skill / 思源宋体 / Windows 字体边界）

## 目录速览

```text
references/    阶段、角色、写作、结构、检验、AI、合规
templates/     CUMCM 中文论文模板与共享状态模板
tools/         c.py 统一入口、Python 工具、matlab/、latex/、figure/、ai-agents/
assets/        算法资料（来自 mathmodel-skill）
competitions/  cumcm 规则与写作启发
case_patterns/ 优秀论文范式报告与案例卡片
upgrade/       Prompt/结构/检验升级方案与 Action Items
```
