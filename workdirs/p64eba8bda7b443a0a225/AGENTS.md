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

In a specialized laboratory, three experimental catalysts—$a$, $b$, and $c$—represent the three distinct concentrations that satisfy the chemical equilibrium equation $x^{3} - 2018x + 2018 = 0$.

A research team is measuring the "Power Output" of these catalysts. The output of a catalyst at a specific intensity level $n$ is defined as the sum of the $n$-th powers of the concentrations: $S_n = a^n + b^n + c^n$.

The team is searching for two specific intensity levels, $p$ and $q$, that satisfy a "Perfect Efficiency Ratio." This ratio is achieved when the average output at the combined intensity level $p+q$ is exactly equal to the product of the average outputs at the individual intensity levels $p$ and $q$. Mathematically, this balance is reached when:
$$\frac {S_{p+q}} {p+q} = \left(\frac {S_p} {p}\right)\left(\frac {S_q} {q}\right)$$

where $p$ and $q$ are positive integers and $0 < p \leq q$.

Determine the values of $p$ and $q$ for the smallest possible integer $q$ that satisfies this equilibrium condition, and calculate the final stability index given by the value of $p^2 + q^2$.

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
