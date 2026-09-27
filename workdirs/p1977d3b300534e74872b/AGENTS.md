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

A specialized logistics hub is managing a fleet of 2020 identical delivery drones, each currently carrying a 1-ton payload. In this facility, two operators, Controller A and Controller B, manage the consolidation of cargo through a series of rounds.

In each round, Controller A selects any two cargo containers (with weights $x$ and $y$) currently in the bay and moves them to the processing station. Controller B then decides how to consolidate them: they can either merge them into a single container with a weight of $x+y$, or they can use one to offset the other, resulting in a single container with a weight of $|x-y|$.

The operation continues until one of two terminal conditions is met at the end of a round:
1. The weight of one specific container is strictly greater than the combined weight of all other remaining containers.
2. Every container remaining in the bay has a weight of exactly 0.

Upon termination, Controller B must pay a "processing fee" to Controller A. The fee is exactly one gold coin for every container remaining in the bay at that moment. Controller A acts to maximize the total number of coins received, while Controller B acts to minimize the payment.

If both controllers follow their optimal strategies, what is the total number of gold coins that Controller A will receive?

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
