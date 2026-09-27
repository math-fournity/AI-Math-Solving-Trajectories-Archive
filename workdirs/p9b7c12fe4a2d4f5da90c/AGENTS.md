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

A specialized chemical refinery operates using two types of thermal catalysts, Code-5 and Code-2. The efficiency of a reaction is determined by a "Stability Index" ($I$), which must be a perfect square of an integer to prevent equipment failure.

**Phase A: Standard Operations**
A technician explores configurations where the refinery uses $m$ units of Code-5 catalyst and $n+1$ units of Code-2 catalyst. The Stability Index for this phase is calculated by the formula:
$$I_a = \frac{5^{m} + 2^{n+1}}{5^{m} - 2^{n+1}}$$
Let $S_a$ be the set of all pairs of positive integers $(m, n)$ that result in $I_a$ being a perfect square.

**Phase B: Variable Prime Operations**
The refinery introduces a third additive, a rare element represented by a prime number $p$. In this configuration, the refinery uses $m$ units of Code-5 and $n$ units of Code-2, combined with the prime additive $p$. The Stability Index for this phase is:
$$I_b = \frac{5^{m} + 2^{n} \cdot p}{5^{m} - 2^{n} \cdot p}$$
Let $S_b$ be the set of all triples of positive integers $(m, n, p)$, where $p$ is a prime number, that result in $I_b$ being a perfect square.

**The Final Objective:**
Calculate the total "Resource Load" of the refinery's valid configurations. This is defined as the sum of $(m + n)$ for every pair in $S_a$, plus the sum of $(m + n + p)$ for every triple in $S_b$.

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
