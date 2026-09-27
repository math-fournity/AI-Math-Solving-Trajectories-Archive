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

In a remote industrial park, a rectangular plot of land labeled $ABCD$ occupies exactly $30$ acres. At each corner of the plot, a circular storage silo has been constructed. The silo at corner $A$ has a radius of $2$ miles; the silo at corner $B$ has a radius of $3$ miles; the silo at corner $C$ has a radius of $5$ miles; and the silo at corner $D$ has a radius of $4$ miles.

To secure the area, a perimeter of laser fencing is established using the common external tangents of the silos. Specifically, two straight laser lines are drawn as the external tangents connecting the silos at opposite corners $A$ and $C$. Another two straight laser lines are drawn as the external tangents connecting the silos at the remaining opposite corners $B$ and $D$.

The intersection of these four laser lines forms a quadrilateral security zone designated as $WXYZ$. The segments $\overline{WX}$ and $\overline{YZ}$ are the portions of the boundary lines that were derived from the tangents of the silos at $A$ and $C$. If the combined length of these two specific boundary segments, $\overline{WX} + \overline{YZ}$, is exactly $20$ miles, what is the total area of the quadrilateral security zone $WXYZ$ in square miles?

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
