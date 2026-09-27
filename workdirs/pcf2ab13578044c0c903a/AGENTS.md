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

In a specialized logistics network, a system of $n$ interconnected hubs requires specific integer-coded frequency settings, denoted as $a_1, a_2, \dots, a_n$. These settings are used to configure a master control function for the $n$-th generation network, defined by the formula:
$$P_n(x) = x^n + a_1 x^{n-1} + a_2 x^{n-2} + \dots + a_{n-1} x + a_n$$
A system is considered "perfectly synchronized" if and only if the $n$ roots of the function $P_n(x)$ are exactly the same values as the integer coefficients $a_1, a_2, \dots, a_n$ (accounting for their multiplicities).

For any fixed network size $n$, let $S_n$ be the set of all possible perfectly synchronized control functions. We define the "total interference" of a single function as the sum of the absolute values of its settings: $|a_1| + |a_2| + \dots + |a_n|$. 

Furthermore, let $g(n)$ represent the sum of these total interference values across all unique control functions contained in $S_n$. 

Calculate the cumulative interference across the first four generations of network sizes, specifically the value of:
$$g(1) + g(2) + g(3) + g(4)$$

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
