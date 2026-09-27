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

In the high-stakes world of offshore oil drilling, two rival companies, Zenith and Nadir, are competing for drilling rights in a newly discovered sector divided into five plots. Geologists have determined that the five plots contain varying deposits of oil, valued at 1, 2, 3, 4, and 5 billion barrels respectively.

The five value markers are shuffled and placed in a hidden stack. The top marker is removed and placed face-up on a control board, visible to both companies. Zenith (the first player) and Nadir (the second player) take turns claiming plots until all five markers have been distributed. 

On a company's turn, they must choose one of two logistics actions:
1. **Direct Acquisition:** Take the current hidden marker from the top of the stack into their portfolio, revealing its value to the opponent.
2. **Strategic Swap:** Take the visible face-up marker into their portfolio and replace it with the marker currently at the top of the hidden stack (making this new marker the face-up option for the next turn).

The company that acquires a set of plots with the highest total value wins the drilling rights. Assuming both Zenith and Nadir employ perfect mathematical strategies to maximize their total value and win, what is the probability that Nadir (the second player) wins?

If the probability is expressed as an irreducible fraction $\frac{a}{b}$, calculate $a + b$.

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
