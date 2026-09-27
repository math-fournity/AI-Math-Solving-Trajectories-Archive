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

A specialized chemical refinery manages the flow rates of four volatile compounds: $x, y, z$, and $u$. The efficiency of the mixing chambers is governed by "harmonic coupling constants." The plant manager monitors these constants through the following industrial specifications:

1.  The combined efficiency of the first two compounds is $\frac{xy}{x+y} = \frac{1}{a}$.
2.  The combined efficiency of the second and third compounds is $\frac{yz}{y+z} = \frac{1}{b}$.
3.  The combined efficiency of the third and fourth compounds is $\frac{zu}{z+u} = \frac{1}{c}$.
4.  The global efficiency of the four-way intersection is $\frac{xyzu}{x+y+z+u} = \frac{1}{d}$.

The quality control team investigates two specific operational configurations:
- **Configuration $S_1$**: The constants are set to $a=1, b=2, c=-1, d=1$.
- **Configuration $S_2$**: The constants are set to $a=1, b=3, c=-2, d=1$.

For every valid set of flow rates $(x, y, z, u)$ that satisfies the specifications in a given configuration, a performance metric $V$ is calculated using the formula:
$$V = \frac{1}{x} + \frac{2}{y} + \frac{3}{z} + \frac{4}{u}$$

Find the sum of all possible values of $V$ generated across all solutions found in both $S_1$ and $S_2$.

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
