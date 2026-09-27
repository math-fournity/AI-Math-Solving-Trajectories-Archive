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

In a specialized logistics network, three main distribution hubs, labeled $A$, $B$, and $C$, are connected by straight transit corridors. The distances between these hubs are precisely $AB = 15$ kilometers, $BC = 16$ kilometers, and $CA = 17$ kilometers. A circular boundary road, $\Omega$, acts as the outer perimeter of this network, passing exactly through the three hubs.

A central command post, $N$, is positioned on the outer perimeter $\Omega$ at the exact midpoint of the longer (major) arc connecting $B$ and $C$. Inside the triangular region formed by the hubs, a security fence, $\omega$, is constructed in the shape of a circle that is perfectly tangent to all three transit corridors. The points where this fence touches the corridors $AC$ and $AB$ are designated as checkpoints $E$ and $F$, respectively.

An observation drone is stationed at a specific coordinates $X$, located on the same side of the line segment $EF$ as hub $A$. The drone’s position is calibrated such that the triangular formation $XEF$ is geometrically similar to the triangle formed by the hubs $ABC$ (where the vertices $X$, $E$, and $F$ correspond to $A$, $B$, and $C$ respectively).

A straight fiber-optic cable is laid from the command post $N$ to the drone at $X$. This cable crosses the transit corridor $BC$ at a junction point $P$.

Calculate the ratio of the distance between junction $P$ and drone $X$ to the distance between drone $X$ and command post $N$, expressed as the value of $\frac{PX}{XN}$.

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
