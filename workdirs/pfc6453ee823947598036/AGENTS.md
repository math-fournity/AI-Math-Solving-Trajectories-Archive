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

In a massive industrial simulation, 200 autonomous processing units are undergoing a long-term efficiency trial. Every 24-hour cycle, each unit is tasked with a single computational duel against another unit. At the end of each duel, the unit that completes the task faster is awarded 1 energy credit, while the slower unit receives 0 credits.

To ensure competitive parity throughout the trial, the pairing protocol is reset every morning: all 200 units are ranked from 1st to 200th based on their cumulative energy credits earned since the start of the simulation. They are then matched into 100 specific pairs based on this leaderboard: the 1st ranked unit faces the 2nd, the 3rd faces the 4th, and so on, down to the 199th facing the 200th.

Engineers are monitoring the "credit gap"—the difference in cumulative energy credits between any two units in the simulation. They have determined that there is a specific threshold $D$ such that, regardless of the individual outcomes of the duels, the difference in credits between some pair of units is guaranteed to eventually exceed $D$ if the simulation runs for enough cycles.

Based on an analysis of the stability of the credit sums within these adjacent leaderboard pairs, find the value of $D$.

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
