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

A specialized irrigation system is designed around a triangular plot of land with vertices $A$, $B$, and $C$, where the side lengths are all distinct. To maximize efficiency, two circular sprinkler systems are installed: an "In-Plot" circle that touches the boundary fences $BC$, $AC$, and $AB$ at points $D$, $E$, and $F$, and an "Outer-Plot" circle (tangent to $BC$ and the extensions of $AB$ and $AC$) that touches these lines at points $D_1$, $E_1$, and $F_1$.

A central control unit $G$ is located at the unique intersection of the straight underground pipes $AD$, $BE$, and $CF$. A secondary monitoring hub $G_1$ is located at the intersection of pipes $AD_1$, $BE_1$, and $CF_1$. A technician lays a fiber-optic cable along the straight line $GG_1$. This cable intersects the primary water main—which runs along the internal angle bisector of the corner at vertex $A$—at a specific junction point $X$.

Surveyors provide the following measurements for the site:
1. The distance from vertex $A$ to the junction point $X$ is exactly $1$ unit.
2. The cosine of the angle at vertex $A$ is $\sqrt{3}-1$.
3. The length of the boundary fence $BC$ is $8\sqrt[4]{3}$ units.

The total area-related product of the boundary lengths $AB \cdot AC$ can be expressed in the form $\frac{j+k\sqrt{m}}{n}$ for positive integers $j, k, m, n$, where $\gcd(j,k,n)=1$ and $m$ is square-free.

Compute the value of $1000j+100k+10m+n$.

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
