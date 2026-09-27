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

In a remote mountain range, a research station is designed as a perfect equilateral triangle. Along the perimeter and interior of this triangular plot, there are exactly 10 sensor nodes arranged in a grid of rows: the top row has 1 node, the second row has 2 nodes, the third row has 3 nodes, and the base row has 4 nodes. The distance between any two adjacent nodes (horizontally or along the 60-degree diagonal lines) is exactly 100 meters.

A maintenance drone must perform a "Full Circuit Inspection." A Full Circuit is defined as a sequence of nodes $S_1, S_2, \dots, S_{10}$ that satisfies three strict criteria:
1. The drone must visit every one of the 10 nodes exactly once.
2. Each leg of the flight (from $S_i$ to $S_{i+1}$) must be exactly 100 meters long, meaning the drone only moves between immediate neighbors in the grid.
3. The drone must return to its starting point from the final node (the distance from $S_{10}$ back to $S_1$ must also be exactly 100 meters).

Two circuits are considered distinct if the sequences of nodes are different (for example, starting at a different node or traversing the same spatial path in the opposite direction).

How many distinct Full Circuit sequences are possible for the drone to follow?

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
