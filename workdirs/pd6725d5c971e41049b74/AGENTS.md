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

In a remote industrial mining colony, the central computer allocates power modules based on the priority of worker pairings. There are four ranks of personnel: Elite Commanders ($A$), Senior Engineers ($B$), Technical Specialists ($C$), and General Laborers ($D$). Each rank is assigned a fixed positive integer power-draw value.

The colony’s protocol dictates that the total power consumption of a pair (the sum of their two individual values) must strictly determine their priority for housing. The administration has established a descending preference list for these pairings. To ensure the system functions correctly, the power sums of these pairs must follow this exact strictly decreasing order:

1. Two Elite Commanders ($A+A$)
2. One Elite Commander and one Senior Engineer ($A+B$)
3. One Elite Commander and one Technical Specialist ($A+C$)
4. Two Senior Engineers ($B+B$)
5. One Senior Engineer and one Technical Specialist ($B+C$)
6. One Elite Commander and one General Laborer ($A+D$)
7. Two Technical Specialists ($C+C$)
8. One Senior Engineer and one General Laborer ($B+D$)
9. One Technical Specialist and one General Laborer ($C+D$)
10. Two General Laborers ($D+D$)

The values $A, B, C$, and $D$ must be the smallest possible positive integers that satisfy this strict descending chain of inequalities (where $A+A > A+B > A+C > B+B > \dots > D+D$).

Find the unique set of least positive integers $(A, B, C, D)$ and calculate the system's identification code: $1000A + 100B + 10C + D$.

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
