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

In a remote sector of the ocean, three research buoys—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. Navigational sensors confirm the distances between them are exactly $14$ nautical miles from $A$ to $B$, $15$ nautical miles from $A$ to $C$, and $13$ nautical miles from $B$ to $C$.

A central underwater hub, $I$, is positioned at the exact center of a circular supply route that is tangent to the cables connecting the buoys. Specifically, this circular route touches the $BC$ cable at point $D$, the $AC$ cable at point $E$, and the $AB$ cable at point $F$.

The entire region is monitored by a satellite whose orbital path follows the circumcircle passing through the three buoys $A, B,$ and $C$. A deep-sea beacon, $X$, is located at the midpoint of the major arc $BAC$ on this orbital circle (the arc passing through $B, A,$ and $C$ in that order).

A specialized maintenance drone, $P$, is deployed along a straight transit line connecting the beacon $X$ and the hub $I$. To optimize its acoustic pinger, the drone $P$ must be positioned such that the straight line connecting it to the contact point $D$ is exactly perpendicular to the straight line connecting contact points $E$ and $F$.

Calculate the distance $DP$ between the drone and the $BC$ contact point.

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
