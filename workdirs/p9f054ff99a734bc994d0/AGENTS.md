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

A high-security digital vault requires a unique prime number code, denoted as $p$, to be unlocked. This code is engineered such that it can be decomposed into different structural configurations across ten distinct security layers.

For each security layer $k$ (where $k$ ranges from 1 to 10), the code $p$ must satisfy a specific weighted sum of two integer-based security keys, $a_k$ and $b_k$. Specifically, for any given layer $k$, the code must be representable as:
$p = a_k^2 + k \cdot b_k^2$

This means:
- In the 1st layer, the code satisfies $p = a_1^2 + 1b_1^2$.
- In the 2nd layer, the code satisfies $p = a_2^2 + 2b_2^2$.
- In the 3rd layer, the code satisfies $p = a_3^2 + 3b_3^2$.
- This pattern continues identically up to the 10th layer, where $p = a_{10}^2 + 10b_{10}^2$.

If $a_i$ and $b_i$ are required to be integers for all layers $i \in \{1, 2, \dots, 10\}$, find the value of the prime number code $p$.

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
