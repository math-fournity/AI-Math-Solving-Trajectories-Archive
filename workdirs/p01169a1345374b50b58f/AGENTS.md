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

A high-security storage facility consists of a $5 \times 5$ grid of storage units. There are 21 specialized climate-controlled units (the "white units") located at every coordinate $(row, column)$ except for $(2,2)$, $(3,2)$, $(3,4)$, and $(4,4)$. 

The facility manager must assign 21 specific radioactive canisters to these units. Each canister is labeled with a unique two-digit prime number: 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, and 97. Each canister must be used exactly once.

Safety protocols dictate that if two white units share a wall (side-by-side or one above the other), the canisters inside them must be "compatible." Compatibility is defined as having either the same tens digit or the same ones digit.

Due to weight and shielding constraints, specific units are already designated to hold canisters containing a particular digit:
- The unit at (1,1) must hold a canister containing the digit 3.
- The unit at (1,3) must hold a canister containing the digit 3.
- The unit at (1,5) must hold a canister containing the digit 8.
- The units at (3,1), (3,3), and (3,5) must each hold a canister containing the digit 9.
- The unit at (5,1) must hold a canister containing the digit 6.
- The unit at (5,3) must hold a canister containing the digit 1.
- The unit at (5,5) must hold a canister containing the digit 4.

Calculate the sum of the five prime numbers assigned to the units in the first row.

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
