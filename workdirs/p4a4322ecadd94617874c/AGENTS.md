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

In a bustling software development firm, a project manager is overseeing a marathon coding session that is scheduled to last exactly $L$ hours. To ensure the project remains on track, the manager decides to schedule $n$ brief check-in meetings. These meetings are represented as instantaneous timestamps marked at random points throughout the duration of the $L$-hour session.

The $n$ timestamps naturally divide the total $L$ hours of work into $n+1$ distinct work intervals: the time from the start of the session to the first meeting, the time between each consecutive meeting, and the time from the final meeting to the end of the session.

The manager is interested in the "rhythm" of the team. For the workflow to be considered perfectly balanced, no single work interval can exceed a duration of $\frac{L}{n}$ hours. 

Assuming each of the $n$ timestamps is chosen independently and uniformly at random from the interval $[0, L]$, what is the probability that every one of the $n+1$ work intervals has a length less than or equal to $\frac{L}{n}$?

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
