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

Karl starts with $n$ cards labeled $1,2, \ldots, n$ lined up in random order on his desk. He calls a pair $(a, b)$ of cards swapped if $a>b$ and the card labeled $a$ is to the left of the card labeled $b$. Karl picks up the card labeled 1 and inserts it back into the sequence in the opposite position: if the card labeled 1 had $i$ cards to its left, then it now has $i$ cards to its right. He then picks up the card labeled 2 and reinserts it in the same manner, and so on, until he has picked up and put back each of the cards $1, \ldots, n$ exactly once in that order. For example, if $n=4$, then one example of a process is  $$ 3142 \longrightarrow 3412 \longrightarrow 2341 \longrightarrow 2431 \longrightarrow 2341 $$  which has three swapped pairs both before and after. Show that, no matter what lineup of cards Karl started with, his final lineup has the same number of swapped pairs as the starting lineup.

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
