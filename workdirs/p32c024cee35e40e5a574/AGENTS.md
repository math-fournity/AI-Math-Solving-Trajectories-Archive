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

In a specialized laboratory, there are 2013 distinct vials containing experimental liquid isotopes. These vials are labeled with the integers $\{1, 2, \dots, 2013\}$. It is known that the actual concentrations of these isotopes in the vials are also exactly $\{1, 2, \dots, 2013\}$ units, but the labels may have been shuffled so that the number on a vial does not necessarily match the concentration of the liquid inside. Each concentration value is used exactly once across the set of vials.

The lab possesses a high-precision digital differential scale. When a group of vials is placed on the left platform and another group is placed on the right platform, the scale outputs a single numerical value representing the exact difference between the sum of the concentrations on the left and the sum of the concentrations on the right (Left Sum minus Right Sum).

An auditor needs to verify if every single vial's label correctly identifies its internal concentration. This must be guaranteed regardless of how the labels were initially misapplied. If $k$ is the minimum number of measurements required on the differential scale to uniquely determine whether every vial is labeled correctly, what is the value of $k$?

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
