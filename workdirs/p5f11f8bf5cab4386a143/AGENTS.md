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

In a specialized logistics network, there are two fleets of drones: Fleet $S$ and Fleet $T$. Each drone is identified by a positive integer representing its battery capacity in kilowatt-hours (kWh). A drone $a$ from Fleet $S$ is considered "compatible" with a drone $b$ from Fleet $T$ if and only if both of the following energy-sharing conditions are met:
1. $a \geq \frac{b}{2} + 7$
2. $b \geq \frac{a}{2} + 7$

The network is governed by a "Reliability Protocol": for any sub-group of drones $R \subseteq S$, the total number of distinct drones in Fleet $T$ that are compatible with at least one drone in $R$ must be greater than or equal to the number of drones in $R$ (i.e., $|T_{compatible}| \geq |R|$).

You are given that Fleet $S$ contains exactly six specific drones with capacities $\{14, 16, 20, 23, 31, 32\}$. Furthermore, the size of Fleet $T$ is at least 20 ($|T| \geq 20$). 

If the Reliability Protocol is strictly maintained for every possible sub-group of Fleet $S$, what is the minimum possible sum of the battery capacities of all drones in Fleet $T$?

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
