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

A high-tech server farm contains 16 storage drives, uniquely labeled 1 through 16. Each drive contains a specific amount of data measured in terabytes, corresponding to the powers of 2 from $2^1, 2^2, 2^3, \dots, 2^{16}$. The distribution of these data capacities among the drives is completely random.

An automated maintenance protocol runs for exactly eight cycles. In each cycle, you must first select one drive to move to your permanent archive (its contents remain unknown to the system, but you can see the data amount through a security exploit). Immediately after your selection, the system's "cleanup" script randomly selects one of the remaining available drives, reveals its data capacity to you, and permanently wipes it.

This process repeats for 8 cycles until you have archived 8 drives and the system has deleted 8 drives. Your total reward is the sum of the data capacities stored on the 8 drives you archived.

Assuming you use your knowledge of the values in each drive to maximize your total data according to an optimal strategy, what is the expected total amount of data you will collect?

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
