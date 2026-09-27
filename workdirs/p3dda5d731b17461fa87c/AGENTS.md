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

An architect is designing a modular hexagonal plaza defined by six perimeter pillars labeled $A, B, C, D, E, F$. To ensure structural symmetry, each of the six straight walkways forming the perimeter of the plaza (segments $AB, BC, CD, DE, EF$, and $FA$) must have a length of exactly $1$ decameter, and the pillars must be positioned such that the resulting hexagon is convex.

To support a decorative central canopy, the architect must install six structural support beams. Each beam connects one of the perimeter pillars to a unique anchor point located strictly within the interior of the plaza ($A$ connects to $A_1$, $B$ to $B_1$, $C$ to $C_1$, $D$ to $D_1$, $E$ to $E_1$, and $F$ to $F_1$). For aesthetic consistency, every one of these six support beams must have an identical length of $a$ decameters. 

A critical safety constraint dictates that no two of these beams may cross or touch at any point along their lengths, except possibly at the pillars themselves (meaning no two segments $AA_1, BB_1, CC_1, DD_1, EE_1$, or $FF_1$ can share an interior point).

Find the largest real number $a$ for which such a configuration of the plaza and its internal beams is mathematically possible.

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
