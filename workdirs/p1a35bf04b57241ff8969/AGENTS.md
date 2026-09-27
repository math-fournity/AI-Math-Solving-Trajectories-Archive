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

In the competitive world of skyscraper architecture, two rival firms, Emerald Construction and Ruby Developers, are competing to fill a digital grid. A construction site consists of a foundation with $m$ designated plots arranged in a single row. The city's zoning laws dictate that no plot can ever exceed a height of $n$ stories.

The two firms take turns adding one floor at a time to the site. Emerald Construction always goes first, placing a green glass floor either directly on an empty foundation plot or on top of an existing floor, provided the height limit is not exceeded. Ruby Developers follows by placing a red steel floor under the same constraints.

Emerald Construction wins the contract if they can complete at least one "Emerald Level"—a specific height $h$ (where $h$ is a floor level from the 1st floor to the $n$-th floor) where all $m$ plots across the row are occupied by green glass floors. Ruby Developers wins if they can successfully prevent any such monochromatic level from being completed.

Let $S$ be the set of all pairs $(m, n)$ of positive integers, with $1 \le m \le 20$ and $1 \le n \le 20$, for which Emerald Construction has a guaranteed winning strategy regardless of Ruby's moves. Find the total number of elements in the set $S$.

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
