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

In a specialized chemical processing plant, a central reaction chamber is fed by five different catalyst injectors. Each injector $i$ (where $i = 1, 2, 3, 4, 5$) releases a specific flow rate $a_i$ into the system. The efficiency of the reaction depends on the "stability setting" $k$ of the chamber’s pressure valve.

Engineers have discovered that for any integer stability setting $k$, the total output of the system follows a precise physical law. Specifically, the sum of the injectors' contributions—where each injector's flow $a_i$ is divided by the sum of the square of the stability setting and the injector's index $i$—is exactly equal to the reciprocal of the square of that stability setting.

Through calibration tests, the engineers confirmed that this law holds perfectly for stability settings $k = 1, 2, 3, 4,$ and $5$.

The plant supervisor now needs to calculate the total output for a high-intensity "Overdrive Phase." In this phase, the stability setting is adjusted to $k = 6$. At this specific setting, the total output is determined by the sum:
\[ \frac{a_1}{6^2+1} + \frac{a_2}{6^2+2} + \frac{a_3}{6^2+3} + \frac{a_4}{6^2+4} + \frac{a_5}{6^2+5} \]

Based on the data from the first five settings, what is the exact value of this sum? Express your answer as a single fraction.

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
