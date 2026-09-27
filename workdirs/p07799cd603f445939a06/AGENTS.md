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

A specialized deep-sea sensor probe utilizes a primary recursive processing unit. The core algorithm, designated as $p_1(x)$, transforms an input signal $x$ according to the cubic function $4x^3 - 3x$. For advanced data layers, the probe uses higher-order processing where the $(n+1)$-th iteration, $p_{n+1}(x)$, is defined by feeding the output of the $n$-th iteration back into the primary algorithm: $p_{n+1}(x) = p_1(p_n(x))$.

A calibration state occurs when the output of a processing layer exactly matches its input, such that $p_n(x) = x$. For any given iteration $n$, let $A(n)$ be the set of all unique real-valued signals $x$ that result in this calibration state.

The mission logs require two specific metrics for these calibration sets:
1. $P(n)$ is defined as the product of all signal values contained in the set $A(n)$.
2. $M(n)$ is defined as the arithmetic mean of all signal values contained in the set $A(n)$.

Calculate the exact value of the ratio $\frac{M(8)}{P(4)}$.

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
