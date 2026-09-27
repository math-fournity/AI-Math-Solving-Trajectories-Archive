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

In a sprawling logistics hub, a central control tower is located at point $A$. Two primary supply arteries extend from this tower: the Northern Route ($AB$) with a length of 18 units, and the Western Route ($AC$) with a length of 36 units.

A circular security perimeter, denoted as circle $\omega$ with its command center at point $O$, is established to monitor the area. This perimeter passes exactly through the endpoints of the routes, $B$ and $C$. Along the way, the perimeter boundary crosses the Northern Route again at checkpoint $B'$ and the Western Route again at checkpoint $C'$.

To enhance communication, two localized signal zones are created. The first zone is a circular field with diameter $BB'$, and the second is a circular field with diameter $CC'$. These two signal zones are perfectly synchronized such that they are externally tangent to each other at a specific relay station, $T$.

Sensors indicate that the direct distance from the control tower $A$ to the relay station $T$ is exactly 12 units.

Calculate the distance from the control tower $A$ to the command center $O$. If the resulting distance is an irreducible fraction $\frac{a}{b}$, provide the final value as $a + b$.

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
