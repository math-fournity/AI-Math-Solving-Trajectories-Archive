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

A guard proposes the following game to the prisoners. All will be taken to the yard, where each of them will have a hat placed on their head in one of 5 possible colors. The guard will then line them up so that each prisoner can see all the hats except their own and will ask the first prisoner in line if they know the color of their hat. The prisoner answers "yes" or "no" aloud. If they answer "no", they will be immediately locked in solitary confinement. If they answer "yes", the guard will ask them what color their hat is, to which the prisoner must respond in such a way that the other prisoners do not hear the answer. If the answer is wrong, that prisoner will be immediately locked in solitary confinement in front of everyone, and if the answer is correct, that prisoner will be immediately released in front of everyone. The guard then approaches the next prisoner in line and repeats the same procedure, continuing until the last prisoner. The prisoners have the option to devise a strategy before the game begins, but once the game starts, no communication among the prisoners is allowed. If there are 2015 prisoners in the prison, what is the maximum number of prisoners that will be guaranteed to be released if the prisoners employ an optimal strategy?

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
