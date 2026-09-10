---
name: mathmodel-c
version: 1.0.0
lang: zh-CN
description: 面向 CUMCM 国赛的 MATLAB-first 数学建模协作 Skill：融合机理建模、数据分析、优化、预测、AI/Agent 协作、可复现结果、中文论文与提交合规。Use when a team is preparing or executing a mathematical modeling competition, especially CUMCM A题, with MATLAB and AI/agents.
---

# 数模 C：MATLAB-first CUMCM 融合工作流

## 总原则

1. 官方规则优先于本 Skill；题意优先于算法；模型解释优先于复杂度。
2. MATLAB 是核心求解、仿真、优化和制图平台；Python 仅作辅助、格式处理或降级路线。
3. 每问先做可解释基线，再做主模型；没有验证不宣称有效、优于或最优。
4. AI/Agent 可以分析、编码、审查和润色，但不能替队员裁决题意、核心假设、关键结果或最终提交。
5. 所有关键数字必须沿着“公式→代码→结果→图表→论文”追溯。
6. 训练模式完整，比赛模式轻量；流程服务于建模，不反过来拖慢比赛。
7. 本 Skill 根目录只读；实际项目目录由用户单独初始化并写入。

## 唯一主流程

0. 启动与环境冻结：确认届次、规则、队伍、MATLAB/Python/LaTeX、AI记录方式。
1. 选题：三人独立分析 A/B/C，按可理解性、匹配度、可实现性、可验证性和风险比较。
2. 拆题：建立每问的输入—输出—约束—评价指标—依赖图。
3. 模型选型：每问最多一个基线、一个主模型、一个必要备选；先机理后算法。
4. 模型合同：冻结变量、假设、目标、约束、求解器、验证与输出文件。
5. MATLAB 最小切片：从项目根目录跑通小数据/等价实例的读取—预处理—求解—结果—图。
6. 全量求解与稳健性：参数、初值、随机种子、边界、量纲、可行性、敏感性。
7. 结果锁定：生成结构化结果、复现清单和主张—证据映射。
8. 论文装配：使用 CUMCM 中文 LaTeX 模板；先结果后段落，最后摘要。
9. 终审提交：规则、匿名、AI披露、页数、文件大小、图表、数字和支撑材料。

## 四个比赛硬门

- M 门（模型合同）：每问的输入、输出、变量、假设、目标、约束、验证齐全。
- R 门（运行）：MATLAB 主入口可独立运行，产生真实结果和至少一张有意义的图。
- E 门（证据）：论文数字、公式、代码、结果和图表一致，可复现。
- W 门（交付）：论文结构、格式、匿名、AI披露和支撑材料符合当届规则。

训练模式可将四门细化为 B 的 M1/P1/P2/W1/W2；比赛模式只保留四门，不为流程生成无效文档。

## 角色

- 建模主：题意、机理、假设、方程、模型取舍和物理解释。
- MATLAB 主：数据、函数、求解、实验、结果、图表和复现。
- 论文主：符号、证据链、论文、LaTeX、引用、合规和终审。
- Agent 是按任务临时调用的协作者，不是第四名队员；关键结果必须由队员复核。

## 路径合同

每个比赛项目使用：`state/`、`题目/`、`数据/`、`求解/`、`结果/`、`图表/`、`论文/`、`支撑材料/`。
每问至少有 `求解/问题X/main_qX.m`，最终论文入口固定为 `论文/论文.tex`，结果优先保存 CSV/MAT/JSON，图表由代码生成。

## 双阶段与多机运行策略

- 可先用数模A形成完整 `DRAFT` 初稿；初稿冻结后必须由数模C按角色重做模型、MATLAB结果、证据链和论文，最终只认 C-approved 版本。
- 三台电脑各自安装 Skill；比赛项目只有一个权威目录。在一起时使用可信局域网共享，分开时使用受控离线交接包；赛题/附件/比赛项目不上传 GitHub。
- 建模主、MATLAB主、论文主的写入边界和交接格式见 `docs/三人分工与Skill使用方案.md`、`docs/A初稿到C优化整合流程.md`、`docs/多机异构Agent交接规范.md`。

## 运行时加载与质量升级

- 写作前必须读取 `references/writing/高分表达控制.md`、`references/writing/摘要与结果分析范式.md`。
- 框架生成前必须读取 `references/structure/论文结构范式.md`、`references/structure/递进式建模.md` 和 `references/structure/图表叙事节奏.md`。
- 检验设计必须读取 `references/validation/假设闭环.md`、`references/validation/鲁棒性与敏感性.md`；按题型建立检验矩阵。
- 论文生成依赖 `模板/模型合同.md`、`模板/主张—证据表.md` 和图表契约；缺证据返回 `MISSING_EVIDENCE`，不得编造数字。
- 结果固化后运行 `tools/bind_evidence.py`，将模型版本、结果版本和证据状态绑定；版本变化使相关主张退回 `REVIEW`。

## 启动方式

先阅读 `使用指南.md`，再按模式读取 `references/stages/` 中对应阶段；进入 MATLAB 阶段读取 `tools/matlab/README.md`，进入 AI 阶段读取 `references/ai/`，进入论文阶段读取 `competitions/cumcm/` 和 `templates/cumcm/`。
进入写作/框架阶段还必须读取 `references/writing/`、`references/structure/`；进入检验阶段读取 `references/validation/`。完成结果后运行 `tools/bind_evidence.py`；需要生成 AI 详情时运行 `tools/ai-agents/build_ai_report.py`。
