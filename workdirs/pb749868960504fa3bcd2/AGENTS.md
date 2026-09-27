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

In the coastal territory of Planimetria, three navigation beacons—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. This perimeter is an acute scalene triangle. The territory’s central monitoring station is located at $O$, the center of the unique circular path passing through all three beacons (the circumcircle). A specialized maintenance hub is located at $H$, the orthocenter of the triangle $ABC$.

An experimental signal beam is projected from Alpha. This beam follows a straight line tangent to the circle passing through $A, H,$ and $O$. This signal beam travels across the territory until it hits a relay station, $P$, located on the boundary of the main circular perimeter ($P \neq A$).

Two sensor zones are defined: Zone 1 is the circular region passing through $A, O,$ and $P$; Zone 2 is the circular region passing through $B, H,$ and $P$. These two zones overlap, and their points of intersection are $P$ and a secondary data point $Q$. A fiber-optic cable is laid along the straight line connecting $P$ and $Q$. This cable crosses the supply route $BO$ at a specific junction point $X$.

Surveyors have recorded the following measurements:
- The distance from beacon Bravo ($B$) to junction $X$ is exactly $2$ leagues.
- The distance from the central station ($O$) to junction $X$ is exactly $1$ league.
- The direct distance between beacons Bravo ($B$) and Charlie ($C$) is $5$ leagues.

The total energy requirement for the Alpha sector is defined by the product of the distances $AB$ and $AC$. This product can be expressed in the form $\sqrt{k}+m\sqrt{n}$ for positive square-free integers $k$ and $n$, and a positive integer $m$.

Compute the value of $100k+10m+n$.

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
