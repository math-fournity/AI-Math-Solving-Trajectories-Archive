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

In a remote research outpost, three identical observation towers—Tower Alpha, Tower Beta, and Tower Gamma—are positioned at the corners of a perfectly equilateral triangle. Each tower is exactly $n = 100$ levels high, and every level features a single large outward-facing data screen.

The first level of each tower is a restricted mechanical zone with no personnel. However, every level from the 2nd to the 100th is occupied by exactly one researcher. These researchers are tasked with monitoring the data screens of the neighboring towers according to strict line-of-sight protocols:
- A researcher stationed on level $k$ ($2 \le k \le 100$) can observe exactly four screens: the screens on level $k$ and level $k-1$ of the two towers they are not currently standing in.
- No researcher can see any screens located within their own tower, nor can they see any screens on levels other than $k$ and $k-1$.

The command center has decided to calibrate these $3n = 300$ screens by settting each one to one of three distinct light frequencies: Red, Green, or Blue. To ensure data diversity, the screens must be colored such that every single researcher in the outpost is able to see at least one screen of each of the three colors (Red, Green, and Blue) within their specific field of vision of four screens.

Find the total number of ways to color the 300 screens to satisfy this condition.

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
