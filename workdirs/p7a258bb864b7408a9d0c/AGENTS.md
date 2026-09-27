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

A specialized circular ecological reserve is divided into four sectors by four straight perimeter fences: $PQ$, $QR$, $RS$, and $SP$. Because the reserve is circular, the four corner posts $P, Q, R,$ and $S$ all lie exactly on the same circular boundary. Surveyors have measured the internal angles of the reserve, noting that the angle at post $P$ formed by fences $SP$ and $PQ$ is $110^\circ$, while the angle at post $Q$ formed by fences $PQ$ and $QR$ is $50^\circ$.

A primary maintenance road $AB$ is constructed by connecting the midpoint $A$ of fence $PQ$ to the midpoint $B$ of fence $RS$. A monitoring station $X$ is located at a specific point along this road. The position of station $X$ is determined by two conditions: first, the distance from post $P$ to station $X$ is exactly equal to the distance from post $R$ to station $X$. Second, the ratio of the distance along the road from $A$ to $X$ compared to the distance from $B$ to $X$ is identical to the ratio of the length of fence $PQ$ to the length of fence $RS$.

An ecologist at station $X$ needs to calculate the visibility angle between the lines of sight connecting the station to posts $P$ and $R$. Find the measure of $\angle PXR$ in degrees.

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
