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

In a futuristic circular space station, a primary maintenance corridor is represented by the diameter line $AB$. A central power hub is located at point $C$ on this corridor, positioned such that the distance from docking bay $A$ to the hub is exactly half the distance from the hub to docking bay $B$ (satisfying the structural constraint $2 \cdot AC = BC$).

Two specialized sensor drones, $D$ and $E$, are positioned on the station's outer circular hull. Drone $D$ is deployed along a line passing through the power hub $C$ that runs perfectly perpendicular to the main corridor $AB$. Drone $E$ is positioned such that the straight-line path between drone $D$ and drone $E$ passes directly through the exact geometric center of the space station, forming a second diameter.

Engineers are calculating the energy signatures of two specific triangular zones. The first is the triangular region formed by the power hub and the two drones, $\triangle{DCE}$. The second is the triangular region formed by the two docking bays and drone $D$, $\triangle{ABD}$. 

What is the ratio of the area of the drone-hub triangle ($\triangle{DCE}$) to the area of the docking bay triangle ($\triangle{ABD}$)?

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
