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

In the city of Gridland, an urban planning department is developing a rectangular park that spans exactly $n = 2025$ units wide (from $x=0$ to $x=2025$) and $m = 2023$ units deep (from $y=0$ to $y=2023$). The department has decided to partition the entire area of this park into $T$ distinct triangular garden plots.

The surveyors have established a strict classification for the boundaries (sides) of these plots:
- A boundary is "Standard" if it lies perfectly horizontal (on a line $y=k$ for some non-negative integer $k$) or perfectly vertical (on a line $x=j$ for some non-negative integer $j$).
- A boundary is "Irregular" if it does not follow these specific integer grid lines.

The layout of these plots must adhere to two strict zoning laws:
1. Every triangular plot must have at least one Standard boundary. Furthermore, the altitude of the triangle measured from that Standard boundary to the opposite vertex must be exactly 1 unit.
2. Every Irregular boundary must be internal to the park; specifically, any Irregular boundary must serve as a shared fence between exactly two adjacent triangular plots (no Irregular boundary can lie on the outer perimeter of the park).

Let $k$ represent the number of triangular plots that possess at least two Standard boundaries. Based on these constraints, what is the minimum possible value of $k$?

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
