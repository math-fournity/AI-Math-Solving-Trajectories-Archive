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

In a remote logistics network, three major distribution hubs—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—are connected by three straight supply routes: route $BC$ has a length of $a$ units, route $CA$ has a length of $b$ units, and route $AB$ has a length of $c$ units.

To optimize regional deliveries, "Ex-Hub" stations are established. The $A$-Ex-Hub is located at point $A_1$ on route $BC$, where the $A$-excircle (the circle outside the triangle tangent to $BC$ and the extensions of $AB$ and $AC$) touches the road. Similarly, the $B$-Ex-Hub is located at $B_1$ on route $CA$, and the $C$-Ex-Hub is located at $C_1$ on route $AB$.

The network's central management team is evaluating specific configurations for these routes based on two strict criteria:

1. The dimensions $a$, $b$, and $c$ must be positive integers such that the "regional reach" values—defined as $(-a+b+c)$, $(a-b+c)$, and $(a+b-c)$—are all even integers no greater than 100.
2. A specialized monitoring circle is drawn through the midpoints of the segments $AA_1$, $BB_1$, and $CC_1$. For the network to be considered "perfectly synchronized," this monitoring circle must be exactly tangent to the triangle's incircle (the circle inside the triangle tangent to all three supply routes).

Determine the total number of distinct sets of integer route lengths $(a, b, c)$ that satisfy these synchronization requirements.

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
