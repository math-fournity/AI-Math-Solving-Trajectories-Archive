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

In the highly automated "Nexus" energy grid, four regional power stations—Alpha, Beta, Gamma, and Delta—produce variable amounts of gigawatts, represented by the positive values $a, b, c,$ and $d$ respectively. 

The grid's stability is governed by a strict equilibrium protocol. The total output of the four stations must satisfy a specific operational constraint: the sum of all possible triple-products of their outputs must be numerically equal to the product of all four outputs ($abc + abd + acd + bcd = abcd$).

The efficiency overhead of the system, denoted by $E$, is calculated by summing the ratios of each station's output to the combined output of the other three stations, then subtracting a constant factor of $4/3$. Mathematically, $E = \frac{a}{b+c+d} + \frac{b}{a+c+d} + \frac{c}{a+b+d} + \frac{d}{a+b+c} - \frac{4/3}{1}$.

A systems engineer discovers a linear safety bound for this overhead. He proposes that for a specific constant coefficient $\gamma$, the efficiency overhead $E$ will always be less than or equal to $\gamma$ multiplied by the "deviation" of the total grid output from a baseline of 16 units (where deviation is $a+b+c+d-16$).

Determine the specific real value of $\gamma$ for which the inequality $E \leq \gamma(a+b+c+d-16)$ holds true for all valid power outputs $a,b,c,d$ under the grid's equilibrium protocol.

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
