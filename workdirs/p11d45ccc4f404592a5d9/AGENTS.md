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

17. (NET 2) ${ }^{\mathrm{IMO} 6}$ Let $n$ be an integer greater than 1 . In a circular arrangement of $n$ lamps $L_{0}, \ldots, L_{n-1}$, each one of that can be either ON or OFF, we start with the situation where all lamps are ON, and then carry out a sequence of steps, $S_{t e p_{0}}, S t e p_{1}, \ldots$. If $L_{j-1}(j$ is taken $\bmod n)$ is ON, then $S_{t e p}^{j}$ changes the status of $L_{j}$ (it goes from ON to OFF or from OFF to ON) but does not change the status of any of the other lamps. If $L_{j-1}$ is OFF, then $S_{t e p}^{j}$ does not change anything at all. Show that: (a) There is a positive integer $M(n)$ such that after $M(n)$ steps all lamps are ON again. (b) If $n$ has the form $2^{k}$, then all lamps are ON after $n^{2}-1$ steps. (c) If $n$ has the form $2^{k}+1$, then all lamps are ON after $n^{2}-n+1$ steps.

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
