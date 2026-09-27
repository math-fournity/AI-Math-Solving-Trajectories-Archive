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

A specialized satellite $A$ is orbiting a deep-space anomaly following a trajectory defined by the hyperbolic function $y = \frac{2011}{x}$, where $x$ and $y$ represent spatial coordinates in megameters. In the same sector, a planetary body occupies an elliptical region defined by the equation $\frac{x^{2}}{25} + \frac{y^{2}}{9} = 1$.

The satellite $A$ projects two laser beams, $AP$ and $AQ$, which are perfectly tangent to the surface of the elliptical planet at contact points $P$ and $Q$, respectively. Deep within the planet's interior lies a unique magnetic core located at the ellipse's left focus, denoted as $F$.

The mission control needs to calculate the efficiency of the gravitational interaction between the satellite, the contact points, and the core. As the satellite $A$ moves along its hyperbolic path, the distances between these points change. Determine the minimum possible value of the ratio:
$$\frac{|AF|^{2}}{|PF| \cdot |QF|}$$

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
