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

Consider the ring of symmetric polynomials $\Lambda_N=\mathbb{C}[x_1, \ldots, x_N]^{S_N}$ in $N$ variables and its subspace of homogeneous symmetric polynomials of degree $M$, denoted by $\Lambda_N^M$. A polynomial $f\in \Lambda_N$ is said to have a $(k,r)$-clustering property if it satisfies the following condition for some $g\in \mathbb{C}[Z, x_{k+1}, \ldots, x_N]$:

$$ f(\underbrace{Z,Z,\cdots, Z}_{k\text{ times}}, x_{k+1},\ldots, x_N)=\prod_{i=k+1}^N(Z-x_i)^r g(Z,x_{k+1}, \ldots, x_N) $$

Let $V_{N,M}^{(k,r)}$ be the $\mathbb{C}$-vector space spanned by homogeneous symmetric polynomials of degree $M$ with the $(k,r)$-clustering property. For $N=nk$ and $M=n(n-1)nk/2$, where $k+1$ and $r-1$ are coprime, determine if the following statement is true:

$$ \dim V^{(k,r)}_{N,M}=1 $$

It is known that $V_{N,M}^{(k,r)}\neq \{0\}$ because the Jack polynomial $P^{\alpha}_{\Lambda}(x_1, \ldots, x_N)$, with $\Lambda$ being a specific partition and $\alpha=-\frac{r-1}{k+1}$, is well-defined and belongs to $V_{N,M}^{(k,r)}$. Is this polynomial the only one with the given properties?

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
