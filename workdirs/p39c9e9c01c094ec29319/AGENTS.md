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

In a futuristic industrial facility, a specialized floor-cleaning drone moves along the surface of a circular testing bay with a radius of 1 meter. The drone is tethered to a central spool at the origin $(0,0)$ by a high-tension cable that always forms a straight line between the drone and the center. As the drone moves, the cable dispenses chemical treatments onto the floor: whenever the drone moves counterclockwise relative to the center, the cable coats the swept area with a black sealant; whenever it moves clockwise, it coats the swept area with an orange resin. Both substances are applied at a density of exactly 1 gallon per square meter of swept area, regardless of any previous coatings.

The drone begins its operation at the coordinate $(1,0)$. Its movement protocol consists of 89 discrete steps. Each step $n$ (for $n=1, 2, \dots, 89$), the drone travels in a straight line from its current position on the boundary of the circle to a new position on the boundary. Specifically, if its position at the start of step $n$ is $(\cos(\theta_n), \sin(\theta_n))$, it moves to $(\cos(\theta_n + \alpha_n), \sin(\theta_n + \alpha_n))$. The angular displacement for the first step is $\alpha_1 = 253^\circ$, and for each subsequent step, the displacement decreases by $2^\circ$ (so $\alpha_2 = 251^\circ$, $\alpha_3 = 249^\circ$, and so on).

After the drone completes all 89 steps, the facility manager calculates the total volume of black sealant used and the total volume of orange resin used. The absolute difference between these two volumes, measured in gallons, is expressed in the form $\frac{\sqrt{a}-\sqrt{b}}{c} \cot 1^{\circ}$, where $a, b,$ and $c$ are positive integers such that no prime divisor of $c$ divides both $a$ and $b$ twice (i.e., $\gcd(a, b, c^2)$ is square-free). 

Find the value of $a+b+c$.

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
