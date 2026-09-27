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

In the coastal territory of Arcania, three lighthouses—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular shipping lane. The distance from Alpha to Bravo is exactly 6 nautical miles, Bravo to Charlie is 5 nautical miles, and Alpha to Charlie is 7 nautical miles. 

A central regional hub, Point $X$, is located at the intersection of two specialized signal beams. These beams are projected from lighthouses Bravo and Charlie such that each beam is perfectly tangent to the unique circular boundary passing through all three lighthouses (the territorial waters circle).

A small research buoy, $Z$, is anchored at a specific coordinate on this same circular territorial boundary. A straight underwater cable connects Charlie ($C$) to the buoy ($Z$). A deep-sea sensor, $Y$, is positioned on this cable such that the line connecting the hub ($X$) to the sensor ($Y$) is perfectly perpendicular to the cable $CZ$. The sensor $Y$ sits between $C$ and $Z$ at a position where the distance from the sensor to the buoy ($YZ$) is exactly three times the distance from the sensor to lighthouse Charlie ($CY$).

A secondary circular monitoring zone is defined as the circle passing through Bravo ($B$), Charlie ($C$), and the sensor ($Y$). A straight supply route extending from Alpha ($A$) through Bravo ($B$) continues until it intersects the boundary of this secondary monitoring zone at a point designated as the Maintenance Station $K$.

Calculate the distance from lighthouse Alpha ($A$) to the Maintenance Station $K$.

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
