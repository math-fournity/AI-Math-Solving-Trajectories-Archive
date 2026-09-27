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

In the futuristic city of Omelas, a grand computational engine relies on a biological processor governed by a prime frequency $p$, where $p > 2$. The engine’s total processing power, $N$, is determined by the ratio of high-intensity cycles to the stability of its cooling units.

Specifically, the engine executes a sequence of high-intensity operations totaling $H = \frac{3p-3}{2}$ factorial steps. To maintain equilibrium, this load is distributed across three identical cooling cores. Each core provides a stabilization factor equal to $S = \frac{p-1}{2}$ factorial. The total efficiency $N$ is calculated by dividing the total high-intensity steps by the product of the stabilization factors of all three cores:
\[ N = \frac{\left(\frac{3p-3}{2}\right)!}{\left[\left(\frac{p-1}{2}\right)!\right]^3} \]

As the engine reaches a critical state, the system technician needs to determine the "Harmonic Residual" of the power output. This value is defined as the remainder when the total processing power $N$ is divided by the square of the prime frequency, $p^2$.

Find $N \pmod{p^2}$.

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
