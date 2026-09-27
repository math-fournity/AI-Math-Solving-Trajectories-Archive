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

In a futuristic circular city, there are $2n+1$ power stations arranged as the vertices of a regular polygon, labeled $S_1, S_2, \dots, S_{2n+1}$. A telecommunications company wants to build a "Sub-Network" by selecting exactly $m$ stations from these $2n+1$ locations to serve as nodes for a convex $m$-sided transmission loop. 

A Sub-Network is classified as "High-Frequency" if at least one of its $m$ interior angles is acute (strictly less than 90 degrees). Let $N(n, m)$ represent the total number of unique ways to select a set of $m$ stations that form a High-Frequency Sub-Network, where $n \geq m \geq 5$ are integers.

Calculate the sum of the number of possible High-Frequency Sub-Networks when $n=6, m=5$ and when $n=7, m=5$. That is, find the value of $N(6, 5) + N(7, 5)$.

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
