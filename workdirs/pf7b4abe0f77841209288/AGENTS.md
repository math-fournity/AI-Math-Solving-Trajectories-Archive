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

A logistics company manages a fleet of 301 distinct automated storage bins, indexed from 0 to 300. Each bin $i$ is assigned a power capacity $f(i)$, which must be a non-negative integer. Due to system constraints, the capacities must be non-increasing, such that $f(0) \geq f(1) \geq f(2) \geq \dots \geq f(300) \geq 0$. Furthermore, the total power allocated across all 301 bins cannot exceed 300 units: $\sum_{i=0}^{300} f(i) \leq 300$.

The company also maintains a performance efficiency rating $g(k)$ for any total workload $k$, where $k$ is a non-negative integer. This rating $g$ is constrained by the power capacities of the bins. Specifically, for any selection of 20 workloads $n_1, n_2, \dots, n_{20}$ (where each $n_j$ is a non-negative integer), the efficiency of their sum is bounded by the sum of the capacities of the corresponding bins:
$$g(n_1 + n_2 + \dots + n_{20}) \leq f(n_1) + f(n_2) + \dots + f(n_{20})$$

Given these constraints, determine the maximum possible value of the total efficiency sum for all workloads from 0 to 6000:
$$\sum_{k=0}^{6000} g(k)$$

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
