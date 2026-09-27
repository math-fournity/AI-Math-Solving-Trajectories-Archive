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

A specialized environmental sensor measures the concentration of a rare pollutant, $p$, across a 2D grid based on horizontal distance $x$ and vertical distance $y$. The concentration is modeled by a general cubic bivariate polynomial:
\[ p(x,y) = a_0 + a_1x + a_2y + a_3x^2 + a_4xy + a_5y^2 + a_6x^3 + a_7x^2y + a_8xy^2 + a_9y^3 \]
During a field study, researchers discover that the pollutant concentration is exactly zero at eight specific survey coordinates: $(0,0)$, $(1,0)$, $(-1,0)$, $(0,1)$, $(0,-1)$, $(1,1)$, $(1,-1)$, and $(2,2)$.

Mathematical analysis reveals that there exists one additional fixed coordinate $(x_f, y_f)$, distinct from the eight listed above, where the pollutant concentration is guaranteed to be zero regardless of the specific coefficients $a_i$ chosen for the model. 

This fixed point can be expressed as a coordinate of fractions $\left(\frac{a}{c}, \frac{b}{c}\right)$, where $a, b,$ and $c$ are positive integers, the fraction $\frac{a}{c}$ is in simplest form ($\gcd(a,c)=1$), and $c > 1$. Calculate the value of $a + b + c$.

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
