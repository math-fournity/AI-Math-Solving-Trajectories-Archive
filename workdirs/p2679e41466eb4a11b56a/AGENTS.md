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

In a remote sector of deep space, a cosmic dust cloud has formed a perfect conical nebula $\mathcal{C}$ with its vertex at a pulsar named $A$. A flat, thin energy shield $\pi$ passes through the nebula, and the intersection forms an elliptical gateway $\mathcal{E}$.

The longest corridor of this gateway is defined by the segment $BC$, which has a length of $4$ light-years. Measurements confirm that the distance from the pulsar $A$ to the far end of the corridor $C$ is $5$ light-years, while the distance from the pulsar $A$ to the near end $B$ is $3$ light-years.

To stabilize the gateway, two spherical space stations are constructed within the nebula. One station is placed in the smaller region of the cone between the pulsar and the energy shield, while the other is placed in the vast region of the cone stretching beyond the shield. Both stations are engineered to be perfectly tangent to the interior walls of the conical nebula and also tangent to the elliptical energy shield $\pi$ at its focal points.

Based on the spatial geometry of this sector, what is the ratio of the radius of the smaller space station to the radius of the larger space station?

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
