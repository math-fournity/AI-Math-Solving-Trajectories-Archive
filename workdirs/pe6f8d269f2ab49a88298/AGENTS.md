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

In the high-tech logistics hub of Sector 5, a sequence of automated transport ships is being loaded for a deep-space mission. Each ship is modeled as a vertical column of 5 storage bays. Every bay must be loaded with one of two types of cargo: a "Type 0" fuel cell or a "Type 1" power core.

The mission commander dictates that a fleet of $n$ ships (where $n$ is a natural number) is considered "stable" if there exist 3 specific ships in the fleet and 3 specific bay levels (out of the 5 possible levels) such that all 9 resulting intersection points across those 3 ships and 3 levels contain the exact same type of cargo.

The central computer determines that there exists a specific threshold value $m$. If the size of the fleet $n$ satisfies the inequality $n^3 \geq m$, then no matter how the cargo is distributed among the bays of the $n$ ships, the fleet is guaranteed to be "stable."

Find the smallest natural number $m$ such that every possible cargo configuration of a fleet with $n$ ships, where $n^3 \geq m$, must be stable.

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
