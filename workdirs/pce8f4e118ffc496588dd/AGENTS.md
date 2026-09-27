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

In a remote archipelago, there are 2013 communication towers arranged in a perfect circle. Each tower is currently emitting either a Blue signal or a Red signal. 

The network operates in synchronized "transmission cycles." At the start of each cycle, an automated satellite takes a snapshot of the entire ring to record the current signal status of every tower. Immediately following the snapshot, the towers update simultaneously according to a specific protocol: if a tower has at least one immediate neighbor (the tower directly to its left or right) emitting a different color signal than its own, that tower flips its signal color to match the color its neighbor currently has. (Note: If a tower's neighbors both have a different color than its own, but are the same as each other, it flips to that color. If its neighbors are different from each other—one same, one different—it flips to the different color. If both neighbors are already the same color as the tower, it remains unchanged).

Given an initial configuration of Blue and Red signals, the system continues these cycles indefinitely. What is the largest possible number of unique satellite snapshots that can be collected from a single starting arrangement?

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
