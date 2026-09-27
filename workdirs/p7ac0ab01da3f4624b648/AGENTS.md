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

In a remote industrial zone, a circular security perimeter is defined by $n$ watchtowers ($n \geq 3$), labeled $T_1, T_2, \dots, T_n$ in clockwise order. These towers are positioned such that the fence lines connecting consecutive towers ($T_i$ to $T_{i+1}$, with $T_{n+1}$ being $T_1$) form a convex polygon representing the secure facility's boundary.

The facility employs a "Symmetry Surveillance Protocol" to test the vulnerability of each tower's position. For any tower $T_i$, a "Shadow Point" $S_i$ is calculated. To find $S_i$, a surveyor identifies the midpoint of the straight line segment connecting the two neighboring towers, $T_{i-1}$ and $T_{i+1}$ (where $T_0$ is $T_n$). The Shadow Point $S_i$ is defined as the point such that the midpoint of the segment $T_i S_i$ is exactly that previously identified midpoint between the neighbors.

A tower $T_i$ is classified as "Secure" if its corresponding Shadow Point $S_i$ lies either within the interior of the facility or exactly on the boundary fence. 

Given that the towers must form a convex $n$-sided shape, determine the minimum possible number of "Secure" towers this facility can have, expressed as a function of $n$.

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
