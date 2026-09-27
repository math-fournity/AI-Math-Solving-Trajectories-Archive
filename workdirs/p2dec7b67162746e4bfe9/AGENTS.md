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

In the coastal province of Trigonometry, three lighthouse stations—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular safety zone. Surveyors have measured the direct nautical distances between them: the distance from Alpha to Bravo is exactly 13 miles, Bravo to Charlie is 14 miles, and Charlie back to Alpha is 15 miles.

To monitor the fleet, the navy identifies two strategic coordination points within this triangle: the Command Center ($O$), located at the center of the unique circular path passing through all three stations, and the Signal Hub ($H$), located at the intersection of the three altitudes of the triangle.

A specialized radar dome is projected such that its boundary forms a perfect circle passing through Alpha, the Command Center, and the Signal Hub. This radar boundary intersects the straight supply line between Alpha and Bravo at a checkpoint named Delta ($D$), and it intersects the straight supply line between Alpha and Charlie at a checkpoint named Echo ($E$).

Logistics officers determine that the ratio of the distance from Alpha to Delta ($AD$) to the distance from Alpha to Echo ($AE$) can be expressed as a fraction $m/n$ in lowest terms, where $m$ and $n$ are positive relatively prime integers. Calculate the value of $m - n$.

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
