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

In a specialized digital manufacturing grid, a robotic arm operates on a square workspace defined by a coordinate system. The grid contains $4n^2$ specific anchor points, where $n$ is a fixed positive integer. These points are defined as all locations $(x, y)$ where both $x$ and $y$ are non-negative integers strictly less than $2n$.

A designer is tasked with partitioning all $4n^2$ anchor points into a collection of polygons. To ensure structural integrity, the following rules must be followed:
1. Every single anchor point in the grid must be used as a vertex for exactly one polygon.
2. The vertices of every polygon must be chosen from the set of anchor points.
3. The polygons do not need to be of the same type (they can be triangles, quadrilaterals, or any other polygon), provided every point is accounted for as a vertex.

The efficiency of the manufacturing layout is measured by the total area covered by all the polygons in the collection. Given the fixed integer $n$, calculate the maximum possible value for the sum of the areas of all polygons in the set.

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
