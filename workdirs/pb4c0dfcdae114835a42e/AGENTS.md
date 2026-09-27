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

In a specialized tiered data-processing facility, there are 29 processing nodes arranged in a grid-like structure. The nodes are organized into six horizontal ranks. From top to bottom, the number of nodes in each rank is as follows:
- Rank 1 (Top): 5 nodes
- Rank 2: 5 nodes
- Rank 3: 5 nodes
- Rank 4: 5 nodes
- Rank 5: 5 nodes
- Rank 6 (Bottom): 4 nodes

The nodes are aligned such that each rank from Rank 1 to Rank 5 is positioned directly above the rank beneath it. However, the 4 nodes in Rank 6 are positioned directly beneath the leftmost 4 nodes of Rank 5.

A single data packet is injected into one of the 5 nodes in Rank 1. Every second, the packet must move to a node in the rank immediately below its current position. From any given node, the packet can only move via two possible protocols:
1. **Vertical Drop:** To the node directly below its current position (available only if a node exists at that coordinate in the next rank).
2. **Diagonal Shift:** To the node one position to the left and one rank down from its current position (available only if a node exists at that coordinate in the next rank).

The packet continues this downward transmission until it reaches any node in Rank 6. How many distinct transmission paths can the data packet take from the top rank to the bottom rank?

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
