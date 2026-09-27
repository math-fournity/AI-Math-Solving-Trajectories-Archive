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

In a specialized logistics hub, there are eight distinct docking bays numbered 1 through 8. An operations manager needs to assign eight different delivery vehicles—coded as $V_1, V_2, V_3, V_4, V_5, V_6, V_7,$ and $V_8$—to these eight bays. Each vehicle must be assigned to exactly one bay, and no two vehicles can share the same bay.

Due to size and equipment constraints, the vehicles are restricted to specific bays as follows:
- Vehicle $V_1$ can only be assigned to a bay numbered 1, 2, 3, 4, or 5.
- Vehicle $V_2$ can only be assigned to a bay numbered 1, 2, 3, 4, 5, or 6.
- Vehicle $V_3$ can only be assigned to a bay numbered 1, 2, 3, 4, 5, 6, or 7.
- Vehicle $V_4$ can only be assigned to a bay numbered 1, 2, 3, 4, 5, 6, 7, or 8.
- Vehicle $V_5$ can only be assigned to a bay numbered 1, 2, 3, 4, 5, 6, 7, or 8.
- Vehicle $V_6$ can only be assigned to a bay numbered 2, 3, 4, 5, 6, 7, or 8.
- Vehicle $V_7$ can only be assigned to a bay numbered 3, 4, 5, 6, 7, or 8.
- Vehicle $V_8$ can only be assigned to a bay numbered 4, 5, 6, 7, or 8.

How many different valid assignments of the eight vehicles to the eight docking bays are possible?

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
