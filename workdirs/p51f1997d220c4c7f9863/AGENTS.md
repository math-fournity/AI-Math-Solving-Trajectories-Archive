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

In a large logistics hub, a digital grid is used to manage shipping costs across a rectangular terminal consisting of 100 rows and 200 columns. To initialize the system, a computer randomly selects 100 distinct positive integers $a_1, a_2, \dots, a_{100}$ from the set $\{1, 2, \dots, 2016\}$ to serve as "row tariffs." Similarly, it randomly selects 200 distinct positive integers $b_1, b_2, \dots, b_{200}$ from the same set $\{1, 2, \dots, 2016\}$ to serve as "column tariffs." The processing cost for any specific bay located at the intersection of row $i$ and column $j$ is calculated as the sum of its tariffs: $a_i + b_j$.

An automated transport bot must travel from bay $(1, 1)$ to bay $(100, 200)$. The bot moves through the grid one bay at a time. From its current bay, it can move to any of the eight surrounding bays (horizontally, vertically, or diagonally). The total cost of a path is defined as the sum of the processing costs of every bay the bot enters, including the starting bay $(1, 1)$ and the destination bay $(100, 200)$.

Let $M$ be the minimum possible total cost for a valid path from the start to the destination. If the expected value of $M$ is expressed as a simplified fraction $\frac{p}{q}$, find the value of $p + q$.

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
