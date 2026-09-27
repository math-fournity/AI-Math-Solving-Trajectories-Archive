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

In a specialized logistics hub, high-tech modular floor tiles are designed as unit squares. Each tile features a distinct data-link connector on each of its four edges, color-coded with one of four colors: Red (R), Yellow (Y), Blue (B), and Green (G). A tile is only valid if all four of its edges feature different colors.

These tiles are used to assemble large $m \times n$ rectangular grids. The assembly process follows two strict physical constraints:
1. **Internal Connectivity:** Two tiles can only be placed side-by-side if the edges being joined share the exact same color.
2. **External Insulation:** To prevent interference, the completed $m \times n$ rectangle must be "externally monochromatic." This means all edges on the top boundary of the rectangle must be the same color, all edges on the bottom boundary must be the same color, all edges on the left boundary must be the same color, and all edges on the right boundary must be the same color. 
3. **Boundary Diversity:** The four colors chosen for the four boundaries (Top, Bottom, Left, and Right) must be distinct from one another.

Let $m$ and $n$ represent the number of tiles along the length and width of such a rectangle. Based on the constraints required for a valid assembly, determine the necessary condition that $m$ and $n$ must satisfy. Applying this condition, calculate the total number of integer pairs $(m, n)$ such that $1 \le m \le 100$ and $1 \le n \le 100$ for which a valid rectangle can be constructed.

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
