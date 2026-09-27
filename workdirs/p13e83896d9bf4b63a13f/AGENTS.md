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

A specialized architectural firm is designing a new four-sided central plaza, defined by four corner pillars named Alpha (A), Bravo (B), Charlie (C), and Delta (D) in a convex arrangement. To stabilize the structure, two straight support beams, AC and BD, are laid across the plaza, intersecting at a central hub located at point Echo (E).

The site surveyors have recorded the following precise angular measurements for the alignment of these beams relative to the outer perimeter:
- At pillar Alpha, the angle between the edge to Bravo and the beam to Charlie is exactly $50^\circ$.
- At pillar Alpha, the angle between the beam to Charlie and the edge to Delta is exactly $60^\circ$.
- At pillar Bravo, the angle between the edge to Charlie and the beam to Delta is exactly $30^\circ$.
- At pillar Delta, the angle between the beam to Charlie and the edge to Charlie is not measured directly; instead, the angle between the beam to Bravo and the edge to Charlie is recorded as $25^\circ$.

The head architect needs to calculate the specific angle of intersection between the two beams at the hub. Specifically, find the measure of the angle Alpha-Echo-Bravo ($\angle AEB$) in degrees.

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
