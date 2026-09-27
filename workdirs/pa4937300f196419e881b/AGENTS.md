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

A specialized architectural firm is designing a high-tech observation outpost shaped like a triangular pyramid, designated $SABC$. The foundation of the structure is a triangular concrete pad $ABC$. The location of the vertical support beam $SB$ is unique because the two steel-reinforced walls, $ASB$ and $CSB$, are both built perfectly perpendicular to the ground level of the foundation $ABC$.

The third exterior wall, $ASC$, is a slanted glass facade tilted at an angle of $\beta = 60^\circ$ relative to the foundation $ABC$. To ensure stability, the triangular foundation $ABC$ is designed such that the angle at corner $B$ ($\angle ABC$) is $\alpha = 60^\circ$. Furthermore, the foundation is precisely sized so that its three corners $A$, $B$, and $C$ sit exactly on the perimeter of a circular drainage ring with a radius of $r = 1$ unit.

The entire structure is to be enclosed within a spherical pressurized dome (the circumscribed sphere of the pyramid) to protect it from the environment. Let $R$ represent the radius of this enclosing sphere.

Calculate the value of $R^2$ based on the specific design parameters $r=1, \alpha=60^\circ, \text{ and } \beta=60^\circ$.

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
