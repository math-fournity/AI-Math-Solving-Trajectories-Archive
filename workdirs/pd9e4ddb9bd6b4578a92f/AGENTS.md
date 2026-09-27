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

In a remote high-security server farm, a $4 \times 4$ array of 16 processing cores is arranged in a square grid. Each core is assigned a specific security clearance level ranging from 1 to 4. The distribution of these clearance levels across the grid is as follows:

- The first row contains levels 1, 2, 3, and 4 in that order.
- The second row contains levels 2, 3, 4, and 1.
- The third row contains levels 3, 4, 1, and 2.
- The fourth row contains levels 4, 1, 2, and 3.

To optimize data flow, the system administrator must partition all 16 cores into exactly four distinct subnetworks. These subnetworks must adhere to three strict protocols:
1. **Capacity Constraint:** Each subnetwork must consist of exactly four cores.
2. **Connectivity Constraint:** Each subnetwork must be physically connected, meaning any two cores within a subnetwork must be reachable from one another through a sequence of horizontally or vertically adjacent cores belonging to that same subnetwork.
3. **Diversity Constraint:** Each subnetwork must contain exactly one core of each security level (one core of level 1, one of level 2, one of level 3, and one of level 4).

In how many distinct ways can the administrator partition the grid into four subnetworks while satisfying all three protocols?

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
