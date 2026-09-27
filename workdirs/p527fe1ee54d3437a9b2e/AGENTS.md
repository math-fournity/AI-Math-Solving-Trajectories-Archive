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

In a specialized corporate conglomerate, a massive "Global Innovation Project" is conducted among 20 different international branches. Within this group, a specific subset of $k$ branches are also designated as "Regional Hubs." 

The project operates on a round-robin schedule where every branch collaborates with every other branch exactly once. Each collaboration results in a performance rating: 2 points for a "High Success" rating, 1 point for a "Standard Success" rating, and 0 points for a "Baseline" rating.

The project maintains two separate leaderboards:
1. **The Global Leaderboard:** This includes the points from collaborations between all 20 branches.
2. **The Regional Leaderboard:** This only counts the points from collaborations where both participating branches are members of the $k$ Regional Hubs.

Determine the maximum possible value of $k$ such that one specific Regional Hub can finish with a point total that is strictly higher than any other Regional Hub on the Regional Leaderboard, while simultaneously finishing with a point total that is strictly lower than any other branch on the Global Leaderboard.

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
