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

A specialized architectural firm is designing a luxury compound surrounded by $n$ straight security walls ($n \geq 3$), forming a convex $n$-sided perimeter. The corners of the compound are designated as observation posts $A_1, A_2, \dots, A_n$ in clockwise order.

For any specific post $A_i$, the security team defines a "Strategic Pivot Point" located exactly halfway along the straight-line patrol path connecting its two immediate neighbors, $A_{i-1}$ and $A_{i+1}$ (where $A_0$ is defined as $A_n$ and $A_{n+1}$ is defined as $A_1$). 

A post $A_i$ is classified as "Centrally Shielded" if the point reached by starting at $A_i$ and moving through the Strategic Pivot Point to a position exactly twice as far from $A_i$ as the pivot point is (the reflection of $A_i$ across the midpoint) falls within the compound's enclosed area or exactly on its perimeter.

In terms of $n$, what is the minimum number of Centrally Shielded posts that such a convex $n$-sided compound must possess?

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
