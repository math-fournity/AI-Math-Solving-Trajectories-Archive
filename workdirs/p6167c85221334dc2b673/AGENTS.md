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

A high-tech circular particle accelerator contains 2024 distinct stabilization chambers, indexed sequentially from 1 to 2024, arranged in a perfect ring. For each chamber $i$, let $a_i$ represent its specific energy level, measured as a strictly positive real number. Due to the ring's geometry, chamber 1 is adjacent to chamber 2024 and chamber 2.

The system is in a "Discrete Harmonic State" if, for every single chamber $i$, the sum of the energy levels of its two immediate neighbors ($a_{i-1}$ and $a_{i+1}$) is a perfect integer multiple of its own energy level $a_i$. Specifically, for each $i \in \{1, 2, \dots, 2024\}$, the ratio $k_i = \frac{a_{i-1} + a_{i+1}}{a_i}$ must be a positive integer (where we define $a_0 = a_{2024}$ and $a_{2025} = a_1$).

Engineers define the "Total Resonance Score" $S$ of the accelerator as the sum of these 2024 integer ratios: $S = \sum_{i=1}^{2024} k_i$.

If the energy levels across the chambers are not all identical, what is the maximum possible value of the integer $S$?

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
