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

Deep in a subterranean research facility, two high-precision laser frequencies are being calibrated across a sensor field. The operational range of the facility is restricted to a spatial dimension $x$ within the interval $[-3, 3]$.

The first laser’s phase is governed by the function $P_1(x) = \pi(x^3 - 6x)$, while the second laser’s phase is governed by $P_2(x) = \pi(x^3 - 3x^2)$. 

Due to the periodic nature of the optical sensors, a "Signal Resonance" occurs whenever the cotangent of the first phase is exactly equal to the cotangent of the second phase. Mathematically, resonance is achieved at any point $x$ where:
\[ \cot(P_1(x)) = \cot(P_2(x)) \]

Note that a resonance signal is physically impossible and undefined if the phase $P_1(x)$ or $P_2(x)$ is an integer multiple of $\pi$, as the sensor's capacity would be overloaded (the cotangent becomes undefined).

How many distinct points of Signal Resonance exist within the restricted interval $[-3, 3]$?

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
