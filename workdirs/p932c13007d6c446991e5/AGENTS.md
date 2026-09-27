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

In the competitive world of high-stakes coffee roasting, a group of $n$ artisanal roasters (where $n > 1$) is competing in a grand tournament consisting of 12 distinct roasting rounds. In each round, every roaster produces a unique blend, and a panel of judges ranks them from 1st place down to $n$-th place based on flavor profile.

The tournament uses a fixed scoring system $(a_1, a_2, \ldots, a_n)$ where $a_1 \ge a_2 \ge \dots \ge a_n$. For every round, the roaster ranked 1st receives $a_1$ points, the roaster ranked 2nd receives $a_2$ points, and so on, down to the $n$-th ranked roaster who receives $a_n$ points. After all 12 rounds are completed, the points for each roaster are summed. The roaster with the highest total score is awarded the title of "Master Roaster." If multiple roasters tie for the highest total score, all of them are named "Master Roasters."

The tournament directors are looking for a specific scenario: they want to find a set of point values $(a_1, a_2, \ldots, a_n)$ and a specific distribution of rankings for the first 11 rounds such that, regardless of how the roasters rank in the final 12th round, there will always be at least two "Master Roasters" crowned due to a tie in the final standings.

Determine the minimum number of roasters $n$ for which such a scoring system and preliminary ranking distribution exist.

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
