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

A specialized chemical engineering laboratory is testing the stability of three experimental catalysts: Alpha ($a$), Beta ($b$), and Gamma ($c$). These catalysts are measured by their mass in kilograms, and the total mass of the three substances used in every trial must always equal exactly $3$ kilograms ($a + b + c = 3$).

The lab monitors a "Total Resistance Index" for the reaction, which is calculated by summing the inverse square roots of specific molecular interactions. Specifically, the index is the sum of:
- The inverse square root of the interaction between Beta and Gamma plus the mass of Alpha ($1/\sqrt{bc+a}$)
- The inverse square root of the interaction between Gamma and Alpha plus the mass of Beta ($1/\sqrt{ca+b}$)
- The inverse square root of the interaction between Alpha and Beta plus the mass of Gamma ($1/\sqrt{ab+c}$)

Safety regulations require that this Total Resistance Index must always be greater than or equal to a safety threshold. This threshold is defined as a constant factor $k$ multiplied by the inverse square root of the sum of the pairwise products of the catalyst masses ($1/\sqrt{ab+bc+ca}$).

What is the largest possible value of the constant $k$ for which this safety inequality remains true for all valid positive masses of the three catalysts?

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
