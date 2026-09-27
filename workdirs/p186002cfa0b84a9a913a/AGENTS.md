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

A team of civil engineers is designing a sustainable irrigation system for three neighboring farmland plots. The total water volume allocated to these plots per day is exactly 3 million gallons. Let $x, y,$ and $z$ represent the volume of water (in millions of gallons) assigned to each respective plot, where each value must be non-negative.

The structural integrity of the reservoir system is determined by a complex stress-load inequality. The "Primary Stability Index" of the system is calculated as the sum of the fourth powers of the individual water volumes ($x^4 + y^4 + z^4$). To ensure safety, this index must always be greater than or equal to a baseline value. This baseline consists of a "Core Pressure" term, defined as three times the product of the three volumes ($3xyz$), plus a "Flow Turbulence" term. 

The Flow Turbulence term is calculated as a constant $k$ multiplied by the product of the differences between the volumes of the adjacent plots: $(x-y)(y-z)(z-x)$.

Determine the maximum possible value of the constant $k$ such that the stability condition $x^4 + y^4 + z^4 \ge 3xyz + k(x-y)(y-z)(z-x)$ remains satisfied for every possible distribution of the 3 million gallons across the three plots.

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
