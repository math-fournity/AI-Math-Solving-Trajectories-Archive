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

In the Kingdom of Planimetria, three distinct guilds—the Builders (B), the Craftsmen (C), and the Architects (A)—share a triangular territory defined by the vertices $A$, $B$, and $C$. At the exact geographic center (the centroid) of their lands sits the Grand Archive, $G$.

To monitor their borders, the guilds established three circular observation zones, each passing through the Grand Archive and two of the guild capitals:
- The Southern Zone (Circle $I$) covers $B, C,$ and $G$.
- The Western Zone (Circle $J$) covers $C, A,$ and $G$.
- The Eastern Zone (Circle $K$) covers $A, B,$ and $G$.

The administrative centers of these zones are located at their respective circular centers: $I$, $J$, and $K$. 

A straight supply road connects the Western center $J$ and the Eastern center $K$. Meanwhile, a specialized survey line is drawn starting from the Southern center $I$, passing directly through the midpoint of the border between the Builders and the Craftsmen ($BC$). This survey line extends until it intersects the $KJ$ supply road at a specific checkpoint labeled $Y$.

Government records provide the following measurements:
- The radius of the Eastern Zone (Circle $K$) is exactly $5$ leagues.
- The radius of the Western Zone (Circle $J$) is exactly $8$ leagues.
- The distance from the Architect capital $A$ to the Grand Archive $G$ is $6$ leagues.

Based on these geographical constraints, what is the distance between the Eastern center $K$ and the checkpoint $Y$?

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
