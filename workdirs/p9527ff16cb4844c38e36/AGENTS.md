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

Given a nonconstant geodesic $\gamma \in \Omega_{p,q}$ with no conjugate points in the interval $0 < \tau \leq 1$, let $\mathcal{H}_\gamma$ be the Hessian operator associated with $\gamma$. Suppose the smallest eigenvalue of $\mathcal{H}_\gamma$ is positive, and let $a > 0$ be the constant such that the inequality 
\[
\int_0^1 \left(|\nabla X|^2 - \langle R(X, \dot{\gamma}) \dot{\gamma}, X \rangle \right) dt \geq a \int_0^1 |X(t)|^2 dt
\]
holds for all $X \in \operatorname{Vect}_0(\gamma)$. Further, let $b > 0$ be a constant such that $\langle R(v, \dot{\gamma}(t)) \dot{\gamma}(t), v \rangle \leq b|v|^2$ for all $t \in [0,1]$ and $v \in T_{\gamma(t)} M$. Verify that the estimate 
\[
\int_0^1 \left(|\nabla X|^2 - \langle R(X, \dot{\gamma}) \dot{\gamma}, X \rangle \right) dt \geq \varepsilon \int_0^1 \left(|\nabla X(t)|^2 + |X(t)|^2 \right) dt
\]
holds for $\gamma' = \gamma$ and $X \in \operatorname{Vect}_0(\gamma)$ with $\varepsilon = \frac{a}{a + b + 1}$.

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
