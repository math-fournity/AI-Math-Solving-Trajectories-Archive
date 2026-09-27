# AI-Math-Solving-Trajectories-Archive

AI 数学竞赛题解题系统**早期世代**的每题运行现场归档——约 5 万个 run 目录、40 万+ 文件，
覆盖平凡解题系统（Normal Solver）与多轮 POC 世代的完整解题现场：对话录、会话轨迹、
终端日志、采集快照与解题工作目录。作为未来系统化解题工程的原始数据集发布。

> 分工：早期管线代码见
> [AI-Math-Normal-Solver](https://github.com/math-fournity/AI-Math-Normal-Solver)；
> 当前世代主系统见
> [AI-Math-Competition-Problem-Solving-System](https://github.com/math-fournity/AI-Math-Competition-Problem-Solving-System)；
> 当前世代运行现场见
> [AI-Math-Solving-Trajectories](https://github.com/math-fournity/AI-Math-Solving-Trajectories)；
> 数据表（含本世代 `devin_problem_runs` 50,552 条运行记录）见
> [AI-Math-Solving-Databases](https://github.com/math-fournity/AI-Math-Solving-Databases)。

## 目录结构

| 目录 | 内容 |
|---|---|
| `runs/` | 每题轨迹目录（TRAJECTORY 侧）：`exports/`（对话录导出）、`sessions_db/trajectory.jsonl`（会话轨迹事件流）、`collector/`（终端面板快照）、`session_info.json`（运行元数据）、`tmux/`（原始终端日志） |
| `workdirs/` | 每题解题工作目录：题面 AGENTS.md、prompts、proof 等 |
| `analysis-devin-failure/` | devin 解题失败分析现场（full-analysis-* 每题分析目录；原始日志未纳入） |
| `analysis-devin-failure-workdirs/` | 失败分析的工作目录侧 |

## 世代与命名对照

| 前缀模式 | 世代/批次 |
|---|---|
| `p<24位hash>` | 按题 ID 散列命名的批量 run（平凡解题系统 auto_runner 时代，数量最多） |
| `dpb-2026MMDD-*` | batch_problem_runner 批次（tier1/tier2、并发度与题目 compfiles/omni_math/mathnet/fate 标注在名中） |
| `vms-poc8-*` / `vms-poc9-*` | POC 8/9 世代（tree/dynamic/lineage/interference/bare 变体） |
| `ab-253-*` / `ab-test-*` / `e2e-253-*` | 题目 253 的 A/B 与端到端实验 |
| `bare-c1/c4/c6-*` | bare 能力基线测试 |
| `359-retest-*` / `362-codex-direct-*` | 1631/1709/1843/1962 题集复测与 codex 直跑对照 |
| `eight-p1-*` | eight-p1 世代（L/D/R 变体，1962/1843/1709 题集） |
| `round2-verify` / `clean-ext-*` / `pdf*` | 二轮验证、外部清理延伸与 pdf 提取实验 |

## 数据说明

- 对话录与轨迹为 AI 解题过程记录，不含 API 密钥/凭据（已做凭据模式扫描）。
- 未纳入上传：mitm 代理原始流量捕获（`mitm/`，可能含请求头凭据）、失败分析的原始
  日志（`_logs/`）、基础设施目录（`_shared/_pipe/_queue_in/_batches`）——它们仅保留
  在本地，永不删除。
- run 目录与数据表可通过 `session_info.json` 的 `devin_session_id`、目录名中的
  `p<problem_key>` 与数据表 `devin_problem_runs` 对账。

## License

MIT License，见 [LICENSE](LICENSE)。
