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

In a remote industrial park, a rectangular solar field $ABCD$ is being partitioned for a new installation. Two control stations, $E$ and $F$, are positioned on the northern boundary $\overline{AB}$ and the southern boundary $\overline{CD}$, respectively, such that the distance $BE$ is strictly less than $CF$.

The engineering team plans to mirror the section $BCFE$ across the line segment $\overline{EF}$. During this projection, the corner $C$ is mapped to a specific relay point $C'$ located on the western boundary $\overline{AD}$. Simultaneously, the corner $B$ is mapped to a point $B'$. 

Diagnostic scans of the layout reveal two critical geometric properties:
1. The angle formed at the intersection of the northern boundary and the projected line, $\angle B'EA$, is exactly congruent to the angle $\angle AB'C'$.
2. The distance from the northwestern corner $A$ to the projected point $B'$ is precisely $5$ units.
3. The distance along the northern boundary from corner $B$ to station $E$ is exactly $23$ units.

The total area of the original solar field $ABCD$ can be expressed in the form $a + b\sqrt{c}$ square units, where $a, b$, and $c$ are integers and $c$ is square-free. Compute the value of $a + b + c$.

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
