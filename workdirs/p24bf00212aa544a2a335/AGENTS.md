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

A shipping logistics company operates a massive rectangular warehouse organized into a grid of $m$ rows and $n$ columns of storage bays. The manager decides to install specialized automated sensors in some of these bays. 

In this facility, two bays are considered "linearly linked" if they lie on the same diagonal line (either primary or secondary). A set of $2r$ distinct sensor-equipped bays ($a_1, a_2, \dots, a_{2r}$, where $2r \geq 4$) is defined as a "Critical Loop" if it satisfies two conditions:
1. For every index $k$ from $1$ to $2r$, the bay $a_k$ is linearly linked to the bay $a_{k+1}$.
2. For every index $k$ from $1$ to $2r$, the bay $a_k$ is NOT linearly linked to the bay $a_{k+2}$.
(In these conditions, we use cyclic indexing where $a_{2r+1} = a_1$ and $a_{2r+2} = a_2$).

The safety inspector requires that the warehouse layout must be designed such that it is impossible to form even a single "Critical Loop" among the sensor-equipped bays. 

Based on these constraints, determine the maximum possible number of bays that can be equipped with sensors.

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
