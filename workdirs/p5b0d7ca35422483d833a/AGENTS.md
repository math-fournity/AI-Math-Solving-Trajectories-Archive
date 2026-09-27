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

In the year 2020, a specialized robotic rover is stationed at the Command Center, designated as coordinate (0,0) on a digital grid. Its mission is to deliver a payload to a Research Outpost located at coordinates (20,20).

The rover’s navigation system is programmed with only three specific movement commands:
1. **Eastward Shift:** Move exactly 1 unit East (increase the x-coordinate by 1).
2. **Northward Shift:** Move exactly 1 unit North (increase the y-coordinate by 1).
3. **Hyper-Diagonal Jump:** Move exactly 1 unit East and 1 unit North simultaneously (increase both x and y coordinates by 1).

However, the terrain is plagued by "Interference Zones." Any grid intersection (lattice point) where the sum of the North and East coordinates is a multiple of 3 is a dead zone that will fry the rover's circuits. The only exception is the Command Center itself (0,0), which is shielded. For the rover to safely reach the Research Outpost at (20,20), it must never land on any intermediate grid point where the sum of the coordinates is divisible by 3.

How many unique valid sequences of movements can the rover take to reach the Research Outpost without ever entering an Interference Zone?

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
