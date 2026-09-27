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

A high-tech research consortium consists of 12 independent laboratories. To foster innovation, the consortium organizers have mandated a "Collaborative Exchange" program where every laboratory must complete exactly one joint project with every other laboratory in the group. 

Upon the completion of a project, a panel of experts evaluates the results and awards "Innovation Credits" based on the following criteria:
*   If one laboratory’s contribution is judged significantly superior, that laboratory is awarded 3 credits and the other receives 0 credits.
*   If the project is judged to be a balanced collaboration where neither laboratory outperformed the other, both laboratories are awarded 1 credit each.

At the end of the program, a "Premier Innovator" status is granted to any laboratory that ranks among the top tier of performers. To maintain the prestige of this status, the organizers want to ensure that it is mathematically impossible for more than 6 laboratories to qualify for it. 

What is the minimum number of Innovation Credits a specific laboratory must earn to guaranteed that no more than 6 laboratories (including itself) have a total credit count equal to or greater than its own?

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
