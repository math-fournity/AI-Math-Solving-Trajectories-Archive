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

A network of $n$ satellite ground stations is deployed across a vast, flat desert plain. To ensure high-quality data transmission, the network's geometry must satisfy two strict technical constraints:
1. No three ground stations are located exactly on the same straight line.
2. The straight-line distance between any two distinct stations is unique; no two pairs of stations are separated by the same distance.

Engineers classify the signal links between these stations based on relative distance. For any two stations $A$ and $B$, the link between them is designated as a "Median-Range Link" if there exists a third station $C$ in the network such that the distance from $A$ to $C$ is shorter than the distance between $A$ and $B$, and the distance between $A$ and $B$ is, in turn, shorter than the distance from $B$ to $C$ (i.e., $|AC| < |AB| < |BC|$).

If three stations $A$, $B$, and $C$ are positioned such that the three links connecting them ($AB$, $BC$, and $CA$) are all classified as "Median-Range Links," the trio is identified as a "Stabilized Communication Delta."

What is the smallest integer $n$ for which any set of $n$ ground stations satisfying the two initial constraints must contain at least one Stabilized Communication Delta?

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
