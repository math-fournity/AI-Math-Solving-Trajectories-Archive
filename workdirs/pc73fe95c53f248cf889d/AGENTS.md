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

In a remote desert, four survey markers—$A$, $B$, $C$, and $D$—are positioned along a perfect circular perimeter centered at a central observation tower $O$. A straight access road extends from the tower through marker $B$ until it intersects a straight boundary wall containing markers $D$ and $C$ at an outpost $E$ (the markers appear in order $D, C, E$ along the wall). Simultaneously, a second straight access road extends from the tower through marker $C$ until it intersects a straight fence containing markers $A$ and $B$ at a supply depot $F$ (the markers appear in order $A, B, F$ along the fence).

A mapping drone calculates the following terrestrial measurements:
- The distance from marker $A$ to outpost $E$ is 4 kilometers.
- The distance from outpost $E$ to marker $C$ is 4 kilometers.
- The distance from marker $C$ to supply depot $F$ is 4 kilometers.

The drone also identifies a specific geometric property: a circular monitoring zone passing through the tower $O$, marker $D$, and outpost $E$ exactly bisects the straight-line path connecting marker $B$ and supply depot $F$.

The surveyor needs to calculate the land area of the triangular region defined by markers $A$ and $D$ and the supply depot $F$. Find the area of triangle $ADF$.

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
