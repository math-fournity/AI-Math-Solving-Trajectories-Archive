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

Let \( M \) be a positive integer. At a party with 120 people, 30 wear red hats, 40 wear blue hats, and 50 wear green hats. Before the party begins, \( M \) pairs of people are friends. (Friendship is mutual.) Suppose also that no two friends wear the same colored hat to the party.

During the party, \( X \) and \( Y \) can become friends if and only if the following two conditions hold:
a) There exists a person \( Z \) such that \( X \) and \( Y \) are both friends with \( Z \). (The friendship(s) between \( Z, X \) and \( Z, Y \) could have been formed during the party.)
b) \( X \) and \( Y \) are not wearing the same colored hat.

Suppose the party lasts long enough so that all possible friendships are formed. Let \( M_{1} \) be the largest value of \( M \) such that regardless of which \( M \) pairs of people are friends before the party, there will always be at least one pair of people \( X \) and \( Y \) with different colored hats who are not friends after the party. Let \( M_{2} \) be the smallest value of \( M \) such that regardless of which \( M \) pairs of people are friends before the party, every pair of people \( X \) and \( Y \) with different colored hats are friends after the party. Find \( M_{1} + M_{2} \).

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
