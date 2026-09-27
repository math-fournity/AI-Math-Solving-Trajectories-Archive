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

In the remote logistics hub of Port Apex, a specialized team of seven cargo drones is commissioned to deliver a critical sensor to a Deep Sea Outpost. Each drone is equipped with a battery capacity that allows for exactly 4 days of operation. Due to the high-pressure environment, a drone can never carry more than 4 days' worth of energy at any time.

The mission starts at Port Apex. The drones can transfer energy units to one another in full-day increments while in transit. To ensure the safety of the fleet, any drone that begins its return journey to Port Apex must have sufficient energy to reach the port and, once it docks, it cannot be redeployed for the remainder of the mission. Each drone consumes exactly one day’s worth of energy for every day it spends traveling (either away from or toward the port). 

The drones are permitted to depart Port Apex on different days if the strategy requires it, but all travel and energy transfers occur in discrete, integer-day intervals. 

What is the maximum distance (in days of travel) the Deep Sea Outpost can be located from Port Apex such that one specific drone, the "Lead Unit," reaches the Outpost while every other drone in the team successfully returns to Port Apex without running out of energy?

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
