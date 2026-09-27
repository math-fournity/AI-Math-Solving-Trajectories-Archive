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

Let $\Omega \subset \mathbb{R}^n$ be a bounded and open set, and consider a Carathéodory function $a: \Omega \times \mathbb{R} \times \mathbb{R}^n \rightarrow \mathbb{R}^n$ that satisfies the following conditions:
1. $a(x,.,.)$ is continuous on $\mathbb{R} \times \mathbb{R}^n$ for almost every $x \in \Omega$.
2. $a(.,s,\xi)$ is measurable in $\Omega$ for every $(s,\xi) \in \mathbb{R} \times \mathbb{R}^n$.
3. There exist $k \in L^{p'}(\Omega)$, $\beta \geq 0$, and $p > 1$ such that $p' = \frac{p}{p-1}$, and
   $$|a(x,s,\xi)| \leq k(x) + \beta(|s|^{p-1}+|\xi|^{p-1})$$
   for almost every $x \in \Omega$ and every $(s,\xi) \in \mathbb{R} \times \mathbb{R}^n$.

If $u_m \rightarrow u$ in $L^{\infty}(\Omega)$ and $u_m \rightarrow u$ uniformly, does it follow that
$$a(x,u_m, \xi) \rightarrow a(x,u,\xi) \text{ in } L^{1}(\Omega)?$$

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
