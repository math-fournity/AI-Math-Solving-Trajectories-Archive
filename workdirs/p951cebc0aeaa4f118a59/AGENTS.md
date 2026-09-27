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

In a futuristic city, a square lot of land is defined by the coordinates $(0,0), (1,0), (1,1),$ and $(0,1)$. A developer is testing a series of architectural designs for a public park, indexed by a sensitivity parameter $\alpha$, where $0 < \alpha < 1$.

For a specific value of $\alpha$, the park $R(\alpha)$ is restricted by a specific "cut-off" zone. While the boundaries of the lot at $x=1$, $y=1$, and the segment of the y-axis between $y=1$ and $y=1-\alpha$ are always included, the bottom-left corner of the lot is truncated. Specifically, the boundary of the park $R(\alpha)$ is the convex pentagon formed by the vertices:
- $(0, 1-\alpha)$
- $(\alpha, 0)$
- $(1, 0)$
- $(1, 1)$
- $(0, 1)$

The city council decides that the only permanent structures allowed are those that fall within the "Universal Zone" $R$. This zone is defined as the area that remains part of the park regardless of which value of $\alpha$ is chosen between $0$ and $1$. In other words, a coordinate $(x, y)$ is in $R$ if and only if it is contained in $R(\alpha)$ for every possible $\alpha \in (0, 1)$.

Calculate the area of the Universal Zone $R$.

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
