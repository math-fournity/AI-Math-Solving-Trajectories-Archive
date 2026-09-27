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

An architectural firm is designing a rectangular stained-glass mural for a gallery floor. The mural occupies a region on a grid-lined workspace with corners at $(0,0), (11,0), (0,13)$, and $(11,13)$. This $11 \times 13$ rectangle is divided into several smaller triangular glass panes according to two strict structural rules:

1. Every triangle in the mural must have at least one "primary edge." A primary edge is defined as a side that lies exactly on one of the grid lines $x=j$ or $y=k$ (where $j$ and $k$ are integers). Furthermore, the height of the triangle measured perpendicularly from this primary edge to the opposite vertex must be exactly $1$ unit.
2. Any side of a triangle that is not a primary edge is considered a "secondary edge." To ensure structural integrity, every secondary edge must be a shared boundary between exactly two adjacent triangles.

The lead designer identifies specific triangles that are particularly sturdy: those that possess at least two primary edges. 

Let $N$ be the total number of such sturdy triangles used to complete the partition of the $11 \times 13$ mural. Determine the minimum possible value of $N$.

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
