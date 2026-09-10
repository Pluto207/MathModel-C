# 多机异构 Agent 交接规范

## 0. 队长/主协调人的部署需要（你）

建议由当前 OpenClaw 所在的 Windows/WSL2 电脑作为主协调机，并完成以下一次性部署：

1. 确认已 clone `https://github.com/Pluto207/MathModel-C.git`，进入仓库根目录；
2. 运行 `python tools/fonts/fetch_sourcehan.py`，再运行 `python tools/fonts/setup_fonts.py`；
3. 运行 `python tools/c.py self-check`，确认 `status: PASS`；
4. 确认 OpenClaw 能读取本仓库的 `SKILL.md`、`references/`、`templates/` 和 `tools/`；
5. 确认本机有 MATLAB 与 XeLaTeX；在 MATLAB 中加入 `tools/matlab/` 并运行环境预检；
6. 建立唯一比赛项目目录，例如 `D:\mathmodel2026`，只对可信局域网开启 SMB 读写共享；
7. 在共享目录中由你执行一次 `python <本机MathModel-C路径>/tools/c.py init 2026国赛-A题 --questions 4`；
8. 在项目根目录填写 `团队分工.md`，指定角色、唯一项目路径、当前写入者和交接负责人；
9. 由你维护 `state/decision_log.json`、阶段决策和最终整合版本；不要让多个 Agent 同时修改它；
10. 比赛期间不把赛题 PDF、附件、项目代码、结果、论文草稿上传 GitHub；分开时使用可信局域网或受控离线介质交接。

主协调机不必承担全部计算，但必须保留项目权威目录和最终整合权。若你的电脑不是最适合跑 MATLAB 的机器，让 MATLAB 主在其电脑计算，再通过交接包导入经审核的结果。

## 1. 两层同步

### Skill 层

每台电脑分别从 GitHub 克隆并安装自己的 Agent Skill：

```text
OpenClaw：按其工作区/技能目录注册
Claude Code：~/.claude/skills/mathmodel-c/
Codex：~/.codex/skills/mathmodel-c/
其他 Agent：按其 skills 目录注册
```

Skill 可以用 GitHub 同步，更新前先 `git pull`。

### 比赛项目层

赛题 PDF、附件、代码、结果和论文不上传 GitHub。线下集中时放在主工作区机的 SMB 局域网共享目录；分开时使用受控的离线交接包（加密 U 盘或可信本地介质），回到一起再由整合负责人导入主工作区。

不要让三台电脑各自维护一份“最终项目”。项目唯一权威目录由队长在 `团队分工.md` 写明。

## 2. 交接包

分开前只交接增量和必要依赖：

```text
handoff_日期_问题X_版本/
├── MANIFEST.md
├── changed_files.txt
├── 模型合同.md
├── 代码/
├── 结果/
├── 图表/
├── 论文片段/
└── 待办.md
```

`MANIFEST.md` 必须写：当前阶段、负责人、模型版本、结果版本、输入文件摘要、变更文件、运行命令、关键结果、未解决问题、下一位负责人和审核状态。

## 3. 交接顺序

1. 当前负责人停止写入并保存；
2. 生成变更清单和结果 manifest；
3. 另一位队员核对文件数量、哈希/版本和运行命令；
4. 整合负责人备份主工作区；
5. 导入交接包，不直接覆盖未确认文件；
6. 运行 `c.py check/evidence/version/figure/paper`；
7. 相关角色标记 `REVIEWED` 或 `APPROVED` 后继续。

## 4. 写锁

- 同一时刻只能一人写同一文件；
- 论文 `.tex` 只能由论文主写；
- `state/decision_log.json` 只能由队长/整合负责人写；
- 结果只能由对应 MATLAB 负责人生成，不手工改结果；
- Agent 必须在 Prompt 中写明允许读、允许写、禁止路径；
- 发现冲突时保留两份，交给整合负责人裁决，不直接覆盖。

## 5. 竞赛红线

GitHub 只放 Skill。不要上传赛题、附件、比赛项目结果或包含题面内容的日志；不要把赛题发送到队外 AI/服务。具体以当届官方规则和赛区通知为准。
