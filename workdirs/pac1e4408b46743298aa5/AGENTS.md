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

Consider a three-dimensional space with origin $O$. You have a finite number of points $P_1, P_2, \cdots, P_n$, each assigned a nonzero integer charge $q_i$. For any other point $R$ in the space, define the vector function $$\vec{F(R)} = \sum_{i = 1}^{n} \frac{q_i}{D(P_i, R)^2} \vec{r_i},$$ where $D(P_i, R)$ is the Euclidean distance between $P_i$ and $R$, and $\vec{r_i}$ is a unit vector directed from $P_i$ to $R$. Now, choose a ray $\vec{\ell}$ originating from $O$ in any direction. Is it true that for any configuration of points and charges, there exists a rational number $\alpha$ such that $$\lim_{x \rightarrow \infty} \| F(R_x) \| x^{\alpha}$$ converges to a nonzero constant, where $R_x \in \ell$ with $D(O, R_x) = x$ and $\| F(R_x) \|$ is the magnitude of the function at $R_x$?

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
