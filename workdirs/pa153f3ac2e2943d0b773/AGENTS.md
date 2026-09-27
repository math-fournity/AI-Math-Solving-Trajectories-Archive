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

In a high-security data center, there is a grid of processing nodes arranged in a $19 \times 19$ square array. Currently, $n$ distinct data packets are stored, each occupying exactly one node.

The system operates in discrete cycles. At the start of every cycle, a load-balancing protocol triggers: every single packet must simultaneously migrate to a node that is directly adjacent to its current position (either horizontally or vertically). To prevent data corruption, no two packets are allowed to occupy the same node at the end of a cycle. 

Furthermore, the hardware architecture imposes a specific momentum constraint: no packet can move along the same axis (horizontal or vertical) in two consecutive cycles. For example, if a packet moves from node $(x, y)$ to $(x+1, y)$ in cycle 1, it is strictly forbidden from moving to $(x+2, y)$ or back to $(x, y)$ in cycle 2; it must move to either $(x+1, y+1)$ or $(x+1, y-1)$.

What is the maximum number of data packets $n$ that can be placed in this grid such that this migration process can continue for an infinite number of cycles without ever violating a constraint or reaching a state where a valid move is impossible?

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
