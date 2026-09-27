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

In a specialized circular testing facility, a robotic arm is anchored at a base point $A$ on the perimeter of a circular track with diameter $AB$. Three sensors—$X, Y,$ and $Z$—are positioned along the track such that $A, X, Y, B,$ and $Z$ form the vertices of a convex pentagon in clockwise order. A laser guidance rail is positioned tangent to the circular track at the specific location of sensor $Y$. 

The robotic arm $AB$ monitors two signal lines: one extending from $B$ through sensor $X$ and another from $B$ through sensor $Z$. These signal lines intersect the laser guidance rail at transmission nodes $L$ and $K$, respectively. Precise calibration reveals two geometric constraints: the arm's reach to sensor $Y$ (segment $AY$) exactly bisects the angle formed between the arm's reach to node $L$ and its reach to sensor $Z$ ($\angle LAZ$). Furthermore, the straight-line distance from $A$ to sensor $Y$ is identical to the distance between sensors $Y$ and $Z$ ($AY = YZ$).

As the sensors shift along the track to optimize data reception, engineers monitor a specific performance index defined by the expression:
$$\frac{AK}{AX} + \left(\frac{AL}{AB}\right)^2$$
where each term represents the distance between the corresponding points.

If the minimum possible value of this performance index is expressed in the form $\frac{m}{n} + \sqrt{k}$, where $m, n,$ and $k$ are positive integers and $\text{gcd}(m, n) = 1$, calculate the system code $m + 10n + 100k$.

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
