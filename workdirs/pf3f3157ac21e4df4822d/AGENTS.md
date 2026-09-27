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

In a highly secure automated manufacturing facility, a control system is governed by a specialized efficiency function $f(x) = \sum_{i=0}^{n} a_i x^i$. The performance coefficients $a_i$ for this system are strictly required to be integers.

The facility’s output is calibrated based on the energy levels of two specific fuel isotopes. These isotopes are identified by their atomic stability ratings, $p_1$ and $p_2$, both of which are prime numbers.

During a diagnostic stress test, engineers observed two specific operational outputs:
1. When the system was injected with a power load equal to the square of the first isotope's rating ($p_1^2$), the system’s net torque was measured at $-56$ units.
2. When the system was injected with a power load equal to the square of the second isotope's rating ($p_2^2$), the net torque was measured at $56$ units.

Identify all possible pairs of prime stability ratings $(p_1, p_2)$ that satisfy these diagnostic results. What is the sum of every $p_1$ and $p_2$ found across all valid pairs?

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
