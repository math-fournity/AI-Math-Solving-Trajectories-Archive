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

In a specialized digital signal processing laboratory, a team of engineers is testing a "Signal Harmonic Multiplier" device. The base signal distortion function is defined by $f^1(x) = x^3 - 3x$, where $x$ represents the input voltage amplitude. The device can be daisy-chained such that the output of one iteration serves as the input for the next, defined by $f^n(x) = f(f^{n-1}(x))$.

The engineers are analyzing a massive chain of $2022$ identical units. They identify a specific set of resonant frequencies, $\mathcal{R}$, which are defined as the non-zero real and complex roots of the final output function $f^{2022}(x)$ divided by $x$. 

To calculate the total precision loss of the system, the lead scientist needs to determine the sum of the inverse squares of all resonant frequencies in the set $\mathcal{R}$:
$$\sum_{r \in \mathcal{R}} \frac{1}{r^{2}}$$
The result of this calculation is expressed in the form $\frac{a^{b} - c}{d}$, where $a, b, c,$ and $d$ are positive integers. To standardize the reporting, $b$ must be as large as possible, and the fraction $\frac{c}{d}$ must be in simplest form (where $c$ and $d$ are relatively prime).

Find the value of $a + b + c + d$.

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
