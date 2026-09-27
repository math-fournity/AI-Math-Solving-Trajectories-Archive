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

In a specialized historical archive, three sequential storage vaults are labeled with the consecutive positive integers $n$, $n+1$, and $n+2$. An auditor is examining the properties of these three identification numbers to verify the security of the collection. The following observations are recorded:

1. For one of the vault numbers, the sum of its decimal digits is a prime number.
2. For another vault number, the sum of its decimal digits is an even perfect number (where a number $k$ is perfect if the sum of its divisors equals $2k$).
3. For the third vault number, the sum of its decimal digits is exactly equal to the total number of its positive divisors.
4. Within the decimal representation of each individual vault number, the digit '1' appears at most twice.
5. If the constant 11 is added to exactly one of the three vault numbers, the resulting sum is a perfect square.
6. Each of the three vault numbers possesses exactly one prime divisor that is less than 10.
7. All three vault numbers are square-free, meaning no prime factor is repeated in their prime factorization.

Calculate the sum of the identification numbers of the three vaults, $n + (n+1) + (n+2)$.

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
