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

In a specialized logistics facility, there is a vault containing 1000 unique metal storage crates, each labeled with a distinct integer ID from 1 to 1000. The dimensions of each crate (length, width, and height) are all equal to its ID number.

An inspector randomly selects 3 crates from the vault to form a "Cargo Set." These crates are removed from the vault. From the remaining 997 crates, the inspector randomly selects another 3 crates to form a "Housing Set." 

Let $a_1, a_2,$ and $a_3$ be the ID numbers of the three crates in the Cargo Set. These three values are used to define the dimensions of a single rectangular brick: $a_1 \times a_2 \times a_3$. 

Let $b_1, b_2,$ and $b_3$ be the ID numbers of the three crates in the Housing Set. These three values are used to define the internal dimensions of a single rectangular box: $b_1 \times b_2 \times b_3$.

The inspector wishes to determine the probability $p$ that the $a_1 \times a_2 \times a_3$ brick can be placed entirely inside the $b_1 \times b_2 \times b_3$ box, such that the sides of the brick are parallel to the sides of the box (allowing for any rotation of the brick by 90-degree increments).

If $p$ is expressed as a fraction in lowest terms, what is the sum of the numerator and the denominator?

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
