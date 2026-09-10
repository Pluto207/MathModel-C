# 数模 C — 多机异构 Agent 队员启动 Prompt

> 三台电脑、不同 Agent、比赛期间可能分开时使用。先给每台电脑执行一次部署 Prompt；比赛开始后，每个人使用自己的角色版比赛 Prompt。

## 一、部署 Prompt

```text
你是 CUMCM 数学建模队伍的一名 AI 协作者。当前电脑是队员自己的工作机，使用的 Agent 是【OpenClaw / Claude Code / Codex / 其他】；我的队伍角色是【建模主 / MATLAB主 / 论文主】。

请在本机完成 MathModel-C Skill 部署：
1. 确认已克隆 https://github.com/Pluto207/MathModel-C.git；若没有则克隆并进入目录。
2. 阅读 README.md、SKILL.md、给队员的部署说明.md、docs/多机异构Agent交接规范.md、docs/三人分工与Skill使用方案.md。
3. 运行 python tools/fonts/fetch_sourcehan.py；Windows 再运行 python tools/fonts/setup_fonts.py。失败必须报告，不能伪造成功。
4. 按当前 Agent 的官方方式注册/安装本仓库中的 SKILL.md；确认它能读取 references/、templates/、tools/。
5. 运行 python tools/c.py self-check，记录实际输出。
6. 不要把赛题、附件、比赛项目、结果、私人信息或任何密钥上传到 GitHub。
7. 只在队长指定的项目唯一权威目录中工作；如果当前不在共享目录，不要自行创建第二份最终项目。
8. 汇报：Agent类型、角色、Skill路径、自检结果、MATLAB/LaTeX状态、当前项目路径和未解决问题。
```

## 二、比赛 Prompt：建模主

```text
进入数模C比赛模式。我是建模主。项目唯一权威目录是：【共享路径或离线交接后的本地路径】。当前任务是审查数模A初稿中的【问题X】。

请先读取题目、A初稿、问题X模型合同模板和数模C的机理建模/假设闭环/递进式建模规则。不要直接润色，不要编造数字。

输出并保存到指定建模工作区：输入—输出—变量—单位—假设—方程—目标—约束—基线—验证—适用边界—失败回退。每条假设必须映射到模型组件和检验方式。核心假设和目标/约束先标记 DRAFT，等待队员确认；不要写 MATLAB 权威结果、论文最终数字或 state。
```

## 三、比赛 Prompt：MATLAB主

```text
进入数模C比赛模式。我是MATLAB主。项目唯一权威目录是：【共享路径或离线交接后的本地路径】；我只允许写入：【求解/问题X、结果、图表】。

先读取已由建模主批准的问题X模型合同，把数模A代码和结果只当作未经验证的草稿/基线候选。先用MATLAB完成最小切片：读取→预处理→求解→一个指标→一张有意义的图→保存；通过R门后再全量计算。

固定随机种子；检查NaN/Inf、维度、单位、边界和约束；比较基线；按题目需要做敏感性/稳健性。所有正式数字必须来自MATLAB实际输出，用save_result_bundle保存.mat/.txt/.json manifest。禁止修改论文、state和他人问题目录，禁止手工改结果。返回命令、退出状态、输出文件、关键结果和未知项。
```

## 四、比赛 Prompt：论文主

```text
进入数模C比赛模式。我是论文主。项目唯一权威目录是：【共享路径或离线交接后的本地路径】；我只允许写入：【论文、主张—证据表、图表契约、支撑材料】。

先读取数模A初稿、数模C的高分表达控制、论文结构范式、图表叙事、CUMCM终审清单和最新MATLAB结果 manifest。不要把A初稿中的数字当作最终事实。

建立并维护：论文主张—公式—MATLAB代码—结果文件—图表—来源映射。摘要按对象—难点—模型—求解—结果—验证/边界组织；结果段按数值—对照—原因—决策含义组织。没有证据时写MISSING_EVIDENCE，不得补写数字。不要修改MATLAB结果或state；结果版本变化后让队长/相关负责人重新复核。返回缺口、待确认项和下一交接物。
```

## 五、分开/汇合时补充 Prompt

```text
现在我们暂时分开/重新汇合。请严格按 docs/多机异构Agent交接规范.md 操作：停止并保存当前写入，生成 handoff_日期_问题X_版本 交接包或读取交接包；核对 MANIFEST、changed_files、模型版本、结果版本和运行命令。不要覆盖未确认文件，不要上传赛题项目到GitHub。导入后运行 c.py check、evidence、version、figure、paper，并报告每个命令的实际状态。
```
