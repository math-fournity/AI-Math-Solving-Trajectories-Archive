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

A specialized architectural firm is designing a triangular park defined by three landmark pillars: A, B, and C. The distances between these pillars are recorded as $AB = 6$ units, $BC = 5$ units, and $AC = 7$ units. The firm intends to build a circular jogging track that passes perfectly through pillars A, B, and C.

Two straight glass walkways are constructed, starting from pillars B and C, such that each walkway is perfectly tangent to the circular track. These two walkways meet at a control hub located at point X. 

A decorative light is positioned at point Z on the circular track. To facilitate maintenance, a straight service cable is stretched from pillar C to the light at Z. A technician at hub X projects a laser beam toward this cable, hitting it at point Y such that the beam XY is perpendicular to the cable CZ. Point Y lies strictly between C and Z. Sensors indicate that the distance from the laser hit point to the light, $YZ$, is exactly three times the distance from the pillar to the hit point, $CY$.

A secondary circular sensor zone is established that passes through pillar B, pillar C, and the laser hit point Y. This sensor zone boundary intersects the straight line path extending through pillars A and B at a specific marker designated as point K. 

Determine the length of the segment $AK$. If the result is an irreducible fraction $\frac{a}{b}$, calculate the value $a+b$.

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
