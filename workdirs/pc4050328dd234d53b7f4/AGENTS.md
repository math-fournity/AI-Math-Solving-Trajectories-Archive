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

An elite team of deep-sea archaeologists has located several artifacts scattered on the seabed, which they believe mark the boundaries of a perfectly cubic ancient vault buried beneath the sand. To reconstruct the exact position and orientation of this cube, the researchers have mapped seven specific sonar pings to the planes containing the vault's six square faces:

1. Two distinct sonar pings, $A_1$ and $A_2$, originated from the flat plane containing the "floor" of the vault.
2. Two distinct sonar pings, $F_1$ and $F_2$, originated from the flat plane containing the "ceiling" of the vault. It is confirmed that these four points ($A_1, A_2, F_1, F_2$) are non-coplanar.
3. One sonar ping, $E$, originated from the plane containing the "front" wall.
4. One sonar ping, $H$, originated from the plane containing the "back" wall (the face parallel to the front wall).
5. One sonar ping, $J$, originated from the plane containing the "right-side" wall.

Note that the labels "floor," "ceiling," "front," "back," and "right-side" are used solely to identify which pairs of planes are parallel and which are perpendicular; the vault's orientation in the water is unknown. 

Based on the coordinates of these seven specific points, what is the maximum number of distinct cubes that could satisfy these spatial constraints?

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
