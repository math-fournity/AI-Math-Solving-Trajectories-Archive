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

A specialized deep-sea sensor network consists of 11 nodes positioned at locations corresponding to the 11th roots of unity in a complex signal plane. One node, the "Origin Signal," is located at 1, while the remaining 10 nodes are designated as "Sub-nodes" $\alpha_1, \alpha_2, \ldots, \alpha_{10}$.

A master calibration function $f(x) = x^{10} + c_9x^9 + \dots + c_1x$ is programmed into the system, where every coefficient $c_i$ must be an integer. The system's architecture requires that the calibration value at both the zero-energy state ($x=0$) and the Origin Signal ($x=1$) must be exactly 0. 

A unique physical property of this network is that when the function is applied to any of the 10 Sub-nodes, the square of the output must result in a constant interference value of $-11$. That is, $(f(\alpha_i))^2 = -11$ for all $i \in \{1, 2, \dots, 10\}$.

The central processing unit calculates a structural stability index based on the interaction of these coefficients. Calculate the absolute value of the following combination of the function's internal parameters:
$|c_1 + 2c_2c_9 + 3c_3c_8 + 4c_4c_7 + 5c_5c_6|$

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
