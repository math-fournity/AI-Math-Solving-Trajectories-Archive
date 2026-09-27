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

In a remote high-security server facility, there is a grid of 16 data storage bays arranged in a perfect 4-by-4 square. At the start of a system maintenance cycle, 15 of these bays are occupied by active server units, while exactly one bay remains empty.

The system administrator can perform a "data compression" maneuver to reduce the number of active units. This maneuver can only be executed under the following conditions:
1. The administrator must select three bays, $A, B,$ and $C$, that are located in the same horizontal row or the same vertical column.
2. Bay $A$ must be immediately adjacent to bay $B$, and bay $B$ must be immediately adjacent to bay $C$.
3. Initially, bays $A$ and $B$ must contain active server units, and bay $C$ must be empty.
4. When the maneuver is performed, the unit in bay $B$ is decommissioned and removed from the grid, while the unit in bay $A$ is physically transferred into the empty bay $C$.

The goal of the maintenance cycle is to continue performing these maneuvers until only one active server unit remains in the entire 16-bay grid. 

Depending on which of the 16 bays is chosen to be the empty one at the very beginning, it may or may not be possible to reach this final state of a single remaining unit. How many different locations for the initially empty bay allow for the successful reduction of the system to exactly one server unit?

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
