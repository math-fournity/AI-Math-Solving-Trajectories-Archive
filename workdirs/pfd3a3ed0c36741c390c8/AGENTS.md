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

In a specialized testing facility, a laser-guided robotic probe moves along a straight industrial track. Four critical sensor markers, designated $Z_1, Z_2, Z_3,$ and $Z_4$, are placed in that specific order along this linear path. The distances between these markers are precisely measured: the gap between $Z_1$ and $Z_2$ is 5 meters, the gap between $Z_2$ and $Z_3$ is 1 meter, and the gap between $Z_3$ and $Z_4$ is 3 meters.

The facility’s positioning system operates on a Cartesian grid where two signal emitters are fixed at coordinates $(0, -a)$ and $(0, a)$, for some positive constant distance $a$. A receiver at any point $(x, y)$ calculates its "signal intensity" based on the distances $d_1 = \sqrt{x^2 + (y+a)^2}$ and $d_2 = \sqrt{x^2 + (y-a)^2}$ from these emitters.

The system detects that the outer markers $Z_1$ and $Z_4$ both lie on a specific interference boundary defined by the energy equilibrium equation:
$$d_1^2 + d_2^2 = 4a^2 + d_1 d_2$$

Furthermore, the system detects that the inner markers $Z_2$ and $Z_3$ both lie on a different interference boundary defined by the energy equilibrium equation:
$$d_1^2 + d_2^2 = 4a^2 - d_1 d_2$$

Given these spatial constraints, the value $a^2$ can be expressed in the form $\frac{m+n \sqrt{p}}{q}$, where $m, n, p,$ and $q$ are positive integers, $m, n,$ and $q$ are relatively prime, and $p$ is squarefree. Find the sum $m+n+p+q$.

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
