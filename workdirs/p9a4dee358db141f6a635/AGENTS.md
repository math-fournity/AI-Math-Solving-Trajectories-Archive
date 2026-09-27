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

In a specialized urban planning district, four survey markers—named Alpha ($A$), Bravo ($B$), Charlie ($C$), and Delta ($D$)—define the boundaries of a quadrilateral plot. A highway contractor is analyzing the layout based on the following measurements:

The road connecting marker Bravo to Alpha meets the road to Charlie at an angle of exactly $60^\circ$ ($\angle ABC = 60^\circ$). The corners at Alpha and Charlie are perfectly squared, meaning the path from Alpha to Bravo is perpendicular to the path from Alpha to Delta ($\angle BAD = 90^\circ$), and the path from Charlie to Bravo is perpendicular to the path from Charlie to Delta ($\angle BCD = 90^\circ$).

Precise measurements show that the distance between Alpha and Bravo is 2 kilometers ($AB = 2$), while the distance between Charlie and Delta is exactly 1 kilometer ($CD = 1$). 

Two underground utility lines are laid in straight lines: one connecting Alpha to Charlie ($AC$) and the other connecting Bravo to Delta ($BD$). These two lines intersect at a central junction point, $O$.

The planning committee needs to calculate the sine of the angle formed at the junction between the Alpha and Bravo lines ($\sin \angle AOB$). What is the value of $\sin \angle AOB$?

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
