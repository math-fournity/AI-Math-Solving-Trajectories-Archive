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

In a sprawling logistics hub, a robotic sorter is programmed to navigate a 10-row by 10-column grid of 100 storage bays. The robot must perform a "full inventory sweep," meaning it moves from one bay to an adjacent bay (sharing a wall) at each step, visiting every single one of the 100 bays exactly once.

The facility has a "Main Transit Line" consisting of the 10 bays located along a single main diagonal (a line of bays connecting two opposite corners of the grid). 

Engineers are monitoring the robot’s efficiency regarding this transit line. They are specifically looking for a "Re-entry Event," defined as a sequence of three consecutive squares in the robot's path ($B_1, B_2, B_3$) such that:
1. The robot is currently at a bay $B_1$ located on the Main Transit Line.
2. In the next step, it moves to a bay $B_2$ that is NOT on the Main Transit Line.
3. In the very next step, it moves to a bay $B_3$ that IS back on the Main Transit Line.

Let $S$ be the total number of such "Re-entry Events" that occur during the robot's entire 100-bay path. 

Considering all possible starting bays, all possible valid paths that visit every bay once, and either of the two main diagonals, determine the minimum possible value of $S$.

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
