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

Consider a holomorphic function $W(t_1,\dotsc,t_n)$ defined on a connected open set $U$ of $\mathbb{C}^n$. Let $\mathbf{t}^{(0)}$ be a point in $U$. Suppose there exists a cycle $\gamma$ in $\mathbb{C}^m$ and a rational function $F(\mathbf{t}, x_1,\dotsc, x_m)$ such that for all $\mathbf{t}$ in a neighborhood of $\mathbf{t}^{(0)}$:

1. The map $\mathbf{x} \mapsto F(\mathbf{t}, \mathbf{x})$ is continuous on $\gamma$.
2. $W(\mathbf{t}) = \oint_\gamma F(\mathbf{t}, \mathbf{x})\mathrm{d} \mathbf{x}$.

Is it true that for every point $\mathbf{t}^{(1)}$ in $U$, there exists another cycle $\gamma_1$ such that these properties hold in a neighborhood of $\mathbf{t}^{(1)}$?

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
