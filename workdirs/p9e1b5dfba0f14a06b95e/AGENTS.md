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

In the city of Apollonia, a specialized solar power station is built within a perfectly circular containment wall. Four sensor towers, labeled $A, B, C$, and $D$, are positioned exactly on this circular perimeter. The distances between these towers are measured as follows: the cables from $A$ to $B$ and $B$ to $C$ both span 5 kilometers, the cable from $C$ to $D$ spans 3 kilometers, and the cable from $D$ to $A$ spans 8 kilometers.

The station’s control grid is defined by two straight maintenance tracks. The first track begins at tower $D$ and passes through tower $A$ to reach a remote signal booster $P$. The second track begins at tower $D$ and passes through tower $C$ to reach a remote signal booster $Q$. A mobile monitoring unit is located at a specific point $R$, positioned such that the distance from $R$ to $P$ is exactly equal to the distance from tower $C$ to $Q$, and the distance from $R$ to $Q$ is exactly equal to the distance from tower $A$ to $P$.

An engineer discovers that the straight-line path from the monitoring unit $R$ to tower $B$ is perfectly perpendicular to the straight-line path connecting the two boosters $P$ and $Q$.

Calculate the absolute difference between the distance from $C$ to $Q$ and the distance from $A$ to $P$. If the result is an irreducible fraction $\frac{a}{b}$, determine the final value of $a + b$.

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
