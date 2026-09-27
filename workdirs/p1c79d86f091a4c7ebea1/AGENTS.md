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

In the futuristic city of Chronos, an energy grid is powered by 25 distinct thermal reactors, numbered $n = 1$ to $25$. The city’s central AI allocates power according to a specific decay-growth formula to balance the load across the sectors.

For each reactor $n$, the total megawatt output is determined by taking the reactor's identification number $n$ and raising it to a power equal to $(26 - n)$. 

The first reactor ($n=1$) operates at a power of $1^{25}$ megawatts. The second reactor ($n=2$) operates at $2^{24}$ megawatts, the third at $3^{23}$ megawatts, and this pattern continues systematically until the final reactor ($n=25$), which operates at $25^{1}$ megawatts.

To ensure the city’s life-support systems remain functional, the Chief Engineer needs to calculate the total combined power output of all 25 reactors.

What is the total value of the sum $1^{25} + 2^{24} + 3^{23} + \ldots + 24^{2} + 25^{1}$?

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
