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

In a remote industrial mining complex, a chief engineer is monitoring the combined output of a series of $m$ specialized extraction pumps. Each pump $i$ (where $i$ ranges from $1$ to $m$) has a unique fixed "efficiency constant" denoted by a positive integer $a_i$. Not all pumps have the same efficiency constant, and the sum of all constants is defined as $S = \sum_{i=1}^m a_i$.

The instantaneous production rate of a single pump depends on a global power input $n$. Specifically, the output of pump $i$ is given by the square root of the sum of the power input and its efficiency constant, or $\sqrt{n+a_i}$. 

The engineer observes a strange phenomenon: for all integer power inputs $n$ exceeding a certain threshold $N$, the integer part of the total combined output of all $m$ pumps is perfectly identical to the integer part of the output of a single massive "master generator." The master generator’s output is governed by two non-negative integer settings, $b$ and $c$, according to the formula $\sqrt{bn+c}$.

Mathematically, the relationship is expressed as:
$$\left\lfloor \sum_{i=1}^m \sqrt{n+a_i} \right\rfloor = \left\lfloor \sqrt{bn+c} \right\rfloor \text{ for all } n > N$$

Find the sum of the master generator's settings, $b + c$, expressed in terms of the number of pumps $m$ and the sum of their efficiency constants $S$.

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
