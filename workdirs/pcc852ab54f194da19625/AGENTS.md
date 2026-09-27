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

In a futuristic city, an experimental racing track is designed in the shape of a perfect ellipse, defined by the coordinate equation $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ (where $a > b > 0$). The track features two high-frequency signal towers located at the ellipse's foci, $F_{1}$ (the western focus) and $F_{2}$ (the eastern focus).

A straight maintenance cable connects two points on the track, $A$ and $B$, passing directly through the eastern signal tower $F_{2}$. Technical sensors indicate that the distance from point $A$ to the tower $F_{2}$ is exactly twice the distance from the tower $F_{2}$ to point $B$ ($|AF_{2}|=2|F_{2}B|$). Furthermore, a surveyor at the western tower $F_{1}$ measures the visual angle between the two cable ends, determining that $\tan \angle AF_{1}B = \frac{3}{4}$.

Let $e$ represent the eccentricity of this elliptical track. If the triangular region formed by the western tower $F_{1}$, the eastern tower $F_{2}$, and the cable endpoint $B$ covers an area of exactly 2 square units, calculate the value of the design constant given by $a^2 + b^2 + 100e^2$.

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
