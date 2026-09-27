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

In a specialized logistics network, there are 100 regional distribution hubs arranged in a large circle. Each hub $i$ (where $i = 1, 2, \ldots, 100$) is assigned a positive integer $a_i$ representing its fleet capacity. 

The efficiency rating of each hub, denoted by $b_i$, is calculated based on its neighbors in the circle. Specifically, for any hub $i$, its efficiency $b_i$ is defined as the sum of the capacities of its two immediate neighbors divided by its own capacity. Due to regulatory requirements, the capacity values $a_1, a_2, \ldots, a_{100}$ must be chosen such that every efficiency rating $b_1, b_2, \ldots, b_{100}$ results in a whole number (an integer). Note that for the first and last hubs, the neighbors are connected cyclically: $b_1 = \frac{a_{100} + a_2}{a_1}$ and $b_{100} = \frac{a_{99} + a_1}{a_{100}}$.

The network's Total Performance Score is defined as the sum of these efficiency ratings: $S_{100} = b_1 + b_2 + \ldots + b_{100}$. 

What is the maximum possible value of the Total Performance Score $S_{100}$?

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
