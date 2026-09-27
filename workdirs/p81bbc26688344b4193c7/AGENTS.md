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

In a remote territory, a survey team is mapping a triangular sector defined by three outposts: Alpha ($A$), Bravo ($B$), and Charlie ($C$). The sector's central observation tower is located at the circumcenter $O$ of triangle $ABC$, while the main communication hub $H$ is situated at the triangle's orthocenter.

A technician identifies a direct cable route from Bravo through the hub $H$ that connects to the perimeter road $AC$ at a junction point $E$. To monitor the terrain, the team establishes two additional markers: point $M$ at the exact midpoint of the cable segment between $H$ and $B$, and point $N$ at the exact midpoint of the path between $H$ and the observation tower $O$.

A specialized research unit is formed within the smaller triangular zone defined by Alpha ($A$), junction $E$, and marker $M$. The unit's command post $I$ is placed at the incenter of triangle $AEM$. A linear supply trail starts at Alpha, passes through the command post $I$, and continues until it intersects the boundary line $ME$ at a terminal point $J$.

The surveyors provide the following measurements:
- The distance from Alpha to the observation tower $O$ is $20$ units.
- The distance from Alpha to marker $N$ is $17$ units.
- The path from Alpha to $N$ is perfectly perpendicular to the path from $N$ to $M$ (angle $ANM = 90^\circ$).

If the ratio of the distance from Alpha to the command post $I$ to the distance from Alpha to the terminal point $J$ is expressed as a reduced fraction $\frac{m}{n}$ for relatively prime positive integers $m$ and $n$, compute the value of $100m + n$.

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
