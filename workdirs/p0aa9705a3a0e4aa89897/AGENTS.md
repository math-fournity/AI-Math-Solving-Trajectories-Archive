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

In the city of Arithmea, a grand infrastructure project is underway to build an infinite series of interconnected segments along a single road. The elevation of the road at any distance $x$ (measured in kilometers from the origin) is defined by a function $p(x)$. 

The construction is divided into one-kilometer zones. For each non-negative integer $n$, the elevation profile within the zone $x \in [n, n+1]$ is governed by a specific engineering polynomial, $p_n(x)$. The design specifications are as follows:

1.  In the first zone ($x \in [0, 1]$), the elevation is simply defined by $p_0(x) = x$.
2.  To ensure structural harmony, the rate of change (slope) of the elevation in the $n$-th zone is equal to the elevation profile of the previous zone. That is, for all integers $n \geq 1$, $\frac{d}{dx} p_n(x) = p_{n-1}(x)$.
3.  The road must be smooth and uninterrupted; therefore, the function $p(x)$ is continuous across all zone boundaries for all $x \geq 0$.

A surveyor is interested in the cumulative elevation values at a specific landmark located at $x = 2009$. Using the polynomials defined by the zones above, calculate the sum of the values of every polynomial in the sequence evaluated at this landmark:

\[ \sum_{n=0}^{\infty} p_{n}(2009) \]

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
