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

A specialized high-speed conveyor belt operates for exactly 1 minute, represented by the interval $[0, 1]$. A sensor tracks the displacement of a mechanical arm on this belt, modeled by a polynomial function $P(x)$ of degree 99. The arm is programmed such that its displacement is exactly zero at the start of the cycle ($x=0$) and exactly zero at the end of the cycle ($x=1$).

An engineer is testing the "repetitive vibration" threshold of the arm. They are looking for a specific duration $a$ such that, regardless of the specific coefficients of the 99th-degree polynomial chosen for the arm's path, there will always be two distinct moments in time, $x_1$ and $x_2$ within the 1-minute cycle, where the arm is at the exact same displacement ($P(x_1) = P(x_2)$) and the time elapsed between those two moments is exactly $a$ ($x_2 - x_1 = a$).

Determine the maximum possible value $h$ such that for every duration $a$ in the range $[0, h]$, the existence of these two moments $x_1$ and $x_2$ is guaranteed for any such polynomial.

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
