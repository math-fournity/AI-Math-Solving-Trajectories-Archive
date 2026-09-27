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

In the field of architectural acoustics, a team of engineers is designing a modular sound-dampening chamber. The chamber is divided into $n$ distinct acoustic zones, where $n$ is a positive integer. Each zone $i$ is assigned a specific absorption coefficient $x_i$, where every $x_i$ must be a positive value. To maintain the structural integrity of the soundproofing material, the sum of these coefficients must be exactly 1, such that $x_1 + x_2 + \dots + x_n = 1$.

The "Interference Index" of the chamber is calculated by taking the absorption coefficient of each zone and raising it to the power of the coefficient of the subsequent zone (with the final zone's coefficient raised to the power of the first), and then multiplying all these results together. Specifically, the index is defined as:
\[ \text{Index} = x_1^{x_2} \cdot x_2^{x_3} \cdot \dots \cdot x_n^{x_1} \]

The lead architect determines that for the chamber to be commercially viable, this Interference Index must never exceed the value of $\frac{1}{n}$, regardless of how the absorption coefficients $x_1, \dots, x_n$ are distributed.

Find the greatest positive integer $n$ for which this condition is guaranteed to hold for all possible sets of positive coefficients.

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
