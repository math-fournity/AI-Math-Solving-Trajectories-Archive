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

In a remote industrial sector, there are $n$ distinct energy reservoirs, indexed as $R_1, R_2, \ldots, R_n$. At the start of the operation, each reservoir $R_i$ is charged with exactly $i$ units of energy. 

The facility operates through a continuous maintenance cycle. For the operation to proceed indefinitely, a supervisor must perform the following three-step protocol during every cycle:

1.  **Selection:** The supervisor identifies exactly $k+1$ reservoirs to participate in the cycle.
2.  **Redistribution:** From the selected group of $k+1$ reservoirs, the supervisor designates $k$ reservoirs as "sources" and the remaining one reservoir as the "receiver."
    *   From each of the $k$ source reservoirs, at least half of the current energy units must be extracted and discarded.
    *   The single receiver reservoir, if it is indexed as $R_i$, is then injected with a fresh supplement of exactly $i$ energy units.
3.  **Stability Check:** If any of the $n$ reservoirs in the facility reaches a state of zero energy, the entire system suffers a permanent shutdown. Otherwise, the cycle repeats.

Given that $k$ is a fixed positive integer, determine the minimum integer $n \ge k+1$ such that there exists a strategy to manage the energy levels so that the facility never shuts down.

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
