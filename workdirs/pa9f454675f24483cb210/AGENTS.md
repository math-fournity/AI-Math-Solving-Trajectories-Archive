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

In the center of a specialized hexagonal park (Hexagon $ABCDEF$), a surveyor stands at a specific point $P$. The park is a perfect regular hexagon. From point $P$, the surveyor measures the shortest direct distances (perpendiculars) to each of the six perimeter fences.

The measured distances to the northern fence $AB$, the northeastern fence $CD$, and the northwestern fence $EF$ are recorded as follows:
- The distance to fence $AB$ (at point $G$) is $PG = \frac{9}{2}$ units.
- The distance to fence $CD$ (at point $I$) is $PI = 6$ units.
- The distance to fence $EF$ (at point $K$) is $PK = \frac{15}{2}$ units.

The points $G$, $H$, $I$, $J$, $K$, and $L$ represent the feet of the perpendiculars from the surveyor at $P$ to the fences $AB$, $BC$, $CD$, $DE$, $EF$, and $FA$ respectively. The surveyor marks these six points and calculates the area of the interior hexagon $GHIJKL$ formed by connecting them in order.

The area of this interior hexagon $GHIJKL$ is expressed in the form $\frac{a\sqrt{b}}{c}$ for positive integers $a$, $b$, and $c$, where $a$ and $c$ are relatively prime and $b$ is square-free. Find the value of $a + b + c$.

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
