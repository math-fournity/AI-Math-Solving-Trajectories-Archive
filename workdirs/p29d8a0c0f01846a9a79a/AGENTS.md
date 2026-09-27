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

A logistics company, "Unitary Solutions," operates a fleet of transport drones indexed by their capacity levels, ranging from 1 unit up to a maximum level of $n$ units. Every available capacity level $M = \{1, 2, \dots, n\}$ is currently assigned to one of two distinct maintenance hangars, Hangar A or Hangar B, such that every level is serviced by exactly one hangar.

The company’s safety protocol requires that the hangars are organized such that no single hangar can fulfill a "Load Balance Equation." This equation is satisfied if a hangar contains ten drone capacity levels $x_1, x_2, \dots, x_{10}$ (not necessarily distinct) such that the sum of the first nine capacities exactly equals the tenth capacity:
$$x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9 = x_{10}$$

The Board of Directors wants to find the threshold $n$ where this protocol becomes impossible to follow. Specifically, they need to determine the smallest positive integer $n$ such that, regardless of how the $n$ capacity levels are distributed between the two hangars, there will always be at least one hangar containing ten levels that satisfy the Load Balance Equation.

Find $n$.

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
