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

In a large logistics warehouse, a floor manager oversees a 5-meter by 5-meter square zone divided into 1-meter by 1-meter floor tiles. The manager is implementing a tiered security protocol involving four nested containment areas:

1.  First, a 4-meter by 4-meter square "Sector" must be designated within the 5-meter by 5-meter zone.
2.  Second, a 3-meter by 3-meter square "Vault" must be designated within the previously chosen 4-meter by 4-meter Sector.
3.  Third, a 2-meter by 2-meter square "Safe" must be designated within the previously chosen 3-meter by 3-meter Vault.
4.  Finally, a 1-meter by 1-meter square "Lockbox" (a single floor tile) must be designated within the 2-meter by 2-meter Safe.

All designated squares must align perfectly with the boundaries of the 1-meter floor tiles. 

If the security protocol requires that the final 1-meter by 1-meter Lockbox must be the exact central tile of the original 5-meter by 5-meter zone, in how many distinct ways can the sequence of the four nested squares (Sector, Vault, Safe, and Lockbox) be chosen?

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
