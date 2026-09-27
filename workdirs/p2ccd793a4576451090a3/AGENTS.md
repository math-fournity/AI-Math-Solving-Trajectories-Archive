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

In a remote industrial complex, three specialized pressure valves are assigned capacity ratings denoted by the positive integers $x$, $y$, and $z$. These ratings must adhere to a strict safety protocol:

1.  **Total System Capacity:** The combined throughput of the entire system, calculated as the least common multiple of the three ratings, $[x, y, z]$, must exactly equal the sum of the redundant safety margins between pairs. Specifically, this value must equal the greatest common divisor of the first and second ratings, $(x, y)$, plus the greatest common divisor of the second and third ratings, $(y, z)$, plus the greatest common divisor of the third and first ratings, $(z, x)$.
2.  **Operational Hierarchy:** To ensure stability, the valves are calibrated such that the first rating is no greater than the second, and the second is no greater than the third ($x \le y \le z$).
3.  **Core Synchronization:** The system is "irreducible," meaning the greatest common divisor of all three ratings together is exactly 1; that is, $(x, y, z) = 1$.

Let $S$ be the set of all possible ordered integer triples $(x, y, z)$ that satisfy these industrial specifications. Your task is to find the total sum of all ratings across all valid configurations. Calculate the sum of all elements in all solution tuples in $S$, represented as $\sum_{(x, y, z) \in S} (x + y + z)$.

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
