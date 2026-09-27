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

In the imperial capital of Gridania, an architect is designing a decorative garden feature consisting of a specific arrangement of stone pedestals.

The pedestals are placed at every coordinate $(x, y)$ such that $|x| = |y| \le 3$, where $x$ and $y$ are integers. This creates a set of pedestals located at the corners and along the diagonals of a $6 \times 6$ square grid centered at the origin.

The architect must plant one of three types of flowers—Red Roses, Blue Lilies, or Green Ferns—on each pedestal. However, botanical restrictions dictate that "adjacent" pedestals cannot host the same type of flower. Two pedestals, $P$ and $Q$, are considered "adjacent" if they satisfy either of the following conditions:
1. The distance between them is exactly $\sqrt{2}$ units (representing immediate diagonal neighbors).
2. The straight line segment connecting them is parallel to either the horizontal or vertical axis of the grid.

Let $C(3)$ represent the total number of distinct ways to assign the three flower types to these specific pedestals such that no two adjacent pedestals share the same flower color.

Compute the value of $C(3)$.

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
