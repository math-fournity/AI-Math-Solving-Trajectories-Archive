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

In a remote mountain range, a specialized communications array is constructed in the shape of a regular tetrahedron $ABCD$. The triangular base $ABC$ consists of three ground stations forming an equilateral triangle with a side length of $4\sqrt{3}$ units. A central transmitter $D$ is positioned such that the angle formed by the structural beams at the apex, $\angle DAB$, is exactly $\arctan \sqrt{\frac{37}{3}}$.

To reinforce the structure, engineers have identified three specific points, $A_1$, $B_1$, and $C_1$, which are the midpoints of the vertical support cables $AD$, $BD$, and $CD$ respectively. Two critical fiber-optic lines are strung through the interior of the array: one connecting ground station $B$ to midpoint $A_1$, and another connecting ground station $A$ to midpoint $C_1$.

A third utility line is stretched between ground station $C$ and midpoint $B_1$. A spherical weather sensor is then deployed within the array. This sensor is calibrated such that its surface is tangent to the ground plane $ABC$ and simultaneously touches the three interior lines: the segment $AC_1$, the segment $BA_1$, and the segment $CB_1$.

Determine the following specifications for the installation:
1) The value of $\cos \phi$, where $\phi$ is the angle of intersection (inclination) between the paths of lines $BA_1$ and $AC_1$.
2) The value $d$, representing the shortest clearance distance between the lines $BA_1$ and $AC_1$.
3) The value $r$, representing the radius of the spherical weather sensor.

Calculate the final system constant given by the expression: $32 \cos \phi + d^2 \cdot \frac{301}{36} + r$.

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
