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

In the competitive world of high-performance server cooling, a system’s "Efficiency Rating" is a function $f$ that maps an integer workload level $x \in \mathbb{Z}$ to an integer power consumption value $f(x) \in \mathbb{Z}$. 

A cooling system is classified as "Ultra-Resilient" if it satisfies a specific safety redundancy constraint: for any two workload levels assigned to the system, $m$ and $n$, the sum of their respective power consumption values must strictly exceed the square of the larger workload. That is, $f(m) + f(n) > \max(m^2, n^2)$ for all pairs of integers $m$ and $n$.

A team of engineers is designing an Ultra-Resilient system such that the total power consumption for the first thirty positive integer workloads, represented by the sum $\sum_{i=1}^{30} f(i)$, is minimized.

Under the condition that the system is designed to achieve this minimum possible total sum, what is the smallest possible power consumption value for a workload level of 25 (i.e., the minimum possible value of $f(25)$)?

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
