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

A team of civil engineers is designing a modular irrigation system consisting of $n$ parallel pipes, where $n$ is an integer at least 2. Each pipe $i$ has a non-integer, positive flow resistance $a_i$. These pipes are calibrated such that their total efficiency is perfectly balanced, meaning the sum of their reciprocal resistances equals exactly 1: 
$$\frac{1}{a_1} + \frac{1}{a_2} + \cdots + \frac{1}{a_n} = 1.$$

For maintenance purposes, the engineers must replace each pipe $i$ with a standard-grade pipe that has a positive integer resistance $b_i$. To ensure the system remains close to original specifications, each new resistance $b_i$ must be one of the two integers closest to the original value: either the floor $\lfloor a_i \rfloor$ or the ceiling $\lceil a_i \rceil$.

The engineers need to ensure that the new total efficiency, $E = \sum_{i=1}^n \frac{1}{b_i}$, strictly exceeds the original balance of 1, but does not exceed a maximum tolerance threshold $C$.

Find the smallest constant $C > 1$ such that, regardless of the initial non-integer resistances $a_i$ or the number of pipes $n \geq 2$, there always exists a choice of integer resistances $b_i \in \{\lfloor a_i \rfloor, \lceil a_i \rceil\}$ satisfying:
$$1 < \frac{1}{b_1} + \frac{1}{b_2} + \cdots + \frac{1}{b_n} \leq C.$$

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
