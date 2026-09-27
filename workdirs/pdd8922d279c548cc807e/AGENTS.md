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

In a remote industrial complex, a specialized chemical reactor combines three rare reagents—Alpha ($a$), Beta ($b$), and Gamma ($c$)—measured in liters of positive real quantities. The efficiency of the reactor is determined by the sum of three specific process ratios.

The first process, the Hydrogenation Phase, has an efficiency defined by the ratio of the Alpha supply plus three times the Gamma supply, divided by the total of the Alpha supply, twice the Beta supply, and the Gamma supply.

The second process, the Catalytic Phase, contributes an efficiency value equal to four times the Beta supply divided by the sum of the Alpha supply, the Beta supply, and twice the Gamma supply.

The third process, the Purification Phase, experiences a loss in efficiency. This loss is calculated as eight times the Gamma supply divided by the sum of the Alpha supply, the Beta supply, and three times the Gamma supply.

The total performance index of the reactor is the sum of the efficiencies from the first two phases minus the efficiency loss from the third phase:
\[ \text{Performance} = \frac{a + 3c}{a + 2b + c} + \frac{4b}{a + b + 2c} - \frac{8c}{a + b + 3c} \]

What is the absolute minimum value this performance index can reach for any combination of positive reagent quantities?

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
