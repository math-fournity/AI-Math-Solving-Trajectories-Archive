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

In the remote Archipelago of Geometry, four navigation beacons—$A$, $B$, $C$, and $J$—are positioned such that $J$ is the unique point where a ship would be equidistant from the three shipping lanes forming the triangle $ABC$, specifically situated outside the triangle opposite to beacon $A$. A central hub, point $I$, is located at the intersection of the three internal acoustic paths that bisect the interior angles of the triangle $ABC$.

An engineering firm is laying two circular fiber-optic cables, $\omega_b$ and $\omega_c$. The first cable, $\omega_b$, is centered at coordinates $O_b$; it passes through beacon $B$ and is perfectly tangent to the straight acoustic path $CI$ at the exact location of hub $I$. The second cable, $\omega_c$, is centered at $O_c$; it passes through beacon $C$ and is perfectly tangent to the straight acoustic path $BI$ at hub $I$.

A straight maintenance trench is dug between the centers of the two cable circles, $O_b$ and $O_c$. Simultaneously, a direct power line is laid between the central hub $I$ and the external beacon $J$. These two lines—the maintenance trench and the power line—intersect at a switching station labeled $K$.

Calculate the ratio of the distance between the hub and the switching station to the distance between the switching station and the external beacon, expressed as the fraction $\frac{IK}{KJ}$.

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
