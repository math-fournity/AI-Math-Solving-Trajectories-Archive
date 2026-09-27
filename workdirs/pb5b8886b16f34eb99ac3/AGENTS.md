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

In a specialized digital archive, a researcher is exploring a hierarchy of security clearances organized into 2011 distinct tiers. 

To determine the final encryption key $N$, the researcher must calculate the sum of the products of clearance levels assigned to a sequence of 2011 officers, denoted as $a_1, a_2, a_3, \dots, a_{2011}$. The levels are assigned based on a strict chain of command:
- The first officer's level, $a_1$, can be any integer from $0$ to $2$.
- Each subsequent officer's level, $a_n$, must be an integer such that $0 \le a_n \le a_{n-1}$ for all $n$ from $2$ to $2011$.

For every possible valid sequence of levels $(a_1, a_2, \dots, a_{2011})$, the researcher calculates the product of all levels in that sequence: $(a_1 \times a_2 \times a_3 \times \dots \times a_{2011})$. 

The value $N$ is the sum of these products over all possible sequences. Find the remainder when $N$ is divided by 1000.

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
