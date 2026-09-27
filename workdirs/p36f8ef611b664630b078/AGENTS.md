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

In the coastal province of Geometria, three lighthouses—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular navigational sector. Surveyor drones have measured the direct distance from Alpha to Bravo as exactly 17 nautical miles, while the distance from Alpha to Charlie is exactly 23 nautical miles. 

The regional shipping hub, Point $G$, is located precisely at the centroid of the triangle formed by these three lighthouses. To improve maritime safety, two auxiliary signal buoys, Bravo-Prime ($B_1$) and Charlie-Prime ($C_1$), are anchored on the unique circular boundary that passes through the three lighthouses. The placement of these buoys is strictly regulated: the line segment $BB_1$ must be perfectly parallel to the shipping lane $AC$, and the line segment $CC_1$ must be perfectly parallel to the shipping lane $AB$.

Deep-sea fiber optic cables are laid in a straight line connecting buoy $B_1$ and buoy $C_1$. Monitoring stations have confirmed a rare alignment: the shipping hub $G$ lies exactly on the straight line path between $B_1$ and $C_1$.

The squared distance of the remaining side of the sector, $BC^2$, is calculated to be a rational number $\frac{m}{n}$ in lowest terms (where $m$ and $n$ are relatively prime positive integers). Determine the value of $100m + n$.

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
