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

In a specialized logistics hub, there are 8 distinct docking bays, numbered sequentially from 1 to 8. Eight automated delivery drones, also numbered 1 through 8, are currently parked in these bays, with each drone $n$ initially occupying the bay labeled with the same number $n$.

A software update requires a complete reassignment of the drones to the bays. You must calculate the total number of ways to redistribute the drones such that every drone is moved to a new bay, with exactly one drone per bay (a bijective mapping), under the following two strict operational protocols:

1.  **Parity Shift Protocol:** To prevent signal interference, every drone must be moved to a bay whose number has a different parity than the drone's own ID number. That is, if a drone’s ID $n$ is even, it must be moved to an odd-numbered bay; if its ID $n$ is odd, it must be moved to an even-numbered bay.
2.  **No Reciprocal Exchange Protocol:** To ensure a varied distribution, no two drones are allowed to swap bays with each other. Specifically, if drone $A$ is moved to the bay originally occupied by drone $B$, then drone $B$ cannot be moved to the bay originally occupied by drone $A$.

How many different valid reassignment configurations exist that satisfy both protocols?

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
