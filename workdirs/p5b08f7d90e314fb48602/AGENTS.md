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

In a remote industrial network, a sequence of $n$ pressure valves is arranged in a line, with their pressure levels denoted as $a_0, a_1, \ldots, a_n$. Due to safety stabilization protocols, the pressure at the two boundary terminals must be zero, such that $a_0 = a_n = 0$.

Engineers have discovered that the pressure at any internal valve $k$ (where $1 \leq k \leq n-1$) is governed by a constant environmental factor $c$ and the cumulative feedback of the downstream valves. Specifically, the pressure at valve $k$ is maintained according to the mechanical equilibrium:
\[ a_k = c + \sum^{n-1}_{i=k} a_{i-k} \cdot \left(a_i + a_{i+1} \right) \]

For any fixed number of segments $n$, there exists a maximum threshold for the environmental factor, $C_{max}(n)$, beyond which the system of equations has no real-valued solutions for the pressure levels $a_k$.

Calculate the total sum of the reciprocals of these maximum thresholds for systems ranging from size 1 to 10:
\[ \sum_{n=1}^{10} \frac{1}{C_{max}(n)} \]

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
