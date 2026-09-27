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

In the city of Flatland, two rectangular solar farms share a common corner at a central control hub located at point $A$. The first farm, $ABCD$, is a perfect square with a side length of 1 kilometer, where vertices $A, B, C, D$ are arranged in counterclockwise order. 

The city planners decide to expand this infrastructure by applying a uniform scale factor to the first farm, centered at hub $A$. This creates a second, larger square solar farm $AB'C'D'$, where $B'$ lies on the line extending through $AB$ and $D'$ lies on the line extending through $AD$. A specialized high-tension power line is strung in a straight path directly from the boundary corner $B$ of the original farm to the far corner $C'$ of the expanded farm. Surveyors measure this power line to be exactly 29 kilometers long.

A triangular conservation zone is formed by the boundary points $B$, $D$, and the far corner $C'$. Calculate the total area of this triangular zone $BDC'$ in square kilometers. If $x$ is the area you obtain, report the value of $\lfloor 10^1x \rfloor$.

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
