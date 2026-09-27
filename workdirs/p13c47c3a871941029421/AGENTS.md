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

An oil and gas company is revising its sales strategy for natural and liquefied gas for the winter. There are two weather scenarios: a calm winter ($D_1$) and a winter with severe frosts ($D_2$).
In scenario $D_1$, the demand is 2200 $m^3$ of natural gas and 3500 $m^3$ of liquefied gas.
In scenario $D_2$, the demand is 3800 $m^3$ of natural gas and 2450 $m^3$ of liquefied gas.
The production and transport cost per $m^3$ is 19 for natural gas and 25 for liquefied gas. The consumer price is 35 for natural gas and 58 for liquefied gas.
The company wishes to determine the optimal volumes of natural gas ($N$) and liquefied gas ($L$) to procure to maximize its guaranteed profit, assuming that any gas produced but not demanded by the scenario results in a loss equal to its production cost. 
Let $N$ be the planned amount of natural gas and $L$ be the planned amount of liquefied gas in the optimal mixed strategy. Calculate the sum $N + L$.

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
