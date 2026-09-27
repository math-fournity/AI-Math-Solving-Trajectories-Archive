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

A specialized robotic arm is mounted on a straight laboratory track $\Delta$. The base of the arm consists of a slider $AB$ of variable length that moves along the track in a fixed positive direction, with the starting joint $A$ positioned at the origin $(0,0)$. The robot’s upper structure is a horizontal crossbar $CD$ of variable length, held parallel to the track. 

To maintain structural integrity, the arm’s configuration must always satisfy three mechanical constraints:
(i) The length of the base slider $AB$ cannot exceed a maximum extension $a$;
(ii) The distance between the midpoint $E$ of the base $AB$ and the midpoint $F$ of the crossbar $CD$ is exactly $l$;
(iii) The sum of the squares of the lengths of the two support struts, $AD$ and $BC$, must equal a constant tension value $k$.

As the robot adjusts its configuration to meet these constraints, the joint $D$ moves through space, tracing a specific path $L_D$. In the Cartesian plane where the track $\Delta$ is the $x$-axis, this path $L_D$ forms a circular arc.

Let $(x_c, y_c)$ be the coordinates of the center of the circle containing the path $L_D$, and let $r$ be the radius of this circle. Determine the value of $x_c^2 + y_c^2 + r^2$ expressed in terms of the constants $k$ and $l$.

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
