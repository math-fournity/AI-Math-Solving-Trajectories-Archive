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

At a party, there are $n = 101$ couples. The $n$ husbands are seated at a round table, and the $n$ wives are seated at another round table. The king and queen (who are not part of the couples) shake hands with the guests in two different ways:

(i) The king shakes hands with the husbands one by one clockwise, starting from a man $M_1$. Simultaneously, each time the king shakes hands with a man, the queen moves clockwise around the wives' table to shake hands with that man's wife. Starting from the wife of $M_1$, once the king has shaken hands with every man and returns to $M_1$, the queen has completed $a$ full revolutions around the wives' table.

(ii) The queen shakes hands with the wives one by one clockwise, starting from a woman $W_1$. Simultaneously, each time the queen shakes hands with a woman, the king moves clockwise around the husbands' table to shake hands with that woman's husband. Starting from the husband of $W_1$, once the queen has shaken hands with every woman and returns to $W_1$, the king has completed $b$ full revolutions around the husbands' table.

Determine the maximum possible value of $|a-b|$.

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
