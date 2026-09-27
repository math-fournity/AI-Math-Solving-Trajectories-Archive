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

In a remote industrial refinery, three chemical processors—Alpha ($x$), Beta ($y$), and Gamma ($z$)—manage non-negative quantities of raw catalysts. The total energy output of the facility is determined by a complex interaction between these processors.

The "Primary Combustion" energy is calculated by summing the cubes of the individual catalyst quantities: $x^3 + y^3 + z^3$. 

Additionally, there is a "Secondary Reaction" efficiency constant, $C$. This constant scales the sum of the products formed by each processor interacting with the square of the next one in the sequence: $C(xy^2 + yz^2 + zx^2)$.

To ensure the refinery remains stable, the sum of the Primary Combustion and the Secondary Reaction must always be greater than or equal to a "Threshold Limit." This limit is defined by the factor $(C + 1)$ multiplied by the sum of the products formed by the square of each processor interacting with the next one: $(C + 1)(x^2y + y^2z + z^2x)$.

As the lead systems engineer, your task is to calibrate the facility. What is the maximum possible value of the constant $C$ such that this stability inequality holds for all possible non-negative catalyst levels $x, y,$ and $z$?

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
