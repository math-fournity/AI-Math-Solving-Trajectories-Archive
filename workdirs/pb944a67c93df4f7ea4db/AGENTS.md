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

In the city of Metropolia, the Department of Energy manages four different power sources: Solar ($x$), Wind ($y$), Geothermal ($w$), and Hydroelectric ($z$). These sources provide energy units to five different industrial districts, each with specific consumption rates and total energy requirements.

- **The Forge District** requires 13 units of Solar, 7 of Wind, 12 of Geothermal, and 6 of Hydroelectric to meet its daily quota of 65 megawatt-hours.
- **The Transit Hub** requires 9 units of Solar, 2 of Wind, 17 of Geothermal, and 12 of Hydroelectric to reach its capacity of 69 megawatt-hours.
- **The Residential Core** utilizes 6 units of Solar, 9 of Wind, 7 of Geothermal, and 5 of Hydroelectric to maintain its load of 62 megawatt-hours.
- **The Tech Park** demands 7 units of Solar, 11 of Wind, 19 of Geothermal, and 7 of Hydroelectric to power its servers, totaling 71 megawatt-hours.
- **The Harbor District** needs 11 units of Solar, 3 of Wind, 23 of Geothermal, and 17 of Hydroelectric to operate its cranes, totaling 73 megawatt-hours.

The city council is planning to build a "Mega-Grid" that combines the energy outputs of these sources in a specific configuration. To calculate the budget for this new project, the chief engineer needs to determine the total energy produced by a combined load of exactly 20 units of Solar, 28 units of Wind, 50 units of Geothermal, and 42 units of Hydroelectric.

Based on the consumption data from the five districts, what is the value of $20x + 28y + 50w + 42z$?

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
