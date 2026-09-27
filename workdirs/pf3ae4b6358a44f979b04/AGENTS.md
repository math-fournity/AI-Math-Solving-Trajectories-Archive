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

Discuss geometrically the general solution of \[\frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R}.\] For convenience, let us assume that in solving the given system we have obtained a pair of integrable equations \[P_1 dx + Q_1 dy + R_1 dz = 0 \quad \text{and} \quad P_2 dx + Q_2 dy + R_2 dz = 0\] whose integrals are respectively \[g(x, y, z) = C_1 \quad \text{and} \quad h(x, y, z) = C_2.\] Through a general point \((x_0, y_0, z_0)\) of space there pass two surfaces (one of each of the above families) whose curve of intersection \(C_0\) is the integral curve of the given system through the point. The tangent planes to the two surfaces at \((x_0, y_0, z_0)\) are normal to the directions \((P_1, Q_1, R_1)\) and \((P_2, Q_2, R_2)\) evaluated at the point, and the line of intersection \(L_0\) of these planes is normal to the two directions. Let \((X, Y, Z)\) be a set of direction numbers for \(L_0\); then \[X = \lambda \begin{bmatrix} Q_1 \\ R_2 \end{bmatrix}, \quad Y = \lambda \begin{bmatrix} R_1 \\ P_2 \end{bmatrix}, \quad Z = \lambda \begin{bmatrix} P_1 \\ Q_2 \end{bmatrix}\] are proportional to \(P, Q, R\) (all evaluated at the point). Now \(L_0\) is the tangent to \(C_0\) at \((x_0, y_0, z_0)\), since the tangent to a space curve at one of its points lies in the tangent plane at the point of any surface containing the curve. Hence, the integral curves of the system \[\frac{dx}{P} = \frac{dy}{Q} = \frac{dz}{R}\] consist of a doubly infinite system of curves characterized by the fact that at any point \((x_0, y_0, z_0)\) the tangent to the curve through the point has \((P_0, Q_0, R_0)\) as direction numbers.

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
