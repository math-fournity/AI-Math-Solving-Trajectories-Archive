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

In a remote desert, three research stations, Alpha ($A$), Bravo ($B$), and Charlie ($C$), form an acute triangular perimeter. A central communications hub is located at the circumcenter $O$ of the triangle, and a logistics depot is situated at the centroid $G$ of the triangle.

The technicians are establishing a local coordinate system. First, they define a line of sight tangent to the circular perimeter (the circumcircle passing through $A, B,$ and $C$) specifically at station Alpha. Next, they construct a maintenance road that passes through the logistics depot $G$ and runs exactly perpendicular to the path connecting the logistics depot $G$ to the communications hub $O$.

A specialized sensor, $X$, is placed at the intersection of the tangent line at Alpha and this perpendicular maintenance road. Following the maintenance road further, a relay node $Y$ is installed at the point where the road intersects the straight boundary line between stations Bravo and Charlie.

The surveyors measure three specific angles within this network: the internal angle at station Bravo ($\angle ABC$), the internal angle at station Charlie ($\angle BCA$), and the angle formed at the hub between the sensor and the relay ($\angle XOY$). They determine that the degree measures of these three angles, in the order listed, follow a strict ratio of $13 : 2 : 17$.

The degree measure of the internal angle at station Alpha ($\angle BAC$) can be expressed as a simplified fraction $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find the value of $m+n$.

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
