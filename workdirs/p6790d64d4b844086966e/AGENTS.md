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

In the competitive world of boutique logistics, a "Standard Package" is defined as any shipment that has exactly eight unique shipping routes (divisors) available for its delivery. For any such package, the lengths of these eight routes are listed in strictly increasing order as $d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8$.

A logistics manager discovers a specific class of shipments called "Priority-Red" packages. A package qualifies as Priority-Red if its fifth-shortest route length ($d_5$) is exactly 4 units less than three times its third-shortest route length ($d_3$). Mathematically, this is expressed by the efficiency constraint: $d_5 = 3d_3 - 4$.

The manager notes that a package with a total volume of $2014$ cubic units satisfies the Priority-Red criteria. To optimize warehouse space, the manager needs to identify all other potential Priority-Red packages with smaller volumes.

How many Priority-Red packages exist with a total volume strictly less than $2014$?

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
