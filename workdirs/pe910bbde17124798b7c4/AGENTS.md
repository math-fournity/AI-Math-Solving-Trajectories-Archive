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

In the competitive world of high-tech logistics, a specialized cargo drone is programmed to transport materials across five distinct research hubs, designated $p_1, p_2, p_3, p_4$, and $p_5$. Each hub is assigned a unique identification code that must be a prime number. 

The drone’s fuel efficiency is governed by a specific energy balance equation. On one side of the equilibrium, the drone consumes energy equal to $23$ units multiplied by the product of the codes of hubs $p_1, p_4$, and $p_5$. Added to this is an auxiliary power boost, calculated as a constant integer $k$ multiplied by the square root of $(2015 \times p_1 \times p_2 \times p_3)$. For the drone to maintain a stable flight, this total must exactly equal the square of the code for hub $p_1$ multiplied by the product of the codes for hubs $p_2$ and $p_3$.

Given that $k$ must be a positive integer, find the smallest possible value of $k$ that allows this energy balance equation to hold true for some set of prime hub codes.

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
