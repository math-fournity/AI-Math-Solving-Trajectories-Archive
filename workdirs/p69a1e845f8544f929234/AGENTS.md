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

A specialized urban planning commission is mapping out four key logistics hubs—the Junction ($J$), the Maintenance Depot ($M$), the Information Center ($I$), and the Terminal ($T$)—which all lie on a circular transit loop $\mathcal{K}$.

The positions of these hubs are determined by the layout of three primary delivery zones that form a triangle $ABC$. 
- The Information Center ($I$) is located at the center of the largest circle that can be inscribed within the triangular boundaries of $ABC$.
- The Junction ($J$) is located at the center of the circle that is tangent to the boundary $BC$ and the extensions of boundaries $AB$ and $AC$.
- The Maintenance Depot ($M$) is situated exactly at the midpoint of the boundary $BC$.
- To locate the Terminal ($T$), the planners first identified point $N$, the midpoint of the major arc $BAC$ on the circle passing through $A, B,$ and $C$. The Terminal ($T$) is then placed such that the original point $A$ is the midpoint of the straight line segment connecting $N$ and $T$.

The planners represent the precise GPS coordinates of these hubs as complex numbers $j, m, i,$ and $t$ on a coordinate plane. They need to calculate a specific Network Reliability Index $R$, defined by the cross-ratio of these four points:
$$R = \frac{(m-i)(t-j)}{(j-i)(t-m)}$$

Find the value of $R$.

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
