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

A specialized deep-sea research team is tasked with monitoring a 100-kilometer stretch of an underwater fiber-optic cable, represented as a continuous line from the 0 km mark to the 100 km mark.

To monitor the cable, the team uses $N$ specialized acoustic sensors. Each sensor $i$ (where $i=1, 2, \dots, N$) has a fixed detection range of exactly 1 kilometer. Specifically, the $i$-th sensor covers the interval $[a_i, a_i+1]$. The placement of these sensors is constrained such that the starting point $a_i$ of any sensor must be chosen so that its entire 1-kilometer range lies within the 100-kilometer stretch (i.e., $[a_i, a_i+1] \subset [0,100]$).

The project requirements specify two conditions for the sensor deployment:
1. The combined coverage of all $N$ sensors must completely monitor the entire 100-kilometer cable without any gaps.
2. The deployment must be "minimal," meaning that if any single sensor is removed from the set of $N$ sensors, the remaining $N-1$ sensors will fail to cover the 100-kilometer stretch (there will be at least one uncovered gap).

Based on these constraints, what is the maximum possible number of sensors $N$ that can be used?

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
