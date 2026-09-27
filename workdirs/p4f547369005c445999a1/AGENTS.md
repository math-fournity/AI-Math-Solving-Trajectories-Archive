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

In a specialized logistics hub, three automated shipping containers are being calibrated based on their volumetric efficiency ratings. The efficiency of each container is calculated using the formula $x(x+3)$, where $x$ represents a specific characteristic integer of the container.

Two "Primary" containers have characteristic ratings $p$ and $q$, where both $p$ and $q$ must be prime numbers. A third "Standard" container has a characteristic rating $n$, where $n$ is a positive integer. The hub’s power grid remains stable only if the combined efficiency of the two Primary containers exactly equals the efficiency of the Standard container. This balance is defined by the equilibrium equation:
$$p(p+3) + q(q+3) = n(n+3)$$

Let $S$ be the set of all possible ordered triples $(p, q, n)$ that satisfy this equilibrium condition. To finalize the system's safety report, you must identify every valid configuration in $S$ and calculate the total sum of the squares of the ratings for all such configurations.

Find the sum of $p^2 + q^2 + n^2$ for all $(p, q, n) \in S$.

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
