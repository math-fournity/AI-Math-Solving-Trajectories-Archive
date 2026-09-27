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

In a remote research facility, a diamond-shaped array of 25 sensor nodes is laid out on a coordinate grid. Each node must be assigned a unique frequency channel from the set $\{1, 2, 3, \dots, 25\}$. The nodes are positioned at the following coordinates $(row, column)$:

*   **Row 1:** (1,4)
*   **Row 2:** (2,3), (2,4), (2,5)
*   **Row 3:** (3,2), (3,3), (3,4), (3,5), (3,6)
*   **Row 4:** (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7)
*   **Row 5:** (5,2), (5,3), (5,4), (5,5), (5,6)
*   **Row 6:** (6,3), (6,4), (6,5)
*   **Row 7:** (7,4)

To prevent signal interference, the facility enforces two strict protocols:
1.  **Harmonic Isolation:** If two nodes are adjacent (sharing a horizontal or vertical side), their frequency channels $x$ and $y$ must be distinct enough such that one is at least double the other (i.e., $x \geq 2y$ or $y \geq 2x$).
2.  **Power Phase Restriction:** Nodes at specific coordinates must use even-numbered channels, while all others must use odd-numbered channels. The nodes restricted to **even** channels are: (1,4), (2,3), (2,4), (3,3), (3,5), (3,6), (4,1), (4,5), (5,3), (5,5), (6,5), and (7,4). All remaining 13 nodes must be assigned **odd** channels.

The following initial channel assignments have already been locked in:
*   Node (1,4) is set to **16**
*   Node (4,1) is set to **22**
*   Node (4,7) is set to **19**
*   Node (7,4) is set to **14**

Based on these protocols and the complete configuration of the grid, determine the sum of the frequency channels assigned to the seven nodes located in the center row (Row 4).

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
