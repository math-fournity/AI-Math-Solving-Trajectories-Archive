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

In the high-stakes world of digital logistics, two competing algorithms, Max (the "Requester") and Min (the "Assigner"), are determining the final output of a specialized subtraction engine. The engine consists of two four-digit memory registers, represented as:
$$[A_1][A_2][A_3][A_4] - [B_1][B_2][B_3][B_4]$$
There are exactly 8 empty slots waiting to be filled. The process follows these rules:
1. The game lasts exactly 8 turns.
2. In each turn, Max chooses any single digit from the set $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.
3. Immediately after a digit is chosen, Min chooses one of the remaining empty slots to place that digit.
4. Once a digit is placed, it cannot be moved.

Max’s objective is to force the digits into a configuration that results in the largest possible non-negative difference. Min’s objective is to assign the digits provided by Max to the slots in a way that results in the smallest possible non-negative difference.

If both algorithms operate with perfect logic to achieve their respective goals, what will be the final value of the subtraction $(A_1 A_2 A_3 A_4) - (B_1 B_2 B_3 B_4)$ at the end of the 8 turns?

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
