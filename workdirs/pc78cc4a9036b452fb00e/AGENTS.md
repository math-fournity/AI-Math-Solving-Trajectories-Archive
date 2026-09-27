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

In the futuristic city of Neo-Aethel, a digital architectural algorithm generates a structural sequence of "Energy Beams" denoted by $a_n$. The design is governed by strict foundational protocols: 
- The 0th beam has a power level of $a_0 = 0$.
- The 1st beam has a power level of $a_1 = 1$.
- The 2nd beam has a power level of $a_2 = 2$.

For every subsequent beam where $n \ge 0$, the power level of the $(n+3)$-th beam is calculated by adding the power level of the $(n+1)$-th beam to the power level of the $n$-th beam (specifically, $a_{n+3} = a_{n+1} + a_n$). 

A systems engineer is conducting a safety audit and needs to identify every beam index $n$ (where $n$ is a positive integer) that results in a power level $a_n$ exactly equal to a power of two (such as 1, 2, 4, 8, etc.). 

Find the sum of all such positive integers $n$.

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
