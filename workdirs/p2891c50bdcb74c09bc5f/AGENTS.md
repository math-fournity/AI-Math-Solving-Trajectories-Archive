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

In a futuristic industrial facility, a high-precision storage module is designed in the shape of a perfect cube with an edge length of 1 unit. The vertices of the floor are labeled $A, B, C, D$ in clockwise order, and the corresponding vertices of the ceiling are $A_1, B_1, C_1, D_1$ directly above them.

A specialized light-refracting glass pane is installed within the module, anchored at three specific points:
1. Point $E$, which is the exact midpoint of the floor-level structural beam $AB$.
2. Point $F$, located on the vertical support pillar $AA_1$. The position of $F$ is calibrated such that the distance from the ceiling $A_1$ to $F$ is exactly half the distance from $F$ to the floor $A$, maintaining a ratio of $A_1F:FA = 1:2$.
3. The corner vertex $B_1$ on the ceiling.

This glass pane forms a flat surface defined by the triangle $B_1EF$. To calibrate the facility’s optical sensors, engineers need to determine the steepness of this glass pane relative to the ceiling plane ($A_1B_1C_1D_1$). Let $\theta$ represent the dihedral angle formed between the plane of the glass pane $B_1EF$ and the plane of the ceiling.

Calculate the value of $\tan^2 \theta$.

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
