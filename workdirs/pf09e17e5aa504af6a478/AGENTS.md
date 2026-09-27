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

In a futuristic energy grid, three power nodes—Alpha ($a$), Beta ($b$), and Gamma ($c$)—each maintain a power level of at least 2 units. These levels define a stability equation $ax^2 + bx + c = 0$. Two engineers, Adam and Boris, take turns modifying the grid to achieve specific stability states. The grid is considered "unstable" if the equation has two distinct real roots. The first engineer to create an unstable state wins the game.

Adam always takes the first turn. 
- On Adam's turn, he must select one node and change its power level to the sum of the power levels of the other two nodes.
- On Boris's turn, he must select one node and change its power level to the product of the power levels of the other two nodes.

We define the function $S(a, b, c)$ to determine the outcome of the game based on the initial power levels:
- $S(a, b, c) = 1$ if Adam has a guaranteed winning strategy.
- $S(a, b, c) = 2$ if Boris has a guaranteed winning strategy.
- $S(a, b, c) = 0$ if neither player can force a win (the game continues indefinitely).

Calculate the total value of the following sum:
$S(3, 4, 3) + S(2, 2, 2) + S(4, 3, 5) + S(2, 6, 2)$

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
