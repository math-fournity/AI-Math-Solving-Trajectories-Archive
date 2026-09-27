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

In a specialized shipping port, there are $n$ cargo ships docked in a row and $n$ destination warehouses lined up on a pier. Let $n$ be a positive integer. We define a distribution plan $f$ that assigns a certain number of shipping containers from each ship $x$ to each warehouse $y$, where $x$ and $y$ are integers such that $1 \leq x, y \leq n$.

The distribution plan must adhere to the following strict logistics protocols:
- The number of containers sent from any ship $x$ to any warehouse $y$, denoted as $f(x, y)$, must be a non-negative integer.
- Each of the $n$ ships carries exactly $n - 1$ containers, all of which must be distributed among the $n$ warehouses.
- To prevent the crossing of transport cranes and ensure safety, the logistics must be "non-crossing": for any two assignments where containers are actually moved (i.e., $f(x_1, y_1) > 0$ and $f(x_2, y_2) > 0$), it is forbidden for a ship further down the row to send goods to a warehouse earlier on the pier. That is, if $x_1 < x_2$, then it must be that $y_1 \leq y_2$.

Let $N(n)$ be the total number of distinct valid distribution plans that satisfy these protocols. Calculate the explicit value of $N(4)$.

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
