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

In a remote circular sanctuary with a radius of exactly 1 kilometer, five monitoring stations—named Alpha, Bravo, Charlie, Delta, and Echo—are positioned along the perimeter in that specific clockwise order. 

The sanctuary's surveillance grid is defined by laser beams connecting these stations. The layout is precisely calibrated such that the angle formed at Bravo by the beams from Echo and Delta is $30^\circ$. Similarly, the angle at Charlie formed by Alpha and Echo is $30^\circ$, the angle at Delta formed by Bravo and Alpha is $30^\circ$, and the angle at Echo formed by Charlie and Bravo is $30^\circ$.

The paths of these lasers intersect at five specific relay hubs within the sanctuary:
- Hub 1 is located where the laser from Bravo to Delta crosses the laser from Charlie to Echo.
- Hub 2 is located where the laser from Charlie to Echo crosses the laser from Delta to Alpha.
- Hub 3 is located where the laser from Delta to Alpha crosses the laser from Echo to Bravo.
- Hub 4 is located where the laser from Echo to Bravo crosses the laser from Alpha to Charlie.
- Hub 5 is located where the laser from Alpha to Charlie crosses the laser from Bravo to Delta.

A maintenance crew needs to clear the brush within the central pentagonal zone formed by these five relay hubs (Hub 1, Hub 2, Hub 3, Hub 4, and Hub 5). What is the total area of this pentagonal region in square kilometers?

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
