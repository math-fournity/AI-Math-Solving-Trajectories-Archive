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

A futuristic city’s power grid is designed around a parabolic protective force field in a coordinate plane (measured in kilometers). This field is defined by the quadratic equation $Ax^2 + Bxy + Cy^2 + Dx + Ey + 4 = 0$, where the coefficients $A, B, C, D,$ and $E$ are integers. 

The edge of the field is precisely calibrated to touch two main power conduits: it is tangent to the horizontal $x$-axis at the point $(1,0)$ and tangent to the vertical $y$-axis at the point $(0,2)$. 

The central stabilizer of this field lies along the parabola’s axis of symmetry, described by the linear equation $ax + by = c$. In this design, $a, b,$ and $c$ are constants where $a$ is a positive integer such that the greatest common divisor of $a$ and the absolute value of $b$ is 1 ($\gcd(a, |b|) = 1$). 

At the very tip of the force field sits the emitter, located at the parabola's vertex $(x_v, y_v)$.

Calculate the sum of all the system parameters: $A + B + C + D + E + a + b + c + x_v + y_v$.

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
