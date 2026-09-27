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

Consider the smooth compact manifolds $X$ and $Y$. Let $C^{-\infty}(X \times Y)$ denote the space of generalized functions on the product manifold $X \times Y$. Define the canonical linear map \( T: C^{-\infty}(X \times Y) \to \text{Bil}(C^\infty(X), C^\infty(Y)) \), where the target is the space of continuous bilinear functionals from \( C^\infty(X) \times C^\infty(Y) \to \mathbb{C} \). The map is given by \( (T\Phi)(f,g) = \Phi(f \otimes g) \). It is known that \( T \) is an isomorphism of vector spaces. Determine the standard topologies on the source and target for which \( T \) is an isomorphism of topological vector spaces. Specifically, consider the strong topology on \( C^{-\infty}(X \times Y) \) and the topology on the target given by the seminorms \( ||B||_{K,L} = \sup_{k \in K, l \in L} |B(k,l)| \), where \( K \subset C^\infty(X) \) and \( L \subset C^\infty(Y) \) are arbitrary bounded subsets. Is \( T \) a topological isomorphism under these conditions?

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
