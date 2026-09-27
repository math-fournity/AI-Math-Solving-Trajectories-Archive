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

A specialized biological research facility is monitoring a sequence of bacterial colony populations, represented by the positive value $a_n$ for each generation $n \geq 1$. 

The growth dynamics of these colonies are governed by a strict metabolic constraint. Specifically, for every generation $n$, the population of the previous generation ($a_{n-1}$) must not exceed the $n$-th power of the growth observed between the current generation and two generations into the future ($a_{n+2} - a_n$). Furthermore, this same $n$-th power value is constrained such that it cannot exceed the population of the immediate next generation ($a_{n+1}$). Mathematically, this relationship is expressed as:

\[ a_{n-1} \leq \left(a_{n+2} - a_n \right)^n \leq a_{n+1} \]

The lead researcher needs to determine the long-term stability of this biological system. Based on the constraints provided, calculate the value of the following limit:

\[ \lim_{n \to \infty} \frac{a_n}{n} \]

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
