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

In a futuristic energy grid, a central processor manages five distinct power frequencies. These frequencies are the roots of a specific "Efficiency Profile," a fifth-degree monic polynomial $P(x) = x^5 + a_4 x^4 + a_3 x^3 + a_2 x^2 + a_1 x + a_0$ with real-valued tuning coefficients.

The stability of the grid relies on a "Symmetry Protocol." This protocol dictates that if any frequency $\alpha$ (whether represented by a real number or a complex phase) is part of the system’s profile, then two specific modified frequencies must also be present in the same five-frequency set:
1. The reciprocal frequency, $\frac{1}{\alpha}$.
2. The complementary frequency, $1-\alpha$.

Let $S$ be the set of all possible Efficiency Profiles $P(x)$ that satisfy these constraints. An engineer needs to calculate a total "System Load" value. This value is determined by evaluating each valid polynomial in $S$ at an input of $x=1$ and then summing all these results together.

What is the sum of $P(1)$ for all polynomials $P$ in the set $S$?

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
