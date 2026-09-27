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

In a remote sector of the ocean, three research buoys—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. A central data hub, Giga ($G$), is located at the exact geometric center (centroid) of the triangle formed by these three buoys.

Marine surveyors have recorded two specific angular measurements from their charts: the angle formed at buoy Charlie between the lines of sight to Alpha and Bravo ($\angle ACB$) is exactly $85^\circ$. Furthermore, the angle subtended at the central hub Giga by the two buoys Alpha and Bravo ($\angle AGB$) is $140^\circ$.

Two maintenance drones are currently positioned along the submerged cables connecting the hub to the buoys. Drone Kilo ($K$) is located on the cable between Giga and Bravo ($BG$), while drone Lima ($L$) is located on the cable between Giga and Alpha ($AG$). 

Sensors indicate the following directional alignments:
- The angle between the line from Alpha to Charlie and the line from Alpha to drone Kilo ($\angle CAK$) is $40^\circ$.
- The angle between the line from Bravo to Charlie and the line from Bravo to drone Lima ($\angle CBL$) is $40^\circ$.

A technician needs to calibrate the sonar sweep between the two drones. Calculate the measure of the angle formed at buoy Charlie between the lines of sight to drone Kilo and drone Lima ($\angle KCL$).

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
