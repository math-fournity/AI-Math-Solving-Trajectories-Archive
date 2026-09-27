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

In a remote industrial mining complex, an excavation zone is shaped like a truncated triangular pyramid. The lower horizontal floor is defined by a triangular boundary $ABC$, and the upper horizontal ceiling is defined by triangle $A_1B_1C_1$, such that the floor and ceiling are parallel. Three structural support pillars, $AA_1$, $BB_1$, and $CC_1$, connect the corners.

The pillar $AA_1$ is perfectly vertical, standing perpendicular to the floor $ABC$. A safety sensor is mounted at point $N$ on pillar $AA_1$ such that the distance from the floor to the sensor ($AN$) and the distance from the sensor to the ceiling ($NA_1$) are in a ratio of $1:2$.

The maintenance crew has noted that the diagonal cross-section formed by the points $B$, $B_1$, and $C$ creates a perfect equilateral triangle. A spherical scanning field $\Omega$ with a radius of $R = \sqrt{5}$ units is generated to monitor the zone; this field passes exactly through the points $B$, $B_1$, and $C$, and it is tangent to the vertical pillar $AA_1$ precisely at the sensor location $N$.

Surveyors have measured the floor layout and determined that the interior angle $\angle ABC$ has a value of $\arccos \sqrt{\frac{2}{5}}$.

Let $L$ represent the length of the support pillar $BB_1$.
Let $\theta$ represent the angle (measured in radians) between the vertical pillar $AA_1$ and the slanted plane defined by the points $B, B_1, C$.
Let $x$ represent the length of the ceiling edge $A_1B_1$.

Calculate the total structural rating given by the formula:
$$L^2 + \frac{4\theta}{\pi} + (2-x)^2$$

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
