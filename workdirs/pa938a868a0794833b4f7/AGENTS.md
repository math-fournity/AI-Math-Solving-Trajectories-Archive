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

A supply chain consists of 2023 consecutive logistics hubs, indexed from 1 to 2023. Each hub $i$ is assigned a "flow direction" $s_i$, which is either a value of 1 (forward) or -1 (reverse). 

An automated delivery drone must navigate a route through these hubs. A valid route is defined as a selection of $n$ hubs $(n \ge 1)$ indexed $t_1, t_2, \ldots, t_n$ that satisfy the following navigation constraints:
1. The drone must visit hubs in increasing order of their indices: $1 \le t_1 < t_2 < \dots < t_n \le 2023$.
2. To conserve energy, the drone can only travel a distance of 1 or 2 units between consecutive stops. Specifically, for every $i$ from 1 to $n-1$, the difference $t_{i+1} - t_i$ must be exactly 1 or 2.

The "net displacement" of a route is defined as the absolute value of the sum of the flow directions of the hubs visited: $|s_{t_1} + s_{t_2} + \dots + s_{t_n}|$.

Find the largest integer $C$ such that, regardless of how the flow directions $s_1, \dots, s_{2023}$ are assigned to the hubs, it is always possible to find a valid route with a net displacement of at least $C$.

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
