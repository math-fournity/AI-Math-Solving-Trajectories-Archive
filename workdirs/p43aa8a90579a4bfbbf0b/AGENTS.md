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

In a remote triangular territory defined by three outposts, $A$, $B$, and $C$, the distances between the stations are $AB = 13$ km, $BC = 14$ km, and $CA = 15$ km. Two autonomous survey drones, "Crimson" and "Azure," are programmed to patrol the perimeter of this triangle indefinitely.

Crimson starts at Outpost $A$ and travels counterclockwise ($A \to C \to B \to A$) at a constant speed $v$. Azure also starts at Outpost $A$ but travels clockwise ($A \to B \to C \to A$). However, Azure’s engine only ignites at the exact moment Crimson has already covered a distance of $2$ km. Once active, Azure travels at a constant speed of $4v$ (four times faster than Crimson).

As they circle the perimeter repeatedly, the drones will occasionally pass each other or occupy the same coordinate. Consider the set of all distinct spatial locations on the perimeter where these two drones meet during their infinite motion. These locations serve as the vertices of a convex polygon. 

Calculate the area of this convex polygon. If $x$ is the area, find $\lfloor 10^3x \rfloor$.

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
