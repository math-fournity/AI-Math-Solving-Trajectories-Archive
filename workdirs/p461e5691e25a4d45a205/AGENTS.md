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

In a specialized semiconductor fabrication facility, a precision engineering project is organized around a prime number of master nodes, denoted by $p$. To ensure data redundancy across the network, the facility establishes a total of $N = (p-1)(p-2)$ secondary processing units.

Each processing unit is assigned a unique identification index $k$, where $k$ ranges from $1$ to $(p-1)(p-2)$. The computational load for a specific unit $k$ is determined by a specific efficiency formula: first, the index $k$ is multiplied by the number of master nodes $p$; then, the cube root of this product is calculated. To maintain system stability, the unit only processes the integer portion of this result (the floor of the cube root).

The facility manager needs to determine the total aggregate workload $S(p)$ of the entire system, defined as the sum of these integer workloads across all $N$ units.

Find the value of $S(p) = \sum_{k=1}^{(p-1)(p-2)} \lfloor \sqrt[3]{kp} \rfloor$ in terms of $p$.

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
