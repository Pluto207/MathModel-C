# 三人分工与 Skill 使用方案

## 固定角色

| 队员 | 第一阶段：数模A | 第二阶段：数模C | 最终交付 |
|---|---|---|---|
| 建模/物理主 | 快速读题、初步假设、基础模型 | 模型合同、假设闭环、方程/约束复核、检验设计 | APPROVED 模型与验证矩阵 |
| MATLAB/计算主 | 初步代码、基础结果、快速出图 | MATLAB 重做、基线/主模型、约束、敏感性、manifest | 权威结果包与图表 |
| 论文/整合主 | 初稿骨架、章节和初步结果位置 | 主张—证据、结果替换、表达升级、LaTeX、终审 | C-approved 论文与支撑材料 |

## 共同使用顺序

1. 三人可以用 A 快速形成共同初稿；
2. 初稿冻结后，建模主先用 C 完成模型合同；
3. MATLAB 主读取已批准合同并重做；
4. 论文主同步建立证据表，但等正式结果锁定后写最终数字；
5. 全员审查核心假设、约束、摘要数字和最终结论。

## 各角色必读

- 建模主：`references/modeling/机理建模.md`、`references/validation/假设闭环.md`、`references/structure/递进式建模.md`。
- MATLAB 主：`tools/matlab/README.md`、`references/stages/Stage_05_MATLAB求解.md`、`references/stages/Stage_06_稳健性.md`。
- 论文主：`references/writing/`、`references/structure/`、`references/compliance/CUMCM终审清单.md`。

## 写入边界

- 建模主写模型分析与合同；不直接覆盖 MATLAB 权威结果；
- MATLAB 主写自己的问题目录、结果和图表；不直接修改论文主稿；
- 论文主写论文、证据表和格式材料；不手工改 MATLAB 结果；
- `state/decision_log.json` 由队长或指定整合负责人维护；
- 同一文件同一时间只能有一个写入者。

## 交接状态

```text
DRAFT → REVIEWED → APPROVED
```

核心假设、目标函数、约束、关键数字和摘要必须至少两人确认后才是 `APPROVED`。
