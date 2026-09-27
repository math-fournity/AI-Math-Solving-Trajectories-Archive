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

In the competitive field of deep-sea pressure engineering, a firm is designing a specialized triangular stabilizer module. The structural integrity of this module is governed by three positive performance parameters: $x$, $y$, and $z$. These parameters are strictly constrained by the "Unity Saturation Law," which states that the product of the three parameters, multiplied by their sum, must equal exactly 1: 
$$xyz(x + y + z) = 1$$

To ensure the safety of the module under extreme oceanic conditions, engineers have identified a critical safety threshold $S$, defined by the product of two specific load-bearing capacities. The first capacity is calculated as $2x + y$, and the second capacity is calculated as $2x + z$. 

To prevent structural failure, the product of these two capacities must always be strictly greater than a specific safety constant $k$. That is:
$$(2x + y)(2x + z) > k$$

Determine the maximum possible value of the constant $k$ that satisfies this inequality for all valid configurations of $x$, $y$, and $z$.

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
