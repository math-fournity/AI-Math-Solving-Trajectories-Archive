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

In a remote industrial outpost, two technicians, Unit A and Unit B, are conducting a sequence of five power-calibration tests. Each technician has been allocated exactly five power-regulator chips with fixed output levels of 1, 2, 3, 4, and 5 gigawatts (one chip of each level per person).

The calibration process consists of five discrete stages. In each stage, both technicians simultaneously select and install one of their remaining chips into a test socket. The power levels are compared:
- If Unit A’s chip has a strictly higher wattage than Unit B’s chip, Unit A is awarded 1 performance credit.
- If Unit B’s chip has a strictly higher wattage than Unit A’s chip, Unit B is awarded 1 performance credit.
- If both chips have the same wattage, no performance credits are awarded to either technician for that stage.

Once a chip is used in a stage, it is discarded and cannot be used again. After all five stages are complete and all chips have been used, the technician with the higher total number of performance credits is declared the winner of the calibration cycle. If they have an equal number of credits, the cycle ends in a draw.

Across all possible permutations of how these two sets of chips can be played against each other, what percentage of these outcomes results in a win for Unit A?

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
