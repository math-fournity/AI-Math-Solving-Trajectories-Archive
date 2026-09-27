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

In a specialized logistics district, the boundary of a restricted cargo zone is defined by the hyperbolic curve $C: \frac{x^{2}}{4}-y^{2}=1$. A straight conveyor belt path $l$ is planned to pass through a specific control terminal located at coordinates $M(1,-1)$. This path $l$ is designed such that it intersects the eastern (right) boundary of the cargo zone at two distinct docking stations, $A$ and $B$, and crosses a main transit line represented by the $x$-axis at a junction point $N$.

The positions of these points along the path $l$ are governed by two efficiency ratios, $\lambda_{1}$ and $\lambda_{2}$. These ratios are defined by the vector relationships $\overrightarrow{MA} = \lambda_{1} \overrightarrow{AN}$ and $\overrightarrow{MB} = \lambda_{2} \overrightarrow{BN}$, where $\lambda_{1}, \lambda_{2} \in \mathbf{R}$.

Safety analysts have determined that the combined operational variance of the system, calculated as $V = \frac{\lambda_{1}}{\lambda_{2}} + \frac{\lambda_{2}}{\lambda_{1}}$, falls within a specific range of $(-\infty, a) \cup (b, +\infty)$ based on all possible orientations of the path $l$ that satisfy the intersection constraints.

Determine the value of the design constant $35a + b$.

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
