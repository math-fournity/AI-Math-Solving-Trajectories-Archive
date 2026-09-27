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

In a specialized logistics warehouse, a technician manages a row of $n$ binary toggle switches. Each switch can be set to "Active" (A) or "Inactive" (I). The technician follows a specific automated protocol: at each step, he counts the total number of Active switches currently in the row. If that count is $k > 0$, he toggles the state of the $k$-th switch from the left (changing A to I or I to A). If the count $k$ is 0, all switches are Inactive, and the process terminates.

For instance, if there are $n=3$ switches and the starting configuration is $IAI$, the sequence of operations is:
1. Count is 1 ($k=1$): Toggle the 1st switch $\to$ $AAI$.
2. Count is 2 ($k=2$): Toggle the 2nd switch $\to$ $AII$.
3. Count is 1 ($k=1$): Toggle the 1st switch $\to$ $III$.
The process stops after $L(IAI) = 3$ operations.

Let $A(n)$ represent the arithmetic mean of the number of operations $L(C)$ required to stop, calculated over all $2^n$ possible initial configurations $C$ for a fixed row length $n$. 

Calculate the value of the sum:
$$\sum_{n=1}^{10} A(n)$$

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
