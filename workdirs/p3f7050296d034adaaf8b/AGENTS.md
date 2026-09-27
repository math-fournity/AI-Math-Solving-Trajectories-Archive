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

A specialized chemical processing plant operates a closed-loop system of $n$ reactors, where $n \geq 3$. The plant manager receives $n$ distinct batches of raw catalysts with specific potency levels, represented by the positive real numbers $x_1, x_2, \dots, x_n$. 

To optimize the reaction, the manager must arrange these batches into a circular sequence $y_1, y_2, \dots, y_n$ (where the indices wrap around such that $y_{n+1}=y_1$ and $y_{n+2}=y_2$). For every triplet of consecutive reactors $(i, i+1, i+2)$ in the cycle, an "Efficiency Coefficient" is calculated by dividing the square of the first reactor's potency ($y_i^2$) by a composite turbulence factor derived from the next two reactors ($y_{i+1}^2 - y_{i+1}y_{i+2} + y_{i+2}^2$).

The total performance of the system is defined as the sum of these Efficiency Coefficients across all $n$ positions:
$$ \sum_{i=1}^{n} \frac{y_{i}^{2}}{y_{i+1}^{2}-y_{i+1} y_{i+2}+y_{i+2}^{2}} $$

Determine the largest real number $M$ such that, regardless of the initial potency values provided, there always exists at least one permutation of the batches that results in a total performance sum greater than or equal to $M$.

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
