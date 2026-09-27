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

A specialized bio-engineering firm is monitoring the metabolic efficiency of a new cellular culture. The total energy output of the culture is determined by its growth stage $x$, where $x$ is a positive real number.

The research team has identified two primary biological factors that influence the system's energy balance. The first factor, the Primary Metabolic Rate, is defined as the triple of the ratio of the stage increment $(x+1)$ to the square root of the growth stage $\sqrt{x}$. The second factor, the Secondary Metabolic Rate, is defined as the ratio of the same stage increment $(x+1)$ to the square root of the quadratic stability expression $\sqrt{x^2 - x + 1}$.

The lead scientist, Dr. Aris, introduces a calibration constant $a$, which represents a real-valued external energy offset. The system reaches equilibrium when the Primary Metabolic Rate is exactly equal to the sum of the calibration constant $a$ and the Secondary Metabolic Rate.

Mathematically, this equilibrium is represented by the equation:
$$\frac{3(x+1)}{\sqrt{x}} = a + \frac{x+1}{\sqrt{x^2 - x + 1}}$$

Determine all possible values of the real parameter $a$ for which the cellular culture reaches equilibrium at exactly one unique growth stage $x$.

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
