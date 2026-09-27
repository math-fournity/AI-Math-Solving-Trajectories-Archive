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

In a remote archipelago, two architects, Captain Liora and Commander Jace, are competing to establish outposts on an $m \times n$ grid of islands, where both $m$ and $n$ are integers greater than 2.

The competition follows these strict protocols:
1. Captain Liora begins the expedition by building a "Cavalier Outpost" on any island of her choice.
2. Commander Jace must then build a "Regent Outpost" on an unoccupied island that is exactly a $(1, 2)$ or $(2, 1)$ jump away from the Cavalier Outpost Liora just built (moving like a chess knight).
3. Captain Liora must then build a new "Cavalier Outpost" on an unoccupied island that lies in the same row, column, or diagonal as the Regent Outpost Jace just built (moving like a chess queen).
4. The architects continue to take turns under these specific movement constraints (Jace always moving relative to Liora’s last placement, and Liora always moving relative to Jace’s last placement).
5. An architect loses the game if they are unable to place their respective outpost on an empty island according to their movement rule.

Let $L(m, n) = 1$ if Captain Liora has a winning strategy for a grid of size $m \times n$, and $L(m, n) = 0$ if Commander Jace has a winning strategy.

Calculate the sum of $L(m, n)$ for all integer pairs $(m, n)$ such that $3 \le m \le 20$ and $3 \le n \le 20$.

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
