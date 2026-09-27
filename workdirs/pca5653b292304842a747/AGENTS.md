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

A specialized logistics company manages $n$ storage hubs (where $n > 1$). They are testing two different distribution protocols for a specific chemical compound: Protocol A and Protocol B. Under these protocols, the volumes of the compound stored at the hubs are represented by non-negative values $a_1, a_2, \dots, a_n$ for Protocol A and $b_1, b_2, \dots, b_n$ for Protocol B.

The technical constraints of the storage system dictate the following:
1.  **Volume Parity:** The product of the volumes stored in all hubs must be identical for both protocols ($a_1 \cdot a_2 \cdot \dots \cdot a_n = b_1 \cdot b_2 \cdot \dots \cdot b_n$).
2.  **Unit Normalization:** Under Protocol B, the total sum of the volumes across all $n$ hubs must equal exactly 1 unit ($b_1 + b_2 + \dots + b_n = 1$).
3.  **Dispersion Constraint:** The "Total Pairwise Deviation" of Protocol A cannot exceed that of Protocol B. That is, the sum of the absolute differences between every possible pair of hub volumes in Protocol A is less than or equal to the sum of the absolute differences between every possible pair of hub volumes in Protocol B:
\[ \sum_{1 \leq i<j \leq n}\left|a_{i}-a_{j}\right| \leq \sum_{1 \leq i<j \leq n}\left|b_{i}-b_{j}\right| \]

Based on these constraints, determine the maximum possible total volume that can be stored across all hubs under Protocol A ($a_1 + a_2 + \dots + a_n$).

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
