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

A specialized circular conservation zone, $\Gamma$, is managed from a central research hub, $I$. The zone is inscribed within a larger triangular territory defined by three observation outposts: Alpha ($A$), Beta ($B$), and Gamma ($C$). The distances between these outposts are exactly 5 kilometers between Alpha and Beta ($AB=5$), 6 kilometers between Beta and Gamma ($BC=6$), and 7 kilometers between Gamma and Alpha ($CA=7$).

Regional planners have established three circular surveillance sectors. The first sector is the unique circle passing through outposts Beta, Gamma, and the central hub $I$. This sector's boundary intersects the edge of the conservation zone $\Gamma$ at two specific points, which define a straight seismic sensor line $\overline{X_1 X_2}$. The second sector is the circle passing through Gamma, Alpha, and hub $I$, whose intersection with the edge of $\Gamma$ defines a second sensor line $\overline{Y_1 Y_2}$. The third sector is the circle passing through Alpha, Beta, and hub $I$, whose intersection with the edge of $\Gamma$ defines a third sensor line $\overline{Z_1 Z_2}$.

These three sensor lines—$\overline{X_1 X_2}$, $\overline{Y_1 Y_2}$, and $\overline{Z_1 Z_2}$—are extended until they intersect one another, forming a triangular restricted area in the heart of the zone. The area of this newly formed triangle is expressed in the form $\frac{m \sqrt{p}}{n}$ square kilometers for positive integers $m, n,$ and $p$, where $m$ and $n$ are relatively prime and $p$ is squarefree. 

Compute the value of $m+n+p$.

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
