# 第三方来源与许可

数模C 不是从零开始的原创软件包，而是对以下公开/本地来源的融合与二次开发。发布和再分发时须保留各自许可与署名。

## 1. Mrite（数模A 的上游）

- 来源：https://github.com/Rzna-5559/Mrite
- 贡献内容：CUMCM 中文论文目录结构、XeLaTeX 模板骨架、字体组织方式、机理/工程题表达方法。
- 许可：上游 README 声明为 MIT；本仓库复制其工作区改造内容作为 C 的论文与建模表达基线。
- 使用要求：保留上方来源链接；示例论文中的数字、结论与参考文献不得作为新题答案复用。

## 2. mathmodel-skill（数模B 的内核）

- 来源：`数模B/.dsh/skills/mathmodel-skill`（本地副本）
- 贡献内容：10 阶段流程、三角色、状态日志 schema、CUMCM 规则包、算法资料、LaTeX/图表/XLSX/PDF 工具。
- 许可：MIT License（Copyright (c) 2026 rootkiller6788），许可证全文见随附的该目录 LICENSE 说明；发布时保留上述版权与许可声明。

## 3. Source Han Serif CN（思源宋体）

- 来源：Adobe/Google 开源思源宋体（Source Han Serif / Noto Serif CJK）。
- 贡献内容：`templates/cumcm/论文/fonts/SourceHanSerifCN-*.otf`。
- 许可：SIL Open Font License 1.1（OFL）。再分发须保留 OFL 声明，并不得单独出售字体文件。
- 官方许可：https://openfontlicense.org （OFL-1.1 文本见 https://scripts.sil.org/OFL）

## 4. Windows 系统字体（不随仓库分发）

- `templates/cumcm/论文/fonts/system/` 下的 Times New Roman、Arial、SimKai、Consolas 为微软系统字体，仅可用于 Windows 系统本地渲染，**禁止再分发**。
- 本仓库已通过 `.gitignore` 排除该目录；克隆后运行 `python tools/fonts/setup_fonts.py` 从本机 `C:\Windows\Fonts` 生成所需文件。

## 5. 竞赛资料与优秀论文

- `竞赛资料/`（A/B 的本地参考源，不入本仓库）为历年赛题与优秀论文，版权归各作者与主办方；本仓库仅保留不构成实质复制的索引/案例结论，不随仓库分发原始 PDF 或长段抽取文本。
- 案例卡片与范式报告是可迁移观察，不是官方评分标准。

## 声明

- 本仓库不包含任何参赛者个人身份信息、学号、密钥或凭据（已做检索确认）。
- 竞赛规则具有时效性：提交前必须以当届官方文件为准，本仓库规则包仅作核对辅助。
