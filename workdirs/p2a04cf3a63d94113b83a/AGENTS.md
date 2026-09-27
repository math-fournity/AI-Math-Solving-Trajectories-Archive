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

In a specialized logistics network, four high-security warehouses are identified by their unique encryption keys: $a, b, c,$ and $d$. To ensure maximum security, each key must be a prime number. Furthermore, the security protocol mandates specific minimum capacities for three of the warehouses: Warehouse $a$ must have a key greater than 3, Warehouse $b$ must have a key greater than 6, and Warehouse $c$ must have a key greater than 12. There is no such restriction on the key for Warehouse $d$.

The network’s stability is governed by a precise energy balance equation based on the squares of these keys. The system requires that the sum of the squared keys of the first and third warehouses, minus the sum of the squared keys of the second and fourth warehouses, equals exactly 1749. Mathematically, this balance is expressed as:
\[a^2 - b^2 + c^2 - d^2 = 1749\]

A technician needs to calculate the total power load of the system to prepare for a maintenance cycle. This load is defined as the sum of the squares of all four encryption keys. Based on these configurations, determine all possible values for the total power load $a^2 + b^2 + c^2 + d^2$.

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
