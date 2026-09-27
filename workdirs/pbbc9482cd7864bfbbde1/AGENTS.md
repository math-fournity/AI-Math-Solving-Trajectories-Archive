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

In the city of Arithema, there is a perfect square park bounded by four main roads: North ($BC$), East ($CD$), South ($DA$), and West ($AB$). A landscape architect is designing a new layout for the park.

Two straight walking paths are paved across the park. The first path, $AK$, begins at the southwest corner ($A$) and ends at a water fountain ($K$) located exactly at the midpoint of the North road ($BC$), such that $BK = KC$. The second path, $BN$, begins at the northwest corner ($B$) and ends at a statuesque landmark ($N$) on the East road ($CD$). The landmark $N$ is positioned such that the distance from the northeast corner ($C$) to $N$ is twice the distance from $N$ to the southeast corner ($D$), meaning $CN:ND = 2:1$.

These two paths, $AK$ and $BN$, intersect at a central gazebo, point $T$. This intersection divides the park into several zones. The city council has measured the zone formed by the quadrilateral $KCNT$ and found its area to be exactly 13 acres.

Based on this information, calculate the area, in acres, of the triangular region $BTA$ located in the western portion of the park.

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
