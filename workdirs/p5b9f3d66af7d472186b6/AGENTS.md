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

A network security architect, Dima, is testing a server’s "Stability Score," which currently sits at $0$. He is playing a strategic simulation against an automated firewall system, Sasha. 

Sasha possesses $10$ unique data packets, each with a fixed power level corresponding to the powers of two: $1, 2, 4, 8, 16, 32, 64, 128, 256,$ and $512$. 

The simulation proceeds in rounds. In each round, the following sequence occurs:
1. Dima chooses an integer $p$, where $0 < p < 10$. Dima can choose a different value for $p$ in every round.
2. Sasha must then assign a "Positive" (+) status to exactly $p$ of the data packets and a "Negative" (–) status to the remaining $10 - p$ packets.
3. The values of all $10$ packets are summed according to their assigned signs, and this total is added to the server’s Stability Score.

Dima’s goal is to manipulate the rounds so that the server’s Stability Score deviates as far from zero as possible. Sasha’s goal is to make choices that keep the score as close to zero as possible. 

Find the greatest absolute value of the Stability Score that Dima can guaranteed-achieve after a finite number of rounds, regardless of how Sasha assigns the signs to the packets in each round.

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
