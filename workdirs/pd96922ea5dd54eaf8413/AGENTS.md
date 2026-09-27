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

In a specialized seven-story vertical hydroponics facility, each of the 7 grow-beds on the ground floor (Level 1) is assigned a specific "Growth Index," which is a positive whole number. 

The facility is designed such that the automated nutrient system for the level directly above is determined by the sum of the indices of the two adjacent beds below it. Thus, Level 2 contains 6 nutrient nodes, each being the sum of the two beds below it. This process continues up the building: Level 3 has 5 nodes (each the sum of two adjacent nodes from Level 2), Level 4 has 4 nodes, Level 5 has 3 nodes, Level 6 has 2 nodes, and the apex (Level 7) contains a single final distribution node.

Across the entire facility, there are exactly 28 total nodes (7 + 6 + 5 + 4 + 3 + 2 + 1). An "Energy Efficiency Bonus" is triggered for any node that results in an even number. 

What is the minimum possible number of nodes across the entire 28-node structure that can be even?

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
