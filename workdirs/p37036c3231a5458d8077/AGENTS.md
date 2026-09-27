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

In a remote digital architecture project, a lead engineer is designing a square server grid with dimensions of $(2n+1) \times (2n+1)$ server nodes. The grid is wired in a strict alternating "checkerboard" binary state: every node is either in state "Active" or state "Idle." The layout is configured such that the nodes at the four extreme corners of the square grid are all in the "Active" state.

The engineer uses specialized cooling modules called "L-Blocks" to manage the heat of these Active nodes. Each L-Block is a rigid component that covers exactly three adjacent node positions, forming an "L" shape (specifically, it occupies three squares that meet at a common corner). 

The project requirements stipulate that every single "Active" node on the entire board must be covered by an L-Block to prevent overheating. However, the L-Blocks are highly sensitive and cannot overlap with one another. While the L-Blocks may cover "Idle" nodes during the process, their primary mission is to ensure every "Active" node is accounted for.

Find the smallest integer $n \ge 1$ for which it is mathematically possible to cover every "Active" node on the grid using these non-overlapping L-Blocks.

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
