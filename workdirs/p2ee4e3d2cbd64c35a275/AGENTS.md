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

In a highly secure logistics hub, a central computer manages cargo using a capacity modulus $m = 2^2 \cdot 3^3 \cdot 5^5 = 337,500$. The hub operates $n$ different shipping lanes. For each lane $i$, the system assigns two specific "routing coefficients," $a_i$ and $b_i$, which are fixed integers.

To authorize a transport cycle, a logistics officer must determine a set of "load factors" $x_1, x_2, \dots, x_n$ (where each $x_i$ is an integer) that satisfy two strict security protocols:

1.  **Validation Protocol:** At least one load factor $x_i$ must be coprime to the capacity modulus $m$ (meaning $\gcd(x_i, m) = 1$).
2.  **Equilibrium Protocol:** The total weighted load across both routing dimensions must be perfectly balanced relative to the modulus. Specifically, the sum $\sum_{i=1}^n a_i x_i$ must be a multiple of $m$, and the sum $\sum_{i=1}^n b_i x_i$ must also be a multiple of $m$.

The system is designed such that for a specific number of lanes $n$, these load factors can be found regardless of which integer values are chosen for the routing coefficients $a_i$ and $b_i$.

Find the smallest positive integer $n$ that guarantees such a set of load factors $x_1, \dots, x_n$ always exists for any possible choice of $a_1, \dots, a_n$ and $b_1, \dots, b_n$.

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
