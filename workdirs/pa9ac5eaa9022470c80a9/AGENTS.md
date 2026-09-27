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

In the competitive world of professional coffee roasting, 14 roasters—all of different ages—entered a round-robin "Roast-Off." In this tournament, every roaster participated in exactly one head-to-head match against every other participant. 

The scoring for each match was strictly regulated: the winner of a duel earned 1 point, the loser earned 0 points, and in the event of a "perfect flavor profile tie," both roasters earned 1/2 point.

After all matches were completed, a final leaderboard was generated. To resolve cases where roasters finished with the same total points, a tie-breaking rule was applied: between any two players with the same score, the younger roaster was assigned the higher ranking.

Upon reviewing the final statistics, Jan, the tournament coordinator, observed a specific distribution: the combined total points of the top 3 ranked roasters was exactly equal to the combined total points of the bottom 9 ranked roasters. Simultaneously, Joerg, the head judge, noted that throughout the entire competition, the total number of matches ending in a tie was the maximum mathematically possible given the tournament's final point distribution.

Determine the total number of ties that occurred during the competition.

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
