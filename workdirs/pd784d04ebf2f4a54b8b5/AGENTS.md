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

In a specialized semiconductor fabrication facility, engineers are designing microchip layouts on rectangular grids of size $m \times n$, where both $m$ and $n$ are dimensions ranging from 2 to 20 units inclusive. To optimize the circuitry, each grid must be perfectly partitioned into two specific types of modular components without any gaps or overlapping:

1.  **The Quad-Core Module:** A square component that occupies a $2 \times 2$ area (4 units).
2.  **The Penta-L Module:** An L-shaped component that occupies 5 units. This component is shaped like a $3 \times 3$ square but is missing its upper-right $2 \times 2$ section.

The components are flexible in their orientation and can be rotated by 90, 180, or 270 degrees to fit the layout. 

A specific grid dimension pair $(m, n)$ is classified as "efficient" if it is possible to completely cover the $m \times n$ area using any combination of these two module types. Let $S$ represent the set of all such "efficient" pairs $(m, n)$ within the constraints $2 \leq m \leq 20$ and $2 \leq n \leq 20$. 

Calculate the total number of unique elements in set $S$.

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
