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

A team of civil engineers is designing a complex modular suspension bridge system. The stability of the bridge is governed by a structural integrity equation involving several variable load factors, $x$.

The design requires the coordination of $n$ distinct primary support modules. For each module $k$ (where $k=1, \dots, n$), the stress strain is modeled by a non-constant polynomial $f_k(x)$ with integer coefficients. The secondary reinforcement for each module is calculated as the square of the stress strain minus one, represented by the expression $(f_k^2(x) - 1)$. 

According to the master safety blueprint, the product of the reinforcement values of all $n$ modules, when added to a unit constant of 1, must exactly equal the square of a specific load-bearing capacity. This capacity is defined as the product of the quadratic base profile $(x^2 + 2013)$ and an auxiliary distribution polynomial $g(x)$, which also must have integer coefficients.

The governing equation for the system is:
$$1 + \prod_{k=1}^{n} (f^2_k(x) - 1) = \left( (x^2 + 2013)g(x) \right)^2$$

Find all positive integers $n$ for which there exist non-constant polynomials with integer coefficients $f_1(x), \dots, f_n(x)$ and $g(x)$ that satisfy this structural requirement.

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
