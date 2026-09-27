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

In a specialized logistics center, three transport drones are assigned to deliver a combined total of 400 kilograms of cargo. The cargo is pre-packaged into containers of three specific weight classes: 50 kg, 20 kg, and 10 kg. 

To maintain balance, the following operational constraints are strictly enforced:
1. Each drone is permitted to carry containers of only one weight class (for example, if Drone A carries 20 kg containers, every container it carries must weigh exactly 20 kg).
2. The denominations of weight assigned to each drone (50, 20, or 10) do not have to be unique; multiple drones may be assigned the same container weight class.
3. The total weight carried by the three drones must sum to exactly 400 kg.
4. For synchronization purposes, the quantity of containers loaded onto one of the drones must be exactly equal to the mathematical product of the quantities of containers loaded onto the other two drones.

Based on these constraints, how many distinct ways are there to assign the container weights and the number of containers to the three drones?

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
