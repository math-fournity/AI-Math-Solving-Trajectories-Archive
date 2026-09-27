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

A specialized architecture firm is designing a triangular recreational plaza, designated as area $ABC$. In this layout, the angle at the primary vertex $A$ is strictly obtuse. To plan the drainage system, engineers have marked point $D$ as the specific location on the straight boundary $BC$ that is directly perpendicular to vertex $A$.

For the landscaping design, two critical reference markers have been placed: marker $M$ sits exactly at the midpoint of the boundary $BC$, and marker $N$ sits exactly at the midpoint of the segment $BD$.

The project leads have noted three specific spatial constraints for this site:
1. The distance between vertex $A$ and vertex $C$ is exactly $2$ units.
2. The sightline angle between the paths $AB$ and $AN$ is identical to the angle between the paths $AM$ and $AC$ (i.e., $\angle BAN = \angle MAC$).
3. The product of the lengths of side $AB$ and side $BC$ is numerically equal to the length of the internal path $AM$.

The designers need to install a decorative fence along the straight line extending through $A$ and $M$. To determine the necessary clearance, calculate the shortest distance from vertex $B$ to the line $AM$.

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
