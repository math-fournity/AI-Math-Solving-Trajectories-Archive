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

In a remote sector of the galaxy, three space stations—Alpha (A), Beta (B), and Gamma (C)—form a triangular formation. Long-range sensors confirm that the angle at station Alpha is exactly $60^\circ$. The distance between Alpha and Beta is 12 parsecs, and the distance between Alpha and Gamma is 14 parsecs.

A specialized communications buoy is positioned at point Delta (D) along the direct flight path between Beta and Gamma. This buoy is precisely aligned such that the angle formed by the transmission lines Alpha-Beta and Alpha-Delta is equal to the angle formed by Alpha-Gamma and Alpha-Delta.

A parabolic signal relay arc, representing the circumcircle of the Alpha-Beta-Gamma formation, tracks a path through space. The transmission line starting at Alpha and passing through Delta is extended until it hits this relay arc at a deep-space probe labeled Mike (M).

Two local interference fields are generated:
1. The first field is defined by the circular perimeter passing through Beta, Delta, and Mike. This perimeter intersects the Alpha-Beta corridor at a docking waypoint Kilo (K), which is distinct from Beta.
2. The second field is defined by the circular perimeter passing through Gamma, Delta, and Mike.

A straight-line data beam is projected from waypoint Kilo through probe Mike. This beam continues until it intersects the boundary of the second interference field at a final terminal labeled Lima (L), where Lima is a point distinct from Mike.

Calculate the exact ratio of the distance between Kilo and Mike to the distance between Lima and Mike.

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
