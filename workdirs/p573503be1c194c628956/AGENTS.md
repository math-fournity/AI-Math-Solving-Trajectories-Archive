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

In the high-tech logistics center of a futuristic city, an automated sorting system uses a specialized security protocol based on numerical sequences. The system requires the generation of data packets, each consisting of a sequence of 6 integer weights: $(a_5, a_4, a_3, a_2, a_1, a_0)$.

To ensure security, these weights must adhere to the following strict operational constraints:
1. Each weight must be a distinct integer chosen from the available set of calibrated values $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}$.
2. The lead weight $a_5$ must be non-zero (which is naturally satisfied by the available set).
3. The sequence must represent a polynomial $P(x) = a_5x^5 + a_4x^4 + a_3x^3 + a_2x^2 + a_1x + a_0$ that is perfectly compatible with the system's core filter.
4. The core filter is defined by the quadratic expression $x^2 - x + 1$. For a sequence to be valid, the polynomial $P(x)$ must be exactly divisible by $x^2 - x + 1$.

How many unique sequences of weights satisfy all these security requirements?

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
