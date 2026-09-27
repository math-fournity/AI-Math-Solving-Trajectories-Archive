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

In a remote territory, an engineering team is mapping five strategic outposts: Alpha ($A$), Bravo ($B$), Charlie ($C$), Delta ($D$), and Echo ($E$). To establish a secure communication perimeter, they have recorded the following spatial data:

(a) The surveillance angle between outposts Bravo, Alpha, and Delta ($\angle BAD$) is exactly $45^\circ$. Within this sector, the team noted that the sum of the transmission angle from Bravo to Charlie to Delta ($\angle CBD$) and the angle from Delta to Alpha to Echo ($\angle DAE$) also totals $45^\circ$. Furthermore, the sum of the external boundary angles at Charlie ($\angle BCD$) and Echo ($\angle DEA$) measures $300^\circ$.

(b) The distance ratio between the Alpha-Bravo line and the Alpha-Delta line ($BA/DA$) is exactly $2\sqrt{2}/3$. Direct laser measurements confirm that the distance from Charlie to Delta is $7\sqrt{5}/3$ units, while the distance from Delta to Echo is $15\sqrt{2}/4$ units.

(c) A specialized signal resonance formula for this configuration must be satisfied: the square of the distance between Alpha and Delta, multiplied by the distance between Bravo and Charlie, is equal to the product of the distances of Alpha-Bravo, Alpha-Echo, and Bravo-Delta ($AD^2 \cdot BC = AB \cdot AE \cdot BD$).

Calculate the exact distance between outposts Bravo and Delta ($BD$).

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
