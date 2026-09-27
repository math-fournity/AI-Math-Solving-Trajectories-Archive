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

In a remote industrial outpost, two energy-monitoring variables, $a$ and $b$, can fluctuate across any real-number values. The station’s power consumption and stability are governed by two physical constants, $v$ and $w$.

The station’s Operational Load (the left side of the equation) is calculated by the formula:
$(2^{a+b}+8)(3^{a}+3^{b})$

The station’s Safety Threshold (the right side of the equation) is determined by the formula:
$v(12^{a-1}+12^{b-1}-2^{a+b-1})+w$

Engineers have discovered that for the station to remain functional, the Operational Load must never exceed the Safety Threshold, regardless of the values of $a$ and $b$. To minimize resource costs, the administrators must determine the specific constants $v$ and $w$ that satisfy this permanent inequality while minimizing the specific stress-test value defined by the expression $128v^{2}+w^{2}$.

Compute the smallest possible value of $128v^{2}+w^{2}$ that ensures the inequality holds for all real $a$ and $b$.

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
