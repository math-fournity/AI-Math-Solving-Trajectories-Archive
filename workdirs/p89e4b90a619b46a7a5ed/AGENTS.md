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

15. There are 10 players $A_{1}, A_{2}, \cdots, A_{10}$, whose initial points are $9,8,7,6,5,4,3,2,1,0$, and their initial rankings are 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th. Now a round-robin tournament is held, meaning that every two players will play exactly one match, and each match must have a winner. If a higher-ranked player beats a lower-ranked player, the winner gets 1 point and the loser gets 0 points; if a lower-ranked player beats a higher-ranked player, the winner gets 2 points and the loser gets 0 points. After all matches are completed, the cumulative points of each player (the sum of the points from this round-robin tournament and their initial points) are calculated, and the players are re-ranked based on their cumulative points. Find the minimum possible cumulative points of the new champion (ties are allowed).

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
