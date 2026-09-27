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

In a remote industrial sector, 9 specialized quality inspectors are assigned to evaluate 12 different shipments of raw minerals. For each shipment, an inspector must assign a unique "impurity rank" from 1 to 12, where a rank of 1 indicates the highest purity and a rank of 12 indicates the lowest purity. Each of the 12 ranks must be used exactly once by every inspector.

After the inspections are completed, the data reveals a high level of consistency: for any given shipment, the difference between the highest rank it received and the lowest rank it received across all 9 inspectors is at most 3.

The total "quality burden" for each shipment is calculated by summing the 9 ranks it received. Let these total burdens be denoted as $c_{1}, c_{2}, \dots, c_{12}$. When these totals are sorted in non-decreasing order such that $c_{1} \le c_{2} \le \dots \le c_{12}$, what is the maximum possible value that the smallest total burden, $c_{1}$, can take?

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
