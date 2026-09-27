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

In a cutting-edge data center, a rectangular cluster of 9 processing nodes is organized into a rigid $3 \times 3$ grid. The node located at the top-left corner (Row 1, Column 1) is pre-configured as the "Primary Server," while the node at the bottom-right corner (Row 3, Column 3) is pre-configured as the "Backup Server."

The remaining 7 nodes must be assigned to one of two isolated sub-networks: the Primary Network or the Backup Network. To ensure system stability, the assignments must follow a strict connectivity rule:

1. Every node assigned to the Primary Network must be able to reach the Primary Server by moving only horizontally or vertically through other nodes assigned to the Primary Network.
2. Every node assigned to the Backup Network must be able to reach the Backup Server by moving only horizontally or vertically through other nodes assigned to the Backup Network.

No communication path can pass through a node belonging to the opposite network.

How many different ways can the 7 remaining nodes be assigned to these two networks such that these connectivity requirements are satisfied for both the Primary and Backup systems?

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
