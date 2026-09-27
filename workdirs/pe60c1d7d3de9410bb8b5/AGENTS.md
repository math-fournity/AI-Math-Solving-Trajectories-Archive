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

In a remote sector of the ocean, a maritime rescue operation is coordinated within a triangular zone defined by three buoys: Alpha ($A$), Bravo ($B$), and Charlie ($C$). The zone forms an acute triangle. The command center tracks four specific coordinates critical to the mission:

1.  The Dispatch Center ($H$) is located at the orthocenter of the triangular zone.
2.  The Central Monitoring Station ($O$) is located at the circumcenter of the zone.
3.  The Rescue Fleet’s perimeter is defined by the circle ($\Gamma$) passing through all three buoys.
4.  The Supply Depot ($M$) is located at the midpoint of the minor arc $BC$ on the perimeter $\Gamma$.

The logistics team observes a unique geometric formation: the four points $A$, $H$, $M$, and $O$ form a rhombus. Furthermore, the direct supply line connecting the Dispatch Center ($H$) to Buoy Bravo ($B$) and the navigation route connecting the Supply Depot ($M$) to the Central Monitoring Station ($O$) intersect at a point situated exactly on the boundary line segment $AC$.

Calculations are required to determine the relative area efficiency of the logistics diamond compared to the entire rescue zone. Calculate the ratio of the area of the rhombus $AHMO$ to the area of the triangle $ABC$:

\[ \frac{\text{Area}(AHMO)}{\text{Area}(ABC)} \]

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
