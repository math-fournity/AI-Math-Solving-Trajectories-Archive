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

A high-security data center uses a circular sequence of $N$ encryption nodes to process a daily batch of data. On the first day, the lead engineer, Merlin, configures the nodes in an initial arrangement. 

From the second day onward, the daily procedure is as follows:
1. Merlin first chooses a specific arrangement for the $N$ nodes.
2. After Merlin’s setup, the system administrators are permitted to perform a sequence of local optimizations. They can swap the positions of any two nodes that are currently adjacent, provided that those two specific nodes were **not** adjacent in the original arrangement from the first day.

The system administrators want to reach a state where the circular order of the nodes is identical to an arrangement used on any previous day. If they can achieve this through their allowed swaps, the project concludes that evening.

Note that circular arrangements are considered identical if one can be rotated to match the other. Merlin is not part of the circular sequence.

What is the maximum number of days the project can last such that Merlin can definitely guarantee the meetings continue, regardless of how the administrators choose to swap the nodes?

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
