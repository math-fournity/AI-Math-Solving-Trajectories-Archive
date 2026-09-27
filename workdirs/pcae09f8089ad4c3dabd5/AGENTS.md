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

In a futuristic data center, a network engineer manages a system of 2020 processors, indexed $i=1, 2, \ldots, 2020$. Each processor stores a single data packet $x_i$, which is an integer representing a signal state modulo 2020. The current state of the entire system is represented by the 2020-tuple $(x_1, x_2, \ldots, x_{2020})$.

The system operates via a specific synchronization function $f$. When the function is triggered, every processor $i$ simultaneously updates its value to a new state based on three constants assigned to that specific processor ($a_i, b_i$, and $c$) and the previous states of specific units in the array. Specifically, the new value of the $i$-th processor is calculated as:
$$x_{i-2} + a_i x_{2019} + b_i x_{2020} + c x_i \pmod{2020}$$
In this calculation, if a processor index $i-2$ is less than 1 (specifically $x_{-1}$ or $x_0$), its value is hardcoded to 0. Note that the constant $c$ is a global configuration parameter shared by all processors, while the pairs $(a_i, b_i)$ are unique to each processor $i$.

The engineer is looking for the smallest positive integer $m$ such that there exists at least one configuration of the $2 \times 2020 + 1$ constants $(a_1, \ldots, a_{2020}, b_1, \ldots, b_{2020}, c)$ that forces every possible initial state $(x_1, \ldots, x_{2020})$ to the "all-zero" state $(0, 0, \ldots, 0)$ after exactly $m$ applications of the function $f$.

Let $m$ be this minimum number of iterations. For this specific value of $m$, let $n$ be the total number of distinct configurations of the tuple $(a_1, \ldots, a_{2020}, b_1, \ldots, b_{2020}, c)$ that result in the system reaching the all-zero state after $m$ iterations for every possible input.

Compute the value $100m + n$.

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
