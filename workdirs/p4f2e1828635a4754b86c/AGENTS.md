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

A specialized chemical reactor begins its operation with an initial concentration of a catalyst, $C = 1$ unit. To reach stabilization, a computer-controlled injector randomly introduces one of four concentration boosters every minute. The system chooses from the set $\{3, 5, 8, 9\}$, where each multiplier $r$ has an equal $25\%$ probability of being selected. After each injection, the current concentration $C$ is multiplied by the chosen value $r$.

The reaction process terminates under two specific safety conditions based on the modular properties of the concentration relative to a critical threshold of $13$. If the concentration $C$ reaches a state where $C + 1$ is a multiple of $13$, the "Alpha" safety valve (Fred's outcome) triggers and the process stops. If the concentration reaches a state where $C + 3$ is a multiple of $13$, the "Beta" safety valve (George's outcome) triggers and the process stops. If neither condition is met, the injector continues its cycle the following minute.

Determine the probability that the process terminates via the Alpha safety valve. If the probability is expressed as an irreducible fraction $\frac{a}{b}$, calculate the value of $a + b$.

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
