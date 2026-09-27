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

A specialized laser surveillance system is monitored across a coordinate-mapped grid. At the center of the grid, two curved security perimeters are defined by the hyperbola $\Gamma: \frac{x^{2}}{3}-y^{2}=1$. An observer stands at a fixed location $P$ (which is not on the perimeters). From this point, the observer can cast a sensor beam $l$ that sweeps through the area. 

Let $\Omega_{p}$ be the set of all possible straight-line sensor beams passing through $P$ that intersect the perimeters at exactly two distinct points, $M$ and $N$. For any such beam $l$, the system calculates a "detection product" $f_{P}(l)$, defined as the product of the distances from the observer to the two intersection points: $f_{P}(l) = |PM| \cdot |PN|$.

A location $P$ is classified as a “Signal Core” if it satisfies two conditions:
1. There exists a specific sensor beam $l_0 \in \Omega_p$ such that its two intersection points with the perimeters lie on opposite sides of the vertical $y$-axis.
2. For every other possible sensor beam $l \in \Omega_p$ (where $l \neq l_0$), the detection product of that beam is strictly greater than the detection product of the specific beam: $f_{P}(l) > f_{P}(l_0)$.

Calculate the area of the region on the grid consisting of all possible "Signal Core" locations.

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
