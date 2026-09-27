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

In a remote industrial zone, two surveillance boundaries are defined on a coordinate grid. Boundary $C_1$ follows the path of a hyperbola defined by the equation $x^2 - y^2 = 2m^2$, where $m$ is a non-zero scaling constant. Boundary $C_2$ is a parabolic perimeter. The vertex of this parabola is located at a control station $N$ at coordinates $(n, 0)$. The focus of the parabolic perimeter $C_2$ coincides exactly with the left focus $F$ of the hyperbolic boundary $C_1$.

A straight service road $l$, maintaining a constant incline with a slope of 1, is constructed to pass directly through the focus $F$. This road intersects the parabolic perimeter $C_2$ at two specific checkpoints, labeled $P$ and $Q$.

An environmental survey determines that for specific configurations of $m$ and $n$, the area of the triangular region formed by the two checkpoints $P, Q$ and the control station $N$ is exactly $S_{\triangle PNQ} = 4\sqrt{2}m^2$.

Let $S$ be the set of all possible values for the ratio $k = \frac{n}{m}$ that satisfy these geometric conditions. Calculate the sum of the squares of all elements contained in the set $S$.

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
