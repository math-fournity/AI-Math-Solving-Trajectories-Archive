# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.
You may use computation for exploration or verification.

Output your complete proof directly in your response (in this TUI).
Do NOT write any files — do not use write/edit tools.
End your proof with a line containing exactly: ### PROOF COMPLETE
Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {n | ...}`)

## Problem

# Problem

A high-security data center maintains two circular synchronization rings: the Alpha Ring, containing $n = 101$ primary servers, and the Beta Ring, containing the $n$ corresponding backup units for those specific servers. Two diagnostic probes, the Master Probe and the Slave Probe, perform integrity checks on these rings in two distinct operational modes:

(i) In the first mode, the Master Probe scans the primary servers in the Alpha Ring one by one in a clockwise direction, starting with Server $S_1$. Every time the Master Probe pings a primary server, the Slave Probe simultaneously moves clockwise around the Beta Ring to ping that specific server’s designated backup unit. By the time the Master Probe has scanned every primary server exactly once and returns to $S_1$, the Slave Probe has completed exactly $a$ full revolutions around the Beta Ring.

(ii) In the second mode, the Slave Probe scans the backup units in the Beta Ring one by one in a clockwise direction, starting with Backup Unit $B_1$. Every time the Slave Probe pings a backup unit, the Master Probe simultaneously moves clockwise around the Alpha Ring to ping that unit’s corresponding primary server. By the time the Slave Probe has scanned every backup unit exactly once and returns to $B_1$, the Master Probe has completed exactly $b$ full revolutions around the Alpha Ring.

The backup units are arranged in the Beta Ring in a specific fixed permutation relative to their primary counterparts in the Alpha Ring. Determine the maximum possible value of the absolute difference $|a-b|$.

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说（必须用英文原文）：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
