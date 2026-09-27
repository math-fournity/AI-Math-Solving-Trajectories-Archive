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

A specialized logistics firm operates three delivery drones across a flat, two-dimensional city grid. The firm utilizes three specific "load factors" represented by the values $x_1 = -1$, $x_2 = 2$, and $x_3 = 5$. 

The drones are deployed to three distinct delivery locations, represented by position vectors $\vec{\alpha_1}, \vec{\alpha_2}, \vec{\alpha_3}$ relative to a central hub. The only constraint on these deployments is that the furthest drone from the hub is exactly 36 units away (meaning the maximum magnitude among the three vectors is 36).

The firm’s total "displacement impact" is calculated by assigning one of the three load factors to each drone's position vector and summing them. Specifically, for any set of drone positions, the firm chooses a permutation $(k_1, k_2, k_3)$ of the load factors $(x_1, x_2, x_3)$ to maximize the magnitude of the resulting vector:
\[ \vec{V} = x_{k_1} \vec{\alpha_1} + x_{k_2} \vec{\alpha_2} + x_{k_3} \vec{\alpha_3} \]

Find the largest possible value $C$ such that, regardless of how the drones are positioned (as long as at least one is 36 units from the hub), the firm can always find a permutation of load factors that ensures the magnitude of the displacement impact $|\vec{V}|$ is at least $C$.

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
