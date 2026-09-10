# 多机异构 Agent 交接规范

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
