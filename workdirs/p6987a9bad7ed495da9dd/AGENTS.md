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

In a remote nature reserve, a surveyor is mapping a large triangular plot of land bounded by three landmarks: the Alpha Outpost ($A$), the Beta Base ($B$), and the Gamma Camp ($C$). The distance from Alpha to Beta is 100 kilometers, Beta to Gamma is 120 kilometers, and Gamma to Alpha is 140 kilometers.

Three straight supply trails are established across the plot:
1. The Delta Trail connects Alpha to a point $D$ on the path between Beta and Gamma. The distance from Beta to $D$ is 90 kilometers.
2. The Foxtrot Trail connects Gamma to a point $F$ on the path between Alpha and Beta. The distance from Alpha to $F$ is 60 kilometers.
3. The Echo Trail connects Beta to a point $E$ on the path between Alpha and Gamma. The exact location of $E$ is currently being determined.

These trails intersect within the reserve, forming several smaller regions. Let $K$ be the intersection of the Echo Trail and the Foxtrot Trail. Let $L$ be the intersection of the Delta Trail and the Foxtrot Trail. Let $M$ be the intersection of the Delta Trail and the Echo Trail.

The surveyor notices a unique property regarding the surface areas of the land parcels formed by these intersections: the area of the central triangular region $KLM$ is exactly equal to the sum of the areas of three other triangular regions: the region $AME$ (bounded by Alpha, $M$, and $E$), the region $BKF$ (bounded by Beta, $K$, and $F$), and the region $CLD$ (bounded by Gamma, $L$, and $D$).

Based on this specific area relationship, calculate the distance from Gamma ($C$) to the point $E$.

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
