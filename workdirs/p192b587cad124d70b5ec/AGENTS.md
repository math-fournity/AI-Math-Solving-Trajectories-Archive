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

A specialized cargo drone is programmed to deliver supplies to a colony on a distant planet. The drone’s navigation system operates on a circular dial with $n$ discrete sectors, labeled $0, 1, 2, \ldots, n-1$. The drone starts at sector $1$. Two remote operators, Ariane and Bérénice, take turns inputting commands to move the drone’s position $x$. Ariane always takes the first turn.

On any given turn, the current operator must choose one of two commands:
1.  **Inching:** Move the drone to the next sector, $(x+1) \pmod n$.
2.  **Boosting:** Double the drone’s current sector index, $(2x) \pmod n$.

Ariane’s objective is to force the drone to land on the "Home Base" located at sector $0$. Bérénice’s objective is to use her turns to ensure the drone never reaches sector $0$, no matter how many moves are made. Both operators play with perfect logic and foresight.

Let $S$ be the set of all integers $n$ in the range $2 \le n \le 100$ for which Ariane has a guaranteed strategy to reach sector $0$ and win the game.

Find the sum of all the elements in $S$.

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
