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

In a futuristic digital city, an architect is designing a high-security encryption gate. To unlock the gate, two security codes, $m$ and $n$, must be selected from a secure server containing integers ranging from $0$ to $2023$, inclusive.

The gate’s processing core operates on a cycle of $2024$ units. For the codes to be valid, the architect dictates that the "Square-Load" of the first code must perfectly synchronize with the "Divisor-Sum" of the second code within the city's $2024$-unit cycle.

The "Square-Load" is defined as the value of the first code squared ($m^2$). 

The "Divisor-Sum" is a complex calculation based on the number $2023$. To find it, one must identify every positive integer $d$ that is a divisor of $2023$. The second code $n$ is then raised to the power of each of these divisors individually, and all the resulting values are summed together ($\sum_{d \mid 2023} n^d$).

The gate unlocks only if the Square-Load is congruent to the Divisor-Sum modulo $2024$.

How many distinct ordered pairs of security codes $(m, n)$ exist that will successfully unlock the encryption gate?

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
