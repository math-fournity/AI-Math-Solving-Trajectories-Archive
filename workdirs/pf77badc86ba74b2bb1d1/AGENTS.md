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

In the coastal logistics hub of Delta Sector, there is a large plot of land shaped like a trapezoid, defined by two parallel boundaries: the northern perimeter road $AD$ and the southern service road $BC$. A central maintenance station $M$ is located exactly at the midpoint of the southern road $BC$.

A surveyor stands at a specific observation post $P$ located on the northern perimeter road $AD$. From this post, the surveyor sights a line of utility poles starting at $P$ and passing directly through the maintenance station $M$; this line continues until it intersects the eastern property line $DC$ at a remote signal tower $Q$.

A specialized underground fiber-optic cable is laid along a path starting from the observation post $P$. This cable runs perfectly perpendicular to the northern perimeter road $AD$. This cable path intersects a straight drainage pipe that connects the corner terminal $B$ to the signal tower $Q$. The point where the fiber-optic cable and the drainage pipe cross is marked as junction $K$.

Field measurements show that the angle formed at the signal tower between the junction $K$ and the eastern property line segment $QD$ (the angle $\angle KQD$) is $64^\circ$. Furthermore, the angle formed at the corner property marker $D$ between the junction $K$ and the signal tower $Q$ (the angle $\angle KDQ$) is $38^\circ$.

Based on this layout, what is the measure of the angle $\angle KBC$, in degrees, at the corner terminal $B$ between the junction $K$ and the southern service road $BC$?

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
