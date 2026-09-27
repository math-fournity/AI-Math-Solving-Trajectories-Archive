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

In a vast salt flat, two specialized survey beacons, Alpha ($A$) and Charlie ($C$), are permanently anchored at a distance of exactly $200$ units apart. A central coordinate marker, Kilo ($K$), is placed exactly at the midpoint of the segment connecting Alpha and Charlie.

Two mobile robotic rovers, Bravo ($B$) and Delta ($D$), are patrolling the flat. Their navigation systems are programmed such that Kilo ($K$) always remains the exact midpoint of the line segment between the two rovers.

A transmission beam is projected along the angle bisector of $\angle BCD$. This beam crosses the straight-line path between Alpha and Bravo at a relay point designated as Item ($I$), and it crosses the straight-line path between Alpha and Delta at a relay point designated as Juliet ($J$).

A local monitoring system tracks two circular zones: 
- Zone 1 ($\omega_1$) is defined by the circle passing through the positions of Alpha, Bravo, and Delta.
- Zone 2 ($\omega_2$) is defined by the circle passing through the positions of Alpha, Item, and Juliet.

The boundaries of Zone 1 and Zone 2 intersect at two distinct locations: Alpha ($A$) and a second data-logging point, Mike ($M$).

As the rovers Bravo and Delta move while maintaining their midpoint constraint at Kilo, the position of point Mike shifts. Find the maximum possible perpendicular distance from the data-logging point Mike ($M$) to the straight line established by the beacons Alpha and Charlie ($AC$).

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
