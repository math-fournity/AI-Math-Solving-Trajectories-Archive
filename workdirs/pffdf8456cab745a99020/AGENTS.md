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

In a high-security data facility, a mainframe is composed of a $100 \times 100$ grid of server nodes. Each node must be set to one of two states: "Active" (represented by a high signal) or "Inactive" (represented by a low signal). 

Due to safety regulations, every node located on the perimeter of the grid (those in the outermost rows and columns) must be set to the "Active" state.

Analysts are monitoring the stability of the grid by looking at every possible $2 \times 2$ cluster of four adjacent nodes. A cluster is defined as "Balanced" if it meets one of two criteria:
1. It is monochromatic (all four nodes are in the same state).
2. It follows a checkerboard pattern (diagonal nodes are in the same state, but adjacent nodes are in opposite states).

The system has been configured such that there are currently no monochromatic $2 \times 2$ clusters anywhere on the board. 

Let $S$ be the total number of Balanced clusters in the grid. Given the perimeter constraint and the absence of monochromatic clusters, what is the minimum possible value of $S$?

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
