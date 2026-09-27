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

In a class of 35 students divided into two non-empty groups, sky-scrapers and blockheads, consider the following four statements:
1. Every sky-scraper is taller than every blockhead.
2. There are more blockheads shorter than the shortest sky-scraper than there are sky-scrapers shorter than the tallest blockhead.
3. There are more sky-scrapers who are taller than at least one blockhead than there are blockheads who are taller than at least one sky-scraper.
4. The average height of blockheads is lower than the average height of sky-scrapers.

For any two distinct statements $i$ and $j$ from the set $\{1, 2, 3, 4\}$, let $a_{i,j} = 1$ if statement $i$ implies statement $j$ for any distribution of heights, and $a_{i,j} = 0$ otherwise. Calculate the value of the sum $\sum_{i=1}^4 \sum_{j \neq i} a_{i,j}$.

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
