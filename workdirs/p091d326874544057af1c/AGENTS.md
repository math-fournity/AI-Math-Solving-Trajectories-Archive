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

In the city of Digitalis, every building is assigned a residential security code, which is a positive integer. The "Energy Signature" of a building is calculated by summing the individual digits of its security code.

The city’s zoning law defines the "Next-Tier Neighbor" of a building with code $n$ as the building with the smallest security code $F(n)$ such that:
1. $F(n)$ is strictly greater than $n$.
2. The Energy Signature of $F(n)$ is exactly equal to the Energy Signature of $n$.

For instance, the building with code $2019$ has an Energy Signature of $2+0+1+9=12$. Its Next-Tier Neighbor is the building with code $2028$, because $2+0+2+8=12$, and no integer between $2019$ and $2028$ has digits summing to $12$.

The Department of Urban Planning needs to calculate a cumulative "Infrastructure Index" for the first thousand buildings. Compute the sum of the security codes of the Next-Tier Neighbors for all buildings with codes from $1$ to $1000$ inclusive. 

That is, find the value of:
$F(1) + F(2) + F(3) + \cdots + F(1000)$

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
