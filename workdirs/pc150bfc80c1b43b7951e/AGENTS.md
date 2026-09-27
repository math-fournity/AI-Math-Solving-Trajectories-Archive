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

In a remote sector of the galaxy, two rival engineering guilds, the Xylons and the Yorics, use automated drones to construct modular bridges. The state of each bridge is determined by a series of alternating "interference pulses" based on the foundational power levels $x$ and $y$, which are represented by positive real numbers.

A Xylon reactor core processes a sequence starting with $x$. Every time a Yoric pulse $y$ is applied, the system calculates the absolute difference between the current state and $y$. Every time a Xylon pulse $x$ is applied, it calculates the absolute difference between the current state and $x$. The Xylon reactor undergoes exactly 2019 such operations in a specific alternating pattern:
Starting with the value $x$, it first subtracts $y$ and takes the absolute value, then subtracts $x$ and takes the absolute value, then subtracts $y$ and takes the absolute value, and so on. The process continues until exactly 2019 absolute value operations have been performed. (The sequence of subtractions is $y, x, y, x, \dots$ until 2019 pairs of bars are filled).

Simultaneously, a Yoric reactor core performs the mirror-image operation. It starts with the foundational value $y$ and undergoes 2019 absolute value operations, but it alternates the pulses in the opposite order: first subtracting $x$, then $y$, then $x$, and so on, until 2019 absolute value operations have been completed.

Deep-space sensors indicate that despite their different starting points and pulse orders, the final energy output of the Xylon reactor is exactly equal to the final energy output of the Yoric reactor.

Based on this equilibrium, determine the sum of all possible values of the ratio $\frac{x}{y}$.

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
