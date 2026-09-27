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

A specialized bio-engineering lab is monitoring the growth rates of four different bacterial cultures. The total biomass level of the system is governed by a balance of four distinct growth functions and a linear output offset.

The system reaches equilibrium when the combined activity of the first three cultures equals the net output of the system. The mathematical model for this equilibrium is as follows:

The first culture has a growth intensity of $\sqrt{x+4}$. 
The second culture has a growth intensity of $\sqrt{3-x}$.
The third culture, a hybrid strain, has a growth intensity of $\sqrt{12-x-x^2}$.

On the other side of the equation, the net output is determined by a baseline value of $x-1$ plus a fourth culture's growth intensity of $\sqrt{2x+5}$.

In this model, $x$ represents the nutrient concentration level in the substrate. Given that all radical expressions must represent real-valued growth (non-negative values under the square roots), find the exact value of the nutrient concentration level $x$ that satisfies the equilibrium equation:

$$\sqrt{x+4}+\sqrt{3-x}+\sqrt{12-x-x^2}=x-1+\sqrt{2x+5}$$

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
