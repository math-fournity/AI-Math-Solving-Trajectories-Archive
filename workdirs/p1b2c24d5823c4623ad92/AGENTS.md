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

In a bustling telecommunications hub, there are $n$ distinct fiber-optic cables ($n \ge 4$) laid out across a flat layout board. 

Engineers categorize the relationship between any two specific cables, let’s call them Cable A and Cable B, by looking at the remaining $n-2$ cables in the system. If at least two of these other cables physically cross over both Cable A and Cable B, the pair $\{A, B\}$ is classified as a "Synergistic Connection." However, if there are fewer than two cables that cross both A and B, the pair is instead classified as a "Fragmented Connection."

Note that when counting these connections, the order of the cables in a pair does not matter (the pair $\{A, B\}$ is the same as $\{B, A\}$).

After a full audit of the network, the Lead Architect discovers that the total number of "Synergistic Connections" among the $n$ cables is exactly 2012 greater than the total number of "Fragmented Connections."

Based on this network audit, what is the minimum possible value of $n$?

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
