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

In a remote territory, three supply depots—Alpha, Bravo, and Charlie—are positioned at the vertices of a triangle. The straight-line distances between these depots are $a$ kilometers, $b$ kilometers, and $c$ kilometers, respectively. 

The regional logistics coordinator must manage two critical facilities: a central hub (the circumcenter) that sits at a distance $R$ from each depot, and a safety bunker (the incenter) that is located at a distance $r$ from each of the three roads connecting the depots.

Through empirical observation, the coordinator notices that the efficiency ratio $E = \frac{R}{2r}$ is always greater than or equal to a base value of $1$. However, she discovers that this ratio can be further bounded by adding a specific term related to the "imbalance" of the depot distances. This term is defined as the product of a constant $k$ and the sum of the squared differences between the road lengths, divided by the square of the total perimeter of the supply route.

Mathematically, she asserts that for any possible arrangement of the three depots, the following inequality must hold:
$$\frac{R}{2r} \geq 1 + \frac{k}{(a+b+c)^2} \left[ (a-b)^2 + (b-c)^2 + (c-a)^2 \right]$$

Determine the greatest positive value of the constant $k$ for which this logistical inequality remains true for all possible triangular depot configurations.

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
