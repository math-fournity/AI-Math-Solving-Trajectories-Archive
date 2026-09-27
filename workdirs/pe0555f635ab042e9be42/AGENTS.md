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

A logistics company is tasked with assigning $n$ packages, labeled $1, 2, \dots, n$ based on their weight in kilograms, into three shipping containers. Every package must be assigned to exactly one container, though some containers may remain empty. The arrangement of packages within each container is irrelevant to the shipping logs, meaning the assignment is defined only by which packages end up together; for example, if the same groups of packages are formed, the assignment is considered identical regardless of whether a group is labeled "Container A" or "Container B."

The company must adhere to two strict safety protocols:

1.  **Vibration Stability:** In any container, if the packages are sorted by weight from lightest to heaviest, the parity of the labels of any two consecutive packages must be different (i.e., an even label cannot follow an even label, and an odd label cannot follow an odd label).
2.  **Initial Load Balance:** If all three containers are utilized (none are empty), it is mandatory that at least one container’s lightest package has an even-numbered label.

Calculate the total number of distinct ways to partition the $n$ packages into these three containers such that both protocols are satisfied.

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
