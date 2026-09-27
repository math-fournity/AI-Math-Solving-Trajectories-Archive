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

In a remote desert territory, a surveyor is mapping a four-sided plot of land defined by four landmarks: the Airbase ($A$), the Barracks ($B$), the Communications Hub ($C$), and the Depot ($D$). The boundary lines connecting these points form a convex shape. 

The surveyor notices a unique symmetry in the terrain: the angle of the slope measured at the Airbase ($ \angle BAD $) is exactly equal to the angle measured at the Communications Hub ($ \angle BCD $). To improve logistics, a straight supply road is paved starting from the Barracks ($B$), which perfectly bisects the angle formed by the paths to the Airbase and the Communications Hub ($ \angle ABC $). This road runs straight until it hits the exact midpoint of the perimeter fence connecting the Communications Hub and the Depot ($CD$).

Drone measurements reveal that the length of the fence between the Communications Hub and the Depot ($CD$) is exactly three times as long as the fence between the Airbase and the Depot ($AD$). 

Find the ratio of the distance between the Airbase and the Barracks ($AB$) to the distance between the Barracks and the Communications Hub ($BC$).

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
