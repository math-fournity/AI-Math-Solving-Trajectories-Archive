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

A logistics company operates a central distribution hub organized into a massive rectangular grid of storage bays. The floor plan consists of 53 horizontal aisles, and each aisle contains exactly 47 individual bays. To organize the facility, the manager assigns a unique identification number to every bay: the first aisle is numbered 1 through 47 from left to right, the second aisle 48 through 94, and this pattern continues sequentially until the last bay in the 53rd aisle.

The company uses an automated sorting system that only activates bays whose identification numbers can be expressed as a linear combination of the dimensions of the grid. Specifically, a bay is "activated" if its ID number $N$ satisfies the equation $N = 47x + 53y$ for some non-negative integers $x$ and $y$. 

All bays that do not meet this mathematical criterion remain "deactivated." These deactivated bays form a single, unbroken contiguous region $R$ within the grid (where "contiguous" means the bays are connected to one another horizontally or vertically). 

Calculate the total perimeter of this deactivated region $R$, defined as the total number of exterior unit-length edges surrounding the cluster of deactivated bays.

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
