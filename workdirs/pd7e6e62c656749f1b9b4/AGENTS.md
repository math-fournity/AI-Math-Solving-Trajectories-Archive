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

In a specialized logistics network, there are two distinct zones of cities, Zone A and Zone B. Each zone contains exactly $n$ cities, and the geographical layout is such that no three cities across the entire network lie on a single straight line.

To facilitate trade, a collection of shipping routes $S$ is established. Each route is a direct connection between one city in Zone A and one city in Zone B. A city can be connected to multiple cities in the opposite zone, but there is at most one route between any two specific cities.

A network configuration $S$ is classified as "Level-$l$ Stable" if every single city in both Zone A and Zone B is served by at least $l$ shipping routes. We define $M(n, l)$ as the maximum possible total number of shipping routes in a configuration $S$ that is Level-$l$ Stable, but possesses the "Criticality Property": removing any single route from $S$ immediately causes at least one city to fall below the requirement of $l$ routes, thereby breaking the Level-$l$ Stability.

Calculate the value of the sum:
$$\sum_{n=10}^{20} M(n, 3)$$

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
