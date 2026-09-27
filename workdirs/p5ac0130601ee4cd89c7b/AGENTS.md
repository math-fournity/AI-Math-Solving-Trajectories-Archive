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

In the city of Centuria, an architect is designing a massive plaza in the shape of a convex polygon with 101 distinct marble pedestals as vertices. To connect these pedestals, the architect has mapped out every possible straight-line walkway that does not follow the perimeter (the diagonals of the 101-gon).

The city council has decided to pave these walkways in two phases. In Phase A, they will select a specific number of walkways, denoted as $k$. In Phase B, all remaining walkways not chosen in Phase A will be paved.

The lead engineer issues a requirement: no matter how the 101 pedestals are positioned (as long as they form a convex 101-gon), the total combined length of the $k$ walkways selected in Phase A must be greater than or equal to the total combined length of all the walkways paved in Phase B. This must hold true regardless of which specific walkways are assigned to Phase A and which are assigned to Phase B.

What is the least positive integer $k$ that guarantees the sum of the lengths of the $k$ chosen walkways will always be at least the sum of the lengths of the remaining walkways?

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
