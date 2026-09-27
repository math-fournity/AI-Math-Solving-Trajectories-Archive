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

A specialized architecture firm is designing a triangular park, defined by three boundary markers $A$, $B$, and $C$. The southern boundary $BC$ measures exactly 15 kilometers. At the corner of marker $B$, the internal angle between the boundaries $BA$ and $BC$ is $60^\circ$. 

A central communications hub is located at point $Q$ within the park. To facilitate maintenance, three straight access paths ($QX, QY,$ and $QZ$) are paved from the hub to each boundary such that each path meets its respective boundary at a right angle: $X$ on $BC$, $Y$ on $CA$, and $Z$ on $AB$. Surveyors have determined that the distance from marker $B$ to the junction $Z$ is 8 kilometers, and the length of the access path $ZQ$ is 6 kilometers. Furthermore, the angle formed between the hub, the marker $C$, and the boundary $CA$ (denoted $\angle QCA$) is $30^\circ$.

The firm plans to install a circular perimeter fence that passes through the three junctions $X, Y,$ and $Z$. A straight underground cable line is laid following the path of $QX$. This cable line extends beyond junction $X$ and intersects the circular fence at a second point, $W$.

Engineers need to calculate the ratio of the straight-line distance between $W$ and $Y$ to the straight-line distance between $W$ and $Z$. If this ratio $WY/WZ$ is expressed as a fraction $p/q$ in simplest form, what is the value of $p+q$?

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
