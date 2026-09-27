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

A specialized tech laboratory is stress-testing seven different high-performance processing units, labeled $U_1, U_2, U_3, U_4, U_5, U_6,$ and $U_7$. The lab supervisor has scheduled three separate cooling-system test cycles, each lasting exactly 90 minutes. During these cycles, the main testing rig can only host one processing unit at a time. Every unit must be tested at some point, and collectively, they must account for the entire 270-minute duration across the three cycles.

The experimental design requires two specific conditions regarding the total accumulated run-time (measured in whole minutes) for the units:
1. The sum of the minutes logged by $U_1, U_2, U_3,$ and $U_4$ must be a multiple of 7.
2. The sum of the minutes logged by $U_5, U_6,$ and $U_7$ must be a multiple of 13.

Given that there is no limit to how many times the supervisor can swap units in or out of the rig, and assuming each unit's total time is a non-negative integer, how many different distributions of total run-times across the seven units are possible?

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
