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

In a digital fabrication lab, a technician is programming a robotic cutter to carve a decorative "pixel-path" out of a rectangular grid of sensors. 

The lab has various rectangular sensor arrays of size $m \times n$, where $m$ and $n$ are integers such that $2 \le m, n \le 20$. Each array consists of $m \times n$ total sensors positioned at integer coordinates $(i, j)$ for $1 \le i \le m$ and $1 \le j \le n$. 

The technician's task is to create a single, continuous, non-self-intersecting closed path (a simple polygon) that satisfies four strict manufacturing constraints:
1. Every vertex of the path must be located exactly at one of the sensor positions in the $m \times n$ array.
2. Every single sensor in the $m \times n$ array must lie somewhere on the perimeter of the path.
3. Every turn the path makes must be a perfect right angle (either $90^{\circ}$ inward or $270^{\circ}$ inward).
4. Every straight segment of the path between two consecutive vertices must have a length of exactly $1$ unit or exactly $3$ units.

Let $V$ be the set of all possible pairs of dimensions $(m, n)$ within the given range for which such a path can successfully be constructed. 

Calculate the total number of pairs $(m, n)$ in $V$.

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
