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

A specialized urban planning committee is tasked with designing a "dual-sector expansion zone" for a city. The core of the zone is an existing community park, represented by a convex polygon $P$ with a total land area of exactly $1$ unit. 

The committee plans to build a secondary "mirror district" $Q$. This district must be an exact duplicate of the park $P$, but rotated 180 degrees (centrally symmetric) around a single central hub point $M$ located anywhere on the city map. To ensure the project is cohesive, the city must also acquire all the land situated between the original park $P$ and the new district $Q$ to form a single, unified convex development zone (the convex hull of $P \cup Q$).

The lead architect needs to determine the minimum possible value $\alpha$ such that, no matter what shape the original convex park $P$ takes, there will always exist at least one location for the hub $M$ that keeps the total area of the unified convex development zone at or below $\alpha$ units.

Find the smallest real number $\alpha$ that satisfies this requirement for any possible convex park of area $1$.

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
