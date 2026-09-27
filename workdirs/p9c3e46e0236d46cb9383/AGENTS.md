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

In a remote archipelago, there are 98 different circular islands. Each island $n$ is characterized by the number of docking ports it has, where $n$ ranges from 3 to 100 (specifically, $n \in \{3, 4, \dots, 100\}$). On each island, the $n$ docking ports are arranged in a perfect circle, and each port is connected to exactly two adjacent ports by a bridge, forming a ring of $n$ bridges.

Two engineers, Alpha and Beta, are competing to reinforce these bridges. They take turns selecting one unreinforced bridge at a time to upgrade with titanium. Alpha always takes the first turn.

The rules for reinforcement are strictly dictated by structural stability:
- Alpha (Player 1) can only reinforce a bridge if it currently has either zero or two adjacent bridges already reinforced.
- Beta (Player 2) can only reinforce a bridge if it currently has exactly one adjacent bridge already reinforced.

The competition continues on a single island until a player, on their turn, finds no bridges that satisfy their specific reinforcement rule. The player unable to make a move loses the game on that island. Both engineers are masters of game theory and always play with an optimal strategy to win.

Let $W(n)$ be a function representing the winner of the game on an island with $n$ bridges. Define $W(n) = 1$ if Alpha has a winning strategy for that island, and $W(n) = 2$ if Beta has a winning strategy.

Calculate the total sum of the winners' values across all islands: 
$\sum_{n=3}^{100} W(n)$

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
