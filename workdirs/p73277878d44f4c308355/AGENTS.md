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

A specialized automated logistics hub operates on a two-dimensional grid of storage slots identified by coordinates $(m, n)$, where $m$ and $n$ are positive integers. A robotic carrier starts at a specific slot $(m, n)$ and must reach the central processing terminal located at $(0, 0)$ by executing any sequence of the following three legal maneuvers:

1.  **Diagonal Retraction**: For any positive integer $z$, the carrier can move from its current position $(x, y)$ to $(x-z, y-z)$.
2.  **Horizontal Expansion**: The carrier can multiply its current x-coordinate by a scaling factor $p$, moving from $(x, y)$ to $(px, y)$.
3.  **Vertical Expansion**: The carrier can multiply its current y-coordinate by the same scaling factor $p$, moving from $(x, y)$ to $(x, py)$.

Let $S(p)$ be the set of all starting configurations $(m, n)$ from which the carrier can successfully reach the terminal $(0, 0)$ in a finite number of moves.

In a system where the scaling factor $p$ is exactly $7$, a diagnostic test is run on all possible starting positions $(m, n)$ within the range $1 \le m \le 100$ and $1 \le n \le 100$. Find the total number of such pairs $(m, n)$ that belong to the set $S(7)$.

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
