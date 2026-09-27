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

A specialized deep-sea salvage drone is tasked with locating a sunken research module positioned at an unknown integer depth $m$ meters below the surface, where $1 \leq m \leq 1001$. 

The drone’s battery management system operates under a specific cost protocol for every descent attempt:
1. To initiate any single descent to a target depth $k$, the drone consumes a flat fee of $1$ unit of energy.
2. If the module is located at or below the drone's target depth ($m \geq k$), the drone successfully docks. Upon docking, it consumes an additional amount of energy equal to the distance remaining to reach the module, which is exactly $m - k$ units. The mission then ends.
3. If the module is shallower than the target depth ($m < k$), the drone fails to dock, consumes a heavy penalty of $10$ units of energy due to emergency stabilization, and must be reset at the surface to attempt another guess.

The drone operator wishes to program the first target depth $k$ such that, even in the absolute worst-case scenario for the module's location $m$, the total energy consumed is kept to the absolute minimum possible. 

What integer value should the operator choose for the drone's first target depth $k$ to minimize this maximum potential energy expenditure?

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
