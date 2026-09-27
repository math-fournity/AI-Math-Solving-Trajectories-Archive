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

In the strategic logistics hub of a maritime port, four key docking stations are positioned at coordinates labeled $A, B, C,$ and $D$. Two primary underwater fiber-optic cables are laid out in straight lines: the first cable connects station $A$ to station $B$, and the second connects station $C$ to station $D$. These two cables intersect at a central switching junction, $P$.

Internal diagnostic sensors report the following cable segment lengths:
- The distance from station $A$ to junction $P$ is $8$ kilometers.
- The distance from station $B$ to junction $P$ is $24$ kilometers.
- The distance from station $C$ to junction $P$ is $11$ kilometers.
- The distance from station $D$ to junction $P$ is $13$ kilometers.

To monitor regional activity, two security perimeters are established. The first follows a straight line passing through $D$ and $A$, extending beyond $A$. The second follows a straight line passing through $B$ and $C$, extending beyond $C$. These two perimeter lines eventually meet at a remote observation tower, $Q$.

A specialized signal beam is projected from tower $Q$ directly to the central junction $P$. It is observed that this beam $QP$ perfectly bisects the angle formed at the tower between the two security perimeters (the angle $\angle BQD$).

The ratio of the length of the perimeter segment $AD$ to the length of the perimeter segment $BC$ is found to be a fraction $\frac{m}{n}$ in simplest form, where $m$ and $n$ are relatively prime positive integers. Determine the value of $m+n$.

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
