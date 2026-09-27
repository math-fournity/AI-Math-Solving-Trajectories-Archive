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

In a specialized logistics warehouse, the floor is mapped as a grid of storage bays denoted by coordinates $(x, y)$, where both $x$ and $y$ are integers ranging from $-4$ to $4$ inclusive. This grid defines a region $\Gamma$ containing all possible bay locations.

A logistics manager needs to place a set of automated robots at different bay locations within $\Gamma$. To prevent navigation errors, any two distinct robots placed at bays $P(x_1, y_1)$ and $Q(x_2, y_2)$ must satisfy a "Stability Protocol" (Property $T$):
1. If the absolute horizontal distance of Robot $P$ from the central axis ($|x_1|$) is strictly greater than that of Robot $Q$ ($|x_2|$), then the absolute vertical distance of Robot $P$ ($|y_1|$) must be greater than or equal to that of Robot $Q$ ($|y_2|$).
2. Conversely, if the absolute horizontal distance of Robot $P$ ($|x_1|$) is strictly less than that of Robot $Q$ ($|x_2|$), then its absolute vertical distance ($|y_1|$) must be less than or equal to that of Robot $Q$ ($|y_2|$).
3. If their absolute horizontal distances are equal ($|x_1| = |x_2|$), the protocol is automatically satisfied regardless of their vertical positions.

What is the maximum number of robots that can be placed in the warehouse such that every pair of robots complies with the Stability Protocol?

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
