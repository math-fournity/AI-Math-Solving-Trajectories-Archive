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

In a remote territory, three specialized survey stations are positioned at locations $A$, $B$, and $C$. To monitor the land between them, three observation outposts—Alpha ($R$), Beta ($P$), and Gamma ($Q$)—have been constructed according to strict geometric protocols:

1. **Outpost Alpha ($R$)** is located such that its distances to stations $A$ and $B$ are equal ($RA = RB$), and the sightlines from Alpha to these two stations form a perfect $90^\circ$ angle ($\angle ARB = 90^\circ$).
2. **Outpost Beta ($P$)** is located such that its distances to stations $B$ and $C$ are equal ($PB = PC$), and the sightlines from Beta to these two stations form a perfect $90^\circ$ angle ($\angle BPC = 90^\circ$).
3. **Outpost Gamma ($Q$)** is located such that its distances to stations $C$ and $A$ are equal ($QC = QA$), and the sightlines from Gamma to these two stations form a perfect $90^\circ$ angle ($\angle CQA = 90^\circ$).

A logistics team measuring the straight-line distances between outposts and the primary stations recorded the following data:
- The distance from Outpost Beta ($P$) to Station $A$ is exactly 15 kilometers ($PA = 15$).
- The distance from Outpost Gamma ($Q$) to Station $B$ is exactly 14 kilometers ($QB = 14$).
- The distance from Outpost Alpha ($R$) to Station $C$ is exactly 13 kilometers ($RC = 13$).

The territory is defined by the hexagonal perimeter formed by traveling between the points in the order $R \rightarrow B \rightarrow P \rightarrow C \rightarrow Q \rightarrow A$ and back to $R$. Calculate the total area of the hexagon $RBPCQA$ in square kilometers.

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
