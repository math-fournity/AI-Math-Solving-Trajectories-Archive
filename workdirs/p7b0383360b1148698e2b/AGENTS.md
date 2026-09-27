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

A specialized five-sided space station, represented by the docking ports $A, B, C, D$, and $E$ in that order, lies on a perfect circular orbit. To stabilize the structure, three high-tension support cables of equal length have been installed between specific ports: one from $A$ to $C$, one from $B$ to $D$, and one from $C$ to $E$.

Inside the station, these cables cross at two navigational hubs. Hub $X$ is located where the cables $AC$ and $BD$ intersect, while Hub $Y$ is located where the cables $BD$ and $CE$ intersect. Technical surveys of the interior have provided the following segment lengths along the cables:
- The distance from port $A$ to hub $X$ is 6 meters ($AX = 6$).
- The distance between hub $X$ and hub $Y$ is 4 meters ($XY = 4$).
- The distance from hub $Y$ to port $E$ is 7 meters ($YE = 7$).

The total interior deck area of the convex pentagonal station $ABCDE$ is calculated to be $\frac{a\sqrt{b}}{c}$ square meters, where $a, b,$ and $c$ are integers, $c > 0$, $b$ is square-free, and $\gcd(a, c) = 1$. Find the value of $100a + 10b + c$.

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
