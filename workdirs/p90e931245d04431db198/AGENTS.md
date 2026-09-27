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

A specialized logistics hub manages a fleet of 100 delivery drones, indexed from 1 to 100. A dispatcher needs to select a subset of these drones, $S$, to form a strategic task force. To ensure the robustness and connectivity of the fleet, the selection must satisfy two operational protocols regarding the "shared frequency" $(x, y)$, defined as the greatest common divisor of the drones' index numbers $x$ and $y$:

i) Every drone selected for $S$ must have an index number from the available range of 1 to 100 inclusive.

ii) For any two drones $a$ and $b$ chosen for the task force, there must exist at least one drone $c$ in the task force that is "frequency-independent" from both, meaning the shared frequency between $a$ and $c$ is 1, and the shared frequency between $b$ and $c$ is also 1.

iii) For any two drones $a$ and $b$ chosen for the task force, there must exist at least one drone $d$ in the task force that is "frequency-linked" to both, meaning the shared frequency between $a$ and $d$ is greater than 1, and the shared frequency between $b$ and $d$ is also greater than 1.

Determine the maximum possible number of drones that can be included in the task force $S$ while satisfying these conditions.

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
