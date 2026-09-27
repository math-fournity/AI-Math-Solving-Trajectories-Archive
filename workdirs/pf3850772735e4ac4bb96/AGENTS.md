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

In a remote circular sanctuary with a radius of $2$ kilometers, three research stations, $A$, $B$, and $C$, are positioned on the perimeter. The angular separation between the stations is such that the difference between the interior angles at $B$ and $C$ is exactly $15^\circ$. 

The sanctuary’s central command post, $O$, sits at the exact geometric center of the circle. A specialized signal tower, $H$, is located at the triangle’s orthocenter, and a supply depot, $G$, is situated at the centroid. A secondary relay station, $L$, is established by reflecting the signal tower $H$ across the command post $O$.

Two straight survey paths are projected from station $A$: one passing through the supply depot $G$ and the other through the relay station $L$. These paths extend until they hit the sanctuary's perimeter again at points $X$ and $Y$, respectively. 

To expand the network, two auxiliary markers, $B_1$ and $C_1$, are placed on the perimeter such that the line segment $BB_1$ is parallel to the path between $A$ and $C$, and the segment $CC_1$ is parallel to the path between $A$ and $B$. 

A new boundary line is drawn connecting $X$ and $Y$, and another connecting $B_1$ and $C_1$. These two lines intersect at a specific observation point $Z$. It is determined that the distance from the central command post $O$ to this observation point $Z$ is $2\sqrt{5}$ kilometers. 

The squared distance between station $A$ and the observation point $Z$, denoted as $AZ^2$, can be expressed in the form $m - \sqrt{n}$ for positive integers $m$ and $n$. Find the value of $100m + n$.

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
