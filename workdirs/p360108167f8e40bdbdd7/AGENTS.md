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

In a remote territory, three survey outposts—A, B, and C—form a triangular perimeter. A central logistics hub, $K$, is positioned exactly at the triangle's symmedian point. A specialized angle $\theta$ is defined as the deviation of the survey angle $\angle AKB$ from a right angle (specifically, $\theta = \angle AKB - 90^\circ$). This angle $\theta$ is confirmed to be positive and strictly less than the interior angle at outpost $C$.

A secondary observation station, $K'$, is established within the perimeter such that stations $A, K', K,$ and $B$ all lie on the same circular boundary, and the sighting angle $\angle K'CB$ is exactly $\theta$. Furthermore, a third communication node, $P$, is placed within the triangle such that the line $K'P$ is perpendicular to the boundary $BC$, while the sighting angle $\angle PCA$ also equals $\theta$.

Field measurements have determined two critical constraints for this configuration:
1. The sine of the communication angle at node $P$ relative to outposts $A$ and $B$ satisfies the relation $\sin \angle APB = \sin^2(C - \theta)$.
2. The product of the lengths of the two median transport routes originating from outposts $A$ and $B$ (extending to the midpoints of the opposite boundaries) is exactly $\sqrt{\sqrt{5}+1}$.

Based on these geographical constraints, calculate the maximum possible value of the structural density metric defined by the formula $5AB^2 - CA^2 - CB^2$. If this value is expressed in the form $m \sqrt{n}$ for positive integers $m$ and $n$ (where $n$ is squarefree), compute the final result as $100m + n$.

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
