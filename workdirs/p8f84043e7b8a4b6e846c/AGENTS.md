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

In a remote territory, three specialized research stations—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. Strategic surveyors have mapped the distances between them: the path from Alpha to Bravo ($AB$) is 13 kilometers, the path from Bravo to Charlie ($BC$) is 14 kilometers, and the path from Charlie to Alpha ($CA$) is 15 kilometers.

The central command hub, denoted as the "Heat-Sync" ($H$), is located at the unique point where the three altitudes of the triangle $ABC$ intersect. This hub is used to coordinate three overlapping circular satellite coverage zones. Specifically, there are three distinct circular zones:
1. The first zone is defined by the circle passing through stations Alpha, Heat-Sync, and Bravo.
2. The second zone is defined by the circle passing through stations Bravo, Heat-Sync, and Charlie.
3. The third zone is defined by the circle passing through stations Charlie, Heat-Sync, and Alpha.

The regional communications director wants to place a new circular signal booster area that is tangent to all three of these satellite coverage zones. While there is a trivial point of intersection at the hub itself, the director requires a booster area with a nonzero radius.

If the radius of this signal booster area is expressed as an irreducible fraction $\frac{a}{b}$, compute the value of $a + b$.

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
