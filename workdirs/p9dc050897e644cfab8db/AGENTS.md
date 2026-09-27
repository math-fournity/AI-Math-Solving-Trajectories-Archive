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

In the competitive world of cloud computing, three data centers—Alpha, Beta, and Gamma—operate with processing capacities of $A, B$, and $C$ petaflops, respectively ($A, B, C > 0$). 

The "Efficiency Rating" of each center is calculated by dividing its individual capacity by the sum of its capacity squared and a "Cross-interference Factor." This factor is determined by a universal system constant $K$ ($K > 0$) multiplied by the capacities of the other two centers. Specifically, the ratings are:
- Alpha: $\frac{A}{A^2 + KBC}$
- Beta: $\frac{B}{B^2 + KAC}$
- Gamma: $\frac{C}{C^2 + KAB}$

A global regulatory board mandates that the total sum of these three Efficiency Ratings must never exceed a specific "Network Benchmark." This benchmark is calculated by taking the sum of the reciprocals of the three capacities—$\left( \frac{1}{A} + \frac{1}{B} + \frac{1}{C} \right)$—and scaling it by a factor of $\frac{1}{K+1}$.

Determine the maximum possible value of the constant $K$ such that the total sum of the three Efficiency Ratings remains less than or equal to the Network Benchmark for any possible positive capacities $A, B$, and $C$.

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
