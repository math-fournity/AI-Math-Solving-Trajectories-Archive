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

A metropolitan power grid is represented by a square circuit board of size $2n \times 2n$. Every cell on the board must be covered by a "Power Link," which is a component that occupies exactly two adjacent cells. There are two types of Power Links: Horizontal Links and Vertical Links.

The city engineers perform maintenance by rearranging these links according to the following strict operational protocols:

1. **Rotation Protocol:** If two Horizontal Links occupy a $2 \times 2$ area (one positioned directly above the other), they may be rotated $90$ degrees to become two Vertical Links side-by-side.
2. **Upward Displacement:** If there are two Vertical Links side-by-side and a single Horizontal Link is positioned directly above them (covering the top edges of both), the Horizontal Link can be shifted down two rows while the two Vertical Links are shifted up one row to occupy the space previously held by the Horizontal Link.
3. **Downward Displacement:** If there are two Vertical Links side-by-side and a single Horizontal Link is positioned directly below them (covering the bottom edges of both), the Horizontal Link can be shifted up two rows while the two Vertical Links are shifted down one row to occupy the space previously held by the Horizontal Link.

A configuration of the board is considered "Stable" if it is impossible to apply any of the three protocols listed above. 

Determine $N(n)$, the total number of unique Stable configurations possible for a board of size $2n \times 2n$ for any $n \ge 1$.

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
