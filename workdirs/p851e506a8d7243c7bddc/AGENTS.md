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

A high-security data vault consists of a grid of 100 storage nodes arranged in a $10 \times 10$ array. Each node can be set to one of two states: "Active" (represented by the value $+1$) or "Standby" (represented by the value $-1$).

The system initialization follows a strict two-step protocol:
1. **Perimeter Hardening:** All 36 nodes located on the perimeter of the grid (the first row, last row, first column, and last column) are permanently set to the "Standby" state ($-1$).
2. **Sequential Activation:** One by one, each of the 64 interior nodes is programmed. To set the state of an empty interior node at position $(i, j)$, the system identifies two previously filled nodes that are closest to $(i, j)$ and lie on opposite sides of it—either within the same row or within the same column. The state of node $(i, j)$ is then calculated as the product of the values of these two chosen neighbors. This process repeats until all 100 nodes in the grid have been assigned a value.

Depending on the order in which the interior nodes are chosen and whether a row-pair or column-pair is used for the calculation, the final distribution of states in the grid will vary.

Let $M$ be the maximum possible number of "Active" ($+1$) nodes that can exist in the completed $10 \times 10$ grid, and let $m$ be the minimum possible number of "Active" ($+1$) nodes that can exist. Find the value of $M + m$.

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
