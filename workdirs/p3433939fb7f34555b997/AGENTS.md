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

In the mountainous borderlands of three provinces, a triangular telecommunications network is established with base stations at points $A$, $B$, and $C$. The direct cable lengths between them are $BC = 13$ km, $CA = 11$ km, and $AB = 10$ km. A maintenance hub $A_1$ is located exactly at the midpoint of the cable connecting $B$ and $C$. A straight service road $\ell$ passes through hub $A_1$, intersecting the paths $AC$ and $AB$ at checkpoints $B_1$ and $C_1$ respectively.

Two regional monitoring towers, $B_2$ and $C_2$, are positioned such that they remain equidistant from stations $B$ and $C$ (placing them on the perpendicular bisector of $BC$). Tower $B_2$ is strategically located so that the signal beam from $B_2$ to checkpoint $C_1$ is perpendicular to the path $AB$. Similarly, tower $C_2$ is located such that the signal beam from $C_2$ to checkpoint $B_1$ is perpendicular to the path $AC$.

A central processing unit $P$ is located at the intersection of the fiber optic lines $BB_2$ and $CC_2$. Furthermore, two circular security zones are defined: one with diameter $BB_2$ and another with diameter $CC_2$. These two zones overlap at two points, one of which is the hub $A_1$. The other intersection point is a satellite uplink $Q$, which is located on the same side of the boundary line $BC$ as the main station $A$.

As the orientation of the service road $\ell$ varies, the positions of $P$ and $Q$ shift. Determine the minimum possible value of the ratio sum $\frac{PB}{PC} + \frac{QB}{QC}$. If this minimum value is expressed as $\frac{a \sqrt{b}}{c}$ for positive integers $a, b, c$ where $\gcd(a, c) = 1$ and $b$ is squarefree, calculate the sum $a + b + c$.

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
