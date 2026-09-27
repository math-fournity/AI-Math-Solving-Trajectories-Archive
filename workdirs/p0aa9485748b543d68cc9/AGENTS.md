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

In a specialized logistics network, a series of $n$ industrial hubs are positioned along a linear pipeline at increasing distances from a central station. We denote the distance of the $k$-th hub from the station as $y_k$ (in kilometers), where $0 = y_0 < y_1 < \dots < y_n$.

An engineer is evaluating the efficiency of a two-stage delivery system across these hubs.

1.  **The Supply Cost:** For each segment between hub $k-1$ and hub $k$, the transport cost is determined by the formula $\frac{(k+1)^{3/2}}{\sqrt{y_k^2 - y_{k-1}^2}}$. The total supply cost for the system is the sum of these values from $k=1$ to $n$.
2.  **The Maintenance Demand:** Each hub $k$ requires a maintenance budget defined by the value $\frac{k^2 + 3k + 3}{y_k}$. The total maintenance demand is the sum of these values from $k=1$ to $n$.

The project director needs to determine a universal safety multiplier, $\alpha$, that ensures the total supply cost, when scaled by $\alpha$, will always be greater than or equal to the total maintenance demand, regardless of the number of hubs $n$ or their specific distances $y_k$.

Find the smallest real constant $\alpha$ such that for all positive integers $n$ and all sequences $0 = y_0 < y_1 < \dots < y_n$, the following inequality is guaranteed to hold:

$$\alpha \sum_{k=1}^{n} \frac{(k+1)^{3/2}}{\sqrt{y_k^2 - y_{k-1}^2}} \geq \sum_{k=1}^{n} \frac{k^2 + 3k + 3}{y_k}$$

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
