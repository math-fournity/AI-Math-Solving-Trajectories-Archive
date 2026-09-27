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

A specialized satellite network is being deployed to monitor a triangular region of a planet defined by three ground stations, $A$, $B$, and $C$. The primary monitoring satellite orbits along a perfectly circular path $\omega$ that passes through $A$, $B$, and $C$. The center of this orbital circle, $O$, serves as the origin for the system's radial measurements. The distance from the station $A$ to the center $O$ is exactly $\frac{\sqrt{105}}{5}$ units.

Engineers identify a specific point $A_{\omega}$ on the orbital path $\omega$ that is diametrically opposite to station $A$. On the ground, a surveyor marks point $H$, which is the foot of the altitude from station $A$ to the straight line segment $BC$. To establish auxiliary relay zones, two points $H_B$ and $H_C$ are plotted such that $B$ is the midpoint of $HH_B$ and $C$ is the midpoint of $HH_C$.

Two signal towers, $P$ and $Q$, are constructed at specific intersections:
- Tower $P$ is located where the line extending through $A_{\omega}B$ meets the line passing through $H_B$ perpendicular to $BC$.
- Tower $Q$ is located where the line extending through $A_{\omega}C$ meets the line passing through $H_C$ perpendicular to $BC$.

Two circular signal coverage zones are established: $\omega_1$ is centered at $P$ with radius $PA$, and $\omega_2$ is centered at $Q$ with radius $QA$. It is discovered that the orbital path $\omega$ and the two coverage zones $\omega_1$ and $\omega_2$ all intersect at a single common point $X$, distinct from $A$. The direct distance from station $A$ to this intersection point $X$ is exactly $4$ units.

The efficiency of the network depends on the square of the difference between the distances of the primary station from the two secondary stations, calculated as $|AB - AC|^2$. This value can be expressed in the form $m - n\sqrt{p}$ for positive integers $m$ and $n$ and a squarefree positive integer $p$. Find the value of $m + n + p$.

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
