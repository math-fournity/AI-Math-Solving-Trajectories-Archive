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

In a remote territory, an expedition has established a perimeter defined by six supply depots arranged as the vertices of a convex hexagon, labeled $A, B, C, D, E,$ and $F$. To improve communication, the team constructs six relay towers, $A_1, B_1, C_1, D_1, E_1,$ and $F_1$, located exactly at the midpoints of the transport routes $AB, BC, CD, DE, EF,$ and $FA$ respectively.

The team scouts the internal route, which forms a smaller hexagonal loop connecting the towers $A_1 \to B_1 \to C_1 \to D_1 \to E_1 \to F_1 \to A_1$. Upon measurement, the engineers discover a unique geometric property: every internal angle of this tower-to-tower hexagonal loop is exactly equal.

Let $p$ represent the total length of the outer boundary connecting the original supply depots ($AB+BC+CD+DE+EF+FA$), and let $p_1$ represent the total length of the inner relay tower loop ($A_1B_1+B_1C_1+C_1D_1+D_1E_1+E_1F_1+F_1A_1$).

It is mathematically established that the ratio of these perimeters satisfies the inequality $p \geq k \cdot p_1$. Based on these constraints, what is the value of $k^2$?

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
