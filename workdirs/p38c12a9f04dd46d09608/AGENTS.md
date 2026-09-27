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

A remote triangular nature reserve is defined by three ranger stations: Station A, Station B, and Station C. The straight-line distances between them are exactly 13 km from A to B, 14 km from B to C, and 15 km from A to C. The entire reserve is enclosed within a circular boundary road, denoted as $\omega$, which passes through all three stations.

A straight supply road $\ell$ is constructed parallel to the southern boundary $BC$. This road $\ell$ intersects the western boundary $AB$ at point $D$, the eastern boundary $AC$ at point $E$, and hits the circular boundary road $\omega$ at two points, $K$ and $L$ (ordered $K, D, E, L$ along the road). 

Two circular helipads are constructed near the boundaries. Helipad $\gamma_1$ is designed to be tangent to the road segment $KD$, the boundary segment $BD$, and the circular boundary road $\omega$. Similarly, helipad $\gamma_2$ is tangent to the road segment $LE$, the boundary segment $CE$, and the circular road $\omega$. 

There is a central observation hub $P$ located at the intersection of the two internal common tangents of the circular helipads $\gamma_1$ and $\gamma_2$. As the position of the supply road $\ell$ is adjusted (while remaining parallel to $BC$), the observation hub $P$ moves along a specific straight-line path. If the total length of the segment traced by point $P$ is $L$, find the value of $L^2$.

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
