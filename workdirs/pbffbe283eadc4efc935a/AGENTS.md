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

In the city of Arithmos, two rival logistics managers, Jacob and Laban, are tasked with filling a central silo. Each manager has a private warehouse containing exactly 2021 crates. The weights of the crates in each warehouse are the squares of the integers from 1 to 2021 (i.e., $1^2, 2^2, 3^2, \dots, 2021^2$ units).

The silo currently contains 0 units of material. The managers take turns adding to the silo, with Jacob always taking the first turn. In each turn, a manager selects one crate from their own warehouse that has not been used yet, records its weight, and adds its contents to the silo’s total weight. They continue alternating turns until both warehouses are completely empty (a total of 4042 crates added).

The city council has decreed that every time the total weight of the material in the silo is exactly divisible by 4 after a manager completes their turn, Jacob is awarded one unit of credit. 

Jacob wants to maximize his total credits, while Laban, seeking to minimize Jacob's success, will play as strategically as possible to prevent the silo weight from being a multiple of 4. What is the maximum number of credits $K$ that Jacob can guaranteed to earn, regardless of how Laban chooses his crates?

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
