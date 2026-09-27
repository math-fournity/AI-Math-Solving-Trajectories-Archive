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

In a remote digital civilization, a master programmer is building a secure encryption library based on a prime number $p$ and the field of integers modulo $p$, denoted as $\mathbb{F}_p$. The library $W$ is a collection of data-transformation functions, where each function is represented as a polynomial with coefficients in $\mathbb{F}_p$.

The library is initialized with two fundamental "seed" functions:
1.  The Incrementer: $A(x) = x + 1$
2.  The Custom Shifter: $B(x) = x^{p-2} + x^{p-3} + \dots + x^2 + 2x + 1$

To expand the library, the programmer follows a strict recursive rule: if any two functions $h_1(x)$ and $h_2(x)$ (where $h_1$ and $h_2$ could be the same) are already in $W$, their "composed output" must also be added to $W$. The composed output $r(x)$ is defined as the unique polynomial of degree at most $p-1$ that is congruent to the composition $h_1(h_2(x))$ modulo the polynomial $x^p - x$.

$W$ is defined as the smallest possible set of polynomials that satisfies these criteria. Given these parameters, what is the total number of unique polynomials contained in the library $W$?

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
