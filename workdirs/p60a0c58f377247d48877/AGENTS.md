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

In a specialized logistics warehouse, there are $n$ distinct packages labeled with identification numbers from $\{1, 2, \cdots, n\}$. These packages must be distributed into three specific storage bays: Bay 1, Bay 2, and Bay 3. To maintain structural stability and organizational efficiency, the warehouse manager enforces two strict protocols:

1. **The Parity Sequence Protocol:** Within each bay, if you line up the assigned packages in increasing order of their identification numbers, no two adjacent packages can have the same parity. That is, an even-numbered package must be followed by an odd-numbered package, and vice versa.

2. **The Minimum Entry Protocol:** If every bay receives at least one package, the manager checks the package with the lowest identification number in each of the three bays. According to safety regulations, exactly one of those three "minimum" packages must be an even-numbered package.

Note that it is permissible for one or more bays to remain completely empty. If any bay is empty, the second protocol regarding minimum elements does not apply to that empty bay.

How many different ways can the $n$ packages be distributed among the three bays such that both protocols are satisfied?

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
