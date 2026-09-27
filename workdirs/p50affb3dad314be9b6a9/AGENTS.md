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

A specialized textile factory uses a large loom to weave a fabric base shaped like a parallelogram, $ABCD$. The length of the side $AB$ is 8 meters, the side $AD$ is 11 meters, and the angle $\angle BAD$ at the corner is exactly $60^\circ$. 

The design team is marking three specific points for sensor placement on the edges of the fabric:
1. Point $X$ is located on the top edge $CD$ such that the ratio of the distance $CX$ to $XD$ is exactly $1:3$.
2. Point $Y$ is located on the side edge $AD$ such that the ratio of the distance $AY$ to $YD$ is exactly $1:2$.
3. Point $Z$ is located on the bottom edge $AB$. Its position is determined by a laser alignment system: when three lasers are projected across the fabric along the paths $AX$, $BY$, and $DZ$, they all intersect at a single common point.

A triangular reinforcement patch is to be sewn onto the fabric with its vertices at the sensor locations $X$, $Y$, and $Z$. Calculate the area of this triangular patch $XYZ$.

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
