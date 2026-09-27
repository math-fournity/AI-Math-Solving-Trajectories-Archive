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

A high-tech research facility is testing a series of $2n$ experimental batteries, whose energy levels are denoted by $a_1, a_2, \ldots, a_{2n}$. These energy levels are non-negative values that, when combined, represent a single unit of total energy (the sum of all $a_i$ equals 1). Due to the cooling requirements of the facility, the batteries must be sorted in non-increasing order of their energy levels, such that $a_1 \ge a_2 \ge \cdots \ge a_{2n}$.

The batteries are paired into $n$ power modules. The first module contains the two most powerful batteries ($a_1$ and $a_2$), the second module contains the next two ($a_3$ and $a_4$), and so on, until the $n$-th module which contains the two weakest batteries ($a_{2n-1}$ and $a_{2n}$). The efficiency of each module is calculated as the sum of the squares of the energy levels of its two batteries. 

The total system performance is defined as the product of the efficiencies of all $n$ modules:
\[ (a_1^2 + a_2^2) \times (a_3^2 + a_4^2) \times \cdots \times (a_{2n-1}^2 + a_{2n}^2) \]

Given these constraints on the energy distribution, what is the maximum possible value for the total system performance?

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
