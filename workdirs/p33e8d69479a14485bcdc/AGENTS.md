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

In a vast desert, a logistics company is establishing four specialized communication zones. 

The main boundary of the operation is a massive elliptical perimeter, designated as Zone A. The two primary signal towers, North Station and South Station, are located at the ellipse's focal points, situated at coordinates $(-4, 0)$ and $(4, 0)$ respectively.

Three circular support sectors are constructed within this layout:
- Sector B is a circular zone centered exactly at the North Station $(-4, 0)$ and its edge perfectly touches the elliptical perimeter of Zone A.
- Sector C is a circular zone centered exactly at the South Station $(4, 0)$ and its edge also perfectly touches the elliptical perimeter of Zone A.
- Sector D is a circular zone centered at the origin $(0, 0)$. This sector is designed such that its edge is simultaneously tangent to the elliptical perimeter of Zone A, the edge of Sector B, and the edge of Sector C.

A final emergency relay hub must be placed such that it is circular and its outer boundary is tangent to the elliptical perimeter of Zone A, the boundary of Sector C, and the boundary of Sector D. 

What is the radius of this emergency relay hub?

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
