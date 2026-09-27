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

In the Kingdom of Isoscelia, a vast triangular territory is defined by three watchtowers: Alpha ($A$), Beta ($B$), and Gamma ($C$). The distance between the Alpha and Beta towers forms the base of the kingdom. The surveyor's records indicate that the internal angle at tower Gamma is exactly $36^\circ$, while the internal angles at Alpha and Beta are perfectly equal.

A series of five straight communication cables are laid out sequentially within the territory:
1. The first cable starts at tower Alpha and ends at a relay station $D$ located on the straight road between Beta and Gamma. This cable bisects the kingdom's angle at tower Alpha.
2. The second cable runs from tower Beta to a point $E$ on the first cable ($AD$), bisecting the kingdom's angle at tower Beta.
3. The third cable starts at relay station $D$ and connects to a point $F$ on the second cable ($BE$), bisecting the angle formed at $D$ by the road $DC$ and the first cable $DA$.
4. The fourth cable starts at point $E$ and connects to a point $G$ on the third cable ($DF$), bisecting the angle formed at $E$ by the first cable $ED$ and the second cable $EB$.
5. The final cable starts at point $F$ and connects to a point $H$ on the fourth cable ($EG$), bisecting the angle formed at $F$ by the second cable $FE$ and the third cable $FD$.

The length of this final cable, $FH$, is measured to be exactly $1$ league. Based on this layout, calculate the total distance between tower Alpha and tower Gamma (the length of side $AC$).

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
