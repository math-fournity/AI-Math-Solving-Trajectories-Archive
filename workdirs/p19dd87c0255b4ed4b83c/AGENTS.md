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

In a remote sector of the galaxy, three space stations—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular navigation sector. Long-range sensors determine that the interior angle at station Bravo is exactly $130^\circ$.

To facilitate communication, two straight signal beams are projected from the other stations: one beam, $AA_1$, originates from Alpha and perfectly bisects the interior angle at $A$, terminating at point $A_1$ on the boundary $BC$. Similarly, a second beam, $CC_1$, originates from Charlie and bisects the interior angle at $C$, terminating at point $C_1$ on the boundary $AB$.

Two specialized relay satellites, Kilo ($K$) and Lima ($L$), are deployed along the straight-line trade route $AC$. Their positions are fixed based on coordinates relative to station Bravo: the angle formed between the path to Alpha and the path to Kilo ($\angle ABK$) is exactly $80^\circ$. Conversely, the angle formed between the path to Charlie and the path to Lima ($\angle CBL$) is also exactly $80^\circ$.

A technician is mapping the trajectories for two maintenance corridors: one connecting relay Kilo to signal terminal $A_1$, and another connecting relay Lima to signal terminal $C_1$. 

What is the measure of the angle (in degrees) formed at the intersection of the line segment $KA_1$ and the line segment $LC_1$?

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
