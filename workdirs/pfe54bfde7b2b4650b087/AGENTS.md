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

In a futuristic data-processing facility, a central security vault is shaped like a perfect regular pentagon. For structural stability, the facility was designed by extending all five wall lines of the vault, as well as the five lines formed by its internal diagonals, infinitely across a two-dimensional floor plan. These ten infinite lines intersect to divide the entire floor into various polygonal sectors. Some sectors are enclosed by walls on all sides, while others are "open-ended" hallways that lead infinitely away from the center.

A tiny maintenance drone begins its journey inside the central pentagonal vault. The drone operates on a specific movement protocol: every minute, it identifies all the boundary lines (edges) of its current sector. It selects one of these edges at random, with each edge having an equal probability of being chosen, and crosses it into the adjacent sector. 

If the drone ever enters one of the open-ended, unbounded sectors, it loses its signal and permanently deactivates. 

Consider the drone’s journey after it makes its very first move to leave the central vault. Let $x$ be the expected number of times the drone will return to and re-enter the central pentagonal vault before it eventually deactivates in an unbounded sector. 

Find the closest integer to $100x$.

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
