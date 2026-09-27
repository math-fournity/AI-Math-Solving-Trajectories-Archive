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

In a specialized laser-grid testing facility, three sensor beacons are positioned at coordinates $A, B,$ and $C$ forming a triangular field. The direct cable distances between them are measured: the line $AB$ spans $2\sqrt{6}$ units, $BC$ spans $5$ units, and $CA$ spans $\sqrt{26}$ units. Let $M$ be the midpoint of the cable $BC$. The facility’s central processing circle, $\Omega$, is defined as the unique circle passing through $A, B,$ and $C$. 

Within this field, the "signal interference node" $H$ is located at the orthocenter of triangle $ABC$. Secondary relay points $E$ and $F$ are established where the signal paths $BH$ and $CH$ intersect the cables $AC$ and $AB$, respectively. To stabilize the grid, two additional reference points are marked: $R$ at the midpoint of the line segment $EF$, and $N$ at the midpoint of the line segment $AH$.

A calibration beam $AR$ is fired, and its path intersects the circle passing through $A, H,$ and $M$ at a secondary point $L$. A specialized monitoring circle is then drawn through points $A, N,$ and $L$; this circle intersects the main circle $\Omega$ at point $J$, and it intersects the circle passing through $B, N,$ and $C$ at point $O$.

The facility engineers identify a specific intersection point $U$, which is the second point (other than $M$) where the circle $AHM$ meets the circle $JMO$. A final laser trajectory is traced along the line $AU$, and its intersection with the circle passing through $A, H,$ and $C$ (other than the origin point $A$) is designated as vertex $V$.

If the square of the distance between sensor $C$ and vertex $V$ is represented as a reduced fraction $\frac{m}{n}$ for relatively prime positive integers $m$ and $n$, find the value of $100m + n$.

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
