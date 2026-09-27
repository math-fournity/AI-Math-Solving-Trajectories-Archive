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

In a specialized logistics hub, two different protocols are used to calculate the capacity of storage containers over time. 

The first protocol, the "Fiber-Optic Sequence" ($F$), begins with the first two units at a value of 1 ($F_1=1, F_2=1$). For every subsequent unit, the capacity is the sum of the two preceding units ($F_{n+2} = F_{n+1} + F_n$ for $n \geq 1$).

The second protocol, the "Linear-Link Sequence" ($L$), begins with the first unit at 1 and the second unit at 2 ($L_1=1, L_2=2$). Like the first protocol, each following unit is the sum of the two preceding units ($L_{n+2} = L_{n+1} + L_n$ for $n \geq 1$).

A systems engineer needs to calculate a specific "Efficiency Ratio" for a massive data transfer. This ratio is defined as the product of 15 specific "Fiber Gains" divided by the product of the first 13 "Linear-Link" values. 

Each "Fiber Gain" for a given index $n$ is calculated by dividing the capacity of the $(2n)$-th Fiber-Optic unit by the capacity of the $n$-th Fiber-Optic unit (expressed as $\frac{F_{2n}}{F_n}$).

Calculate the value of the Efficiency Ratio:
$$\frac{\prod_{n=1}^{15} \frac{F_{2 n}}{F_{n}}}{\prod_{n=1}^{13} L_{n}}$$

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
