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

In the futuristic city of Numeria, a massive power grid is structured as a $2022 \times 2022$ square grid of batteries. Initially, every battery has a charge level of $0$. A Grid Operator and a System Glitch interact with the grid in a series of turns, with the Operator acting first:

- In each turn, the Grid Operator selects exactly one battery cell. This action injects a pulse that increases the charge level by $1$ unit for that specific battery and all of its immediate neighbors (a maximum of nine batteries in total).
- Immediately following this, the System Glitch targets exactly four distinct battery cells on the grid. For each of these four batteries, if its charge level is currently greater than $0$, the charge is decreased by $1$ unit.

A battery is classified as "Overcharged" if its charge level reaches at least $10^{6}$ units. 

Determine the maximum value $K$ such that the Grid Operator can guarantee that at least $K$ batteries eventually become Overcharged, regardless of the strategy employed by the System Glitch.

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
