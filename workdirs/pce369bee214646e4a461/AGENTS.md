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

In a specialized metallurgical research facility, engineers are testing a new composite material formed by 17 distinct micro-spheres. For each sphere $i$ (where $i = 1, 2, \ldots, 17$), let $a_i$ represent its radius in millimeters, where every $a_i$ is a positive real number.

The experimental environment imposes a strict structural constraint: the sum of the squares of all 17 radii must be exactly 24 square millimeters ($\sum_{i=1}^{17} a_i^2 = 24$). 

Additionally, a stability threshold exists based on the combined volumetric and linear properties of the spheres. If the sum of the cubes of the radii plus the sum of the radii is strictly less than a specific capacity constant $c$ ($\sum_{i=1}^{17} a_i^3 + \sum_{i=1}^{17} a_i < c$), the spheres must satisfy a "triple-link" geometric property. This property requires that any three radii $a_i, a_j, a_k$ (for $1 \le i < j < k \le 17$) must be able to form the sides of a non-degenerate triangle.

What is the largest value of the constant $c$ such that this triple-link geometric property is guaranteed to hold for any set of 17 radii satisfying the given constraints?

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
