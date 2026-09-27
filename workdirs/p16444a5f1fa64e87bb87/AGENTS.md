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

In the coastal city of Apollonia, a new semicircular harbor is defined by a straight breakwater $\overline{AB}$. Five surveillance stations, $A, X, Y, B$, and $Z$, are positioned along the curved boundary of the harbor in that order. Because the boundary is a semicircle with diameter $\overline{AB}$, the stations form an inscribed convex pentagon $AXYBZ$.

The city's communication hub is at station $Y$. A straight fiber-optic cable is laid tangent to the harbor's curved boundary at point $Y$. This tangent line intersects the direct sightline extending from $B$ through $X$ at a relay point $L$, and it intersects the sightline extending from $B$ through $Z$ at a second relay point $K$.

To ensure signal integrity, two geometric constraints are met: first, the sightline from $A$ to $Y$ perfectly bisects the angle formed between the sightline $A$ to $L$ and the sightline $A$ to $Z$ (so $\angle LAY = \angle YAZ$). Second, the direct distance between stations $A$ and $Y$ is exactly equal to the direct distance between station $Y$ and station $Z$.

A logistics engineer is tasked with minimizing the following structural efficiency cost:
\[ \frac{AK}{AX} + \left( \frac{AL}{AB} \right)^2 \]
where $AK, AX, AL,$ and $AB$ represent the straight-line distances between those respective points.

The minimum possible value of this expression can be written in the form $\frac{m}{n} + \sqrt{k}$, where $m, n,$ and $k$ are positive integers and $\gcd(m, n) = 1$. Compute the value of $m + 10n + 100k$.

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
