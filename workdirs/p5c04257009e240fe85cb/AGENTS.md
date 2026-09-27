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

In a remote digital archive, a signal processing unit generates a sequence of data packets $(x_n)$. The initial packet density is determined by two security clearance levels, $m$ and $k$, which are integers satisfying the condition $m > k \geq 0$. These levels correspond to terms in the Fibonacci sequence $(F_n)$, where the sequence begins with $F_0 = 1, F_1 = 1$ and follows the rule $F_{n+2} = F_n + F_{n+1}$ for all $n \geq 0$.

The initial density is set as $x_0 = \frac{F_k}{F_m}$. For every subsequent step $n \geq 0$, the unit updates the packet density according to the following logic:
- If the current density $x_n$ is not exactly $1$, the next density is calculated as $x_{n+1} = \frac{2x_n - 1}{1 - x_n}$.
- If the density $x_n$ reaches exactly $1$, it remains $1$ for all future steps ($x_{n+1} = 1$).

A "Stable State" occurs for a pair of clearance levels $(k, m)$ if the sequence of densities $(x_n)$ eventually hits the value $1$. 

Let $S$ be the set of all such pairs $(k, m)$ that result in a Stable State. Determine the total number of pairs $(k, m)$ in set $S$ that satisfy the additional constraint $m \leq 100$.

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
